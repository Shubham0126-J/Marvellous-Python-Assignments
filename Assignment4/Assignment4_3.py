from functools import reduce 

checknum = lambda no : 70 <= no <= 90

increase = lambda no : no + 10 

product = lambda A, B : A * B 

def main ():

    no = int(input("Enter number of elements : "))

    data =[]

    for i in range (no):
        num = int (input(f"Enter Number {i + 1 } : "))
        data.append(num)


    fdata = list(filter(checknum, data))
    print("Filter output is : ",fdata)

    mdata = list(filter(increase, fdata))
    print("Map output is : ",mdata)

    rdata = reduce(product, mdata)
    print("Reduce output is : ", rdata)

if __name__ == "__main__":
    main()