import re

pattern = r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)"

string = "https://www.sudanicoder.com:8080/category.py?article=105?name=how-to-do"

search = re.search(pattern, string)

print(search.group(), end = "\n\n")

print(search.groups(), end = "\n\n")

for group in search.groups():
    print(group)

print()
print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")
