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
options = Options()
options.add_argument("--headless")
username = os.getenv('US')
pwd = os.getenv('pwd')
url = "https://sso.satitm.chula.ac.th/adfs/oauth2/authorize?response_type=code&client_id=9d7865f9-7fe8-490f-bb72-25defaf77212&redirect_uri=https%3A%2F%2Fwww.mycourseville.com%2Fapi%2Fsatitm%2Fcallback"

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver",options=options))
driver.get(url)


driver.find_element(By.ID,"userNameInput").send_keys(username)
driver.find_element(By.ID,"passwordInput").send_keys(pwd)
driver.find_element(By.ID,"submitButton").click()

print("login succesfully")

driver.get("https://www.mycourseville.com/api/oauth/authorize?response_type=code&client_id=smartschool_cudplus&redirect_uri=https://cudplus.onsmart.school/callback&scope=public,launching,email")

driver.get("https://cudplus.onsmart.school/utility/notifications")

sleep(2)
e = driver.find_elements(By.TAG_NAME,"ul")

print(e[2].text.split(" "))
notiraw=e[2].text.split(" ")
notiraww=[]
for i in notiraw:

    if "\n" in i:
        notiraww.append(i.split("\n")[0])
        notiraww.append(i.split("\n")[1])

    else:
        notiraww.append(i)

print(notiraww)
noti=[]
for j in notiraww:
    noti.append(j)
    if "แล้ว" in j:
        noti.append("/")
print(noti)
notlist=split_list(noti,"/")

print(notlist)
prime=[]
for q in notlist:
    prime.append(" ".join(q))
print(prime)
with open("log.txt","a") as file:
    file.write(" , ".join(prime) + "\n")
driver.quit()