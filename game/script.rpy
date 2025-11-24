# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random
    renpy.add_layer(layer="AboveEverything",above="screens",below=None,menu_clear=True,sticky=True)
    
    def writingSpriteHandler():
        time = 1
        while animating:
            if time > 5:
                time =1
                renpy.show("marms_base")
                #renpy.image("characters/Alby_@2.webp")
            break

    def slide_vibrate(trans, st, at, /):
        if st > 1.0:
            trans.xalign = 1.0
            trans.yoffset = 0
            return None
        else:
            trans.xalign = st
            trans.yoffset = random.randrange(-10, 11)
            return 0


init:
    $ renpy.music.register_channel("sound1", mixer="sfx", loop=False)
    $ renpy.music.register_channel("sound2", mixer="sfx", loop=False)
    $ renpy.music.register_channel("soundLoop1", mixer="sfx", loop=True)
    $ renpy.music.register_channel("soundLoop2", mixer="sfx", loop=True)
    $ renpy.music.register_channel("voice1", mixer="voice", loop=False)
    $ renpy.music.register_channel("music1", mixer="music", loop=True)

    $ renpy.music.register_channel("channelEmote", mixer="sfx", loop=False)

image removeThis = "removeThis.png"



#marms is for testing, remove later
layeredimage marms:
    always:
        "marms_base"

    group clothing:
        xpos 160
        ypos 330
        attribute bowtie:
            zoom 0.3
        attribute tophat:
            zoom 0.3
            xpos 160
            ypos 0

#this needs overhauled later once I implement a dialogue opacity option and I figure out how default and persistant values work fully
default persistent.dialogueBoxOpacity = 1.0

label start:
    $ persistent.dialogueBoxOpacity = 1.0

    menu startQuestion:
        "Which mode do you want?"
        "Test scene":
            jump testScene
        "Main game":
            jump scene_Intro
        "Scene1":
            jump scene1
        "Scene2":
            jump scene2
        "Scene3":
            jump scene3
        "Scene4":
            jump scene4
    

#----------------------------#
#---------TEST SCENES--------#
#----------------------------#

label testScene:
    $ persistent.dialogueBoxOpacity = 1.0
    scene bg registration
    "start the thing"
    show blackScreen zorder 10 onlayer AboveEverything
    with fade
    show screen inputBlocker
    show cg1 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,1)
    pause 3
    show tyWriting zorder 200 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    "Start here"
    show cg1 at move(0.1,1) 
    "now flip"
    
    

    "writing starts now"
    show writing1 zorder 200
    show writing2 zorder 200
    show ty cg zorder 100
    show border zorder 50
    jump endScene


label testCG:
    show blackScreen zorder 10 onlayer AboveEverything
    with fade
    show screen inputBlocker
    show cg1 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    pause 3
    show tyWriting zorder 200 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    ""
    hide blackScreen
    hide tyWriting
    with dissolve
    show cg1 at diaryMove(0.5,2.0,2)
    with ease


#----------------------------#
#---------MAIN SCENES--------#
#----------------------------#

