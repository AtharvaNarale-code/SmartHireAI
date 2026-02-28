from google import genai 

def get_recruiter_note(api_key,name,domain,skills,score):
    client = genai.Client(api_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"Candidate: {name}, Domain: {domain}, Score: {score}. Skills: {skills}. Write a 40-word HR fitment note in form strong point: , major skill gap(dont include languages in skill gap): , suitable for which role:"
        )
        return response.text.strip()
    except Exception as e:
        return f"Error :{e}"
    
