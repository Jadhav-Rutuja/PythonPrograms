# 4. Write a program which accept one number from user and return addition of its factors.

def AddFact(Value):
    Factors = 0
    for i in range(1,Value,1):
        if((Value % i)==0):
            Factors = Factors + i
    return Factors

def main():
    print("Enter the number : ")
    No = int(input())

    Ret = AddFact(No)

    print("Addition of factors is : ",Ret)
    
if __name__ == "__main__":
    main()