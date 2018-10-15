# spotify_recommend_playlist

<img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref/app_1.png" width="800" height="400">

 
## 0) IDEA 

- Build a prior detector catch users' taste (ML model), pass the predict output as parameter to Spotify recommendation API then get the Spotify recommended playlist 

```
User rate the songs ---> detector ---> Model_training  ---> Spotify_ML_API ---> recommended_playlist ---> Web_UI 

```

## 1) FILE STRUCTURE 

```
├── [1.8k]  README.md
├── [3.1k]  collect_data.py  : Script collect data (/data)
├── [ 160]  data             : Scraped data for model training 
├── [ 613]  install.sh       : Bash help install needed environment 
├── [3.3k]  server.py        : Script hold server-side services (Python flask)
├── [ 192]  templates	     
│   ├── [9.4k]  client.js    : Script hold client-side services (playlist..) (JS)
│   ├── [4.0k]  index.html   : Main html file 
│   └── [3.6k]  style.css    : Main CSS file 
├── [4.6k]  utility.js       : Backup JS help script 
└── [2.8k]  utility.py       : Python script query spotify API 

```

## 2) QUICK START

- Step 1 
	- Get the spotify SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET 
	- https://developer.spotify.com/dashboard/applications
	- (You MUST have the spotify Premium account )
- Step 2 
	- Create an APP at developer page with created SPOTIPY_CLIENT_ID
	- https://developer.spotify.com

- Step 3 
	- Execute the following commands then run the web APP locally 
	- The APP UI should be available at : http://127.0.0.1:7777/


#### Method 1) Run directly  

```bash 

$ cd ~ && git clone https://github.com/yennanliu/spotify_recommend_playlist.git
$ cd ~ && cd spotify_recommend_playlist
$ bash install.sh 
$ export SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
$ export SPOTIPY_CLIENT_SECRET=<your_CLIENT_SECRET>
$ python server.py 
# The APP UI should be available at : http://127.0.0.1:7777/

```

#### Method 2) Run via Docker 

```bash 

$ cd ~ 
# https://hub.docker.com/r/yennanliu/spotify_rec_env/
$ docker pull yennanliu/spotify_rec_env:v1 
$ docker images 
$ docker ps 
# launch container 
docker run  spotify_rec_env:v1 
# run image 
docker run -it spotify_rec_env:v1 
# inside docker env 
#((base) root@3797bf037d38:/#)
(base) root@3797bf037d38:/ export SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
(base) root@3797bf037d38:/ export SPOTIPY_CLIENT_SECRET=<your_CLIENT_SECRET>
(base) root@3797bf037d38:/ cd spotify_recommend_playlist/ 
(base) root@3797bf037d38:/ python server.py 
# The APP UI should be available at : http://127.0.0.1:7777/

```



## 3) TECH
- Backend : Python3 flask, spotipy, sklearn 
- Frontend : Javascript, Ajax, HTML, CSS, Bootstrap 


## 4) INSPIRED BY 
- https://nelson.glitch.me/#


## 5)REF 

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



