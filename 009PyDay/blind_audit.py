# BLIND AUDIT Day 009

from header import header

def get_result(participants):
    greatest_bid = 0
    winner = ""

    for key in participants:
        if participants[key] > greatest_bid:
                greatest_bid = participants[key]
                winner = key
    
    print(f"Winner is {winner} with ${greatest_bid}!!")


continue_audit = True
participants = {}

print(header)

while continue_audit:

    new_person_name = input("What is your name? -> ")
    new_person_bid = int(input("What is your bid? -> $"))

    participants[new_person_name] = new_person_bid

    comming_participants = input("Do you want to add another participant? Y or N -> ")

    if comming_participants == "N":
        continue_audit = False

    # Clear console
    print('\033c', end='')

print("Result is...\n.\n,\n")
get_result(participants)



