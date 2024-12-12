class Bank:
    def __init__(self):
        self.balance = 1000
        self.pin = 3024

    def options(self):
        while True:
            print("\nSelect an option:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Balance Enquiry")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                self.withdraw()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.enquiry()
            elif choice == "4":
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def validate(self):
        print("Welcome to ABC Bank")
        for attempts_left in range(3, 0, -1):
            number = int(input("Enter your PIN: "))
            if number == self.pin:
                print("PIN validated successfully!")
                self.options()
                return
            else:
                print(f"Invalid PIN. You have {attempts_left - 1} attempts left.")
        print("All attempts are used. Your card is blocked for today.")
        exit()

    def deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount < 100:
            print("Deposit amount should be greater than 100.")
        elif deposit_amount > 50000:
            print("Maximum deposit amount is 50,000.")
        elif deposit_amount % 100 != 0:
            print("Only multiples of 100 are accepted.")
        else:
            self.balance += deposit_amount
            print(f"Deposited {deposit_amount}. New balance: {self.balance}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount < 100:
            print("Minimum withdrawal amount is 100.")
        elif amount == self.balance:
            print("Withdrawal amount cannot equal the balance. You need to maintain a minimum balance of 500.")
        elif amount > 20000:
            print("Maximum withdrawal amount per transaction is 20,000.")
        elif amount % 100 != 0:
            print("Only multiples of 100 are accepted.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def enquiry(self):
        print(f"Your current balance is: {self.balance}")


# Create an instance of the Bank class and validate the user
obj = Bank()
obj.validate()
