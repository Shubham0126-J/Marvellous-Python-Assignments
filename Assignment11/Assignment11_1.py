def print_number(n):
    if n == 0:
        return 
    print_number( n - 1 )
    print(n, end=' ')

def main():
    no = int(input("Enter Number : "))
    print_number(no)

if __name__ == "__main__":
    main()