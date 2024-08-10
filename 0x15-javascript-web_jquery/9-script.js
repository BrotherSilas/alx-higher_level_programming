// Using jQuery to run this code when the document is ready
$(document).ready(function () {
  // Making a GET request to fetch the greeting in French
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (starWars) {
    // Setting the text of the div with id 'hello' to the value of 'hello' from the fetched data
    $('#hello').text(starWars.hello);
  });
});
