#######################################################################
# Desctiption: An improved version that gives hints based on word bank
# Name: Mehdi Hachimi
# Date Created: 12/06/2015
# Date Modified: 25/04/2019
#######################################################################



from hangman_hard import *


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3

    print('Welcome to the game Hangman!') 
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('-------------')
    lettersGuessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    while guesses > 0:

        if warnings == 0:
            print('Sorry sir you have exhausted your warnings, GAME OVER.')
            exit()

        print('You have ' + str(warnings) + ' warnings left.')
        print('You have ' + str(guesses) + ' guesses left.')

        remainings = get_available_letters(lettersGuessed)


        print('Available letters: ' + remainings)
        letter = input('Please guess a letter: ').lower()
        if letter == "*":
            show_possible_matches(get_guessed_word(secret_word, lettersGuessed))
            continue
        lettersGuessed.append(letter)

        if lettersGuessed[lettersGuessed.index(letter)] in string.ascii_lowercase:
            if lettersGuessed[lettersGuessed.index(letter)] in remainings:
                if was_letter_guessed(secret_word, lettersGuessed):
                    print('Good guess: ' + get_guessed_word(secret_word, lettersGuessed))
                else:
                    print('Oops! that letter is not in my word: ' + get_guessed_word(secret_word, lettersGuessed))
                    if lettersGuessed[lettersGuessed.index(letter)] in vowels:
                        guesses -= 2
                        print('-------------')
                        continue
                    guesses -= 1

                print('-------------')

            else:
                warnings -= 1
                print('Oops! you already guessed this letter. You have now ' + str(warnings) + ' warnings left:' + get_guessed_word(secret_word, lettersGuessed))
                print('-------------')
                continue
        else:
            warnings -= 1
            print('Oops! That is not a valid letter. You have now ' + str(warnings) + ' warnings left:' + get_guessed_word(secret_word, lettersGuessed))
            print('-------------')
            continue

        if is_word_guessed(secret_word, lettersGuessed):
            print('Congratulations, you won!')
            print('Your total score for this game is : ' + str(guesses * len(secret_word)))
            exit()

    print('Sorry you ran out of guesses. The word was ' + secret_word)




if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)