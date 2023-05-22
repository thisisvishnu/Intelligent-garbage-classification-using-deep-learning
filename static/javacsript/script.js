$(document).ready(function() {
    // Handle form submission using AJAX
    $('#predict-form').submit(function(event) {
        event.preventDefault(); // Prevent form from submitting traditionally
  
        var formData = new FormData($(this)[0]);
  
        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // Update the result element with the predicted class
                $('#result').text('Predicted class: ' + response.class);
            },
            error: function(xhr, status, error) {
                // Handle error if any
                console.error(error);
            }
        });
    });
  });