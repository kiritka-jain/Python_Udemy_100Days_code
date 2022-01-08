from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

chrome_driver_path = '/Users/kirti/Documents/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

period = timedelta(minutes=2)
start_time =datetime.now()
end_time = start_time + period
checking_period = start_time +timedelta(seconds=5)
minutes = 0

# cookie clicker
cookie = driver.find_element_by_id('cookie')


def check_for_buying_elements():
    money = driver.find_element_by_id('money')
    present_money = int(money.text)
    elements = driver.find_elements_by_css_selector('#store b')
    elements_list = []
    for element in elements:
        element_data = element.text.split('-')
        if element_data[0] != "":
            product_name = element_data[0]
            product_val = element_data[1].replace(',', '')
            element_val = [product_name, int(product_val)]
            elements_list.append(element_val)
    elements_list = elements_list[::-1]
    for product in elements_list:
        if present_money >= product[1]:
            item = 'buy'+product[0].strip()
            print(item)
            buy_item = driver.find_element_by_id(item)
            buy_item.click()

while start_time <= end_time:
    start_time = datetime.now()
    cookie.click()
    if checking_period < start_time:
        check_for_buying_elements()
        checking_period = start_time + timedelta(seconds=5)

money = driver.find_element_by_id('money')
present_money = int(money.text)
print(present_money)
cookie_per_sec = driver.find_element_by_id('cps')
print(cookie_per_sec.text)


driver.quit()

# after every 5 second checker highest thing that can be purchased
# timer 5 minute print cookie/sec


# driver.quit()
