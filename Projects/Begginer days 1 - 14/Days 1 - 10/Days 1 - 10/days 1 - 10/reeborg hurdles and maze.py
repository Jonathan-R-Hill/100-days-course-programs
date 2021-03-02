"""
Hurdle 4 at: 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

"""
# Code for the website below
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    move()
    
while not at_goal():
    if not wall_on_right and wall_in_front():
        jump()
    
    elif not wall_on_right and is_facing_north():
        jump()
    
    elif wall_in_front() and wall_on_right():
        turn_left()
        
    elif wall_on_right():
        move()
    else:
        turn_right()
        move()
"""