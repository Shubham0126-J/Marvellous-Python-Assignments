import multiprocessing

def square(n):
    return n * n 

def main():
    no = int(input("Enter number of elements : "))

    numbers = []

    for i in range (no):
        num = int(input(f"Enter Number {i + 1}: "))
        numbers.append(num)

    with multiprocessing.Pool() as pool:
        result = pool.map(square, numbers)

    
    print("Original numbers : ", numbers)
    print("Squared results : ", result)

if __name__ == "__main__":
    main()