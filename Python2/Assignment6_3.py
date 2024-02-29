# 3. Write a program which contains one class named as Numbers. Arithmetic class contains one instance
# variables as Value. Inside init method initialise that instance variables to the value which is accepted
# from user. There are four instance methods inside class as ChkPrime(), ChkPerfect(0, SumFactors(0, Factors().
# ChkPrime() method will returns true if number is prime otherwise return false. ChkPerfect() method will returns
# true if number is perfect otherwise return false.Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method as a helper method
# if required. After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self,A):
        self.Value = A

    def ChkPrime(self):
        i = 0
        Flag = True

        for i in range(2,int(self.Value / 2)+1):
            if(self.Value % i == 0):
                Flag = False
                break

        return Flag

    def ChkPerfect(self):
        Ans = self.SumFactors()

        if(self.Value == Ans):
            return True
        else:
            return False

    def Factors(self):
        for i in range(1,int(self.Value/2)+1):
            if(self.Value % i == 0 ):
                print(i,end=" ")

    def SumFactors(self):
        Sum = 0

        for i in range(1, int(self.Value / 2) + 1):
            if (self.Value % i == 0):
                Sum = Sum + i

        return Sum

def main():
    print("Enter the number :")
    No1 = int(input())

    Obj1 = Arithmetic(No1)

    Ret1 = Obj1.ChkPrime()
    if (Ret1 == True):
        print("{} is a prime number".format(No1))
    else:
        print("{} is not a prime number".format(No1))

    Ret1 = Obj1.ChkPerfect()
    if (Ret1 == True):
        print("{} is a perfect number".format(No1))
    else:
        print("{} is not a perfect number".format(No1))

    Obj1.Factors()
    print()

    Ret1 = Obj1.SumFactors()
    print("Summation is :", Ret1)

    print("Enter the number :")
    No2 = int(input())

    Obj2 = Arithmetic(No2)

    Ret2 = Obj2.ChkPrime()
    if (Ret2 == True):
        print("{} is a prime number".format(No2))
    else:
        print("{} is not a prime number".format(No2))

    Ret2 = Obj2.ChkPerfect()
    if (Ret2 == True):
        print("{} is a perfect number".format(No2))
    else:
        print("{} is not a perfect number".format(No2))

    Obj2.Factors()
    print()

    Ret2 = Obj2.SumFactors()
    print("Summation is :", Ret2)

if __name__ == "__main__":
    main()