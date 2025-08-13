# BANK SYSTEM =====
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Check Balance
# "5. Show All Accounts"
# 6. Exit
from sys import excepthook


def introduction():
    print()
    print("===== BANK SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

def create_account(account,customers):
    name = input("Enter your name:")
    account += 1
    customer = {
        "name": name,
        "account": str(account),
        "deposit": 0
    }
    customers.append(customer)
    print("Account created for", customer["name"], ".Account number:", customer["account"])

def deposit(customers):
    account_n = input("Enter account number:")
    for i, customer in enumerate(customers):
        if account_n == customer["account"]:
            try:
                income = int(input("Enter deposit amount:"))
                customer["deposit"] += income
                print(income, "has been deposited")
                break
            except ValueError:
                print("Number only")
                break
        if i == len(customers) -1:
            print("There is no customers")


def withdraw(customers):
    account_n = input("Enter account number:")
    for i,customer in enumerate(customers):
        if account_n == customer["account"]:
           try:
                withdrawal = int(input("Enter withdrawal amount:"))
                customer["deposit"] -= withdrawal
                print(withdrawal, "has been withdrawn")
                break
           except ValueError:
                print("Number only")
                break
        if i == len(customers)-1:
            print("There is no customers")

def check_balance(customers):
    account_n = input("Enter account number:")
    for i,customer in enumerate(customers):
        if account_n == customer["account"]:
            print(f"{customer["name"]}'s account balance: {customer["deposit"]}")
            break
        if i == len(customers)-1:
            print("Account not found.")


def show_all(customers):
    print("=== All Accounts ===")
    for customer in customers:
        print(f"Account: {customer['account']}  | Owner: {customer['name']} | Balance: {customer['deposit']}")



account = 0
customers = []
while True:
    introduction()
    option = input("Select a menu option: ")
    if option == "1":
        create_account(account,customers)

    elif option == "2":
        deposit(customers)

    elif option == "3":
       withdraw(customers)

    elif option == "4":
       check_balance(customers)

    elif option == "5":
        show_all(customers)

    elif option == "6":
       break


