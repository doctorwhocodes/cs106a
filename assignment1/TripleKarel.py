from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(4):
        put_beeper()
        move()
    turn_left()
    for i in range(3):
        move()
        put_beeper()
    move()
    turn_left()
    for i in range(4):
        move()
        put_beeper()
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    move()
    turn_left()
    for i in range(3):
        move()
        put_beeper()
    move()
    turn_left()
    for i in range(3):
        move()
        put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    turn_left()
    for i in range(3):
        move()
        put_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
