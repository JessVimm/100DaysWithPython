# Code for Reeborg's World Maze exercise at reeborg.ca

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
right_turns_made = 0
    
while not at_goal():
    if not wall_on_right():
        if right_turns_made < 4:
            right_turns_made += 1
            turn_right()
            move()
        else:
            turn_left()
            right_turns_made = 0
    elif front_is_clear():
        move()
        right_turns_made = 0
    else:
        turn_left()
        right_turns_made = 0
