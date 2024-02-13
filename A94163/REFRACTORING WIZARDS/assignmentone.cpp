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


/** 2.Descriptive Variable Names:**
Use descriptive names for variables and parameters to enhance code readability. 
For example, replace `amount` with `initialBalance` in the constructor.**/
  
   
   class BankAccount {
   public:
       BankAccount(double initialBalance) : balance(initialBalance) {}
       
       double getBalance() const { return balance; }
       void deposit(double amount) { balance += amount; }
       void withdraw(double amount) { balance -= amount; }
       
   private:
       double balance;
   };

   /**3.Code Formatting:
Maintain consistent and clear code formatting for better readability. Consider using indentation consistently, and surround binary operators with spaces.**/

   int main() {
       BankAccount account(1000);
       account.deposit(500);
       account.withdraw(200);
       cout << "Current balance: " << account.getBalance() << endl;
       return 0;
   }

/**4.Comments:
Add comments to explain complex logic or provide context where needed.**/

   // Example code for a simple bank account management system
   #include <iostream>
   using namespace std;

   class BankAccount {
   public:
       // Constructor with initial balance
       BankAccount(double initialBalance) : balance(initialBalance) {}
       
       // Accessor method to get the current balance
       double getBalance() const { return balance; }
       
       // Deposit money into the account
       void deposit(double amount) { balance += amount; }
       
       // Withdraw money from the account
       void withdraw(double amount) { balance -= amount; }
       
   private:
       double balance;
   };

   int main() {
       // Creating a BankAccount object with an initial balance of 1000
       BankAccount account(1000);
       
       // Depositing 500 into the account
       account.deposit(500);
       
       // Withdrawing 200 from the account
       account.withdraw(200);
       
       // Displaying the current balance
       cout << "Current balance: " << account.getBalance() << endl;
       return 0;
   }

