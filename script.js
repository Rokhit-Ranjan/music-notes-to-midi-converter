document.getElementById('convertButton').addEventListener('click', () => {
    const notes = document.getElementById('notesInput').value;
    
    fetch('http://127.0.0.1:5500/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ notes })
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const link = document.getElementById('downloadLink');
        link.href = url;
        link.download = 'music.mid';
        link.style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});
