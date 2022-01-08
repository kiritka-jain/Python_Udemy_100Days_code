from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/kirti/Documents/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # Holding article count number

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# stats = driver.find_element_by_css_selector('#articlecount a')
# print(stats.text)

# Signing up for lab form
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element_by_name('fName')
first_name.send_keys("timmy")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element_by_name('lName')
last_name.send_keys("turtle")
last_name.send_keys(Keys.ENTER)

email_id = driver.find_element_by_name('email')
email_id.send_keys("timmytut@gmail.com")
email_id.send_keys(Keys.ENTER)

sign_up = driver.find_element_by_css_selector('button')
sign_up.click()




# driver.quit()