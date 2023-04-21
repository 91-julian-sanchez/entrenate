import os
from dotenv import load_dotenv
import openai
from interface import run as interface_run
 
load_dotenv()  # take environment variables from .env.
lang='Spanish'
role_assistant='Tech Recruiter'
user_assistant='Developer'
level='junior'
choices_dict = {
    'yes_no': 'Preguntas cerradas de "sí o no" ✅',
    'multiple_choice': 'Preguntas de opción múltiple con única respuesta 🔘',
    'short_answer': 'Preguntas abiertas de respuesta corta ✏️'
}

def context():
    return f"You are an {role_assistant} assistant. You use a tone that is technical. The questions and answers generated should be easy to understand for a {level} {user_assistant}. gives the answers in {lang}."

def assistant_chatbot(selected_values):
    print(f"Can you ask me 4 questions about programming basics?. use: {','.join(selected_values)}")
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": context()},
            # {"role": "user", "content": "Hello, who are you?"},
            # {"role": "assistant", "content": f"Greeting! I am an {role_assistant} assistant. How can I help you today?"},
            {"role": "user", "content": f"Can you ask me 4 questions about programming basics?. use {' y '.join(selected_values)}"}
        ]
    )
    print(response)

if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")
    questions_kind = interface_run()
    # print(questions_kind)

    selected_values = []

    for option in questions_kind:
        selected_values.append(choices_dict[option])

    # print(selected_values)

    if os.getenv('ASSISTANT_ENABLED')== 'True':
     assistant_chatbot(selected_values)