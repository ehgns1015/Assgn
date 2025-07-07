# BANK SYSTEM =====
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Check Balance
# "5. Show All Accounts"
# 6. Exit
account = 0
customers = []
while True:
    print()
    print("===== BANK SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")
    option = input("Select a menu option: ")
    if option == "1":
        name = input("Enter your name:")
        account += 1
        customer = {
            "name": name,
            "account": str(account),
            "deposit": 0
        }
        customers.append(customer)
        print("Account created for",customer["name"],".Account number:",customer["account"])


    elif option == "2":
        account_n = input("Enter account number:")
        for customer in customers:
            if account_n == customer["account"]:
                deposit = int(input("Enter deposit amount:"))
                customer["deposit"] += deposit
                print(deposit,"has been deposited")
    elif option == "3":
        account_n = input("Enter account number:")
        for customer in customers:
            if account_n == customer["account"]:
                withdrawal = int(input("Enter withdrawal amount:"))
                customer["deposit"] -= withdrawal
                print(withdrawal, "has been withdrawn")

    elif option == "4":
        account_n = input("Enter account number:")
        for customer in customers:
            if account_n == customer["account"]:
                print(f"{customer["name"]}'s account balance: {customer["deposit"]}")
    elif option == "5":
        print("=== All Accounts ===")
        for customer in customers:
            print(f"Account:{customer["account"]}  | Owner:{customer["name"]} | Balance:{customer["deposit"]}")

    elif option == "6":
        break
    else:
        print("I don't understand")


