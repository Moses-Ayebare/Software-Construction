# DIP: Introducing abstraction to separate Report from employee classes
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bonus(self):
        pass

    @abstractmethod
    def write_report(self):
        pass

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

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

    def write_report(self):
        print(f"Developer Report: {self.name}")
