let ctx = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4'], // Timestamps ( date / heure )
        datasets: [{
            label: 'Temperature',
            data: [10,20,30,40], //Valeur récupéré par l'Arduino
            borderColor: [
                'rgba(255, 15, 15, 1)',
            ],
            borderWidth: 1
        }, {
            label: 'humidity',
            data: [20,10,0,0], //Valeur récupéré par l'Arduino
            borderColor: [
                'rgba(15, 255, 15, 1)',
            ],
            borderWidth: 1
        }, {
            label: 'Temperature ressentie',
            data: [15,25,35,45], //Valeur récupéré par l'Arduino
            borderColor: [
                'rgba(15, 15, 255, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});