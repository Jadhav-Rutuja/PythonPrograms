# 1. Write a recursive program which display below pattern.
# Input :    5
# Output :   *  *  *  *  *

def Display(No):
    if(No>0):
        print("*",end=" ")
        Display(No-1)

def main():
    print("Enter the number :")
    Number = int(input())

    Display(Number)

if __name__ == "__main__":
    main()