label scene_Intro:
    $ persistent.dialogueBoxOpacity = 1.0
    scene bg registration
    play soundLoop1 "BGS_Forest_1.ogg" fadein 1.0 volume 0.5
    show ty at appear(0.65) 
    show marsh at appear(0.45)
    show marsh at move(-0.3,1.5)
    with None
    show marsh:
        xpos -0.3
    with dissolve
    "Marsh leaves in a hurry, and I find myself alone outside registration." 
    "It's pretty normal for him to struggle to find something for me to do, but with the ongoing preparations for the fall season, I feel especially useless doing nothing."
    "So I go searching for someone to help."
    show ty at move (1.3,2)
    with None
    show ty:
        xpos 1.3
    with dissolve

    scene bg park
    show tibbs at appear (0.35)
    show ty at appear (1.3)
    with fade
    show ty at move(0.8,1.5)
    with dissolve
    "But the first person I come across is someone who wrote the book on self-sufficiency."
    show blackScreen zorder 10 onlayer AboveEverything
    with fade
    show screen inputBlocker
    show cg1 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    pause 3
    hide ty
    show tibbs zorder 50:
        xpos 0.65
    show camper1 zorder 50 at appear(0.35)
    show tyWriting zorder 200 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    ""
    hide blackScreen
    hide tyWriting
    with dissolve
    show cg1 at diaryMove(0.5,2.0,2)
    with ease
    show camper1 talk
    gu  "How do you get to the river from here?"
    show camper1
    show tibbs talk
    play voice1 "Tibs_01TrailRiver_1.ogg"
    ti "There’s a trail that goes by the river, but it’s one of the paths we haven’t gotten to cleaning up yet."
    stop voice1
    show tibbs
    show camper1 talk
    gu "Is it safe to take?"
    show camper1
    show tibbs talk
    play voice1 "Tibs_02Treacherous_1.ogg"
    ti "It’s a bit more treacherous than the main paths, but people still use it pretty often. There’s this, uh, tree that runs along the river—damn it—what was it called? Marsh is always yapping about it. Anyway, it’s got these, uh, droopy things growing on it."
    stop voice1
    show tibbs 
    show camper1 talk
    gu "...Droopy things."
    show camper1
    show tibbs talk
    play voice1 "Tibs_03ThingFlowers_1.ogg"
    ti "Yeah, the're like the things that turn into flowers."
    stop voice1
    show tibbs
    show camper1 talk
    gu "You mean catkins?"
    show camper1
    show tibbs talk
    play voice1 "Tibs_04Catkins_1.ogg"
    ti "Yes! Catkins. Hard to miss. Once you start seeing those you know you’re by the river."
    stop voice1
    show tibbs 
    show camper1 talk
    gu "Thanks for the help!"
    show camper1
    show tibbs talk 
    play voice1 "Tibs_05NoProblem_1.ogg"
    ti "No problem..."
    stop voice1
    show tibbs 
    show camper1 at move(-1.,2)
    with None
    show camper1:
        xpos -1.0
    with dissolve
    show tibbs talk frown
    play voice1 "Tibs_06ForestyStuff_1.ogg"
    ti "Ugh, this forestry stuff is better off with Marsh."
    stop voice1
    hide camper1
    show ty at appear(1.15)
    with None
    show tibbs at move (0.2, 1.5)
    show ty at move(0.75,1.5)
    "I can only imagine the wealth of knowledge a park ranger of his caliber has at his disposal. And one day, if I’m lucky, that could be me!"
    show dustin at appear(1.2)
    show dustin behind ty at move(0.85, 0.5)
    show tibbs at move(-0.2,0.5)
    with None
    pause 0.5
    show dustin talk
    with vpunch
    play voice1 "Dustin_Greeting_3.ogg"
    du "Heya, Ty!"
    stop voice1
    show ty talk:
        xzoom -1.0
    show ty talk at move(0.5,1)
    show dustin
    play voice1 "Ty_Greeting_2.ogg"
    ty "Hello, Dustin"
    show ty
    show dustin talk
    play voice1 "Dustin_Deer_1.ogg"
    du "What’re you standing around for, Ty-guy? You’re looking like a deer in headlights."
    stop voice1
    show dustin 
    show ty talk 
    show tibbs at move(-0.2,2)
    ty "A deer? But I’m always a deer."
    show ty
    show dustin talk
    du "Don’t think too hard about it, buddy. Whatcha up to? Marsh working you ragged?"
    show dustin at move(0.75,0.5)
    show ty talk
    ty "He told me to ask around if anyone needed help."
    show ty
    show dustin talk
    du"Oh, epic! Here, take my phone! I wanna get a video of this!"
    show dustin at move (0.65,0.5)
    "Dustin shoves his phone into my hands before I can respond. He darts off, coming to a stop next to a large pile of leaves."
    show dustin at move (0.7,1)
    show ty at move(0.3,1)
    show tibbs at move(-0.2,1)
    with ease
    pause 1
    show dustin talk
    du "Are you filming?"
    show dustin 
    "I press the record button on Dustin’s phone and aim it at the wolf waving at me from a little ways away. I give him a thumb’s up."
    show dustin talk
    du "Yahoo!!"
    show dustin at moveWithVertical (1.5,0.3,0.3)
    pause 0.2
    show dustin:
        pos (1.2,1.0)
    "Dustin does a full cannonball leap into the pile, scattering leaves into the wind. He rushes back to me, a brown leaf caught in the bushy fur of his wagging tail."
    show dustin talk at move (0.65,1)
    with ease
    du "Lemme see, lemme see!"
    show dustin 
    play voice1 "Dustin_Laugh_1.ogg"
    "Dustin snatches his phone from my hands and watches the video I had recorded with the biggest of grins plastered over his face."
    stop voice1
    show ty talk
    ty"Aren’t you supposed to be cleaning up these leaves? Won’t Marsh get mad if he sees you making a mess?"
    show ty 
    show dustin talk
    du"There’s, like, a bajillion trees around here! No one’s gonna notice if a pile or two hasn’t been raked up yet! Now, come on! Let’s get another vid!"
    show dustin
    show blackScreen zorder 10 onlayer AboveEverything
    with fade
    show screen inputBlocker
    show cg2 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    pause 3
    show tyWriting zorder 200 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    ""
    hide blackScreen
    hide tyWriting
    with dissolve
    show cg2 at diaryMove(0.5,2.0,2)
    with ease
    show dustin talk
    du "Yo, Ty! Earth to Ty! Do those antlers get any signal?"
    show dustin 
    show ty talk
    play voice1 "Ty_Surprise_1.ogg"
    ty "Sorry, what?"
    stop voice1
    show ty 
    show dustin talk
    du "I was saying we should go see what Alby’s up to."
    show dustin
    show ty talk
    ty "What about the leaves?"
    show ty
    show dustin talk
    du "They’ll still be there when we get back! C’mon, I wanna show these to him."
    "Dustin turns on his heel, but when I move to follow him, my nose hits his back."
    show dustin at move(0.9,1)
    show ty at move(0.85,1)
    pause 1.0
    show ty talk at move(0.7,0.2)
    show dustin frown
    play voice1 "Ty_Confusion_1.ogg"
    ty "Dustin? What's wrong?"
    stop voice1
    jump scene1

