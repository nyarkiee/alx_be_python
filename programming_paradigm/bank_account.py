class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the BankAccount with an optional initial balance (default 0)."""
        self.__account_balance = float(initial_balance)  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit a specified amount to the account."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
