$(document).ready(function () {
  // jQuery click event handler for fetching translation
  $('#btn_translate').click(fetchTranslation);
  // jQuery keypress event handler for ENTER key in INPUT#language_code
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    // jQuery AJAX GET request to fetch translation
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // Display the fetched translation in the DIV#hello
      $('#hello').text(data.hello);
    });
  }
});
