# 3.Write a program which contains one function named as Add() which accepts two numbers from user
# and return addition of that two numbers.

def Add(Number1,Number2):
    Ans = Number1 + Number2
    return Ans

def main():
    print("Enter the first number :")
    no1 = int(input())

    print("Enter the second number :")
    no2 = int(input())

    Ret = Add(no1,no2)

    print("Addition is : ",Ret)

if __name__=="__main__":
    main()