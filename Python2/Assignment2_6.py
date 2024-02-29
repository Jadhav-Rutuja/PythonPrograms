# 6. Write a program which accept one number and display below pattern.
#input : 5
#Output :
#  *  *  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *

def DisplayPattern(Value):
      for i in range(Value,0,-1):
            for j in range(0,i,1):
                print("*",end=" ")
            print()

def main():
    print("Enter the number : ")
    No = int(input())

    DisplayPattern(No)

if __name__ == "__main__":
    main()
