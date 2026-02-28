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

