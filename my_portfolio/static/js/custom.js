$(function(){
    // Refactor and handle serve side!!
    if(localStorage.getItem('sent') == 'true'){
        toastr.success('Email sent', 'Success');
        localStorage.clear();
    }
    
    $("#contact-form")[0].reset();



});



$('#send-email').on('click', function () {

  // Need to handle this server side ...
    localStorage.setItem('sent', 'true');
    window.location.reload();


});
