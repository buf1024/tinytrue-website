$(function () {
	passage_setup();
});

function passage_setup() {
    $("#submit_comment").bind("click", submit_comment);
    $("button[id^='comment_reply']").bind("click", comment_reply);
}

function submit_comment() {
    var name = $("#input_name").val();
    var email = $("#input_email").val();
    var comment = $("#input_comment").val();
    if(name == "" || email == "") {
        alert("昵称或电子邮箱为空!");
        return;
    }
    if(comment.length <= 20) {
        alert("评论不能少于20个字符!");
        return;
    }
    var site = $("#input_site").val();
    
    var id = $("#submit_comment").attr("data");
    var obj = {"id":id, "name":name, "email":email, "site":site, "comment":comment};
    var jobj = JSON.stringify(obj);
    var url = "/comment/passage";
    
    $.post(url, jobj, function(data) {
        if(data == "FAIL") {
            alert("提交评论失败!");
        }else{
            location.reload();
        }
    });
    
    return;
}

function comment_reply() {
    var id = $("#" + event.target.id).attr("data");
}