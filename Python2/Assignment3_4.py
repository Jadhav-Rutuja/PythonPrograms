# 4. Write a program which accept N number from user and store it into List.
# Accept one another number from user and return frequency of that number from List.

def Frequency(Arr,Value,No1):
    Freq = 0
    for i in range(0,Value,1):
        if(No1==Arr[i]):
            Freq = Freq + 1
    return Freq

def main():
    print("Enter number of elements : ")
    No = int(input())

    NList = []

    print("Enter the elements :")

    for i in range(0, No, 1):
        Elements = int(input())
        NList.append(Elements)

    print("Enter the number :")
    Number = int(input())

    Ret = Frequency(NList,No,Number)

    print("Frequency of number in the List :",Ret)

if __name__ == "__main__":
    main()
