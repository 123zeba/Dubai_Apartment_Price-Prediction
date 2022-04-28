# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:47:17 2022

@author: Rishab
"""


from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

info=[]
for x in range(1,1400):
    url="https://www.bayut.com/to-rent/apartments/dubai/page-"
    p=requests.get(url+str(x))

    #print(page)

    soup=BeautifulSoup(p.content,'html.parser')
    lists= soup.find_all('li',class_="ef447dde")
    
    
    for list in lists:
        price=list.find('span',class_="f343d9ce").text
        title=list.find('div',class_="_7afabd84" ).text
        inf=list.find_all('span',class_="b6a29bc0")
        no_of_bedrooms=inf[0].text
        no_of_bathrooms=inf[1].text
        try:
            sqft=inf[2].text
        except IndexError:
            break
            
        
        
        #info=[title,location,price,area]
        info.append([price,title,no_of_bedrooms,no_of_bathrooms,sqft])
        
        print(len(info))
        
df=pd.DataFrame(info)        

df.to_csv("bayut1.csv", header=['price','title','no_of_bedrooms','no_of_bathrooms','sqft'], index=False)

    
        
        
            
            
           
            
             