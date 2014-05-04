$(function () {
	passage_setup();
});

function passage_setup() {
    tinymce.init({selector:"#tinymce_editor"});

    $("#passage_save").bind("click", passage_save);
    $("#passage_save_draft").bind("click", passage_save_draft);
/*    $("#dialog_confirm_no").bind("click", dialog_confirm_no);
    $("#dialog_confirm_yes").bind("click", dialog_confirm_yes);*/
}

function dialog_confirm_yes() {
    var id = $("#dialog_confirm_yes").attr("data");  
    var obj = {"id":id};
    var jobj = JSON.stringify(obj);
    $.post("/manage/catalog/delete", jobj, function(data) {
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

function passage_save() {
    edit_passage(false);

}

function passage_save_draft() {
    edit_passage(true);
}
function edit_passage(isdraft) {
    var title = $("#passage_title").val();
    if(title == "") {
        alert("文章标题为空!");
        return 0;
    }
    var content = tinymce.get("tinymce_editor").getContent();
    if(content == "") {
        alert("文章内容为空!");
        return 0;
    }
    var sumary = $("#passage_summary").val();
    if(sumary == "") {
        alert("文章摘要为空!");
        return 0;
    }
    var cat = $("#passage_catalog").val();
    if(cat <= 0) {
        alert("文章分类无效!");
        return 0;
    }
    var visiable = $("#passage_visiable").is(":checked");    
    var front = $("#passage_front").is(":checked");
    var comment = $("#passage_commentable").is(":checked");    
    var tags = $("#passage_tags").val();
    
    var obj = new Object();
    obj.title = title;
    obj.content = content;
    obj.sumary = sumary;
    obj.catalog = cat;
    obj.visiable = visiable;
    obj.front = front;
    obj.commentable = comment;
    obj.tags = tags;
    
    obj.isdraft = isdraft;
    
    var role = $("#passage_save").attr("role");
    
    obj.role = role;
    
    if(role == "update") {
        obj.id = $("#passage_save").attr("data");
    }
    
    var jobj = JSON.stringify(obj);
       
    $.post("/manage/passage/edit", jobj, function (data) {
        if(data == "FAIL") {
            alert("保存文件失败!");
        }else{
            location.href = "/manage/passage";
        }
    });
}
