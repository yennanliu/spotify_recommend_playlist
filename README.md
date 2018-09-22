# spotify_recommend_playlist

<img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref/app_1.png" width="800" height="400">

 

## File structure 
```
├── [1.8k]  README.md
├── [3.1k]  collect_data.py  : Script collect data (/data)
├── [ 160]  data        	 : Scraped data for model training 
├── [ 613]  install.sh 		 : Help bash install needed environment 
├── [3.3k]  server.py   	 : Main script hold the APP backend service (flask)
├── [ 192]  templates	     
│   ├── [9.4k]  client.js    : Script hold client-side services (playlist..) (JS)
│   ├── [4.0k]  index.html   : Main html file 
│   └── [3.6k]  style.css    : Main CSS file 
├── [4.6k]  utility.js       : Backup JS help script 
└── [2.8k]  utility.py       : Help python script query spotify API 


```

## Quick start 

- Step 1 
	- Get the spotify SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET 
	- https://developer.spotify.com/dashboard/applications
	- (You MUST have the spotify Premium account )
- Step 2 
	- Create an APP at developer page with created SPOTIPY_CLIENT_ID
	- https://developer.spotify.com

- Step 3 
	- Execute the following commands then run the web APP locally 

```bash 

$ cd ~ && git clone https://github.com/yennanliu/spotify_recommend_playlist.git
$ cd ~ && cd spotify_recommend_playlist
$ bash install.sh 
$ export SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
$ export SPOTIPY_CLIENT_SECRET=<your_CLIENT_SECRET>
$ python server.py 

```

## Tech
- Backend : Python3 flask, spotipy 
- Frontend : Javascript, HTML, CSS 


## Inspired by 
- https://nelson.glitch.me/#


## Ref 

- Projects 
	- https://github.com/arirawr/nelson
	- https://glitch.com/~spotify-web-playback
	- https://glitch.com/@spotify
	- https://glitch.com/@a

- SDK / API doc. 
	- https://beta.developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/
	- https://developer.spotify.com/documentation/web-playback-sdk/reference/
	- https://developer.spotify.com/console/get-recommendations 

- Access token  
	- https://ericdaat.github.io/scraping-kshe-radio-to-spotify-playlist.html
	- https://github.com/drshrey/spotify-flask-auth-example

- ML
	- http://smarterplaylists.playlistmachinery.com/go.html
	- https://github.com/smyrbdr/make-your-own-Spotify-playlist-of-playlist-recommendations
	- https://medium.com/deep-learning-turkey/build-your-own-spotify-playlist-of-best-playlist-recommendations-fc9ebe92826a



