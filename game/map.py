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
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ") 
    try:
        if re.match('[0-9]', choice) and int(choice) < 50: 
            dead("Nice, you're not greedy, you win!")
        elif int(choice) >= 50:
            dead("You greedy bastard!")
    except ValueError:
        print "Man, learn how to type a number!"
        print
        print
        gold_room()


def bear_room():
    '''
    '''
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I have no idea what that means."



def cthulu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head? Or maybe something more brave?"

    tries = 0
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
        while tries < 11:
            if tries == 0:   
                print "Your vision begins to blur and goes dark."
                print "You hear in the distance a familiar bellow:"
                print "Mortal... completing this task will prove your sanity in the face of a god..."
                print "ENTERRRRRRRRRRRR"
                cthulu_mind_test()
                tries =+ 1
            elif 1 <= tries <= 10:
                print "You may try again. Beware, these are not unlimited..."
                print 10 - tries, "tries left"
                cthulu_mind_test()
                tries =+ 1
            else:
                print 
                dead("You go insane and flee into the deepest depths of your mind!")
    else:
        cthulu_room()


#tries = 0 # how to get this into the function and used in the nested functions?
          # maybe not possible? blech
# def cthulus_mind():

#     if tries == 0:   
#         print "Your vision begins to blur and goes dark."
#         print "You hear in the distance a familiar bellow:"
#         print "Mortal... completing this task will prove your sanity in the face of a god..."
#         print "ENTERRRRRRRRRRRR"
#         cthulu_mind_test()
#     elif 1 <= tries <= 10:
#         print "You may try again. Beware, these are not unlimited..."
#         print 10 - tries
#         cthulu_mind_test()
#     else:
#         print "You go insane and begin to flee!"
#         start()

def cthulu_mind_test(): # this really should be its own function - complete
    print "Suddenly arcane rune symbols enter your field of vision"
    print "You recognize them! Arithmitic..."
    print "You then hear a deep echo:"
    print "What is EIGHT to the power of TWO?!!"
    choice = int(raw_input("> "))

    try:
        if choice == 64:
            print "Ahhh, the force is strong with you..."
            gold_room()
#                cthulu_mind_test2()
        else:
            print "AH HA! You are no match for the INSANITY!"
            print
            print
            cthulu_room()
    except ValueError:
        print "You're uttering gibberish, a sign of INSANITY!"
        print
        print
        cthulu_mind_test()

    return

def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    if choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


def gargoyle_room():
    print "You enter the room and see three gargoyles staring back at you.."
    print "You see that each gargyole is inscribed with a symbol on it's base"
    print "They read, 'Omnia', 'Amor', 'Vincit'"
    print "A button below each gargoyle appears to be present." 
    pass



def heart_room():
    pass

def swamp_room():
    pass

def monkey_room():
    pass

def pit_room(): 
    print "As you enter, the door reads 'Pit of Dispair'."
    print "The door swiftly closes behind you. It appears you are trapped"
    print "Looking up, you see two platforms to your left and right."
    print """
    Protruding from the walls you see that there is a way up.
    Rocks embedded in the walls, vines, and small gaps where other unsuccessful
    adventurers have attempted to escape are all visible.
    """

    # Define switches at top of pit
    left_switch = False
    right_switch = False

    #  Turns out the Timer() function isn't very useful for a game.
    # def platform_crumble():
    #     exit("The platform crumbles beneath you and you fall to your death.")

    # define platform crash function so I don't have to write out the code twice.
    def platform_crash():


# loop until left_switch and right_switch are True
    while left_switch or right_switch = False:
        choice = raw_input("> ")
        # create mechanism to activate switch
        if "climb" and "left" in choice:
            print "You scale the wall to your left, reaching the platform."
            print "It doesn't seem very sturdy"
            print "You see a switch in the wall! Do you activate it?"
            activate_switch = raw_input("> ")
            if "activate" or "push" or "press" in activate_switch:
                crash = 0
                while crash < 16:
                    print "The platfrom begins to shake under you"











