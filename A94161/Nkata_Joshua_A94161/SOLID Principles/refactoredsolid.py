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