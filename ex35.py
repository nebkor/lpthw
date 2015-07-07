from sys import exit
import re

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    try:
        goldnum = int(choice)
        if goldnum < 50:
            dead("Nice, you're not greedy, you win!")
        # else if goldnum is *not* less than 50..
        elif not (goldnum < 50):
            dead("You greedy bastard!")
    except ValueError:
        print "Man, learn how to type a number!"
        print
        print
        gold_room()


def bear_room():
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

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty.")
    elif "brave" in choice:
        print "You decide to fight the insanity. Cthulu values your bravery."
        print 'Cthulu bellows, "Mortal... Why have you decided to fight?"'
        bellows = ['Resistance', 'Is', 'Fuetile']
        for i in bellows:
            print "%s..." % i
        cthulus_mind()
    else:
        cthulu_room()


def cthulus_mind():
    tries = 0

    while tries < 11:
        if tries == 0:
            print "Your vision begins to blur and goes dark."
            print "You hear in the distance a familiar bellow:"
            print "Mortal... completing this task will prove your sanity in the face of a god..."
            print "ENTERRRRRRRRRRRR"
            cthulu_mind_test()
            tries += 1
        elif 0 < tries < 10:
            print "You may try again. Beware, these are not unlimited..."
            print 10 - tries
            cthulu_mind_test()
            tries += 1
        else:
            print "You go insane and begin to flee!"
            start()
    return


def cthulu_mind_test():
    print "Suddenly arcane rune symbols enter your field of vision"
    print "You recognize them! Arithmitic..."
    print "You then hear a deep echo:"
    print "What is EIGHT to the power of TWO?!!"

    try:
        choice = int(raw_input("> "))
        if choice == 64:
            print "Ahhh, the force is strong with you..."
            gold_room()
        else:
            print "AH HA! You are no match for the INSANITY!"
            print
            print
    except ValueError:
        print "You're uttering gibberish, a sign of INSANITY!"
        print
        print

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


start()