label scene1:
    scene bg campsite
    with fade
    "I crane my neck to peer around Dustin’s back. He’s gone stiff as a board, lips pursed and eyes wide."
    "Following his line of sight, I’m met with the sight of Gavin, the campground’s local electrician, fiddling with a fuse box."
    show gavin at appear(0.9):
        xzoom -1.0
    show ty at appear(0.1):
        xzoom -1.0
    show dustin shock at appear(0.5)
    with dissolve 
    du "Play it cool, Dustin. Just…play it cool."
    show dustin frown at move(0.5,0.2)
    with ease
    "Dustin starts walking again, his movements decidedly more stilted and uneven than before. I cock my head, watching as he slows his pace when he reaches Gavin."
    show dustin frown at move(0.6,0.2)
    with ease
    "He steals one quick glance in the badger’s direction, almost as if he wants to say something."
    gu "Excuse me?"
    show camper1 at appear(-0.2)
    show gavin:
        xzoom 1.0
    show camper1 at move(0.3,1.5)
    show dustin shock at moveAndFlip(0.5,1)
    "Dustin nearly leaps out of his skin. Gavin turns to look at the commotion, and as two pairs of eyes fall on Dustin, the pink wolf turns white as a sheet."
    show dustin talk frown 
    play voice1 "Dustin_Fluster_1.ogg"
    du " I–uh–I mean–um, what’s up?"
    stop voice1
    show dustin frown 
    gu "Which way goes toward the river?"
    show dustin talk frown 
    du "Uh…th-that way."
    show dustin frown 
    show ty frown 
    "Dustin points off in a direction, though not in the direction of the river."
    gu "Thanks!"
    show camper1 at moveAndFlip(-0.2,1.5)
    show dustin shock
    show ty 
    "Left alone with Gavin, the color does not return to Dustin’s face. He nods shakily at the badger, who nods back at him."
    "Then Dustin scurries away as fast as his legs can take him."
    hide camper1
    show dustin shock at move(0.6,1)
    pause 1
    show dustin shock at move(-0.2,0.3)
    du "Let’s go, Ty! Can’t leave Alby waiting!"
    "With Dustin now just a dust cloud streaking around a corner, Gavin turns his attention to me."
    hide dustin
    show ty talk
    ty "G’morning, Gavin."
    show ty
    "The badger nods to me."
    ga "Mm."

    show blackScreen zorder 10 onlayer AboveEverything
    with fade
    show screen inputBlocker
    show cg3 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    pause 3
    show tyWriting zorder 200 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    ""
    hide blackScreen
    hide tyWriting
    with dissolve
    show cg3 at diaryMove(0.5,2.0,2)
    with ease

    stop soundLoop1
    scene bg giftshop
    with fade
    pause 0.1
    play music1 "DEER DIARY - Friendly Faces.ogg" fadein 1.0
    show alby at appear (1.3):
        ypos 1.1
    show dustin at appear (-0.2)
    show ty at appearAndFlip (-0.2)
    with dissolve
    pause 3
    show dustin at move (0.3, 1.5)
    show ty at move (0.1,1.5)
    pause 1.5
    show dustin talk
    play voice1 "Dustin_Excited_2.ogg"
    du "Yo, Alby! You in here?"
    show dustin
    #show alby at jiggle(40,0.2,2)
    play voice1 "Alby_Greeting_2.ogg"
    al "Hey, dudes! I’m in the back!"
    stop voice1
    show alby at move(1.05,1)
    "We shuffle through the shop, finding Alby half-hidden within a maze of cardboard boxes full of new merchandise for the park’s fall season."

    show dustin talk   
    play voice1 "Dustin_Frustrated_3.ogg"
    du "Dude, you just missed it. I totally just crashed and burned trying to talk to Gavin."
    stop voice1
    show dustin 

    show alby talk
    al "Again? Man, what’s it gonna take to get you to actually be able to talk to the guy?"
    show alby
    show dustin talk
    du "I’ll get back to you when I figure that part out. It doesn’t help that he’s always running around without his shirt on. Why does he do that?"
    show dustin 
    show alby talk
    play voice1 "Alby_Affirm_1.ogg"
    al "Cuz it’s hot!"
    stop voice1
    show alby
    show ty talk
    ty "It’s 50 degrees out today."
    show ty
    show alby talk
    play voice1 "Alby_Negative_2.ogg"
    al "No, man. I meant it’s hot to walk around shirtless."
    stop voice1
    show alby
    show dustin talk
    du "Yeah, I don’t think that’s really it."
    show dustin 
    with None
    show alby:
        linear 0.2 xzoom -1
    pause 0.2
    show alby talk at moveAndFlipWithVertical(0.90,1.0,1)
    al "It’s either that or he’s just one big space heater that needs to cool off from time to time. I get like that in the winter, too."

    show blackScreen zorder 10 onlayer AboveEverything
    with fade
    show screen inputBlocker
    show cg4 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    pause 3
    show tyWriting zorder 200 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    ""
    hide blackScreen
    hide tyWriting
    with dissolve
    show cg4 at diaryMove(0.5,2.0,2)
    with ease

    al "Yo, dudes! Check this out!"

    show dollBear at itemAppear(0.70,0.3,0.2):
        zoom 1.2
    "Alby whips out a small wooden figure of a bear that bears a striking resemblance to Marsh."
    show dollBear at jiggleVertical(20,0.2,0.5)
    show alby talk
    ma2 "Hewwo, hewwo, everyone! It’s me Marsh! Remember: littering is a crime, and criminals get fed to the bears!"
    show alby
    show dollBear at move(0.70,0.1)
    show dustin talk
    du "Yo, dude, that's hilarious! Lemme try!"
    show dustin
    show dollBear at moveWithArc(0.4,-70,0.3)
    "Alby tosses the bear statue to Dustin before reaching back into the box he found it in."
    show dollBear at jiggleVertical(20,0.2,0.5)
    show dustin talk
    ma2 "Remember, campers! Feed the deer, you’re in the clear! Feed the bear? Get outta there!"
    show dollBear at move(0.4,0.1)
    show dustin
    show alby talk
    play voice1 "Alby_Laugh_2.ogg"
    al "Ha ha ha! Nice one, man. But check this out."
    stop voice1
    show alby
    show dollBear at itemDisappear(0.2)
    with None
    hide dollBear
    show dollWolf at itemAppear(0.72,0.3,0.2):
        rotate 10
    show dollBadger behind dollWolf at itemAppear(0.55,0.3,0.2):
        rotate -10
    with dissolve
    "Alby reveals two more statues from behind his back, a wolf and a badger."
    show alby talk
    du2 "Oh, Gavin! Kiss me! Kiss me like Naruto and Sasuke! Muah muah muah muah!"
    show alby
    show dollWolf at itemFight(-60)
    show dollBadger at itemFight(60)
    "Alby smashes the two statues together over and over, so much so that I’m afraid he’s going to damage the wood. Dustin is less than amused."
    
    show dustin talk frown
    play voice1 "Dustin_Negative_2.ogg"
    du "I would NOT say that!"
    stop voice1
    show dustin shock
    show dollWolf at move(0.72,0.1)
    show dollBadger at move (0.55,0.1)
    show alby talk
    al "Oh, sorry, Let me try again"
    show dollBadger at jiggleVertical(20,0.3,0.3)
    ga2 "Wow, Dustin! You’re so cool and hunky! Tell me more about Sword Art Online."
    show dollBadger at move(0.55,0.1)
    show alby
    show dustin talk frown
    play voice1 "Dustin_Angry_1.ogg"
    du "Okay, that’s enough out of you."
    stop voice1
    show dollBadger at itemDisappear(0.2)
    show dollWolf at itemDisappear(0.2)
    show dustin frown at move(1.2, 0.5)
    show alby at move(1.2,0.4)
    "Alby can’t wipe the smile off his face as Dustin chases him around the gift shop to steal back the wooden figurines." 
    "As they weave in and out through displays of cheap toys and animal hand puppets, I reach my hand into the box Alby had been searching through."
    show ty at toAndBackAgain(0,60,0.4)
    pause 0.5 
    show dollDog at itemAppear(0.23,0.5,0.3)
    show alby at move(0.6,1)
    "I pull out another wooden figure, this one a dog."
    show alby talk
    al "Whatcha got there, little dude?"
    show alby
    "I show them the dog."
    show alby talk
    play voice1 "Alby_Interested_2.ogg"
    al "Oh, shit! It’s Tibbs! Let’s hear your best Tibbs."
    stop voice1
    show alby 
    show ty talk
    ty "Oh, um...."
    show ty
    show dustin at move(0.9,1)
    show alby talk
    al "Here, let me start you off."
    show dollBear at itemAppear(0.4,0.5,0.2)
    "Alby snatches the bear statue from Dustin and holds it up next to mine."
    show dollBear at jiggleVertical(20,0.3,0.3)
    ma2 "Howdy, Tibbs! Are you ready for another fun-filled, spectacular day at Break Trail National Park?"
    show dollBear at reset()
    show dollDog at jiggleVertical(20,0.3,0.3)
    show alby
    show ty talk
    ti2 "Uh, yup."
    stop music1
    show ty 
    show dollDog at reset()
    "The gift shop falls silent as Alby waits expectantly for more material to bounce off of."
    play music1 "DEER DIARY - Friendly Faces.ogg" fadein 1.0
    show alby talk
    al "We'll have to work on your improv."
    show alby 
    show ty talk
    play voice1 "Ty_Sad_2.ogg"
    ty "Sorry."
    stop voice1
    show ty
    show alby talk
    show dollDog at itemDisappear(0.2)
    show dollBear at itemDisappear(0.2)
    al "Don’t be sorry, little man! Here, lemme give you your first lesson."
    hide dollDog
    hide dollBear
    show alby at toAndBackAgain(-500,0,1)
    "Alby swivels around me and swipes a fox mask off a display. He holds it at arms length, staring directly into the mask’s empty eye holes."
    show alby talk
    al "You have to feel the character. Become the character! Think not what to say, but what Tibbs would say in this very moment."
    show alby 
    show ty talk
    ty "Tibbs would say to get back to work."
    show ty 
    show alby talk
    al "Okay, you don’t need to be that in character. It’s all about conflict!"
    show alby
    show ty talk
    ty "Conflict?"
    show ty
    show alby talk
    al "Yeah! Like the romantic tension between Dustin and his hunky electrician friend."
    show alby
    show dustin talk frown
    du "Or the climactic struggle between two lifelong rivals having their final battle!"
    show dustin frown
    show alby at moveAndUnFlip(0.6,1)
    show dustin shock at move (0.9,0.2)
    al "Feel their struggle and their anguish!"

    "Alby shifts seamlessly into character, dropping to one knee with hands clasped in a desperate plea."
    show alby talk at moveWithVertical(0.6,1.15,0.3)
    al "Alas, my dear beloved! For our love was truly not meant to be!"
    show alby
    show dustin frown talk
    du "You call that a struggle? Now, THIS is a struggle!"
    show dustin at move(0.95,0.1)

    "Dustin pulls a foam sword from a barrel and thwaps Alby over the head with it."
    show dustin frown at move(0.65,0.15)
    show alby talk at moveWithVertical(0.45,1.0,0.3)
    play voice1 "Alby_Struggle_2.ogg"
    al "Oof!"
    stop voice1
    show alby
    show dustin frown talk
    du "Did that wake you up? If you won’t see reason, then I'll have to knock some more sense into you!"
    show dustin frown

    "Dustin wields two foam swords, twirling around into a dramatic battle stance that looks less than practical."

    show dustin frown talk
    play voice1 "Dustin_Technique_1.ogg"
    du "Here comes my special move! Hyaah!!"
    show dustin frown at jiggleVertical(60,0.11,0.8)
    show alby at albyFuckingDies()
    play voice1 "Alby_Laugh_1.ogg"
    "Dustin assaults Alby with a flurry of foamy strikes that send the larger skunk into a laughing fit as he doubles over on the floor."
    stop voice1
    hide alby
    show dollDog at itemAppear(0.25,0.4,0.2)
    "As Dustin continues to attack Alby with flashy, impractical sword attacks, I find myself looking down at the canine figure in my hands, thinking about Tibbs."
    
    #journal time
    stop music1 fadeout 2.0
    jump scene2

