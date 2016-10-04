from contextlib import closing
from selenium.webdriver import Chrome # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup




with closing(Chrome()) as browser:
    url = "http://www.livescore.com/soccer/spain/primera-division/#/round-4"
    browser.get(url)
    # wait for the page to load
    WebDriverWait(browser, timeout=10)
    page_source = browser.page_source
    nuevo = page_source.encode('UTF-8')
    print nuevo
    html = open("livescore.html", "r")
    soup = BeautifulSoup(html, "html.parser")
