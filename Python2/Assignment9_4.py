# 4. Write a program which accept two file names from user and compare contents of both the files.
# If both the files contains same contents then display success otherwise display failure.
# Accept names of both the files from command line.
# Input : Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt

import os
from filecmp import *
from sys import *

def Compare_File(FileName1,FileName2):
        if(cmp(FileName1,FileName2)):
            print("Success")
        else:
            print("Failure")

def main():
    if (len(argv) != 3):
        print("Invalid number of arguments ")
        exit()

    Compare_File(argv[1],argv[2])

if __name__ == "__main__":
    main()