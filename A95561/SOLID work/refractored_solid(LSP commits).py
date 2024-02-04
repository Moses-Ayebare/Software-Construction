#Liskov Substitution Principle (LSP):
#Subclasses should be substitutable for their base classes without altering program correctness.
# LSP: Ensuring Manager and Developer are substitutable for Employee
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def write_report(self):
        print(f"Manager Report: {self.name}")

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def calculate_bonus(self):
        return 500

    def write_report(self):
        print(f"Developer Report: {self.name}")

    def code_review(self):
        print(f"{self.name} is conducting a code review.")
