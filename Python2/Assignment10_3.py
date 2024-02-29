# 3.Design automation script which accept two directory names. Copy all files from first directory
# into second directory.Second directory should be created at run time.
#     Usage : DirectoryFileSearch.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory
# as Temp and copy all files from Demo to Temp.

import os
import time
import shutil
from sys import *

def DirectoryRename(Dir_Name1,Dir_Name2):
    print("Inside directory method")
    print("Name of input directory :",Dir_Name1)

    os.mkdir(Dir_Name2)

    for foldername,subfolder,Filenames in os.walk(Dir_Name1):
        print("Folder name is :"+foldername)

        for fnames in Filenames:
            shutil.copy(os.path.join(Dir_Name1,fnames),Dir_Name2)
    print(" ")
    print("Files in directory "+Dir_Name1+" are copies into directory "+Dir_Name2)

    listprocess = []

    seperator = "-" * 80
    log_path = os.path.join(Dir_Name1, "MarvellousLog%s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger :" + str(time.ctime()) + "\n")
    f.write(seperator + "\n")

    for foldername, subfolder, Filenames in os.walk(Dir_Name2):
        print("Folder name is :" + foldername)

        for fnames in Filenames:
            listprocess.append(fnames)

        for element in listprocess:
            f.write("%s\n" % element)

        print(" ")

def main():
    print("Directory application")

    if(len(argv)!=3):
        print("Insuficient arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This script will travel the directory and copy files in another directory")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : Application_name Directory_Name1 Directory_Name2")
        exit()

    DirectoryRename(argv[1],argv[2])

if(__name__ == "__main__"):
    main() 