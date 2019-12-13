```
#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless --autoplay-policy=no-user-gesture-required")

base_url = "https://www.youtube.com/watch?v=RktaL51BVLs"
#对应的chromedriver的放置目录
driver = webdriver.Chrome(executable_path=(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'), chrome_options=chrome_options)

driver.get(base_url + "")

start_time=time.time()
print('this is start_time ',start_time)
video = driver.find_elements_by_xpath("/html/body/video")
time.sleep(10000)#这里要sleep一下，否则driver打开后会立即关闭
driver.close()
end_time=time.time()
print('this is end_time ',end_time)
```
