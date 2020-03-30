# Python Object Oriented Programming
import datetime

class Employee:

    num_of_emps = 0 # Class Variable
    raise_amount = 1.02 # Class Variable

    def __init__(self, FirstName, LastName, salary):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = int(salary)
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

print("\n {}".format(Employee.__dict__))

emp_1 = Employee("John", "Doe", 2500)

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(emp_1.FullName()))
print("\n {}".format(emp_1.email))
print("\n {}".format(emp_1.salary))

print("\n {}".format(emp_1.__dict__))

emp_2 = Employee("Test", "User", 5000)

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(Employee.FullName(emp_2)))
print("\n {}".format(emp_2.email))
print("\n {}".format(emp_2.salary))

emp_2.apply_raise()
print("\n {}".format(emp_2.salary))

print("\n {}".format(emp_2.__dict__))

emp_3 = Employee("Null", "None", 10000)

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(Employee.FullName(emp_3)))
print("\n {}".format(emp_3.email))
print("\n {}".format(emp_3.salary))

Employee.apply_raise(emp_3)
print("\n {}".format(emp_3.salary))

print("\n {}".format(emp_3.__dict__))

emp_4 = Employee("Root", "Admin", 15000)

print("\n Number of employee's {}.".format(Employee.num_of_emps))

print("\n {}".format(Employee.FullName(emp_4)))
print("\n {}".format(emp_4.email))
print("\n {}".format(emp_4.salary))

Employee.set_raise_amount(1.04)
Employee.apply_raise(emp_4)
print("\n {}".format(emp_4.salary))

print("\n {}".format(emp_4.__dict__))

emp_str = "Expert-Coder-20000"
new_emp = Employee.from_string(emp_str)

print("\n {}".format(Employee.FullName(new_emp)))
print("\n {}".format(new_emp.email))
print("\n {}".format(new_emp.salary))

Employee.set_raise_amount(1.05)
Employee.apply_raise(new_emp)
print("\n {}".format(new_emp.salary))

my_date = datetime.date.today()
print("\n Yes it is work day {}".format(Employee.is_workday(my_date)))

print("\n {}".format(new_emp.__dict__))

print("\n {}".format(Employee.__dict__))
