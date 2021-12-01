function createTransaction() {
    let form_ser = $('#form-transaction').serializeArray()
    var data_json = {}

    // $.map(form_ser, (n, i) => {
    //     data_json[n['name']] = n['value'];
    // });
    
    for (var i = 0; i < form_ser.length; i++){
        data_json[form_ser[i]['name']] = form_ser[i]['value'];
    }
    console.log(data_json)
    $.ajax({
        type: 'POST',
        url: '/api/transaction/create',
        data: data_json,
        success: function() {
            showToast('Transacción realizada con éxito.')
        }.bind(this),
        error: function() {
            showToast('No se pudo realizar la transacción.')
        }.bind(this)
    });
    return false;
}

function showToast(msg = 'Text') {
    $('#toast-text').text(msg);
    $('.toast').toast('show')
}