import random
import string
from hangman.words import words



print("HANGMAN")

def valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=valid_word(words)
    word_letters=set(word) #letter in word
    alphabet =set(string.ascii_uppercase)
    used_letters=set() #what the user has guessed

    lives=7

    while len(word_letters) > 0 and lives>0:
        print(f"you have {lives} lives left and you have already used the letters:"," ".join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('Current word:',' '.join(word_list))

        user_letter = input("GUess the letter:").upper()
        if user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            
            else:
                lives=lives-1
                print(f"\n Your letter {user_letter} not in the word")
        
        elif user_letter in used_letters:
            print("YOu have already guesses that letter ,guess again")
        
        else:
            print("Enter a valid letter")
    
    if lives==0:
        print(f"lives finish ,you died. The word was {word}")
    else:
        print("You guesses correctly")


hangman()