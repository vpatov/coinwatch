import json
import requests
import time
import datetime

api_url = 'https://api.coinmarketcap.com/v1/ticker/'

def get_coins(start=None):
    if start == None:
        start = 0

    try:
    	response = requests.api.get(api_url,params={'start':start})
    except Exception as e:
    	print(e)
    	return []

    if (response.status_code == 200):
    	return json.loads(response.text)
    else:
        return []

def get_all_coins():
    coins = []
    start = 0
    limit = 300
    while(True):
        time.sleep(0.2)
        more_coins = get_coins(start)
        print(len(more_coins))
        start += len(more_coins)

        if (more_coins):
            coins += more_coins
        else:
            break

    return coins

all_coins = get_all_coins()

f = open('all_coins' + str(len(all_coins)),'w')
json.dump(all_coins,f)
f.close()
print("Success: %d coins" % len(all_coins))
print(datetime.datetime.now())
