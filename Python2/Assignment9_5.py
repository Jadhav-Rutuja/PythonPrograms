# 5. Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt    Marvellous
# Search "Marvellous" in Demo.txt

import os
from sys import *

def StringFreq(Filename, Str):
    fd = open(Filename, "r")

    Data = fd.read()

    Frequency = Data.count(Str)

    return Frequency

def main():
    print("Enter the file name:")
    Name = input()

    print("Enter the string")
    str = input()

    Ret = StringFreq(Name, str)
    print("The frequency of string is:", Ret)

if __name__ == "__main__":
    main()