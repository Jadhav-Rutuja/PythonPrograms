# 2. Write a program which accept N number from user and store it into List.
# Return Maximum number from that List.

def MaxNumbers(Arr,Value):
    Max = 0

    for i in range(0,Value,1):
        if(Max<Arr[i]):
            Max = Arr[i]
    return Max

def main():
    print("Enter number of elements : ")
    No = int(input())

    NList = []

    print("Enter the elements :")

    for i in range(0, No, 1):
        Elements = int(input())
        NList.append(Elements)

    Ret = MaxNumbers(NList,No)

    print("Maximum number in the List :",Ret)

if __name__ == "__main__":
    main()
