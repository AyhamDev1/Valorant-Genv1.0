from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import colorama
from colorama import Fore
from faker import Faker
import time
import random
import string

#Made By HendrixServices (DO NOT SKID YOU NIGGER)
#THIS DOSENT CAPTCHA SOLVE COPE LIL SKIDS 

colorama.init()


#Here it Generates the  Username in these order 

#first row is Hendrix (1 in 100 chances of a number) then Service EXAMPLE : (Hendrix12Service)

#Secound row is HendrixService12 it puts the number beside Service on the right 
def generate_username():
    if random.choice([True, False]):
        return f"Hendrix{random.randint(1, 100)}Service"
    else:
        return f"{random.randint(1, 100)}HendrixService"
#Generates a strong password that bypasses the Security of RIOT GAMES SIGN UP PAGE**
def generate_password():
    length = 10
    strength = "Okay"
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password, strength

driver = webdriver.Chrome()
#generates random gmails
fake = Faker()

random_email = fake.email() + "@gmail.com"

cleaned_email = random_email.split('@')[0] + "@gmail.com"
#opens the signup page
driver.get("https://auth.riotgames.com/login#client_id=prod-xsso-playvalorant&code_challenge=xM3RBMSrtcllbaYAbIpQBlIHD0a82NyTVYuUx9hoojw&code_challenge_method=S256&prompt=signup&redirect_uri=https%3A%2F%2Fxsso.playvalorant.com%2Fredirect&response_type=code&scope=openid%20account%20email&show_region=true&state=ba7dcdf90946630a676f3848c8&uri=https%3A%2F%2Fplayvalorant.com%2Fen-us%2Fdownload")


email_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input'
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email_input_xpath)))
email_input.send_keys(cleaned_email)

checkbox_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[2]/label/input'
checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, checkbox_xpath)))
checkbox.click()


time.sleep(1)

submit_button_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button'
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
submit_button.click()

time.sleep(1)

number_8_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[1]/input'
number_8_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, number_8_input_xpath)))
number_8_input.send_keys("8")

number_08_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div[2]/input'
number_08_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, number_08_input_xpath)))
number_08_input.send_keys("08")

number_1999_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="input-birthday-year"]')))
number_1999_input.send_keys("1999")

final_submit_button_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button'
final_submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, final_submit_button_xpath)))
final_submit_button.click()

print(Fore.GREEN + f"Email: {cleaned_email}" + Fore.RESET)
print(Fore.GREEN + f"BirthDate: 08/08/1999" + Fore.RESET)  


time.sleep(1)

# Generate a unique username
username = generate_username()


username_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input'
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, username_input_xpath)))
username_input.send_keys(username)


submit_button_username_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/button'
submit_button_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_username_xpath)))
submit_button_username.click()


print(Fore.GREEN + f"Username '{username}' Successfully Generated." + Fore.RESET)


time.sleep(1)

# Generate a unique password
password, strength = generate_password()


password_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[1]/div/input'
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_input_xpath)))
password_input.send_keys(password)

password_confirm_input_xpath = '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/input'
password_confirm_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_confirm_input_xpath)))
password_confirm_input.send_keys(password)


submit_button_password_xpath = '//button[@data-testid="btn-signup-submit"]'
submit_button_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_password_xpath)))
submit_button_password.click()


print(Fore.GREEN + f"Successfully Generated password: {password} ({strength} strength)." + Fore.RESET)

# User prompt to keep the script running
input("Press Enter to exit the script.")


driver.quit()
