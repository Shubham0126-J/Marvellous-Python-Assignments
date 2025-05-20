def checknum():

    no = 5

    data = []

    for i in range(no):
        num = int(input(f"Enter Number { i + 1 } : "))
        data.append(num)

    ret = max(data)

    print("Maximum number is : ", ret)


if __name__ == "__main__":
    checknum()