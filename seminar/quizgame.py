# Trivia Quiz Game

def ask_question(question, options, correct_option):
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = input("\nEnter the number of your answer: ")

    if int(answer) == correct_option:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer was {options[correct_option - 1]}")
        return 0

def trivia_game():
    score = 0
    print("Welcome to the Trivia Quiz Game!")

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "correct_option": 3
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"],
            "correct_option": 1
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": 3
        }
    ]
    
    for q in questions:
        score += ask_question(q["question"], q["options"], q["correct_option"])
    
    print(f"\nYour final score is {score}/{len(questions)}!")
    
if __name__ == "__main__":
    trivia_game()
