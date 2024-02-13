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


// Proper code following the proper principles
/** 1. Consistent Naming Conventions:
Ensure that naming conventions are consistent. For instance, consider using camelCase for member variables and functions, 
and capitalize the first letter of class names.**/
  
   
   class BankAccount {
   public:
       BankAccount(double initialBalance) : balance(initialBalance) {}
       
       double getBalance() const { return balance; }
       void deposit(double amount) { balance += amount; }
       void withdraw(double amount) { balance -= amount; }
       
   private:
       double balance;
   };

   
