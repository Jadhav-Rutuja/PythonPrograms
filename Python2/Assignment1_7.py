# 7.Write a program which contains one function that accept one number from user
# and returns true if number is divisible by 5 otherwise return false.

def Division(Number):
    if((Number % 5) == 0):
        return True
    else:
        return False

def main():
    print("Enter the number :")
    No = int(input())

    Ret = Division(No)

    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__=="__main__":
    main()