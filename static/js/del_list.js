    function list_del() {
        var del = $("#count5");
        del.css("opacity","1");
        $(".checkbox").show();
        var dow = $("#count6");
        dow.css("opacity","1");
        dow.css("background","#008573");
        var cancel = $("#count7");
        cancel.css("opacity","1");
        cancel.css("background","#ffa07b");
        var geturl = $("#count8");
        geturl.css("opacity","1");
        geturl.css("background","#b87333");
    }
    function del() {
        var checked = $("input[name='check']:checked");
        var ids = [];
        $.each(checked,function () {
            ids.push($(this).attr("value"));

        });
            var temp_form = document.createElement("form");
            var input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'ids';
            input.value = ids;
            temp_form.action = '/edit/';
            //如需打开新窗口，form的target属性要设置为'_blank'
            temp_form.target = "_self";
            temp_form.method = "post";
            temp_form.appendChild(input);
            temp_form.style.display = "none";
            //添加参数
            document.body.appendChild(temp_form);
            //提交数据
            if($("#count5").css("opacity")=="1"){
                temp_form.submit();
            }

    }
    function list_dow() {
        var checked = $("input[name='check']:checked");
        var ids = [];
        $.each(checked,function () {
            ids.push($(this).attr("value"));
        });
            var temp_form = document.createElement("form");
            var input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'ids';
            input.value = ids;
            temp_form.action = '/download/';
            //如需打开新窗口，form的target属性要设置为'_blank'
            temp_form.target = "_self";
            temp_form.method = "post";
            temp_form.appendChild(input);
            temp_form.style.display = "none";
            //添加参数
            document.body.appendChild(temp_form);
            //提交数据
            if($("#count6").css("opacity")=="1" && ids.length!=0){
                temp_form.submit();
            }
    }
    function cancel() {
    var checked = $("input[name='check']:checked");
    $.each(checked,function () {
            $(this).prop("checked",false);
            $(this).attr("checked",false);
        });
    $("#count5").css("opacity","0");
    $("#count6").css("opacity","0");
    $("#count7").css("opacity","0");
    $(".checkbox").hide();
    }

    function get_url() {
        var checked = $("input[name='check']:checked");
        var ids = [];
        $.each(checked,function () {
            ids.push($(this).attr("value"));
        });
        var temp_form = document.createElement("form");
            var input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'ids';
            input.value = ids;
            temp_form.action = '/urls/';
            //如需打开新窗口，form的target属性要设置为'_blank'
            temp_form.target = "_blank";
            temp_form.method = "post";
            temp_form.appendChild(input);
            temp_form.style.display = "none";
            //添加参数
            document.body.appendChild(temp_form);
            //提交数据
            if($("#count8").css("opacity")=="1" && ids.length!=0){
                temp_form.submit();
            }
    }