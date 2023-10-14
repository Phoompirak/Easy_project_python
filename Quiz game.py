#Python game

questions = ("What's your name: ", "How are you: ","How much: ","Are you gay?: ", "You stubid?: ")

options = (
    ("A. I'm gay","B. I'm stubid","C.I'm No idea","D. My name's ..."),
    ("A. I'm 15 years old","B. I'm so hot","C. I'm very wel","D. You stubid"),
    ("A. 13 Bath","B. I'm 15 years old","C.14th December 2007","D. No, I'm gay"),
    ("A. Yes, I'm gay","B. No, I'm man","C. Same old same old","D. Fuck.."),
    ("A. Yes, you'r stubid","B. No, I'm stubid","C. No, I'm Genius","D. Mai ru")
)

answers = ("D","A","A","B","C")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("(^○^) -----CORRECT!----- (^○^)")
    else:
        print("ヽ(*^^*) INCORRECT! ヽ(*^^*)")
        print(f"{answers[question_number]} is the correct answer")
    question_number+=1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

#คำตอบที่ถูก VS การเดาของคุณ
print("answer:", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}% in {len(questions)}")