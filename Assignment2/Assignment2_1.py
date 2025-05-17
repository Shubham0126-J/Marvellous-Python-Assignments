# 1.

import moduleAssignment as m

def main():

    a = float(input("Enter First Number : "))
    b = float(input("Enter Second Number: "))

    result = m.add(a, b)
    print ("Addition is : ", result)

    result = m.sub(a, b)
    print("substraction is : ", result)

    result = m.mult(a, b)
    print ("multiplication is : ", result)

    result = m.div(a, b)
    print ("Division is : ", result) 
                                         
if __name__ == "__main__":
    main()