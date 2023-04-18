import os
from dotenv import load_dotenv
import openai
 
load_dotenv()  # take environment variables from .env.
lang='Spanish'
rol='Tech Recruiter'
def assistant_chatbot():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": f"You are an {rol} assistant. You use a tone that is technical. gives the answers in {lang}."},
            {"role": "user", "content": "Hello, who are you?"},
            {"role": "assistant", "content": f"Greeting! I am an {rol} assistant. How can I help you today?"},
            {"role": "user", "content": "Can you ask me 4 questions about programming basics?"}
        ]
    )
    print(response)


if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")
    assistant_chatbot()