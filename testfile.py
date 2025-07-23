import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from sys import *
import os
from dotenv import load_dotenv
import tempfile

from email.message import EmailMessage
import ssl
import smtplib
import requests
from datetime import date
from bs4 import BeautifulSoup

load_dotenv()
def split_list(lst, delimiter):
    result = []
    current = []
    for item in lst:
        if item == delimiter:
            result.append(current)
            current = []
        else:
            current.append(item)
    result.append(current)  # Add the last segment
    return result

#options.add_argument("--headless")

username = os.getenv('US')
pwd = os.getenv('pwd')
url="https://www.mycourseville.com/api/login"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"),
    options=chrome_options
)
driver.get(url)




driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(pwd)
driver.find_element(By.ID,"cv-login-cvecologinbutton").click()
print("login succesfully")
sleep(1)

driver.get("https://www.mycourseville.com/api/oauth/authorize?response_type=code&client_id=smartschool_cudplus&redirect_uri=https://cudplus.onsmart.school/callback&scope=public,launching,email")

driver.get("https://cudplus.onsmart.school/utility/notifications")
driver.get("https://cudplus.onsmart.school/lms/homework?course=14511&homework=67058")
sleep(2)
v = driver.find_element(By.CSS_SELECTOR,".ss-component-section-body")
print(v.text)