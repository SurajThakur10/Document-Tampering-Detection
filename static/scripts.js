// script.js

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var form = this;
    var formData = new FormData(form);

    // Send a POST request to the server with form data
    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the result
        document.getElementById('ssimScore').textContent = data.ssim_score;
        document.getElementById('resultText').textContent = data.result_text;
        document.getElementById('result').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});
