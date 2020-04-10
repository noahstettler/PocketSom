(function() {
    d3.csv('../Data2/m_colors.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.Color))            
            const trace1 = {
                x: data.map(entry => entry.Color),
                y: data.map(entry => entry.Body),
                name: "body",
                type: 'bar'
            }
            const trace2 = {
                x: data.map(entry => entry.Color),
                y: data.map(entry => entry.Tannin),
                name: "tannin",
                type: 'bar'
            }
            const trace3 = {
                x: data.map(entry => entry.Color),
                y: data.map(entry => entry.Acid),
                name: "acid",
                type: 'bar'
            }
            const trace4 = {
                x: data.map(entry => entry.Color),
                y: data.map(entry => entry.ABV),
                name: "alcohol by volume(abv)",
                type: 'bar'
            }
            const trace5 = {
                x: data.map(entry => entry.Color),
                y: data.map(entry => entry.Dryness),
                name: "dryness",
                type: 'bar'
            }
            const trace6 = {
                x: data.map(entry => entry.Color),
                y: data.map(entry => entry.Fruit),
                name: "fruit",
                type: 'bar'
            }           
            const layout = {
                title: 'Red vs. White: Average Tasting Metrics',
                barmode: 'group',
                xaxis: {
                    title: 'Color of Wine',
                  },
                  yaxis: {
                    title: 'Intensity',
                  }
            }
            Plotly.newPlot('m_colors', [trace1, trace2, trace3, trace4, trace5, trace6], layout)
        })
        .catch(err => console.log(err))       
})()