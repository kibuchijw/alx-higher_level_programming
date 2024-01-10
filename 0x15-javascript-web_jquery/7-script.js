// jQuery GET request to fetch character name
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  // Update the text of DIV#character with the fetched character name
  $('#character').text(data.name);
});
