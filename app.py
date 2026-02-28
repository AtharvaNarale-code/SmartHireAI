
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

from Backend.extraction import (
    pdf_extract,
    list_to_json,
    extract_skill_from_resume,
    generate_analysis_metrics,
    calculate_skill_strength,
)
import Backend.Skilldomain as Skilldomain
from Backend.llm import get_recruiter_note, get_candidate_roadmap

load_dotenv()   
GEMINI_KEY = os.getenv("GEMINI_API_KEY")


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024#cap to store resumes 

#all routing and rendering logic is here

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hr")
def hr_view():
    return render_template("hr.html")

def _process_single_resume(file, candidate_name: str, domain: str) -> dict:
    try:
        # 1. Extract text from PDF
        raw_text = pdf_extract(file)
        if not raw_text:
            raise ValueError("Empty PDF — could not extract text.")

        # 2. Section parsing + skill extraction
        structured = list_to_json(raw_text)
        skills     = extract_skill_from_resume(structured, Skilldomain.SKILL_DICT)
        metrics    = generate_analysis_metrics(skills)

        # 3. Weighted scoring (strong=1.5, medium=1.0, weak=0.5)
        scoring = calculate_skill_strength(metrics)
        score   = scoring["skill_strength_score"]

        # 4. LLM recruiter note 
        note = get_recruiter_note(GEMINI_KEY, candidate_name, domain, skills, score)
        return {
            "name":           candidate_name,
            "score":          score,
            "weighted_sum":   scoring["weighted_sum"],
            "net_skills":     scoring["net_skills"],
            "metrics":        metrics,
            "skills":         skills,
            "recruiter_note": note,
        }
    except Exception as exc:
        return {
            "name":           candidate_name,
            "score":          0.0,
            "weighted_sum":   0.0,
            "net_skills":     0,
            "metrics":        {},
            "skills":         {},
            "recruiter_note": f"Processing failed: {exc}",
            "error":          str(exc),
        }