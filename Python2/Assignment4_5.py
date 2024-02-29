# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.Filter should filter out all prime numbers.
# Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.

def filterX(Data,No):
   Result = []
   for i in range(0,No):
      for no in range(2,Data[i],1):
         if((Data[i]%no)==0):
            i+=1
      if i==1:
         Result.append(Data[i])

   return Result

def mapX(Data):
   Result = []
   for No in Data:
      No = No*2
      Result.append(No)

   return Result

def reduceX(Data):
   Max = 0
   for No in Data:
      if(No > Max):
         Max = No

   return Max

def main():
   print("Enter the number of elements :")
   Size = int(input())

   Data_Input = []
   print("Enter the Data :")
   for Cnt in range(0,Size,1):
      value = int(input())
      Data_Input.append(value)

   print("Data is :",Data_Input)

   Data_Filter = filterX(Data_Input,Size)

   print("Data after filter is :",Data_Filter)

   Data_Map = mapX(Data_Filter)

   print("Data after map is :", Data_Map)

   Data_Reduce = reduceX(Data_Map)

   print("Data after reduce is :", Data_Reduce)

if __name__ == "__main__":
   main()