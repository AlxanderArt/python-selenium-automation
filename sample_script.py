from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
# implicitly_wait => checks for el every 100ms / applied to all find_element and find_elements
# driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, timeout=4)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

SEARCH_BTN = (By.NAME, 'btnK214532452143421')
driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN), message='Search button was not clickable').click()

# verify search results
assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
