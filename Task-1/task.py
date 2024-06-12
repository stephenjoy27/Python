questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    }
]


def start_quiz():
    score = 0
    for question in questions:
        print(question["question"])
        options = question["options"]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if options[int(user_answer) - 1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answer']}")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
        
        print()  
    
    print(f"Your final score is {score} out of {len(questions)}.")


start_quiz()