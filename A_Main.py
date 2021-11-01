from B_Functions import *
greet_user()
rangee = rangee()
difficulty = choose_difficulty()
attempts_left = determine_num_attempts(difficulty)
while attempts_left == 0:
    difficulty = choose_difficulty()
    attempts_left = determine_num_attempts(difficulty)
attempts_left = display_num_attempts_left(attempts_left)
the_number = randint(1, rangee)
loop_parameter = 'not yet'
while loop_parameter == 'not yet':
    to_continue = attempts_left
    if to_continue != 0:
        guess = input("Make a guess: ")
        if guess.isdigit() == True:
            loop_parameter = logic_guess(guess, the_number, rangee)
            attempts_left -= 1
            if loop_parameter == 'not yet':
                print(f"You have {attempts_left} attempts remaining to guess the number")
    
            if attempts_left == 0 and loop_parameter != 'win':
                loop_parameter = 'lose'
                print(f"You have lost. The number was {the_number}")
        else:
            print(f"Your guess MUST be a whole number. '{guess}' is not a valid number.")
     

