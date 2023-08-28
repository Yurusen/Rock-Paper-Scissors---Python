import random  # Import the random answer for generating computer choices

# Function to gets user's choice
def get_user_choice():
    user_input = input("Enter your choice (rock/paper/scissors/bomb): ").lower()
    if user_input in ['rock', 'paper', 'scissors', 'bomb']:
        return user_input
    else:
        print('Error!')

# Function to gets computer's choice
def get_computer_choice():
    random_number = random.randint(0, 2)  # Generate a random number (0 to 2)
    if random_number == 0:
        return 'rock'
    elif random_number == 1:
        return 'paper'
    else:
        return 'scissors'

# Function to determine the winner!
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'You have tied!'
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return 'Computer has won!'
        else:
            return 'You won!'
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return 'Computer has won!'
        else:
            return 'You won!'
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return 'Computer has won!'
        else:
            return 'You won!'
    elif user_choice == 'bomb':
        return 'You won with the MASTER WORD'

# Function to play the game
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print('You threw ' + user_choice)
    print('The computer threw ' + computer_choice)
    print(determine_winner(user_choice, computer_choice))

# Main function to start the game
def main():
    play_game()

# Checks if the script is being run directly
if __name__ == "__main__":
    main()
