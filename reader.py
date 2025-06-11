

from email.message import EmailMessage
import ssl
import smtplib
import requests
from datetime import date
from bs4 import BeautifulSoup


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

print(a)
print(set(a[0]).difference(set(a[1])))


res=[str(set(a[0]).difference(set(a[1])))]
pwd = "pttq izsc qslj unns"
sender="why1spr.socute@gmail.com"
if res!=[] or res!=[""] or res!="set()":
    for i in res:
        reciever = "kittiphasa29@gmail.com"
        subjecst = i
        body= ""
        em = EmailMessage()
        em['From']= sender
        em['To'] = reciever
        em['Subject']= subject
        em.set_content(body)
        con = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=con) as smtp:
            smtp.login(sender,pwd)
            smtp.sendmail(sender,reciever,em.as_string())

