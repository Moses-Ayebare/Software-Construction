#Open-Closed Principle (OCP):
#Classes should be open for extension (adding new behavior) but closed for modification (changing existing behavior).
#Making Report class open for extension but closed for modification
class Report:
    def generate_report(self, employee):
        employee.write_report()

class Manager:
    def write_report(self):
        print(f"Manager Report: {self.name}")

class Developer:
    def write_report(self):
        print(f"Developer Report: {self.name}")
