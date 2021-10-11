#!/usr/bin/env python
# coding: utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pyttsx3
import lxml
import docx


# # In[1]:
# #Using the file present in the directory
def ReadingTextDocuments(filename):
    doc = docx.Document(filename)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])


# In[2]:=
# Using Selenium to convert text to Speech through online website
def calling_this():
    driver = webdriver.Chrome(
        r'E:\software\Chrome Driver\chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://www.naturalreaders.com/online/');
    driver.find_element_by_id("inputDiv").clear()

    str = ReadingTextDocuments('File.docx.docx')

    search_box = driver.find_element_by_id("inputDiv")
    search_box.send_keys(str)

    act = ActionChains(driver)
    act.click(driver.find_element_by_id("circle")).perform()


# Utilizing Beautifulsoup/pyttsx3 for webscraping without the need of a webdriver or website for TTS.
def get_text():
    article = []
    source = requests.get('https://arstechnica.com/gadgets/').text
    soup = BeautifulSoup(source, 'lxml')

    element = soup.find("li", class_="tease article")
    header = element.find("h2").text
    description = element.find("p", class_="excerpt").text

    author = element.find('span').text
    date = element.find('time', class_="date").text

    article.append([header, description, author, date])

    for item in article:
        speak(item)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# In[3]:
# Calling the Function
def main():
    user_input = input("Would you like to use (1) Selenium or (2) BeautifulSoup: ")

    if user_input == "1":
        calling_this()
    elif user_input == "2":
        get_text()
    else:
        print("Please enter a valid number...")
        main()


if __name__ == '__main__':
    main()
