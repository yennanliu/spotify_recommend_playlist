#!/bin/sh





# ref 
# https://developer.spotify.com/console/get-recommendations/?seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50&market=US
# https://developer.spotify.com/dashboard/applications
# https://github.com/drshrey/spotify-flask-auth-example

curl -X "GET" "https://api.spotify.com/v1/recommendations?market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQB65jgcpPYBEFEFYj_QzbiZhtHYb75A37b4i5_QaYcOcebPoN2fbE1i2qti6LTrXIcNELh6QtJA2Xv9gPSfCS6JkqJQl2acpbUFe4M21kyYSPEYaIs0t2sFCAgWSYb8x6oWz6vaQp_xkx-HhxiFDQepkJeqC1n6VA"


