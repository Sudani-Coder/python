theName = input("\nWhat\'s your name? ").strip().capitalize()
theEmail = input("\nPlease enter your email address --> ").strip()

theUserName = theEmail[:theEmail.index('@')]
theWebsite = theEmail[theEmail.index('@') + 1:]

print(f"\nHello {theName} your email is {theEmail}")
print(f"\nYour username is {theUserName} and your website is {theWebsite}")
print()
