$(function () {

// 双联动日期示例
    (function(){
        var dateFirst = $('#date_first');
        var dateLast = $('#date_last');
        var dateFirstApi;
        var dateLastApi;

        dateFirst.cxCalendar(function(api){
            dateFirstApi = api;
        });

        dateLast.cxCalendar(function(api){
            dateLastApi = api;
        });

        dateFirst.bind('change', function(){
            var firstTime = parseInt(dateFirstApi.getDate('TIME'), 10);
            var lastTime = parseInt(dateLastApi.getDate('TIME'), 10);

            if (lastTime < firstTime) {
                dateLastApi.clearDate();
            };

            dateLastApi.setOptions({
                startDate: firstTime
            });
            dateLastApi.gotoDate(firstTime);
            dateLastApi.show();
        });
    })();


    $('.sure-citydata').click('on',function () {
        var obj = {firsttime:$('#date_first').val(),lasttime:$('#date_last').val(),index:$('.selectindex option:selected').text(),city:$('.selectcity option:selected').text()}

        $.ajax({
            url:'',
            data:obj,
            success:function (e) {
                $('.citydata-lefttable').empty();
                var arr = ['社会融资规模占GDP比重','第一产业增值占GDP比重','第二产业增值占GDP比重']
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
                var dataarr = [{_201701:'111',_201702:'111',_201703:'111',_201704:'111',_201705:'111'},{_201701:'111',_201702:'111',_201703:'111',_201704:'111',_201705:'111'}]
                var option = "<tr>"+
                    "<th>2017-01数据值</th>"+
                    "<th>2017-02数据值</th>"+
                    "<th>2017-03数据值</th>"+
                    "<th>2017-04数据值</th>"+
                    "<th>2017-05数据值</th>"+
                    "</tr>";

                dataarr.map(function (msg) {
                    console.log(msg);
                    option += "<tr>"+
                        "<td>"+msg._201701+"</td>"+
                        "<td>"+msg._201702+"</td>"+
                        "<td>"+msg._201703+"</td>"+
                        "<td>"+msg._201704+"</td>"+
                        "<td>"+msg._201705+"</td>"+
                        "</tr>";
                })
                $('.citydata-righttable').append(option);
            }
        })
    })

})
