from selenium import webdriver 
from selenium.webdriver.common.by import By
import pyperclip
import time
import random
import string
import json
import ast
import os

def generate_username(length=8):
    # Define the pool of characters to choose from
    characters_alphabet = random.choices(string.ascii_letters, k=int(length*.7))
    number = random.choices(string.digits, k=length-int(length*.7))
    username = characters_alphabet+number
    #print(characters_alphabet)
    
    # Use random.choices to pick length characters from the pool
    username = ''.join(username)
    
    return username.lower()

def generate_password(length=12):
    characters_alphabet = random.choices(string.ascii_letters, k=int(length*.7))
    number = random.choices(string.digits, k=length-int(length*.7)-1)
    special_char = random.choices(["!","@","$","%","&","*"], k=1)
    password = characters_alphabet+number+special_char
    password = ''.join(password)
    password = password.lower()
    password = password.capitalize()
    return password

def get_message(wd, message_xpath):
    message_txt_element = wd.find_element(by=By.XPATH, value=message_xpath)
    message = message_txt_element.text
    return message


driver_path = "../chromedriver"
account_detail_json = "../data/tutanote_account.json"
link = "https://mail.tutanota.com/login?noAutoLogin=true&keepSession=true"

MORE_XPATH = "/html/body/div/div[3]/div[2]/div/div[3]/div/button/small"
SIGNUP_XPATH = "/html/body/div/div[3]/div[2]/div/div[4]/div/div/div/button[1]/div/div"
FREE_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[5]/button/div"
AGREE_1_XAPTH = "/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div"
AGREE_2_XAPTH = "/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]"
AGREE_OK_XPATH = "/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]/div/div"
EMAIL_INPUT_XAPTH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/input"
PASSWORD_INPUT_XAPTH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/input"
REPEAT_PASSWORD_INPUT_XAPTH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/input"
TERM_AGREE_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/input"
AGE_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/input"
NEXT1_BUTTON_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[5]/button/div"
# Loading pop-up after clinking on next
PREPEARING_XPATH = "/html/body/div/div[2]/div[2]/div/div/div/div/p"
RECOVERYCODE_COPY_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[3]/button[1]/div/span"
RECOVERY_OK_BUTTON_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[4]/div/button/div"

MESSAGE_TXT_XPATH = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/small/div"

wd = webdriver.Chrome(driver_path)
country_code = ["US-C","US", "US-W", "CA", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "GB-N", "TR", "HK"]

while True:
    select_country = country_code[random.randint(0, len(country_code))]
    status = os.system(f"windscribe connect {select_country}")
    wd.maximize_window()
    wd.get(link)
    more_element = wd.find_element(by=By.XPATH, value=MORE_XPATH)
    more_element.click()
    time.sleep(1)
    signup_element = wd.find_element(by=By.XPATH, value=SIGNUP_XPATH)
    signup_element.click()
    time.sleep(10)
    free_element = wd.find_element(by=By.XPATH, value=FREE_XPATH)
    free_element.click()
    time.sleep(1)
    agree1_element = wd.find_element(by=By.XPATH, value=AGREE_1_XAPTH)
    agree1_element.click()
    agree2_element = wd.find_element(by=By.XPATH, value=AGREE_2_XAPTH)
    agree2_element.click()
    agreeok_element = wd.find_element(by=By.XPATH, value=AGREE_OK_XPATH)
    agreeok_element.click()
    time.sleep(3)
    message_txt_element = wd.find_element(by=By.XPATH, value=MESSAGE_TXT_XPATH)
    message = message_txt_element.text
    email_id = generate_username()
    password = generate_password()
    domain="tutanota.com"
    if message=="Please enter mail address.":
        email_input_element = wd.find_element(by=By.XPATH, value=EMAIL_INPUT_XAPTH)
        time.sleep(1)
        email_input_element.clear()
        email_input_element.send_keys(email_id)
        time.sleep(5)
        message = get_message(wd, MESSAGE_TXT_XPATH)
        if message == "Email address is available.":
            print("Enter password....")
            password_input_element = wd.find_element(by=By.XPATH, value=PASSWORD_INPUT_XAPTH)
            password_input_element.send_keys(password)
            repeat_password_input_element = wd.find_element(by=By.XPATH, value=REPEAT_PASSWORD_INPUT_XAPTH)
            repeat_password_input_element.send_keys(password)
            term_agree_element = wd.find_element(by=By.XPATH, value=TERM_AGREE_XPATH)
            term_agree_element.click()
            time.sleep(2)
            age_element = wd.find_element(by=By.XPATH, value=AGE_XPATH)
            age_element.click()
            time.sleep(2)
            next1_element = wd.find_element(by=By.XPATH, value=NEXT1_BUTTON_XPATH)
            next1_element.click()
            time.sleep(2)
            prepering_element = wd.find_element(by=By.XPATH, value=PREPEARING_XPATH)
            prep_counter = 0
            while prepering_element:
                print("Loading....")
                time.sleep(5)
                
                try:
                    prepering_element = wd.find_element(by=By.XPATH, value=PREPEARING_XPATH)
                except:
                    break
            recovery_code_copy_element = wd.find_element(by=By.XPATH, value=RECOVERYCODE_COPY_XPATH)
            recovery_code_copy_element.click()
            recovery_code = pyperclip.paste()
            recovery_code_ok_element = wd.find_element(by=By.XPATH, value=RECOVERY_OK_BUTTON_XPATH)
            recovery_code_ok_element.click()
            with open(account_detail_json, "r") as json_file:
                account_details = json.load(json_file)

            singel_account_info = {"email_id":email_id+"@"+domain,
                                   "password":password,
                                   "recovery_code": recovery_code}
            account_details["All account"][email_id] = singel_account_info

            json_object = json.dumps(account_details, indent=4)

            with open(account_detail_json, "w") as json_file:
                json_file.write(json_object)

        elif message == "Email address is not available.":
            wd.close()
            time.sleep(5)

        os.system("windscribe disconnect")
    