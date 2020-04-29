#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Importing all the necessary modules to scrap data from web

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(executable_path='C:/Users/pAndu/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=option)


# In[2]:


browser.get('https://www.zaubacorp.com/company/RELIANCE-INDUSTRIES-LIMITED/L17110MH1973PLC019786')


# In[3]:


from bs4 import BeautifulSoup
soup_level1 = BeautifulSoup(browser.page_source, 'html5lib')


# In[4]:


print(soup_level1.prettify())


# In[31]:


Company_Information = soup_level1.find("table", attrs = {"class":"table table-striped"}).getText()


# In[42]:


print("Company Information:")
print(CIN)


# In[44]:


contact_details = soup_level1.find("div", attrs = {"class":"col-12"}).getText()
print("Contact Details:", contact_details)


# In[45]:


directors = soup_level1.find_all("tr",attrs = {"data-parent":"#OrderPackages"})
print("Company Directors Information:")
for i in directors:
    print(i.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




