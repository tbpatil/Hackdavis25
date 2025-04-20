import google.generativeai as genai
import sys, os
from dotenv import load_dotenv

# Add parent directory to path for relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from knowledge.dr_stage_info import stage_info

# Load Gemini API key from .env
# load_dotenv()
# Reload env with override in case old values are cached
load_dotenv(override=True)
API_KEY = os.getenv("GEMINI_API_KEY")
print("LOADED API KEY:", API_KEY)
genai.configure(api_key=API_KEY)


def generate_short_summary(stage, confidence, user_info=None):
    context = stage_info.get(stage)
    if context is None:
        return "Invalid stage", 0
    
        # Optional: enrich prompt with user information
    user_name = user_info.get("name","The Patient")
    years = user_info.get("years_with_diabetes", "N/A") if user_info else "N/A"
    treatments = ", ".join(user_info.get("treatments", [])) if user_info and user_info.get("treatments") else "unspecified treatment"
    symptoms = ", ".join(user_info.get("symptoms", [])) if user_info and user_info.get("symptoms") else "no specific symptoms reported"


    prompt = f"""
You are a medical assistant helping a diabetic patient named {user_name}.User their {user_name} when referring to them. 

The patient has been diagnosed with Diabetic Retinopathy Level {stage}, and the model confidence is {confidence*100:.1f}%.
Based on the following clinical explanation, give a short, essential summary in simple language. Avoid technical jargon.

Clinical reference:
{context}
"""

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text, len(response.text.split())

def generate_detailed_summary(stage, confidence, user_info=None):
    context = stage_info.get(stage)
    if context is None:
        return "Invalid stage", 0

    # Optional: enrich prompt with user information
    user_name = user_info.get("name", "The Patient")
    years = user_info.get("years_with_diabetes", "N/A") if user_info else "N/A"
    treatments = ", ".join(user_info.get("treatments", [])) if user_info and user_info.get("treatments") else "unspecified treatment"
    symptoms = ", ".join(user_info.get("symptoms", [])) if user_info and user_info.get("symptoms") else "no specific symptoms reported"

    prompt = f"""
You are a medical assistant helping {user_name}. User their {user_name} when referring to them. 

They have been diagnosed with Diabetic Retinopathy Level {stage}, and the model confidence is {confidence*100:.1f}%.
They have had diabetes for {years} years and are currently being treated with {treatments}.
They reported the following vision symptoms: {symptoms}.

Based on the following clinical explanation, provide a detailed summary in clear, reassuring language.
Include what this stage means, potential risks, and what actions to take.

Clinical reference:
{context}
"""

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text, len(response.text.split())
