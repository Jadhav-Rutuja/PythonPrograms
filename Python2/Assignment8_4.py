# 4. Write a recursive program which accept number from user and return summation of its digits.
# Input :  879
# Output :  24

def Summation(No):
    if(No == 0):
        return 0
    else:
        return(No % 10 + Summation(int(No/10)))

def main():
    print("Enter the number :")
    Number = int(input())

    Ret = Summation(Number)
    print("Summation of digits is :",Ret)

if __name__ == "__main__":
    main()
