def power_r(x, n):
    if n == 0:
        return 1
    return x * power_r (x, n-1)

def main():
    x = int(input("Enter base(x): "))
    n = int(input("Enter Exponenet(n): "))
    result = power_r(x, n)
    print(f"{x} ^ {n} is : ", result)

if __name__ == "__main__":
    main()