myAdmins = ["Admin", "Root", "The User", "SuperVisor", "Omer Taha", "Super User", "Sudani Coder", "John Doe", "Ali Ahmed", "System Admin", "Root Admin", "Manager"]

print("\n")

for admin in myAdmins:
    print(admin, end = "    ")

print("\n")

i = 0
while i < len(myAdmins):
    print(f"#{str(i + 1).zfill(2)} {myAdmins[i]}", end = "\n\n")
    i += 1

else:
    print("All Admin's Printed To Screen.")
