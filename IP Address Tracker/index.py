## project: 10
# Tracing IP Address
import requests

res = requests.get("https://ipinfo.io")
data = res.json()

"""
print("\n", res.text, end = "\n\n")
print(data, end = "\n\n")

print(type(res.text), end = "\n\n")
print(type(data), end = "\n\n")
"""

print("\nThe IP Address Is --> {}".format(data["ip"]), end = "\n\n")
print("The City Is --> {}".format(data["city"]), end = "\n\n")
print("The Region Is --> {}".format(data["region"]), end = "\n\n")
print("The Country Is --> {}".format(data["country"]), end = "\n\n")
print("The Internet Service Provider Is --> {}".format(data["org"]), end = "\n\n")
print("The location Is --> {}".format(data["loc"]), end = "\n\n")

location = data["loc"].split(",")
lattitude = location[0]
longitude = location[1]

print("The Lattitude Is --> {}".format(lattitude), end = "\n\n")
print("The Longitude Is --> {}".format(longitude), end = "\n\n")