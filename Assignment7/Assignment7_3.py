checkeven = lambda no : no % 2 == 0

def main():

   no = int(input("Enter number of elements : "))

   data = []

   for i in range(no):
      num = int(input(f"Enter Number { i + 1 } : "))
      data.append(num)

   print("Enter Numbers : ", data)

   fdata = list (filter(checkeven, data))
   print("Filter output Even number  : ", fdata)

if __name__ == "__main__":
   main()