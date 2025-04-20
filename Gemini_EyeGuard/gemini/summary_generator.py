import google.generativeai as genai
from app.gemini_principal.knowledge.dr_stage_info import stage_info

# Configura la API key (puedes mejorar esto con un .env)
# genai.configure(api_key="AIzaSyB2PBS31t2Hc7n4ppVkzmC_KvX9G5kTbjE")

from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

def generate_short_summary(stage, confidence):
    context = stage_info.get(stage)
    if context is None:
        return "Invalid stage", 0

    prompt = f"""
You are a medical assistant helping a diabetic patient understand their diagnosis.

The patient has been diagnosed with Diabetic Retinopathy Level {stage}, and the model confidence is {confidence*100:.1f}%.
Based on the following clinical explanation, give a short, essential summary in simple language. Avoid technical jargon.

Clinical reference:
{context}
"""

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text, len(response.text.split())

def generate_detailed_summary(stage, confidence):
    context = stage_info.get(stage)
    if context is None:
        return "Invalid stage", 0

    prompt = f"""
You are a medical assistant helping a diabetic patient understand their diagnosis.

The patient has been diagnosed with Diabetic Retinopathy Level {stage}, and the model confidence is {confidence*100:.1f}%.
Based on the following clinical explanation, provide a detailed summary in clear, reassuring language. Include what this stage means, potential risks, and what actions to take.

Clinical reference:
{context}
"""

    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text, len(response.text.split())
