import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Google search scenario
# 1. Open the browser, Launch the website google.com (given condition)
# 2. type 'selenium python' in the search and hit Enter (Actions-When)
# 3. Verify the results is more than 20 mln (Test here, check point-Then)
# 4.Verify that it takes less than a second for the search (Test here, checkpoint- Then)
# 5. Close the browser
# keywords: HTML, Locator: xpath, id, cssSelector, name, link_name, partial_link_name, class_name,

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # start the browser
driver.get("http://google.com")
print("Opened the browser and google website")
time.sleep(2)

search_text_box = driver.find_element_by_name("q") #Locates the search box element in the HTML DOM
print("identified google search box")
time.sleep(2)

search_text_box.clear
search_text_box.send_keys("python selenium") # enters provided text in the search box
print("cleared the search box then typed 'python selenium' words in it")
time.sleep(2)

search_text_box.send_keys(Keys.RETURN) # simulates hitting the Enter key on your keyboard
print("hit the enter button")
time.sleep(2)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)

# "About 31,100,000 results (0.39 seconds)
#Verify the result num is > 20mln
result_msg_list = result_msg.split()
result_num_str = result_msg_list[1].replace(',','')
result_num = int(result_num_str)
assert result_num > 20000000, "Resukt num is less than 20 mln"

print('Verifying result number Passed')

#Verify the performance, Less than a second

result_time_str = result_msg_list[3].replace('(','')
result_time = float(result_time_str)
assert result_time < 1, "Search took more than 1 second"
print('Verifying search performance Passed')


print("now closing the browser...")
driver.close()
