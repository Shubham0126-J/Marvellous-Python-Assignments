class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price 

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price. Price must be greater than Zero")

    def display(self):
        print(f"title : {self.title}, price:{self.__price}")

book1 = Book("Python Programming", 499)

print("Price using getter: ", book1.get_price())

book1.set_price(550)

book1.display()