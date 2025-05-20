
def checksum():

    sum = 0 

    for i in range (1, 100 + 1):
        if i % 2 == 0:
            sum = sum + i 
    
    print("Addition of even numbers is : ",sum)


if __name__ == "__main__":
    checksum()