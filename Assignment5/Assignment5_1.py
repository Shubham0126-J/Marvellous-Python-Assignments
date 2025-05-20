def addition(A, B):
    ans = 0
    result = A + B 
    return result

def difference(A, B):
    result= A - B
    return result

def product(A, B):
    result = A * B 
    return result

def division(A, B):
    result = A / B 
    return result 

def main():
    no1 = int(input("Enter First Number : "))

    no2 = int(input ("Enter second Number : "))

    result = addition(no1, no2)
    print("Addition is : ", result)

    result = difference(no1, no2)
    print("difference is : ", result)

    result = product(no1, no2)
    print("Product is : ", result)

    result = division(no1,no2)
    print("Division is : ", result)

if __name__ == "__main__":
    main()