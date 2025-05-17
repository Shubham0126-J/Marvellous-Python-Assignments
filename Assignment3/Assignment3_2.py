def main():

    number = []
    n = int(input("How many numbers you want to Enter : "))

    for i in range (n):
        num = int(input (f"Enter number { i + 1 } : "))
        number.append(num)

    max_number = max(number)

    print("Maximumn Number from list is : ", max_number)

if __name__ == "__main__":
    main()