# ISP: Creating separate interfaces for Manager and Developer
class Manager:
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

    def write_report(self):
        print(f"Manager Report: {self.name}")

class Developer:
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

    def write_report(self):
        print(f"Developer Report: {self.name}")
