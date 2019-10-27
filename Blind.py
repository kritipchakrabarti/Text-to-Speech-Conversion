#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Using the file present in the directory
import docx
def ReadingTextDocuments(filename):
    doc=docx.Document(filename)
    
    completedText = []
    
    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)
    
    return '\n'.join(completedText)


# In[2]:


#Using Selenium to convert text to Speech through online website
def calling_this():
    from selenium import webdriver
    driver = webdriver.Chrome(r'E:\software\Chrome Driver\chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://www.naturalreaders.com/online/');
    driver.find_element_by_id("inputDiv").clear()
    
    str=ReadingTextDocuments('File.docx.docx')  
    
    search_box = driver.find_element_by_id("inputDiv")
    search_box.send_keys(str)
    
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    
    act=ActionChains(driver)
    act.click(driver.find_element_by_id("circle")).perform()
    


# In[3]:

#Calling the Function
calling_this()






