def checknum():

    l = int(input("Enter length of rectangle : "))

    w = int(input ("Enter width of Rectangle : "))

    area = l * w 

    perimeter = 2 * ( l + w )

    print("Area of Rectangle is : ", area)

    print("Perimeter of Rectangle is : ", perimeter)

if __name__ == "__main__":
    checknum()