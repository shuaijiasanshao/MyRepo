$(function () {

    Highcharts.setOptions({
        global : {
            useUTC : false
        }
    });

    $('#container').highcharts('StockChart', {
        chart : {
            events : {
                load : function () {
                    var series_data_1 = this.series[0],
                        series_data_2 = this.series[1],
                        series_data_3 = this.series[2];

                    setInterval(function() {
                        $.getJSON('/data', function(data) {
                            console.log(data);
                            var data_1 = data.data_1,
                                data_2 = data.data_2,
                                data_3 = data.data_3;

                            $.each(data_1, function(i, d){
                               series_data_1.addPoint(d, true, true)
                            })
                            $.each(data_2, function(i, d){
                               series_data_2.addPoint(d, true, true)
                            })
                            $.each(data_3, function(i, d){
                               series_data_3.addPoint(d, true, true)
                            })
                        });
                    },1000)
                }
            }},

            legend: {
                enabled: true,
                layout: 'vertical',
                align: 'left',
                verticalAlign: 'top',
                backgroundColor: '#FCFFC5',
                borderColor: 'black',
                borderWidth: 2,
                shadow: true
            },

            rangeSelector: {
                buttons: [{
                    count: 1,
                    type: 'minute',
                    text: '1M'
                }, {
                    count: 5,
                    type: 'minute',
                    text: '5M'
                }, {
                    count: 1,
                    type: 'hour',
                    text: '1H'
                }, {
                    count: 2,
                    type: 'hour',
                    text: '2H'
                }, {
                    type: 'all',
                    text: 'All'
                }],
                inputEnabled: true,
                selected: 4
            },

            title : {
                text : 'Test random data'
            },

            xAxis: {
                title: {
                    text: 'time'
                },
                type: 'datetime',
                tickPixelInterval: 50
            },

            yAxis: [{
                title: {
                    text: 'value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            }],

            exporting: {
                enabled: false
            },

            series : [{
                name : 'data_1',
                type: 'spline',
                data: (function() {
                    var data = [],
                        time = (new Date()).getTime(),
                        i;

                    // 给曲线y值赋初值0
                    for (i = -999; i <= 0; i++) {
                        data.push({
                            x: time + i * 1000,
                            data_1: 0
                        });
                    }
                    return data;
                })()
            },{
                name : 'data_2',
                type: 'spline',
                data: (function() {
                    var data = [],
                        time = (new Date()).getTime(),
                        i;

                    // 给曲线y值赋初值0
                    for (i = -999; i <= 0; i++) {
                        data.push({
                            x: time + i * 1000,
                            data_2: 0
                        });
                    }
                    return data;
                })()

            },{
                name : 'data_3',
                type: 'spline',
                data: (function() {
                    var data = [],
                        time = (new Date()).getTime(),
                        i;
                    // 给曲线y值赋初值0
                    for (i = -999; i <= 0; i++) {
                        data.push({
                            x: time + i * 1000,
                            data_3: 0
                        });
                    }
                    return data;
                })()
            }]
        }
    );
});