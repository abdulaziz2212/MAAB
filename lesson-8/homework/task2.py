import uuid
import os

class Account:
    def __init__(self,account_number, name, balance):
        self.number=account_number
        self.name=name
        self.balance=balance
    
    def __str__(self):
        return f"Account Number: {self.number} | Name: {self.name} | Balance: ${self.balance:.2f}"

class Bank:
    filename='accounts.txt'

    def __init__(self):
        self.accounts=self.load_from_file()

    def create_account(self,name, initial_deposit):
        account_id=str(uuid.uuid4())[:8]
        new_account=Account(account_id,name,initial_deposit)
        self.accounts[account_id]=new_account
        self.save_to_file(new_account)
        print(f"Account created successfully! Account ID: {account_id}")

    def view_account(self,account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print(f"No Account with number: {account_number} is found")

    def deposit(self,account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            self.save_to_file()
            print(f"Deposited {amount} into account {account_number}.")
            print(self.accounts[account_number])
        else:
            print(f"No Account with number: {account_number} is found")


    def withdraw(self,account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].balance >= amount:
                self.accounts[account_number].balance -= amount
                self.save_to_file()
                print(f"Withdrew {amount} from account {account_number}.")
                print(self.accounts[account_number])
            else:
                print("Insufficient balance")
        else:
            print(f"No Account with number: {account_number} is found")

    def save_to_file(self,new_account=None):
        if new_account:
            with open(self.filename, 'a') as file:
                file.write(f"{new_account.number},{new_account.name},{new_account.balance}\n")
        else:
            with open(self.filename, 'w') as file:
                for acc in self.accounts.values():
                    file.write(f"{acc.number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        accounts={}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    data=line.strip().split(',')
                    account_number,name,balance=data
                    accounts[account_number]=Account(account_number,name,float(balance))
        return accounts

def main():
    bank=Bank()
    while True:
        print("\nWelcome to the our Bank application! ")
        print("1. Add new account record")
        print("2. Search for the account  by account number")
        print("3. Deposit monet to the account")
        print("4. Withdraw money from the account")
        print("5. Exit")

        choice=input('Enter your choice: ')
        if choice == '1':
            name=input("Enter the name: ")
            while True:
                try:
                    balance = float(input("Enter the balance: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a numeric balance.")

            bank.create_account(name,balance)

        elif choice == '2':
            account_id=input('Enter the account number to view: ').strip()
            bank.view_account(account_id)

        elif choice == '3':
            account_id=input('Enter the account number to deposit: ').strip()
            while True:
                try:
                    amount = float(input("Amount to deposit: "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid amount.")
            bank.deposit(account_id,amount)

        elif choice == '4':
            account_id=input('Enter the account number to withdraw: ').strip()
            while True:
                try:
                    amount = float(input("Amount to withdraw: "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid amount.")

            bank.withdraw(account_id, amount)
        elif choice == '5':
            print('Exiting the program. ')
            break
        else:
            print('Invalid choice. Please try again. ')

if __name__ == "__main__":
    main()
