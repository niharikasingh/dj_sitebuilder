function update_page(question_id, question_type, question_option) {

    // Toasts
    toast(question_id, question_type, question_option);

    // Colors
    color(question_id, question_type, question_option);

    // Dictionary
    var card_dictionary = dictionary(question_id, question_type, question_option);

    // Display next card below current card
    nextcard(card_dictionary);

    // If student has filled out final card
    if ('STUDENT_EMAIL' in card_dictionary) {

        // Load modal for finalization
        loadmodal(card_dictionary);

    }

    else {
        // Return true
        return true
    }
}