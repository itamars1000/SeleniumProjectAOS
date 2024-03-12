# Class for all the functions that related to create account
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class CreateAccountPage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def enter_username(self, uname):
        username = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username.send_keys(uname)

    def enter_email(self, em):
        email = self.driver.find_element(By.NAME, "emailRegisterPage")
        email.send_keys(em)

    def enter_password(self, pw):
        password = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password.send_keys(pw)

    def enter_confirm_password(self, pw, cpw):
        if cpw != pw:
            raise Exception("Confirm password must be equal to password")
        c_password = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        c_password.send_keys(cpw)

    def get_agree_terms(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#formCover > sec-view > div > input")

    def click_register(self):
        self.driver.find_element(By.ID, "register_btn").click()

    def create_account(self, un, email, pw, cpw):
        self.enter_username(un)
        self.enter_email(email)
        self.enter_password(pw)
        self.enter_confirm_password(cpw, pw)
        self.get_agree_terms().click()
        self.click_register()
