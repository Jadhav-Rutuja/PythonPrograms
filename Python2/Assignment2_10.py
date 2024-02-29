# 10. Write a program which accept number from user and return addition of digits in that number.

def AdditionDigit(Value):
      Sum = 0
      while(Value!=0):
          Digit = int(Value % 10)
          Sum = Sum + Digit
          Value = Value/10
      return Sum

def main():
    print("Enter the number : ")
    No = int(input())

    Ret = AdditionDigit(No)

    print("Addition of digits in the number :",Ret)

if __name__ == "__main__":
    main()
