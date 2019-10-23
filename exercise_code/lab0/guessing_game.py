from random import randint


def guess(attempts, numrange):
    number = randint(1, numrange)
    if attempts > 0:
        print("Welcome! Can you guess my secret number?")
        print('You have %s guesses remaining' % attempts)
        number_input = int(input('Make a guess: '))
        if number_input > number:
            attempts -= 1
            print("No - too high!")
            guess(attempts, numrange)
        elif number_input < number:
            attempts -= 1
            print('No - too low!')
            guess(attempts, numrange)
        else:
            print('Well done! You got it right.')
            print("END-OF-GAME: thanks for playing!")
    else:
        print('No more guesses - bad luck!')
        print("END-OF-GAME: thanks for playing!")


guess(3, 10)
