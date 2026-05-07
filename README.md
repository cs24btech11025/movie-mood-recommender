# movie-mood-recommender
A Python script that recommends movies based on your mood using Google Gemini AI. Type how you're feeling and it suggests 3 movies with reasons why they fit
----
##what it does:
you describe your mood in plain english and it recommends 3 movies which fits that criteria and gives reason why it picked each of them
----
##how it works:
```
You type your mood
        ↓
Python sends it to Gemini AI
        ↓
Gemini recommends 3 movies with reasons
        ↓
Printed cleanly in the terminal
```
---
## Tools used 
- Python
- Google Gemini API — AI movie recommendations
- Requests — sending API calls
- python-dotenv — keeping API key safe
---
##How to run it:
**clone the repo**
'''
git clone https://github.com/cs24btech11025/movie-mood-recommender
cd movie-mood-recommender
'''
**install dependencies**
'''
pip install requests python-dotenv
'''
**get free google api key**
Go to [aistudio.google.com](https://aistudio.google.com)
->get api key
->copy it
**create a new .env file**
write
'''
GEMINI_API_KEY="your-api-key"
'''
**run it!**
'''
python movie_recommender.py
'''
## What I learned
- Calling an AI API (Gemini) from Python
- Parsing nested JSON responses
- Storing secrets safely with `.env`
- Debugging API errors (400, 404, 429)
---
