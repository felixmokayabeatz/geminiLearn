import google.generativeai as genai
import os


# API_KEY = os.environ["API_KEY"]

# genai.configure(api_key=os.environ["API_KEY"])


API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)


print(os.getenv('API_KEY'))

model = genai.GenerativeModel('gemini-pro"')


response = model.generate_content("Write a story about a AI and magic")
print(response.text)