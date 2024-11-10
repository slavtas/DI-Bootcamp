class BankAccount:
    def __init__(self,owner_name,number,balance = 0):
        self.owner_name = owner_name
        self.number = number
        self.transactions = []
        self.balance = balance
            
    def show_balance(self):
        print(f'Your balance now is {self.balance}')

    def deposit(self,amount):
        self.balance += amount
        self.show_balance()
        self.transactions.append(f'Deposit: {amount}')
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        self.show_balance()
        self.transactions.append(f'Withdraw: {- amount}')
        return self.balance
    
    def show_transactions(self):
        for i,track in enumerate(self.transactions):
            print(f'Transaction {i+1}: {track}')
        return self.show_balance()

    


my_account = BankAccount('Slava Boytsun', 712, 100)
my_account.deposit(50)
my_account.deposit(75)
my_account.withdraw(45)
my_account.withdraw(15)
my_account.deposit(15)
my_account.withdraw(85)
my_account.deposit(50)
my_account.deposit(60)

my_account.show_transactions

print(my_account.transactions)

# class BankAccount:

#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []

#     def view_balance(self):
#         self.transactions.append("View Balance")
#         print(f"Balance for account {self.account_number}: {self.balance}")

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount

#     def view_transactions(self):
#         print("Transactions:")
#         print("-------------")
#         for transaction in self.transactions:
#             print(transaction)
