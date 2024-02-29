# 1. Design automation script which accept directory name and display checksum of all files.
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

def DisplayChecksum(path,Dir_Name):
    listprocess = []

    if not os.path.exists(Dir_Name):
        try:
            os.mkdir(Dir_Name)
        except:
            pass

    seperator = "-" * 80
    log_path = os.path.join(Dir_Name, "MarvellousLog%s.log" % time.time())
    f = open(log_path, 'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger :" + str(time.ctime()) + "\n")
    f.write(seperator + "\n")

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                listprocess.append(filen)
                listprocess.append(file_hash)
        for element in listprocess:
            f.write("%s\n\n" % element)

    else:
        print("Invalid Path")

def main():
    print("----Checksum Application----")
    print("Application Name:" + argv[0])
    if(len(argv)!=3):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This Script is used to traverse specific directory and find checksum of files")
        exit()

    if (argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : Application_name Path_os_directory Dir_Name")
        exit()

    DisplayChecksum(argv[1],argv[2])

if __name__ == "__main__":
    main()