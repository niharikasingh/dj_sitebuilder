function loadmodal(card_dictionary) {

    // Initialize modal
    $('.modal').modal({
        dismissible: false,
        opacity: .5,
        in_duration: 300,
        out_duration: 200,
        starting_top: '4%',
        ending_top: '10%',
        ready: function () {

            // Programmatically fill in modal data
            $('#STUDENT_NAME_MODAL').val(card_dictionary['STUDENT_NAME']);
            $('#INSTRUCTOR_NAME_MODAL').val(card_dictionary['INSTRUCTOR_NAME']);
            $('#CLIENT_NAME_MODAL').val(card_dictionary['CLIENT_NAME']);
            $('#CLIENT_GENDER_MODAL').val(card_dictionary['CLIENT_GENDER']);
            $('#CLIENT_DOB_MODAL').val(card_dictionary['CLIENT_DOB']);
            $('#CLIENT_ADDRESS_MODAL').val(card_dictionary['CLIENT_ADDRESS']);
            $('#COURT_MODAL').val(card_dictionary['COURT']);
            $('#DOCKET_MODAL').val(card_dictionary['DOCKET']);
            $('#ARRAIGNMENT_MODAL').val(card_dictionary['ARRAIGNMENT']);
            $('#CHARGE_1_MODAL').val(card_dictionary['CHARGE_1']);
            $('#CHARGE_2_MODAL').val(card_dictionary['CHARGE_2']);
            $('#CHARGE_3_MODAL').val(card_dictionary['CHARGE_3']);
            $('#CHARGE_4_MODAL').val(card_dictionary['CHARGE_4']);
            $('#CHARGE_5_MODAL').val(card_dictionary['CHARGE_5']);
            $('#COMPLAINT_DATE_MODAL').val(card_dictionary['COMPLAINT_DATE']);
            $('#OFFENSE_DATE_MODAL').val(card_dictionary['OFFENSE_DATE']);
            $('#INCIDENT_ADDRESS_MODAL').val(card_dictionary['INCIDENT_ADDRESS']);
            $('#INCIDENT_NUMBER_MODAL').val(card_dictionary['INCIDENT_NUMBER']);
            $('#NEXT_DATE_MODAL').val(card_dictionary['NEXT_DATE']);
            $('#NEXT_PURPOSE_MODAL').val(card_dictionary['NEXT_PURPOSE']);
            $('#STUDENT_EMAIL_MODAL').val(card_dictionary['STUDENT_EMAIL']);
        }
    });

    // Open modal
    $('#modal').modal('open');
}