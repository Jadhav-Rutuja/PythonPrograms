# 1.Design automation script which accept directory name and file extension from user.
# Display all files with that extension.
#     Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search.

import os
import time
from sys import *

def DirectoryFileSearch(Dir_Name,extension):
    print("Inside directory method")
    print("Name of input directory :",Dir_Name)

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

    for foldername,subfolder,Filenames in os.walk(Dir_Name):
        print("Folder name is :"+foldername)

        for fnames in Filenames:
            File_extension = os.path.splitext(fnames)[-1].lower()
            if(File_extension == extension):
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
        print("This script will travel the directory and display the names of entries")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : Application_name Directory_Name Extension")
        exit()

    DirectoryFileSearch(argv[1],argv[2])

if(__name__ == "__main__"):
    main()