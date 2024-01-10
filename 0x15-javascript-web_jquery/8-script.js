// jQuery AJAX GET request to fetch movie titles
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  // Iterate through each movie and create list items with movie titles
  $.each(response.results, function(index, movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
