# Python Object Oriented Programming

class Employee:

    def __init__(self, FirstName, LastName, salary):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = salary
        self.email = FirstName + "." + LastName + "@company.com"

    def FullName(self):
        return "{} {}".format(self.FirstName, self.LastName)

emp_1 = Employee("sudani", "coder", 100000000)
emp_2 = Employee("Test", "User", 10000)

print(emp_1.FullName())