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