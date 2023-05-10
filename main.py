import os
from decorators import log_decorator
from dotenv import load_dotenv
import openai
from interface import (
    display_select_question_types,
    display_prompt_closed_question,
    display_prompt_short_answer,
)
 
load_dotenv()  # take environment variables from .env.
lang='Spanish'
structured_output=f"""Provide them in JSON format with the following keys: question, answer_options, if the question is "open-ended", the value of answer_options must be None."""
assistant_role='Tech Recruiter'
user_role='Developer'
user_level='junior'
max_questions = 5
types_questions_dict = {
    'yes_or_no': ('Preguntas cerradas de "sí o no" ✅', '"yes or no" option'),
    'multiple_choice': ('Preguntas de opción múltiple con única respuesta 🔘', 'multiple choice question with only one answer'),
    'short_answer': ('Preguntas abiertas de respuesta corta ✏️', 'open-ended and short answer')
}

@log_decorator
def system_context():
    return f"""You are an {assistant_role} assistant. You use a tone that is technical. The questions and answers generated should be easy to understand for a {user_level} {user_role}. gives the answers only in {lang}."""

@log_decorator
def build_user_question(type_question):
    return f"""Can you ask me a question about programming basics?. the question must be a '{type_question}'. {structured_output}"""

@log_decorator
def __chat_completion_create(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    response_content = response.choices[0].message.content
    return response_content
    
def handle_user_response(type_question, messages):
    if type_question == '"yes or no" option':
        content = display_prompt_closed_question(choices=["Si", "No"])
        messages.append({"role": "user", "content": f"La respuesta es {content}?"})
    elif type_question == 'multiple choice question with only one answer':
        content = display_prompt_closed_question(choices=["A", "B", "C", "D"])
        messages.append({"role": "user", "content": f"La respuesta es la opción {content}?"})
    else:
        content = display_prompt_short_answer()
        messages.append({"role": "user", "content": f"La respuesta es: {content}?"})
    return messages

import random

def assistant_chatbot(selected_type_question):
    context = {"role": "system", "content": system_context()}
    messages = [context]
    question_count = 0
    while question_count < max_questions:
        selected_index = random.randint(0, len(selected_type_question) - 1)
        selected_question = selected_type_question[selected_index]
        if os.getenv('ASSISTANT_ENABLED') == 'True':
            messages.append({"role": "user", "content": build_user_question(selected_question)})
            response_content = __chat_completion_create(messages)
            print(f"{response_content}\n")
            messages.append({"role": "assistant", "content": response_content})
            messages = handle_user_response(selected_question, messages)
            response_content = __chat_completion_create(messages)
            print(f"💻💬 {response_content}\n")
        question_count += 1


if __name__ == '__main__':
    openai.api_key = os.getenv("CHATGPT_API_KEY")
    selected_question_types = [types_questions_dict[option] for option in display_select_question_types()]
    selected_question_types = [question_type for _, question_type in selected_question_types]
    assistant_chatbot(selected_question_types)
    