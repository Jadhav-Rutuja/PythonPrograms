# 5. Write a program which accept one number from user and check whether number is prime or not.

def ChkPrime(Value):
    if Value>1:
      for i in range(2,Value,1):
            if((Value%i)==0):
                return False

def main():
    print("Enter the number : ")
    No = int(input())

    Ret = ChkPrime(No)

    if(Ret == False):
        print("Number is not prime")
    else:
        print("Number is Prime")
        
if __name__ == "__main__":
    main()
