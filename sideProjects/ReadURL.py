import urllib.request
#import requests
#!conda install -c anaconda beautifulsoup4
from bs4 import BeautifulSoup
# import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
#tags = soup('table')
result =  soup.find("table",{"class":'wikitable sortable'})
#test = result.findAll('td')
#print(type(result),type(soup))
rows = result.findAll('tr')
for row in rows:
    #print('in Row')
    print(row.text,'ROW TEXT')
    cols = row.findAll('td')
    for col in cols:


        if(col.findNext('td').text.strip() == 'Not assigned'):
        #    print('This actually workssssssss')
            break
        print(col.text,'COL TEXT')
# for trow in result:
#     print('Working')
# df = pd.read_html(soup)
# df.head()
