# Class for all the functions that general on the website and all general processes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
from HomePage import HomePage
from CategoryPage import Category_Page
from ProductPage import Product_Page


class General:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.home_page = HomePage(self.driver)
        self.category_Page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.tests_file = load_workbook(filename="Tests.xlsx")
        self.tf = self.tests_file['tests']

    def logo_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='logo']").click()
        self.wait.until(EC.visibility_of(self.home_page.get_categories_list()[1]))

    def add_product_to_cart(self, cat, item, quan, color):
        self.home_page.click_category(cat)
        self.category_Page.click_product(item)
        self.product_page.change_quantity(quan)
        self.product_page.click_color(color)
        self.product_page.click_add_to_cart()

    def get_cart_icon(self):
        return self.driver.find_element(By.ID, "menuCart")

    def click_on_cart(self):
        self.get_cart_icon().click()

    def get_account_icon(self):
        return self.driver.find_element(By.ID, "menuUserLink")

    def click_account_icon(self):
        self.get_account_icon().click()

    def click_my_orders(self):
        self.driver.find_element(By.XPATH, "//*[@id='menuUserLink']/div/label[2]").click()

    def get_my_account(self):
        return self.driver.find_element(By.XPATH, "//*[@id='menuUserLink']/div[1]/label[1]")

    def get_order_number(self):
        return self.driver.find_element(By.XPATH, "//*[@id='myAccountContainer']/div/table/tbody/tr[2]/td[1]")

    def enter_username_sign_in(self, un):
        username = self.driver.find_element(By.CSS_SELECTOR, "[name='username']")
        username.send_keys(un)

    def enter_password_sign_in(self, pw):
        password = self.driver.find_element(By.CSS_SELECTOR, "[name='password']")
        password.send_keys(pw)

    def sign_in(self, un, pw):
        self.click_account_icon()
        self.enter_username_sign_in(un)
        self.enter_password_sign_in(pw)
        self.driver.find_element(By.ID, "sign_in_btn").click()
        self.wait.until(EC.visibility_of(self.driver.find_element(By.CLASS_NAME, "categoryCell")))

    def get_connect_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']")

    def get_log_in_window_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='login ng-scope']")

    def sign_out(self):
        self.click_account_icon()
        self.driver.find_element(By.XPATH, "//*[@id='menuUserLink']/div/label[3]").click()

    def get_delete_button(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteBtnText")

    def delete_account(self):
        self.click_account_icon()
        self.wait.until(EC.visibility_of(self.get_my_account()))
        self.get_my_account().click()
        self.wait.until(EC.visibility_of(self.get_delete_button()))
        self.get_delete_button().click()
        self.wait.until(EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, "[class='deletePopupBtn deleteRed']")))
        self.driver.find_element(By.CSS_SELECTOR, "[class='deletePopupBtn deleteRed']").click()
        print('Deleted successfully')
