$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (response) {
    $('#list_movies').empty();
    response.results.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  },
  error: function (xhr, status, error) {
    console.error('Error:', error);
  }
});
