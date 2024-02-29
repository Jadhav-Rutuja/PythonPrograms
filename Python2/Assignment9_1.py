# 1. Write a program which accepts file name from user and check whether that file exists in current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.

import os

def CheckFile(FileName):
    if(os.path.exists(FileName)):
        print("File is existing")
        return
    else:
        print("File is not existing")

def main():
    print("Enter the file name to check that file is exist or not : ")
    Name = input()

    CheckFile(Name)

if __name__ == "__main__":
    main()