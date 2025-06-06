# 🏦 Robust Banking System & Unit Testing Suite 🏦

This repository showcases a foundational Python-based banking system, meticulously engineered for precision and reliability, coupled with a comprehensive unit testing module. Developed with an emphasis on **defensive programming, assertive logic, and rigorous test coverage**, this project demonstrates critical software development practices essential for financial applications.

---
## Table of Contents

* [Project Overview](#project-overview)
* [Key Features & Design Principles](#key-features--design-principles)
    * [Core Banking Logic (`bank.py`)](#core-banking-logic-bankpy)
    * [Comprehensive Unit Testing (`testing_module.py`)](#comprehensive-unit-testing-testing-modulepy)
    * [Custom Error Handling (`custom_errors.py`)](#custom-error-handling-custom-errorspy)
* [Technical Implementation Highlights](#technical-implementation-highlights)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation & Setup](#installation--setup)
    * [Running the Tests](#running-the-tests)
* [File Structure](#file-structure)
* [Author](#author)

---
## Project Overview

This project simulates a basic bank account management system, embodying core principles of financial software development: **correctness, safety, and auditability**. It is built upon a robust `BankAccount` class designed to handle deposits, withdrawals, and transfers, complete with features like transaction limits and account banning. A dedicated unit testing module provides exhaustive validation, ensuring the system's integrity under both normal and edge-case scenarios. This dual focus on **resilient implementation** and **rigorous testing** is paramount in high-stakes environments like investment banking and quantitative finance.

---
## Key Features & Design Principles

The project is structured to demonstrate best practices in building reliable systems:

### Core Banking Logic (`bank.py`)

The `BankAccount` class is the heart of the system, featuring:

* **Unique Account Identification:** Each account receives a unique, sequential `account_number`, starting from a specified base (`1045`).
* **Initial Account Bonus:** Accounts are initialized with a non-negative balance and an automatic bonus (`$49.99`), demonstrating initial state management and extensibility for various product offerings (via potential subclasses).
* **Fundamental Transaction Operations:** `deposit()`, `withdraw()`, and `transfer_to()` methods handle funds movement.
* **Transaction Limits:** `set_transaction_limit()` allows for setting maximum amounts for withdrawals/transfers, preventing excessive individual transactions.
* **Account Banning:** `ban_account()` and `unban_all()` provide mechanisms to flag accounts for suspicious activity or audit, restricting all financial operations.
* **Defensive Programming:** Extensive input validation (type checking, non-negativity checks) is implemented to prevent invalid operations and ensure data integrity. Custom errors are raised for invalid inputs or restricted actions.
* **Assertions for Logic Integrity:** Internal `assert` statements are strategically used to validate assumptions about the system's state during development and debugging, ensuring the logic remains "airtight."

### Comprehensive Unit Testing (`testing_module.py`)

A dedicated module leverages Python's `unittest` framework to provide:

* **Full Method Coverage:** Test cases written for every public method of the `BankAccount` class.
* **Positive Case Validation:** Verifies correct balance updates and state changes for valid deposits, withdrawals, and transfers.
* **Negative Case & Edge Case Handling:** Rigorous testing of invalid inputs (e.g., negative amounts, incorrect types, insufficient funds, exceeding transaction limits), ensuring the system fails gracefully and raises appropriate custom errors.
* **Banning Functionality Validation:** Tests confirm that banned accounts correctly restrict operations and that `unban_all` functions as expected.
* **Assertions in Tests:** Utilizes `assertEqual`, `assertRaises`, and other `unittest` assertions to provide clear, automated verification of expected outcomes.

### Custom Error Handling (`custom_errors.py`)

A separate module defines custom exceptions (e.g., `InvalidAmountError`, `InsufficientFundsError`, `BannedAccountError`). These ensure:

* **Granular Error Reporting:** Specific and meaningful error messages are provided for different failure conditions.
* **Improved Debugging & User Feedback:** Developers and higher-level applications can easily interpret and handle specific error types.
* **System Robustness:** Prevents unexpected program termination due to common invalid scenarios.

---
## Technical Implementation Highlights

* **Object-Oriented Design:** The `BankAccount` class encapsulates account data and behavior, promoting modularity and maintainability.
* **Global State Management:** `set_next_account_number()` and `unban_all()` (class methods) demonstrate controlled modification of global state, particularly useful for test setup and teardown.
* **Strict Type & Value Validation:** Input parameters for all methods undergo stringent checks, a cornerstone of reliable financial systems.
* **Clear Separation of Concerns:** Core banking logic is isolated in `bank.py`, custom error definitions in `custom_errors.py`, and testing in `testing_module.py`.

---
## Getting Started

To explore or extend this banking system, follow these steps.

### Prerequisites

* Python 3.x

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/suveer-dhawan/banking-system.git](https://github.com/suveer-dhawan/banking-system.git)
    cd banking-system
    ```

### Running the Tests

To verify the system's correctness and robustness, execute the unit tests:

```bash
python -m unittest testing_module.py
```
This command will run the entire suite of tests defined in ```testing_module.py``` and report any failures, providing confidence in the banking logic.
---
## File Structure

The project has a straightforward and organized file structure:
```
.
├── bank.py                     # Core BankAccount class and logic
├── custom_errors.py            # Custom exception definitions
├── testing_module.py           # Comprehensive unit test suite
└── README.md                   # This documentation file
```
---

## Author

* **Suveer Dhawan** - [GitHub Profile](https://github.com/suveer-dhawan)