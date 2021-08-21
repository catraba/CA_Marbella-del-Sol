var myVar = document.getElementById("myVar").value;
var temporada = document.getElementById("temporada").value;
var obj = JSON.parse(myVar.replace(/'/g, '"'));

  let old_sel = null;
  let old_grafica = null;
  
  
  function getPrueba () {
    var sel = document.getElementById("prueba").value;

    if (old_sel != null) {
      old_grafica.destroy(); 

      try {
        old_grafica = createChart(sel, temporada);
      } catch (err) {}

    } else {
      var grafica = createChart(sel, temporada);

      old_sel = sel;
      old_grafica = grafica;
    }
  }
  
  function createChart (sel, temporada) {
    var ctx = document.getElementById("myChart").getContext("2d");  
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: obj[sel]['Fechas'],
        datasets: [
          {
            label: sel,
            data: obj[sel]['Tiempos'],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)'
            ]
          },
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: false
          },
          title: {
            text: "TEMPORADA " + temporada,
            display: true
          }
        },  
        scales: {
          x: {
            title: {
              display: true,
              text: 'Semana'
            }
          }
        }
      }
    });

    return myChart
  }