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

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("\n --> {}".format(emp.FullName()))

print("\n {}".format(Employee.__dict__))

print("\n {}".format(Developer.__dict__))

dev_1 = Developer("Sudani", "Coder", 25000, ["HTML", "CSS", "JS", "PY", "SQL"])

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(dev_1.FullName()))
print("\n {}".format(dev_1.email))
print("\n {}".format(dev_1.salary))
print("\n {}".format(dev_1.prog_lang))

Developer.set_raise_amount(1.10)
dev_1.apply_raise()

dev_str = "Super-User-1000-bash"
new_dev = Developer.from_string(dev_str)

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(Developer.FullName(new_dev)))
print("\n {}".format(new_dev.email))
print("\n {}".format(new_dev.salary))
print("\n {}".format(new_dev.prog_lang))

new_dev.apply_raise()
print("\n {}".format(new_dev.salary))

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(Manager.FullName(mgr_1)))
print("\n {}".format(mgr_1.email))
print("\n {}".format(mgr_1.salary))
mgr_1.print_emps()

mgr_1.add_emp(new_dev)

mgr_1.print_emps()

mgr_1.remove_emp(new_dev)

mgr_1.print_emps()

print("\n {}".format(Employee.__dict__))
