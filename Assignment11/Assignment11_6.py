def sum_r(n):
    if n == 1:
        return 1
    else :
        return n + sum_r(n -1)

def main():
    no = int(input("Enter number : "))
    result = sum_r (no)
    print(f"Sum of natural number upto {no} is : ", result)
if __name__ == "__main__":
    main()