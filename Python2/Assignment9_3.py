# 3. Write a program which accept file name from user and create new new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line arguments.
# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

import os
from shutil import *
from sys import *

def CopyFile(FileName):
        fd = open('Demo.txt',"a")
        print("File is created successfully")

        copy(FileName,'Demo.txt')
        print("The contents of file is copied successfully in Demo.txt ")

def main():
    if(len(argv)!=2):
        print("Invalid number of arguments ")
        exit()

    CopyFile(argv[1])

if __name__ == "__main__":
    main()