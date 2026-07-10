# Define function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
# Define function to jump as this was repeated
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
# Created FOR loop as the jump function needed to be called about 6 times
for step in range(6):
    jump()
