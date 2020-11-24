#Python program to scrape website  
#and save quotes from website 

import requests 
from bs4 import BeautifulSoup 
import csv 
import pandas as pd
import sys

  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)  

soup = BeautifulSoup(r.content, 'html5lib') 

quotes=[]  # a list to store quotes    

table = soup.find('div', attrs = {'id':'all_quotes'})  

for row in table.findAll('div', 

                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt'].split(" #")[0] 
    quote['author'] = row.img['alt'].split(" #")[1] 
    quotes.append(quote) 

# print(sys.argv[1])

inspirational_quotes = pd.DataFrame(quotes)  
# print(inspirational_quotes.head())
# saving the dataframe to csv 

inspirational_quotes.to_csv(sys.argv[1])

print("completed")
# run python code using line below
# python3 iq_ws.py iq_ws.csv