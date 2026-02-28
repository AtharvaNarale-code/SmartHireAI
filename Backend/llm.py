from google import genai

def get_recruiter_note(api_key, name, domain, skills, score):
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"Candidate: {name}, Domain: {domain}, Score: {score}. Skills: {skills}. Write a 40-word HR fitment note in form strong point: , major skill gap(dont include languages in skill gap): , suitable for which role:"
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def get_candidate_roadmap(api_key, name, domain, skills, score):
    """
    Generates Skill Gaps, a Learning Path, and a Mermaid Flowchart.
    """
    client = genai.Client(api_key=api_key)
    
    # Inside get_candidate_roadmap in llm.py
    prompt = f"""
    Act as a Technical Career Coach. 
    Candidate Background: {skills} (Score: {score})
    Target Role: {domain}

    Compare candidate's skills against standard requirements for a {domain}. 
    Even if candidate has high scores in their OWN field , 
    identify what they LACK to enter {domain}.
    generate linear chart in mermaid syntax showing learning path from current skills to target role.

    Example: If a Data Scientist applies for Game Dev, identify 'C++' and 'Game Engines' as MAJOR gaps.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={'response_mime_type': 'application/json'}
        )
        import json
        return json.loads(response.text)
    except Exception as e:
        print(f"Roadmap Error: {e}")
        return {
            "skill_gaps": [], 
            "learning_path": ["Focus on core domain fundamentals."], 
            "mermaid_chart": "graph TD\n  A[Start] --> B[Learn Fundamentals] --> C[Target Role]"
        }