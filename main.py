import os
from dotenv import load_dotenv
import openai
 
load_dotenv()  # take environment variables from .env.
lang='Spanish'
role_assistant='Tech Recruiter'
user_assistant='Developer'
level='junior'

def context():
    return f"You are an {role_assistant} assistant. You use a tone that is technical. The questions and answers generated should be easy to understand for a {level} {user_assistant}. gives the answers in {lang}."

def assistant_chatbot():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": context()},
            {"role": "user", "content": "Hello, who are you?"},
            {"role": "assistant", "content": f"Greeting! I am an {role_assistant} assistant. How can I help you today?"},
            {"role": "user", "content": "Can you ask me 4 questions about programming basics?"}
        ]
    )
    print(response)


if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")
    assistant_chatbot()