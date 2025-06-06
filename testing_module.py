"""
Name- Suveer Dhawan

This program is for comprehensive automated testing of the BankAccount class by 
using unit testing (unittest module).
"""

import unittest
from bank import BankAccount 
from custom_errors import *

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """
        Setting up accounts for ease of use in tests. 
        Resetting class methods at the start to ensure uniformity.
        """
        BankAccount.set_next_account_number(1045)
        BankAccount.unban_all()
        self.account1 = BankAccount("Tom Cruise", 1000)
        self.account2 = BankAccount("Glen Powell", 987.50)
        self.account3 = BankAccount("Robert Downey Jr.", 0)

    
    def test_valid_deposit(self):
        """
        1.1 Valid deposit
        Test the deposit method of the BankAccount class to ensure it correctly adds
        the deposited amount to the account balance.
        """
        account = BankAccount("John Doe", 1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1549.99, 
        f"Deposit method failed to update balance correctly. Expected $1549.99, got ${account.balance}")

        #Making deposit test more robust with floating case
        self.account1.deposit(0.01)
        self.assertEqual(1050, self.account1.balance, 
        f"Deposit method failed to update balance correctly. Expected $1050, got ${self.account1.balance}")

        #Checking edge case for deposit of 0 dollars
        self.account2.deposit(0)
        self.assertEqual(1037.49, self.account2.balance,
        f"Deposit method failed to update balance correctly. Expected $1037.49, got ${self.account2.balance}")

        # Checking increase in balance after deposit
        starting_balance_account3 = self.account3.balance
        
        self.account3.deposit(200.00)
        self.assertEqual(249.99, self.account3.balance, 
        f"Deposit method failed to update balance correctly. Expected $249.99, got ${self.account3.balance}")

        self.assertGreater(self.account3.balance, starting_balance_account3, 
        f"Incorrect implementation of account3.deposit, balance after deposit must be greater than starting balance.")
        

    """ Initialisation and Instantiation based testing """
    
    def test_invalid_balance_type(self):
        """
        1.2 Initial Balance
        
        Checking invalid bank initial balance type assertions.
        """
        # Example of how to check if an error is being raised
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with the balance 'fifty'. Either no error or the incorrect error was raised."):
            BankAccount("Rupert", "fifty") 

        # Balance as None
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with the balance as None. Either no error or the incorrect error was raised."):
            BankAccount("Rupert", None) 

        # Balance as a list of values
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with the balance as a list of values. Either no error or the incorrect error was raised."):
            BankAccount("Rupert", [45, 50, 70]) 

    
    def test_instantiation(self):
        """ 
        1.3 Instantiation check
        
        Checking whether an instance of BankAccount is succesfully created 
        """
        self.assertIsInstance(self.account1, BankAccount, 
        f"Account1 was not instantiated correctly, expected BankAccount, received {type(self.account1)}")
        
        self.assertIsInstance(self.account2, BankAccount, 
        f"Account2 was not instantiated correctly, expected BankAccount, received {type(self.account2)}")


    def test_initialisation(self):
        """
        1.4 Initialisation Test

        Checking all the class variables and instance variables for account1 to ensure
        that the BankAccount class is initialised correctly. 
        """
        #Running tests for Account 1
        expected_owner = "Tom Cruise"

        #Testing class Variables
        assert hasattr(BankAccount, "account_number"), "BankAccount class missing class variable: account_number"
        # Since we have created 3 accounts, Class variable for account_number should be updated to 1048
        expected_account_number = 1048   
        self.assertEqual(expected_account_number, BankAccount.account_number, 
        f"BankAccount.account_number is not initialised correctly, expected {expected_account_number}, received {BankAccount.account_number}")
        
        assert hasattr(BankAccount, "bonus"), "BankAccount class missing class variable: bonus"
        expected_bonus = 49.99
        self.assertEqual(expected_bonus, BankAccount.bonus, 
        f"BankAccount.bonus is not initialised correctly, expected ${expected_bonus}, received ${BankAccount.bonus}")

        assert hasattr(BankAccount, "banned_accounts"), "BankAccount class missing class variable: banned_accounts"
        expected_banned_accounts = {}
        self.assertEqual(expected_banned_accounts, BankAccount.banned_accounts, 
        f"BankAccount.banned_accounts is not initialised correctly, expected {expected_banned_accounts}, received {BankAccount.banned_accounts}")

        
        #Testing instance variables
        assert hasattr(self.account1, "owner"), "BankAccount class missing instance variable: owner"
        self.assertEqual(expected_owner, self.account1.owner, 
        f"account1.owner is not initialised correctly, expected {expected_owner}, received {self.account1.owner}")
        
        assert hasattr(self.account1, "balance"), "BankAccount class missing instance variable: balance"
        expected_balance = 1049.99    #1000 + 49.99
        self.assertEqual(expected_balance, self.account1.balance, 
        f"account1.balance is not initialised correctly, expected ${expected_balance}, received ${self.account1.balance}")
        
        assert hasattr(self.account1, "account_number"), "BankAccount class missing instance variable: account_number"
        expected_account1_number = 1045   #First account created so 1045
        self.assertEqual(expected_account1_number, self.account1.account_number, 
        f"account1.account_number is not initialised correctly, expected {expected_account_number}, received {self.account1.account_number}")

        assert hasattr(self.account1, "transaction_limit"), "BankAccount class missing instance variable: transaction_limit"
        self.assertEqual(None, self.account1.transaction_limit, 
        f"account1.transaction_limit is not initialised correctly, expected None, received {self.account1.transaction_limit}")

        
        #Testing Edge cases 
        #Empty string name and 0 starting balance
        new_account = BankAccount(" ", 0)
        
        self.assertEqual(" ", new_account.owner, 
        f"new_account.owner is not initialised correctly, expected empty string "", received {new_account.owner}")
        
        self.assertEqual(49.99, new_account.balance, 
        f"new_account.balance is not initialised correctly, expected $49.99, received ${new_account.balance}")

        # Special characters and floating point balance with many decimal places
        new_account = BankAccount("**BOB@##", 10.50000000000)
        
        self.assertEqual("**BOB@##", new_account.owner, 
        f"new_account.owner is not initialised correctly, expected name **BOB@##, received {new_account.owner}")
        
        self.assertEqual(60.49, new_account.balance, 
        f"new_account.balance is not initialised correctly, expected $60.49, received ${new_account.balance}")

    
    def test_invalid_owner_type(self):
        """
        1.5 Invalid Owner Type

        Checking if errors are raised when incorrectly initialising accounts with non-string values for owner  
        """
        #Owner name as int
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with the owner name 123. Either no error or the incorrect error was raised."):
            BankAccount(123, 750.09)

        #Owner name as float
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with the owner name 37.5. Either no error or the incorrect error was raised."):
            BankAccount(37.5, 50)

        #Owner name as None
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with None value for owner name. Either no error or the incorrect error was raised."):
            BankAccount(None, 50)

        #Owner name as List of names
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when making a bank account with list of values for owner name. Either no error or the incorrect error was raised."):
            BankAccount(["Adam", "Bob", "Charlie"], 500000)

    
    def test_invalid_balance_value(self):
        """
        1.5 Invalid Balance Value

        Checking if errors are raised when incorrectly initialising accounts with negative values for starting balance  
        """
        with self.assertRaises(CustomValueError, 
        msg="Expected a type error to be raised when making a bank account with negative starting balance of -2000. Either no error or the incorrect error was raised."):
            BankAccount("Adam", -2000)

        with self.assertRaises(CustomValueError, 
        msg="Expected a type error to be raised when making a bank account with negative starting balance of -0.05. Either no error or the incorrect error was raised."):
            BankAccount("Clown", -0.05)

    
    """ Set account number Testing """
    
    def test_valid_set_next_account_number(self):
        """
        1.6 Valid Set Account number

        Testing valid implementation of set_next_account_number.
        """
        #Test 1 with random number
        BankAccount.set_next_account_number(2000)
        self.assertEqual(2000, BankAccount.account_number, 
        f"Incorrect implementation of BankAccount.set_next_account_number, expected: 2000, received: {BankAccount.account_number}")

        #Checking implementation
        new_account = BankAccount("", 500)
        self.assertEqual(2000, new_account.account_number, 
        f"Incorrect implementation of BankAccount.set_next_account_number, expected: 2000, received: {self.account1.account_number}")

        #Test 2 with edge case minimum value
        BankAccount.set_next_account_number(1045)
        self.assertEqual(1045, BankAccount.account_number, 
        f"Incorrect implementation of BankAccount.set_next_account_number, expected: 1045, received: {BankAccount.account_number}")

        #Test 3 with random large number
        BankAccount.set_next_account_number(1000000)
        self.assertEqual(1000000, BankAccount.account_number, 
        f"Incorrect implementation of BankAccount.set_next_account_number, expected: 1000000, received: {BankAccount.account_number}")


    def test_invalid_set_next_account_number(self):
        """
        1.7 Invalid Set Account number

        Testing invalid implementation of set_next_account_number for invalid input type and values
        """
        #Test 1 with string
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when setting next account number to 'fifty'. Either no error or the incorrect error was raised."):
            BankAccount.set_next_account_number("fifty")

        #Test 2 with float
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when setting next account number to 1050.00. Either no error or the incorrect error was raised."):
            BankAccount.set_next_account_number(1050.00)

        #Test 3 with invalid value
        with self.assertRaises(CustomValueError, 
        msg="Expected a type error to be raised when setting next account number to 1044, as it is less than 1045. Either no error or the incorrect error was raised."):
            BankAccount.set_next_account_number(1044)

        with self.assertRaises(CustomValueError, 
        msg="Expected a type error to be raised when setting next account number to -10, as it is less than 1045. Either no error or the incorrect error was raised."):
            BankAccount.set_next_account_number(-10)


    """ Ban account tests """

    def test_valid_ban_account(self):
        """
        1.8 Valid Ban Account test

        Testing correct implementation of ban_account method for BankAccount class
        """
        #Ban test 1
        self.account1.ban_account("Suspicious behavior")
        self.assertIn(self.account1.account_number, BankAccount.banned_accounts,
        f"Incorrect implementation of account1.ban_account, Account {self.account1.account_number} should be in BankAccount.banned_accounts but was not found.")

        #Checking Reason
        self.assertEqual("Suspicious behavior", BankAccount.banned_accounts[self.account1.account_number], 
        f"Incorrect recording of reason for ban, expected: Suspicious behavior, received: {BankAccount.banned_accounts[self.account1.account_number]}")

        #Ban test 2
        self.account2.ban_account("")
        self.assertIn(self.account2.account_number, BankAccount.banned_accounts, 
        f"Incorrect implementation of account1.ban_account, Account {self.account2.account_number} should be in BankAccount.banned_accounts but was not found.")

        #Checking Reason
        self.assertEqual("", BankAccount.banned_accounts[self.account2.account_number], 
        f"Incorrect recording of reason for ban, expected: , received: {BankAccount.banned_accounts[self.account2.account_number]}")

    
    def test_invalid_ban_account(self):
        """
        1.9 Invalid Ban Account test

        Testing implementation of ban_account method with incorrect reason and double ban on an account
        """
        #Reason test with int values
        with self.assertRaises(CustomTypeError, 
        msg = "Expected a type error to be raised when ban reason is non string value of 23000. Either no error or the incorrect error was raised."):
            self.account1.ban_account(23000)

        #Reason test with float values
        with self.assertRaises(CustomTypeError, 
        msg = "Expected a type error to be raised when ban reason is non string value of 45.50. Either no error or the incorrect error was raised."):
            self.account2.ban_account(45.50)


        #Double banning account
        self.account3.ban_account("Fraud")

        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operation error to be raised when banning an already banned account. Either no error or the incorrect error was raised."):
            self.account3.ban_account("Double Fraud")


    def test_unban_all(self):
        """
        2.1 Test Unban all

        Testing correct implementation of unban all class method of BankAccount class. The banned_accounts dictionary should be reset.
        """
        #Banning account for the test
        self.account1.ban_account("Fraud")
        
        BankAccount.unban_all()

        #Checking if account is still banned
        self.assertNotIn(self.account1.account_number, BankAccount.banned_accounts, 
        f"Incorrect implementation of BankAccount.unban_all, BankAccount.banned_accounts should be reset but contains Account {self.account1.account_number}")

        # checking dictionary length
        self.assertEqual(0, len(BankAccount.banned_accounts), 
        f"BankAccount.banned_accounts has not been reset correctly, expected: 0, received: {len(BankAccount.banned_accounts)}")

    
    """ Deposit Tests (cont..) """

    def test_invalid_deposit_type(self):
        """
        2.2 Invalid Deposit type

        Testing deposit with invalid input types (string, list).
        """
        #Test 1 with string value 
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when depositing 'fifty' to account1. Either no error or the incorrect error was raised."):
            self.account1.deposit("fifty")

        #Test 2 with list of values
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when depositing list of values to account2. Either no error or the incorrect error was raised."):
            self.account2.deposit([45, 59, 1139])


    def test_invalid_deposit_value(self):
        """
        2.3 Invalid Deposit value

        Testing deposit with invalid deposit amounts (negative, zero).
        """
        #Test 1 with negative deposit amount 
        with self.assertRaises(CustomValueError, 
        msg= "Expected a value error to be raised when depositing negative amount to account3. Either no error or the incorrect error was raised."):
            self.account3.deposit(-450)

        #Test 2 with negative floating deposit amount 
        with self.assertRaises(CustomValueError, 
        msg= "Expected a value error to be raised when deposit amount is -0.01. Either no error or the incorrect error was raised."):
            self.account2.deposit(-0.01)

    
    def test_ban_account_deposit(self):
        """
        2.4 Deposit to banned account

        Ensuring no deposits can be made to banned accounts.
        """
        # Banning account for testing
        self.account1.ban_account("Fraud")

        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a deposit to banned account1. Either no error or the incorrect error was raised."):
            self.account1.deposit(500)

        #Test 2 with edge case float value
        self.account2.ban_account("Suspicious behavior")

        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a deposit to banned account2. Either no error or the incorrect error was raised."):
            self.account2.deposit(0.01)

    

    """ Withdrawal Tests """

    def test_valid_withdraw(self):
        """
        2.5 Valid Withdrawal

        Testing correct implentation of withdrawal for int and float amounts
        """
        starting_balance_account1 = self.account1.balance
        
        #Testing for integer values
        self.account1.withdraw(500)
        self.assertEqual(549.99, self.account1.balance, 
        f"Withdraw method failed to update balance correctly. Expected $549.99, got ${self.account1.balance}")
        
        # Ensuring decrease in balance after withdrawal
        self.assertLess(self.account1.balance, starting_balance_account1, 
        f"Incorrect implementation of account1.withdraw, balance after withdrawal must be less than starting balance.")

        # Testing for float values
        self.account3.withdraw(0.99)
        self.assertEqual(49, self.account3.balance, 
        f"Withdraw method failed to update balance correctly. Expected $49, got ${self.account3.balance}")

        #Testing for edge case of 0 as withdrawal value
        self.account3.withdraw(0.00)
        self.assertEqual(49, self.account3.balance, 
        f"Withdraw method failed to update balance correctly. Expected $49, got ${self.account2.balance}")

        # Testing for edge case, withdrawing entire balance (987.50 + 49.99)
        self.account2.withdraw(1037.49)
        self.assertEqual(0.00, self.account2.balance, 
        f"Withdraw method failed to update balance correctly. Expected $0.00, got ${self.account2.balance}")



    def test_invalid_withdraw_type(self):
        """
        2.6 Invalid Withdrawal type

        Testing withdraw with invalid input types (string, list).
        """
        #Test 1 with string value 
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when withdrawing 'thirty' from account1. Either no error or the incorrect error was raised."):
            self.account1.withdraw("thirty")

        #Test 2 with list of values
        with self.assertRaises(CustomTypeError, 
        msg="Expected a type error to be raised when withdrawal amount from account2 is a list of values. Either no error or the incorrect error was raised."):
            self.account2.withdraw([995, 49, 10])

    
    def test_invalid_withdraw_value(self):
        """
        2.7 Invalid Withdraw value

        Testing withdraw with invalid withdrawal amounts (negative, zero, insufficient balance).
        """
        #Test 1 with negative withdraw amount 
        with self.assertRaises(CustomValueError, 
        msg= "Expected a value error to be raised when withdrawing negative amount from account1. Either no error or the incorrect error was raised."):
            self.account1.withdraw(-150)

        #Test 2 with negative float as withdraw amount 
        with self.assertRaises(CustomValueError, 
        msg= "Expected a value error to be raised when withdrawal amount is -100.00. Either no error or the incorrect error was raised."):
            self.account2.withdraw(-100.00)

        #Test 3 when withdrawal amount greater than balance by very small value (50.00 when balance is 49.99)
        with self.assertRaises(AssertionError, 
        msg= "Expected an Assertion error to be raised when account3 has insufficient balance. Either no error or the incorrect error was raised."):
            self.account3.withdraw(50.00)


    def test_ban_account_withdraw(self):
        """
        2.8 Withdraw from banned account

        Ensuring no withdrawals can be made from banned accounts.
        """
        # Banning account for testing
        self.account1.ban_account("Money laundering")

        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a withdrawal from banned account1. Either no error or the incorrect error was raised."):
            self.account1.withdraw(200)

        #Test 2 with edge case float value
        self.account2.ban_account("Insider Trading")

        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a withdrawal from banned account2. Either no error or the incorrect error was raised."):
            self.account2.withdraw(0.01)

    
    def test_limit_withdraw(self):
        """
        2.9 Withdraw exceeding transaction limit

        Ensuring no withdrawals can be made that are greater than maximum transaction limit.
        """ 
        #Setting transaction limit
        self.account1.set_transaction_limit(500.00)

        #Testing with int value 
        with self.assertRaises(CustomLimitError, 
        msg = "Expected a Limit error to be raised when attempting a withdrawal greater than transaction limit from account1. Either no error or the incorrect error was raised."):
            self.account1.withdraw(550)

        #Testing with float value slightly higher
        with self.assertRaises(CustomLimitError, 
        msg = "Expected a Limit error to be raised when attempting a withdrawal greater than transaction limit from account1. Either no error or the incorrect error was raised."):
            self.account1.withdraw(500.01)


    
    """ Transfer Tests """
    
    def test_valid_transfer_to(self):
        """
        3.1 Valid Transfer

        Testing correct implementation of transfer to method (int, float)  
        """ 
        # Test 1 - Account 1 to Account 3, integer amount
        self.account1.transfer_to(self.account3, 200)

        #Checking if transfer was correctly completed
        self.assertEqual(849.99, self.account1.balance, 
        f"Incorrect implementation of transfer_to method, account1 expected balance: $849.99, received: ${self.account1.balance}")

        self.assertEqual(249.99, self.account3.balance, 
        f"Incorrect implementation of transfer_to method, account3 expected balance: $249.99, received: ${self.account3.balance}")


        # Test 2 - Account 2 to Account 1, max float amount
        self.account2.transfer_to(self.account1, 1037.49)

        #Checking if transfer was correctly completed
        self.assertEqual(0.00, self.account2.balance, 
        f"Incorrect implementation of transfer_to method, account2 expected balance: $0.00, received: ${self.account2.balance}")

        expected_balance = 1037.49 + 1049.99 - 200
        self.assertEqual(expected_balance, self.account1.balance, 
        f"Incorrect implementation of transfer_to method, account1 expected balance: ${expected_balance}, received: ${self.account1.balance}")

        # Test 3 - Account 3 to Account 1, edge case, transfer 0 dollars
        self.account3.transfer_to(self.account1, 0)

        #Checking if transfer was correctly completed
        self.assertEqual(249.99, self.account3.balance, 
        f"Incorrect implementation of transfer_to method, account3 expected balance: $0.00, received: ${self.account3.balance}")

        expected_balance = 1037.49 + 1049.99 - 200 + 0
        self.assertEqual(expected_balance, self.account1.balance, 
        f"Incorrect implementation of transfer_to method, account1 expected balance: ${expected_balance}, received: ${self.account1.balance}")


    def test_invalid_transfer_to_type(self):
        """
        3.2 Invalid Transfer to type

        Checking transfer_to method for invalid input types.
        """
        #Invalid instance for target_account
        with self.assertRaises(CustomTypeError, 
        msg = "Expected a Type error to be raised when attempting to transfer to invalid instance of target_account. Either no error or the incorrect error was raised."):
            self.account1.transfer_to("Glen Powell", 200)

        with self.assertRaises(CustomTypeError, 
        msg = "Expected a Type error to be raised when attempting to transfer to invalid instance of target_account. Either no error or the incorrect error was raised."):
            self.account1.transfer_to("account2", 300)

        #String input type for amount
        with self.assertRaises(CustomTypeError, 
        msg = "Expected a Type error to be raised when transfer amount is a string. Either no error or the incorrect error was raised."):
            self.account1.transfer_to(self.account2, "300")


    def test_invalid_transfer_to_value(self):
        """
        3.3 Invalid Transfer to value

        Checking transfer_to method for invalid input values.
        """
        #Test 1 with negative transfer amount 
        with self.assertRaises(CustomValueError, 
        msg= "Expected a value error to be raised when transferring negative amount from account1. Either no error or the incorrect error was raised."):
            self.account1.transfer_to(self.account2, -150)

        #Test 2 when withdrawal amount greater than balance by very small value (50.00 when balance is 49.99)
        with self.assertRaises(AssertionError, 
        msg= "Expected an Assertion error to be raised when account3 has insufficient balance. Either no error or the incorrect error was raised."):
            self.account3.transfer_to(self.account2, 50.00)
        
        #Test 3 - sender and receiver accounts are the same
        with self.assertRaises(CustomValueError, 
        msg= "Expected a value error to be raised when sender and receiver accounts are the same. Either no error or the incorrect error was raised."):
            self.account2.transfer_to(self.account2, 100)


    def test_ban_transfer_to(self):
        """
        3.4 Transfer involving banned account

        Attempting transfer in cases where one or both accounts are banned.
        """
        # Banning account for testing
        self.account1.ban_account("Money laundering")

        # Sender is banned
        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a transfer from banned account1. Either no error or the incorrect error was raised."):
            self.account1.transfer_to(self.account2, 200)

        #Test 2 with edge case float value and banned receiver
        self.account2.ban_account("Insider Trading")

        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a transfer to banned account2. Either no error or the incorrect error was raised."):
            self.account3.transfer_to(self.account2, 0.01)

        #Test 3 - both sender and receiver are banned accounts
        with self.assertRaises(CustomOperationError, 
        msg = "Expected an Operations error to be raised when making a both accounts are banned. Either no error or the incorrect error was raised."):
            self.account1.transfer_to(self.account2, 150)


    def test_limit_transfer_to(self):
        """
        3.5 Transfer exceeding transaction limit

        Checking transfer with amount greater than transaction limit
        """
        #Setting transaction limit
        self.account2.set_transaction_limit(300.00)

        #Testing with int value 
        with self.assertRaises(CustomLimitError, 
        msg = "Expected a Limit error to be raised when transfer amount is greater than transaction limit from account2. Either no error or the incorrect error was raised."):
            self.account2.transfer_to(self.account3, 450)

        #Testing with float value slightly higher
        with self.assertRaises(CustomLimitError, 
        msg = "Expected a Limit error to be raised when transfer amount is greater than transaction limit from account2. Either no error or the incorrect error was raised."):
            self.account2.transfer_to(self.account3, 300.01)


    
    """ Transaction limit tests """
    
    def test_valid_set_transaction_limit(self):
        """
        3.6 Setting valid transaction limit

        Testing correct setup of max transaction limit (int, float, None).
        """
        # Testing for normal integer
        self.account1.set_transaction_limit(1000)
        self.assertEqual(1000, self.account1.transaction_limit, 
        f"Incorrect implementation of account1.set_transaction_limit, expected: 1000, received: {self.account1.transaction_limit}")

        # Testing for long float
        self.account2.set_transaction_limit(999.9921)
        self.assertEqual(999.9921, self.account2.transaction_limit, 
        f"Incorrect implementation of account2.set_transaction_limit, expected: 999.99, received: {self.account2.transaction_limit}")

        # Testing for 0 as max limit while updating transaction limit
        self.account1.set_transaction_limit(0.00)
        self.assertEqual(0.00, self.account1.transaction_limit, 
        f"Incorrect implementation of account1.set_transaction_limit, expected: 0.00, received: {self.account1.transaction_limit}")

        # Testing for None
        # None to remove transaction limit of account2
        self.account2.set_transaction_limit(None)
        self.assertEqual(None, self.account2.transaction_limit, 
        f"Incorrect implementation of account2.set_transaction_limit, expected: 999.99, received: {self.account2.transaction_limit}")

        # None when transaction limit is already None for account3
        self.account3.set_transaction_limit(None)
        self.assertEqual(None, self.account3.transaction_limit, 
        f"Incorrect implementation of account3.set_transaction_limit, expected: None, received: {self.account3.transaction_limit}")


    def test_invalid_set_transaction_limit(self):
        """
        3.7 Setting invalid transaction limit

        Testing incorrect setup of max transaction limit (string, negative).
        """
        #Testing for string as transaction limit
        with self.assertRaises(CustomTypeError, 
        msg = "Expected a Type error to be raised when setting transaction limit as 'Ten'. Either no error or the incorrect error was raised."):
            self.account1.set_transaction_limit("Ten")

        #Testing for negative transaction limit
        with self.assertRaises(CustomValueError, 
        msg = "Expected a Value error to be raised when setting transaction limit as -3000. Either no error or the incorrect error was raised."):
            self.account2.set_transaction_limit(-3000)

        #Testing for negative floating transaction limit
        with self.assertRaises(CustomValueError, 
        msg = "Expected a Value error to be raised when setting transaction limit as -0.01. Either no error or the incorrect error was raised."):
            self.account3.set_transaction_limit(-0.01)


    def test_is_banned(self):
        """
        3.8 Test is_banned()

        Testing the is_banned method of BankAccount class for both banned and unbanned accounts. 
        """
        #Banning account for test 
        self.account1.ban_account("Fraud")

        self.assertTrue(self.account1.is_banned(), 
        f"Incorrect implementation of account1.is_banned(), expected: True, received: {self.account1.is_banned()}")

        #Checking unbanned account
        self.assertFalse(self.account2.is_banned(), 
        f"Incorrect implementation of account1.is_banned(), expected: False, received: {self.account1.is_banned()}")

        #Checking ban + unban 
        BankAccount.unban_all()
        
        self.assertFalse(self.account1.is_banned(), 
        f"Incorrect implementation of account1.is_banned(), expected: False, received: {self.account1.is_banned()}")

    
    """ String representation test """
    def test_str_method(self):
        """
        3.9 Test formatting

        Testing formatting for BankAccount's string method
        """
        
        # Using example cases to check correct formatting
        # Standard account - A/C number starting from 1048, as 3 accounts have already been created
        account4 = BankAccount("RE", 1000)
        expected4 = "RE's account (1048): Balance=$1,049.99 | Limit=$N/A | Banned=No"
        self.assertEqual(expected4, str(account4), "Incorrect implentation of __str__ method for account4")

        # Account with transaction limit
        account5 = BankAccount("CC", 10**7)
        account5.set_transaction_limit(10)
        expected5 = "CC's account (1049): Balance=$10,000,049.99 | Limit=$10.00 | Banned=No"
        self.assertEqual(expected5, str(account5), "Incorrect implentation of __str__ method for account5")
        
        # Banned account
        account6 = BankAccount("Gary", 70.33)
        account6.ban_account("Suspicious activity")
        expected6 = "Gary's account (1050): Balance=$120.32 | Limit=$N/A | Banned=Yes | Ban Reason: Suspicious activity"
        self.assertEqual(expected6, str(account6), "Incorrect implentation of __str__ method for account6")
                

if __name__ == "__main__":
    unittest.main()