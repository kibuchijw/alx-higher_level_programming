// jQuery click event handler for DIV#toggle_header
$('DIV#toggle_header').click(function () {
  // Toggle class 'red' to 'green' & vice versa when DIV#toggle_header is clicked
  $('HEADER').toggleClass('green red');
});
