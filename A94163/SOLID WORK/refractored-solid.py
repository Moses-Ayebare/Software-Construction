from abc import ABC, abstractmethod

# Core class representing an employee with their name and role
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role