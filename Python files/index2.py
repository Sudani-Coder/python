import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

myFile = open(r"test\nfiles\fun.txt", "w")

myFile.write("Hello World, Welcome To My Text File From Python Script.\n" * 10)

myFile.close()

myFile = open(r"test\nfiles\names.txt", "w")

myNames = ["Sudani Coder\n", "Omer Taha\n", "Super User\n", "Root Admin\n"]

myFile.writelines(myNames)

myFile.close()

myFile = open(r"test\nfiles\names.txt", "a")

i = 0
for line in range(10):
    myFile.write(f"0{i} Hello World\n")
    i += 1

myFile.close()
