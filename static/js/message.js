$(document).on('submit', '#form-message', function(e){
    e.preventDefault();
    $.ajax({
      type: 'POST',
      url: '/add-message/',
      data: {
        message: $('#id_message').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        action: 'post',
      },
      dataType: 'json',
      success: function(data){
        alert("Your message has been sent");
        $("#form-message")[0].reset();
      }
    })
  })