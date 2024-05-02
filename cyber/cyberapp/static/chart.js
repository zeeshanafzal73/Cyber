// admin_logged_in_users_chart.js
document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from server
    fetch('/path/to/logged_in_users_chart/')
    .then(response => response.json())
    .then(data => {
        // Render chart using Chart.js
        var ctx = document.getElementById('logged-in-users-chart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: data,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });
});
