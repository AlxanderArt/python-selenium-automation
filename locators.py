from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Locators
# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'searchDropdownBox')

# By XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute']")

# By attributes, any tag
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")
# By many attrs
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute'  and @type='text']")
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute'  and @type='text' and @otherarr='value']")

# By text
driver.find_element(By.XPATH, "//a[text()='Holiday Gifts']")
driver.find_element(By.XPATH, "//a[text()='Holiday Gifts' and @class='nav-a  ']")
driver.find_element(By.XPATH, '//a[@class="nav-a  " and text()="Holiday Gifts"]')

# By attr, partial match
driver.find_element(By.XPATH, "//a[contains(@aria-label, 'selection is English (EN)')]")
driver.find_element(By.XPATH, "//a[contains(@aria-label, 'selection is English (EN)') and contains(@class, 'nav-a')]")

# Bad practices: using dynamically generated parts of attributes (class / id / names etc.)
driver.find_element(By.XPATH, "//a[@class='styles_ndsLink__GUaai styles_onLight__QKcK7 sc-b8685e67-1 sc-d9c75939-0 grtDbE bgAxjv']")
driver.find_element(By.XPATH, "//input[@class='styles_searchInput__W2xFo']")
driver.find_element(By.XPATH, "//input[@class='styles_searchInput__dg215g']")
# To avoid "__W2xFo" => 
driver.find_element(By.XPATH, "//input[contains(@class, 'styles_searchInput')]")








