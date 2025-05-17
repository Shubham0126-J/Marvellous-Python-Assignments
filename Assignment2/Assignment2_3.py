def checknum():
    
    no = int(input("Enter a Number: "))

    factorial = 1

    for i in range (1, no + 1):
        factorial = factorial * i

    print("Factorial of ",no,"is : ", factorial)


if __name__ =="__main__":
    checknum()