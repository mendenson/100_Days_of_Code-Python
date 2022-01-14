import random
import hangman_art
import hangman_words

# import the words from hangman_words
from hangman_words import word_list

# import the arts from hangman_art
from hangman_art import logo, stages, victory, death

# randomly choose a word from the word_list and assign it to 
# a variable callen chosen_word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# lives in the game
end_of_game = False
life = 6

print(logo)

# create a empty list called display
display = []
for _ in range(word_length):
    display += "_"
print("\n")
print(display)


while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    # check the guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess is display:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        life -= 1
        print(f"You guessed {guess}, that's not in the world.You lose a life.")
        # death
        if life == 0:
            end_of_game = True
            print(f"The word was {chosen_word}!")
            print("YOU LOSE!")
            print(death)

    # join all the elements in the list and turn it into a String        
    if life > 0 and end_of_game == False:
        print(f"{' '.join(display)}")
        print(stages[life])

    # victory
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")
        print(victory)
    
    