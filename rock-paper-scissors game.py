import random
rock = "✊"
paper = "✋"
scissors = "✌"
computer_score = 0
user_score = 0
for n in range(0, 5):
    choice= int(input("what do you want? 0 for rock, 1 for paper or 2 for scissors? "))
    random_int= random.randint(0,2)
    if choice==0:
        print(rock)
        print("Computer Choice: ")
        if random_int==0:
            print(rock)
            print("You draw!")
        elif random_int==1:
            print(paper)
            print("You lose!")
            computer_score += 1
        elif random_int==2:
            print(scissors)
            print("You win!")
            user_score += 1
    elif choice==1:
        print(paper)
        print("Computer Choice: ")
        if random_int==0:
            print(rock)
            print("You win!")
            user_score += 1
        elif random_int==1:
            print(paper)
            print("You darw!")
        elif random_int==2:
            print(scissors)
            print("You lose!")
            computer_score += 1
    elif choice==2:
        print(scissors)
        print("Computer Choice: ")
        if random_int==0:
            print(rock)
            print("You lose!")
            computer_score += 1
        elif random_int==1:
            print(paper)
            print("You win!")
            user_score += 1
        elif random_int==2:
            print(scissors)
            print("You draw!")
print(f"The computer final scores is :{computer_score} and the user final score is {user_score}.")
if computer_score > user_score:
    print("the final result: The Computer win. ")
elif computer_score < user_score:
    print("the final result: The User win. ")
else:
    print("Ther is no winner and result is draw.")