import os
import time
import smtplib, ssl
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()
context = ssl.create_default_context()

caps = [1, 1]
with open('cap.txt', 'r') as file:
  caps[0] = int(file.readline())
  caps[1] = int(file.readline())

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = f"{os.getenv('EMAIL')}"  # Enter your address
receiver_email = f"{os.getenv('RECEIVER')}"  # Enter receiver address
password = f"{os.getenv('PASSWORD')}"
messages = (
  """\
Subject: New A Trail of Blood Chapter

There's a new chapter of A Trail of Blood available!!.
""" + f"https://mangajar.com/manga/a-trail-of-blood/chapter/{caps[0]}",
  """\
Subject: New Boruto Chapter

There's a new chapter of Boruto available!!.
""" + f"https://scansexplorer.com.br/manga/boruto-naruto-next-generations/capitulo-{caps[1]}/"
)

PATH = 'C:\chromedriver.exe'

urls = [
  f"https://mangajar.com/manga/a-trail-of-blood/chapter/{caps[0]}",
  f"https://scansexplorer.com.br/manga/boruto-naruto-next-generations/capitulo-{caps[1]}/"
]

xpaths = [
  '/html/body/div[1]/div[2]/img[1]',
  '//*[@id="image-0"]'
]

option = Options()
option.headless = True
driver = webdriver.Chrome(PATH, options=option)

for i in range(0, len(urls)):

  driver.get(urls[i])
  time.sleep(5)

  try:
    if driver.find_element_by_xpath(xpaths[i]):
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messages[i])
      with open('cap.txt', 'w') as file:
        caps[i] += 1
        for cap in caps:
          file.write(f"{cap}\n")
  except:
    print('Not found')
  
driver.quit()