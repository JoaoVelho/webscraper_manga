import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    with open('cap.txt', 'w') as file:
      cap += 1
      file.write(str(cap))
except:
  print('Not found')
  
driver.quit()