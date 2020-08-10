import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
sum = 0
tags = soup('span')

tester = []
for tag in tags:

    tester.append(tag.get('Contents',tag.contents[0]))
    print(tag.get('Contents:',tag.contents[0]))
print(tester)
for nums in tester:
    nums = int(nums)
    sum+= nums
    count += 1
print(sum , count)
#What the code does
#-------------------------------------------------------------
#The code takes a user input for a websites url and procceds to use
# import urlib for quick access to urlibarary Uses BeautifulSoup to clean html,
#Also use BeautifulSoup function to gather all lines with soup(span)
#then puts all num in span in a list and finally adds it up with a for loop



#Test code for trying a dict in a parse.
#------------------------------------------------------------
#print(tag.findall('[0-9]+', None))
#numHolder[tag] = numHolder.get('Contents',tag.contents[0]
#numHolder was a dict
#    print(type(tag))
#print(numHolder.items())
# for k,v in numHolder.items():
#     sum += int(v)
#     print()
#     count += 1
#     print(v,count,sum)
#print(count,sum,"Done")
