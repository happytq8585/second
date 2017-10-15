//删除用户的id
var delid = null;
//根据删除的内容不同传一个特定的字符串   例如 删除用户时传进来user 删除权限管理时 传进来power  根据这个写ajax是来判断删除的是什么  同事避免删除事件重复多次
var delroot = null;
//删除用户出现弹窗
function BusinessDel(id,root){
    delid=id;
    delroot = root;
    $('.delAlert').css({display:'block'})
}
//取消删除用户
function noDel(){
    $('.delAlert').css({display:'none'})
}
//取消添加用户
function noAdd(){
    $('.addAlert').css({display:'none'});
}

function get_cookie_by_name(name) {
    var start = document.cookie.indexOf(name);
    if (start != -1) {
        var res = "";
        var end = document.cookie.indexOf(";", start+1);
        if (end == -1) {
            res = document.cookie.substring(start+name.length+1);
        } else {
            res = document.cookie.substring(start+name.length+1, end);
        }
        return res;
    }
    return "";
}

//确认删除用户
function sureDel(){
    noDel();
    var xsrf = get_cookie_by_name('_xsrf');
    var url  = '';
    var data = {};
    if (delroot == 'user') {
        url = '/delconnector';
        data = {'uid':delid, '_xsrf': xsrf};
    } else if (delroot == 'power') {
        url = '/delauth';
        data = {'aid': delid, '_xsrf':xsrf};
    }
    $.ajax({
        'url': url,
        'type': 'POST',
        'data': data,
        success:function (e) {
            alert('删除成功');
            window.location.reload();
        },
        error: function(e) {
            alert('出错啦');
        }
    });
}
function clearword(){
    $('.addBox-word').html('');
}
$(function () {
    $('.BusinessAdd').click('on',function () {
        $('.addAlert').css({display:'block'});
    });

    //添加用户的对象  其中select  会有一个默认值极为初始值
    var addsure = {};
    //选择城市
    addsure.city = $('.selectcity').val();
    //选择职务
    addsure.place = $('.selectposition').val();
    //选择部门
    addsure.department = $('.selectdepartment').val();
    //性别
    addsure.gender = $('.gender').val();
    $('.addBox-word').html('');
    //确认添加用户
    $('#sureAdd').click('on',function () {
        $('.addBox').find('input').map(function () {
            addsure[$(this).attr('name')] = $(this).val();
        });
        if (addsure.name == '') {
            $('.addBox-word').html('请填写用户名!');
            return -1;
        }
        if (addsure.password == '') {
            $('.addBox-word').html('请填写密码!');
            return -1;
        }
        $('.addAlert').css({display:'none'});
        var xsrf = get_cookie_by_name('_xsrf');
        addsure._xsrf = xsrf;
        $.ajax({
            'url':'/addconnector',
            'type': 'POST',
            'data':addsure,
            success:function (e) {
                if (e == '0') {
                    alert('添加成功!');
                } else if (e == '1') {
                    alert('用户已存在!');
                }
                window.location.reload();
            },
            error:function(e) {
                alert('系统出错!');
            }
        });
    });

    //添加权限
    $('.addpower').click('on',function () {
        $('.addpower-input').css({display:'block'});
    })
    //取消添加
    $('#del-adpower').click('on',function () {
        $('.addpower-input').css({display:'none'});
    })
    //确认添加
    $('#sure-addpower').click('on',function () {
        var addpower = $(this).prev().val();
        $('.addpower-input').css({display:'none'});
        var xsrf = get_cookie_by_name('_xsrf');
        if(addpower!=""){
            $.ajax({
                'url':'/addauth',
                'type': 'POST',
                'data':{'name':addpower, '_xsrf':xsrf},
                success: function(e) {
                    if (e == '0') {
                        alert('添加成功');
                        window.location.reload();
                    } else if (e == '1') {
                        alert('该权限已经存在');
                    } else {
                        alert('添加失败');
                    }
                },
                error: function(e) {
                }
            })
        }

        $(this).prev().val('');
    })

    //授权管理
    $('.sure-authorize').click('on',function () {
        //这里不确定你需要的数据是什么  一种是 只有授权的数组（例如  【'信息1','信息2'】）   还有一种是 包含每个权限以及其是否授权的TRUE FALSE 的对象（例如  {"信息1"：TRUE,"信息2"：FALSE,"信息3"：FALSE,"信息4"：TRUE}）

        var obj = {};

        var arr = [];

        $('.authorize').find('input').map(function () {
            //这个是包含所有权限以及是否添加的对象
            obj[$(this).attr('value')] = this.checked;
            //这个是添加权限的数组 数组里面有的就添加
            if(this.checked){
                arr.push($(this).attr('value'));
            }

        })
        if (arr.length == 0) {
            alert('没有选择权限以授权');
            return -1;
        }
        var xsrf = get_cookie_by_name('_xsrf');
        var arr_data = arr.join(',');
        $.ajax({
            'url':'/authorize',
            'type': 'POST',
            //根据你的需求选择那种数据   剩下的一种可以删掉
            'data': {'data': arr_data, '_xsrf':xsrf},
            success: function(e) {
                if (e == '1') {
                    alert('没有数据上传!');
                } else {
                    alert('授权成功!');
                }
            },
            error: function(e) {
                alert('出错啦');
            }
        })
        console.log(obj,arr);
    })
    $('.cancle-authorize').click('on',function () {
        $('.authorize').find('input').map(function () {
            this.checked = false;
        })
    })

})



