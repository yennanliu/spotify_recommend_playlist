# python 3


import requests
import pandas as pd 


# ----------------------------------------
# help func 


def get_recommend_spotify_api():
	""" will get spotify API access token dynamically later """
	scrape_data=requests.get("https://api.spotify.com/v1/recommendations?market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50", headers={"Authorization": "Bearer BQCbp7cnqQKQ_w1FU2C55plNxF3Dipf7vTzc1FH0A-o2jEUSZRxTNAG7cLX4AhX9bMAnRoWiheysYZGMDcYbBK9qx7Fu7UWl-RyNyLBT3U7-Sl4UAM6x3BhS88NjZivRy6JuMEswZkqTQ-wfIlR8mel1Ogdb2WQscQ"})
	scrape_json = scrape_data.json()
	print ('scrape_json  : ' , scrape_json)




# ----------------------------------------


if __name__ == '__main__':
	get_recommend_spotify_api()







	