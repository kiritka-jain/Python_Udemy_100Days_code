from selenium import webdriver

chrome_driver_path = '/Users/kirti/Documents/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')
event_time = driver.find_elements_by_class_name('event-widget li time ')
event_name = driver.find_elements_by_class_name('event-widget li a ')
total_events = len(event_time)
upcoming_events = {}
for index in range(total_events):
    upcoming_events[index]={
        'time':event_time[index].text,
        'event':event_name[index].text
    }
print(upcoming_events)

driver.quit()
