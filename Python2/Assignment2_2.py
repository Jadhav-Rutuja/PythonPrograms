# 2.Write a program which accept one nnumber and display below pattern.

#input : 5
#Output :
#  *  *  *  *  *
#  *  *  *  *  *
#  *  *  *  *  *
#  *  *  *  *  *
#  *  *  *  *  *

def DisplayPattern(value):
    for i in range(0,value,1):
        for j in range(0,value,1):
            print("*",end=" ")
        print()

def main():
    print("Enter the number : ")
    No = int(input())

    DisplayPattern(No)

if __name__ == "__main__":
    main()