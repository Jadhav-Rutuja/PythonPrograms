# 3. Write a program which accept one number from user and return its factorial.

def Factorial(Value):
    Factors = 1
    for i in range(1,Value+1,1):
        Factors = Factors * i
    return Factors

def main():
    print("Enter the number : ")
    No = int(input())

    Ret = Factorial(No)

    print("The factorial of the number is : ",Ret)

if __name__ == "__main__":
    main()