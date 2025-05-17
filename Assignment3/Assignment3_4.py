

def main():

    numbers = []
    n = int(input("How many numbers you want to enter : "))

    for i in range(n):
        num = int (input (f"Enter number {i + 1} : "))
        numbers.append(num)

    num_search = int(input ("Enter number to search : "))
    result = numbers.count(num_search)

    print("Frequency of ", num_search, "is : ",result)


if __name__ == "__main__":
    main()