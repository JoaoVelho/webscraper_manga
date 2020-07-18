import os
import time
import smtplib, ssl
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()
context = ssl.create_default_context()

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.getenv('EMAIL')  # Enter your address
receiver_email = os.getenv('RECEIVER')  # Enter receiver address
password = os.getenv('PASSWORD')
message = """\
Subject: New A Trail of Blood Chapter

There's a new chapter of A Trail of Blood available!!."""

PATH = '/mnt/c/Users/ADM/downloads/chromedriver.exe'

with open('cap.txt', 'r') as file:
  cap = int(file.read())
url = f"https://mangajar.com/manga/a-trail-of-blood/chapter/{cap}"

option = Options()
option.headless = True
driver = webdriver.Chrome(PATH, options=option)

driver.get(url)

try:
  if driver.find_element_by_xpath('/html/body/div[1]/div[2]/img[1]'):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
    with open('cap.txt', 'w') as file:
      cap += 1
      file.write(str(cap))
except:
  print('Not found')
  
driver.quit()