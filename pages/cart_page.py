from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_ACRT_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    empty_cart_msg = 'Your cart is empty'

    def open_cart_page(self):
        self.open_url('/cart')

    def verify_empty_cart_msg(self):
        self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_ACRT_MSG)
        # self.wait_until_url_contains('cart')
        # self.verify_url(f'{self.base_url}/cart')

        # empty_msg_element = self.find_element(*self.EMPTY_ACRT_MSG)
        # print(empty_msg_element)
        # print(empty_msg_element.text)
        #
        # self.driver.refresh() # refresh the webpage
        # print('\nAfter Refresh: \n')
        # empty_msg_element = self.find_element(*self.EMPTY_ACRT_MSG)
       #  print(empty_msg_element)
       #  print(empty_msg_element.text)
