import os
import requests
import dotenv
dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(mood):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={GEMINI_API_KEY}"
    body = {
        "contents":[{
            "parts":[{"text": f"""You are a movie recommendation engine.
Recommend 3 movies based on this request: {mood}
For each movie give the title, year, and one sentence on why it fits."""}]
        }]
    }
    response = requests.post(url, json=body)
    result=response.json()
    print(result['candidates'][0]['content']['parts'][0]['text'])

if __name__=="__main__":
    mood=input("What kind of movies are you in the mood for? ")
    ask_gemini(mood)
