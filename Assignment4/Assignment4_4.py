from functools import reduce

checkeven = lambda no : no % 2 == 0

square = lambda no : no ** 2 

sum = lambda A, B : A + B

def main():

    no = int (input("Number of elements : "))

    data = []

    for i in range (no):
        num = int(input(f"Enter Number { i + 1} : "))
        data.append(num)

    fdata = list(filter(checkeven, data))
    print("List after filter : ",fdata)

    mdata = list(map(square, fdata))
    print("List after map : ",mdata )

    rdata = reduce(sum, mdata)
    print("Sum is : ", rdata)

if __name__ == "__main__":
    main()