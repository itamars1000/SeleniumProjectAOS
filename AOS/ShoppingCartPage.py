# Class for all the functions that related to shopping cart page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ShoppingCartPage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_checkout_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='shoppingCart']/table/tfoot/tr[1]/td[2]/span[2]")

    def edit_list(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='shoppingCart']/table/tbody/tr/td[6]/span[1]/a[1]")

    def quantities_list(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='shoppingCart']/table/tbody/tr/td[5]/label[2]")
