$(function () {
	tiny_setup();
});

function tiny_setup() {
    $("#nav-menu-nogame").bind("click", nav_menu_nogame);
}

function nav_menu_nogame() {
    $("#nogame_dialog").modal();
}

function admin_login_submit() {
    var email$ = $('#inputEmail')[0];
    var password$ = $('#inputPassword')[0];
    var pass = false;
         
    if(email$.value != "" && password$.value != "") {
        pass = true;
    }
    
    if(pass) {
        var login_form$ = $('#admin-login-summit')[0];
        login_form$.submit();
    }else {
        $('#glabal_dialog').modal();
    }
    return pass;
}

/**/
