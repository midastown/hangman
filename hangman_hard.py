#####################################################################
# Desctiption: Hangman game mechanics
# Name: Mehdi Hachimi
# Date Created: 01/06/2015
# Date Modified: 25/04/2019
#####################################################################


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def was_letter_guessed(secret_word, letters_guessed):
    i = len(letters_guessed)
    if letters_guessed[i - 1] in secret_word:
        return True
    else:
        return False


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are lowercase

    letters_guessed: list (of letters), which letters have been guessed so far, assumes that all letters are lowercase

    returns: boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    '''

    new_list = []
    for i in secret_word:
        if i not in new_list:
            new_list.append(i)

    counter = 0
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in new_list:
            counter += 1

    if counter == len(new_list):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, that represents which letters in secret_word have been guessed so far.
    '''
    guess = []
    secretword_inList = []
    for i in secret_word:
        guess.append('_ ')
        secretword_inList.append(i)

    for i in letters_guessed:
        if i in secretword_inList:
            while secretword_inList.count(i) >= 1:
                guess[secretword_inList.index(i)] = i
                secretword_inList[secretword_inList.index(i)] = '_ '

    return ''.join(guess)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far

    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    '''

    alphabet = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in alphabet:
            alphabet.remove(i)

    return ''.join(alphabet)

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''
    guesses = 6
    warnings = 3
    print('first word: ' + wordlist[0])
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



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word

    returns: boolean, True if all the actual letters of my_word match the corresponding letters of other_word, False otherwise
    '''

    goodWord = my_word.replace(' ', '')
    counter = 0
    underscore = '_'
    adders_list = []

    if len(other_word) == len(goodWord):
        goodList = list(goodWord)
        otherList = list(other_word)

        for i in range(len(goodList)):

            if goodList[i] == otherList[i]:
                if otherList[i] not in adders_list:
                    adders_list.append(otherList[i])
                counter += 1
                continue

            elif goodList[i] == underscore and otherList[i] not in adders_list:
                counter += 1
                continue

            else:
                return False

    if counter == len(goodWord):
        return True

    return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    '''

    list_of_matches = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            list_of_matches.append(i)
    if len(list_of_matches) == 0:
        return 'No match found'
    else:
        print(*list_of_matches, sep=", ")
        print('---------------')






if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)