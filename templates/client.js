// client-side js
// run by the browser each time your view template is loaded

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
