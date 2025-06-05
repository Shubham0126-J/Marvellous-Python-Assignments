def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits (n//10)

def main():

    no = int(input("Enter Number : "))
    no = abs(no)
    result = sum_of_digits(no)
    print(f"Sum of digits of {no} is : ", result)

if __name__ == "__main__":
    main()