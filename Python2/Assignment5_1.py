# 1. Write a program which contains one class named as Demo. Demo class contains two instance variables as no1,no2.
# That class contains one class variable as Value. There are two instance methods of class as Fun and Gun which
# displays values of instance variables. Initialise instance variables in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    Value = 0
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Value of first instance variable in Fun method :",self.No1)
        print("Value of second instance variable in Fun method :",self.No2)

    def Gun(self):
        print("Value of first instance variable in Gun method :",self.No1)
        print("Value of second instance variable in Gun method :",self.No2)

def main():
    print("Enter the first number :")
    Value1 = int(input())

    print("Enter the first number :")
    Value2 = int(input())

    Obj1 = Demo(Value1,Value2)

    Obj2 = Demo(Value1,Value2)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()
