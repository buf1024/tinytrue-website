$(function () {
	mngcomment_setup();
});

function mngcomment_setup() {
    $("button[id^='mngcomment_view']").bind("click", mngcomment_view);
    $("button[id^='mngcomment_reply']").bind("click", mngcomment_reply);
    $("button[id^='mngcomment_delete']").bind("click", mngcomment_delete);
    
    $("#dialog_confirm_no").bind("click", dialog_confirm_no);
    $("#dialog_confirm_yes").bind("click", dialog_confirm_yes);
}

function dialog_confirm_yes() {
    var id = $("#dialog_confirm_yes").attr("data");  
    var obj = {"id":id};
    var jobj = JSON.stringify(obj);
    $.post("/manage/comment/delete", jobj, function(data) {
        if(data == "FAIL") {
            alert("操作失败!");
        }else{
            location.reload();
        }
    });
}

function dialog_confirm_no() {
    $("#dialog_confirm").modal("hide");
}

function mngcomment_view(event) {
    var idpair = $("#" + event.target.id).attr("data");
    var ids = idpaire.split('|');
    
    location = "/passage/" + ids[1] + "#" +ids[0]
}

function mngcomment_delete(event) {
    /*var id = $("#" + event.target.id).attr("data");
    $("#dialog_confirm").modal();
    $("#dialog_confirm_yes").attr("data", id);  */

}

function mngcomment_reply(event) {
  /*  $("#dialog_catalog_title").html("增加分类");
    $("#catalog_title").val("");
    $("#catalog_desc").val("");
    var sel = "#catalog_opt_type option[value='1'";
    $(sel).attr("selected", true);
    $("#dialog_catalog_save").attr("role", "new");
    $("#dialog_catalog").modal();*/
}
