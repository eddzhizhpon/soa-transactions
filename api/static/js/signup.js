function createUser() {
    $.ajax({
        type: 'POST',
        url: '/api/auth/signup/',
        data:  $('#form-user').serialize(),
        success: function(response) {
            showToast('Usuario creado con éxito.')
        }.bind(this),
        error: function(xhr, errmsg, err) {
            var msg = ''
            let errors = xhr.responseJSON.errors;
            console.log(typeof errors)
            for (let errorid in errors) {
                msg += errorid + ': ' + errors[errorid] + '\n';
            }
            showToast('No se pudo crear al usuario.\n' + msg)
        }.bind(this)
    });
    return false;
}

function generatePassword() {
    $.ajax({
        type: 'GET',
        url: '/api/auth/genpassword',
        success: function(response) {
            $('#password').val(response['password'])
            $('#password1').val(response['password'])
            $('#password2').val(response['password']) 
        }.bind(this),
        error: function(xhr, errmsg, err) {
            $('#genpassword').disabled = false;
            showToast('No se pudo generar la contraseña.\n')
        }.bind(this)
    });
    return false;
}

function showToast(msg = 'Text') {
    $('#toast-text').text(msg);
    $('.toast').toast('show')
}