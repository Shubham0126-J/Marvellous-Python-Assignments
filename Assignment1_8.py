''' 8. Write a program which accept number from user and print that number 
       of "*" on screen. '''


def Chknum():
    number = int(input("Enter a Number : "))
    
    for i in range(number):
        print ("*", end=" ")

if __name__ == "__main__":
    Chknum()