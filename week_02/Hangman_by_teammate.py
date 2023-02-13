'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

word = 'java'
tries_n = 6
done = False
guesses = []

while not done:
    print(f'You have {tries_n} tries left.')
    print('Used letters:', end=' ')
    for letter in guesses:
        print(letter, end=' ')
    print('')
    print('Word:', end=' ')
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print('')
    guess = input('Guess a letter: ')
    guesses.append(guess.lower())
    if guess not in word:
        tries_n -= 1
    if tries_n == 0:
        break
    done = True

    for letter in word:
        if letter not in guesses:
            done = False
    print('')


if done:
    print(f'You guessed the word {word} !')
else:
    print(f'You loose, the word was {word} !')
