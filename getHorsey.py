import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import requests
import json

# api = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjcnlwdG9maWVsZF9hcGkiLCJleHAiOjE2MjI0OTgzNDcsImlhdCI6MTYyMDA3OTE0NywiaXNzIjoiY3J5cHRvZmllbGRfYXBpIiwianRpIjoiOGM4MTBiN2YtYTZmNi00MTVmLWI1NTAtY2Q5NDRhZGUwYTMxIiwibmJmIjoxNjIwMDc5MTQ2LCJzdWIiOnsiZXh0ZXJuYWxfaWQiOiJiNmY4ZWRmNi0zZTY4LTRkZmMtODJlNC1kM2M5ODQxZTcxMDIiLCJpZCI6NDAzMDcsInB1YmxpY19hZGRyZXNzIjoiMHg5NjVkY2UxOTM2QzA0NDVhYjg4NDFhMzdDQTY1M2FGODk2MGI1M0NFIiwic3RhYmxlX25hbWUiOiJkb3RteXQifSwidHlwIjoiYWNjZXNzIn0.pKeD0a5idbLhnrzSGkYOkUhdKGHSeTtEdqRuEBEQ1jqcktbAn52LZV2r7DP3WAv5k-dZDJPsSEwPB9l0M2xqyA"

# The day the racing algo was changed to its current form
# "from": "2020-12-02T00:00:00.00Z"	

api = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjcnlwdG9maWVsZF9hcGkiLCJleHAiOjE2MjUzMzQ0NTIsImlhdCI6MTYyMjkxNTI1MiwiaXNzIjoiY3J5cHRvZmllbGRfYXBpIiwianRpIjoiODgwYzNjOTAtNmRlYi00NjEzLTljOWYtZDU1NDRhMDk3ZjZhIiwibmJmIjoxNjIyOTE1MjUxLCJzdWIiOnsiZXh0ZXJuYWxfaWQiOiJiNmY4ZWRmNi0zZTY4LTRkZmMtODJlNC1kM2M5ODQxZTcxMDIiLCJpZCI6NDAzMDcsInB1YmxpY19hZGRyZXNzIjoiMHg5NjVkY2UxOTM2QzA0NDVhYjg4NDFhMzdDQTY1M2FGODk2MGI1M0NFIiwic3RhYmxlX25hbWUiOiJkb3RteXQifSwidHlwIjoiYWNjZXNzIn0.infHKqrWqtNWXaIP-dd3uFGKAsBLDjJ5bPicil97tEyAc8GO_oMmLivFFgxGG43PMeZF-cqdrFXu8X28E4E2BQ"

import http.client

def query():

	conn = http.client.HTTPSConnection("zed-ql.zed.run")

	payload = """
	query ($input: GetRaceResultsInput, $before: String, $after: String, $first: Int, $last: Int) {
		getRaceResults(before: $before, after: $after, first: $first, last: $last, input: $input) {
			edges {
				cursor
				node {
					country
					city
					name
					length
					startTime
					fee
					raceId
					weather
					status
					class
					prizePool {
						first
						second
						third
					}
					horses {
						name
						horseId
						finishTime
						finalPosition
						name
						gate
						ownerAddress
						bloodline
						gender
						breedType
						gen
						coat
						hexColor
						imgUrl
						class
						stableName
					}
				}
			}
			pageInfo {
				startCursor
				endCursor
				hasNextPage
				hasPreviousPage
			}
		}
	}
	"""

	json_data = {
		"query": payload,
		"variables": {
			"first": 2,
			"input": {
				# "location": {
				# 	"country": "Poland",
				# 	"city": "Katowice"
				# },
				"dates": {
		            "from": "2020-12-02T00:00:00.00Z",
		            "to": "2021-05-05T19:19:00.568Z"

				},
				"distance": {
					"from": 1000,
					"to": 1000
				},
				"classes": [
					1
				]	
			}
		}
	}

	headers = {
	    'Content-Type': "application/json",
	    'x-developer-secret': api
	    }
	# GraphQL -> json with "dump"
	conn.request("POST", "/graphql", json.dumps(json_data), headers)

	res = conn.getresponse()
	data = res.read()

	# what is this? 

	# with open('data.json', 'w') as outfile:
 #   		json.dump(data.decode("utf-8"), outfile)

	json_string = data.decode("utf-8")

	jd = json.loads(json_string)

	return jd






