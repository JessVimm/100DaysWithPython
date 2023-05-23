from header import header
import random 
EASY_MODE = 10
HARD_MODE = 5

def guess_game(guesses):
  number = random.randint(1, 100)
  
  while guesses > 0:
    print(f"{guesses} attempts left")
    guess = int(input("Make a guess -> "))
    if guess == number:
      print(f"That's right! {number} was the number.")
      guesses = 0
    else:
      if guess > number:
        print("Too high!")
      elif guess < number:
        print("Too low!")
      guesses -= 1
      if guesses == 0:
        print(f"Sorry. You've run out of guesses. The number was {number}.")

print(header)
print("Guess the number between 1 and 100!\n")
game_mode = input("Do you want an 'easy' or 'hard' game? -> ")

if game_mode == 'easy':
  guess_game(EASY_MODE)
elif game_mode == 'hard':
  guess_game(HARD_MODE)
else:
  print("Something wrong happened. Try again.")