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
function login() {
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        if(username=="" || password=="") {
            $('.Login-word').html('请输入用户名密码')
        }else{
            var xsrf = get_cookie_by_name('_xsrf');
            $.ajax({
                'url':'/login',
                'type': 'POST',
                'data':{'username':username, 'password':password, '_xsrf':xsrf},
                success:function(e){
                    //这里需要返回三种结果  1 用户不存在   2 密码输入错误  3 登陆成功
                    if (e == '0') {
                        window.location.href = "/";
                    } else if (e == '1') {
                        alert('用户名或密码不正确!');
                    }
                },
                error: function(e) {
                    alert(e);
                }
            });
        }
}
$(function () {
    $('.Login-btn').click('on', login);
    $('.Login-box').find('input').map(function () {
        
    })
})
function clearword(){
    $('.Login-word').html('');
}
