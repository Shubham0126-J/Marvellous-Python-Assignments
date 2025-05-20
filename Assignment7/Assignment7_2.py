double = lambda no : no * 2

def checknum():

   no = int(input("Enter number of Elements : "))

   data = []

   for i in range (no):
      num = int(input(f" Enter Number { i + 1 } : "))
      data.append(num)

   print (data)

   mdata = list (map (double , data))
   print("Double Number : ", mdata)


if __name__ == "__main__":
   checknum()