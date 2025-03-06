import random

class BankAccount:
    def __init__ (self,name,pin,balance=0):
        self.name=name
        self.__pin=pin
        self.__balance=balance
        self.acc_num=random.randint(1000000, 9999999)
        self.transactions=[]
    
    def authenticate(self,pin):
        return self.__pin==pin

    def deposit(self, amount,pin):
        if self.authenticate(pin):
            if amount<=0:
                print("enter sufficient amount to deposit")
            else:
                self.__balance+=amount
                print(f"new balance = {self.__balance}")
        
        else:
            print("Wrong PIN!!!")
    
    def withdraw(self,amount,pin):
        if self.authenticate(pin):
            if self.__balance<amount:
                print("Insufficiant Balance")
            else:
                self.__balance-=amount
        
        else:
            print("Wrong PIN!!!")


    def balance_check(self,pin):
        if self.authenticate(pin):
            print(f'Balance = {self.__balance}')
        
        else:
            print("Wrong PIN!!!")
        

    def getbalance(self):
        return self.__balance

    
    def transfer(self, receiver, amount,pin):
        if self.authenticate(pin):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                receiver.deposit(amount,pin)
                self.transactions.append(f"Transferred {amount} to {receiver.name}. Balance: {self.__balance}")
                print(f"Transferred {amount} to {receiver.name}. Balance: {self.__balance}")
            else:
                print("Transfer failed. Insufficient balance.")
        
        else:
            print("Wrong PIN!!!")

    def view_statement(self,pin):
        if self.authenticate(pin):
            print(f"\nTransaction History for {self.name}:")
            for txn in self.transactions:
                print(txn)
        
        else:
            print("Wrong PIN!!!")
    
        

class SavingsAccount(BankAccount):
    def __init__(self, name,pin, Ibalance=0):
        super().__init__(name,pin, Ibalance)
        self.interest_rate = 0.03

    def apply_interest(self):
        interest = self.getbalance() * self.interest_rate
        self.deposit(interest,self._BankAccount__pin)
        print(f"Interest of {interest:.2f} applied.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, pin, account_type):
        if account_type == "savings":
            account = SavingsAccount(name, pin, 500)  # Minimum balance 500
        elif account_type == "current":
            account = BankAccount(name, pin, 1000)  # Minimum balance 1000
        else:
            print("Invalid account type!")
            return None

        self.accounts[account.acc_num] = account
        print(f"Account created successfully! Account Number: {account.acc_num}")
        return account

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    # Admin Feature: View All Accounts
    def admin_view_all_accounts(self):
        print("\n--- All Accounts in Bank ---")
        for acc_num, acc in self.accounts.items():
            print(f"Account No: {acc_num} | Name: {acc.name} | Balance: ₹{acc._BankAccount__balance}")

# Example Usage
bank = Bank()

# Creating Accounts
acc1 = bank.create_account("Hemant", 1234, "current")
acc2 = bank.create_account("pranav", 1234, "savings")
acc3 = bank.create_account("sarthak", 1234, "savings")
# Deposits & Withdrawals
acc1.deposit(20000,1234)
acc1.withdraw(500, 1234)

# Transfers
acc1.transfer(acc2, 2000, 1234)
acc1.transfer(acc3, 2000, 1234)
# Checking Balance & Transactions
acc1.balance_check(1234)
acc1.view_statement(1234)

# Admin View (Shows All Accounts)
bank.admin_view_all_accounts()

