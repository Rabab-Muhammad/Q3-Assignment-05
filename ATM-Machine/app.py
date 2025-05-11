class ATM:
    def __init__(self):
        # Default ATM pin and Balance
        self.pin = "1234"
        self.balance = 5000
        self.is_authenticated = False

    def check_pin(self, input_pin):
        # Verify the entered pin
        if input_pin == self.pin:
            self.is_authenticated = True
            print("✅ PIN Verified Successfully!")
            print("🔓 Access Granted. Welcome!\n")
        else:
            print("❌ Incorrect PIN!")
            print("🔒 Access Denied. Please try again.\n")

    def check_balance(self):
        # Display the current balance if authenticated
        if self.is_authenticated:
            print(f"💰 Current Balance: Rs. {self.balance:.2f}\n")
        else:
            print("⚠️ Access Denied!")
            print("🔑 Please enter the correct PIN first.\n")

    def deposit(self, amount):
        # Deposit the specified amount if authenticated and amount is positive
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f"✅ Rs. {amount:.2f} deposited successfully!")
                print(f"💳 New Balance: Rs. {self.balance:.2f}\n")
            else:
                print("⚠️ Invalid Amount!")
                print("💡 Deposit amount must be positive.\n")
        else:
            print("🔒 Access Denied!")
            print("🔑 Please enter the correct PIN first.\n")

    def with_draw(self, amount):
        # Withdraw the specified amount if authenticated, amount is positive, and balance is sufficient
        if self.is_authenticated:
            if amount <= 0:
                print("⚠️ Invalid Amount!")
                print("💡 Withdraw amount must be positive.\n")
            elif amount > self.balance:
                print("❌ Transaction Failed!")
                print("💸 Insufficient Balance.\n")
            else:
                self.balance -= amount
                print(f"✅ Rs. {amount:.2f} withdrawn successfully!")
                print(f"💳 New Balance: Rs. {self.balance:.2f}\n")
        else:
            print("🔒 Access Denied!")
            print("🔑 Please enter the correct PIN first.\n")

    def exit(self):
        # Exit the ATM session
        print("🙏 Thank you for using the ATM!")
        print("👋 Goodbye. Have a great day!\n")
        return False

    def menu(self):
        # Display user menu and handle user interaction
        print("\n========== Welcome to the ATM ==========\n")
        attempts = 0
        while attempts < 3:
            input_pin = input("🔑 Please enter your 4-digit PIN: ")
            if input_pin == self.pin:
                self.is_authenticated = True
                print("✅ PIN verified successfully!\n")
                break
            else:
                attempts += 1
                print(f"❌ Incorrect PIN! {3 - attempts} attempts left.\n")
        else:
            print("⚠️ Too many incorrect attempts. Exiting...\n")
            return
        
        # ATM menu loop
        while True:
            print("========== ATM Menu ==========\n")
            print("1. 💰 Check Balance")
            print("2. 💸 Deposit Amount")
            print("3. 🏧 Withdraw Amount")
            print("4. 🚪 Exit")
            choice = input("Please select an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                try:
                    amount = float(input("\nEnter amount to deposit: Rs. "))
                    self.deposit(amount)
                except ValueError:
                    print("❌ Invalid input! Please enter a numeric value.\n")

            elif choice == '3':
                try:
                    amount = float(input("\nEnter amount to withdraw: Rs. "))
                    self.with_draw(amount)
                except ValueError:
                    print("❌ Invalid input! Please enter a numeric value.\n")
            elif choice == '4':
                if not self.exit():
                    break
            else:
                print("❌ Invalid option! Please select between 1-4.\n")


if __name__ == "__main__":
    atm = ATM()  
    atm.menu()   
