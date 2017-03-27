function nextcard(card_dictionary){

    var from = ('#' + card_dictionary['current'][0] + '_CARD');
    var to = ('#' + card_dictionary['current'][1] + '_CARD');

    $(to).insertAfter(from);

    // Display next card
    $(to).fadeIn(1000);

    // Scroll to next card
    $("html, body").animate({scrollTop: $(from).offset().top + 500}, 500);

    // Stop focusing input of prvevious card
    $(from.substring(0, from.length - 5)).blur();

    // Start focusing input of next card
    setTimeout(function () {
        $(to.substring(0, to.length - 5)).focus();
    }, 400);
}
