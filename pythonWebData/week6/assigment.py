import urllib.request, urllib.parse , urllib.error
import json
url = input('Enter Link:')

urlOpen = urllib.request.urlopen(url)
data = urlOpen.read().decode()
js = json.loads(data)
sum = 0
#print('First', js)
for i in js['comments']:
    sum += int(i['count'])
    print('Number:', i['count'],sum)

print('Your sum is',sum,"-All finished")
