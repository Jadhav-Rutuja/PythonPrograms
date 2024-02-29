# 2. Write a program which accept file name from user and open that file and display the contents of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console.

import os

def DisplayContents(FileName):
    fd = open(FileName,"r")
    Data = fd.read()
    print("Contents from the file is :")
    print(Data)

    fd.close()

def main():
    print("Enter the file name to open : ")
    Name = input()

    DisplayContents(Name)

if __name__ == "__main__":
    main()