label scene2:
    scene bg honeypot
    play soundLoop1 "BGS_Cafe.ogg" fadein 2 volume 0.2
    show ty at appear(0.22):
        xzoom -1
    show alby behind ty,dustin at appear(0.8):
        xzoom -1
    show dustin at appear(0.5)
    with fade

    show dustin talk frown
    play voice1 "Dustin_Angry_3.ogg"
    du "It’s so dang frustrating! I can’t even look at him without freezing up!"
    stop voice1
    show dustin frown 
    show alby talk
    al "Have you considered he might be a gorgon sister? Hsssss!"
    show alby 
    show dustin talk frown 
    du "Not helping, man."
    show dustin frown
    show alby talk 
    al "Okay, but for real. Maybe try finding a group setting to talk to him in. Have a buffer with you so you can default to them if things go south."
    show alby 
    show dustin talk frown 
    du "That might be tough. Gavin’s always working on his own."
    show dustin frown 
    show alby talk
    al "Maybe we can try inviting him to one of those holiday parties Marsh is always throwing. I can shmooze him up with you and then dip once you’re comfortable."
    show alby
    show dustin talk 
    play voice1 "Dustin_Interest_2.ogg"
    du "That might actually work, huh...."
    stop voice1
    show dustin 
    show alby talk
    al "See? I know what I'm talking about. What about you, Ty?"
    show alby 
    show ty talk
    ty "Um, what about me?"
    show ty
    show alby talk
    al "Dustin’s got his little crush on the electrician, but what about you? Do you liiiiike anyone?"
    show alby 
    "I blink back at two overly expectant faces looming ever closer to me, their careful eyes scanning my expression for any hint of embarrassment."
    show ty talk
    #VOICE LINE TO GO HERE
    ty "I like you guys."
    show ty
    "Based on their reactions, that wasn't the answer they were looking for."
    show alby talk
    al "Aw, shucks, little bud. I'm flattered. I like you too."
    show alby
    show dustin talk frown
    du "I can’t be the only one dealing with a hopeless crush at work, can I?"
    show dustin 
    show alby talk 
    al "I’m certainly not pining after any hunkies or honies right now. Don’t think I can say the same about Tibbs, though."
    show alby 
    show dustin talk frown
    play voice1 "Dustin_Confused_1.ogg"
    du "Tibbs? Ranger Tibbs? “Talk to me and get your face chewed off” Tibbs? With WHO?"
    stop voice1
    show dustin shock
    show alby talk
    al "Well, Marsh, obviously. The sexual tension between those two is palpable, man. You can almost taste in in the air."
    show alby 
    show dustin talk frown 
    play voice1 "Dustin_Negative_2.ogg"
    du "There’s no way! Like, sure, maybe they work well together, but Tibbs is 100%% business."
    stop voice1
    show dustin shock
    show alby talk
    al "Maybe on the surface, but I swear there’s some feelings bubbling underneath just waiting to boil over."
    show alby 
    show dustin talk
    du "As if! Ty, back me up here."
    show dustin 
    show ty talk
    ty "I think they’re just business partners."
    show ty
    show dustin talk 
    du "See? Tibbs isn’t at work to make friends. He clocks in, does his job, and then leaves as soon as he clocks out. He rarely even says goodbye to anyone."
    show dustin
    show alby talk 
    al "That’s because he doesn’t want the drama."
    al "He knows our nosy butts would be all over him and Marsh if word got out that they were dating. That’s why I have a theory that they’re having secret rendezvous late at night after we all go home."
    show alby 
    show dustin talk 
    du "Fat chance! And even if that was true, do you really think Marsh could keep a secret like that? Dude’s an open book!"
    show dustin 
    "Alby’s grin grows especially devious."
    show alby talk 
    play voice1 "Alby_Laugh_2.ogg"
    al "I have my theories about those two…"
    stop voice1
    show alby 
    show dustin talk frown 
    du "The only thing I wanna know is what Tibbs actually does when he’s not at work. He’s gotta have a hobby or something."
    show dustin frown 
    show alby talk
    al "Why don't you ask him?"
    show alby
    show dustin talk frown 
    play voice1 "Dustin_Huh_1.ogg"
    du "Are you kidding? Forget Gavin! Try talking to Tibbs!"
    stop voice1
    show dustin shock 
    show alby talk
    al "He’s a little frumpty, but I’m sure he’ll talk if you strike up some chill conversation."
    show alby
    show dustin talk frown 
    du "Yeah? So you’re saying you tried? How’d that work out for you?"
    show dustin frown 
    show alby talk 
    play voice1 "Alby_Sigh_1.ogg"
    al "It was like the in-person equivalent of being left on read."
    stop voice1
    show alby 
    show dustin talk 
    du "I knew it!"
    show dustin 
    show alby talk 
    al "What about you, Ty? You ever crack open a convo with Ranger Tibbs?"
    show alby 
    show ty talk 
    play voice1 "Ty_Negative_2.ogg"
    ty "Nope."
    stop voice1
    show ty
    "But, boy, do I want to."

    #JOURNAL SEQUENCE
    stop soundLoop1 fadeout 2

    jump scene3

