class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price 
        return False 

    def display(self):
        print(f"Product_name : {self.name}, Price : {self.price}")

p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 25000)
p3 = Product("Tablet", 50000)

print("Comaring p1 and p2: ")
print ("Equal price?", p1 == p2)

print("\nComparing p1 and p3: ")
print("Equal price?", p1 == p3)