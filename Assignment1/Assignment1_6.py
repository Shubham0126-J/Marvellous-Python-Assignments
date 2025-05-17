''' 6. Write a program which accept number from user and check whether that number is 
       positive or negative or zero '''

def Chknum():
    number = float (input("Enter number : "))

    if number < 0 :
        print ("Negative")
    elif number > 0 :
        print ("Positive")
    else :
        print("zero")

if __name__ == "__main__":
    Chknum()
