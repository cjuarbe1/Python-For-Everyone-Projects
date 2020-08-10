import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

url = input('Enter URL link- ')
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html, 'html.parser')
position = int(input('Enter the position you want to look at:'))
count = int(input('Enter the times you want to look:'))
testForPosition = 1
word = ""
while count>0:
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if position == testForPosition:
            url = tag.get('href', None)
            word = re.findall('by_(.+)\.',url)
            print(url, word)
            testForPosition = 1

            break
        testForPosition+= 1
    count-= 1
print('All Done' , word)
