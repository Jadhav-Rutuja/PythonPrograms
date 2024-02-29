# 3. Design python appplication which creates two threads as evenlist and oddlist. Both the threads
# accept list of integers as parameter. Evenlist thread add all even elements from input list and
# display the addition. Oddlist thread add all odd elements from input list and display the addition.

import threading

def AddEven(No):
    Sum = 0
    for i in range(1,No+1,1):
        if((i % 2)==0):
            Sum = Sum + i
    print("Addition of even numbers is :",Sum)

def AddOdd(No):
    Sum = 0
    for i in range(1,No+1,1):
        if((i % 2)!=0):
            Sum = Sum + i
    print("Addition of odd numbers is :",Sum)

def main():
    Number = int(input("Enter the number :"))

    Evenlist = threading.Thread(target = AddEven, args = (Number,))
    Oddlist = threading.Thread(target = AddOdd, args = (Number,))

    Evenlist.start()
    Oddlist.start()

    Evenlist.join()
    Oddlist.join()

if __name__ == "__main__":
    main()