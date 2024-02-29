# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.Filter should filter out all such numbers which are even.
# Map function will calculate its square. Reduce will return addition of all that numbers.

def filterX(Data):
   Result = []
   for No in Data:
      if((No%2) == 0):
         Result.append(No)

   return Result

def mapX(Data):
   Result = []
   for No in Data:
      No = No**2
      Result.append(No)

   return Result

def reduceX(Data):
   Ans = 0
   for No in Data:
      Ans = Ans + No

   return Ans

def main():
   print("Enter the number of elements :")
   Size = int(input())

   Data_Input = []
   print("Enter the Data :")
   for Cnt in range(0,Size,1):
      value = int(input())
      Data_Input.append(value)

   print("Data is :",Data_Input)

   Data_Filter = filterX(Data_Input)

   print("Data after filter is :",Data_Filter)

   Data_Map = mapX(Data_Filter)

   print("Data after map is :", Data_Map)

   Data_Reduce = reduceX(Data_Map)

   print("Data after reduce is :", Data_Reduce)

if __name__ == "__main__":
   main()