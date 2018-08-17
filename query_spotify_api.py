# python 3


import requests
import pandas as pd 


# ----------------------------------------
# help func 


def get_recommend_spotify_api():
	""" will get spotify API access token dynamically later """
	scrape_data=requests.get("https://api.spotify.com/v1/recommendations?market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50", headers={"Authorization": "Bearer BQDA5HZO1Szrt4OR7alNZ-KzeGb_wuI5VGDBicL8kbwqj9WPQ9OJzF7aNDCy20_wBr-LOBhrrmt3qFlVOiGx0oVHAJSjPCZGfKEbxuykRSOi4FpxdMw0Qh0USyAkRQp0RepfsExJUAigGoxmH_YaCdddyFygSsbzwQ"})
	scrape_json = scrape_data.json()
	print ('scrape_json  : ' , scrape_json)
	# transform json to dataframe 
	name=[]
	external_urls=[]
	id_=[]
	album_type=[]
	for i in range(len(scrape_json['tracks'])):
		#print (scrape_json['tracks'][i]['album'])
		name.append(scrape_json['tracks'][i]['album']['artists'][0]['name'])
		external_urls.append(scrape_json['tracks'][i]['album']['artists'][0]['external_urls']['spotify'])
		id_.append(scrape_json['tracks'][i]['album']['artists'][0]['id'])
		album_type.append(scrape_json['tracks'][i]['album']['type'])
	data=pd.DataFrame({ 'name' : name,
						'external_urls' : external_urls,
						'id' : id_,
						'album_type' : album_type})
	print (data)




# ----------------------------------------


if __name__ == '__main__':
	get_recommend_spotify_api()






