class BankAccount():
    ROI = 10.5

    def __init__(self):
        self.name = input("Enter Account Holder's Name : ")
        self.amount = float(input("Enter Initial Balance : "))

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.amount += deposit_amount
        print(f"{deposit_amount} deposited successfully. ")

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
        else :
            print("Insufficient Balance ")

    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print(f"Interest on Current balance {self.amount} at {BankAccount.ROI}% is: {interest}")

    def Display(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.amount}")

print("---Account1----")
account1 = BankAccount()
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()

print("\n---Account2----")
account2 = BankAccount()
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()
account2.Display()