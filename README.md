# Spotify_Recommend_Playlist

[![Build Status](https://travis-ci.org/yennanliu/spotify_recommend_playlist.svg?branch=master)](https://travis-ci.org/yennanliu/spotify_recommend_playlist)

- Team discusisson doc 
	- [google sheet](https://docs.google.com/spreadsheets/d/1m8XjTOgJBmAV6EVHB09P1V2q8DbRAM4FRK8jtWBG7W8/edit?usp=sharing)

## Intro
- Build an UI grab user's song taste via `Tinder like` process, then train a ML model from user taste data, then predict the potentail users liked songs via the classification from ML model, finally call the `Spotify recommendation API` then get the playlist of the songs that fit such user classification

## Architecture
<p align="center"><img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/doc/pic/architecture.svg" width="800" height="400"></p>
 
- Architecture Idea 

```
User rate the songs ---> detector ---> Model_training  ---> Spotify_ML_API ---> recommended_playlist ---> Web_UI 
```

## FILE STRUCTURE 

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

## QUICK START

#### Prerequisites

<details>
<summary>Prerequisites</summary>

- Step 1 
	- Get the spotify SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET 
	- https://developer.spotify.com/dashboard/applications

- Step 2 
	- Create an APP at developer page with created SPOTIPY_CLIENT_ID
	- https://developer.spotify.com
- Step 3 
	- Rename [.creds.yml.dev](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/.creds.yml.dev) to `.creds.yml` and update the Spotify credential (SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
- Step 4
	- Execute the following commands (Method 1)then run the web APP locally 
	- The APP UI should be available at : http://127.0.0.1:7777/

</details>

#### Method 1) Run (manually)  

- [quick start](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/doc/quick_start.md)


#### Method 2) Run (docker)

- [quick start docker](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/doc/quick_start_docker.md)


## TECH
- Backend : Python3 flask, spotipy, sklearn 
- Frontend : Javascript, Ajax, HTML, CSS, Bootstrap 

## REF 

<details>
<summary>REF</summary>

- [ref.md](https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref.md) 
- Inspired by 
	- https://nelson.glitch.me/#
</details>

## TODO

<details>
<summary>TODO</summary>

- Fix JS Ajax call API part
- Fix frontend layout 
- Dockerize the project  
</details>
