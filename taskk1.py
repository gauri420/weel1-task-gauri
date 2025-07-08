def check_answer(user_input, correct_answer):
    """Check if the user's answer is correct."""
    return user_input.strip().upper() == correct_answer.upper()

def run_quiz():
    questions = [
        ("Which is the largest animal on Earth?", "A"),
        ("Which planet is closest to the Sun?", "C"),
        ("What is the national flower of India?", "B"),
        ("Who is known as the father of computers?", "D"),
        ("How many continents are there in the world?", "A"),
    ]

    options = [
        ["A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Shark"],
        ["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
        ["A. Rose", "B. Lotus", "C. Marigold", "D. Lily"],
        ["A. Isaac Newton", "B. Albert Einstein", "C. Nikola Tesla", "D. Charles Babbage"],
        ["A. 7", "B. 5", "C. 6", "D. 8"]
    ]

    score = 0

    for index, (question, correct_answer) in enumerate(questions):
        print(f"\nQ{index+1}: {question}")
        for opt in options[index]:
            print(opt)

        while True:
            user_input = input("Enter your answer (A/B/C/D): ").strip().upper()
            if user_input in ['A', 'B', 'C', 'D']:
                break
            else:
                print("⚠️ Invalid input! Please enter A, B, C, or D.")

        if check_answer(user_input, correct_answer):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}.")

    print("\n🎯 Quiz Complete!")
    print(f"Your final score: {score} out of {len(questions)}")

    if score == 5:
        print("🏆 Excellent! You're a genius!")
    elif score >= 3:
        print("👍 Good job! Keep learning.")
    else:
        print("📚 Needs improvement. Try again!")

if __name__ == "__main__":
    run_quiz()
