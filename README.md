# Portfolio
 Python project
 * Requirements: create a program that models a basic banking system
   * When prgram begins, it will load accounts data from multiple bank accounts
   * Once the accounts are loaded, user will be prompted to enter 4-digit PIN. Invalid PIN will cause to display error message and re-prompt a valid PIN, if invalid pin is entered over 3 times, program will exit; If user enters a valid PIN, The program will display related account information
   * After login to account, the program will prompt 4 options: option 1 for view balance, option 2 for make a deposit, option 3 for withdraw funds, option4 for return to main menu
 * Program design
   * Create a main module tha provides user the ability to login into account and perform banking operation
   * Create an Account Class that will be used to store account information
   * Create an ATM Class that will be used to provide the functionality required to perform banking operations
     * Class Attribute - savingsAccounts: a dictionary that holds multiple instances of the account class
     * Instance Method - makeDeposit: updates the account balance when user is logged into and returns the current account balance
     * Instance Method - makeWithdraw: updates the account balance the user is logged into and returns the current balance
     * Instance Method - viewAccountBalance: returns the account balance the user is logged into
     * Instance Method - loadAccounts: populates savingsAccounts dictionary with account instances
     * Instance Method - login: returns true or false.  If an account is associated with the PIN, returns true.  Otherwise, return false. 
  * Result: 
  Program was created with full described functions: login to bank account, view account informaiton, deposit funds and withdraw funds
 
 Data Hacking 
