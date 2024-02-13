//ORIGINAL WRONG CODE
// Example code for bank account management system
#include <iostream>
using namespace std;

class BankAccount {
public:
    BankAccount(double balance) : balance(balance) {}
    
    double getBalance() const { return balance; }
    void deposit(double amount) { balance += amount; }
    void withdraw(double amount) { balance -= amount; }
    
private:
    double balance;
};

int main() {
    BankAccount account(1000);
    account.deposit(500);
    account.withdraw(200);
    cout << "Current balance: " << account.getBalance() << endl;
    return 0;

    
