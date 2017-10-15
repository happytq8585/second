$(function () {
    $('.EconomicsAdd').click('on',function () {
        $('.addpower-input').css({display:'block'})
    })
    $('.FinanceAdd').click('on',function () {
        $('.addpower-input1').css({display:'block'})
    })
    $('.ContrastAdd').click('on',function () {
        $('.addpower-input2').css({display:'block'})
    })

    //取消添加经济指标
    $('#del-adpower').click('on',function () {
        $('.addpower-input').css({display:'none'});
    })
    //确认添加经济指标
    $('#sure-addpower').click('on',function () {
        console.log();
        var addpower = $(this).prev().val();
        $('.addpower-input').css({display:'none'});

        if(addpower!=""){
            $.ajax({
                url:'',
                data:addpower,
            })
        }

        $(this).prev().val('');
    })

    //取消添加金融基础指标
    $('#del-finance').click('on',function () {
        $('.addpower-input1').css({display:'none'});
    })
    //确认添加金融基础指标
    $('#sure-addfinance').click('on',function () {
        console.log();
        var addpower = $(this).prev().val();
        $('.addpower-input1').css({display:'none'});

        if(addpower!=""){
            $.ajax({
                url:'',
                data:addpower,
            })
        }

        $(this).prev().val('');
    })

    //取消添加对比分析
    $('#del-Contrast').click('on',function () {
        $('.addpower-input2').css({display:'none'});
    })
    //确认添加对比分析
    $('#sure-addContrast').click('on',function () {
        console.log();
        var addpower = $(this).prev().val();
        $('.addpower-input2').css({display:'none'});

        if(addpower!=""){
            $.ajax({
                url:'',
                data:addpower,
            })
        }

        $(this).prev().val('');
    })
})
var delnum,delword;
function BusinessDel(num,word) {
    console.log(num,word);
    delnum = num;
    delword = word;
    // word 分为三种情况   分别是 Economics（经济）  Finance（金融） Contrast（分析）
    // num  传入的是删除的那一项
    // 两个结合起来就可以准确地判断出删除的数据是那一条
   $('.delAlert').css({display:'block'})
}
// 确定删除
function sureDel() {
    noDel();
    $.ajax({
        url:'',
        data:{delnum:delnum,delword:delword}
    })
}
//取消删除
function noDel() {
    $('.delAlert').css({display:'none'})
}