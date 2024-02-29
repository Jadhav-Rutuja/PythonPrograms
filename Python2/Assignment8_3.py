# 3. Write a recursive program which display below pattern.
# Input :    5
# Output :   5  4  3  2  1

def Display(No):
    if(No>=1):
        print(No,end = " ")
        Display(No-1)

def main():
    print("Enter the number :")
    Number = int(input())

    Display(Number)

if __name__ == "__main__":
    main()
