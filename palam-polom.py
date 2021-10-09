import random
choices = ["🤚", "✋"]
computer1_score = 0
computer2_score = 0
user_score = 0
for n in range(0, 5):
    computer1_choice = random.choice(choices)
    computer2_choice = random.choice(choices)
    user_choice = input("What do you want? 🤚 or ✋ ")
    print(f"The computer1 choice is: {computer1_choice}")
    print(f"The computer2 choice is: {computer2_choice}")
    if computer1_choice == computer2_choice and computer1_choice != user_choice:
        user_score += 1
    elif computer1_choice == user_choice and computer1_choice != computer2_choice:
        computer2_score += 1
    elif computer2_choice == user_choice and computer1_choice != computer2_choice:
        computer1_score += 1

print(f"The computer1 final scores is: {computer1_score} and the computer2 final score is: {computer2_score} and the user final score is {user_score}.")
if computer1_score > user_score and computer1_score > computer2_score:
    print("the final result: Computer1 is winner. ")
elif computer2_score > user_score and computer2_score > computer1_score:
    print("the final result: Computer2 is winner. ")
elif user_score > computer1_score and user_score > computer2_score:
    print("The user is winner.")
else:
    print("Nobody is winner.")