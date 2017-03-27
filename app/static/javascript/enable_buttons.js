function enable_buttons(origin) {

    // Assign question buttons to a variable
    question_buttons = $("[name=" + origin.id + "_BUTTON]");

    console.log(question_buttons)
    // If origin.pattern is undefined, enable button
    if (origin.pattern == undefined) {
        question_buttons.attr('disabled', false);
        console.log("Hello")
    }

    // Else, compare pattern to value
    else {

        // Format pattern as Javascript regex object
        var regex = new RegExp("^" + origin.pattern + "$");

        // If value matches regex, enable buttons
        if (regex.test(origin.value)) {
            question_buttons.attr('disabled', false);

            // If user presses enter, and there is only one button, click the button
            if (question_buttons.length == 1) {
                if (event.keyCode == 13) {
                    question_buttons.click();
                }
            }
        }

        // Else, disable buttons
        else {
            $("[name=" + origin.id + "_BUTTON]").attr('disabled', false)
        }
    }
}