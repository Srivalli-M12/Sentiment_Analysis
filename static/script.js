async function analyzeSentiment() {
    let text = document.getElementById("inputText").value;
    let response = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });

    let data = await response.json();

    // Display sentiment scores
    document.getElementById("result").innerHTML = `
        <p>Positive: ${data.scores.pos}</p>
        <p>Neutral: ${data.scores.neu}</p>
        <p>Negative: ${data.scores.neg}</p>
    `;

    // Render Plotly graph properl
    let figData = JSON.parse(data.graph_json);
    Plotly.newPlot("graph", figData.data, figData.layout);
}