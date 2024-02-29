# 9. Write a program which accept number from user and return number of digits in that number.

def CountDigit(Value):
      Cnt = 0
      while(Value!=0):
          Cnt = Cnt + 1
          Value = Value//10
      return Cnt

def main():
    print("Enter the number : ")
    No = int(input())

    Ret = CountDigit(No)

    print("Numbers of digits in the number :",Ret)

if __name__ == "__main__":
    main()
