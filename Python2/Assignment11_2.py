# 2. Design automation script which accept directory name and write names of duplicates files from
# files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
#     Usage : DirectoryDuplicate.py "Demo"
# Demo is name of directory.

from sys import *
import os
import hashlib
import time

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return  hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    listprocess = []

    seperator = "-" * 80
    log_path = os.path.join(path, "MarvellousLog%s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger :" + str(time.ctime()) + "\n")
    f.write(seperator + "\n")

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

            results = list(filter(lambda x: len(x) > 1, dups.values()))

        if len(results) > 0:
            print("Duplicates Found")

            print("The following files are identical.")

            icnt = 0;
            for result in results:
                for subresult in result:
                    icnt += 1
                    if icnt >= 2:
                        listprocess.append(subresult)
            for element in listprocess:
                f.write("%s\n\n" % element)
        else:
            print("No duplicate files found.")
    else:
        print("Invalid Path")

def main():
    print("Application Name:" + argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This Script is used to traverse specific directory and find duplicates files")
        exit()

    if (argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : Application_name Path_os_directory")
        exit()

    FindDuplicate(argv[1])

if __name__ == "__main__":
    main()