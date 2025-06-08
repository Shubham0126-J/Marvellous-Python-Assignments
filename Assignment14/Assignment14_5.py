class Bankaccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid Amount Entered") 

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdraw successfully")
        else:
            print("Insufficient balance or Wrong amount Entered")

    def display(self):
        print("Accout number: ", self.account_number)
        print("Name : ", self.name)
        print("Balance : ", self.balance)

account1 = Bankaccount(12345, "ABC", 15000)
account1.display()

account1.deposit(10000)

account1.withdraw(3000)

account1.display()