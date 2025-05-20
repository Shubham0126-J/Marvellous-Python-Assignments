
def main():

    no = int(input("Enter a Number : "))

    factorial = 1

    if no < 0:
        print("Factorial is not defined for negative numbers")
   
    else:
        for i in range(1, no + 1):
            factorial = factorial * i

    print(f"Factorial of {no} is : ", factorial)

if __name__ == "__main__":
    main()