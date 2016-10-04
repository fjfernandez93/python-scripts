# from bs4 import BeautifulSoup
# import requests
#
#
# req = requests.get("http://www.livescore.com/soccer/spain/primera-division/#/round-1")
#
# if(req.status_code==200):
#
#     soup=BeautifulSoup(req.text,"html.parser")
#     lista=soup.findAll("div",{"data-type":"evt"})
#     print lista

import mechanize
from bs4 import BeautifulSoup
url = "http://www.livescore.com/soccer/spain/primera-division/#/round-1"
br = mechanize.Browser()
data = br.open(url).get_data()

soup=BeautifulSoup(data,"html.parser")
lista=soup.findAll("div",{"data-type":"evt"})
print lista
