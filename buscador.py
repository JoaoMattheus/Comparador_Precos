from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import path
from os import getcwd

class Buscador:
    def __init__(self):
        # Salvando as Informações do navegador
        self.driver = webdriver.Chrome('./drive/chromedriver.exe')
        self.driver.maximize_window()
    
    def buscaPreco(self, link, xpath):
        self.link = link
        self.xpath = xpath
        self.driver.get(self.link)
        self.driver.set_page_load_timeout(20)
        self.preco = self.driver.find_element_by_xpath(self.xpath).text
        return self.preco

    def fechar(self):
        self.driver.quit()