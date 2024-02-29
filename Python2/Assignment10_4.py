# 4.Design automation script which accept two directory names and one file extension. Copy all files
# with the specific extension from first directory into second directory.
# Second directory should be created at run time.
#     Usage : DirectoryFileSearch.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory
# as Temp and copy all files with extension .exe from Demo to Temp.

import os
import time
import shutil
from sys import *

def File_copy(Dir_Name1,Dir_Name2,extension):
    print("Inside directory method")
    print("Name of input directory :",Dir_Name1)

    os.mkdir(Dir_Name2)

    for foldername,subfolder,Filenames in os.walk(Dir_Name1):
        print("Folder name is :"+foldername)

        for fnames in Filenames:
            File_extension = os.path.splitext(fnames)
            if(File_extension[1]==extension):
                shutil.copy(os.path.join(Dir_Name1,fnames),Dir_Name2)
    print(" ")
    print("Files in directory "+Dir_Name1+" are copies into directory "+Dir_Name2+" of extension "+extension)

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

    if(len(argv)!=4):
        print("Insuficient arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This script will travel the directory and copy files with specific extension into another directory")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : Application_name Directory_Name1 Directory_Name2 Extension")
        exit()

    File_copy(argv[1],argv[2],argv[3])

if(__name__ == "__main__"):
    main() 