$(document).ready(function () {    
    let passwordId = '#password';
    let showPasswordId = '#showPassword';

    $(showPasswordId).click(function (e) {
        let type = $(passwordId).attr('type') === 'password' ? 'text' : 'password';
        $(passwordId).attr('type', type);
    });
});