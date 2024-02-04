#Create a reportwriter interface
class ReportWriter:
    def write_repor(self, employee):
        pass

#MangerReportWriter class
class ManagerReportWriter(ReportWriter):
    def write_report(self, manager):
        print(f"Manager Report: {manager.name}")