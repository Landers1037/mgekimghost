$("#button").click(function () {
    if($("input#photo").val().length >0)
        $('.progress').css('display', 'block');
});
function up() {
    var formData = new FormData($("form")[0]);
    if (formData.get("photo")["name"] != "") {
        $.ajax({
            url: "/upload_new/",
            type: 'POST',
            data: formData,
            // 告诉jQuery不要去处理发送的数据
            processData: false,
            // 告诉jQuery不要去设置Content-Type请求头
            contentType: false,
            xhr: function () {
                var myxhr = $.ajaxSettings.xhr();
                myxhr.upload.addEventListener('progress', progress, false);
                return myxhr;
            },
            // async : false,
            success: function () {
                $("#ajax_refresh").load(location.href+' #row');
            }

        }).fail(function () {
            alert('上传失败');
        });

    }else {
        return false;
    }
}

function progress(e) {
     if (e.lengthComputable) {
         var percent = Math.round(e.loaded * 100 / e.total);
         $('.progress-bar').css('width', percent + '%').text(percent + '%');
     }
}