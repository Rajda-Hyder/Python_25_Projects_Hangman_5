#imports
import random
from words import words 
import string

#function for get valid word
def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word :
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6 # number of lives

    #getting user input
    while len(word_letters) > 0 and lives > 0:

       #  Display guessed letters
        print(f"\nYou have {lives} lives left. Used letters: {' '.join(used_letters)}")

        #letters used
        #' ' .join(['a','b','cd']) ---> 'a b cd' 
        print('You have used these Letters: ', ' '.join(used_letters))

        #What current word is (i.e W _ R D)
        word_list = [letter if letter in used_letters else ' _ ' for letter in word]
        print('current word: ',''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #wrong guess, Loose a life
                print('Incorrect guess😞, you Loose a Life ☠')
        elif user_letter in used_letters:
            print('❎ You have already use this letter.Please try again.') 

        else:
            print('Invalid character.Please try again.') 
    #Game over message
    if lives == 0:
        print(f"💀 You lost! The word was {word}")
    else:
        print(f'💥Congratulation,You Guess Complete Word ✨ {word} ✨ correctly.')          

             
hangman()