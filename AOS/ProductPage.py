# Class for all the functions that related to product page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Product_Page:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.tests_file = load_workbook(filename="Tests.xlsx")
        self.action_chain = ActionChains(self.driver)

    def change_quantity(self, num):
        quan = self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")
        quan.send_keys(Keys.BACKSPACE, num)

    def click_add_to_cart(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']")
        button.click()

    def color_list(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='productProperties']/div[1]/div[1]/span")

    def get_product_color(self, color):
        return self.driver.find_element(By.CSS_SELECTOR, f"[title='{color}'][id='rabbit']")

    def click_color(self, color):
        if len(self.color_list()) > 1:
            self.get_product_color(color).click()

    def get_product_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='Description']/h2")

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, "//*[@id='Description']/h1")

    def get_product_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")
