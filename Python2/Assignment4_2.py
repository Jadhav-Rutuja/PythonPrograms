# 2. Write a program which contains one lambda function which accepts two parameter and return its multiplication.

Multiplication = lambda A,B : A*B

def main():
   print("Enter the first number :")
   No1 = int(input())

   print("Enter the first number :")
   No2 = int(input())

   Ans = Multiplication(No1,No2)

   print("Multiplication is :",Ans)

if __name__ == "__main__":
   main()