// client init config 

// Check hash for token
const hash = window.location.hash
.substring(1)
.split('&')
.reduce(function (initial, item) {
  if (item) {
    var parts = item.split('=');
    initial[parts[0]] = decodeURIComponent(parts[1]);
  }
  return initial;
}, {});
window.location.hash = '';

// Set token
let _token = hash.access_token;

const authEndpoint = 'https://accounts.spotify.com/authorize';

// Replace with your app's client ID, redirect URI and desired scopes
const clientId = '01b263c5ac7d44a8aef137aa1b011ec7';
const redirectUri = 'http://127.0.0.1:7777/';
const scopes = [
  'streaming',
  'user-read-birthdate',
  'user-read-email',
  'user-read-private',
  'playlist-modify-public',
  'user-modify-playback-state'
];






// client-side js
// run by the browser each time your view template is loaded
// get artist input (frontend) and pass data to backend (flask)
$(function() {

  $('form').submit(function(event) {
    event.preventDefault();
    
    $('#recommend').empty();
    let artist = $('select').val();
    //let artist = 'the roots'
    
    // Send a request to our backend (server.py) to get new releases for the currently selected country
    $.get('/recommend?' + $.param({artist: artist}), function(recommendation) {
      
      // Loop through each album in the list
      recommendation.forEach(function(recommend) {

      console.log('-----------------------')
      console.log(recommend)
      console.log('-----------------------')
        
        // Use the returned information in the HTML
        let div = $('<div class="sp-entity-container"><a href="' + recommend.album.external_urls.spotify + 
                '"><div style="background:url(\'' + recommend.album.images[0].url + 
                '\')" class="sp-cover" alt="Album cover"></div></a><h3 class="sp-title">' + recommend.name + 
                '</h3><p class="text-grey-55 sp-by">By ' + recommend.album.artists[0].name + '</p></div>')
        
        div.appendTo('#recommend')
        
      });
    });
  });

});

// get song Genres
function getGenresList() {
  $('#genres-list').empty();
  $.get('/genres?token=' + _token, function(genres) {
    genres.forEach(function(genre) {
      let genreButtonElement = '<label class="btn btn-salmon btn-sm"><input type="checkbox" value="' + genre + '">' + genre + '</label>';
      $('#genres-list').append(genreButtonElement);
    });
  });
  
  $('#genres-list').on('change', 'input', function() {
    if($('#genres-list input:checked').length > 5) {
      $(this).parent().removeClass("active");
      this.checked = false;
      genreLimitAlert("on");
    }
    else {
      genreLimitAlert("off");
    }
  });
}; 
