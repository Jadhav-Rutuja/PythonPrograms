# 3. Write a program which accept N number from user and store it into List.
# Return Minimum number from that List.

def MinNumbers(Arr,Value):
    Min = Arr[0]
    for i in range(0,Value,1):
        if(Min>Arr[i]):
            Min = Arr[i]
    return Min

def main():
    print("Enter number of elements : ")
    No = int(input())

    NList = []

    print("Enter the elements :")

    for i in range(0, No, 1):
        Elements = int(input())
        NList.append(Elements)

    Ret = MinNumbers(NList,No)

    print("Maximum number in the List :",Ret)

if __name__ == "__main__":
    main()
