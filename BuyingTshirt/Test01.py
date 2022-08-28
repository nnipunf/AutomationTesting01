from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Fire_fox_WDM():
    def firefox_launch(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


obj = Fire_fox_WDM()
obj.firefox_launch()