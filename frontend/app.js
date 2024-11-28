async function generateCode() {
    const descriptionInput = document.getElementById("descriptionInput").value;
    const responseDiv = document.getElementById("response");
    
    responseDiv.innerHTML = "Generating code...";

    const response = await fetch('http://127.0.0.1:8000/generate_code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: descriptionInput })
    });

    const data = await response.json();
    responseDiv.innerHTML = `<pre>${data.generated_code}</pre>`;
}

async function submitCode() {
    const codeInput = document.getElementById("codeInput").value;
    const responseDiv = document.getElementById("response");
    
    responseDiv.innerHTML = "Analyzing code...";

    const response = await fetch('http://127.0.0.1:8000/submit_code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: codeInput })
    });

    const data = await response.json();
    responseDiv.innerHTML = `<pre>${data.feedback}</pre>`;
}

