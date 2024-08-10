// Using jQuery to make a GET request to the specified URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (starWars) {
  // Looping through each movie in the data received
  $.each(starWars.results, function (index, movie) {
    // Creating a new list item with the movie title
    const listItem = $('<li></li>').text(movie.title);
    // Appending the list item to the ul with id "list_movies"
    $('#list_movies').append(listItem);
  });
});
