class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_name = "Tamil"
        self.account_number = "xxxxxxxxxxxx4969"
        print(f"Account name: {self.account_name}, Account num: {self.account_number}")
 
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance")
 
    def display(self):
        print("\nNet Available Balance =", self.balance)
 
# Driver code
s = BankAccount()
s.deposit()
s.withdraw()
s.display()