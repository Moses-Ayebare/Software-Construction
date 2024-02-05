from abc import ABC, abstractmethod

# Core class representing an employee with their name and role
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Abstract base class outlining the protocol for crafting reports
class ReportWriter(ABC):
    @abstractmethod
    def craft_report(self, employee):
        pass

# Abstract base class defining the protocol for bonus calculation
class BonusCalculator(ABC):
    @abstractmethod
    def calculate_incentive(self, employee):
        pass

# Report craft made for Managers
class ManagerReportWriter(ReportWriter):
    def craft_report(self, manager):
        print(f"Manager's Report: {manager.name}")

# Report craft made for Developers
class DeveloperReportWriter(ReportWriter):
    def craft_report(self, developer):
        print(f"Developer's Report: {developer.name}")

# Bonus calculation incentive for Managers
class ManagerBonusCalculator(BonusCalculator):
    def calculate_incentive(self, manager):
        return 1000

# Bonus calculation incentive for Developers
class DeveloperBonusCalculator(BonusCalculator):
    def calculate_incentive(self, developer):
        return 500
    
# Abstract class defining the responsibilities
class ManagerialRole(ABC):
    @abstractmethod
    def lead_team(self):
        pass

# Abstract class defining the developer responsibilities
class DeveloperRole(ABC):
    @abstractmethod
    def conduct_code_review(self):
        pass

# Implementation of a Manager with specific leadership actions
class Manager(Employee, ManagerialRole):
    def lead_team(self):
        print(f"{self.name} is guiding the team with authority.")

# Implementation of a Developer with specific code review actions
class Developer(Employee, DeveloperRole):
    def conduct_code_review(self):
        print(f"{self.name} is orchestrating a comprehensive code review.")

if __name__ == "__main__":
    # Creating instances of Manager and Developer
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    # Creating instances of report writers and bonus calculators for each role
    manager_report_writer = ManagerReportWriter()
    developer_report_writer = DeveloperReportWriter()
    manager_bonus_calculator = ManagerBonusCalculator()
    developer_bonus_calculator = DeveloperBonusCalculator()

    # Generating unique reports for Manager and Developer
    manager_report_writer.craft_report(manager)
    developer_report_writer.craft_report(developer)