label scene3:
    scene bg campsite
    
    show alby  at appear(1.3)
    show dustin  at appear(1.2)
    show ty at appear(0.55)
    with fade

    pause 2
    show marsh frown at appear(-0.2)
    show marsh talk frown at move(0.1,0.2)
    with dissolve
    ma "Ty! TY!! Where’s Dustin and Alby? We’ve got a problem!"
    show marsh frown
    show ty talk behind dustin
    play voice1 "Ty_Surprise_2.ogg"
    ty "What’s wrong?"
    stop voice1
    show ty frown
    show dustin talk frown at move(0.9,0.3)
    show alby frown behind dustin at moveAndFlip(0.7,0.7)
    pause 0.2
    du "Whoa! Where’s the fire?"
    show dustin frown
    show marsh talk frown
    ma "There you are! There’s an emergency! A camper has gone missing!"
    show marsh shock at jiggle(150,1,0)
    "Marsh begins worriedly pacing back and forth, chewing on the tips of his claws."
    show marsh talk frown
    ma "Oh, what are we gonna do? What are we going to do?"
    show marsh  frown at reset()
    with ease
    show alby talk frown 
    al "Whoa! Calm down, bossman. Let’s take it from the top. How do we know there’s a missing person in the park right now?"
    show alby frown
    show camper2 worried at appear(-0.2)
    show tibbs at appear(-0.25):
        xzoom -1
    $cameraTime = 1
    unknown "Excuse me"
    show camper2 worried at moveAndFlip(0.3,0.4)
    with dissolve
    
    
    gu "I reported him missing"
    show marsh frown at move(0.3,cameraTime) 
    show tibbs frown at move(0.1,cameraTime) 
    show camper2 worried at move(0.5,cameraTime) 
    show ty frown at move (0.75,cameraTime)
    show alby frown at move (0.9, cameraTime)
    show dustin frown at move (1.1, cameraTime)
    with ease
    gu "My friend went out for a hike this morning and he hasn’t come back yet. I’ve looked everywhere for him, but I can’t find him anywhere."
    show marsh talk frown 
    ma "We’ve GOT to find him! What if a bear got him? Or he fell into the river? Or, or—"
    show marsh frown
    gu "Oh my god!"
    show marsh shock 
    ma "A search party won’t solve anything if he’s DEAD!!"
    gu "OH MY GOD!!"
    show tibbs talk
    ti "Alby, could you please get Marsh out of here before he whips anyone else into a frenzy."
    show tibbs
    show alby talk at move (0.5,0.5)
    show camper2 worried at move(0.7,0.2)
    show ty frown at move(0.85,0.2)
    with ease
    al "Come on, bossman. Let’s see if we can get you a paper bag."
    show marsh frown at move(0.25,cameraTime) 
    show tibbs frown at move(0.6,cameraTime) 
    show camper2 worried at move(1.2,cameraTime) 
    show ty frown at move (1.25,cameraTime)
    show alby at move (0.2, cameraTime)
    show dustin frown at move (1.6, cameraTime)
    with ease
    pause cameraTime
    show alby at moveAndUnFlip(0.1,0.2)

    #ALL THE ANIMATION STUFF GOES HERE
    show tibbs talk:
        xzoom 1
    ti "Hey."
    ti "Don’t worry. I’ve got this all under control. I won’t let anything bad happen here, I promise."
    show tibbs 
    show marsh
    "Marsh’s eyes widen for a moment, but then his expression softens. He nods solemnly to Tibbs."
    show marsh talk 
    ma "I'm counting on you."
    #AND THEN THEY KISSSS
    show marsh 
    show tibbs talk 
    ti "It’s what I’m here for."
    show tibbs smile
    show removeThis
    pause 0.05 
    hide removeThis
    #the others coe in
    "Alby holds his hand up to his face as if to block it from Marsh’s view. He silently mouths to me and Dustin “secret lovers”."
    show tibbs talk
    ti "We should split up and start searching while we’ve still got some daylight."
    show tibbs
    show alby talk
    show dustin at move(0.95,1)
    al "I’ll take Marsh to registration and let everyone else know what’s going on. We’ll party up from there."
    show alby 
    show dustin talk
    du "I’ll gather up the landscaping crew and start searching."
    show dustin
    show tibbs talk 
    ti "Smart thinking, you two."
    show tibbs at moveAndFlip(0.55,0.1)
    #show dustin at move (1.2,0.5)
    show camper2 at moveAndUnFlip(0.80,1)
    pause 0.5
    "Tibbs turns to the panicked camper among us."
    show tibbs talk
    ti "Could you give us a description of your friend?"
    show tibbs 
    gu "Yeah. He’s a dog wearing a blue jacket."
    show dustin talk
    du "I can work with that!"
    show dustin
    show alby talk
    show ty at move(1.2,0.1)
    al "We’ll pass that on to the others."
    show alby at move (-0.2,1)
    show dustin at move (-0.2,1.2)
    show camper2 at move (-0.2,1.2)
    show marsh at move(-0.2,1)
    show tibbs at moveAndUnFlip(0.2,2)
    show ty frown at move(0.85,2)
    show screen inputBlocker
    pause 2
    hide screen inputBlocker
    show ty talk frown
    ty "W-wait! What should I do?"
    show ty frown
    "I swivel on my heel, watching everyone hurry off in different directions. Most of the others go together toward registration, but Tibbs…"    
    "Tibbs is moving on his own."
    show tibbs at move(-0.2,0.8)
    "My heart pounds against my chest seeing him head off into the woods alone."
    show ty frown at move(0.7,1)
    "He’s Tibbs, right? He knows what he’s doing. I should worry about meeting up with the others and leave him to his business."
    show ty frown at move(0.5,1)
    "But at the same time…"

    jump scene4

label scene4:
    "Darkness is quickly falling over the park. My own antlers cast a shadow that stretches out across the grass, reaching out to Tibbs as he strides singlemindedly toward the forest."
    "He'll be fine, right?"
    "No. I’ve got to follow him. I don’t care how competent he is; Tibbs shouldn’t go out into the forest in the dark."
    #journal time

    scene bg forest deep
    show tibbs frown at appear (0.1)
    show ty at appear (-0.2)
    with fade
    "Tibbs strides quickly through the brush, ignoring the path as he moves in a straight line into the depths of the woods. His head is low as he mutters in hushed frustration under his breath."
    show tibbs at moveAndFlip(0.3,1)
    pause 1
    show tibbs at move(0.5,1)
    pause 1 
    show tibbs at move(0.8,1)
    show ty talk at moveAndFlip(0.25,0.5)
    pause 0.5
    ty "Ranger Tibbs! Wait!"
    show ty frown
    "But he doesn’t stop. Tibbs rips through the woods like a dog possessed, so fast that I can barely keep up with him."
    "Panic starts to wash over me as he moves deeper and deeper into the park. My words aren’t reaching him."

    

label endScene:
    m "This is the end"

