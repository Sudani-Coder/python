# Python Object Oriented Programming
import datetime

class Employee:

    num_of_emps = 0 # Class Variable
    raise_amount = 1.02 # Class Variable

    def __init__(self, FirstName, LastName, salary):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = int(salary)

        Employee.num_of_emps += 1 # Class Variable

    @property
    def email(self):
        return "{}.{}@email.com".format(self.FirstName, self.LastName)

    @property
    def FullName(self):
        return "{} {}".format(self.FirstName, self.LastName)

    @FullName.setter
    def FullName(self, name):
        FirstName, LastName = name.split(" ")
        self.FirstName = FirstName
        self.LastName = LastName

    @FullName.deleter
    def FullName(self):
        print("Delete Name!")
        self.FirstName = None
        self.LastName = None

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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.FirstName, self.LastName, self.salary)

    def __str__(self):
        return "{} - {}".format(self.FullName(), self.email)

    def __add__(self, other):
        return self.salary + other.salary
    
    def __len__(self):
        return len(self.FullName())

class Developer(Employee):

    def __init__(self, FirstName, LastName, salary, prog_lang):
        super().__init__(FirstName, LastName, salary)
        self.prog_lang = prog_lang
    
    @classmethod
    def from_string(cls, dev_str):
        first, last, salary, prog_lang = dev_str.split("-")
        return cls(first, last, salary, prog_lang)

class Manager(Employee):

    def __init__(self, FirstName, LastName, salary, employees = None):
        super().__init__(FirstName, LastName, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("\n --> {}".format(emp.FullName()))
