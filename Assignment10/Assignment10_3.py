from functools import reduce
def checknum (no):
    return 70 <= no <= 90

def increase(no):
    return no + 10

def product(A, B):
    return A * B

def main ():

    no = int(input("Enter number of elements : "))

    data = []

    for i in range (no):
        num = int(input(f"Enter number { i + 1 } : "))
        data.append(num)

    print ("Entered list is : ", data)
    fdata = list(filter(checknum, data))
    print("Filterd output is : ", fdata)

    mdata = list(map(increase, fdata))
    print("Mapped output is : ",mdata)

    rdata = reduce(product, mdata)
    print("Reduced output is : ", rdata)

if __name__ == "__main__":
    main()