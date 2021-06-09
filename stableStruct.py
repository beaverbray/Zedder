import json
import pandas as pd
from getHorsey import query
from pprint import pprint

# JSON structure:
	# getRaceResults 
		# Edges
			# cursor ??
			# node = race information
				# horses = horse information

		# pageInfo


# pull data from getHorsey
my_dict = query()

# parse json until we get to strs
fdsa = my_dict['data']['getRaceResults']['edges']

# getRaceResults = (my_dict['data']['getRaceResults']['edges'][0]['node'])
# transform strs to dict
# print(getRaceResults)

# print(len(fdsa))

d = []
for n in range(0, len(fdsa)):
	 d.append((my_dict['data']['getRaceResults']['edges'][n]['node']))


pprint(d[0])
pprint(d[1])

# def raceParse():

# 	for race in d:
# 		for v in race:
# 			print()


# 	print(city)


# raceParse()
# prize pool calc
# # wei * 0.000000000000000001 = eth

# # 'city': 'Manila',
# #               'class': 1,
# #               'country': 'Philippines',
# #               'fee': '0.0149',

# # def raceDescription():

# # 	data = myprint(edges)
	
# # 	city = data['node']['city']
	
# # 	pprint(data)
# # 	# print(f'we are racing in{city} today')

# # 	# data = myprint(edges)
# # 	# pprint(data)


# # raceDescription()












