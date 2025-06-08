class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def Add(self):
        ret1 = self.value1 + self.value2
        print("Addition is : ",ret1)
    
    def substract(self):
        ret1 = self.value1 - self.value2
        print("Subtraction is : ",ret1)


    def multiply(self):
        ret1 = self.value1 * self.value2
        print("multiplication is : ",ret1)

    def divide(self):
        if self.value2 != 0:
            ret1 = self.value1 / self.value2
            print("Division is : ",ret1)
        else:
            print("Enter valid Number")


no1 = int(input("Enter First value: "))
no2 = int(input("Enter second value: "))
ret1 = Calculator(no1, no2)
ret1.Add()
ret1.substract()
ret1.multiply()
ret1.divide()