# Class for all the functions that related to payment with Credit Card or Safe Pay
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OrderPaymentPage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def get_registration_button(self):
        return self.driver.find_element(By.ID, "registration_btn")

    def click_registration(self):
        self.get_registration_button().click()

    def get_next_button(self):
        return self.driver.find_elements(By.ID, "next_btn")[0]

    def click_next(self):
        self.get_next_button().click()

    def enter_safe_pay_username(self, un):
        username = self.driver.find_element(By.NAME, "safepay_username")
        username.send_keys(un)

    def enter_safe_pay_password(self, pw):
        password = self.driver.find_element(By.NAME, "safepay_password")
        password.send_keys(pw)

    def click_pay_now_safe_pay(self):
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    def get_pay_now_credit(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def get_success_message(self):
        return self.driver.find_element(By.ID, "orderPaymentSuccess")

    def get_save_credit_details_button(self):
        return self.driver.find_element(By.NAME, "save_master_credit")

    def get_order_num(self):
        return self.driver.find_element(By.ID, "orderNumberLabel")

    def username_on_payment(self, un):
        username = self.driver.find_element(By.NAME, "usernameInOrderPayment")
        username.send_keys(un)

    def password_on_payment(self, pw):
        password = self.driver.find_element(By.NAME, "passwordInOrderPayment")
        password.send_keys(pw)

    def sign_in_on_payment(self, un, pw):
        self.username_on_payment(un)
        self.password_on_payment(pw)
        self.driver.find_element(By.ID, "login_btn").click()

    def click_on_credit_card_option(self):
        self.driver.find_element(By.XPATH, "//*[@id='paymentMethod']/div/div/div[2]/input").click()

    def enter_card_number(self, num):
        card = self.driver.find_element(By.NAME, "card_number")
        card.send_keys(num)

    def enter_CVV_number(self, num):
        cvv = self.driver.find_element(By.NAME, "cvv_number")
        cvv.send_keys(num)

    def enter_date_number(self, mm, yyyy):
        month = self.driver.find_element(By.NAME, "mmListbox")
        month_dropdown = Select(month)
        month_dropdown.select_by_index(int(mm))
        year = self.driver.find_element(By.NAME, "yyyyListbox")
        month_dropdown = Select(year)
        month_dropdown.select_by_index(int(yyyy)-2023)

    def enter_name(self, n):
        name = self.driver.find_element(By.NAME, "cardholder_name")
        name.send_keys(n)

    def enter_credit_details(self, num, cvv, mm, yyyy, name):
        self.enter_card_number(num)
        self.enter_CVV_number(cvv)
        self.enter_date_number(mm, yyyy)
        self.enter_name(name)
