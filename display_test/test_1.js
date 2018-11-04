var idData = [];
var myChart ;
function showRealTime(ec, list_devData) {
    var vData = [];
    var valData = [];
    var dataH = 0;
    var dateL = 0;
    var Series = [];
    for (var index = 0; index < list_devData.length; index++) {
        var obj = list_devData[index];
        vData.push(obj.dataName);
        idData.push(obj.dataId);
        valData.push(obj.dataValue);
        if (index > 1) {
            dataH = dataH - list_devData[index - 1].dataH > 0 ? dataH : list_devData[index - 1].dataH;
            dateL = dateL - list_devData[index - 1].dateL > 0 ? dataL  : list_devData[index - 1].dateL;
        } else {
            dataH = list_devData[index].dataH;
            dataL = list_devData[index].dataL;
        }
        var serie = new Object();
        serie.name = obj.dataName;
        serie.type = 'line';
        serie.data = (function() {
            var res = [];
            var len = 10;
            while (len--) {
                res.push(obj.dataValue);
            }
            return res;
        })();
        Series.push(serie);
    }

    myChart = ec.init(document.getElementById('main_chart_socket'));
    var option = {
        title : {
            text : '动态数据'
        },
        tooltip : {
            trigger : 'axis'
        },
        legend : {
            data : vData
        },
        toolbox : {
            show : true,
            feature : {
                /*mark : {
                    show : true
                },
                dataView : {
                    show : true,
                    readOnly : false
                },
                magicType : {
                    show : true,
                    type : ['line']
                },
                restore : {
                    show : false
                },*/
                saveAsImage : {
                    show : true
                }
            }
        },
        dataZoom : {
            show : false,
            start : 0,
            end : 100
        },
        xAxis : [{
                    type : 'category',
                    boundaryGap : true,
                    data : (function() {
                        var now = new Date();
                        var res = [];
                        var len = 10;
                        while (len--) {
                            res.unshift(now.toLocaleTimeString().replace(/^\D*/, ''));
                            now = new Date(now - 2000);
                        }
                        return res;
                    })()
                }],
        yAxis : [{
                    type : 'value',
                    scale : true,
                    name : '温度',
                    boundaryGap : [0.2, 0.2]
                }],
        series : Series
    };
    myChart.setOption(option, true);
    /*eval('parent.$("#iframeToDeviceGroup")[0].contentWindow.main_chart_socket= option'); 这个可以存储数据到windowd对象百试不爽*/
}
function refreshshowRealTime(dateId, dateValue) {
    var Sindex = 0;
    for (var index = 0; index < idData.length; index++) {
        if(idData[index] == dateId){
            dateId = index;
        }
    }
    myChart.addData([[Sindex,dateValue, false, false]]);
}