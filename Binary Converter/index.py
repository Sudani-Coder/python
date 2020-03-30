## Project: 1
# Convert a Number into Binary, Octal and Hexadecimal

while True:
    try:
        dec_num = int(input("\n Enter the number: "))
        
        print("\n Binary value is {} ".format(bin(dec_num)))
        print("\n Octal value is {} ".format(oct(dec_num)))
        print("\n Hexadecimal value is {} ".format(hex(dec_num)))

    except ValueError as error:
        print("\n {}\n value error please enter a number.".format(error))
