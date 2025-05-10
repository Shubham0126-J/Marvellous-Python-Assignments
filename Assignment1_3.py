
''' 3. Write a program which contains one function named as Add() which accepts two numbers
       from user and return addition of that two numbers. '''


def Add(no1, no2):
    ans = 0
    return no1 + no2

value1 = float(input("Enter First Number : "))
value2 = float(input("Enter Second Number : "))

result = Add(value1, value2)
print("Addition of Entered number is : ",result)
