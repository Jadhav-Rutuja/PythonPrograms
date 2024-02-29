# 9.Write a program which display first even numbers on screen.

def main():
    for i in range(1,21,1):
        if((i % 2)==0):
            print(i)

if __name__=="__main__":
    main()