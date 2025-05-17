

def main():

    numbers = []
    n = int (input("How many numbers you want to enter : "))

    for i in range (n):
        num = int (input (f"Enter Number {i + 1} : "))
        numbers.append(num)

    min_number = min(numbers)

    print("Minimum number from list is : ", min_number)


if __name__ == "__main__":
    main()