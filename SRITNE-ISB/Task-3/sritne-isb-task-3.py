#!/usr/bin/env python
# coding: utf-8

# # Task 3

# In[4]:


## Importing all the necessary lilbraries
import os
import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
import spacy
import codecs
import en_core_web_sm


## Imporing en_core_web_sm for finding similaritites between two sentences by applying .similarity() method
nlp = en_core_web_sm.load()


# In[5]:


## Lists the directories in the directory '10K-SNP500/' 
os.listdir('10K-SNP500/')


# #### Let take look at one of the file randomly choosen

# In[6]:



## Opening file
file = codecs.open("101829.html", "r", "utf-8")

## The file is html extension, so inorder to get the actual content without html tags we've to BeautifulSoup library
doc = BeautifulSoup(file.read()).getText()

## splitting the document, because we have to find the ocuurances in the file
text = doc.split()

## assining zeros to counts of high_competition and technology_competition
high_competition = 0
technology_competition = 0

## Iterating over the text containing words
for index,word  in enumerate(text):
    
    ## If word is 'competition' adding previous word to 'competition'
    if word == 'competition':
        print("Searched word: \t",text[index-1]+" "+'competition')
        
        token1 = nlp(text[index-1]+" "+'competition')
        
        ## Here, I am using similarity index of the text to 'high competition' and 'technological competition'
        ## the value which is more will add a count, and also some times the words we got by searching is 
        ## not relavant or not synonyms to either 'high competition' or 'technological competition'
        ## in this case, I had a threshold if the value is greater than only count adds, otherwise it won't 
        
        ## Finding similaritites between two sentences by applying .similarity() method
        print("high competition :",token1.similarity(nlp("high competition")))
        print("technological competition:", token1.similarity(nlp("technological competition")), "\n")
        if token1.similarity(nlp("high competition")) > token1.similarity(nlp("technological competition")):
            
            ## I choose threshhold value is 0.5, the best value we choose we get best results
            if token1.similarity(nlp("high competition")) > 0.5:
                
                high_competition += 1
        
        else:
            if token1.similarity(nlp("technological competition")) > 0.5:
                
                technology_competition += 1
            
    elif word == "competitors":
        print("Searched Word:\t", text[index-1]+" "+'competitors')
        token1 = nlp(text[index-1]+" "+'competitors')
        ## Here, I am using similarity index of the text to 'high competitors' and 'technological competitors'
        ## the value which is more will add a count, and also some times the words we got by searching is 
        ## not relavant or not synonyms to either 'high competitors' or 'technological competitors'
        ## in this case, I had a threshold if the value is greater than only count adds, otherwise it won't 
        
        ## Finding similaritites between two sentences by applying .similarity() method
        print("high competitors :",token1.similarity(nlp("high competitors")))
        print("technological competitors:", token1.similarity(nlp("technological competitors")), "\n")
        
        ## I choose threshhold value is 0.5, the best value we choose we get best results
        if token1.similarity(nlp("high competitors")) > token1.similarity(nlp("technological competitors")):
            if token1.similarity(nlp("high competitors\n")) > 0.5:
                
                high_competition += 1
                
        else:
            
            if token1.similarity(nlp("technological competitors")) > 0.5:
                technology_competition += 1
                

## printing counts of phrase occurances of high competition and technological competetion of file '101829.html'
print("high_competition: ", high_competition)
print("technology_competition:", technology_competition)


# In[116]:



## folder name
string = '10K-SNP500/'

## Storing final results in final_results DataFrame
final_results = pd.DataFrame()


## Iterated over all the folders in '10K-SNP500/' directory
for year in os.listdir(string)[1:]:
    string = string + year
    
    ## Printing folder name, tell us which folder we are in.
    print("Year ===> ", year)
    
    ## Iterate over files in each folder(year) in the directory '10K-SNP500/'
    for file in os.listdir(string)[1:]:
        
        ## Making path to each file in the folder
        string = string+"/" + file
        
        ## Opening file
        file = codecs.open(string, "r", "ISO-8859-1")
        
        ## The file is html extension, so inorder to get the actual content without html tags we've to BeautifulSoup library
        doc = BeautifulSoup(file.read()).getText()
        
        ## Adding each file information at the end we need file name, then file name as string[16:]
        file_name = string[16:]
        
        ## After Iterating each time string(path) should be same as original 
        string = string[:15]
        
        ## splitting the document, because we have to find the ocuurances in the file
        doc = doc.split()
        
        ## assining zeros to counts of high_competition and technology_competition
        high_competition = 0
        technology_competition = 0
        
        ## Iterating over the text containing words
        for index,word  in enumerate(doc):
            
            ## If word is 'competition' adding previous word to 'competition'
            if word == 'competition':
                
                ## Here, I am using similarity index of the text to 'high competition' and 'technological competition'
                ## the value which is more will add a count, and also some times the words we got by searching is 
                ## not relavant or not synonyms to either 'high competition' or 'technological competition'
                ## in this case, I had a threshold if the value is greater than only count adds, otherwise it won't 
                
                searched_word = doc[index-1]+" "+'competition'
                searched_word = nlp(searched_word)
                
                if searched_word.similarity(nlp("high competition")) > searched_word.similarity(nlp("technological competition")):
                    
                    ## I choose threshhold value is 0.5, the best value we choose we get best results
                    if searched_word.similarity(nlp("high competition")) > 0.5:
                
                        high_competition += 1
        
                else:
                    if searched_word.similarity(nlp("technological competition")) > 0.5:
                
                        technology_competition += 1
            
            elif word == "competitors":
                
                ## Here, I am using similarity index of the text to 'high competitors' and 'technological competitors'
                ## the value which is more will add a count, and also some times the words we got by searching is 
                ## not relavant or not synonyms to either 'high competitors' or 'technological competitors'
                ## in this case, I had a threshold if the value is greater than only count adds, otherwise it won't 
                
                searched_word = doc[index-1]+" "+'competitors'
                searched_word = nlp(searched_word)
                
                ## I choose threshhold value is 0.5, the best value we choose we get best results
                if searched_word.similarity(nlp("high competitors")) > searched_word.similarity(nlp("technological competitors")):
                    if searched_word.similarity(nlp("high competitors\n")) > 0.5:
                
                        high_competition += 1
                
                else:
            
                    if searched_word.similarity(nlp("technological competitors")) > 0.5:
                        
                        technology_competition += 1
    
        result = pd.DataFrame([[year, file_name, high_competition, technology_competition]], 
                             columns = ['YEAR', 'FILE_NAME', 'COUNT_OF_HIGH_COMPETITION', 'COUNT_OF_TECNOLOGICAL_COMPETITION'])
        final_results = pd.concat([result, final_results], ignore_index = True)
    string = string[:11]
 


# In[117]:


## Let's see the results of the DataFrame
final_results


# In[118]:


## Storing the results of the DataFrame to CSV file
final_results.to_csv('competition_occurances.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




