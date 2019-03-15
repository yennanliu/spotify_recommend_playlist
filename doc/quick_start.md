#### Method 1) Run directly  

```bash 

$ cd ~ && git clone https://github.com/yennanliu/spotify_recommend_playlist.git
$ cd ~ && cd spotify_recommend_playlist
$ bash install.sh 
# way 1) 
# $ export SPOTIPY_CLIENT_ID=<your_CLIENT_ID> && export SPOTIPY_CLIENT_SECRET=<your_CLIENT_SECRET>
# way 2)
$ nano .creds.yml # update .creds.yml with your SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
$ python server.py 
# The APP UI should be available at : http://127.0.0.1:7777/

```