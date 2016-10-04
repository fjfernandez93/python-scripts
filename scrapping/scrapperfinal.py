from contextlib import closing
from selenium.webdriver import Chrome # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re



with closing(Chrome()) as browser:

    for i in range(1,7):

        url = "http://www.livescore.com/soccer/spain/primera-division/#/round-" + str(i)
        browser.get(url)
        # wait for the page to load
        WebDriverWait(browser, timeout=20)
        page_source = browser.page_source
        html = page_source.encode('UTF-8')
        soup = BeautifulSoup(html, "html.parser")

        tag_l = soup.find_all("div",{"data-id":re.compile("^soccer")})



        for tag in tag_l:
            tupla = (tag.find("div",{"class":"ply tright name"}).text.encode('UTF-8'),
            tag.find("div",{"class":"ply name"}).text.encode('UTF-8'),
            tag.find("span",{"class":"hom"}).text.encode('UTF-8'),
            tag.find("span",{"class":"awy"}).text.encode('UTF-8'))

            print tupla
        print "#############"
