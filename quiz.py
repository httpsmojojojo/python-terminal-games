questions = ["What is the capital of Japan?",
             "Which planet is known as the Red Planet?",
             "Who wrote the play Romeo and Juliet?",
             "What is the largest ocean on Earth?"]

answers = ["tokyo",
           "mars",
           "shakespeare",
           "pacific"]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Answer: ").strip().lower()

    if user_answer == answers[i]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        print(f"The correct answer is: {answers[i]}")

print(f"Score: {score}/{len(questions)}")
