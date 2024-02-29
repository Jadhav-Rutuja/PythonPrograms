# 6.Write a program which accept number from user and check whether that number is positive or negative or zero.

def ChkNum():
    if(No > 0):
        print("Positive Number")
    elif(No < 0):
        print("Negative Number")
    elif(No == 0):
        print("Zero")

def main():
    print("Enter the number :")
    Value = int(input())

    ChkNum(Value)

if __name__=="__main__":
    main()