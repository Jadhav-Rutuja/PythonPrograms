# 1. Write a program which accept N number from user and store it into List.
# Return addition of all elements from that List.

def AddNumbers(Arr,Value):
    Sum = 0

    for i in range(0,Value,1):
        Sum = Sum + Arr[i]
    return Sum

def main():
    print("Enter number of elements : ")
    No = int(input())

    NList = []

    print("Enter the elements :")

    for i in range(0, No, 1):
        Elements = int(input())
        NList.append(Elements)

    Ret = AddNumbers(NList,No)

    print("Addition of Elements in the List :",Ret)

if __name__ == "__main__":
    main()
