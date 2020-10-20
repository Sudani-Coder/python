import os

# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

file = open(r"test\nfiles\elzero.txt")
