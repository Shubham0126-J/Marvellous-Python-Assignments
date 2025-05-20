from functools import reduce

product = lambda A , B : A * B 

def main():

   no = int(input("Enter Number of elements : "))

   data = []

   for i in range (no):
      num = int(input(f"Enter Number { i + 1 }: "))
      data.append(num)

   print("Enter number is : ", data)

   rdata = reduce(product, data)

   print("Product of input list is : ", rdata)


if __name__ == "__main__":
   main()