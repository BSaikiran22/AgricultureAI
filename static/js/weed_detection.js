document.getElementById('weedForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('image', document.getElementById('imageInput').files[0]);

    const response = await fetch('http://127.0.0.1:5000/detect_weed', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    document.getElementById('weedResult').innerHTML = `Weed Detected: ${result.weed_detected}`;
});
