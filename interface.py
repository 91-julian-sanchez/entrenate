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

def prompt_short_answer() -> str:
    while True:
        try:
            questions = [
                inquirer.Text('short_answer', message="Tu respuesta es"),
            ]
            answers = inquirer.prompt(questions)
            short_answer = answers['short_answer'].strip()  # elimina espacios en blanco al principio y al final
            if len(short_answer) == 0:
                raise ValueError("La respuesta no puede estar vacía.")
            elif len(short_answer) > 280:
                raise ValueError("La respuesta es demasiado larga (máximo 100 caracteres).")
            return short_answer
        except (KeyError, ValueError) as e:
            console.print(f"❌ [bold red]Error: {e} Por favor, inténtelo de nuevo.[/bold red]\n ")

def prompt_closed_question(choices: any) -> str:
    try:
        questions = [
            inquirer.List('answer',
                           message="Tu respuesta es",
                           choices=choices),
        ]
        answers = inquirer.prompt(questions)
        return answers['answer']
    except KeyError:
        console.print(f"❌ [bold red]Error: seleccione una opción válida ({', '.join(choices)}).[/bold red]\n ")
        return prompt_closed_question(choices)

if __name__ == '__main__':
    print(interfaz_select_question_types())
    print(prompt_short_answer())
    print(prompt_closed_question(choices=['Si', 'No']))
    print(prompt_closed_question(choices=['A', 'B', 'C', 'D']))