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
