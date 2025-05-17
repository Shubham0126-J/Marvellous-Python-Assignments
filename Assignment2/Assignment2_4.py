def checknum():

    no = int(input("Enter a Number : "))

    addition= 0

    for i in range (1, no):
        if no % i == 0 :
            addition = addition + i

    print ("addition of factors is : ",addition)

if __name__ == "__main__":
    checknum()