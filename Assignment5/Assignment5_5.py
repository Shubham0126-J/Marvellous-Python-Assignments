def checknum ():
    try:
        no = int(input("Enter Number : "))

        
        if no % 2 == 0:
            print("Number is Even ")
        else:
            print("Number is Odd")

    except ValueError as vobj :
        print("Invalid data type of Input : ", vobj)

if __name__ == "__main__":
    checknum()