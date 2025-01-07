"""
Implementation of a full-stack feature that calculates data points
using a formula on the backend and visualizes them on the frontend using JavaScript-generated graphs.
Users can input coefficients for a quadratic equation y = ax^2 + bx + c
visualize the graph of the function over a range of x-values.


Save the backend code in a file (e.g., app.py).
Save the frontend code in an HTML file (e.g., index.html).
python app.py
Open the frontend in a browser (ensure it's served from the Flask backend or use a tool like live-server).
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate y = ax^2 + bx + c for a range of x values.
    """
    data = request.json
    a = data.get('a', 0)
    b = data.get('b', 0)
    c = data.get('c', 0)
    x_min = data.get('x_min', -10)
    x_max = data.get('x_max', 10)
    step = data.get('step', 0.1)

    # Generate data points
    x_values = [x_min + i * step for i in range(int((x_max - x_min) / step) + 1)]
    y_values = [a * x**2 + b * x + c for x in x_values]

    return jsonify({'x': x_values, 'y': y_values})

if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quadratic Function Plotter</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Quadratic Function Plotter</h1>
    
    <!-- Input Form -->
    <form id="formula-form">
        <label for="a">a:</label>
        <input type="number" id="a" name="a" value="1" required>
        <label for="b">b:</label>
        <input type="number" id="b" name="b" value="0" required>
        <label for="c">c:</label>
        <input type="number" id="c" name="c" value="0" required>
        <label for="x_min">x_min:</label>
        <input type="number" id="x_min" name="x_min" value="-10" required>
        <label for="x_max">x_max:</label>
        <input type="number" id="x_max" name="x_max" value="10" required>
        <label for="step">Step:</label>
        <input type="number" id="step" name="step" value="0.1" required>
        <button type="submit">Plot</button>
    </form>

    <!-- Graph Container -->
    <canvas id="chart"></canvas>

    <script>
        // Handle Form Submission
        document.getElementById('formula-form').addEventListener('submit', async function (event) {
            event.preventDefault();

            // Gather Input Data
            const a = parseFloat(document.getElementById('a').value);
            const b = parseFloat(document.getElementById('b').value);
            const c = parseFloat(document.getElementById('c').value);
            const x_min = parseFloat(document.getElementById('x_min').value);
            const x_max = parseFloat(document.getElementById('x_max').value);
            const step = parseFloat(document.getElementById('step').value);

            // Send Data to Backend
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ a, b, c, x_min, x_max, step })
            });

            const data = await response.json();

            // Render Chart
            renderChart(data.x, data.y);
        });

        // Render Chart Function
        function renderChart(xValues, yValues) {
            const ctx = document.getElementById('chart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: xValues,
                    datasets: [{
                        label: 'y = ax² + bx + c',
                        data: yValues,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2,
                        fill: false,
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        x: { title: { display: true, text: 'x' } },
                        y: { title: { display: true, text: 'y' } },
                    }
                }
            });
        }
    </script>
</body>
</html>
