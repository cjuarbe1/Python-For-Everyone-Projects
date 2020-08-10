import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sqlite3

conn = sqlite3.connect('champMastery.sqlite')
cur = conn.cursor()


cur.executescript('''
DROP TABLE IF EXISTS champMastery;
CREATE TABLE IF NOT EXISTS champMastery (name TEXT, masteryPoints INTEGER)''')

api_key = 'RGAPI-e2dff412-51bb-43ad-beec-3d73071223f6'
serviceurl = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
urlForSummonerMastery = 'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'
urlForSummonerIdInfo = 'http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json'
#Kinda but not really get the ctx. I know its to ignore the security issues
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE


while True:
    summonerId = input('Enter id: ')
    if len(summonerId) < 1: break
    #url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerId + '?api_key=' + api_key
    parms = dict()
    parms['api_key'] = api_key
    #print(parms)
    url = serviceurl + summonerId +'?' + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()



    try:
        js = json.loads(data)
    except:
        print('Error')
        break

    # if not js :
    #     print('==== Failure To Retrieve ====')
    #     print(data)
    #     continue
    #print(data)
    # dOfChampMastery = dict()
    listOfMastery = []
    listOfChamps = []
    playerId = js['id']
    newUrlSumMas = urlForSummonerMastery + playerId + '?' + urllib.parse.urlencode(parms)
    print('Retrieving', newUrlSumMas)
    sumMasApiii = urllib.request.urlopen(newUrlSumMas)
    sumMasApii = sumMasApiii.read().decode()
    sumMasApi = json.loads(sumMasApii)

    for apiList in sumMasApi:
        #if  listOfChamps[]
        for key,value in apiList.items():
            if key == 'championId' :
                listOfChamps.append(value)
            if key == 'championPoints':
                listOfMastery.append(int(value))
    dOfChampMastery = dict()
    index = 0
    print(type(dOfChampMastery))
    print(listOfChamps, listOfMastery, listOfChamps[0])
    while len(dOfChampMastery) < len(listOfChamps):
        dOfChampMastery[listOfChamps[index]] = listOfMastery[index]
        index += 1
    for k,v in dOfChampMastery.items():
        cur.execute('''INSERT INTO champMastery (name,masteryPoints)
            VALUES ( ?,? )''', ( k,v ) )
        conn.commit()

    print('Done')
    # test = list()
    # for k,v in dOfChampMastery.items():
    #     newtup = (v,k)
    #     test.append(newtup)
    # test = sorted(test)
    # for v,k in test[:]:
    #     print(k,v)
    # print(sorted( [ (v,k) for k,v in dOfChampMastery.items() ]) )
    # for x,y in dOfChampMastery.items():
    #     print('This is key:', x, 'This is Value:', y)




    #print(playerId)

    #print(js['results'][0]['place_id'])

    #print(json.dumps(js, indent=2))
