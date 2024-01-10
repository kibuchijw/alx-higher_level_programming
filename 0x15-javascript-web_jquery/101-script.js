// jQuery click event handler for adding a new element
$('#add_item').click(function () {
  // Create a new <li> element with the text "Item"
  const newItem = $('<li>Item</li>');
  // Append the new <li> element to UL.my_list
  $('ul.my_list').append(newItem);
});

// jQuery click event handler for removing the last element
$('#remove_item').click(function () {
  // Remove the last <li> element from UL.my_list
  $('ul.my_list li:last-child').remove();
});

// jQuery click event handler for clearing all elements
$('#clear_list').click(function () {
  // Remove all <li> elements from UL.my_list
  $('ul.my_list').empty();
});
