// client init config 
// Check hash for token
/*
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


*/



//----------------------------------------------

// Page setup
//setPlaybackSetting(1);


//----------------------------------------------
/*
// Initialise Web Playback SDK
function onSpotifyPlayerAPIReady() {
  
  let player = new Spotify.Player({
    name: 'Nelson',
    getOAuthToken: function(cb) {
      //cb(_token)
      cb('BQCgd4ha3HBSBz53fBNHn0nBIzonFH_Zfjc8KioX79DT6hFEzgImA2F01adjL_5tFXRuwkvW3GPr3Q07mMw')
    },
    volume: 0.8
  });

  player.on('ready', function(data) {
    deviceId = data.device_id;
    localStorage.setItem('nelsonBrowserDeviceID', data.device_id);
  });

  player.on('player_state_changed', function(data) {
    if(data) {
      let currentTrack = data.track_window.current_track.uri;
      updateCurrentlyPlaying(currentTrack);
    }  
  });

  player.connect();
}
*/



//----------------------------------------------
// client-side js
// run by the browser each time your view template is loaded
// get artist input (frontend) and pass data to backend (flask)

// get seleted artist and parse to flask backend  (/Home page)
$(function() {

    $('form').submit(function(event) {
        event.preventDefault();

        $('#recommend').empty();
        let artist = $('select').val();
        //let artist = 'the roots'

        // Send a request to our backend (server.py) to get new releases for the currently selected country
        $.get('/recommend?' + $.param({
            artist: artist
        }), function(recommendation) {

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


// get album pics (/slide_recommend page)
$(function() {

        $('#slide_recommend').empty();
        let artist = $('select').val();
        //let artist = 'the roots'

        // Send a request to our backend (server.py) to get new releases for the currently selected country
        $.get('/slide_recommend?' + $.param({
            artist: artist
        }), function(recommendation) {

            // Loop through each album in the list
            recommendation.forEach(function(recommend) {

                console.log('-----------------------')
                console.log(recommend)
                console.log('-----------------------')

                // Use the returned information in the HTML
                let div = $('<div class="buddy" style="display: block;">' + 
                            '<div class="avatar"  style="display: block; background-image: url(\'' +  recommend.album.images[0].url + '\')"></div>' 
                            + '</div>')

                div.appendTo('#slide_recommend')

            });
        });
    });



//----------------------------------------------
// get song Genres (V1)
/*
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

*/


//----------------------------------------------
// get song Genres  (V2)

function getGenresList() {
    $('#genres-list').empty();
    genres = [
        "acoustic",
        "afrobeat",
        "alt-rock",
        "alternative",
        "ambient",
        "anime",
        "black-metal",
        "bluegrass",
        "blues",
        "bossanova",
        "brazil",
        "breakbeat",
        "british",
        "cantopop",
        "chicago-house",
        "children",
        "chill",
        "classical",
        "club",
        "comedy",
        "country",
        "dance",
        "dancehall",
        "death-metal",
        "deep-house",
        "detroit-techno",
        "disco",
        "disney",
        "drum-and-bass",
        "dub",
        "dubstep",
        "edm",
        "electro",
        "electronic",
        "emo",
        "folk",
        "forro",
        "french",
        "funk",
        "garage",
        "german",
        "gospel",
        "goth",
        "grindcore",
        "groove",
        "grunge",
        "guitar",
        "happy",
        "hard-rock",
        "hardcore",
        "hardstyle",
        "heavy-metal",
        "hip-hop",
        "holidays",
        "honky-tonk",
        "house",
        "idm",
        "indian",
        "indie",
        "indie-pop",
        "industrial",
        "iranian",
        "j-dance",
        "j-idol",
        "j-pop",
        "j-rock",
        "jazz",
        "k-pop",
        "kids",
        "latin",
        "latino",
        "malay",
        "mandopop",
        "metal",
        "metal-misc",
        "metalcore",
        "minimal-techno",
        "movies",
        "mpb",
        "new-age",
        "new-release",
        "opera",
        "pagode",
        "party",
        "philippines-opm",
        "piano",
        "pop",
        "pop-film",
        "post-dubstep",
        "power-pop",
        "progressive-house",
        "psych-rock",
        "punk",
        "punk-rock",
        "r-n-b",
        "rainy-day",
        "reggae",
        "reggaeton",
        "road-trip",
        "rock",
        "rock-n-roll",
        "rockabilly",
        "romance",
        "sad",
        "salsa",
        "samba",
        "sertanejo",
        "show-tunes",
        "singer-songwriter",
        "ska",
        "sleep",
        "songwriter",
        "soul",
        "soundtracks",
        "spanish",
        "study",
        "summer",
        "swedish",
        "synth-pop",
        "tango",
        "techno",
        "trance",
        "trip-hop",
        "turkish",
        "work-out",
        "world-music"
    ]
    console.log(genres)
    genres.forEach(function(genre) {
        console.log(' in the func ')
        let genreButtonElement = '<label class="btn btn-salmon btn-sm"><input type="checkbox" value="' + genre + '">' + genre + '</label>';
        $('#genres-list').append(genreButtonElement);
    });


    $('#genres-list').on('change', 'input', function() {
        if ($('#genres-list input:checked').length > 5) {
            $(this).parent().removeClass("active");
            this.checked = false;
            genreLimitAlert("on");
        } else {
            genreLimitAlert("off");
        }
    });
};


//----------------------------------------------
// get recommendation

function getRecommendations() {

    // Get selected genres
    let genres = [];
    $('#genres-list input:checked').each(function() {
        genres.push($(this).val());
    });
    let genresString = genres.join();
    localStorage.setItem('currentNelsonGenres', genresString);
    $('#current-genres').text(genresString);

    // print selected genres
    //----------
    console.log('selected genres : ' +  genres); 
    console.log('selected genres json : ' +  JSON.stringify({genres})); 
    //----------

    

    
    //----------

    // pass a request to flask backend  (approach 1)
    $.get('/recommend?' + $.param({
        genres: JSON.stringify({genres})
        //genres: $('#current-genres').serialize()
    }))

    //----------


    //---------- 

    // pass genres to flask backend     (approach 2)
    // https://stackoverflow.com/questions/45473474/send-variable-from-javascript-into-flask
     $.ajax({
        url: '/recommend?',
        //url: "{{/recommend}}",
        //url: "{{ url_for("recommend") }}",
        //data: $('#current-genres').serialize(),
        data: JSON.stringify({genres}),
        type: 'POST',
        dataType: "json",
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });

    //----------



    // Get slider values
    let audioFeatures = getSliderValues();
    localStorage.setItem('currentNelsonFeatures', JSON.stringify(audioFeatures));

    // Send the request
    $.get('/recommendations?seed_genres=' + genresString + '&' + $.param(audioFeatures) + '&token=' + _token, function(data) {
        $('#tracks').empty();
        let trackIds = [];
        let trackUris = [];
        if (data.tracks) {
            if (data.tracks.length > 0) {
                data.tracks.forEach(function(track) {
                    trackIds.push(track.id);
                    trackUris.push(track.uri);
                });
                localStorage.setItem('currentNelsonTracks', trackUris.join());
                renderTracks(trackIds);
                play(trackUris.join());
            } else {
                $('#tracks').append('<h2>No results. Try a broader search.</h2>')
            }
        } else {
            $('#tracks').append('<h2>No results. Select some genres first.</h2>')
        }
    });
}