# Python Object Oriented Programming

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
