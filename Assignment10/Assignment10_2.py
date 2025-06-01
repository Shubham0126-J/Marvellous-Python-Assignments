multiplication = lambda A, B : A * B 

def main():

    no1 = int(input("Enter first Number : "))
    no2 = int(input("Enter Second Number : "))

    result = multiplication(no1, no2)
    print(f"Multication of {no1} and {no2} is : ", result)

if __name__ == "__main__":
    main()