import multiprocessing

def compute_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i 
    return result


def main():
    numbers = [3,5,7,10,12]

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    print("Input Numbers : ", numbers)
    print("Factorials : ", results)

if __name__ == "__main__":
    main()
