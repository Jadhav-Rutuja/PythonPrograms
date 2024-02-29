# 2. Write a recursive program which display below pattern.
# Input :    5
# Output :   1  2  3  4  5

def Display(No):
    if(No>=1):
        Display(No-1)
        print(No,end = " ")

def main():
    print("Enter the number :")
    Number = int(input())

    Display(Number)

if __name__ == "__main__":
    main()
