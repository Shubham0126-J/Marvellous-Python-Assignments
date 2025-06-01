from functools import reduce
def checkeven(no):
    return no % 2 == 0

def square(no):
    return no * no

def addition(A, B):
    return A + B 

def main():
    no = int(input("Enter Number of elements : "))

    data = []

    for i in range(no):
        num = int(input(f"Enter number { i + 1 } : "))
        data.append(num)

    print("Entered list is : ", data)

    fdata = list(filter(checkeven, data))
    print("Filtered output is : ", fdata)

    mdata = list(map(square, fdata))
    print("Mapped output is : ", mdata)

    rdata = reduce(addition, mdata)
    print("Reduced output is : ", rdata)

if __name__ == "__main__":
    main()