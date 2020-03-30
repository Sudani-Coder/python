# Python Object Oriented Programming

class Employee:

    num_of_emps = 0 # Class Variable
    raise_amount = 1.02 # Class Variable

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

print("\n {}".format(Employee.__dict__))

print("\n Number of employee's {}.".format(Employee.num_of_emps))

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

print("\n {}".format(Employee.__dict__))
