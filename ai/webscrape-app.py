from bs4 import BeautifulSoup
import requests
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Setup soup with hardcoded link
url = "https://www.genzeon.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

class Website:
    def __init__(self, url, soup):
        self.url = url
        self.title = soup.title.string if soup.title else "No Title"
        
        # Remove irrelevant elements
        for irrelevant in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            irrelevant.decompose()
        
        self.text = soup.get_text(separator='\n', strip=True)

# Create website object
webObject = Website(url, soup)

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt


# Add OpenAI intelligence
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_for(webObject)}
]

response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
print(response.choices[0].message.content)

