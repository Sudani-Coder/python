## project: 7
# fahrenheit to celsius converter

fahrenheit = int(input("Enter a temperature in Fahrenheit --> "))

def calc(fahrenheit):
    return (fahrenheit - 32) * (5.0 / 9.0)

celsius = calc(fahrenheit)

print("Temperature: {} fahrenheit = {} celsius".format(fahrenheit, celsius))