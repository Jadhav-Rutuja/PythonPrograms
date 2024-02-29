# 5. Write a program which accept N number from user and store it into List. Return addition of all
# prime numbers from that list.Main python file accepts  N numbers from user and pass each number
# to ChkPrime() function which is part of our user defined module named as MarvellousNum.
# Name of the function from main python file should be ListPrime() .
import MarvellousNum

def main():
    print("Enter number of elements : ")
    No = int(input())

    NList = []

    print("Enter the elements :")

    for i in range(0, No, 1):
        Elements = int(input())
        NList.append(Elements)

    Ret = MarvellousNum.ChkPrime(NList,No)

    print("Addition of prime numbers are :", Ret)

if __name__ == "__main__":
    main()
