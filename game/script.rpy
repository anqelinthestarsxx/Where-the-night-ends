define p = Character("Player", color="#860000")
define alt = Character("Alternate Player", color="#810000")
default snack_choice = None

label start:

    play music "deskbgm.ogg"
    scene desk

    "You're sitting at your desk."
    "Your Monster is half empty."
    "Yet you take another sip."
    "Your project isn't going to finish itself."
    "You take a deep sigh."
    "You glance at the clock."
    "2:40 AM."
    "You have class in 5 hours."
    "You sigh again, and take another sip of your Monster."
    play sound "almost_done.ogg"
    "'Almost done.' You mutter to yourself."
    "You glance at the clock again."
    "2:41 AM."
    "Your typing speed is slow, like how your brain is functioning right now."
    "But you're pushing through."
    "This is important, your future depends on this project."
    "'Just keep going' you tell yourself."
    "You left your friends behind to work on this project."
    "Simply stopped replying to their messages."
    "You love them.. but school is hell right now."
    "You need to focus."
    "Focus on your project."
    "On your Future."
    "focus."
    "Focus."
    "Why can't you focus?"
    "."
    "."
    "."
    "You can't work like this."
    "You grab your now empty can of Monster, and leave your room."

    scene kitchen

    "You walk down the hall, and into the kitchen."
    "You open the fridge, and grab another can of Monster, practically ice cold this time."
    "The glow of the fridge on your face is bright.."
    "You squint your eyes and close the door."
    "Reaching up to the cabinet, you open it for any snacks."
    play sound "cabinetopen.ogg"
    "Cosmic Brownies.."
    "Or.. "
    "you reach further in the back of the cabinet."
    "Honey buns.."
    menu:
        "Cosmic Brownies":
            "You grab one of the cosmic brownies.."
            "These were always your favorite treat"
            "It's not a full meal but.."
            "Well.. a full meal doesn't sound too bad actually.."
            "Maybe I can order something.."
            "You close the cabinet door, and bring your snacks back to your bedroom."
            $ snack_choice = "Cosmic Brownies"

        "Honey buns":
            "You grab one of the honey buns.."
            "These are a bit more filling than the cosmic brownies would have been..."
            "You close the cabinet door, and bring your snacks back to your bedroom."
            $ snack_choice = "Honey buns"

    "Sighing, you sit back down at your desk."
    "You check the clock once more.."
    "3:00 AM."
    "'what?'"
    "'the fuck?'"
    "You glance at your Monster, and see that it's empty."
    "'But I just-'"
    "You glance at the clock again."
    "2:44 AM."
    if snack_choice == "Cosmic Brownies":
        jump food_order
    else:
        jump back_to_work

#YAY! FIRST BIG BREAKING POINT IN THE CODE~
label food_order:




label back_to_work:

    return