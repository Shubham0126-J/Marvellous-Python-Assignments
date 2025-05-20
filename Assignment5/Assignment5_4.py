def checknum():

    no = int(input("Enter Number of elements :  "))

    data = []

    for i in range(no):
        num = int(input(f"Enter number {i + 1} : "))
        data.append(num)

    ret = max(data)
    print("MAximum Number is : ", ret)


if __name__ == "__main__":
    checknum()