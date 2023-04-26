import os
from dotenv import load_dotenv
import openai
from interface import interfaz_select_question_types
from interface import prompt_yes_or_no_answer
from interface import prompt_multiple_choice_answer
from interface import prompt_short_answer
 
load_dotenv()  # take environment variables from .env.
lang='Spanish'
assistant_role='Tech Recruiter'
user_role='Developer'
user_level='junior'
types_questions_dict = {
    'yes_or_no': ('Preguntas cerradas de "sí o no" ✅', '"yes or no" option'),
    'multiple_choice': ('Preguntas de opción múltiple con única respuesta 🔘', 'multiple choice question with only one answer'),
    'short_answer': ('Preguntas abiertas de respuesta corta ✏️', 'open-ended and short answer')
}

def system_context():
    return f"You are an {assistant_role} assistant. You use a tone that is technical. The questions and answers generated should be easy to understand for a {user_level} {user_role}. gives the answers only in {lang}."

def user_question(type_question):
    return f"Can you ask me a question about programming basics?. the question must be a {type_question}"

def __chat_completion_create(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response_content = response.choices[0].message.content
    print(f"{response_content}\n")
    return response_content
    
def assistant_chatbot(selected_type_question):
    context = {"role": "system", "content": system_context()}
    messages = [context]
    for type_question in selected_type_question:
        if os.getenv('ASSISTANT_ENABLED') == 'True':
            messages.append({"role": "user", "content": user_question(type_question[1])})
            response_content = __chat_completion_create(messages)
            messages.append({"role": "assistant", "content": response_content})

            if type_question[1] in '"yes or no" option':
                content = prompt_yes_or_no_answer()
                messages.append({"role": "user", "content": f"la respuesta es {content} ?"})
                __chat_completion_create(messages)
            elif type_question[1] in 'multiple choice question with only one answer':
                content = prompt_multiple_choice_answer()
                messages.append({"role": "user", "content": f"la respuesta es la opción {content} ?"})
                __chat_completion_create(messages)
            else:
                content = prompt_short_answer()
                messages.append({"role": "user", "content": f"la respuesta es: {content} ?"})
                __chat_completion_create(messages)

if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")

    selected_question_types = [types_questions_dict[option] for option in interfaz_select_question_types()]
    assistant_chatbot(selected_question_types)
    