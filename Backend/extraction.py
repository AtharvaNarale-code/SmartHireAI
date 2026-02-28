import re
import pdfplumber
from typing import Dict
from Backend import Skilldomain

#Pdf Extraction

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
    
#Section Mapping

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
    
#Confidence Detection

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
    

