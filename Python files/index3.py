import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

myFile = open(r"test\nfiles\text.txt", "r")

# myFile.truncate(5)
# print(myFile.tell())
# myFile.seek(13)
# print(myFile.read())

# myFile.close()

# os.remove(r"test\nfiles\text.txt")
