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

driver.get("https://www.mycourseville.com/api/oauth/authorize?response_type=code&client_id=smartschool_cudplus&redirect_uri=https://cudplus.onsmart.school/callback&scope=public,launching,email")

driver.get("https://cudplus.onsmart.school/utility/notifications")
sleep(2)
links = driver.find_elements(By.TAG_NAME, "a")  # gets all <a> elements
hrefs=[]
for link in links:
    href = link.get_attribute("href")

    hrefs.append(href)
print(hrefs[19:])


e = driver.find_elements(By.TAG_NAME,"ul")

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
    if "แล้ว" in j and "ใกล้จะถึงกำหนดส่งแล้ว" not in j and "ได้รับการตรวจแล้ว" not in j:
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
#Reader



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

a=[]
g=[]
with open('log.txt') as f:
    
    for x in f:
        g.append(x)
    g=g[-2:]
    for r in g:
        a.append(r.split(",")[0:-1])

for k in range(len(a[0])):
    if "วันที่แล้ว" in a[0][k]:
        a[0][k]=a[0][k][0:-13]
    elif "ชั่วโมงที่แล้ว" in a[0][k]:
        a[0][k]=a[0][k][0:-17]
    elif "เดือนที่แล้ว" in a[0][k]:
        a[0][k]=a[0][k][0:-15]
    elif "สัปดาห์ที่แล้ว" in a[0][k]:
        a[0][k]=a[0][k][0:-17]

    
for s in range(len(a[1])):
    if "วันที่แล้ว" in a[1][s]:
        a[1][s]=a[1][s][0:-13]
    elif "ชั่วโมงที่แล้ว" in a[1][s]:
        a[1][s]=a[1][s][0:-17]
    elif "เดือนที่แล้ว" in a[1][s]:
        a[1][s]=a[1][s][0:-15]
    elif "สัปดาห์ที่แล้ว" in a[1][s]:
        a[1][s]=a[1][s][0:-17]

    
print(a[1])
dummy=0
for i in a[0]:
    for j in a[1]:
        print(i)
        print(j)
        print("")

        if i==j:
            print("yay")
            first = a[0].index(i)
            later = a[1].index(i)
            dummy=1
            break
    if dummy==1:
        break
print(first,later)
print(a[1][0:later])
if first ==0 and later ==0:
    eme=[]
else:
    eme=a[1][0:later-1]
print(eme)
ps = os.getenv('pc')
sender=os.getenv('sender')
if eme!=[]:
    print("notifications founded")
    for i in eme:
        reciever = "kittiphasa29@gmail.com"
        subject = i
        body= hrefs[19:][eme.index(i)]
        em = EmailMessage()
        em['From']= sender
        em['To'] = reciever
        em['Subject']= subject
        em.set_content(body)
        con = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=con) as smtp:
            smtp.login(sender,ps)
            smtp.sendmail(sender,reciever,em.as_string())
else:
    print("no noti found")

