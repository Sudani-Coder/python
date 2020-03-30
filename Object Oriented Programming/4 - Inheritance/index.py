# Python Object Oriented Programming
import datetime

class Employee:

    num_of_emps = 0 # Class Variable
    raise_amount = 1.02 # Class Variable

    def __init__(self, FirstName, LastName, salary):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = int(salary)
        self.email = FirstName + "." + LastName + "@email.com"

        Employee.num_of_emps += 1 # Class Variable

    def FullName(self):
        return "{} {}".format(self.FirstName, self.LastName)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split("-")
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

class Developer(Employee):
    def __init__(self, FirstName, LastName, salary, prog_lang):
        super().__init__(FirstName, LastName, salary)
        self.prog_lang = prog_lang
