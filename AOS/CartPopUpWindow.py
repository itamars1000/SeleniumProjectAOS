# Class for all the functions that related to the pop-up cart window
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPopUpWindow:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_total_items(self):
        self.wait_popup()
        return self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/table/tfoot/tr/td/span/label")

    def wait_popup(self):
        self.wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/table/tfoot/tr/td/span/label")))

    def get_product_name_from_popup(self):
        self.wait_popup()
        return self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/table/tbody/tr[1]/td[2]/a/h3")

    def get_product_quantity_from_popup(self):
        self.wait_popup()
        return self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/table/tbody/tr[1]/td[2]/a/label[1]")

    def get_product_color_from_popup(self):
        self.wait_popup()
        return self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/table/tbody/tr[1]/td[2]/a/label[2]")

    def get_product_price_from_popup(self):
        self.wait_popup()
        return self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/table/tbody/tr[1]/td/p")

    def remove_last_product(self):
        self.wait_popup()
        self.driver.find_element(By.CSS_SELECTOR, "#product > td:nth-child(3) > div > div").click()

    def cart_popup_product_list(self):
        self.wait_popup()
        return self.driver.find_elements(By.XPATH, "//*[@id='toolTipCart']/div/table/tbody/tr")

    def click_checkout(self):
        self.wait_popup()
        self.driver.find_element(By.ID, "checkOutPopUp").click()

    def empty_cart_message(self):
        return self.driver.find_element(By.XPATH, "//*[@id='toolTipCart']/div/div/label[2]")