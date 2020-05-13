#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

URL = 'https://www.tourradar.com/d/mumbai#month=september-2020'
page = requests.get(URL)


# In[3]:


print (page.content)


# In[22]:


import requests
from bs4 import BeautifulSoup

URL = 'https://www.tourradar.com/d/mumbai#month=september-2020'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


# In[12]:


print(soup)


# In[30]:


results = soup.findAll("div", {"class": "br__price-wrapper"})


# In[31]:


print(results)


# In[ ]:





# In[30]:





# In[32]:


for job_elem in results:
    print(job_elem, end='\n'*5)


# In[82]:


fullo =[]
days=[]
avg_price_per_day=[]


# In[83]:


for job_elem in results:
    title_elem = job_elem.findAll("dd", {"class": "br__price-wrapper-info-description"})
    if None in (title_elem):
        continue
    for indi in title_elem:
        fullo.append(indi.text.strip())
        print(indi.text.strip(), end='\n')
    


# In[84]:


for i in range(len(fullo)):
    if (i%2 != 0):
        avg_price_per_day.append(fullo[i]) 
    else:
        days.append(fullo[i])
            


# In[85]:


print(avg_price_per_day)
print(days)


# In[ ]:




