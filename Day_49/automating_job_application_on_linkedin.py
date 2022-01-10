from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = '/Users/kirti/Documents/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=New%20Delhi%2C%20Delhi%2C'
           '%20India&geoId=115918471&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0')

apply_now_button = driver.find_element_by_class_name('nav__button-secondary')
apply_now_button.click()

email = 'linkedin email id'
login_id = driver.find_element_by_id('username')
login_id.send_keys(email)
password = 'linkedin password'
login_password = driver.find_element_by_id('password')
login_password.send_keys(password)
click_button = driver.find_element_by_class_name('btn__primary--large.from__button--floating')
click_button.click()
jobs = driver.find_elements_by_css_selector(
    'li.jobs-search-results__list-item.occludable-update.p0.relative.ember-view')
for job in jobs:
    if job.find_elements_by_link_text('Python Developer') == 'Python Developer':
        try:
            job.click()
            time.sleep(5)
            save = driver.find_element_by_css_selector('button.jobs-save-button.mr2.artdeco-button.artdeco-button--2.artdeco-button--secondary')
            save.click()
        except NoSuchElementException:
            continue

