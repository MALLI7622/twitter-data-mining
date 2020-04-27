#!/usr/bin/env python
# coding: utf-8

# # TASK 1

# In[21]:


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


## Reading contents of  state_links.csv using pandas library

import pandas as pd
data = pd.read_csv("Technical Analyst/state_links.csv")


# In[3]:


## Displaying the data of state_links.csv
data


# In[15]:


## Importing BeautifulSoup module from bs4 library which is helpful in dealing with scraped data 
from bs4 import BeautifulSoup


# In[22]:


## Let's scrap the data of first url in the state_links.csv

# the below function opens the url in Chrome browser

browser.get("https://www.naukri.com/jobs-in-andhra-pradesh")


# In[23]:


## Below line of code reads the html code of the url

soup_level1 = BeautifulSoup(browser.page_source, 'html5lib')


# In[24]:


## Let's see the html code we get

print(soup_level1.prettify())


# #### As per the task we've have to retrieve information of job titles, company name, Experience, Salary, Location, Description, Date Posted, 
# #### Tags of the job, Scraping Date
# 
# #### Let's see the information of one of the job 

# In[25]:


## datetime library deals with retrieving dates, and times of present
from datetime import date

## Now we're retrieving information of first link,
## state is
print("State:", data['state_links'][0][31:])

## Below line code finds the class `title fw500 ellipsis` with tag a i.e., <a>. getText() method retrieves text from that class
## that is Job title of of the first job. It is similar to all the details. But the function gets only first item. 
job_title = soup_level1.find("a",attrs={"class": "title fw500 ellipsis"}).getText()
print("Job Title:",job_title)

## Retrieves Company name, code is similar to Job title
Company = soup_level1.find("a",attrs={"class": "subTitle ellipsis fleft"}).getText()
print("Company:",Company)

## Retrieves Experience, code is similar to Job title
Experience = soup_level1.find("li",attrs={"class": "fleft grey-text br2 placeHolderLi experience"}).getText()
print("Experience:",Experience)

## Retrieves Salary, code is similar to Job title
salary = soup_level1.find("li",attrs={"class": "fleft grey-text br2 placeHolderLi salary"}).getText()
print("Salary:",salary)

## Retrieves Location, code is similar to Job title
Location = soup_level1.find("li",attrs={"class": "fleft grey-text br2 placeHolderLi location"}).getText()
print("Location:",Location)

## Retrieves Description, code is similar to Job title
Description = soup_level1.find("div",attrs={"class": "job-description fs12 grey-text"}).getText()
print("Description:",Description)

## Retrieves Date posted, code is similar to Job title
Date_posted = soup_level1.find("div",attrs={"class": "type br2 fleft grey"}).getText()
print("Date Posted:",Date_posted)

## Retrieves Tags of the job, code is similar to Job title
Tags = soup_level1.find("ul",attrs={"class": "tags has-description"}).getText()
print("Tags:",Tags)

## printing scraping date by using date module from datetime library
print("Scraping Date:", date.today())


# In[38]:


## Below is the similar line of code as above, but in this case find_all method retrieves all the classes with given tag

## Finding all the Job titles using 'title fw500 ellipsis' class and <a> tag. 
## Because the text is found in that class and the tag.
Job_Titles = soup_level1.find_all("a",attrs={"class": "title fw500 ellipsis"})

## Finding all exeperiences of job profiles using class 'fleft grey-text br2 placeHolderLi experience' and <li> tag.
Experiences = soup_level1.find_all("li",attrs={"class": "fleft grey-text br2 placeHolderLi experience"})

## Finding all salaries of job profiles using class 'fleft grey-text br2 placeHolderLi salary' and <li> tag.
Salaries = soup_level1.find_all("li",attrs={"class": "fleft grey-text br2 placeHolderLi salary"})

## Finding all Locations of job profiles using class 'fleft grey-text br2 placeHolderLi location' and <li> tag.
Locations = soup_level1.find_all("li",attrs={"class": "fleft grey-text br2 placeHolderLi location"})

## Finding all descriptions of job profiles using class 'job-description fs12 grey-text' and <div> tag.
Descriptions = soup_level1.find_all("div",attrs={"class": "job-description fs12 grey-text"})

## Finding all descriptions of job profiles using class 'jobTupleFooter mt-20' and <div> tag.
Dates_posted = soup_level1.find_all("div",attrs={"class": "jobTupleFooter mt-20"})

## ## Finding all descriptions of job profiles using class 'tags has-description' and <ul> tag.
Tags_associated = soup_level1.find_all("ul",attrs={"class": "tags has-description"})


# In[27]:


from datetime import date

## Creating lists of same name by storing information, which is also helpful in storing this information in a DataFrame

JOB_TITLES = []
EXPERIENCE = []
SALARY = []
LOCATIONS = []
DESCRIPTION = []
DATES_POSTED = []
TAGS_ASSOCIATED = []

