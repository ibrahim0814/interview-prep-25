"""
🎯 Challenge: Build a “BankAccount” system

1. Abstract Base Class:
   - Create an abstract class BankAccount with:
     - an abstract method calculate_interest()

2. Concrete Class:
   - Make a subclass SavingsAccount that implements calculate_interest()

3. Dunder Method:
   - Add __eq__ so that two accounts are equal if their account numbers are the same.

4. Static Method:
   - Add is_valid_balance(balance) → returns True if balance is ≥ 0.

5. Class Method:
   - Add from_string(cls, data) → lets you build a SavingsAccount 
     from "name-account_number-balance" format.

Example usage:

acc1 = SavingsAccount("Alice", 101, 1000)
acc2 = SavingsAccount.from_string("Bob-102-2000")

print(acc1 == acc2)                   # False
print(SavingsAccount.is_valid_balance(500))  # True
print(acc1.calculate_interest())      # should return interest amount
"""

"""
🔁 Part 2 — Make your accounts “Pythonic” with __repr__ and __str__

Goals
1) Implement __repr__(self)
   - Purpose: unambiguous, developer-facing representation (good for debugging).
   - Put it in BankAccount if you want all account types to inherit it; otherwise in SavingsAccount.
   - Suggested shape:
       ClassName(name='Alice', acct_num=101, balance=1000.0)
   - Tip: use the class name dynamically and repr-friendly conversions:
       f"{self.__class__.__name__}(name={self.name!r}, acct_num={self.acct_num!r}, balance={float(self.balance)!r})"
   - Do NOT include sensitive data.

2) Implement __str__(self)
   - Purpose: friendly, user-facing string.
   - Suggested shape:
       "Alice (#101): balance $1,000.00"
   - Tip: money formatting:
       f"${self.balance:,.2f}"

3) Quick tests to run
   print(acc1)           # triggers __str__
   print([acc1, acc2])   # collections show __repr__ for their items

   # Expected:
   # - __str__: a clean, readable one-liner for a single account.
   # - __repr__ in list: ClassName(name='...', acct_num=..., balance=...).

4) Optional stretch (ordering)
   - Add __lt__(self, other) so accounts can be sorted.
   - Choose a key (account number OR (balance, acct_num) etc.)
   - Example:
       return (self.acct_num, self.name) < (other.acct_num, other.name)
   - Then try:
       print(sorted([acc2, acc1]))  # should use your __lt__

Notes
- If you implement in the base class, all subclasses get it “for free.”
- Prefer implementing __repr__ even if you skip __str__ (it shows up in lists, the REPL, logs).
"""




from abc import ABC, abstractmethod # this is really important to import for abstract base classes because


class BankAccount(ABC):

    def __init__(self, name: str, acct_num: int, balance: int) -> None:
        self.name = name
        self.acct_num = acct_num
        self.balance = balance
    
    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    def __eq__(self, other: 'BankAccount') -> bool: # this 'BankAccount' syntax is new and important to keep in mind
        return self.acct_num == other.acct_num

    @staticmethod
    def is_valid_balance(balance) -> bool:
        return balance >= 0

    def __repr__(self) -> str:
        return f"BankAccount(name={self.name}, acct_num={self.acct_num}, balance={self.balance})"
        


class SavingsAccount(BankAccount):

    def __init__(self, name: str, acct_num: int, balance: int) -> None:
        super().__init__(name, acct_num, balance)

    def calculate_interest(self) -> float:
        return self.balance * 0.05

    @classmethod
    def from_string(cls, data):
        splitData = data.split('-')
        return cls(splitData[0], splitData[1], splitData[2])


acc1 = SavingsAccount("Alice", 101, 1000)
acc2 = SavingsAccount.from_string("Bob-102-2000")

print(acc1 == acc2)                   # False
print(SavingsAccount.is_valid_balance(500))  # True
print(acc1.calculate_interest())      # should return interest amount


print(acc1)           # triggers __str__
print([acc1, acc2])   # collections show __repr__ for their items





    
