class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a value : "))

    def Factors(self):
        print(f"Factors of {self.Value} are : ", end=' ')
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=' ')
        print( )

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i 
        return sum
  
    def ChkPrime(self):
        if self.Value <= 1:
            return False 
        for i in range(2, int(self.Value ** 0.5 ) + 1 ):
            if self.Value % i == 0:
                return False 
        return True 

    def ChkPerfect(self):
        return self.SumFactors() == self.Value
        
print(" ---- Number1 ---- ")
obj1 = Numbers()
obj1.Factors()
print("Sum of Factors: ", obj1.SumFactors())
print("Is Prime?", obj1.ChkPrime())
print("Is Perfect?", obj1.ChkPerfect())

print("\n---- Number2 ---- ")
obj2 = Numbers()
obj2.Factors()
print("Sum of Factors: ", obj2.SumFactors())
print("Is Prime?", obj2.ChkPrime())
print("Is Perfect?", obj2.ChkPerfect())
