class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"{self.owner}'s account. Balance: £{self.balance}"
        
    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"
        
    def __len__(self):
        # Could represent number of transactions
        return 1  # Placeholder
        
    def __bool__(self):
        # Account is "truthy" if it has a positive balance
        return self.balance > 0
        
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.owner == other.owner and self.balance == other.balance

account = BankAccount("John", 100)
print(account)      # Calls __str__
print(repr(account))  # Calls __repr__
if account:         # Calls __bool__
    print("Account has funds")
