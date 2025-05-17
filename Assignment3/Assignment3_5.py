

from MarvellousNum import chkprime

def listprime(numbers):
    prime_sum = 0

    for num in numbers :
        if chkprime(num):
            prime_sum += num 
    
    return prime_sum

def main():
    n = int(input("Enter number of Elements : "))

    numbers = []

    for i in range (n):
        num = int(input(f"Enter Number {i + 1} : "))
        numbers.append(num)

    result = listprime(numbers)

    print("Sum of prime numbers is ", result)

if __name__ == "__main__":
    main()    