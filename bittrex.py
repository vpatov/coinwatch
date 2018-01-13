import requests
import json
import time

API_URL = 'https://bittrex.com/api'
API_VER = 'v1.1'
API_PUB = 'public'

API_SUMMARY = 'getmarketsummaries'


## Generalize this later.
class BittrexExchange:
	# interval is how many minutes in between updates
	def __init__(self,market_summaries,interval):
		self.market_summaries = {market['MarketName']:[] for market in market_summaries}
		self.interval = interval
		self.daily_requests = (24 * 60) / interval


	def update_market_summaries(self,market_summaries):
		for market in market_summaries:
			if (market['MarketName'] in self.market_summaries):
				self.market_summaries[market['MarketName']].append(
					{
						'timestamp':market['TimeStamp'],
						'ask':market['Ask'],
						'bid':market['Bid'],
						'last':market['Last']
					}
				)
			else:
				print ("Unexpected market {1}".format(market))




def get_market_summaries():
	request = '/'.join((API_URL,API_VER,API_PUB,API_SUMMARY))
	print(request)

	try:
		response = requests.api.get(request)
		if (response.status_code != 200):
			return []
		else:
			json_response = json.loads(response.text)
			if json_response['success']:
				return json_response['result']
			else:
				print(json_response['success'])
				return []

	except Exception as e:
		print(e)
		return []

def find_by_market_name(summaries,market_name):
	for summary in summaries:
		if summary['MarketName'] == market_name.upper():
			return summary
	return None


summaries = get_market_summaries()
exchange = BittrexExchange(summaries,5)
btc_eth = find_by_market_name(summaries,'BTC-ETH')


"""
Market Summary Keys:
MarketName 		<class 'str'>
Created 		<class 'str'>
TimeStamp 		<class 'str'>

Ask 			<class 'float'>
Bid 			<class 'float'>
Last 			<class 'float'>
Low 			<class 'float'>
High 			<class 'float'>

Volume 			<class 'float'>
BaseVolume 		<class 'float'>

OpenBuyOrders 	<class 'int'>
OpenSellOrders 	<class 'int'>

PrevDay 		<class 'float'>
"""






