

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
for k in range(len(a[0])):
    a[0][k]=a[0][k][0:-13].strip()
for s in range(len(a[1])):
    a[1][s]=a[1][s][0:-13].strip()
print(a[1])
print(a[0])
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

