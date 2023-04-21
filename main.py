import os
from dotenv import load_dotenv
import openai
from interface import run as interface_run
 
load_dotenv()  # take environment variables from .env.
lang='Spanish'
assistant_role='Tech Recruiter'
user_role='Developer'
user_level='junior'
types_questions_dict = {
    'yes_no': ('Preguntas cerradas de "sí o no" ✅', '"yes or no" option'),
    'multiple_choice': ('Preguntas de opción múltiple con única respuesta 🔘', 'multiple choice question with only one answer'),
    'short_answer': ('Preguntas abiertas de respuesta corta ✏️', 'open-ended and short answer')
}

def system_context():
    return f"You are an {assistant_role} assistant. You use a tone that is technical. The questions and answers generated should be easy to understand for a {user_level} {user_role}. gives the answers only in {lang}."

def user_question(type_question):
    return f"Can you ask me a question about programming basics?. the question must be a {type_question}"

def assistant_chatbot(selected_type_question):
    for type_question in selected_type_question:
        if os.getenv('ASSISTANT_ENABLED') == 'True':
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                        {"role": "system", "content": system_context()},
                        {"role": "user", "content": user_question(type_question[1])}
                    ]
            )
            response_content = response.choices[0].message.content
            print(f"{response_content}\n")

if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")

    selected_values = []

    for option in interface_run():
        selected_values.append(types_questions_dict[option])

    assistant_chatbot(selected_values)