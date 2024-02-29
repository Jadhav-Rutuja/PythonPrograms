# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
# Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation.
# Write on python program which call all the functiond=s from Arithmetic module by accepting the parameters from user.
import Arithmetic

def main():
    print("Enter the first number : ")
    Number1 = int(input())

    print("Enter the second number : ")
    Number2 = int(input())

    Ret1 = Arithmetic.Add(Number1 , Number2)
    Ret2 = Arithmetic.Sub(Number1 , Number2)
    Ret3 = Arithmetic.Mult(Number1 , Number2)
    Ret4 = Arithmetic.Div(Number1 , Number2)

    print("Addition is : ", Ret1)
    print("Subtraction is : ", Ret2)
    print("Multiplication is : ", Ret3)
    print("Division is : ", Ret4)

if __name__ == "__main__":
    main()