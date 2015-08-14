from sys import exit
import re


# define gold_room()
def gold_room():
    '''
    This is the gold room. Player chooses amount of gold,
    and if the choice is an integer and less than 50, prints "Nice, 
    you're not greedy, you win! Good Job!". If the integer is greater
    than or equal, prints "You greedy bastard! Good Job!" by calling
    "dead()" to quit the game.

    If the player does not type a number, except the ValueError,
    print "Man, learn how to type a number!" then calls the gold_room()
    function to restart it. 
    '''

    instructions = """
    This room is full of gold.
    There is a door to the Northwest and a door to the Norteast.
    """
    print instructions


    while True:
        choice = raw_input("> ") 
        if "take" in choice:
            while True:
                # take input and run the split() method to get a list
                goldnum = raw_input("How much gold do you take? > ").split()

                # iterate over list, test slice to see if it's a digit
                # and then if it's < 50
                for num in goldnum:
                    if num.isdigit() == True and int(num) < 50:
                        dead("Nice, you're not greedy, you win!")
                    elif num.isdigit() == True and int(num) >= 50:
                        dead("You greedy bastard!")
                    elif num.isdigit() == False:
                        pass

                print "Man, learn how to type a number!"
            # With the current implementation, you can't hit a value error and
            # if no number is typed the loop ends and you are taken back to line 26
            # for the while loop....            
            # raise ValueError:
            #     print "Man, learn how to type a number!"
            #     print

        elif "north" in choice and "west" in choice:
            monkey_room()
        elif "north" in choice and "east" in choice:
            pit_room()
        elif "instructions" in choice:
            print instructions
        else:
            print "I don't know what that means."



def bear_room():
    '''
    '''
    instructions = """There is a bear here.
    The bear has a bunch of honey."
    The fat bear is in front of another door to the south."
    How are you going to move the bear?
    """
    print instructions

    bear_moved = False

    while not bear_moved:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "instructions":
            print instructions
        elif choice == "taunt bear":
            print "The bear has moved from the south door. You can go through it now"
            bear_moved = True
        elif "east" in choice:
            start()
        else:
            print "I have no idea what that means."

    # Now the bear is moved
    while True:
        choice = raw_input("> ")

        if choice == "taunt bear":
            dead("The bear gets pissed off and chews your leg off.")
        elif "south" in choice: 
            heart_room()
        elif "east" in choice:
            start()
        elif "instructions" in choice:
            print "The bear has moved from the south door. You can go through it now"
        else:
            print "I have no idea what that means."


def cthulu_room():

    instructions = """
        Here you see the great evil Cthulhu.
        He, it, whatever stares at you and you go insane.
        Do you flee for your life to the West or eat your head? Or maybe something more brave?
        """
    print instructions

    tries = 0

    while True:

        choice = raw_input("> ")

        if "flee" in choice:
            start()
        elif "head" in choice:
            dead("Well that was tasty.")
        elif "brave" or "fight" in choice:
            print "You decide to fight the insanity. Cthulu values your bravery."
            print 'Cthulu bellows, "Mortal... Why have you decided to fight?"'
            bellows = ['Resistance', 'Is', 'Fuetile']
            for i in bellows:
                print "%s..." % i
            break

    test_passed = False
    while tries < 10 and not test_passed:
        if tries == 0:   
            print "Your vision begins to blur and goes dark."
            print "You hear in the distance a familiar bellow:"
            print "Mortal... completing this task will prove your sanity in the face of a god..."
            print "ENTERRRRRRRRRRRR"
        else:
            print "You may try again. Beware, these are not unlimited..."
            print 10 - tries, "tries left."    

        test_passed = cthulu_mind_test()
        tries += 1

    if not test_passed:
        dead("You go insane and flee into the deepest depths of your mind!")
    else:
        print "Ahhh, the force is strong with you..."
        print "A door appears to the South."
        print "There is a door to the West and a door to the South"
        while True:
            choice = raw_input("> ").lower()

            if "south" in choice:
                gargoyle_room()
            elif "west" in choice:
                start()
            else:
                print "I don't know what you're talking about."


def cthulu_mind_test(): # this really should be its own function - complete
    print "Suddenly arcane rune symbols enter your field of vision"
    print "You recognize them! Arithmitic..."
    print "You then hear a deep echo:"
    print "What is EIGHT to the power of TWO?!!"

    test_passed = False

    try:
        choice = raw_input("> ")
        if int(choice) == 64:
            test_passed = True
        else:
            print "AH HA! You are no match for the INSANITY!"
            print
            print
    except ValueError:
        print "You're uttering gibberish, a sign of INSANITY!"
        print
        print
    return test_passed

def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your east and west."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "west":
        bear_room()
    if choice == "east":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


def gargoyle_room():
    instructions = """
        You enter the room and see three gargoyles staring back at you..
        You see that each gargyole is inscribed with a symbol on it's base
        They read, 'Omnia', 'Amor', 'Vincit'
        A button below each gargoyle appears to be present.
        There is a door to the North and a door to the West  
        """
    print instructions

    while True:
        choice = raw_input("> ").lower()
        if "north" in choice:
            cthulu_room()
        elif "west" in choice:
            swamp_room()
        elif "instructions" in choice:
            print instructions
        else:
            print "I don't know what you're talking about"



def heart_room():
    instructions = """
    This is the Heart Room.
    There is a door to the North and a door to the East.
    """
    print instructions

    while True:
        choice = raw_input("> ").lower()
        if "north" in choice:
            bear_room()
        elif "east" in choice:
            swamp_room()
        elif "instructions" in choice:
            print instructions
        else:
            print "I don't know what that means"




def swamp_room():
    instructions = """
    This is the Swamp Room.
    There is a door to the West.
    There is a door to the East.
    There is a door to the Southwest.
    there is a door to the Southeast.
    """
    print instructions

    while True:
        choice = raw_input("> ").lower()
        if "west" in choice and "south" in choice:
            monkey_room()
        elif "west" in choice:
            heart_room()
        elif "east" in choice and "south" in choice:
            pit_room()
        elif "east" in choice:
            gargoyle_room()
        elif "instructions" in choice:
            print instructions
        else:
            print "I dont know what you're talking about"




def monkey_room():
    instructions = """
    This is the Monkey Room.
    There is a door to the North.
    There is a door to the South.
    """
    print instructions

    while True:
        choice = raw_input("> ").lower()
        if "north" in choice:
            swamp_room()
        elif "south" in choice:
            gold_room()
        elif "instructions" in choice:
            print instructions
        else:
            print "I don't know what that means"

def pit_room(): 
    instructions = """
    As you enter, the door reads 'Pit of Dispair'.
    The door swiftly closes behind you. It appears you are trapped.
    Looking up, you see two platforms to your left and right.
    
    Protruding from the walls you see that there is a way up.
    Rocks embedded in the walls, vines, and small gaps where other unsuccessful
    adventurers have attempted to escape are all visible.

    There is a door to the North.
    There is a door to the Southwest.
    """
    print instructions

    while True:
        
        choice = raw_input("> ").lower()

        if "north" in choice:
            swamp_room()
        elif "south" in choice and "west" in choice:
            gold_room()













