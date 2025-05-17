def checknum():

    n=int(input("Enter number : "))

    for i in range (n):
        print(" ".join(str(x) for x in range(1,n+1)))

if __name__ == "__main__":
    checknum()