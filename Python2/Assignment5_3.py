# 3. Write a program which contains one class named as Arithmetic.Arithmetic class contains three instance variables as Value1,Value2.
# Inside init method initialise all instance variables to 0.There are three instance methods inside class as Accpet(), Addition(),
# Substraction(), Multiplication(), Division(). Accept method will accept value of value1 and Value2 from user. Addition() method will
# perform addition of Value1, Value2 and return result. Substraction() method will perform subtraction of Value1, Value2 and return result.
# Multiplication() method will perform multiplication of Value1, Value2 and return result. Division() method will perform division of Value1,
# Value2 and return result. After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the value of Value1 :")
        self.Value1 = int (input())

        print("Enter the value of Value2 :")
        self.Value2 = int(input())

    def Addition(self):

        Result = self.Value1 + self.Value2

        return Result

    def Substarction(self):

        Result = self.Value1 - self.Value2

        return Result

    def Multiplication(self):

        Result = self.Value1 * self.Value2

        return Result

    def Division(self):

        Result = self.Value1 / self.Value2

        return Result

def main():
    Obj1 = Arithmetic()

    Obj1.Accept()

    Ans = Obj1.Addition()
    print("Addition is :",Ans)

    Ans = Obj1.Substarction()
    print("Substraction is :", Ans)

    Ans = Obj1.Multiplication()
    print("Multiplication is :", Ans)

    Ans = Obj1.Division()
    print("Division is :", Ans)

    Obj2 = Arithmetic()

    Obj2.Accept()

    Ans = Obj2.Addition()
    print("Addition is :", Ans)

    Ans = Obj2.Substarction()
    print("Substraction is :", Ans)

    Ans = Obj2.Multiplication()
    print("Multiplication is :", Ans)

    Ans = Obj2.Division()
    print("Division is :", Ans)

if __name__ == "__main__":
    main()