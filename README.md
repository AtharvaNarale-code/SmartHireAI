<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SmartHire AI - Project Documentation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f4f6f9;
            color: #333;
            line-height: 1.6;
        }

        .container {
            width: 85%;
            margin: auto;
            padding: 40px 0;
        }

        h1, h2, h3, h4 {
            color: #1f2937;
        }

        h1 {
            text-align: center;
            font-size: 40px;
        }

        h3 {
            text-align: center;
            color: #4b5563;
        }

        hr {
            margin: 40px 0;
            border: none;
            height: 1px;
            background-color: #ddd;
        }

        img {
            max-width: 100%;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        pre {
            background-color: #1f2937;
            color: #ffffff;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
        }

        ul, ol {
            padding-left: 20px;
        }

        .center {
            text-align: center;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: #111827;
            color: white;
            margin-top: 40px;
        }

        strong {
            color: #2563eb;
        }

    </style>
</head>

<body>

<div class="container">

    <h1>🚀 SmartHire AI</h1>
    <h3>AI-Powered Resume Screening & Candidate Ranking System</h3>

    <div class="center">
        <img src="images/banner.png" alt="SmartHire AI Banner">
    </div>

    <hr>

    <h2>📌 Project Overview</h2>
    <div class="card">
        <p>
            SmartHire AI is an intelligent recruitment assistant designed to automate the resume screening process.
            It uses Artificial Intelligence and Machine Learning techniques to analyze resumes, match them with job descriptions,
            and rank candidates based on relevance score.
        </p>

        <p>
            The goal of this project is to reduce manual hiring effort, eliminate bias,
            and speed up recruitment decisions using data-driven insights.
        </p>
    </div>

    <hr>

    <h2>🎯 Problem Statement</h2>
    <div class="card">
        <ul>
            <li>Recruiters receive hundreds of resumes for a single job role.</li>
            <li>Manual screening is time-consuming and inefficient.</li>
            <li>High chances of missing qualified candidates.</li>
            <li>Human bias affects shortlisting decisions.</li>
        </ul>
    </div>

    <hr>

    <h2>💡 Solution</h2>
    <div class="card">
        <p>SmartHire AI automatically:</p>
        <ul>
            <li>Parses resumes (PDF/DOC format)</li>
            <li>Extracts skills, experience, and qualifications</li>
            <li>Matches resume data with job description</li>
            <li>Generates candidate ranking score</li>
            <li>Displays sorted candidate list</li>
        </ul>
    </div>

    <hr>

    <h2>🛠️ Tech Stack</h2>
    <div class="card">
        <ul>
            <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
            <li><strong>Backend:</strong> Python (Flask)</li>
            <li><strong>Machine Learning:</strong> Scikit-learn, NLP</li>
            <li><strong>Database:</strong> SQLite / MySQL</li>
            <li><strong>Deployment:</strong> GitHub / Local Server</li>
        </ul>
    </div>

    <hr>

    <h2>📂 Project Structure</h2>
    <div class="card">
<pre>
SmartHire-AI/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── model/
│   └── resume_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
</pre>
    </div>

    <hr>

    <h2>🖼️ Project Screenshots</h2>

    <h4>🏠 Home Page</h4>
    <div class="center">
        <img src="images/home.png" alt="Home Page Screenshot">
    </div>

    <h4>📊 Resume Analysis Output</h4>
    <div class="center">
        <img src="images/result.png" alt="Result Page Screenshot">
    </div>

    <hr>

    <h2>⚙️ Installation & Setup</h2>

    <h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/yourusername/SmartHire-AI.git
cd SmartHire-AI
</pre>

    <h3>2️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

    <h3>3️⃣ Run the Application</h3>
<pre>
python app.py
</pre>

    <p>
        Open your browser and go to:
        <strong>http://127.0.0.1:5000</strong>
    </p>

    <hr>

    <h2>📈 Features</h2>
    <div class="card">
        <ul>
            <li>Resume Upload (PDF)</li>
            <li>Skill Extraction using NLP</li>
            <li>Keyword Matching Algorithm</li>
            <li>Candidate Scoring System</li>
            <li>Admin Dashboard (Optional)</li>
        </ul>
    </div>

    <hr>

    <h2>🧠 Future Improvements</h2>
    <div class="card">
        <ul>
            <li>Deep Learning-based resume classification</li>
            <li>AI Interview Bot Integration</li>
            <li>Cloud Deployment (AWS / Azure)</li>
            <li>Real-time Analytics Dashboard</li>
        </ul>
    </div>

    <hr>

    <h2>📊 Working Flow</h2>
    <div class="card">
        <ol>
            <li>User uploads resume</li>
            <li>System extracts text using NLP</li>
            <li>Job description is processed</li>
            <li>Similarity score calculated</li>
            <li>Candidate ranked accordingly</li>
        </ol>
    </div>

    <hr>

    <h2>👨‍💻 Author</h2>
    <div class="card">
        <p>
            <strong>ABC</strong><br>
            B.Tech – Computer Science (AIML)<br>
            Aspiring AI Engineer & Tech Content Creator
        </p>
    </div>

</div>

<footer>
    <p>📜 This project is open-source and available under the MIT License.</p>
    <p>⭐ If you like this project, don’t forget to give it a star!</p>
</footer>

</body>
</html>
