"""
Name- Suveer Dhawan

This program creates class BankAccount to represent a basic bank account system. 
We use custom errors from custom_errors.py for assertions and defensive programming. 
Our basic system has the functionality to deposit, withdraw, and transfer money, and to ban users.
"""

from custom_errors import *

class BankAccount:
    """
    Class for a basic bank account system that allows creation of account, deposit, withdrawal, 
    and transfer of funds, as well as restricting users.

    Class Variables-
        account_number (int): Unique Account ID associated with each account
        bonus (float): Bonus gift for opening account - $49.99
        banned_accounts (dictionary): Dictionary of restricted/banned accounts and ban reasons

    Instance Variables-
        owner (string): Name of account owner
        balance (int/float): non-negative account balance
        account_number (int): Unique Account ID associated with each account
        transaction_limit: maximum transaction amount for withdrawals or transfers (None or int)
    """

    account_number = 1045
    bonus = 49.99
    banned_accounts = {}

    def __init__(self, owner, balance):
        """
        Creates a new BankAccount instance.

        Arguments- 
            owner (string): Name of account owner
            balance (int): non-negative starting account balance
        """
        # Checking input types
        if not isinstance(owner, str):
            raise CustomTypeError(f"Owner name must be string, received {type(owner)}")

        if not isinstance(balance, (int,float)):
            raise CustomTypeError(f"Balance amount must be int or float, received {type(balance)}")

        # Checking input values
        if balance < 0:
            raise CustomValueError(f"Balance amount must be non-negative, received {balance}")

        self.owner = owner
        self.balance = balance + self.bonus
        
        # Setting bank account number for instance, and updating count for class
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1
        
        self.transaction_limit = None

        # Ensuring bonus amount is correctly added to balance when opening new account
        assert self.balance == balance + BankAccount.bonus, "The bonus has not been correctly gifted"

    
    @classmethod
    def set_next_account_number(cls, next_account_number: int) -> None:
        """
        Class method that sets the account number for the next account that will be created.
        """
        #Checking input type
        if not isinstance(next_account_number, (int)):
            raise CustomTypeError(f"Account number must be int, received {type(next_account_number)}") 
        
        # Ensuring account numbers start from 1045
        if next_account_number < 1045:
            raise CustomValueError(f"Account numbers start from 1045, received {next_account_number}")
        
        cls.account_number = next_account_number

        #Checking if account number is incremented
        assert cls.account_number == next_account_number, "Next account number has not been set correctly"

    
    def ban_account(self, reason:str) -> None:
        """
        Method used to flag an account as banned. 
        """
        # Checking input types
        if not isinstance(reason, str):
            raise CustomTypeError(f"Reason to ban account must be string, received {type(reason)}")

        if self.is_banned():
            raise CustomOperationError("The account has already been banned")

        else:
            BankAccount.banned_accounts[self.account_number] = reason

    
    @classmethod
    def unban_all(cls) -> None:
        """
        Class Method that ensures all accounts are unbanned by resetting dictionary. 
        """
        cls.banned_accounts = {}

        #Ensuring banned account dict has been reset
        assert len(BankAccount.banned_accounts) == 0, "Banned accounts dictionary has not been reset correctly" 

    
    def deposit(self, amount: float | int) -> None:
        """
        Method to add a specified non-negative amount to the account balance.
        """
        #Checking input type
        if not isinstance(amount, (int, float)):
            raise CustomTypeError(f"Deposit amount must be int or float, received {type(amount)}") 

        #Checking input values
        if amount < 0:
            raise CustomValueError(f"Deposit amount must be greater than 0, received {amount}")

        #Checking if account is banned
        if self.is_banned():
            raise CustomOperationError(f"Deposits restricted to Account ({self.account_number}) as it Banned")

        
        starting_balance = self.balance
        
        self.balance += amount

        #Ensuring balance increased after deposit
        if amount == 0:
            assert self.balance == starting_balance, "Deposit amount is 0, balance should not change"
        
        # Seperating 0 and non 0 case for more exhaustive testing
        else:
            assert self.balance > starting_balance, "Deposit amount has not been credited to account"


    def withdraw(self, amount: float | int) -> None:
        """
        Method that deducts a specified non-negative amount from the account balance 
        if sufficient funds are available.
        """
        #Checking input type
        if not isinstance(amount, (int, float)):
            raise CustomTypeError(f"Withdrawal amount must be int or float, received {type(amount)}") 

        #Checking input values
        if amount < 0:
            raise CustomValueError(f"Withdrawal amount must be greater than 0, received {amount}")

        #Checking if account is banned
        if self.is_banned():
            raise CustomOperationError(f"Withdrawal restricted from Account ({self.account_number}) as it Banned")

        starting_balance = self.balance

        #Checking sufficient balance
        assert amount <= starting_balance, f"Insufficient funds in Account ({self.account_number}) for withdrawal"

        #Checking transaction limits
        if self.transaction_limit is not None and amount > self.transaction_limit:
            raise CustomLimitError(f"Withdrawal amount ${amount} exceeds maximum transaction limit ${self.transaction_limit}")
        

        self.balance -= amount

        #Ensuring balance decreased after Withdrawal
        if amount == 0:
            assert self.balance == starting_balance, "Deposit amount is 0, balance should not change"
        
        # Seperating 0 and non 0 case for more exhaustive testing
        else:
            assert self.balance < starting_balance, "Withdrawal amount has not been debited from account"

    
    def transfer_to(self, target_account: "BankAccount", amount: float | int) -> None:
        """
        Method that transfers a non-negative amount to another valid BankAccount instance, 
        if enough funds exist.
        """
        #Checking input type
        if not isinstance(target_account, BankAccount):
            raise CustomTypeError("Target must be a BankAccount instance")

        if not isinstance(amount, (int, float)):
            raise CustomTypeError(f"Transfer amount must be int or float, received {type(amount)}") 

        #Ensuring that target_account is different form sending account
        if self is target_account:
            raise CustomValueError("Sender and receiver accounts must be different")
        
        #Checking input values
        if amount < 0:
            raise CustomValueError(f"Transfer amount must be greater than 0, received {amount}")

        #Checking if either account is banned
        if self.is_banned():
            raise CustomOperationError(f"Transfer restricted from Account ({self.account_number}) as it Banned")

        if target_account.is_banned():
            raise CustomOperationError(f"Transfer restricted to Account ({target_account.account_number}) as it Banned")

        starting_balance = self.balance
        target_starting_balance = target_account.balance

        #Checking sufficient balance
        assert amount <= starting_balance, f"Transfer cannot be completed as insufficient funds in Account ({self.account_number})"

        #Checking transaction limits
        if self.transaction_limit is not None and amount > self.transaction_limit:
            raise CustomLimitError(f"Trasfer amount ${amount} exceeds maximum transaction limit ${self.transaction_limit}")

        
        self.withdraw(amount)
        target_account.deposit(amount)
        
        # Seperating 0 and non 0 case for more exhaustive testing
        if amount == 0:
            assert self.balance == starting_balance, "Deposit amount is 0, balance should not change"
            assert target_account.balance == target_starting_balance, "Deposit amount is 0, balance should not change"

        #Ensuring balance changes in both accounts after succesful transfer
        else:
            assert self.balance < starting_balance, f"Transfer amount has not been debited from Account ({self.account_number})"
            assert target_account.balance > target_starting_balance, f"Transfer amount has not been credited to Account ({target_account.account_number})"

    
    def set_transaction_limit(self, limit: float | int | None) -> None:
        """
        Method to set the maximum transaction amount for withdrawals or transfers.
        If limit is None, removes transaction limit.
        """
        #Checking input type
        if limit is not None and not isinstance(limit, (int,float)):
            raise CustomTypeError(f"Transaction limit must be a number, received {type(limit)}")

        if limit is not None and limit < 0:
            raise CustomValueError(f"Transaction limit must be non-negative, received {limit}")
        
        self.transaction_limit = limit

    
    def is_banned(self) -> bool:
        """
        Method to check if the account is banned
        """
        return self.account_number in BankAccount.banned_accounts
    

    def __str__(self) -> str:

        if self.transaction_limit is None:
            limit = "N/A"

        else:
            limit = "{:,.2f}".format(self.transaction_limit)
        
        if self.is_banned():
            return f"{self.owner}'s account ({self.account_number}): Balance=${self.balance:,.2f} | Limit=${limit} | Banned=Yes | Ban Reason: {BankAccount.banned_accounts[self.account_number]}"

        else:
            return f"{self.owner}'s account ({self.account_number}): Balance=${self.balance:,.2f} | Limit=${limit} | Banned=No"