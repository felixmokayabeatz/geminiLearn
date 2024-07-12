import google.generativeai as genai
import os
from dotenv import load_dotenv




dotenv_path = 'G:/geminiLearn/geminiLearn/API_KEY_GEMINI/.env'

# Load environment variables from the specified .env file
load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY_GEMINI')

if API_KEY is None:
    print("No API_KEY Found!")
    
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Hell who are you, and what is 1 +1")

print(response.text)