# 8. Write a program which accept one number and display below pattern.
#input : 5
#Output :
#  1
#  1  2
#  1  2  3
#  1  2  3  4  
#  1  2  3  4  5

def DisplayPattern(Value):
      for i in range(1,Value+1,1):
            for j in range(1,Value+1,1):
                print(j,end=" ")
            print()

def main():
    print("Enter the number : ")
    No = int(input())

    DisplayPattern(No)

if __name__ == "__main__":
    main()
