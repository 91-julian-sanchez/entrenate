from inquirer import prompt, Checkbox
from rich.console import Console

console = Console()
console.print("[italic] ¡Hola! Gracias por venir a esta entrevista. [/italic]😊\n ")
choices_dict = {
    'yes_no': 'Preguntas cerradas de "sí o no" ✅',
    'multiple_choice': 'Preguntas de opción múltiple con única respuesta 🔘',
    'short_answer': 'Preguntas abiertas de respuesta corta ✏️'
}

def select_questions():
    questions = [
        Checkbox('preguntas',
                message='Selecciona el tipo de preguntas que prefieres responder',
                choices= [(v, k) for k, v in choices_dict.items()])
    ]
    answers = prompt(questions)
    if not answers['preguntas']:
        return False
    return answers['preguntas']

def run():
    while True:
        selected_options = select_questions()
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

if __name__ == '__main__':
    print(run())