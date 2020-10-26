import time
from selenium import webdriver


# Inializing a new browser
driver = webdriver.Chrome() # start the browser
driver.maximize_window()
driver.implicitly_wait(10) # common interview question

driver.get("https://letskodeit.teachable.com/p/practice")
print("Opened the browser and google website")
time.sleep(2)

# Find all buttons

buttons = driver.find_elements_by_xpath('//button') # tag name. Will return the whole elements
for button in buttons:
    print("text of button:", button.text)

# Find by link text

open_tab = driver.find_element_by_link_text('Open Tab')
open_tab2 = driver.find_elements_by_partial_link_text('en Tab')
open_tab.click() # this opens a new tab but doesnt switch to it
time.sleep(3)


driver.close() # this will close the current tab
print('current tab is closed')
time.sleep(1)
driver.quit() # this will close the browser
print('Browser Closed')

# search_text_box = driver.find_element_by_name("q") #Locates the search box element in the HTML DOM
# print("identified google search box")
# time.sleep(2)
#
# search_text_box.clear
# search_text_box.send_keys("python selenium") # enters provided text in the search box
# print("cleared the search box then typed 'python selenium' words in it")
# time.sleep(2)