import random

def play():
    user_choice = input("Enter your choice 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer_choice = random.choice(['r','s','p'])

    if user_choice == computer_choice:
        return  'It\'s a tie'
    

    if winner(user_choice, computer_choice):
        return 'You win'
    
    return 'You lost!'
    
def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    

print(play())


