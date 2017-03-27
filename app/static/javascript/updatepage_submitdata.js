function submitdata() {

    var card_dictionary = {};

    $('#modal :input').each(function() {
        card_dictionary[this.id.slice(0, -6)] = this.value
    });

    $.ajax({
        type: "POST",
        url: "/submitdata/",
        data: {submit_data: JSON.stringify(card_dictionary)},
        beforeSend: function () {
            setTimeout(function(){
                $("[id$='_CARD']").fadeOut();
            }, 300);

            setTimeout(function () {
                $("#LOADER_CARD").fadeIn(1000);
            }, 1000);
        },
        success: function (returned_data) {
            $("#LOADER_CARD").fadeOut();
            setTimeout(function () {
                $("#SUBMITTED_CARD").fadeIn(1000);
            }, 1000);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            setTimeout(function () {
                $("#LOADER_CARD").fadeOut(1000);
            }, 3000);
            setTimeout(function () {
                $("#ERROR_CARD").fadeIn(1000);
            }, 4000);
        }
    })
}