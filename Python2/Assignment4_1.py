# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.

PowerTwo = lambda A : A**2

def main():
   print("Enter the number :")
   No = int(input())

   Ans = PowerTwo(No)

   print(Ans)

if __name__ == "__main__":
   main()