## Project: 3
# Encryption using Dictionary
# i will develop my script by adding decrypthion key mother fuckers حطور الكود بتاعي من التشفير الى فك التشفير

keys = {
    "A":"E", "B":"F", "C":"G", "D":"H", "E":"I",
    "F":"J", "G":"K", "H":"L", "I":"M", "J":"N",
    "K":"O", "L":"P", "M":"Q", "N":"R", "O":"S",
    "P":"T", "Q":"U", "R":"V", "S":"W", "T":"X",
    "U":"Y", "V":"Z", "W":"A", "X":"B", "Y":"C",
    "Z":"D", " ":" "
}

message = input("Enter the message: ").upper()

def cipher(key , msg):
    encrypted = ""
    for letters in message:
        if letters in keys:
            encrypted += keys[letters]
        else:
            encrypted += letters
    return encrypted

print(cipher(keys, message))
