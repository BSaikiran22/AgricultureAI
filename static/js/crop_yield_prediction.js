document.getElementById('yieldForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        temperature: document.getElementById('temperature').value,
        humidity: document.getElementById('humidity').value,
        rainfall: document.getElementById('rainfall').value,
    };

    const response = await fetch('http://127.0.0.1:5000/predict_yield', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById('yieldResult').innerHTML = `Predicted Yield: ${result.predicted_yield}`;
});
