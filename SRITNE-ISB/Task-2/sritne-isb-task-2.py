#!/usr/bin/env python
# coding: utf-8

# # TASK 2

# In[1]:


## Imporing all the necessary libraries

import pandas as pd
import warnings
import spacy
import en_core_web_sm
warnings.filterwarnings('ignore')

## Reading the company 'descriptions.xlsx' and 'Industry Segments - Top 10 Keywords.xlsx' using pandas library
company_data = pd.read_excel('Technical Analyst/company descriptions.xlsx')
industries = pd.read_excel('Technical Analyst/Industry Segments - Top 10 Keywords.xlsx')


# In[2]:


## Let's visualize the 'descriptions.xlsx' data 
company_data


# In[3]:


## Let's visualize the data 'Industry Segments - Top 10 Keywords.xlsx'
industries


# In[4]:


## Loading 'en_core_web_sm' for finding similaritites between two sentences by applying .similarity() method
nlp = en_core_web_sm.load()


# #### Let's see one of the company industry segment by applying spacy sentense similarity technique. As see can see in the `Industry Segments - Top 10 Keywords.xlsx` dataset after 26th column `NaN` values are there, so inorder to avoid those I had used python list slicing concept

# In[19]:



## Below code calculates sentense similarities by applying one of the company descriptions to all Industry segments, 
## and it stored to a list, in this case which gives maximum similarity will be the corresponding industry segment 

similar = []
m = 998
for (i,j) in zip(industries['Industry segment'][:27], industries['Tags'][:27]):
    token1 = nlp(company_data['company_description'][m])
    token2 = nlp( j )
    
    ## Here 'token1.similarity(token2)' returns similarity index value of token1 and token2
    ## appending similarity index value each time to the 'similar' list 
    
    ## Finding similaritites between two sentences by applying .similarity() method
    similar.append(token1.similarity(token2))
    

## Let's see here the Company Description and it's classification based on description
print(" Company Description : \n",nlp(company_data['company_description'][m]),"\n\n")

## Here similar.index(max(similar)) returns maximum similarity index value in the similar list 
## then by applying the resultant index to industries['Industry segment'] we will get company industry segment
print("Classification based on description =====>",industries['Industry segment'][similar.index(max(similar))])


# In[11]:



## And also check with some random company

similar = []
m = 43
for (i,j) in zip(industries['Industry segment'][:27], industries['Tags'][:27]):
    token1 = nlp(company_data['company_description'][m])
    token2 = nlp( j )
    
    ## Finding similaritites between two sentences by applying .similarity() method
    similar.append(token1.similarity(token2))
    
print(" Company Description : \n",nlp(company_data['company_description'][m]),"\n\n")
print("Classification based on description =====>",industries['Industry segment'][similar.index(max(similar))])


# #### The `company_data['company_description']` contains some `NaN` data, inorder to resolve that, I've used `company_data['company_short_description']`. In `company_data['company_short_description']` data there are no `NaN` values

# In[20]:



## Storing all the resultant company industry segments to list 'Classification'
classification = []

## Looping over company_data['company_description'] , company_data['company_short_description'] each time
for ( description, short_description ) in zip(company_data['company_description'] , 
                                              company_data['company_short_description']):
    
    ## similarity_score for single company by different Industry Tags 
    similarity_score = []
    
    ## As I mentioned earlier after 26th row there are NaN values in Industry Tags they are no more useful
    
    for tags in industries['Tags'][:27]:
        
        ## Checking if company_data['company_description'] is a NaN
        
        if type( description ) != float:
            
            ## For maintining description as same in each time I'm assigning description to desc
            desc = description
            description = nlp(description)
            tags = nlp(tags)
            
            ## Finding similaritites between two sentences by applying .similarity() method
            similarity_score.append(description.similarity(tags))
            description = desc
            
        else:
            ## For maintining short_description as same in each time I'm assigning short_description to desc
            desc = short_description
            short_description = nlp(short_description)
            tags = nlp(tags)
            
            ## Finding similaritites between two sentences by applying .similarity() method
            similarity_score.append(short_description.similarity(tags))
            short_description = desc
            
    ## appending classified industry segment of each description by applying 
    ## industries['Industry segment'][similarity_score.index(max(similarity_score))] in each company description        
    classification.append(industries['Industry segment'][similarity_score.index(max(similarity_score))])


# In[24]:


## Creating DataFrame for storing the results
Company_Industry_Segment = pd.DataFrame(zip(list(company_data['company_name']), classification),
                                     columns  = ["Company_Name", "Industry_Segment"])


# In[25]:


## Let's see the Company Industry Segment data
Company_Industry_Segment


# In[26]:


## Storing it to a CSV file 
Company_Industry_Segment.to_csv('Company_Industry_Segment.csv')


# In[157]:


## Count the number of occurances of each Industry Segment
Company_Industry_Segment.pivot_table( index = ['Industry_Segment'], aggfunc = 'size')


# In[155]:


print("\n\n")
print("Bar plot represents counting of companies based on industry segments")

## freq_counts is the number of occurances of each Industry Segment
freq_counts = Company_Industry_Segment.pivot_table( index = ['Industry_Segment'], aggfunc = 'size')
plt.figure(figsize = (12, 6))
freq_counts.plot.bar()
plt.xlabel('Industry Segment', color = 'r', fontsize = 15)
plt.ylabel('Counts', color = 'r', fontsize = 15)
sns.set_style('darkgrid')


# In[156]:


print("\n\n")
print("Pie plot represents percentage companies based on industry segments")
plt.figure(figsize = (20, 10))
freq_counts.plot.pie()
plt.ylabel('Industry segments and percentages', color = 'r', fontsize = 15)
sns.set_style('darkgrid')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




