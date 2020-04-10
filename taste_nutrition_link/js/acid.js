(function() {
    d3.csv('../Data2/acid.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.Acid))            
            const trace1 = {
                x: data.map(entry => entry.Acid),
                y: data.map(entry => entry.sodium),
                name: "sodium",
                mode: 'lines+markers'
            }
            const trace2 = {
                x: data.map(entry => entry.Acid),
                y: data.map(entry => entry.calories),
                name: "calories",
                mode: 'lines+markers'
            }
            const trace3 = {
                x: data.map(entry => entry.Acid),
                y: data.map(entry => entry.fat),
                name: "fat",
                mode: 'lines+markers'
            }
            const trace4 = {
                x: data.map(entry => entry.Acid),
                y: data.map(entry => entry.cholesterol),
                name: "cholesterol",
                mode: 'lines+markers'
            }
            const trace5 = {
                x: data.map(entry => entry.Acid),
                y: data.map(entry => entry.carbs),
                name: "carbohydrates",
                mode: 'lines+markers'
            }
            const trace6 = {
                x: data.map(entry => entry.Acid),
                y: data.map(entry => entry.protein),
                name: "protein",
                mode: 'lines+markers'
            }           
            const layout = {
                title: 'Tasting Metric: Acid, Nutrition Correlation',
                xaxis: {
                    title: 'Intensity',
                  },
                  yaxis: {
                    title: '% Daily Value(PDV)',
                  },
                  height: 750
            }
            Plotly.newPlot('acid', [trace1, trace2, trace3, trace4, trace5, trace6], layout)
        })
        .catch(err => console.log(err))       
})()
