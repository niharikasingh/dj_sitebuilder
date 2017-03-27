// Rebuild the dictionary every time the function is called
function dictionary(question_id, question_type, question_option) {

    // Initialize dict
    var card_dictionary = {};

    // Enter the current question into dict
    card_dictionary['current'] = [question_id, question_option];

    // For every card, append key/value pairs into dictionary by iterating over the number of selected buttons
    var selected_buttons = document.getElementsByClassName("btn-large waves-effect waves-white pear");
    for (var i = 0; i < selected_buttons.length; i++) {
        card_dictionary[selected_buttons[i].name.slice(0, -7)] = selected_buttons[i].value;
    }

    // For textboxes with class validate valid, update the value in each key/value pair
    var textboxes_validate = $(".validate, .valid");
    for (var i = 0; i < textboxes_validate.length; i++) {
        if ((textboxes_validate[i].id) in card_dictionary) {
            card_dictionary[textboxes_validate[i].id] = textboxes_validate[i].value;
        }
    }

    // For datepickers, update the value in each key/value pair
    var datepickers = $(".datepicker, .picker__input");
    for (var i = 0; i < datepickers.length; i++) {
        if ((datepickers[i].id) in card_dictionary) {
            card_dictionary[datepickers[i].id] = datepickers[i].value;
        }
    }

    // Return dictionary
    return card_dictionary;
}


    // // NOT BEING USED
    //
    //
    // // For textboxes with class autocomplete, update the value in each key/value pair
    // var textboxes_autocomplete = $(".autocomplete");
    // for (var i = 0; i < textboxes_autocomplete.length; i++) {
    //     if ((textboxes_autocomplete[i].id) in card_dictionary) {
    //         card_dictionary[textboxes_autocomplete[i].id.substring(0,4)] = textboxes_autocomplete[i].value
    //     }
    // }
    //
    // // For dropdowns, update the value in each key/value pair
    // var dropdowns = $(".initialized");
    // for (var i = 0; i < dropdowns.length; i++) {
    //     if ((dropdowns[i].id.substring(0,4)) in card_dictionary) {
    //         card_dictionary[dropdowns[i].id.substring(0,4)] = dropdowns[i].value;
    //     }
    // }