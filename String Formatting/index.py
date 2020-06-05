text = \
"""
    Hello World
    Welcome to python
    I love python prog lang
"""

print(f"\n{text}")

name = "Omer Taha"
age = 21
salary = 20000
MyMoney = 950925995915
MyComplexNumber = 5+6j
persons = [
    {
        "name": name,
        "age": age,
        "salary": salary,
    },
    {
        "name": "Sudani Coder",
        "age": 21,
        "salary": 50000,
    },
    {
        "name": ("Root", "Admin"),
        "age": 21,
        "salary": 50000,
    }
]

print("\nMy name is %s and i am %d year's old, My salary %.2f" %(name, age, salary))

print("\nMy name is {:s} and i am {:d} year's old, My salary {:.2f}".format(persons[1]["name"], persons[1]["age"], persons[1]["salary"]))

print("\nMy Money In Bank Account Is: {:,.2f}".format(MyMoney))

print(f"\nMy name is {name:s} and i am {age:d} year's old, My salary {salary:,.2f}")

print("\nReal Part Is: {}".format(MyComplexNumber.real))
print("Imaginary Part Is: {}".format(MyComplexNumber.imag))

a = {1, 2, 3, 4, 5, "A", "B", "C", "D", "E"}
print(f"\n{a}")
