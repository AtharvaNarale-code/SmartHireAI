import re
import pdfplumber
from typing import Dict
from Backend import Skilldomain


# ===============================
# PDF EXTRACTION
# ===============================

def pdf_extract(uploaded_file) -> str | None:
    extracted_text = ""

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"

        cleaned_text = "\n".join(
            line.strip()
            for line in extracted_text.split("\n")
            if line.strip()
        )

        cleaned_text = re.sub(r"[^\S\r\n]+", " ", cleaned_text)
        cleaned_text = cleaned_text.lower()

        return cleaned_text

    except Exception as e:
        print(f"[pdf_extract] Error: {e}")
        return None


# ===============================
# SECTION MAPPING
# ===============================

def list_to_json(cleaned_text: str) -> Dict[str, str]:
    data = {key: "" for key in Skilldomain.sections_map.keys()}
    current_key = None

    for line in cleaned_text.split("\n"):
        clean_line = line.strip().lower().rstrip(":")
        if not clean_line:
            continue

        found_header = False
        for master_key, aliases in Skilldomain.sections_map.items():
            if any(clean_line == alias for alias in aliases):
                current_key = master_key
                found_header = True
                break

        if not found_header and current_key:
            data[current_key] += " " + line.strip()

    return data


# ===============================
# CONFIDENCE DETECTION
# ===============================

COMPLEX_TERMS = {
    "architecture", "scalable", "distributed", "microservices",
    "low latency", "high availability", "production",
    "pipeline", "real-time", "concurrent", "asynchronous",
}

CONFIDENCE_RANK = {"weak": 1, "medium": 2, "strong": 3}


def detect_confidence(context_line: str, section: str) -> str:
    text = context_line.lower()
    words = set(re.findall(r"\b\w+\b", text))

    # 🔥 Complex terms now require strong verb to qualify
    if any(term in text for term in COMPLEX_TERMS) and \
       any(word in words for word in Skilldomain.SIGNAL_MAP["strong"]):
        return "strong"

    for level in ["strong", "medium", "weak"]:
        if words & Skilldomain.SIGNAL_MAP[level]:
            return level

    return "weak"


# ===============================
# SKILL EXTRACTION (DEDUP FIXED)
# ===============================

def extract_skill_from_resume(resume_json: Dict, skill_dict: Dict) -> Dict:

    sections = {
        "summary":  resume_json.get("summary", ""),
        "projects": resume_json.get("projects", ""),
        "skills":   resume_json.get("skills", ""),
        "experience": resume_json.get("experience", "")
    }

    extracted_skills: Dict[str, list] = {
        "languages":   [],
        "frameworks":  [],
        "databases":   [],
        "ml_tools":    [],
        "cloud_tools": [],
        "concepts":    [],
        "other_tools": [],
    }

    skill_conf_map = {}  # 🔥 store best confidence per skill

    for category, skills in skill_dict.items():
        for skill_key, skill_data in skills.items():

            canonical = skill_data["canonical"]
            best_conf = None

            for alias in skill_data["aliases"]:
                pattern = r"\b" + re.escape(alias) + r"\b"

                for section_name, section_text in sections.items():
                    for line in re.split(r"[.\n•]", section_text):  # 🔥 removed hyphen split
                        if re.search(pattern, line, re.IGNORECASE):
                            conf = detect_confidence(line.strip(), section_name)

                            # 🔥 Experience section gets slight upgrade
                            if section_name == "experience" and conf == "medium":
                                conf = "strong"

                            if not best_conf or CONFIDENCE_RANK[conf] > CONFIDENCE_RANK[best_conf]:
                                best_conf = conf

            if best_conf:
                skill_conf_map[canonical] = best_conf

    # Map to structured categories
    for category, skills in skill_dict.items():
        for skill_key, skill_data in skills.items():
            canonical = skill_data["canonical"]

            if canonical in skill_conf_map:
                entry = {
                    "skill": canonical,
                    "confidence": skill_conf_map[canonical]
                }

                if category == "programming_languages":
                    extracted_skills["languages"].append(entry)
                elif category in ("frontend_frameworks", "backend_frameworks"):
                    extracted_skills["frameworks"].append(entry)
                elif category == "databases":
                    extracted_skills["databases"].append(entry)
                elif category == "data_science_ml":
                    extracted_skills["ml_tools"].append(entry)
                elif category == "cloud_devops":
                    extracted_skills["cloud_tools"].append(entry)
                elif category in ("concepts", "trading_concepts"):
                    extracted_skills["concepts"].append(entry)
                else:
                    extracted_skills["other_tools"].append(entry)

    return {k: v for k, v in extracted_skills.items() if v}


# ===============================
# ANALYSIS METRICS
# ===============================

def generate_analysis_metrics(extracted_skills: Dict) -> Dict:
    return {
        "total_strong_skills": sum(
            1 for sl in extracted_skills.values()
            for s in sl if s.get("confidence") == "strong"
        ),
        "total_medium_skills": sum(
            1 for sl in extracted_skills.values()
            for s in sl if s.get("confidence") == "medium"
        ),
        "total_weak_skills": sum(
            1 for sl in extracted_skills.values()
            for s in sl if s.get("confidence") == "weak"
        ),
    }


# ===============================
# SKILL STRENGTH SCORE (REFINED)
# ===============================

def calculate_skill_strength(analysis_metrics: Dict) -> Dict:

    WEIGHTS = {"strong": 1.6, "medium": 1.0, "weak": 0.3}  # 🔥 weak reduced

    strong = analysis_metrics.get("total_strong_skills", 0)
    medium = analysis_metrics.get("total_medium_skills", 0)
    weak   = analysis_metrics.get("total_weak_skills", 0)

    net_skills = strong + medium + weak

    if net_skills == 0:
        return {
            "net_skills": 0,
            "weighted_sum": 0.0,
            "skill_strength_score": 0.0,
        }

    weighted_sum = (
        strong * WEIGHTS["strong"] +
        medium * WEIGHTS["medium"] +
        weak   * WEIGHTS["weak"]
    )

    base_score = weighted_sum / (net_skills * WEIGHTS["strong"])

    # 🔥 Volume bonus only if strong+medium >= 8
    strong_medium_total = strong + medium
    if strong_medium_total >= 8:
        volume_bonus = min((strong_medium_total - 8) * 0.02, 0.12)
    else:
        volume_bonus = 0

    final_score = min(base_score + volume_bonus, 1.0)

    return {
        "net_skills": net_skills,
        "weighted_sum": round(weighted_sum, 2),
        "skill_strength_score": round(final_score, 4),
    }


# ===============================
# PROJECT DEPTH SCORE
# ===============================

def calculate_project_depth_score(resume_json: Dict, skill_dict: Dict) -> float:

    project_text = resume_json.get("projects", "")

    if not project_text:
        return 0.0

    project_skills = set()

    for category, skills in skill_dict.items():
        for skill_key, skill_data in skills.items():
            for alias in skill_data["aliases"]:
                if re.search(r"\b" + re.escape(alias) + r"\b", project_text, re.IGNORECASE):
                    project_skills.add(skill_data["canonical"])

    return round(min(len(project_skills) / 12, 1.0), 4)
