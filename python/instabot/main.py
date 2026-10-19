import os
from time import sleep
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--headless')


print("opening browser")
browser = webdriver.Firefox(options=options)
browser.implicitly_wait(15)

# try :
browser.get("https://www.instagram.com/")

allow_cookies = browser.find_element("xpath", "//button[text()='Allow all cookies']")
if allow_cookies:
    allow_cookies.click()

print("logging in")
# sleep(2)
username = browser.find_element(
    "xpath", "//input[contains(@aria-label, 'Phone number, username, or email')]"
)
# sleep(2)
password = browser.find_element("xpath", "//input[contains(@aria-label, 'Password')]")

username.send_keys("berna_thefaxmachine")
password.send_keys("bernaRules")

login_div = browser.find_element("xpath", "//div[text()='Log in']")
login_button = login_div.find_element("xpath", "./..")

browser.execute_script("arguments[0].click();", login_button)

print("uploading file")
# my_image.show()
create_button = browser.find_element("xpath", "//span[text()='Create']")
browser.execute_script("arguments[0].click();", create_button)

post_button = browser.find_element("xpath", "//span[text()='Post']")
browser.execute_script("arguments[0].click();", post_button)

# file to upload
upload_file = os.path.abspath('/fax/python/instabot/assets/test.png')

file_input = browser.find_element("xpath", "//form[contains(@role,'presentation')]/input")
file_input.send_keys(upload_file)

print("publishing post")
next_button = browser.find_element("xpath", "//div[text()='Next']")
browser.execute_script("arguments[0].click();", next_button)

sleep(2)

page_source = driver.page_source
print(page_source)

# next_button = browser.find_element("xpath", "//div[text()='Next']")
# if next_button :
#     browser.execute_script("arguments[0].click();", next_button)

# next_button = browser.find_element("xpath", "//div[text()='Share']")
# browser.execute_script("arguments[0].click();", next_button)

print("final")
sleep(10)
# except Exception as e :
  # print(e)
  # print('closing browser')
  # browser.close()
browser.close()
