# class Page: # blueprint / abstract
#
#     def click(self):
#         print('Clicking....')
#
#     def input_text(self, text):
#         print(f'Inputting text {text}')
#
#     def verify_element(self, locator):
#         print(f'Verifying by {locator}')
#
#
# class LoginPage(Page):
#
#     def open_login(self):
#         print('Opening login')
#
#     def click_login(self):
#         self.click()
#
# class RegistrationPage(Page):
#     pass
#
# class Header(Page):
#     pass
#
# login_page = LoginPage()
# login_page.open_login()
# login_page.click_login()
# login_page.verify_element('search btn')