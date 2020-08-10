import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter xml link - ')
try:
    data = urllib.request.urlopen(url).read()
except:
    print('Error Try again')
    quit()

xmlObj = ET.fromstring(data)
test =  xmlObj.findall('comments/comment')
print('Retrieving ',len(data))
print('Count', len(test))

sum = 0
for item in test:
    sum+= int(item.find('count').text)
    #print('Number:', item.find('count').text, ' Current sum:',sum)
print(sum)
