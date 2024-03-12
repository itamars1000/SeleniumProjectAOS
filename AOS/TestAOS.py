from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from HomePage import HomePage
from CategoryPage import Category_Page
from ProductPage import Product_Page
from CartPopUpWindow import CartPopUpWindow
from ShoppingCartPage import ShoppingCartPage
from General import General
from OrderPaymentPage import OrderPaymentPage
from CreateAccountPage import CreateAccountPage
from openpyxl import load_workbook


class TestAOS(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self._outcome = None

    def setUp(self):
        service_chrome = Service(r"C:\Users\Kramer\Documents\selenium1\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get(r"https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.tests_file = load_workbook(filename="Tests.xlsx")
        self.tf = self.tests_file['tests']
        self.col = ''

        self.wait = WebDriverWait(self.driver, 10)

        self.action_chain = ActionChains(self.driver)

        self.home_page = HomePage(self.driver)

        self.category_Page = Category_Page(self.driver)

        self.product_page = Product_Page(self.driver)

        self.general = General(self.driver)

        self.popup = CartPopUpWindow(self.driver)

        self.shopping_cart_page = ShoppingCartPage(self.driver)

        self.payment_page = OrderPaymentPage(self.driver)

        self.create_account = CreateAccountPage(self.driver)

    def test_amount_of_products_in_shopping_cart(self):
        """Add to the shopping cart 2 products with different quantities,
         and check if the amount in the shopping cart is correct"""
        self.general.add_product_to_cart(self.tf['C3'].value, self.tf['C4'].value, self.tf['C5'].value,
                                         self.tf['C6'].value)
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['C7'].value, self.tf['C8'].value, self.tf['C9'].value,
                                         self.tf['C10'].value)
        total_items = self.popup.get_total_items().text
        # check the amount digits in the total items to know how much chars take from the text
        chars_amount = len(str(int(self.tf['C5'].value) + int(self.tf['C9'].value)))
        self.assertEqual(total_items[1:chars_amount + 1], str(int(self.tf['C5'].value) + int(self.tf['C9'].value)))

        # result column
        self.col = 'C'

    def test_check_details_in_popup_window(self):
        """For 3 products, check if the details in the pop-up cart window is correct"""
        self.general.add_product_to_cart(self.tf['D3'].value, self.tf['D4'].value, self.tf['D5'].value,
                                         self.tf['D6'].value)
        # check if there is just one color, and if there is just one, won't be a click
        # check if the name in the pop-up window is like or part of the product name in the page, if the name too long,
        # check without the 3 points.
        self.assertTrue(self.popup.get_product_name_from_popup().text[:-3] in self.product_page.get_product_name().text)
        # check if the quantity in the pop-up window is like in the page
        self.assertEqual(self.product_page.get_product_quantity().get_attribute("value"), self.popup.get_product_quantity_from_popup().text[5:])
        # check if the color in the pop-up window is like the one from the Excel
        self.assertEqual(self.tf['D6'].value, self.popup.get_product_color_from_popup().text[7:])
        # check if the quantity*the product price is equal to the price in the pop-up window
        self.assertEqual((float(self.tf['D5'].value) * float(self.product_page.get_product_price().text[1:].replace(',', '')),
                          float(self.popup.get_product_price_from_popup().text[1:].replace(',', ''))))
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['D7'].value, self.tf['D8'].value, self.tf['D9'].value,
                                         self.tf['D10'].value)
        self.assertTrue(self.popup.get_product_name_from_popup().text[:-3] in self.product_page.get_product_name().text)
        self.assertEqual(self.product_page.get_product_quantity().get_attribute("value"), self.popup.get_product_quantity_from_popup().text[5:])
        self.assertEqual(self.tf['D10'].value, self.popup.get_product_color_from_popup().text[7:])
        self.assertEqual(float(self.tf['D9'].value) * float(self.product_page.get_product_price().text[1:].replace(',', '')),
                         float(self.popup.get_product_price_from_popup().text[1:].replace(',', '')))
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['D11'].value, self.tf['D12'].value, self.tf['D13'].value,
                                         self.tf['D14'].value)
        self.assertTrue(self.popup.get_product_name_from_popup().text[:-3] in self.product_page.get_product_name().text)
        self.assertEqual(self.product_page.get_product_quantity().get_attribute("value"), self.popup.get_product_quantity_from_popup().text[5:])
        self.assertEqual(self.tf['D14'].value, self.popup.get_product_color_from_popup().text[7:])
        self.assertEqual(float(self.tf['D13'].value) * float(self.product_page.get_product_price().text[1:].replace(',', '')),
                         float(self.popup.get_product_price_from_popup().text[1:].replace(',', '')))

        # result column
        self.col = 'D'

    def test_remove_product_from_pop_up(self):
        """Add 2 products to the cart and remove one, check if the cart updated in the pop-up window"""
        self.general.add_product_to_cart(self.tf['E3'].value, self.tf['E4'].value, self.tf['E5'].value,
                                         self.tf['E6'].value)
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['E7'].value, self.tf['E8'].value, self.tf['E9'].value,
                                         self.tf['E10'].value)
        # check the amount of product in the cart and then remove one and check if the amount down by one.
        product_in_cart = len(self.popup.cart_popup_product_list())
        self.popup.remove_last_product()
        self.assertEqual(product_in_cart - 1, len(self.popup.cart_popup_product_list()))

        # result column
        self.col = 'E'

    def test_move_to_shopping_cart(self):
        """Check if after click on the cart icon, the shopping cart page open"""
        self.general.add_product_to_cart(self.tf['F3'].value, self.tf['F4'].value, self.tf['F5'].value,
                                         self.tf['F6'].value)
        self.product_page.click_add_to_cart()
        self.general.click_on_cart()
        # Check if the title of the shopping cart page is exist
        self.assertIsNotNone(self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']"))

        # result column
        self.col = 'F'

    def test_sum_total_price(self):
        """Add 3 products, check if the total price of the order is equal to all products price"""
        self.general.add_product_to_cart(self.tf['G3'].value, self.tf['G4'].value, self.tf['G5'].value,
                                         self.tf['G6'].value)
        # Get the price without the '$' and if the number more than 999, than remove the ','.
        p1_price = float(self.popup.get_product_price_from_popup().text[1:].replace(',', ""))
        print(f"product 1: {self.product_page.get_product_name().text}\n"
              f"quantity: {self.tf['G5'].value}\n"
              f"price: {p1_price}")
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['G7'].value, self.tf['G8'].value, self.tf['G9'].value,
                                         self.tf['G10'].value)
        p2_price = float(self.popup.get_product_price_from_popup().text[1:].replace(',', ""))
        print(f"product 2: {self.product_page.get_product_name().text}\n"
              f"quantity: {self.tf['G9'].value}\n"
              f"price: {p2_price}")
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['G11'].value, self.tf['G12'].value, self.tf['G13'].value,
                                         self.tf['G14'].value)
        p3_price = float(self.popup.get_product_price_from_popup().text[1:].replace(',', ""))
        print(f"product 3: {self.product_page.get_product_name().text}\n"
              f"quantity: {self.tf['G13'].value}\n"
              f"price: {p3_price}")
        self.general.click_on_cart()
        # Check if the checkout price without the '$' is equal to sum of the product prices
        self.assertEqual(self.shopping_cart_page.get_checkout_price().text[1:].replace(',', ""),
                         str(p1_price + p2_price + p3_price))

        # result column
        self.col = 'G'

    def test_edit_on_shopping_page(self):
        """Check if after change quantities of 2 products, the quantities in the cart change correctly"""
        self.general.add_product_to_cart(self.tf['H3'].value, self.tf['H4'].value, self.tf['H5'].value,
                                         self.tf['H6'].value)
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['H7'].value, self.tf['H8'].value, self.tf['H9'].value,
                                         self.tf['H10'].value)
        self.general.click_on_cart()
        # Define quantities to the change
        quan1 = 2
        quan2 = 4
        popup_window = self.driver.find_element(By.ID, "toolTipCart")
        self.wait.until(EC.invisibility_of_element(popup_window))
        # Click on edit of the first product and change the quantity
        self.shopping_cart_page.edit_list()[0].click()
        self.product_page.change_quantity(quan1)
        self.product_page.click_add_to_cart()
        self.wait.until(EC.visibility_of(popup_window))
        # Click on edit of the second product and change the quantity
        self.shopping_cart_page.edit_list()[1].click()
        self.product_page.change_quantity(quan2)
        self.product_page.click_add_to_cart()
        quan_list = self.shopping_cart_page.quantities_list()
        self.assertEqual(quan_list[0].text, str(quan1))
        self.assertEqual(quan_list[1].text, str(quan2))

        # result column
        self.col = 'H'

    def test_backs_on_site(self):
        """Test the back click on the site, open product page and click 2 times back"""
        self.home_page.click_category(self.tf['I3'].value)
        self.category_Page.click_product(self.tf['I4'].value)
        self.product_page.change_quantity(self.tf['I5'].value)
        self.product_page.click_add_to_cart()
        self.driver.back()
        # Check if the title of the category page is TABLETS
        self.assertEqual(self.tf['I3'].value, self.category_Page.get_title_page().text)
        self.driver.back()
        # Check if the categories displayed, it is means that the Home page is displayed
        self.assertTrue(self.home_page.get_categories_element().is_displayed())

        # result column
        self.col = 'I'

    def test_make_order_with_new_user_and_safe_pay(self):
        """Test the function of make an order with new account and pay with Safe Pay"""
        self.general.add_product_to_cart(self.tf['J3'].value, self.tf['J4'].value, self.tf['J5'].value,
                                         self.tf['J6'].value)
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['J7'].value, self.tf['J8'].value, self.tf['J9'].value,
                                         self.tf['J10'].value)
        self.popup.click_checkout()
        self.payment_page.click_registration()
        # Wait for create account page will display
        self.wait.until(EC.visibility_of(self.payment_page.get_registration_button()))

        self.create_account.create_account(self.tf['J17'].value, self.tf['J18'].value, self.tf['J19'].value,
                                           self.tf['J19'].value)
        # Wait for payment page will display
        self.wait.until(EC.visibility_of(self.payment_page.get_next_button()))
        self.payment_page.click_next()
        # Enter Safe Pay details
        self.payment_page.enter_safe_pay_username(self.tf['J20'].value)
        self.payment_page.enter_safe_pay_password(self.tf['J21'].value)
        self.payment_page.click_pay_now_safe_pay()
        # Check if the payment success page displayed
        self.wait.until(EC.visibility_of(self.payment_page.get_success_message()))
        self.assertTrue(self.payment_page.get_success_message().is_displayed())
        order_num = self.payment_page.get_order_num().text
        self.action_chain.move_to_element(self.general.get_cart_icon()).perform()
        self.wait.until(EC.visibility_of(self.popup.empty_cart_message()))
        # Check if the 'empty cart' message displayed on the pop-up window
        self.assertTrue(self.popup.empty_cart_message().is_displayed())
        self.action_chain.move_to_element(self.general.get_account_icon())
        self.wait.until(EC.invisibility_of_element(self.popup.empty_cart_message()))
        self.general.click_account_icon()
        self.wait.until(EC.visibility_of(self.general.get_my_account()))
        self.general.click_my_orders()
        # Check if the order number exists on my orders page
        self.assertEqual(self.general.get_order_number().text, order_num)

        # Delete the test account
        self.general.delete_account()
        # result column
        self.col = 'J'


    def test_make_order_with_exist_user_and_credit_card(self):
        """Test the function of make an order with exist account and pay with credit card"""
        self.general.add_product_to_cart(self.tf['K3'].value, self.tf['K4'].value, self.tf['K5'].value,
                                         self.tf['K6'].value)
        self.general.logo_click()
        self.general.add_product_to_cart(self.tf['K7'].value, self.tf['K8'].value, self.tf['K9'].value,
                                         self.tf['K10'].value)
        self.popup.click_checkout()
        # Sign-in with exists username and password
        self.payment_page.sign_in_on_payment(self.tf['K15'].value, self.tf['K16'].value)
        # Wait for payment page will display
        self.wait.until(EC.visibility_of(self.payment_page.get_next_button()))
        self.payment_page.click_next()
        self.payment_page.click_on_credit_card_option()
        # Enter credit details(number, cvv, mm, yyyy, name)
        self.payment_page.enter_credit_details(self.tf['K22'].value,
                                               self.tf['K23'].value,
                                               self.tf['K24'].value,
                                               self.tf['K25'].value,
                                               self.tf['K26'].value)
        # Click to cancel the save credit details
        self.payment_page.get_save_credit_details_button().click()  # BUG!!!!!!!!
        self.payment_page.get_pay_now_credit().click()
        # Check if the payment success page displayed
        self.wait.until(EC.visibility_of(self.payment_page.get_success_message()))
        self.assertTrue(self.payment_page.get_success_message().is_displayed())
        order_num = self.payment_page.get_order_num().text
        self.action_chain.move_to_element(self.general.get_cart_icon()).perform()
        self.popup.wait_popup()
        # Check if the 'empty cart' message displayed on the pop-up window
        self.assertTrue(self.popup.empty_cart_message().is_displayed())
        self.action_chain.move_to_element(self.general.get_account_icon()).perform()
        self.wait.until(EC.invisibility_of_element(self.popup.empty_cart_message()))
        self.general.click_account_icon()
        self.wait.until(EC.visibility_of(self.general.get_my_account()))
        self.general.click_my_orders()
        # Check if the order number exists on my orders page
        self.assertEqual(self.general.get_order_number().text, order_num)

        # result column
        self.col = 'K'

    def test_log_in_and_log_out(self):
        """Check if after sign in with exist user, the username shown up on the top right of the screen,
        and check after log out the user not connected anymore"""
        # Sign in with exist username and password
        self.general.sign_in(self.tf['L15'].value, self.tf['L16'].value)
        # Wait until the home page will display
        self.wait.until(EC.visibility_of(self.home_page.get_categories_element()))
        # Check if the username display
        self.assertEqual(self.tf['L15'].value, self.general.get_connect_username().text)
        self.general.sign_out()
        # Wait for the username disappear
        self.wait.until(EC.invisibility_of_element(self.general.get_connect_username()))
        self.general.click_account_icon()
        # Check if after click on account icon the log in window display, what ,means the account is logged out
        self.wait.until(EC.visibility_of(self.general.get_log_in_window_element()))
        self.assertTrue(self.general.get_log_in_window_element().is_displayed())

        # result column
        self.col = 'L'

    def tearDown(self):
        # Write in the Excel file which test failed or passed
        try:
            self.tf[f'{self.col}27'].value = 'V'
            self.tests_file.save('Tests.xlsx')
        except:
            pass
