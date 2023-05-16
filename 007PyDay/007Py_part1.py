import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

def clear_console():
    command = 'clear' # For Linux, Mac
    if os.name in ('nt', 'dos'):
        command = 'cls' # For Windows
    os.system(command)

# Pick a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# Create blanks for the guessing word
display = ["_" for _ in chosen_word]

while not end_of_game:
    # Begin game
    guess = input("Guess a letter: ").lower()
    # Clear console
    # clear_console()
    print('\033c', end='')
    # Check if guess is not a repeated answer
    if not guess in display:
      #Check if guessed letter is in word
      for idx in range(word_length):
          letter = chosen_word[idx]
          if letter == guess:
              display[idx] = letter
              print(f"You guessed it right!")
  
      #Check if guessed letter is wrong
      if guess not in chosen_word:
          print(f"Sorry, '{guess}' is not in the word.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print(f"The word was {chosen_word}...")
              print("GAME OVER")
    else:
      print(f"You guessed '{guess}' already. Try again")
      
    # Print current display
    print(f"{' '.join(display)}")

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print hangman stages
    print(stages[lives])