## The data which we get in the above is in html code format, but we need in complete text format. So, to do this 
## I had created a for loop each time it takes one value and also created a zip which takes one 
## one value from all the lists for reducing the time complexity


for (job, exp, sal, loc, desc, date, tags) in zip(Job_Titles, Experiences, Salaries, Locations, 
                                                  Descriptions, Dates_posted, Tags_associated):
    
    ## job.text gets only text in between the class it is similar to all.
    JOB_TITLES.append(job.text)
    EXPERIENCE.append(exp.text)
    SALARY.append(sal.text)
    LOCATIONS.append(loc.text)
    DESCRIPTION.append(desc.text)
    DATES_POSTED.append(date.text)
    TAGS_ASSOCIATED.append(tags.text)
    
    ## Here, I am storing all Job profiles of Andhra Pradhesh State in a Data Frame
    Job_Profiles = pd.DataFrame(list(zip([data['state_links'][0][31:]] * len(DATES_POSTED), JOB_TITLES, EXPERIENCE, LOCATIONS,
                                     DESCRIPTION, TAGS_ASSOCIATED, DATES_POSTED,
                                         [str(scrap_date)] * len(DATES_POSTED)))
                            , columns = ['state','Job Title', 'Experience','Locations','Description',
                                         'Tags Associated','Dates posted','Scraped data'])
    


# In[28]:


## Let's see the Job profiles of Andhra Pradhesh State
Job_Profiles


# In the above we'd seen only one state job profiles, Now we are going to see all the job profiles of the corresponding links that are found in the file `state_links.csv`

# In[29]:


## get_length function is used for getting the no.of jobs in each state which will be helpful creating DataFrame i.e, for each 
## state we've N no.of jobs. So, we've to create N no.of states in a DataFrame and it'll helpful in scrap_date list
def get_length(jobs):
    count = 0
    for i in jobs:
        count += 1
    return count


# In[33]:


from datetime import date

## returns today's date
today = date.today()


format = "%a %b %d"
## display date in DAY-MONTH-DATE format i.e., Mon Apr 27 
scrap_date = today.strftime(format)

## Creating DataFrame for storing the results.
result = pd.DataFrame()

## Below code is mostly similar to the above, but in this case we are retriving state_links information by one by one using 
## for loop. It loops over all the links in the 'state_links.csv'
for i in data['state_links']:
    browser.get(i)
    soup_level1=BeautifulSoup(browser.page_source, 'html5lib')
    Job_Titles = soup_level1.find_all("a",attrs={"class": "title fw500 ellipsis"})
    Experiences = soup_level1.find_all("li",attrs={"class": "fleft grey-text br2 placeHolderLi experience"})
    Salaries = soup_level1.find_all("li",attrs={"class": "fleft grey-text br2 placeHolderLi salary"})
    Locations = soup_level1.find_all("li",attrs={"class": "fleft grey-text br2 placeHolderLi location"})
    Descriptions = soup_level1.find_all("div",attrs={"class": "job-description fs12 grey-text"})
    Dates_posted = soup_level1.find_all("div",attrs={"class": "jobTupleFooter mt-20"})
    Tags_associated = soup_level1.find_all("ul",attrs={"class": "tags has-description"})
    JOB_TITLES = []
    EXPERIENCE = []
    SALARY = []
    LOCATIONS = []
    DESCRIPTION = []
    DATES_POSTED = []
    TAGS_ASSOCIATED = []
    SCRAPING_DATE = []
    
    ## Here I'm creating N no.of same states storing in a list for adding it to DataFrame
    ## N = Job Profiles in a state 
    state = [i[31:]] * get_length(Job_Titles)
    
    ## storing scraping date in N times in a list for adding it to DataFrame
    scrap_dates = [str(scrap_date)] * get_length(Job_Titles)
    
    ## Below code is similar to the above in case of one state 
    for (job, exp, sal, loc, desc, date, tags) in zip(Job_Titles, Experiences, Salaries, Locations, Descriptions,
                                                      Dates_posted, Tags_associated):
        JOB_TITLES.append(job.text)
        EXPERIENCE.append(exp.text)
        SALARY.append(sal.text)
        LOCATIONS.append(loc.text)
        DESCRIPTION.append(desc.text)
        DATES_POSTED.append(date.text)
        TAGS_ASSOCIATED.append(tags.text)
        Job_Profiles = pd.DataFrame(list(zip(state, JOB_TITLES, EXPERIENCE, LOCATIONS, 
                                     DESCRIPTION, TAGS_ASSOCIATED, DATES_POSTED, scrap_dates))
                            , columns = ['state','Job Title', 'Experience','Locations','Description',
                                         'Tags Associated','Dates posted','Scraped date'])
        
        
        ## Finally adding job profiles of each state information to 'result' DataFrame
        result = pd.concat([result, Job_Profiles])


# In[34]:


## Let's look at the results
result


# In[43]:


## Storing the results in a csv file
result.to_csv('task1-naukri-results.csv')


