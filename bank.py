class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit_money(self, amount):
            if amount <= 0:
                print("Value must be positive!")
            else:
                self.balance += amount
                print(f"${amount} deposited successfully! Current Balance = ${self.balance}")

        
    def withdraw_money(self, amount):
        if amount < 0:
            print("Value must be positive")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"${amount} Withdrawed successfully!!. Current Balance = {self.balance}")
    
        

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

def main():
    print("WELCOME!! To the Python Bank...")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("<<<<<------------------------------------------>>>>>")
        print("Choose your suitable Option")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your Choice number: ")

        if(choice == '1'):
            amount = float(input("Deposit money: "))
            account.deposit_money(amount)

        elif(choice == '2'):
            amount = float(input("Withdraw Money: "))
            account.withdraw_money(amount)

        elif(choice == '3'):
            account.check_balance()

        elif(choice == '4'):
            print("Thank you For Banking With us")
            break

        else:
            print("Invalid choice. Please select numbers between 1-4")

if __name__ == "__main__":
    main()