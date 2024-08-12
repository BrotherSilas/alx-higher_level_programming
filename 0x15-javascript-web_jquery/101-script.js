$(document).ready(function () {
  // When the page is fully loaded

  $('#add_item').click(function () {
    // When the "Add item" button is clicked
    $('ul.my_list').append('<li>Item</li>');
    // Add a new <li> element to the end of the list
  });

  $('#remove_item').click(function () {
    // When the "Remove item" button is clicked
    $('ul.my_list li:last-child').remove();
    // Remove the last <li> element in the list
  });

  $('#clear_list').click(function () {
    // When the "Clear list" button is clicked
    $('ul.my_list').empty();
    // Remove all <li> elements from the list
  });
});
