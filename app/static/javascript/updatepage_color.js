function color(question_id, question_type, question_option) {

    // Assign buttons on current card to variable buttons
    var buttons = document.getElementsByName(question_id + '_BUTTON');

    // Iterate over buttons on current card
    for (var i = 0; i < buttons.length; i++) {

        // If current button value equals selected button value, change button color to pear
        if (buttons[i].value == question_option)
            buttons[i].className = ("btn-large waves-effect waves-white pear");

        // Else return current button to default color
        else {
            buttons[i].className = ("btn-large waves-effect waves-white disabled-color");
            }
        }
}