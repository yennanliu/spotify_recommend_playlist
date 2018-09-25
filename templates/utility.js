
// ---------------------------------------------


// Tinder like swipe cards feature  
// credit 
// https://codepen.io/developingidea/pen/meAIn
// set swipe cards 

$(document).ready(function(){

    $(".buddy").on("swiperight",function(){
      $(this).addClass('rotate-left').delay(700).fadeOut(1);
      $('.buddy').find('.status').remove();

      $(this).append('<div class="status like">Like!</div>');      
      if ( $(this).is(':last-child') ) {
        $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
       } else {
          $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
       }
    });  

   $(".buddy").on("swipeleft",function(){
    $(this).addClass('rotate-right').delay(700).fadeOut(1);
    $('.buddy').find('.status').remove();
    $(this).append('<div class="status dislike">Dislike!</div>');

    if ( $(this).is(':last-child') ) {
     $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
      alert('OUPS');
     } else {
        $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
    } 
  });

});

// ---------------------------------------------

// HELP JS on the  spotify client side op 
// credit 
// https://github.com/arirawr/nelson/blob/ac5436a19351118ce2067bfd3e815c52f154c504/client.js
// set sliders

function setUpSliders() {
    const sliderConfig = {
        range: true,
        min: 0,
        max: 1,
        step: 0.01,
        values: [0, 1],
        stop: function() {
            getRecommendations()
        }
    }

    $("#popularity-slider").slider({
        range: true,
        min: 0,
        max: 100,
        step: 1,
        values: [0, 100],
        stop: function() {
            getRecommendations()
        }
    });

}


// get song genre list 

function getGenresList() {
    $('#genres-list').empty();
    $.get('/genres?token=' + _token, function(genres) {
        genres.forEach(function(genre) {
            let genreButtonElement = '<label class="btn btn-salmon btn-sm"><input type="checkbox" value="' + genre + '">' + genre + '</label>';
            $('#genres-list').append(genreButtonElement);
        });
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
}


// get song parameter 

function getSliderValues() {
    let values = {};
    let min_popularity = $('#popularity-slider').slider('values', 0);
    let max_popularity = $('#popularity-slider').slider('values', 1);


    if ($('#mode-minor').is(':checked') && !$('#mode-major').is(':checked')) {
        values["target_mode"] = 0;
    }
    if ($('#mode-major').is(':checked') && !$('#mode-minor').is(':checked')) {
        values["target_mode"] = 1;
    }

    if (min_popularity > 0) {
        values["min_popularity"] = min_popularity;
    }
    if (max_popularity < 100) {
        values["max_popularity"] = max_popularity;
    }
    return values;
}



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


// play song 
function makePlaylist() {
    if (localStorage.getItem('currentNelsonTracks')) {
        $.post('/playlist?tracks=' + localStorage.getItem('currentNelsonTracks') + '&genres=' + localStorage.getItem('currentNelsonGenres') + '&features=' + localStorage.getItem('currentNelsonFeatures') + '&token=' + _token);
        $('#notice').html('<div class="alert alert-success alert-dismissable" role="alert"><b>Sweet!</b> You just created a new Spotify playlist with recommendations from Nelson.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
    }
}

function play(track) {
    if (playbackSetting != 0) {
        $.post('/play?tracks=' + track + '&device_id=' + deviceId + '&token=' + _token);
    }
}

function pause() {
    $.post('/pause?token=' + _token);
}

function remove(track) {
    let trackList = localStorage.getItem('currentNelsonTracks').split(',');
    trackList = trackList.filter(item => item != track);
    localStorage.setItem('currentNelsonTracks', trackList.join());
    let elementId = '#' + track;
    var element = document.getElementById(track);
    element.outerHTML = "";
    delete element;
}