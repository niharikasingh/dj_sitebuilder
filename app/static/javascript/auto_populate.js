function auto_populate(origin) {

    // If data-autocomplete is not empty, change the input value to data-autocomplete
    if ($(origin).data('auto_populate') != 'nan') {
        $(origin).val($(origin).data('auto_populate'))
    }
}