from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException 
import time

# Replace with your own details
username = "qwertyuiop9191"
password = "qwerty123!"
email = "qwertyuiop9191@eurokool.com"
fullname = "qwertyuiop9191"

# Start the browser and go to the Instagram sign up page
chromedriver_path = "../chromedriver.exe"
browser = webdriver.Chrome(chromedriver_path)
browser.get("https://www.instagram.com/accounts/emailsignup/")

# Wait for the page to load
time.sleep(2)

# Find the form fields and enter the details
email_input = browser.find_element_by_name("emailOrPhone")
email_input.send_keys(email)

fullname_input = browser.find_element_by_name("fullName")
fullname_input.send_keys(fullname)

username_input = browser.find_element_by_name("username")
username_input.send_keys(username)

# Check if the chosen username is available
#check_username_button = browser.find_element_by_xpath("//button[text()='Check']")
#check_username_button.click()

time.sleep(2)

password_input = browser.find_element_by_name("password")
password_input.send_keys(password)

# Click the sign up button
sign_up_button = browser.find_element_by_css_selector("button[type='submit']")
sign_up_button.click()

# Wait for the next page to load
time.sleep(2)
while True:
    try:
        not_available_ele = browser.find_element_by_id("ssfErrorAlert")
        username = username+"_123"
        
        username_input = browser.find_element_by_name("username")
        username_input.clear()
        time.sleep(2)
        print(f"Cleared================================={username}")
        username_input.send_keys(username)
        sign_up_button.click()
        break
    except NoSuchElementException:
        pass
        


# Click the "Not Now" button to skip adding friends
not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
not_now_button.click()

# Wait for the next page to load
time.sleep(2)

# Click the "Skip" button to skip setting up your profile
skip_button = browser.find_element_by_xpath("//button[text()='Skip']")
skip_button.click()

# Wait for the next page to load
time.sleep(2)

# Close the browser
browser.close()


not_available_ele = browser.find_element_by_id("ssfErrorAlert")
not_available_ele.text