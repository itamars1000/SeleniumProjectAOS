# Class for all the functions that related to CATEGORY PAGE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import load_workbook


class Category_Page:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.tests_file = load_workbook(filename="Tests.xlsx")

    def get_product_list(self, id):
        return self.driver.find_element(By.CSS_SELECTOR, f"[id='{id}']")

    def click_product(self, id):
        self.get_product_list(id).click()

    def get_title_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, "body > div.uiview.ng-scope > section > article > h3")
