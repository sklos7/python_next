from Week7.Web_Driver_Class.webdriver_functions import *

#****************scenario
# launch_website("http://automationpractice.com/index.php")
# women_tab = "//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/a[1]"
# click_element_by_xpath(women_tab)
# go_back_to_previous_page()
# refresg_browser()
# go_next_page()
# close_browser()

# **************************** scenario 2
# find_elements_tag()
# web_driver_properties()
# web_driver_properties_switch_to_tab()
#"durak"

#************************ Scenario: Log in to "http://automationpractice.com/index.php"



sign_in_link = "//a[contains(text(),'Sign in')]"

email_input = "//input[@id='email']"

password_input = "//input[@id='passwd']"

sign_in_button = "//button[@id='SubmitLogin']"

sing_out_link = "//header/div[2]/div[1]/div[1]/nav[1]/div[2]/a[1]"

# steps:
launch_website("http://automationpractice.com/index.php")
click_element_by_xpath(sign_in_link)
time.sleep(2)
enter_text_by_xpath(email_input, "python@gmail.com")
enter_text_by_xpath(password_input, "durak")
click_element_by_xpath(sign_in_button)
time.sleep(5)
print("Successfully signed in")
print("Signing out now...")
click_element_by_xpath(sing_out_link)
close_browser()