#imports#
from B_Functions import *

#greeting#
greet_user()
rangee = rangee()
# print(rangee)

#difficulty#
difficulty = choose_difficulty()

#starting num of attempts based on difficulty level#
attempts_left = determine_num_attempts(difficulty)
display_num_attempts_left(attempts_left)

#info#
the_number = randint(1, rangee)
# print(f"the number is {the_number}")

#condition block#
loop_parameter = 'not yet'
while loop_parameter == 'not yet':
    #guess#
    guess = input("Make a guess: ")

    loop_parameter = logic_guess(guess, the_number, rangee)
    attempts_left -= 1
    if loop_parameter == 'not yet':
        print(f"You have {attempts_left} attempts remaining to guess the number")
    if attempts_left == 0 and loop_parameter != 'win':
        loop_parameter = 'lose'
        print(f"You have lost. The number was {the_number}")
    

