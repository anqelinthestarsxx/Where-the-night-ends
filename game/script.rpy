#Remember this is the Github Desktop file, NOT the rpy one!
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
    "I'm hungry.."
    "You pick up your phone to order some food."
    "Should.. I order.. or go to the store..?" #Super secret (not rlly) secret "Escape" option? maybe? idk
    menu:
        "Order food":
            "You decide to order some pizza and wings."
            "The little app on your phone says it's being prepared."
            jump wait_for_food
        "Go to the store":
            jump store_run

label wait_for_food:
    "You decide to check the clock one more time before going back to work."
    "2:46 AM"
    "'Ah fuck this.' And back to work you go."
    "You hear something on the carpet approaching your room.."
    "Like someone's walking towards it.."
    "'Mom..?'"
    "You call out to your mom, but she doesn't respond."
    "Probably because she's not supposed to be home"
    "You hear the sound of the door creaking open.."
    "your husky, Winter is standing in the doorway, looking at you."
    "'Jesus Winter! You can't just do that!'"
    "Winter tilts her head at you, like she's confused."
    "You sigh again, and reach into the box of treats by your desk."
    "'Why are you even awake?'"
    "You hand the treat to Winter, and give her very generous rubs."
    "She always seems to know when something's wrong~"
    "Then.."
    play sound "phone_ringing.ogg"
    "."
    "."
    "."
    "Unknown number."
    $ call_choice = renpy.call_screen("phone_call")

    if call_choice == "answer":
        stop sound "phone_ringing.ogg"
        "You answer the phone."
        a "Aaliyah?"
        p "Who is this?"
        a "Listen. I'm you."
        p "ex-excuse me?"
        a "Do NOT let the time hit 3:00 AM."
        p "What do-"
        "The call disconnects."
        jump call_accepted

    elif f call_choice == "decline":
        stop sound "phone_ringing.ogg"
        "You decline the call."
        "The phone stops ringing."
        "You glance at the clock again."
        "2:47 AM"
        "'Just another spam caller..'"
        "'I need to focus.'"
        "You go back to work."
        jump call_declined

screen phone_call():
    timer 5.0 action Return("decline")

    vbox
        textbutton "Answer" action Return("answer")
        textbutton "Decline" action Return("decline")


label call_accepted:
    "You stare at your phone."
    "That was my voice."
    "."
    "."
    "."
    "'No.'"
    "'I'm just tired.'"
    "You set your phone back down."
    "You glance at the clock once again."
    "It's still 2:47."
    "'Yeah.. fuck this-'"
    "You go back to working on your project."
    "'I'm just fucking tired..' You mutter to yourself."
    "You click back onto your presentation."
    "You stare at the same slide you've been working on "
    "You reread the same sentence."
    "It still doesn't make sense."
    "You blink."
    "Your read it again."
    " "
    "You finally make a few changes."
    "Delete."
    "Type."
    "Delete."
    "Type."

    "2:48 AM."

    "You sigh."
    "'Okay'"
    "'One more slide.'"
    "'Should.. I..'"

    menu:
        "Keep working":
            jump keep_working

        "Check the call:":
            jump check_call

        "Get some water":
            jump get_water

label keep_working:
    "You shake your head."
    "'Nope.'"
    "'Not dealing with that right now.'"

    "You turn back toward your computer."
    "Your presentation is still open."

    "You stare at the screen. "
    "The same slide has been sitting there for what feels like forever."

    "You move your mouse."
    "Click."
    "Type."
    "Delete."
    "Type again."

    "Slowly, the slide starts to come together."

    "You glance at the clock."

    "2:48 AM."

    "'Okay.'"
    "'That's better.'"

    "You take another sip of your Monster.."
    "Then look back at your presentation."

    "."
    "."
    "."

    "Something feels wrong."
    "You look at the clock again."
    "2:48 AM."
    "'What?'"
    "You wait a few seconds."
    "2:48 AM."
    "You refresh the clock."
    "2:48 AM."
    "."
    "."
    "."
    "You lean closer to the clock."
    "2:48 AM."
    "You check your computer."
    "2:48 AM."
    "You check your phone."
    "2:48 AM."
    "All three clocks agree."
    "'Okay...'"
    "'That's weird.'"
    "You look back at your presentation."
    "You start typing again."
    "A few sentences."
    "Then a paragraph."
    "You're finally getting somewhere."
    "You glance at the clock."
    "2:49 AM."
    "You sigh in relief."
    "'See?'"
    "'I'm just tired.'"
    "You continue working."
    "."
    "."
    "."
    play sound "notification.ogg"
    "You hear a notification."
    "No new messages."
    "You frown."
    play sound "notification.ogg"
    "The notification sound plays again."
    "Still nothing."
    "You check the clock."
    "2:48 AM."
    "You stare at the clock."
    "2:48 AM."
    "You look at your phone again."
    "Nothing."
    "."
    "."
    "."
    "okay..."
    "You put your phone back down."
    "A few seconds pass."
    play sound "notification.ogg"
    "You freeze."
    "You slowly look at your phone."
    "Nothing."
    "You pick it up."
    "No notifications."
    "You check your messages."
    "Nothing."
    "You check your email."
    "Nothing."
    "You open your presentation again."
    "."
    "."
    "."
    "There's a new slide."
    "Slide 13 of 12."
    "'What the fuck?'"
    "You click on the slide."
    "Don't let it reach 3."
    "That is all the slide reads."
    "You stare at the slide."
    "."
    "."
    "."
    "'I didn't make this.'"
    "You look at the rest of the presentation."
    "Every other slide is exactly how you remember it."
    "You click back to slide 12."
    "Slide 12 of 12."
    "You click forward."
    "Slide 13 of 12."
    "Don't let it reach 3."
    "'Okay.'"
    "You close the presentation."
    "'Nope.'"
    "You reopen the presentation."
    "Slide 13 is still there."
    "You select it."
    "Delete."
    "The slide disappears."
    "You sigh."
    "'Finally.'"
    "You look at the clock."
    "2:49 AM."
    "You turn back to your computer."
    "slide 13 of 12."
    "It's back."
    menu:
        "Delete the slide":
            jump delete_slide
        "Read the slide again":
            jump read_slide
        "Close the presentation":
            jump close_presentation
        "Call the number back":
            jump call_back

label delete_slide:
    "You stare at the slide."
    "'Nope.'"
    "You click the slide."
    "You select everything."
    "Delete."
    "The slide disappears."
    "You stare at the presentation."
    "Slide 12 of 12."
    "'okay.'"
    "You lean back in your chair."
    "You let out a long sigh."
    "'I'm seriously losing it.'"
    "You take another sip of your Monster."
    "You turn back toward your computer."
    "."
    "."
    "."
    "You hear a faint clicking sound."
    "Click."
    "Click."
    "Click."
    "You look at your computer."
    "Slide 13 of 12."
    "You freeze."
    "'No.'"
    "You click on the slide."
    "Don't let it reach 3."
    "You didn't type it."
    "You didn't copy it."
    "You deleted it."
    "And yet..."
    "It's still there."

label read_slide:

label close_presentation:

label call_back:


label check_call:



label get_water:



#DECLINED PATH (for the sake of my organization)
label call_declined








label store_run:
    "TBD!"

label back_to_work:
    "Welcome to where this doesn't work yet."
    "Sorry, not sorry! heh"

    return