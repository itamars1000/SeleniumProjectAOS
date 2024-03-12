# Class for all the functions that related to home page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook



class HomePage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.tests_file = load_workbook(filename="Tests.xlsx")
        self.wait = WebDriverWait(driver, 5)

    def get_categories_list(self):
        return self.driver.find_elements(By.CLASS_NAME, "categoryCell")

    def get_categories_element(self):
        return self.driver.find_element(By.CLASS_NAME, "categoryCell")

    def click_category(self, category):
        for cat in self.get_categories_list():
            if cat.text == category:
                cat.click()
                break
