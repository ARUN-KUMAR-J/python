import random
import string
from words import words
def get_valid_word(words):
    word=random.choice(words)
    while ' ' in word or '-' in word:
        word=random.choice(words)
    return word.upper()
def hangman():
   
    word=get_valid_word(words)
    wordlist=set(word) #letters in word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #letters guessed by user
    lives=len(word)
    while len(wordlist)>0 and lives>0:
        print("lives remaining:",lives)
        
        print("used letters", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word] 
        print("current word  ", ' '.join(word_list))
    
        
         #user input
        user_letter=input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in wordlist:
                wordlist.remove(user_letter)
            else:
                lives=lives-1
                print("Letter not in the word")
        elif user_letter in used_letters:
            print("Sorry You have already used that letter ,Try again!")
        else:
            print("Invalid character, Try again")
    if lives==0:
        print("you died")
    else:
        print("You guessed the word ",word)
    
hangman()
