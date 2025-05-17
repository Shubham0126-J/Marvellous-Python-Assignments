''' 7. Write a program which contains one function that accept one number from user 
       and returns True if number is divisible by 5 otherwise return False. '''

def Chknum():
    number = int(input("Enter a number : "))


    if number % 5 == 0 :
        print("True")
    else :
        print("False")

if __name__ == "__main__":
    Chknum()    
