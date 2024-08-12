$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation () {
    const languageCode = $('#language_code').val(); // Get the language code from input

    // Construct the API URL with the language code
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    // Fetch the translation from the API
    $.get(apiUrl, function (data) {
      // On success, update the content of DIV#hello with the translation
      $('#hello').text(data.hello);
    });
  }

  // Event listener for the "Translate" button click
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Event listener for the "Enter" key press in the language code input field
  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // 13 is the Enter key code
      fetchTranslation();
    }
  });
});
