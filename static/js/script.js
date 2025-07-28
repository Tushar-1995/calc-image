function calculate() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const resultDiv = document.getElementById('result');

    if (num1 && num2) {
        fetch(`/add?a=${num1}&b=${num2}`)
            .then(response => response.text())
            .then(data => {
                resultDiv.textContent = `Result: ${data}`;
            })
            .catch(error => {
                resultDiv.textContent = `Error: ${error.message}`;
            });
    } else {
        resultDiv.textContent = 'Please enter both numbers.';
    }
}