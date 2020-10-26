import time
from selenium import webdriver

#. Inializing a new browser
driver = webdriver.Chrome()
print("Opened the Chrome Browser")

driver.implicitly_wait(10)

def launch_website():
    driver.get('https://letskodeit.teachable.com/p/practice')
    print("opened the the letskode url")
    time.sleep(1)

#1.find all buttons, working with this elements
def find_elements_tag():
    buttons = driver.find_elements_by_xpath("//button")
    for button in buttons:
        print('text if buttons:', button.text)

#2. Find by Link text
def open_tab_by_link_text():
    open_tab = driver.find_element_by_link_text("Open Tab")
    open_tab2 = driver.find_elements_by_partial_link_text("en Tab")
    time.sleep(2)
    return open_tab

def web_driver_properties():
    print("current url: ", driver.current_urlr)
    print("current title: ", driver.title)
    print("current win_handle: ", driver.current_window_handle)
    print("current name: ", driver.name)


#3. Using WebDriver Class properties
def web_driver_properties_switch_to_tab():
    url1 = driver.current_url
    title1 = driver.title
    win_handle1 = driver.current_window_handle
    name1 = driver.name
    print("current url: ", url1)
    print("current title: ", title1)
    print("current win_handle: ", win_handle1)
    print("current name: ", name1)

# After getting all details of the current tab, we are opening new tab
    open_tab_by_link_text().click() #-This opens a new tab but doesnt swith to it

# Switch to a new tab, WedDriver method - switch_to.window(new_handle)
    handles = driver.window_handles
    print(handles)

    url2 = ''
    title2 =''
    win_handle2 = ''


    for handle in handles:
        if handle != win_handle1:
            driver.switch_to.window(handle)

        url2 = driver.current_url
        title2 = driver.title
        win_handle2 = driver.current_window_handle

    print("current url2: ", url2)
    print("current title2: ", title2)
    print("current win_handle2 : ", win_handle2)

#Verifyng new url and title in by Requirment
    assert url2 == 'https://letskodeit.teachable.com/courses'
    assert title2 == "Let's Kode It"

    driver.close()
    print("closed the current tab")
    time.sleep(2)

    driver.switch_to.window(win_handle1)

    print('title after closing a new tab: ', driver.title)
    print('current_url after closing a new tab: ', driver.current_url)
    print('current_window_habdle after closing a new tab: ', driver.current_window_handle)

def close_browser():
    driver.quit()
    print("closed the browser")