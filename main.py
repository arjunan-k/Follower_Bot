# --------------------------------------------Setting the selenium webdriver------------------------------ #

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# setting the chrome driver path and login url and details.

chrome_path = Service(r"C:\Users\user\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_path)
INSTA_URL = "https://www.instagram.com/"
USERNAME = "Type your username"
PASSWORD = "Type your password"
driver.get(url=INSTA_URL)
time.sleep(3)

# filling the login details.

username = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]'
                                         '/div[2]/form/div/div[1]/div/label/input')
username.click()
time.sleep(3)
username.send_keys(USERNAME)
passsword = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]'
                                          '/div[2]/form/div/div[2]/div/label/input')
passsword.click()
time.sleep(3)
passsword.send_keys(PASSWORD)
log_in = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/'
                                       'div[1]/div[2]/form/div/div[3]/button')
log_in.click()
time.sleep(5)

# clicking on the two pop-ups.

not_now = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
not_now.click()
time.sleep(3)
not_now1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/'
                                         'div/div/div/div/div/div[3]/button[2]')
not_now1.click()
time.sleep(5)

# searching the required one you need.

search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/'
                                       'div[2]/div/div/div[2]/div[1]/div/span')
search.click()
time.sleep(2)
search1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/'
                                        'div[2]/div/div/div[2]/input')
search1.send_keys("cristiano")
time.sleep(2)

# clicking on the profile and following his followers.

cristiano = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/'
                                          'div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]'
                                          '/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]')
cristiano.click()
time.sleep(5)
followers = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/'
                                          'main/div/header/section/ul/li[2]/a/div')
followers.click()
time.sleep(2)

# getting the list of followers

all_followers = driver.find_elements(By.CSS_SELECTOR, '._aaey button')

# following each of the followers.

for each in all_followers:
    try:
        each.click()
    except NoSuchElementException:
        continue

# --------------------------------------------Process finished-------------------------------------------- #