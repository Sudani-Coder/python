import requests
from bs4 import BeautifulSoup
from csv import writer

html_doc = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<meta name="description" content="Sudani Coder">
		<meta name="keywords" content="Sudani Coder">
		<meta name="author" content="Sudani Coder">
        <title>Sudani Coder</title>
    </head>
    <body>
        <h1 data-hello="hi">Hello World</h1>
        <h3>hello world, welcome to my python code!.</h3>
        <div id="div1">
            <div>
                <p>Lorem, ipsum dolor, sit amet consectetur adipisicing elit, Expedita reprehenderit esse quae, explicabo voluptatibus quisquam soluta exercitationem debitis!.</p>
            </div>
            <p class="para">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Reiciendis atque hic harum porro totam vero recusandae temporibus ipsa ea consectetur dolore officia.
                <br>
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem reprehenderit sint soluta, commodi et neque quaerat eum eius aspernatur accusamus eos accusantium voluptas ex.
            </p>
        </div>
        <p>hello world, welcome to my python code!, hello world from python code to the fucking world!.</p>
        <div id="div2">
            <p>
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Temporibus libero vero esse illum eos explicabo.
                <br>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Saepe, excepturi! Tempora perferendis vero totam accusantium.
            </p>
        </div>
        <div id="div3">
            <p class="para">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita reprehenderit esse quae, ea tenetur ab ratione. Excepturi tempora quasi.
                <br>
                hello world from python code to the fucking world!.
            </p>
        </div>
    </body>
</html>
"""

url = "https://webscraper.io/test-sites/e-commerce/allinone"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
products = soup.findAll(class_="caption")

with open("output.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["Title", "Link", "Price", "Description"]
    csv_writer.writerow(headers)

    for product in products:
        Title = product.find(class_="title").get_text().replace("\n", "").strip()
        Link = product.find("a")["href"]
        Price = product.select(".price")[0].get_text()
        Description = product.find(class_="description").get_text().replace("\n", "").strip()
        csv_writer.writerow([Title, Link, Price, Description])

# soup = BeautifulSoup(html_doc, "html.parser")

# Direct
# print(soup.head)
# print(soup.body)
# print(soup.head.title)

# find()
# el = soup.find("div")

# find_all() or findAll()
# el = soup.findAll("div")
# el = soup.findAll("div")[2]

# el = soup.find(id="div2")
# el = soup.find(class_="para")
# el = soup.find(attrs={"data-hello": "hi"})

# Select
# el = soup.select("#div3")
# el = soup.select(".para")
# el = soup.select(".para")[1]

# get_text()
# el = soup.find(class_"para").get_text()

# for item in soup.select(".para"):
#     print(item.get_text())

# Navigation
# el = soup.body.contents[3].find_next_sibling()
# el= soup.find(id="div2").find_previous_sibling()
# el = soup.find(class_="para").find_parent()
# el = soup.find("h1").find_next_sibling()
# el = soup.find("h3").find_next_sibling("p")
