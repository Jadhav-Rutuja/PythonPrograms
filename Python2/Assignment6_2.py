# 2. Write a program which contains one class named as BankAccount. BankAccount class contains two
# instance variables as Name & Amount. That class contains one class variable as ROI which is initialise
# to 10.5. Inside init method initialise all name and amount variables by accepting the values from user.
# There are four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateInterest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdraw from user and subtract that amount from class
# instance variable Amount.CalculateInterest() method claculate the interest based on Amount by
# considering rate of interest which is Class variable as ROI. And Display() method will display value
# of all the instance variables as Name and Amount. After designing the above class call all instance
# methods by creating multiple objects.

class BankAccount:
    ROI = 10.5
    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def Accept(self):
        print("Enter the Name:")
        self.Name = input()

        print("Enter the initial amount :")
        self.Amount = int(input())

    def Display(self):
        print("Name of bank holder :", self.Name)
        print("Current amount in account :", self.Amount)

    def Deposit(self,Value):
        self.Amount = self.Amount + Value
        return self.Amount

    def Withdraw(self,Value):
        self.Amount = self.Amount - Value
        return self.Amount

    def CalculateInterest(self,Year):
        self.Interest = self.Amount * Year * BankAccount.ROI
        return self.Interest

def main():
    Obj1 = BankAccount()

    print("Enter the amount to deposit:")
    DepositAmount = int(input())
    TotalAmount = Obj1.Deposit(DepositAmount)
    print("Amount after deposit:", TotalAmount)

    print("Enter the amount to Withdraw:")
    WithdrawAmount = int(input())
    TotalAmount = Obj1.Withdraw(WithdrawAmount)
    print("Amount after withdraw:", TotalAmount)

    print("Enter the number of years:")
    year = int(input())
    Interest = Obj1.CalculateInterest(year)
    print("Interest based on amount:", Interest)

    Obj2 = BankAccount()

    print("Enter the amount to deposit:")
    DepositAmount = int(input())
    TotalAmount = Obj2.Deposit(DepositAmount)
    print("Amount after deposit:", TotalAmount)

    print("Enter the amount to Withdraw:")
    WithdrawAmount = int(input())
    TotalAmount = Obj2.Withdraw(WithdrawAmount)
    print("Amount after withdraw:", TotalAmount)

    print("Enter the number of years:")
    year = int(input())
    Interest = Obj2.CalculateInterest(year)
    print("Interest based on amount:", Interest)

if __name__ == "__main__":
    main()