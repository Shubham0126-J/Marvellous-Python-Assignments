def count_zeroes(n):
    if n == 0:
        return 0
    elif n % 10 == 0: 
        return 1 + count_zeroes( n // 10)
    else:
        return count_zeroes (n // 10)

def main():

    no = int(input("Enter a Number : "))
    result = count_zeroes(no)
    print(f"Count of zeroes from {no} are : ", result)

if __name__ == "__main__":
    main()