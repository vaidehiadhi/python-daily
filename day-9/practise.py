# KBC Game in Python

# List of questions
questions = [
    "What is the capital of India?",
    "Who is known as the Father of the Nation in India?",
    "Which planet is known as the Red Planet?",
    "Who wrote the National Anthem of India?"
]

# List of options for each question
options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Sardar Patel", "D. B. R. Ambedkar"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhas Chandra Bose"]
]

# List of correct answers (corresponding to options)
answers = ["B", "A", "B", "A"]

# Prize money for each question
prizes = [1000, 2000, 5000, 10000]

# Game logic
print("🎉 Welcome to Kaun Banega Crorepati 🎉")
total_winnings = 0

for i in range(len(questions)):
    print(f"\nQuestion {i+1} for ₹{prizes[i]}:")
    print(questions[i])
    
    # Display options
    for opt in options[i]:
        print(opt)
    
    # Get user input
    user_ans = input("Enter your answer (A/B/C/D): ").upper()
    
    # Check answer
    if user_ans == answers[i]:
        print("✅ Correct Answer!")
        total_winnings = prizes[i]
    else:
        print("❌ Wrong Answer!")
        print(f"The correct answer was: {answers[i]}")
        break

print(f"\n🎊 You won a total of ₹{total_winnings}! 🎊")
