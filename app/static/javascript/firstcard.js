function firstcard() {

    $("#primary_splash").fadeOut();

    $("#STUDENT_NAME_CARD").fadeIn(1000).css('marginTop', '10%');

    setTimeout(function(){
        $("#STUDENT_NAME").focus();
    },400);

//     // Display first card
//     document.getElementById("STUDENT_NAME_CARD").style.display = "";
//
//     // Scroll to first card
//     $("html, body").delay(150).animate({scrollTop: $("#STUDENT_NAME_CARD").position().top + 500}, 500);
}

