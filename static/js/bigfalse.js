$(function () {
	tiny_setup();
});

function tiny_setup() {
    $('#nav-menu-nogame').click(nav_menu_nogame);
}

function nav_menu_nogame() {
	$('#glabal_dialog').modal();
}
