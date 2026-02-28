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

### Final Score Formula

## 📷 Dashboard View

<p align="center">
  <img src="images/DAshboard.png" width="800"/>
</p>

## 📷 Candidate View

<p align="center">
  <img src="images/Candidate%20view.png" width="800"/>
</p>
