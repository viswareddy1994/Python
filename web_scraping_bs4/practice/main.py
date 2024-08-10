import os
from bs4 import BeautifulSoup

script_file = os.path.dirname(__file__)
file_path = os.path.join(script_file,"website.html")


with open(file_path,"r",encoding="utf-8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a.get("href")) 
# -- Anchor tags 

# to get all items use find_all menthod
#use find method to get first item 
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1",id="name")
print(heading)

# for class you need to use "class_"
section_heading = soup.find(name="h3",class_="heading")
print(section_heading.get("class"))

# we can drill down to get perticular element just like css selectors using select or select_one methods
# to select an id we use #id_name and for class we use ".classname"

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one(selector="#name")
print(name)

# get all headings we are using select method
headings = soup.select(selector=".heading")
print(headings)
