$(document).ready(function() {
  // jQuery click event handler for fetching translation
  $('#btn_translate').click(function() {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    // jQuery AJAX GET request to fetch translation
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // Display the fetched translation in the DIV#hello
      $('#hello').text(data.hello);
    });
  });
});
