def checktemp():

    C = int(input("Enter temprature in Celsius : "))

    F = (C * 9/5) + 32 

    print(f"Temprature in Fahrenheit is : {F} °F")


if __name__ == "__main__":
    checktemp()