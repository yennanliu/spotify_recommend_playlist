# spotify_recommend_playlist

[![Build Status](https://travis-ci.org/yennanliu/spotify_recommend_playlist.svg?branch=master)](https://travis-ci.org/yennanliu/spotify_recommend_playlist)


## Architecture
<p align="center"><img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/doc/pic/architecture.svg" width="800" height="400"></p>

<img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref/app_1.png" width="800" height="400">
<img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref/app_2.png" width="800" height="400">

 
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

#### Prerequisites

- Step 1 
	- Get the spotify SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET 
	- https://developer.spotify.com/dashboard/applications

- Step 2 
	- Create an APP at developer page with created SPOTIPY_CLIENT_ID
	- https://developer.spotify.com

- Step 3 
	- Update the Spotify credential (SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
	- [.creds.yml](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/.creds.yml) 

- Step 4
	- Execute the following commands (Method 1)then run the web APP locally 
	- The APP UI should be available at : http://127.0.0.1:7777/


#### Method 1) Run directly  

- [quick start](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/doc/quick_start.md)


#### Method 2) Run via Docker 

- [quick start docker](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/doc/quick_start_docker.md)


## 3) TECH
- Backend : Python3 flask, spotipy, sklearn 
- Frontend : Javascript, Ajax, HTML, CSS, Bootstrap 


## 4) INSPIRED BY 
- https://nelson.glitch.me/#


## 5)REF 
- [reference](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref.md) 


## 6) TODO
- Fix JS Ajax call API part
- Fix frontend layout 
- Dockerize the project  
