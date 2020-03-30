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

dev_1 = Developer("Sudani", "Coder", 25000, ["HTML", "CSS", "JS", "PY", "SQL"])

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(dev_1.FullName()))
print("\n {}".format(dev_1.email))
print("\n {}".format(dev_1.salary))
print("\n {}".format(dev_1.prog_lang))

Developer.set_raise_amount(1.10)

print("\n {}".format(Employee.__dict__))
