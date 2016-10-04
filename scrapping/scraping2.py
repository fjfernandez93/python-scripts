from bs4 import BeautifulSoup
import re
html = open("livescore.html", "r")
soup = BeautifulSoup(html, "html.parser")

tag_l = soup.find_all("div",{"data-id":re.compile("^soccer")})



for tag in tag_l:
    tupla = (tag.find("div",{"class":"ply tright name"}).text.encode('UTF-8'),
    tag.find("div",{"class":"ply name"}).text.encode('UTF-8'),
    tag.find("span",{"class":"hom"}).text.encode('UTF-8'),
    tag.find("span",{"class":"awy"}).text.encode('UTF-8'))

    print tupla
