import json
from urllib.request import urlopen

with urlopen("https://ipinfo.io") as response:
    source = response.read()

data = json.loads(source)

for key, value in data.items():
    print(f"{key} => {value}")
