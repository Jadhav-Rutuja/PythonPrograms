# 5. Write a recursive program which accept number from user and return its factorial.
# Input :  5
# Output :  120

def Factorial(No):
    if(No <= 1):
        return 1
    else:
        return(No * Factorial(No - 1))

def main():
    print("Enter the number :")
    Number = int(input())

    Ret = Factorial(Number)
    print("Factorial of number is :",Ret)

if __name__ == "__main__":
    main()
