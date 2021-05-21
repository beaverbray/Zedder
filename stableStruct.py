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
getRaceResults = (my_dict['data']['getRaceResults']['edges'])
# transform strs to dict
# print(getRaceResults)

# print(type(getRaceResults))
edges = dict()

for index, value in enumerate(getRaceResults):
 	edges[index] = value

def myprint(race):
	# key and value in race(items)
    for k, v in race.items():
    	# isinstace returns True if V in DICT
        if isinstance(v, dict):
            myprint(v)
        else:
        	# prints key and values
            pprint("{0} : {1}".format(k, v))



