$(document).ready(function() {
    var data;
    var label;
    $.ajax({
        url: "/get_data",
        type: "get",
        success: function(result) {
          full_data = JSON.parse(result.mood);
          data = full_data['data'];
          label = full_data['labels'];
          createLineChart(data, label);
        },
    });

    function changeColor(data){
        var colors = [];
        for(i = 0; i < data.length; i++){
            var color = "";

            if(data[i] == 1) {
                color = "red";
            }
            else if(data[i] == 2) {
                color = "orange"
            }
            else if(data[i] == 3) {
                color = "blue"
            }
            else if(data[i] == 4) {
                color = "green"
            }
            else{
                color = "yellow"
            }
            colors.push(color);
        }
        console.log(colors);
        return colors;
    }


    function createLineChart(data, label) {
        Chart.defaults.global.defaultFontColor = 'black';
        Chart.defaults.global.defaultFontSize = 13;
        Chart.defaults.global.defaultFontFamily = "'Red Hat Display', sans-serif";

        var ctx = document.getElementById('moodchart').getContext('2d');
        var chart = new Chart(ctx, {
            // want to create line chart
            type: 'line',

            // Data
            data: {
                labels: label,
                datasets: [{
                    // label: 'Mood Rating Trend',
                    // backgroundColor: 'rgb(255,182,193)',
                    pointBackgroundColor: changeColor(data),
                    pointBorderColor: changeColor(data),
                    borderColor: 'rgba(0, 0, 0, 0.3)',
                    borderWidth: 1.5,
                    fill: false,
                    data: data,
                    lineTension: 0,
                }]
            },

            // Styling Configurations
            options: {
                maintainAspectRatio: false,
                legend: { display: false },
                animation: {
                    duration: 0,
                },
                title: {
                    display: true,
                    text: 'Mood Rating Trend (Last 7)',
                },
                labels: {
                },
                scales: {
                    pointLabels: { fontSize: 100 },
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            max: 5,
                            stepSize: 1,
                        },
                        scaleLabel: {
                            display: true,
                            labelString: "Rating",
                        }
                    }],
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: "Date",
                        }
                    }],
                },
                elements: {
                    line: {
                        tension: 0,
                    }
                }
            }
        });
    }

});
