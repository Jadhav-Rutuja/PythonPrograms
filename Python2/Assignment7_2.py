# 2. Design python application which creates two threads as evenfactor and oddfatcor. Both the thread
# accept one parametef as integer. Evenfactor thread will display addition of even factors of given number
# and oddfactor will display addition of odd factors of given number. After execution of both the thread
# gets completed main thread should display message as "exit from main".

import threading

def DisplayEvenFactors(No):
    Sum = 0
    for i in range(2,No,1):
        if((No % i)==0):
            Sum = Sum + i
    print("Addition of even factor numbers is :",Sum)

def DisplayOddFactors(No):
    Sum = 0
    for i in range(1,No,1):
        if((No % i)!=0):
            Sum = Sum + i
    print("Addition of odd factor numbers is :",Sum)

def main():
    Integer = int(input("Enter the number :"))

    Evenfactor = threading.Thread(target = DisplayEvenFactors, args = (Integer,))
    Oddfactor = threading.Thread(target = DisplayOddFactors, args = (Integer,))

    Evenfactor.start()
    Oddfactor.start()

    Evenfactor.join()
    Oddfactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()