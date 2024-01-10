// jQuery AJAX GET request to fetch translation
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  // Display the fetched translation in the DIV#hello
  $('#hello').text(data.hello);
});
