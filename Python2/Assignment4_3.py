# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.Filter should filter out all such numbers which greater than or equal
# to 70 and less than or equal to 90.Map function will increase by 10. Reduce will return product of all that numbers.

def filterX(Data):
   Result = []
   for No in Data:
      if(No>=70 and No<=90):
         Result.append(No)

   return Result

def mapX(Data):
   Result = []
   for No in Data:
      No = No + 10
      Result.append(No)

   return Result

def reduceX(Data):
   Ans = 1
   for No in Data:
      Ans = Ans * No

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