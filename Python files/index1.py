import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

myFile = open(r"test\nfiles\elzero.txt", "r")

# print(f"\n- {myFile} ")
# print(f"\n- {myFile.name} ")
# print(f"\n- {myFile.mode} ")
# print(f"\n- {myFile.encoding} ")

# print(f"\n{myFile.read()}")
# print(myFile.readline())
# print(myFile.readline())
# print(myFile.readlines())

for line in myFile:
    print(line)

myFile.close()
