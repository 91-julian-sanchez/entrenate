import inquirer
from inquirer import prompt, Checkbox
from rich.console import Console

console = Console()
console.print("[italic] ¡Hola! Gracias por venir a esta entrevista. [/italic]😊\n ")
choices_dict = {
    'yes_or_no': 'Preguntas cerradas de "sí o no" ✅',
    'multiple_choice': 'Preguntas de opción múltiple con única respuesta 🔘',
    'short_answer': 'Preguntas abiertas de respuesta corta ✏️'
}

def menu_select_question_types():
    questions = [
        Checkbox('preguntas',
                message='Selecciona el tipo de preguntas que prefieres responder',
                choices= [(v, k) for k, v in choices_dict.items()])
    ]
    answers = prompt(questions)
    if not answers['preguntas']:
        return False
    return answers['preguntas']

def interfaz_select_question_types():
    while True:
        selected_options = menu_select_question_types()
        if not selected_options:
            console.print("❌ [bold red]Error: selecciona una opción válida.[/bold red]\n ")
            continue
        else:
            break

    console.print("[green]👍 Opciones seleccionadas: [/green]")
    for opcion in selected_options:
        console.print(f"  - {choices_dict[opcion]} ")
    console.print("\n")

    return selected_options

def prompt_yes_or_no_answer() -> str:
    questions = [
    inquirer.List('yes_or_no',
                    message="Tu respuesta es",
                    choices=['Si', 'No'],
                ),
    ]
    answers = inquirer.prompt(questions)
    return answers['yes_or_no']

def prompt_multiple_choice_answer() -> str:
    questions = [
    inquirer.List('multiple_choice',
                    message="Tu respuesta es",
                    choices=['A', 'B', 'C', 'D'],
                ),
    ]
    answers = inquirer.prompt(questions)
    return answers['multiple_choice']

def prompt_short_answer() -> str:
    prompt = input()
    return prompt

if __name__ == '__main__':
    print(interfaz_select_question_types())