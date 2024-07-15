import google.generativeai as genai
import os
from dotenv import load_dotenv

dotenv_path = 'G:/geminiLearn/geminiLearn/API_KEY_GEMINI/.env'

# Load environment variables from the specified .env file
load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY_GEMINI')

if API_KEY is None:
    print("No API_KEY Found!")
    exit()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

# ANSI escape code for blue text and bold text
BLUE = '\033[34m'  # Blue text
BOLD = '\033[1m'   # Bold text
RESET = '\033[0m'  # Reset to default color and style

while True:
    # Display prompt in blue and bold
    prompt = input(f"{BLUE}{BOLD}Ask me anything (or type 'exit' to quit): {RESET}")
    
    if prompt.lower() == 'exit':
        print("Goodbye!")
        break

    response = model.generate_content(prompt)
    print(response.text)
