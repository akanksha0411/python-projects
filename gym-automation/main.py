from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "YOUR_EMAIL"
ACCOUNT_PASSWORD = "YOUR_PASSWORD"
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, timeout=2)

login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_input = wait.until(ec.element_to_be_clickable((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(by=By.ID, value="password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_button = driver.find_element(by=By.ID, value="submit-button")
submit_button.click()

# After logging in, we wait for the class schedule page to load
wait.until(ec.element_to_be_clickable((By.ID, "schedule-page")))

booked_cnt = 0
alr_booked_cnt = 0
waitlist_cnt = 0
processed_classes = []
# ./ancestor::div[contains(@id, 'day-group-')]

# Finding individual class cards
class_cards = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='class-card-']")
for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    print(day_title)
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(by=By.CSS_SELECTOR, value="p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(by=By.CSS_SELECTOR, value="h3[id^='class-name-']").text
            book_button = card.find_element(by=By.CSS_SELECTOR, value="button[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"
            if book_button.text == "Booked":
                print(f"✅ Already Booked: {class_name} on {day_title}")
                alr_booked_cnt += 1
                processed_classes.append(f"[Booked] {class_info}")
            elif book_button.text == "Waitlisted":
                print(f"✅ Already on waitlist: {class_info}")
                alr_booked_cnt += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif book_button.text == "Book Class":
                book_button.click()
                booked_cnt += 1
                processed_classes.append(f"[New Booking] {class_info}")
                print(f"✅ Booked: {class_info}")
                time.sleep(0.5)
            elif book_button.text == "Join Waitlist":
                book_button.click()
                waitlist_cnt += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                print(f"✅ Joined waitlist for: {class_info}")
                time.sleep(0.5)

# Booking summary

print("\n BOOKING SUMMARY")
print(f"Classes booked {booked_cnt}.")
print(f"Waitlists joined {waitlist_cnt}.")
print(f"Already booked/waitlisted {alr_booked_cnt}.")
print(f"Total Tuesday 6pm classes processed: {booked_cnt + waitlist_cnt + alr_booked_cnt}")
# driver.quit()

print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
    print(f"  • {class_detail}")
