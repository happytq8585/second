$(function () {
    $('#date_a').cxCalendar();

    //确认查找
    $('.sure-citydata').click('on',function () {
        var obj = {time:$('#date_a').val(),city:$('.selectcity option:selected').text(),index:$('.selectindex option:selected').text()};
        //obj.time 时间    obj.city 城市    obj.index 指标
        $.ajax({
            url:'',
            data:obj,
            success:function (e) {
                $('.table-bordered').empty();
                //这里需要返回表格的内容 格式为 [{},{},{}];
                var dataarr = [{city:'成都',time:'201704',indexname:'社会融资规模',allprice:'111',pricenum:'111',compare:'111',comparenum:'111'},{city:'成都',time:'201704',indexname:'社会融资规模',allprice:'222',pricenum:'222',compare:'222',comparenum:'222'}]
                var tableoption = "<tr>"+
                    "<th>城市</th>"+
                    "<th>数据年月</th>"+
                    "<th>统计指标名称</th>"+
                    "<th>本年累计（亿元）</th>"+
                    "<th>位次</th>"+
                    "<th>比去年同期</th>"+
                    "<th>位次</th>"+
                    "</tr>";

                dataarr.map(function (msg) {
                    console.log(msg);
                    tableoption += "<tr>"+
                        "<td>"+msg.city+"</td>"+
                        "<td>"+msg.time+"</td>"+
                        "<td>"+msg.indexname+"</td>"+
                        "<td>"+msg.allprice+"</td>"+
                        "<td>"+msg.pricenum+"</td>"+
                        "<td>"+msg.compare+"</td>"+
                        "<td>"+msg.comparenum+"</td>"+
                        "</tr>";
                })
                $('.table-bordered').append(tableoption);
            }
        })

    })
    //打印事件
    $('.print-citydata').click('on',function () {
        
    })
})
