# Python Object Oriented Programming

class Employee:

    def __init__(self, FirstName, LastName, salary):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = salary
        self.email = FirstName + "." + LastName + "@company.com"

    def FullName(self):
        return "{} {}".format(self.FirstName, self.LastName)

print("\n {}".format(Employee.__dict__))

emp_1 = Employee("John", "Doe", 2500)

print("\n {}".format(emp_1.FullName()))
print("\n {}".format(emp_1.email))
print("\n {}".format(emp_1.salary))

print("\n {}".format(emp_1.__dict__))

print("\n {}".format(Employee.__dict__))
