power = lambda n : n * n 

def main():

    no = int(input("Enter a parameter : "))

    result = power(no)
    print(f"Power of {no} is : ", result)

if __name__ == "__main__":
    main()