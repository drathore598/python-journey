"""
Day 22: OOP - Classes and Objects
Focus: Classes, constructors (__init__), instance vs class variables,
instance methods, and state encapsulation.
"""

class BankAccount:
    """Represents a bank account with balance tracking and transaction audit."""
    
    bank_name = "Global Dev Bank"  # Class attribute shared across all instances
    
    def __init__(self, account_holder: str, initial_deposit: float = 0.0):
        self.holder = account_holder        # Instance attribute
        self.balance = initial_deposit      # Instance attribute
        self.transactions = []              # Transaction audit log
        
        if initial_deposit > 0:
            self.transactions.append(f"Initial deposit: +${initial_deposit:.2f}")

    def deposit(self, amount: float) -> bool:
        """Deposit funds into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw funds if sufficient balance exists."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"Withdrawal of ${amount:.2f} denied. Available balance: ${self.balance:.2f}")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -${amount:.2f}")
        return True

    def display_statement(self):
        """Print complete transaction statement."""
        print(f"--- Statement for {self.holder} ({self.bank_name}) ---")
        print(f"Current Balance: ${self.balance:.2f}")
        print("Transaction History:")
        for tx in self.transactions:
            print(f"  * {tx}")


print("--- Bank Account OOP Simulation ---")
acc1 = BankAccount("Dheeraj Rathore", 500.0)
acc1.deposit(250.0)
acc1.withdraw(120.0)
acc1.withdraw(900.0)  # Should be rejected
acc1.display_statement()

acc2 = BankAccount("Taylor Reed", 1000.0)
acc2.withdraw(300.0)
print(f"\nAccount 2 ({acc2.holder}) Balance: ${acc2.balance:.2f}")
