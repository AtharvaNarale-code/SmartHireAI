# SmartHire AI
## An Explainable and Intelligent Recruitment Screening System

SmartHire AI addresses the **“Black Box” problem in recruitment** by providing a **transparent, data-driven, and explainable candidate evaluation system**.

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, which often ignores real skill confidence, experience depth, and project impact.  
SmartHire AI replaces this approach with **context-aware skill intelligence** designed for both **HR teams** and **candidates**.

---

## Problem Statement

Modern recruitment systems suffer from:
- Keyword-based filtering
- Lack of transparency in candidate rejection
- Resume keyword stuffing
- No feedback or growth roadmap for candidates

This results in unfair screening and inefficient hiring decisions.

---

## Solution Overview

SmartHire AI provides:
- Contextual skill evaluation
- Experience and project-weighted scoring
- AI-generated recruiter summaries
- Candidate-facing learning roadmaps

This ensures realistic ranking and explainable hiring decisions.

---

## Key Features

### For HR Teams
- Data-driven candidate leaderboard
- Skill confidence analysis
- AI-generated recruiter summaries
- Batch resume screening

### For Candidates
- Transparent skill scoring
- Identified technical gaps
- AI-generated structured learning roadmap
- Domain-based fitment evaluation

---

## System Architecture

The system follows a modular processing pipeline:

**Extraction → Scoring → Intelligence → Visualization**

| Layer | Technology | Purpose |
|------|-----------|---------|
| Backend | Python / Flask 3.0 | API handling and routing |
| Extraction | pdfplumber + Regex | PDF to structured JSON |
| Logic Engine | Weighted Scoring System | Skill confidence evaluation |
| AI Engine | Gemini 1.5 Flash | Recruiter summaries and learning roadmaps |
| Frontend | Tailwind CSS + Mermaid.js | Dashboard UI and flowcharts |

---

## Core Algorithm: Weighted Skill Strength Engine

Skills are detected contextually and categorized into three levels:

- Strong (1.6x multiplier)
- Medium (1.0x multiplier)
- Weak (0.3x multiplier)


### Key Logic Enhancements
- Experience sections receive higher credibility
- Deeper project involvement increases ranking
- Complex skills require strong action verbs
- Keyword stuffing is prevented through contextual validation

---

## HR Intelligence Dashboard

Designed for fast and efficient resume screening.

Features:
- Batch resume uploads
- Automatic leaderboard ranking
- AI-generated 40-word recruiter summaries
- Skill distribution visualization


## 📷 Dashboard View

<p align="center">
  <img src="images/DAshboard.png" width="800"/>
</p>

---

## Candidate Development Portal

A transparent evaluation interface to help candidates understand their fitment.

Features:
- Domain-specific scoring (e.g., ML Engineer, Game Developer)
- Identified skill gaps
- AI-generated step-by-step learning roadmap
- Mermaid.js based roadmap visualization

## 📷 Candidate View

<p align="center">
  <img src="images/Candidate%20view.png" width="800"/>
</p>

---

## Skill Strength Breakdown Example

- Strong Skills: 11  
- Medium Skills: 2  
- Weak Skills: 12  

Total Skills Detected: 25  
Weighted Skill Sum: 23.2  
Final Score: 68%

---
## ⚙ Setup & Installation

1) Install Dependencies:                                                                                                                                                                                             - pip install flask google-genai python-dotenv pdfplumber                                                                                                                                                                
2) Configure Environment Variables
-Create a .env file in the root directory:                                                                                                                                                                          --GEMINI_API_KEY=your_api_key_here

3) Run the Application                                                                                                                                                                                               -  python app.py                                                                                                                                                                                                      - Server will start at:
 -http://127.0.0.1:5000
---

SmartHire-AI/
│
├── app.py
├── Backend/
│   ├── Skilldomain.py
│   ├── scoring_engine.py
│
├── templates/
├── static/
├── images/
│   ├── setup.jpeg
│   ├── leaderboard.jpeg
│   ├── candidate-detail.jpeg
│
└── README.md
