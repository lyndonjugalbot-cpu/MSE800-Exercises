from db import Database
from account import Account, SavingsAccount

def menu():
    
    print("Welcome to the Bank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Add Interest (Savings Account)")
    print("6. Exit")


def main():
    #initialize the database
    database = Database.DB_NAME
    Database.get_connection(database)
    Database.create_table(database)

    status = Database.check_status(database, "383540")
    while True:
        # show menu for the customer
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            savings = input("Savings Account?:(y/n) ").strip()
            if savings == "n":
                name = input("Enter account holder name: ").strip()
                ac_num = Database.create_customer(database, name)
                print(f"Account created successfully! Your account number is {ac_num}")
            elif savings == "y":
                name = input("Enter account holder name: ").strip()
                ac_num = Database.create_cust_savings(database, name)
                print(f"Account created successfully! Your account number is {ac_num}")
            else:
                print("Invalid Input!")
                menu()

        elif choice == "2":
            #Deposit
            ac_num = input("Enter your account number: ").strip()
            amount = input("Enter the deposit amount: ").strip()
            balance = Database.deposit_money(database, amount, ac_num)
            print(f"Deposit Success! Your new balance is: {balance}")

        elif choice == "3":
            #Withdraw
            ac_num = input("Enter your account number: ").strip()
            amount = input("Enter the amount to withdraw: ").strip()
            balance = Database.withdraw_money(database, amount, ac_num)
            print(f"{amount} withdrawn. Your new balance: {balance}")

        elif choice == "4":
            #Check Balance
            ac_num = input("Enter your account number: ").strip()
            balance = Database.check_balance(database, ac_num)
            print(f"Your balance is: {balance}")

        elif choice == "5":
            #Add Interest (Savings Account)
            ac_num = input("Enter your account number: ").strip()
            savings = Database.check_savings_acct(database, ac_num)
            if savings == 1:
                #constant interest of 3%
                balance = Database.interest_balance(database, ac_num)
                if balance > 0:
                    print(f"Your new balance with 3% interest rate: {balance}")
                else:
                    print(f"Your balance is: {balance}")
            else:
                print("This is not a savings account.")
                return
            
        elif choice == "6":
        # Break out of the loop, which ends the program.
            print("Goodbye!")
            break
        
        else:
            print("Invalid option.")
            menu()



if __name__ == "__main__":
    main()


