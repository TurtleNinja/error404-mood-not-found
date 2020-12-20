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


    function createLineChart(data, label) {
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
                    borderColor: '#C4E2FF',
                    data: data,
                    lineTension: 0,
                }]
            },

            // Styling Configurations
            options: {
                maintainAspectRatio: false,
                legend: { display: false },
                title: {
                    display: true,
                    text: 'Mood Rating Trend',
                    fontColor: 'white'
                },
                labels: {
                    fontColor: 'white'
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            max: 5,
                            fontColor: "white",
                        },
                        scaleLabel: {
                            display: true,
                            labelString: "Rating",
                            fontColor: "white",
                        }
                    }],
                    xAxes: [{
                        ticks: {
                            fontColor: 'white'
                        },
                        scaleLabel: {
                            display: true,
                            labelString: "Date",
                            fontColor: "white"
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
