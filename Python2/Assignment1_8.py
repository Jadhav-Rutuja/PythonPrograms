# 8.Write a program which accept number from user and print that number of "*" on screen.

def Display(Number):
   for i in range(0,Number,1):
       print("*",end = " ")

def main():
    print("Enter the number :")
    No = int(input())

    Display(No)

if __name__=="__main__":
    main()