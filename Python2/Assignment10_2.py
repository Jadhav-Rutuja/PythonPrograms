# 2.Design automation script which accept directory name and two file extension from user.
# Rename all files with first file extension with the second file extension.
#     Usage : DirectoryFileSearch.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os
import time
from sys import *

def DirectoryRename(Dir_Name,extension1,extension2):
    print("Inside directory method")
    print("Name of input directory :",Dir_Name)

    listprocess = []

    if not os.path.exists(Dir_Name):
        try:
            os.mkdir(Dir_Name)
        except:
            pass

    seperator = "-" * 80
    log_path = os.path.join(Dir_Name, "MarvellousLog%s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger :" + str(time.ctime()) + "\n")
    f.write(seperator + "\n")

    for foldername,subfolder,Filenames in os.walk(Dir_Name):
        print("Folder name is :"+foldername)

        for fnames in Filenames:
            File_extension = os.path.splitext(fnames)
            if(File_extension[1] == extension1):
                listprocess.append(File_extension[0]+extension2)

        for element in listprocess:
            f.write("%s\n" % element)

        print(" ")

def main():
    print("Directory application")

    if(len(argv)!=4):
        print("Insuficient arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This script will travel the directory and change the file extension")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : Application_name Directory_Name Extension1 Extension2")
        exit()

    DirectoryRename(argv[1],argv[2],argv[3])

if(__name__ == "__main__"):
    main() 