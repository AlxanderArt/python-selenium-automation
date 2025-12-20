from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# Search for tea
driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

# Wait for 5 sec
sleep(5)

# Verify
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
print(actual_text)

assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'
print('Test case PASSED')

driver.quit()
# sleep(5)
