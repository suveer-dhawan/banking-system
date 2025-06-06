"""
This file contains custom errors that have been created for the purpose of testing 
the bank account system. 
"""

class CustomValueError(Exception):
    """
    This error should be raised when the value isn't what its expected to be.
    """
    pass

class CustomTypeError(Exception):
    """
    This error should be raised when the type of the value isn't what its expected to be.
    """
    pass

class CustomAttributeError(Exception):
    """
    This error should be raised when the attribute doesn't exist as expected
    """
    pass

class CustomKeyError(Exception):
    """
    This error should be raised when a key is expected to exist in a dictionary but doesn't exist.
    """
    pass

class CustomOperationError(Exception):
    """
    Raised when an operation is not allowed (e.g., on a banned account).
    """
    pass

class CustomLimitError(Exception):
    """
    Raised when a transaction exceeds the allowed limit.
    """
    pass