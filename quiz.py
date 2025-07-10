def new_func():
    """
crie una lista de questoes com 5 perguntas e 4 alternativas cada.
Cada alternativa deve ser uma string e a resposta correta
cada resposta correrta deve valer 1 ponto.
esse quiz sera de varias capitais do mundo.
"""
# quiz.py

quiz = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Paris", "Londres", "Berlim", "Madri"],
        "answer": "Paris"
    },
    {
        "question": "Qual é a capital do Japão?",
        "options": ["Tóquio", "Pequim", "Seul", "Bangkok"],
        "answer": "Tóquio"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        "answer": "Brasília"
    },
    {
        "question": "Qual é a capital da Itália?",
        "options": ["Roma", "Milão", "Veneza", "Florença"],
        "answer": "Roma"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
        "answer": "Canberra"
    }
]

def show_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}: {option}")

def get_answer(question):
    while True:
        try:
            answer = int(input("Digite o número da sua resposta: "))
            if 1 <= answer <= len(question["options"]):
                return question["options"][answer - 1]
            else:
                print("Resposta inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def main():
    score = 0

    for question in quiz:
        show_question(question)
        user_answer = get_answer(question)
        if check_answer(user_answer, question["answer"]):
            print("Resposta correta!")
            score += 1
        else:
            print(f"Resposta incorreta. A resposta correta é: {question['answer']}")
        print()

    percentual = score / len(quiz)
    if percentual < 0.3:
        print("Você precisa melhorar seu conhecimento sobre capitais.")
    elif percentual < 0.7:
        print("Bom trabalho! Você conhece bem as capitais.")
    else:
        print("Excelente! Você é um expert em capitais do mundo.")

    print(f"Sua pontuação final é: {score}/{len(quiz)}")

if __name__ == "__main__":
    main()