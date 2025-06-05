def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    no = int(input("Enter a Number: "))

    if no < 0:
        print("Factorial is not defined for negative numbers")
    else :
        result = factorial(no)
        print(f"Factorial of {no} is {result}")

if __name__ == "__main__":
    main()