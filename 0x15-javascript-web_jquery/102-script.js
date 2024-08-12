$(document).ready(function () {
  // When the page is fully loaded

  $('#btn_translate').click(function () {
    // When the "Translate" button is clicked
    const languageCode = $('#language_code').val(); // Get the language code from input

    // Construct the API URL with the language code
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    // Fetch the translation from the API
    $.get(apiUrl, function (data) {
      // On success, update the content of DIV#hello with the translation
      $('#hello').text(data.hello);
    });
  });
});
