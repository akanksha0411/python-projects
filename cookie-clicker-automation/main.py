from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import random
from selenium_stealth import stealth
import os

URL = "https://orteil.dashnet.org/cookieclicker/"
user_data_dir = os.path.join(os.getcwd() + "chrome_profile")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True)

driver.get(URL)

sleep(random.uniform(3, 7))

print("Looking for language selection ....")
try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    language_button.click()
    sleep(random.uniform(3, 7))
except NoSuchElementException:
    print("No language selection found")

sleep(random.uniform(3, 7))

cookie = driver.find_element(by=By.ID, value="bigCookie")
store_items = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time
five_mins = time() + 60*5

while True:
    cookie.click()
    if time() > timeout:
        try:
            current_cookie_count = driver.find_element(by=By.ID, value="cookies")
            count_text = current_cookie_count.text
            cookie_count = int(count_text.split()[0].replace(",", ""))

            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
                if best_item:
                    best_item.click()
                    print(f"Bought item: {best_item.get_attribute('id')}")
        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")
        timeout = time() + wait_time


    if time() > five_mins:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break

driver.quit()
