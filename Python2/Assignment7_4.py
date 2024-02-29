# 4. Design python application which creates three threads as small, capital, digits. All the threads
# accepts string as parameter. Small thread display number of small characters, capital thread display
# number of capital thread display number of capital characters and digits thread display number of digits.
# Display id and name of each thread.

import threading

def SmallCharacters(str):
    Count = 0
    for i in range(0,len(str),1):
        if(str[i].islower()):
            Count = Count + 1
    print("Number of small characters :",Count)

def CapitalCharacters(str):
    Count = 0
    for i in range(0,len(str),1):
        if (str[i].isupper()):
            Count = Count + 1
    print("Number of capital characters :", Count)

def NumberOfDigits(str):
    Count = 0
    for i in range(0,len(str),1):
        if(str[i].isdigit()):
            Count = Count + 1
    print("Number of digits :", Count)

def main():
    Str = []
    print("Enter the string :")
    Str = input()

    Small = threading.Thread(target = SmallCharacters, args = (Str,))
    Capital = threading.Thread(target = CapitalCharacters, args = (Str,))
    Digits = threading.Thread(target = NumberOfDigits, args = (Str,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()