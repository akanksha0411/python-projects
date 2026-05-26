from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "YOUR TINDOG URL"
FACEBARK_EMAIL = "any-email@example.com"
FACEBARK_PASSWORD = "anything"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, "button[class^='btn-tindog-login']")
login_button.click()
sleep(1)

facebark_btn = driver.find_element(By.CSS_SELECTOR, "button[class^='btn-facebark']")
facebark_btn.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, "email")
email.send_keys(FACEBARK_EMAIL)
password = driver.find_element(By.ID, "pass")
password.send_keys(FACEBARK_PASSWORD)
fb_login_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button")
fb_login_btn.click()

sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

allow_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
allow_btn.click()

no_notif_btn = driver.find_element(By.CLASS_NAME, "btn-secondary")
no_notif_btn.click()

accept_cookies_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
accept_cookies_btn.click()

sleep(1)

for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)
