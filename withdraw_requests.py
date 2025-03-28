import time
import pickle
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read login credentials from file
with open("credentials.txt", "r") as file:
    lines = file.readlines()
    email = lines[0].strip()
    password_value = lines[1].strip()

# Set up Firefox options
firefox_options = FirefoxOptions()
firefox_options.add_argument("--detach")  # Keeps the browser open

# Initialize the Firefox driver
driver = webdriver.Firefox(options=firefox_options)
wait = WebDriverWait(driver, 10)

# Check if cookies exist
cookie_file = f"{email}.pkl"
try:

    driver.get("https://www.instagram.com/")

    cookies = pickle.load(open(cookie_file, "rb"))
    time.sleep(2)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://www.instagram.com/")

    time.sleep(5)
    print("Logged in using saved cookies.")

except FileNotFoundError:
    print("Cookies not found. Logging in manually...")
    driver.get("https://www.instagram.com/accounts/login/?hl=en")

    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
    email_input.send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    password_input.send_keys(password_value)
    password_input.send_keys(Keys.ENTER)

    time.sleep(8)  # Wait for login

    code = input("Enter 2FA Code: ")  # User manually inputs the code
    verify = wait.until(EC.element_to_be_clickable((By.NAME, 'verificationCode')))
    verify.send_keys(code)
    verify.send_keys(Keys.ENTER)

    time.sleep(5)  # Wait for verification

    # Save cookies
    cookies = driver.get_cookies()

    with open(cookie_file, "wb") as file:
        pickle.dump(cookies, file)

    time.sleep(2)

# Read profile links from Excel
df = pd.read_excel("requests.xlsx", header=None)
profile_links = df.iloc[::2, 0].dropna().tolist()  # Extracting links from odd-numbered rows

# Withdraw requests
for index, link in enumerate(profile_links):
    try:
        driver.get(link)
        time.sleep(random.randint(4, 7))  # Random wait time before interacting

        # Click on "Requested" button
        requested_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._acan._acap._acat._aj1-._ap30")))
        requested_button.click()

        time.sleep(random.randint(5, 9))  # Random wait before confirmation

        # Confirm Unfollow (if prompted)
        try:
            confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--._ap36._a9-_")))
            confirm_button.click()
        except:
            pass  # If no confirmation prompt, continue

        print(f"✅ Withdrawn request from: {link}")

        # Wait randomly after each withdrawal
        wait_time = random.randint(30, 90)  # Random wait between 30 to 90 seconds
        print(f"⏳ Waiting {wait_time} seconds before next request...")
        time.sleep(wait_time)

        # After one request, wait 8-12 minutes randomly
        if (index + 1) % 1 == 0:
            long_wait = random.randint(480, 720)  # 8 to 12 minutes
            print(f"⏳ Taking a break for {long_wait//60} minutes...")
            time.sleep(long_wait)

    except Exception as e:
        print(f"❌ Failed to withdraw request from {link}: {e}")

# Close the browser
driver.quit()
