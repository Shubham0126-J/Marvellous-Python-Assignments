
''' 2. Write a program which contains one function named as Chknum() which accept one parameter 
       as number. If number is even then it should display "Even number" othervise 
       display "Odd Number " on console . '''


def Chknum ():
    no1 = float(input("Enter Number : ")) 

    if (no1 % 2 == 0):
        print("Even number")
    else :
        print("Odd number")

if __name__ == "__main__":
    Chknum()
