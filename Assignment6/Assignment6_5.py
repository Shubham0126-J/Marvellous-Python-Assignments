def checkprime(n):

    if n <= 1 :
        return False
    
    if n == 2 :
        return True
    
    if n % 2 == 0 :
        return False
    
    for i in range (3, int(n ** 0.5)+1 , 2):
        if n % i == 0:
            return False
        
    return True
    
number = int(input("Enter a Number : "))

if checkprime(number):
    print("Number is Prime ")
else:
    print("Number is not prime")


if __name__ == "__main__":
    checkprime