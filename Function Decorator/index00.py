from time import time

def speed_Test(func):
    def wrapper():
        start = time()
        func()
        end = time()

        print(f"Function Run Time is ==> {end - start}")
    
    return wrapper

@speed_Test
def bigLoop():
    for number in range(20000):
        print(number)

bigLoop()
