# 5. Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen.
# After execution of thread1 gets completed then schedule thread2.

import threading

def DisplaySerial(No):
    for i in range(1,No+1,1):
        print(i)

def DisplayReverse(No):
    for i in range(No,0,-1):
        print(i)

def main():
    Number = 50

    Thread1 = threading.Thread(target = DisplaySerial, args = (Number,))
    Thread2 = threading.Thread(target = DisplayReverse, args = (Number,))

    print("Numbers from 1 to 50 :")
    Thread1.start()
    Thread1.join()

    print("Numbers from 50 to 1 :")
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()