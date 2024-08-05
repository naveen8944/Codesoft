import random
def user():
    while True:
        choose = input("Enter any one from(rock/paper/scissors):").lower()
        if choose in ["rock","paper","scissors"]:
            return choose
        else:
            print("Invalid input,Please enter any one from(rock,paper,scissor)again")
def computer():
    return random.choice(["rock","paper","scissors"])
def winner(get_user,get_computer):
    if get_user==get_computer:
        return "It's a tie"
    elif ((get_user=="rock" and get_computer=="scissors")or (get_user=="scissors" and get_computer=="paper")or(get_user=="paper" and get_computer=="rock")):
          return "You won!"
    else:
        return "computer won!"
def play_game():
    user_score=0
    computer_score=0
    while True:
        print("\n--New Game--")
        get_user=user()
        get_computer=computer()
        print(f"\n Your choice:{get_user}")
        print(f"computer's choosen:{get_computer}")
        score=winner(get_user,get_computer)
        print(score)
        if "You won!" in score:
            user_score += 1
        elif "computer won!" in score:
            computer_score += 1
        print(f"\n Score-You:{user_score},computer:{computer_score}")
        play_again = input("\n Play again?(Yes or No):").lower()
        if play_again !="yes":
            break
    print("Thanks for playing! ")
    print(f"Total Score- You:{user_score},computer:{computer_score}")
print("Rock-Paper-Scissors Game!")
play_game()