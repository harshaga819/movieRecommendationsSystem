function getRecommendations() {
    const movie = document.getElementById("movie-select").value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ movie: movie }),
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = "<h3>Recommended Movies:</h3><ul>" +
            data.recommendations.map(title => `<li>${title}</li>`).join('') +
            "</ul>";
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
