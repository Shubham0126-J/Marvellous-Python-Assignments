def checkprime(num): 
   if num <= 1 :
      return False 
   if num == 2:
      return True
   for i in range (2, int( num ** 0.5)+ 1 ):
      if num % i == 0:
         return False 
    
   return True
    

def checknum(numbers):
   return list(filter(checkprime, numbers))

def main():
   no = int(input("Enter number of elements : "))

   data = []

   for i in range (no):
      num = int(input(f"Enter number { i + 1 }: "))
      data.append(num)

   prime_numbers = checknum(data)
   print("Prime numbers are : ", prime_numbers )

if __name__ == "__main__":
   main()