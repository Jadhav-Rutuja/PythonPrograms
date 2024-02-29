# 1. Design python application which creates two thread named as even and odd. Even thread will display
# first 10 even nummbers and odd thread will display first 10 odd numbers.

import threading

def DisplayEven(No):
    for i in range(1,No+1,1):
        if((i % 2)==0):
            print("Even numbers :",i)

def DisplayOdd(No):
    for i in range(1,No+1,1):
        if((i % 2)!=0):
            print("Odd numbers :",i)

def main():
    Number = 20

    Even = threading.Thread(target = DisplayEven, args = (Number,))
    Odd = threading.Thread(target = DisplayOdd, args = (Number,))

    Even.start()
    Even.join()

    Odd.start()
    Odd.join()

if __name__ == "__main__":
    main()