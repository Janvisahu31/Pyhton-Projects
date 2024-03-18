import random
from hangman.words import words



print("Beginner Projects")
print("1.Madlibs")
print("2.Guess the number Computer")
print("3..Guess the number USER")
print("4.Rock paper Scissors")




#string concatenation
#this method simply concatinate the string
#print("Subscribe to "+youtuber)
#this method will add youtuber to {} present there
#print("subscribe to{}".format(youtuber))
#this methos uses f string, we can directly use f string by writing f before the string
#print(f"subscribe to {youtuber}")

print("madlibs")
adj=input("Adjective:")
verb1=input("verb1:")
verb2=input("verb2:")
famous_person=input("famous person:")
madlib= f"computer programming is soo {adj}! It makes me so exited all the \
time because i love to {verb1} . Stay hydrated and {verb2} like you are {famous_person}"
print(madlib)



print("Guess the number(Computer)")

def guessthenum(a):
    if(a==number):
        print("Congratuations you guessed correct")
    else:
        if(a>number):
            print("guess to high")
            b=int(input("Guess your number between 1 to 10:"))
            guessthenum(b)
        else:
            print("guess to low")
            b=int(input("Guess your number between 1 to 10:"))
            guessthenum(b)

number=random.randint(1,10)
a=int(input("Guess your number between 1 to 10:"))
guessthenum(a)


print("Guess the number user")
def comp_guess(x):
    low=1
    high=x
    feedback=""
    while feedback !='c' and low !=high:
        guess=random.randint(low,high)
        feedback=input(f"is the {guess} too high(h),too low(l),or correct(c)").lower()
        if(feedback=='h'):
            high=guess-1
        elif(feedback=='l'):
            low=guess+1
    print("yay the computer guessed correctly")

#rock->scissors
#scissors->paper
#paper->rock

print("ROCK PAPERS SCISSORS")
def RPS():
    uscores=0
    cscores=0
    while(uscores!=5 or cscores!=5):
        user=int(input("Enter your choice:(1,2,3)"))
        print(user)
        comp=random.randint(1,3)
        print(comp)
        if((comp==1 and user==2) or (comp==2 and user==3) or (comp==3 and user==1)):
           cscores=cscores+1
        elif((comp==2 and user==1) or (comp==3 and user==2) or (comp==1 and user==3)):
            uscores=uscores+1
        else:
            print("it was a tie ,play again")
    
    if(uscores==5):
        print("User Won")
    else:
        print("Computer won")



print("1.Rock")
print("2.Scissors")
print("3.Papers")
RPS()



print("HANGMAN")

def valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word

def hangman():
    word=valid_word(words)
    word_letters=set(word) #letter in word
    alphabet =set(string.ascii_uppercase)
    used_letters=set() #what the user has guessed

    lives=7

    while len(word_letters>0) and lives>0:
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



