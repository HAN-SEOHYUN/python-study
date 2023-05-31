#!/usr/bin/env python
# coding: utf-8

# In[3]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[ ]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_element(By.CSS_SELECTOR,"#input")
elem.send.keys("바다")
elem.send_keys(Keys.RETURN)



# In[ ]:


import time
elem = driver.find_element(By.TAG_NAME,"body")
for i in range(60):
  elem.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.1)

try:
  driver.find_element(By.CSS_SELECTOR,''.click())
  
  for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

except:
  pass


# In[ ]:


links=[]
images=driver.find_elements(By.CSS_SELECTOR, "")

for image in images:
  if image.get_attribute('src') is not None:
    links.append(image.get_attribute('src'))
    
print ('찾은 이미지 개수:', len(links))


# In[ ]:


import urllib.request

for i,k in enumerate(links):
  url = k
  urllib.request.urlretrieve(url, "src/project19/사진다운로드/"+str(i)+".jpg")
  
print('다운로드 완료하였습니다.')

