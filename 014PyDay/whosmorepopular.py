from game_data import data
import random

def check_answer(given_answer, popular_adversary):
  '''Check if adversary chosen is the right answer'''
  if given_answer == popular_adversary:
    return True
  else:
    return False

def get_format_output(adversary):
  '''Return output string with the adversary information '''
  name = adversary["name"]
  description = adversary["description"]
  country = adversary["country"]

  return f"{description} {name} from {country}"

def get_choosen_adversary(adversary_a, adversary_b, answer):
  '''Return name of the adversary chosen'''
  if answer == 'A':
     return adversary_a["name"]
  elif answer == 'B':
      return adversary_b["name"]
  else:
      return "Invalid input. Try again."

def get_popular_adversary(adversary_a, adversary_b):
  '''Return name of the adversary with most followers'''
  if adversary_a["follower_count"] > adversary_b["follower_count"]:
    return adversary_a["name"]
  else:
    return adversary_b["name"]

def check_repeated_adversaries(adversary_a_name, adversary_b_name):
  '''Return True if A and B are the same'''
  if adversary_a_name == adversary_b_name:
    print("Spotted same adversaries!")
    return True
  else:
    return False

def choose_adversary():
  '''Pick a random item from list'''
  return random.choice(data)

def start_game():
  # Game flag
  continue_game = True

  # Points
  points = 0

  # Pick random adversaries
  adversary_a = choose_adversary()

  # Print header
  print("----------------------WELCOME----------------------------")

  while continue_game:
    
    adversary_b = choose_adversary()
    
    while check_repeated_adversaries(adversary_a["name"], adversary_b["name"]):
      adversary_b = choose_adversary()
      
    print(f"Adversary A: {get_format_output(adversary_a)}")
    print("\tvs")
    print(f"Adversary B: {get_format_output(adversary_b)}")
    print("\t.\n"*3)
    choice_made = input("Between A and B who is more popular? 'A' or 'B' -> ")
    
    popular_adversary = get_popular_adversary(adversary_a, adversary_b)
    chosen_adversary = get_choosen_adversary(adversary_a, adversary_b, choice_made)
    print('\033c', end='')
    
    if check_answer(chosen_adversary, popular_adversary):
      points += 1
      print(f"That's right! Current score is {points} points.\n")
      adversary_a = adversary_b
    else:
      print(f"Sorry. Final score: {points} points.")
      continue_game = False

# Start the game
start_game()