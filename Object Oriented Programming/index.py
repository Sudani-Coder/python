# Python Object Oriented Programming
import datetime

class Employee:

    num_of_emps = 0 # Class Variable
    raise_amount = 1.04 # Class Variable

    def __init__(self, FirstName, LastName, salary):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = salary
        self.email = FirstName + "." + LastName + "@company.com"

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


print(Employee.num_of_emps)

emp_1 = Employee("sudani", "coder", 100000000)

print(Employee.num_of_emps)

emp_2 = Employee("Test", "User", 10000)

print(Employee.num_of_emps)

print(emp_1.email)
print(emp_1.FullName())
print(emp_1.salary)

emp_1.apply_raise()
print(emp_1.salary)

print(Employee.FullName(emp_2))
print(emp_2.salary)
Employee.apply_raise(emp_2)
print(emp_2.salary)

print(emp_1.__dict__)
print(Employee.__dict__)

Employee.set_raise_amount(1.06)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.apply_raise()
print(emp_1.salary)

emp_str_1 = "Sudani-Coder-91850"
emp_str_2 = "John-Doe-75500"
emp_str_3 = "Omer-Taha-83500"

new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.email)
print(new_emp_2.salary)

my_date = datetime.date.today()
print(Employee.is_workday(my_date))
