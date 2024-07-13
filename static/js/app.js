from .app

function encrypt() {
    const message = document.getElementById('message').value;
    const key = document.getElementById('key').value;
    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').value = data.ciphertext;
    })
    .catch(error => console.error('Error:', error));
}

function decrypt() {
    const message = document.getElementById('message').value;
    const key = document.getElementById('key').value;
    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').value = data.plaintext;
    })
    .catch(error => console.error('Error:', error));
}
