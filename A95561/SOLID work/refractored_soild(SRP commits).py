#Single Responsibility Principle (SRP):
#Each class should have a single, well-defined responsibility.
#Splitting Employee class into separate classes for Manager and Developer
class Manager:
    def __init__(self, name):
        self.name = name

    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer:
    def __init__(self, name):
        self.name = name

    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")
