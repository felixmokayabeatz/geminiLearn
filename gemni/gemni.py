import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

if API_KEY is None:
    print("No API_KEY Found!")
    
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Hell who are you, and what is 1 +1")

print(response.text)