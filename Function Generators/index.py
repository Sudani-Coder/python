def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

myGen = myGenerator()

for num in myGen:
    print(num)
