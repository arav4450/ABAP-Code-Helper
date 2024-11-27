<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ABAP Code Helper System</title>
</head>
<body>

<h1>ABAP Code Helper System</h1>

<p>A system for generating and analyzing ABAP code using an AI-powered language model.</p>

<h2>Features</h2>
<ul>
    <li><strong>Code Generation Prompt</strong>: Users can input a description of the ABAP code they need, and the system generates the corresponding code.</li>
    <li><strong>Code Analysis</strong>: Users can submit existing ABAP code for analysis, and the system provides feedback or suggestions.</li>
    <li><strong>Structured Feedback</strong>: The generated code and feedback are presented in a clear and readable format.</li>
    
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>FastAPI</strong>: For creating the backend API and handling code generation requests.</li>
    <li><strong>Ollama</strong>: For integrating the LLM (Large Language Model) to generate code and provide analysis.</li>
    <li><strong>JavaScript (Frontend)</strong>: To handle user inputs and display results.</li>
    <li><strong>HTML/CSS (Frontend)</strong>: For creating and styling the user interface.</li>
</ul>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/yourusername/abap-code-helper.git
cd abap-code-helper</code></pre>
    </li>
    <li><strong>Set Up the Environment</strong>: Create and activate a virtual environment:
        <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
    </li>
    <li><strong>Install pip-tools</strong>: Install `pip-tools` for dependency management:
        <pre><code>pip install pip-tools</code></pre>
    </li>
    
    <li><strong>Compile and Sync Dependencies</strong>: Use `pip-compile` to generate the `dev.txt` file and `pip-sync` to install the dependencies:
        <pre><code>pip-compile dev.in
pip-sync dev.txt</code></pre>
    </li>
    <li><strong>Download and Install Ollama</strong>: Visit <a href="https://ollama.com/">Ollama.com</a> to download Ollama. Pull the required model by running the following command:
        <pre><code>ollama pull code-llm</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<p>Run the FastAPI backend:</p>
<pre><code>uvicorn main:app --reload</code></pre>
<p>The backend will be available at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>.</p>

<p>Run the Frontend: Open the <code>index.html</code> file in a browser. You can also serve it with a simple HTTP server:</p>
<pre><code>python -m http.server 8000</code></pre>
<p>Navigate to <a href="http://localhost:8000">http://localhost:8000</a> to interact with the application.</p>



</body>
</html>
