$(function () {
    $('#date_a').cxCalendar();

    $('.sure-citydata').click('on',function () {
        var obj = {time:$('#date_a').val(),index:$('.selectindex option:selected').text()};
        //obj.time 时间    obj.index 指标
        $.ajax({
            url:'',
            data:obj,
            success:function (e) {
                $('.citydata-lefttable').empty();
                var arr = ['地区生产总值对比表','固定资产投资额对比表','工业产品产销率对比表']
                var option = ""
                arr.map(function (msg) {
                    //name属性里面放置的是 这个的标识  可以改动  以便于点击获取相对应的表格
                    option += "<p name="+msg+">"+msg+"</p>";
                });

                $('.citydata-lefttable').append(option);
            }
        })
    })

    $('.citydata-lefttable').delegate('p','click',function () {
        console.log($(this).attr('name'));
        $.ajax({
            url:'',
            data:$(this).attr('name'),
            success:function () {
                $('.citydata-righttable').empty();
                var dataarr = [{city:'成都',indexname:'地区生产总值对比表',company:'亿元',allprice:'111',pricenum:'111',compare:'111',comparenum:'111'},{city:'成都',indexname:'地区生产总值对比表',allprice:'222',pricenum:'222',compare:'222',comparenum:'222'}]
                var option = "<tr>"+
                    "<th>指标名称</th>"+
                    "<th>城市</th>"+
                    "<th>计算单位</th>"+
                    "<th>本年累计</th>"+
                    "<th>位次</th>"+
                    "<th>对比数据</th>"+
                    "<th>位次</th>"+
                    "</tr>";

                dataarr.map(function (msg) {
                    console.log(msg);
                    option += "<tr>"+
                        "<td>"+msg.indexname+"</td>"+
                        "<td>"+msg.city+"</td>"+
                        "<td>"+msg.company+"</td>"+
                        "<td>"+msg.allprice+"</td>"+
                        "<td>"+msg.pricenum+"</td>"+
                        "<td>"+msg.compare+"</td>"+
                        "<td>"+msg.comparenum+"</td>"+
                        "</tr>";
                })
                $('.citydata-righttable').append(option);
            }
        })
    })
})
