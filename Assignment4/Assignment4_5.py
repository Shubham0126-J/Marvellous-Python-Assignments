

from functools import reduce

def checkprime (no):

    if no <= 1:
        return False
    for i in range (2, int(no ** 0.5)+1 ):
        if no % i == 0 :
            return False

    return True

def multiply (no):
    result = no * 2
    return result

def max_number(x, y) :
    return x if x > y else y 


def main():

    no = int(input("Enter number of elements : "))

    data = []

    for i in range (no):
        num = int(input(f"Enter number {i + 1} : "))
        data.append(num)

    fdata = list(filter(checkprime, data))
    print("Filter output is : ",fdata)

    mdata = list(map(multiply, fdata))
    print("Map output is : ", mdata)

    rdata = reduce(max_number, mdata)
    print("Max_number is : ",rdata)


if __name__ == "__main__":
    main()