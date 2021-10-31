from random import randint

def determine_num_attempts(difficulty_level):
    """Number of attempts logic, returns the number of attempts available"""
    if difficulty_level == 'easy':
        return 10
    elif difficulty_level == 'hard':
        return 5
    else:
        print(f"I'm sorry, but '{difficulty_level}' is not a valid input.")

def greet_user():
    """Simply prints a greeting for the game"""
    print("Welcome to the Number Guessing Game!")

def rangee():
    """has a local range variable, tells user the range, returns the max num of the range"""
    rangee = 100
    print(f"I'm thinking of a number between 1 and {rangee}.")
    return rangee

def choose_difficulty():
    """Returns a user input of difficulty level"""
    return input("Choose a difficulty. Type 'easy' or 'hard': ")

def display_num_attempts_left(current_num_attempts):
    """displays and returns current number of attempts"""
    print(f"You have {current_num_attempts} attempts remaining to guess the number")
    return current_num_attempts

# def guess():
#     """asks for and returns the user's guess"""
#     return input("Make a guess: ")

def logic_guess(guess, number, rangee):
    """Take the user's guess, the generated number, and the range and prints messages to the user to help them figure it out.
     Returns 'win' or 'not yet'"""
    if int(guess) > rangee:
        print(f"Your guess MUST be a number within the given range")
    if int(guess) > number:
        print("Too high.")
        return 'not yet'
    elif int(guess) < number:
        print("Too low.")
        return 'not yet'
    elif int(guess) == number:
        print(f"Congratulations, the number was {number}! You've won!")
        return 'win'

