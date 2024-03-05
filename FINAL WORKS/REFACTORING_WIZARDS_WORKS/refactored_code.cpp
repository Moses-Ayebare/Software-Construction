#include <iostream>
#include <stdexcept> // Include the necessary header for exception handling
using namespace std;

class BankAccount {
public:
    // Constructor with optional initial balance
    BankAccount(double initialBalance = 0.0) : balance(initialBalance) {}
    
    // Accessor method to get the current balance
    double getBalance() const { return balance; }
    
    // Deposit money into the account
    void deposit(double amount) {
        // Check for invalid deposit amount (non-positive) 
        if (amount <= 0) {
            throw invalid_argument("Deposit amount must be positive.");
        }
        balance += amount;
    }
    
    // Withdraw money from the account
    void withdraw(double amount) { 
        // Check for invalid withdrawal amount (non-positive) 
        if (amount <= 0) {
            throw invalid_argument("Withdrawal amount must be positive.");
        }
        // Check if the funds are enough 
        if (amount > balance) {
            throw runtime_error("Insufficient funds for withdrawal.");
        }
        // Subtract the amount
        balance -= amount;
    }
    
private:
    double balance; // Tracks the account balance
};

int main() {
    // Creating a BankAccount object with an initial balance of 1000
    BankAccount account(1000.0);
    
    // Depositing 500 into the account
    account.deposit(500.0);
    
    // Withdrawing 200 from the account
    account.withdraw(200.0);
    
    // Displaying the current balance
    cout << "Current balance: " << account.getBalance() << endl;
    return 0;
}
