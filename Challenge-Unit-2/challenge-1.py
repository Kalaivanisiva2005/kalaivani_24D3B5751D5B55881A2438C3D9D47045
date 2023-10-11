class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"₹{amount} deposited successfully. New balance: ₹{self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"₹{amount} withdrawn successfully. New balance: ₹{self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}"

# Example usage:
if __name__ == "__main__":
    # Creating a BankAccount instance
    account1 = BankAccount("12345", "Kalaivani", 1000.0)

    # Testing deposit and withdrawal
    print(account1.display_balance())
    print(account1.deposit(500))
    print(account1.withdraw(200))
    print(account1.display_balance())
