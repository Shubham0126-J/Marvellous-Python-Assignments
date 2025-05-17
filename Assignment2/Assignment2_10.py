def checknum():

    n = input("Enter Number : ")
    sum_of_digit = 0

    for i in n :
        
        sum_of_digit +=  int(i)

    print("Sum of digits : ", sum_of_digit)

if __name__ == "__main__":
    checknum()