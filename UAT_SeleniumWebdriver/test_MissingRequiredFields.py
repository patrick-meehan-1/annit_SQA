from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ALWAYS OPEN BROWSER
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
app_url = 'https://www.ariseconstructions.com/'
chrome_browser.get(app_url)

time.sleep(2)


# -------

# Clicked contact button
buttons = chrome_browser.find_elements(By.CLASS_NAME, 'nav-link')
contact_button = buttons[7]
contact_button.click()

# assrted pages title
expected_title = "Contact Us | Arise Constructions | Denver, CO"
assert expected_title in chrome_browser.title

# Filling out form
time.sleep(2)
iframe = chrome_browser.find_element(By.TAG_NAME, 'iframe')
chrome_browser.switch_to.frame(iframe)

fname_field = chrome_browser.find_element(By.NAME, 'lead_attributes.first_name')
fname_field.send_keys("Joe")

lname_field = chrome_browser.find_element(By.NAME, 'lead_attributes.last_name')
lname_field.send_keys("Bloggs")

email_field = chrome_browser.find_element(By.NAME, 'lead_attributes.email')
email_field.send_keys("123@gmail.com")

phone_field = chrome_browser.find_element(By.NAME, 'lead_attributes.phone')
phone_field.send_keys("719-266-2837")

submit_button = chrome_browser.find_element(By.CLASS_NAME, 'cursor-pointer')
submit_button.click()

chrome_browser.switch_to.default_content()



# -------




# ALWAYS CLOSE BROWSER AT THE END
time.sleep(20)
chrome_browser.close()