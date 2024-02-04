#Single Responsibility Principle (SRP)
class ReportWriter:
    def write_report(self, employee):
        pass

class ManagerReportWriter(ReportWriter):
    def write_report(self, manager):
        print(f"Manager Report: {manager.name}")

class DeveloperReportWriter(ReportWriter):
    def write_report(self, developer):
        print(f"Developer Report: {developer.name}")

# Open/Closed Principle (OCP)
class ReportContext:
    def __init__(self, report_writer):
        self.report_writer = report_writer

    def generate_report(self, employee):
        self.report_writer.write_report(employee)

#3: Liskov Substitution Principle (LSP)
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_bonus(self):
        pass

#4: Interface Segregation Principle (ISP)
class ManagerInterface:
    def manage_team(self):
        pass

class DeveloperInterface:
    def code_review(self):
        pass

#5: Dependency Inversion Principle (DIP)
class BonusCalculatorInterface:
    def calculate_bonus(self, employee):
        pass

class Manager(Employee, ManagerInterface, BonusCalculatorInterface):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee, DeveloperInterface, BonusCalculatorInterface):
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

if __name__ == "__main__":
    #Manager and Developer instances
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    #ReportContext with ManagerReportWriter
    manager_report_context = ReportContext(ManagerReportWriter())

    #  Manager Report
    manager_report_context.generate_report(manager)

    # ReportContext with DeveloperReportWriter
    developer_report_context = ReportContext(DeveloperReportWriter())

    #  Developer Report
    developer_report_context.generate_report(developer)

    #BonusCalculator instance
    bonus_calculator = BonusCalculatorInterface()

    # Manager and Developer Bonuses
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)