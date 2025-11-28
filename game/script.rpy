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

    def getRandomPageNoise():
        pageList = ["SFX_Book_1.ogg",
        "SFX_Book_2.ogg",
        "SFX_Book_3.ogg",
        "SFX_Book_4.ogg",
        "SFX_Book_5.ogg",
        "SFX_Book_6.ogg"]
        return random.choice(pageList)


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
    stop music fadeout 1
    #show screen emoteHandler
    jump scene_Intro
    #jump scene5
    

#----------------------------#
#---------TEST SCENES--------#
#----------------------------#

label testScene:
    $ persistent.dialogueBoxOpacity = 1.0
    scene bg registration
    show alby at appear(0.5)
    "start the thing"
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show alby
    "finish here"
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    "now flip"
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    
    

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

label testCG2:
    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg1 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg1 
    show cg1page2 zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg1page2 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

#----------------------------#
#---------MAIN SCENES--------#
#----------------------------#

label scene_Intro:
    $ persistent.dialogueBoxOpacity = 1.0
    scene bg black 
    with fade 
    queue sound2 ["SFX_DoorClose_3.ogg","SFX_ChairRoll_3.ogg","SFX_Chair_2.ogg","SFX_Book_1.ogg"]

    pause 4
    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    queue sound1 "SFX_Pen_3.ogg"
    show cg11 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    $ persistent.dialogueBoxOpacity = 0.0
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg11 at diaryMove(0.5,-1.0,2)
    with ease
    hide screen inputBlocker

    scene bg registration
    show dustin at appear(0.9)
    show alby behind dustin at appear(0.6)
    show ty at appearAndFlip(0.4)
    $ persistent.dialogueBoxOpacity = 1.0
    with fade
    play soundLoop1 "BGS_Forest_1.ogg" fadein 1.0 volume 0.5
    show dustin talk 
    du "I swear it’s really good! You gotta watch it!"
    show dustin 
    show alby talk
    play voice1 "Alby_Negative_1.ogg"
    al "That’s not what I keep seeing people say online."
    stop voice1
    show alby 
    show dustin talk frown 
    play voice1 "Dustin_Angry_2.ogg" volume 6.0
    du "You can’t get your anime opinions from video essays!"
    stop voice1
    show dustin frown 
    show alby talk at moveAndFlip(0.7,0.1)
    al "What about you, Ty? You ever watch this Sword Guys Online show?"
    show alby 
    show ty talk 
    play voice1 "Ty_Negative_1.ogg"
    ty "Can’t say that I have."
    stop voice1
    show ty 
    show dustin shock 
    du "It’s Sword ART Online. Art! And it’s great, I promise!"
    show dustin frown 
    show alby talk at moveAndUnFlip(0.7,0.1)
    al "Whatever you say, big guy."
    show alby at moveAndFlip(0.7,0.1)
    pause 0.2
    show alby talk 
    show tibbs at appearAndFlip(-0.3)
    show marsh behind tibbs at appear(-0.3)
    al "Yo, Ranger Tibbs! When’s the bossman gonna get here? I need him to save me from this talk about mid anime."
    show alby at move(0.75,0.5)
    show ty at moveAndUnFlip(0.6,0.5)
    show tibbs talk at move(0.1,1)
    play voice1 "Tibs_Frustrated_1.ogg"
    ti "We were supposed to start ten minutes ago, so I’m expecting him to show up about…"
    stop voice1
    show tibbs 
    ma "HEYYYY!!"
    show tibbs talk 
    ti "Now."
    show tibbs 
    show marsh at move(0.3,0.2)
    with ease
    "Marsh scrambles onto the scene, panting and heaving as he clutches his knees. Tibbs holds a clipboard out to him, and Marsh straightens up to take it."
    show marsh talk
    ma " Sorry I’m late! Okay! Let’s get today’s morning meeting underway!"
    show marsh 
    show tibbs talk 
    ti "I’ve already prepared the agenda for today. Most of it is about preparations for the upcoming fall season."
    show tibbs 
    show marsh talk 
    play voice1 "Marsh_Affirm_3.ogg"
    ma "I couldn’t have said it better myself, Tibbs!"
    stop voice1
    show marsh 
    show tibbs talk 
    ti "I know."
    show tibbs 
    show marsh talk 
    ma "Alright, let’s get started! Alby, how’s the gift shop looking?"
    show marsh 
    show alby talk
    al "All the new merch came in, but it’s still all boxed up. I’m gonna be cracking them open and stocking the shelves pretty much all day today."
    show alby 
    show marsh talk 
    ma "Awesome! Now for landscaping. With the leaves starting to change, we’re gonna have to stay on top of keeping the walkways clear once they start falling."
    show marsh 
    show dustin talk 
    du "Don’t remind me… We’re gonna be out there raking up leaves all season long. It’s endless!"
    show dustin 
    show tibbs talk
    play voice1 "Tibs_Interested_1.ogg"
    ti "Don’t you guys have a leafblower or two you can use?"
    stop voice1
    show tibbs 
    show alby talk 
    play voice1 "Alby_Laugh_1.ogg"
    al "Yeah, Dustin, what happened to the leafblower?"
    stop voice1
    show alby 
    show dustin talk frown 
    du "It’s, uh, out of commission"
    show dustin frown 
    show tibbs talk 
    play voice1 "Tibs_Sigh_1.ogg"
    ti "I’m not gonna ask. Just focus on keeping the paths clear."
    stop voice1
    show tibbs
    show dustin talk 
    play voice1 "Dustin_Affirm_1.ogg" volume 3.0
    du "You got it!"
    stop voice1
    show dustin 
    show marsh talk 
    ma "I’ll be working on scheduling for our upcoming events. That just leaves you, Tibbs. You’re handling arrivals today, right?"
    show marsh 
    show tibbs talk 
    ti "Yeah, we’ve got a few coming in that I’ll need to process."
    show tibbs 
    show marsh talk 
    ma "I’ll leave you to it, then. Alright, team! Let’s make today another spectacular day!"
    show marsh 
    show alby talk 
    al "Hear, hear, bossman!"
    show alby
    show dustin talk 
    du "Woohoo!"
    show dustin at moveAndFlip(1.3,1)
    show alby at moveAndUnFlip(1.4,1)
    show tibbs at moveAndUnFlip(-0.3,1)
    with None
    pause 0.1
    show dustin:
        xpos 1.3
    show alby:
        xpos 1.4
    show tibbs:
        xpos -0.3
    with dissolve
    show ty talk 
    ty "Um, Marsh? What should I do?"
    show ty 
    show marsh talk 
    ma "Oh, Ty! I almost forgot about you. Hmm… I think pretty much everything is handled. Why don’t you go ask around if anyone needs help with anything?"
    show marsh 
    show ty talk 
    play voice1 "Ty_Affirm_3.ogg"
    ty "Okay."
    stop voice1
    show ty
    "Marsh flashes the brightest of grins."
    show marsh talk
    ma "Today’s gonna be great!"

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg12 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    show marsh
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg12 
    show cg12page2 zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg12page2 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

    "Marsh taps his foot as he reads something off his clipboard. He sighs, then bites his lip."
    show ty talk 
    ty "Marsh? Is there a problem?"
    show ty frown at hop 
    show marsh shock
    ma "{size=*3}Problem?! Where?{/size}"
    show marsh frown 
    show ty talk 
    ty "Um…"
    show ty 
    show marsh talk 
    ma "Oh, um, no! There’s no problem. Everything’s fine."
    ma "We’ve got a long list of preparations to get through, but there won’t be any problems any step of the way. We’ve got this, right?"
    show marsh 
    show ty talk 
    ty "Um...right?"
    show ty 
    show marsh talk 
    ma "Right! Okay, good luck today! I’ll see you later, bye!"

    show marsh at move(-0.3,1.5)
    with None
    show marsh:
        xpos -0.3
    with dissolve
    "Marsh leaves in a hurry, and I find myself alone outside registration." 
    "It's pretty normal for him to struggle to find something for me to do, but with the ongoing preparations for the fall season, I feel especially useless doing nothing."
    "So I go searching for something to do."
    show ty at moveAndFlip (1.3,2)
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
    "But the first person I come across is the last person I expect to need help, let alone accept any."
    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg1 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    hide ty
    show tibbs zorder 50:
        xpos 0.65
    show camper1 zorder 50 at appear(0.35)
    with dissolve
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg1 
    show cg1page2 zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg1page2 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker
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
    gu "Okay, cool. Thanks for the help."
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
    play voice1 "Dustin_Greeting_3.ogg" volume 3.0
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
    play voice1 "Dustin_Deer_2.ogg" volume 9.0
    du "What’re you standing around for, Ty-guy? You’re looking like a deer in headlights."
    stop voice1
    show dustin 
    show ty talk 
    show tibbs at move(-0.2,2)
    ty "Don’t I always look like a deer?"
    show ty
    show dustin talk
    du "Don’t think too hard about it, buddy. Whatcha up to? Marsh working you ragged?"
    show dustin at move(0.75,0.5)
    show ty talk
    ty "He told me to ask around if anyone needed help."
    show ty
    show dustin talk
    du"Oh, epic! You can help me out. Here, take my phone! I wanna get a video of this!"
    show dustin 
    show phone at itemAppear(0.6,0.6,0.2)
    "Dustin shoves his phone into my hands before I can respond. He darts off, coming to a stop next to a large pile of leaves."
    show dustin at move (0.7,1)
    show phone at move (0.4,1)
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
    pause 0.4
    play sound1 "SFX_Leaves_Rustle_3.ogg"
    show dustin:
        pos (1.2,1.0)
    with hpunch 
    "Dustin does a full cannonball leap into the pile, scattering leaves into the wind. He rushes back to me, a brown leaf caught in the bushy fur of his wagging tail."
    stop sound1
    show dustin talk at move (0.65,1)
    with ease
    du "Lemme see, lemme see!"
    show dustin 
    show phone at move(0.5,0.2)
    play voice1 "Dustin_Laugh_1.ogg"
    "Dustin snatches his phone from my hands and watches the video I had recorded with the biggest of grins plastered over his face."
    stop voice1
    show ty talk
    ty"Aren’t you supposed to be cleaning up these leaves? Won’t Marsh get mad if he sees you making a mess?"
    show ty 
    show dustin talk
    show phone at itemDisappear(0.1)
    du"There’s, like, a bajillion trees around here! No one’s gonna notice if a pile or two hasn’t been raked up yet! Now, come on! Let’s get another vid!"
    show dustin

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg2 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg2 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker
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
    show screen inputBlocker
    show dustin at move(0.9,1)
    show ty at move(0.85,1)
    pause 1.0
    hide screen inputBlocker
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
    show dustin shock at appear(0.3)
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
    play voice1 "Dustin_Fluster_1.ogg" volume 8.0
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

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg3 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    hide ty
    hide gavin
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg3 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

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
    pause 2
    play sound1 "SFX_DoorOpen_3.ogg"
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
    show ty at move(0.15,1)
    show dustin at move(0.35,1)
    show alby at move(1.05,1)
    "We shuffle through the shop, finding Alby half-hidden within a maze of cardboard boxes full of new merchandise for the park’s fall season."
    show alby at jiggle(40,0.2,2)
    show dustin talk   
    play voice1 "Dustin_Frustrated_3.ogg" volume 5.0
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

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg4 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg4 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

    al "Yo, dudes! Check this out!"

    show dollBear at itemAppear(0.70,0.3,0.2):
        zoom 1.2
    "Alby whips out a small wooden figure of a bear that bears a striking resemblance to Marsh."
    show dollBear at jiggleVertical(20,0.2,0.5)
    show alby talk
    play voice1 "Alby_Hewwo_1.ogg"
    ma2 "Hewwo, hewwo, everyone! It’s me Marsh! Remember: littering is a crime, and criminals get fed to the bears!"
    stop voice1
    show alby
    show dollBear at move(0.70,0.1)
    show dustin talk
    du "Yo, dude, that's hilarious! Lemme try!"
    show dustin
    show dollBear at moveWithArc(0.45,-70,0.3)
    "Alby tosses the bear statue to Dustin before reaching back into the box he found it in."
    show dollBear at jiggleVertical(20,0.2,0.5)
    show dustin talk
    ma2 "Remember, campers! Feed the deer, you’re in the clear! Feed the bear? Get outta there!"
    show dollBear at reset()
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
    show dollWolf at jiggleVertical(20,0.2,0.5)
    du2 "Oh, Gavin! Kiss me! Kiss me like Naruto and Sasuke! Muah muah muah muah!"
    show dollWolf at reset()
    show alby
    show dollWolf at itemFight(-60)
    show dollBadger at itemFight(60)
    "Alby smashes the two statues together over and over, so much so that I’m afraid he’s going to damage the wood. Dustin is less than amused."
    
    show dustin talk frown
    play voice1 "Dustin_Negative_2.ogg"
    du "I would NOT say that!"
    stop voice1
    show dustin shock
    show dollWolf at reset()
    show dollBadger at reset()
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
    play voice1 "Alby_Character_1.ogg"
    al "You have to feel the character. Become the character! Think not what to say, but what Tibbs would say in this very moment."
    stop voice1
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
    du "It’s time for my secret technique! Hyaah!!"
    show dustin frown at jiggleVertical(60,0.11,0.8)
    show alby at albyFuckingDies()
    play voice1 "Alby_Laugh_1.ogg"
    "Dustin assaults Alby with a flurry of foamy strikes that send the larger skunk into a laughing fit as he doubles over on the floor."
    stop voice1
    hide alby
    show dollDog at itemAppear(0.25,0.4,0.2)
    "As Dustin continues to attack Alby with flashy, impractical sword attacks, I find myself looking down at the canine figure in my hands, thinking about Tibbs."
    
    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg5 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    hide ty
    hide alby 
    hide dustin
    hide dollDog
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg5 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker


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
    al "Have you considered he might be Medusa’s long lost cousin? Hsssss!"
    show alby 
    show dustin talk frown 
    du "Not helping, man."
    show dustin frown
    show alby talk 
    al "Okay, but for real. Maybe try finding a group setting to talk to him in. Have a buffer with you so you can default to them if things go south."
    show alby 
    show dustin talk frown 
    du "How are we gonna do that? He’s just a contractor, so he doesn’t come to any staff meetings."
    show dustin frown 
    show alby talk
    al "Dude, Marsh throws a holiday party like three times a month. We can just invite him to one of those. I can shmooze him up with you and then dip once you’re comfortable."
    show alby
    show dustin talk 
    play voice1 "Dustin_Interest_2.ogg"
    du "That might actually work, huh...."
    stop voice1
    show dustin 
    show alby talk
    al "See? I know what I’m talking about. You can leave all your puppy love problems to me. What about you, Ty? You get any surprise arrows from Cupid lately?"
    show alby 
    show ty talk
    play voice1 "Ty_Confusion_2.ogg"
    ty "Arrows?"
    stop voice1
    show ty
    show alby talk
    al "You know, like Dustin’s got his little crush on the electrician, but what about you? Do you liiiiike anyone?"
    show alby 
    "I blink back at two overly expectant faces looming ever closer to me, their careful eyes scanning my expression for any hint of embarrassment."
    show ty talk
    play voice1 "Ty_YouGuys_1.ogg"
    ty "I like you guys."
    stop voice1
    show ty
    "Based on their reactions, that wasn't the answer they were looking for."
    show alby talk
    play voice1 "Alby_Surprise_2.ogg"
    al "Aw, shucks, little bud. I'm flattered. I like you too."
    stop voice1
    show alby
    show dustin talk frown
    du "I can’t be the only one dealing with a hopeless crush at work, can I?"
    show dustin 
    show alby talk 
    play voice1 "Alby_Pining_1.ogg"
    al "I’m certainly not pining after any hunkies or honies right now. Don’t think I can say the same about Tibbs, though."
    stop voice1
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
    play voice1 "Alby_Read_1.ogg"
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

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg6 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    hide dustin 
    hide ty 
    hide alby
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg6
    show cg6page2 zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg6page2 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker
    stop soundLoop1 fadeout 2

    jump scene3

label scene3:
    scene bg campsite
    with fade
    pause 0.2
    show alby  at appear(1.3)
    show dustin  at appear(1.2)
    show ty at appearAndMove(0.7,0.5,1)
    with dissolve

    pause 2
    show marsh frown at appear(-0.2)
    show marsh talk frown at move(0.1,0.2)
    with dissolve
    ma "Ty! TY!! Where’s Dustin and Alby? We’ve got a problem!"
    play music1 "DEER DIARY - Panik2.ogg" fadein 1
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
    ma "There you are! There’s an emergency! A camper just got reported missing!"
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
    show tibbs at appearAndFlip(-0.25)
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
    show tibbs talk frown 
    play voice1 "Tibs_Frustrated_1.ogg"
    ti "Let’s not jump to any conclusions. We’ll put together a search party."
    stop voice1
    show tibbs frown 
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
    play voice1 "Alby_Sad_2.ogg"
    al "Come on, bossman. Let’s see if we can get you a paper bag."
    stop voice1
    show marsh frown at move(0.25,cameraTime) 
    show tibbs frown at move(0.6,cameraTime) 
    show camper2 worried at move(1.2,cameraTime) 
    show ty frown at move (1.25,cameraTime)
    show alby at move (0.2, cameraTime)
    show dustin frown at move (1.6, cameraTime)
    with ease
    pause cameraTime
    show alby at moveAndUnFlip(0.1,0.2)
    show tibbs talk at moveAndUnFlip (0.6,0.1)
    ti "Hey."
    show screen emoteHandler
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
    #show removeThis
    pause 0.05 
    #hide removeThis
    #the others coe in
    "Alby holds his hand up to his face as if to block it from Marsh’s view. He silently mouths to me and Dustin “secret lovers”."
    hide screen emoteHandler
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
    show marsh at move(-0.3,1)
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
    stop music1 fadeout 2
    "But at the same time…"

    jump scene4

label scene4:
    "Darkness is quickly falling over the park. My own antlers cast a shadow that stretches out across the grass, reaching out to Tibbs as he strides singlemindedly toward the forest."
    "He'll be fine, right?"
    "No. I’ve got to follow him. I don’t care how competent he is; Tibbs shouldn’t go out into the forest in the dark."
    #journal time

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg7 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    hide ty
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg7 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

    
    scene bg forest deep
    play soundLoop1 "BGS_Forest_1.ogg" fadein 1
    show tibbs frown at appear (0.1)
    show ty frown at appear (-0.2)
    with fade
    "Tibbs strides quickly through the brush, ignoring the path as he moves in a straight line into the depths of the woods. His head is low as he mutters in hushed frustration under his breath."
    show tibbs frown at moveAndFlip(0.3,0.5)
    pause 1
    show tibbs frown at move(0.5,0.5)
    pause 1
    show tibbs frown at move(0.8,1)
    show ty talk frown at moveAndFlip(0.25,0.5)
    pause 1

    play voice1 "Ty_RangerTibbs_1.ogg"
    ty "Ranger Tibbs! Wait!"
    stop voice1
    show ty frown
    "But he doesn’t stop. Tibbs rips through the woods like a dog possessed, so fast that I can barely keep up with him."
    show tibbs frown at move(1.3,0.6)
    "Panic starts to wash over me as he moves deeper and deeper into the park. My words aren’t reaching him."
    show ty talk frown 
    ty "R-Ranger Tibbs! Please, wait!"
    show ty frown at move(1.2,0.8)
    pause 0.8
    scene bg black
    with fade
    "Shadows meld into the encroaching night, but Tibbs carries on. I’ve given up on getting through to him, resigned to silently follow him. It’s just about all I can do."
    scene bg forest deepdark
    show tibbs frown at appearAndFlip(0.7)
    show ty frown at appearAndFlip(-0.2)
    with fade
    pause 0.2
    "And then, suddenly, he stops. Tibbs sighs with a breath so heavy it was as if he had been holding it in the entire time."
    show ty frown at move(0.2,0.5)
    pause 0.6
    show tibbs frown at moveAndUnFlip(0.7,0.1)
    "A twig snaps under my foot, and Tibbs spins on his heel to face me."
    play voice1 "Tibs_Confused_1.ogg"
    show tibbs talk frown 
    ti "Wh—Ty? What are you doing here?"
    stop voice1
    show tibbs 
    show ty talk frown 
    ty "I followed you. It’s not safe to go out alone into the park at night."
    show ty frown 
    "Tibbs' face flushes"
    show tibbs talk 
    ti "Ah, yeah. I guess it was closer to sundown than I thought. Damn it, I was so worked up I didn’t even notice you tailing me."
    show tibbs 
    show ty talk frown 
    ty "I’ve never seen you so anxious before."
    show ty frown 
    show tibbs smile
    "Tibbs laughs with a wry smile."
    show tibbs talk frown 
    ti "It’s not really like me, is it? Letting some little issue get to me like this. You’d think I’d have a more level head about these things."
    show tibbs frown 
    show ty talk frown
    ty "You usually do."
    show ty frown
    show tibbs talk frown 
    ti "Yeah."
    show tibbs frown 
    "Tibbs rubs his neck, a distant look on his face."
    show tibbs talk 
    ti "How long have you been working at the park for again?"
    show tibbs 
    show ty talk 
    ty "Just a few months."
    show tibbs talk 
    show ty
    play voice1 "Tibs_Sigh_1.ogg"
    ti "Then you haven’t seen what this place used to be like. It’s bounced back since last summer, but the town and the park used to be on the verge of closing down for good."
    stop voice1
    show tibbs 
    show ty talk frown 
    ty "I remember Marsh mentioning something like that before."
    show ty frown 
    show tibbs talk 
    ti "You have him to thank for patching the campground up. He cares a whole lot about this place, and when I first started here, he taught me to care, too. I owe a lot to him."
    show tibbs 
    "I can barely hide my shock. Marsh and Tibbs have always felt so different from one another. To think that they connected in such a way… It makes me feel like our distant worlds aren’t actually so far apart."
    show ty talk 
    ty "Is that why you’re so anxious to find this person?"
    show ty 
    show tibbs talk frown 
    ti "The park is no stranger to bad press."
    ti "Before Marsh came along, there were quite a few missing person cases, enough to drive people away from this place. Imagine what would happen if those cases started cropping up again."
    show tibbs frown 
    show ty talk 
    play voice1 "Ty_Sad_1.ogg"
    ty "People would start leaving."
    stop voice1
    show ty 
    show tibbs talk frown 
    #italics required on the "will"
    ti "And all of Marsh’s hard work would be for nothing. I can’t let that happen. We will find this person. We have to."
    show tibbs frown 
    "The intense expression on Tibbs’ face is not like the one he usually bears. There’s a passion behind his eyes."
    show ty talk at move(0.25,0.5)
    ty "I understand, but we can’t just go running through the dark to find them."
    show ty 
    show tibbs 
    ti " Yeah, you’re right. I…got ahead of myself. Let’s head back and regroup."
    show tibbs at lookAround(3,-1)
    pause 1
    "Tibbs looks left and right"
    show tibbs talk frown at moveAndUnFlip(0.7,0.1)
    ti "Hold on…where are we?"
    show tibbs 
    show ty talk frown 
    ty " I ran so fast to find you that I wasn’t paying attention to the direction we were going."
    show ty frown 
    show tibbs talk 
    ti "I thought I was headed for the river, but…I don’t recognize this part of the woods."
    show tibbs at lookAround(2, 1)
    show ty at lookAround(2,-1)
    pause 3
    show tibbs talk frown at moveAndUnFlip(0.7,0.1)
    show ty frown at moveAndFlip(0.25,0.1)
    play voice1 "Tibs_Angry_1.ogg"
    ti "Shit! We’re lost, and we’re losing sunlight fast."
    stop voice1
    show tibbs frown 
    show ty talk 
    ty "If we can find the river, then we can follow it back to camp."
    show ty 
    show tibbs talk
    ti "Yeah, you’re right. I’ll lead the way."
    show tibbs at moveAndFlip (0.8,0.3)
    "Lost or not, Ranger Tibbs will get us through this. With his skills, he’ll get us back to camp in no time flat."
    show tibbs at lookAround(1,-1)
    pause 0.5
    show tibbs at moveAndFlip(0.8,0.1)
    "Tibbs scans the area, squinting at the growing darkness. He frowns."
    play voice1 "Tibs_Interested_1.ogg"
    ti "HMM"
    stop voice1
    show ty talk 
    ty "Is something wrong?"
    show ty 
    show tibbs at moveAndUnFlip(0.7,0.3)
    pause 0.3
    show tibbs talk 
    ti "Marsh always says that you can tell when you’re by the river when you can see a certain kind of tree. It’s got these, like, droopy things growing on it."
    show tibbs 
    show ty talk
    ty "Droopy things? You mean catkins?"
    show ty 
    show tibbs talk frown 
    ti "Yes! Catkins! If we can find a tree with those growing on it, we’ll know we’re close to the river."
    show tibbs 
    show ty talk frown 
    ty "But...catkins grow in the spring."
    show ty frown 
    show tibbs talk frown 
    ti "Huh?"
    show tibbs frown 
    show ty talk
    ty "Is the tree you’re looking for a Lincoln Alder?"
    show ty 
    show tibbs talk 
    ti "Oh! Yeah, that’s the one. I swear I can never remember the name no matter how many times Marsh talks about it."
    show tibbs 
    show ty talk
    ty "Well, the Lincoln Alder flowers in the spring. That’s when the catkins grow on it. The tree won’t have any on it in the fall."
    show ty 
    show tibbs talk
    ti "You really know your stuff."
    show tibbs 
    show ty talk 
    ty "Don't you?"
    show ty 
    "A hint of embarrassment shows on Tibbs’ face, but he quickly shakes it away."
    show tibbs talk 
    ti "I-I must’ve forgotten. If you know how to identify this alder, then you should lead the way."
    show ty talk
    show tibbs 
    play voice1 "Ty_Surprise_2.ogg"
    ty "M-me?"
    stop voice1
    show ty frown 
    show tibbs talk 
    ti "Of course. It sounds like you’re the expert, so I’m leaving it to you."
    show tibbs 

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg8 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    hide ty
    hide tibbs
    show bg black
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg8
    show cg8page2 zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show cg8page2 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

    play soundLoop1 "BGS_ForestStream_3.ogg" volume 0.2 fadein 2
    ti "The river! And just in time, too. Let’s follow it back to the campground."
    ty "Wait for me!"
    "We hurry back, following the coastline until finally, the registration building comes into view."
    stop soundLoop1 fadeout 2
    jump scene5

label scene5:
    scene bg registration sunset
    play soundLoop1 "BGS_Forest_1.ogg" volume 0.5 fadein 1
    with fade
    show marsh at appear(-1.8)
    show ty at appear (1.4)
    show tibbs behind ty at appear (1.3)
    ma "TIIIIIIBBBBBBSSSS!!!"
    show tibbs at move(0.55,2)
    show ty at move(0.8,2)
    pause 1
    show marsh at move(0.45,1)
    pause 1.0
    show marsh at jiggle(50,0.1,0),moveWithVertical(0.45,1.3,0.2)
    show tibbs frown at jiggle(50,0.1,0),moveWithVertical(0.55,1.3,0.2)
    pause 0.2 
    show marsh at reset(),moveWithVertical(0.45,1.3,0.2)
    show tibbs frown at reset(),moveWithVertical(0.55,1.3,0.2)
    "Marsh nearly topples Tibbs onto the ground with a running tackle. The ranger only barely manages to recover, but the big bear clings to him in a tight hug."
    show marsh talk
    ma "I thought you were gonna go missing, too!!"
    show marsh at moveWithVertical(0.25,1.0,0.2)
    show tibbs talk at moveWithVertical(0.55,1.0,0.4)
    show ty at move(0.9,0.5)
    ti "I’ve been gone, like, an hour at most."
    show alby at appearAndFlip(1.5)
    show dustin at appear(1.3)
    du "There you are!"
    show tibbs at move(-0.35,1.1)
    show marsh at move(-0.45,1)
    show ty at moveAndFlip(0.3,1)
    show dustin talk at move (0.6,1)
    show alby at move (0.8,1)
    du "We were looking all over for you, Ty!"
    show dustin 
    show ty talk
    ty "You were?"
    show ty smile 
    show alby talk 
    al "We thought you were right behind us, little man. Where’d you go?"
    show alby 
    show ty talk 
    ty "I, um, went with Ranger Tibbs to look for the missing camper."
    show ty smile 
    show dustin talk frown 
    du "With Tibbs?! You went with Tibbs?!"
    show dustin 
    show alby talk 
    al "How’d you build up the guts to do that?"
    show alby 
    show ty talk 
    ty "I’m…not sure. I just didn’t think he should be searching on his own."
    show ty 
    show alby talk 
    al "Your bravery is unmatched, little man. I’ve got some good news for you, though. The camper found his way back to registration a little while ago."
    show alby 
    show ty talk 
    ty "Really? That's great!"
    show ty smile 
    ti "Did I hear that right? Our missing person is safe?"
    show ty smile at moveAndUnFlip(0.45,1)
    show dustin at move (0.7,1)
    show alby at move(0.9,1)
    show marsh at move(0.1,1)
    show tibbs at moveAndFlip(0.25,1)
    pause 1.0
    show alby talk
    al "Sure is"
    show alby 
    show tibbs talk
    ti "What a relief."
    show tibbs smile
    show alby talk 
    al "The dude was looking for the river, but he somehow ended up going the complete opposite way."
    al "Not sure how that happened. He said he asked two different camp employees for directions."
    show dustin shock
    play voice1 "Dustin_Fluster_1.ogg" volume 8.0
    du "Uh, yeah, that’s so weird! Wonder who he talked to."
    stop voice1
    "Tibbs clears his throat"
    show tibbs talk 
    show dustin
    ti "We’ll have to, uh, have a staff meeting about the local geography. We can’t have park employees misdirecting our campers."
    show tibbs 
    show marsh talk 
    play voice1 "Marsh_Affirm_3.ogg"
    ma "That’s a great idea!"
    stop voice1
    show tibbs talk 
    show marsh
    ti "And, Ty, would you like to lead it?"
    show tibbs 
    show dustin shock 
    show alby
    show ty talk 
    play voice1 "Ty_Surprise_1.ogg" 
    ty "Me?"
    stop voice1
    show ty smile
    show alby talk
    dual "Him?!"
    show dustin 
    show alby
    show tibbs talk
    show ty smile
    ti "It was your knowledge of the land that helped us return safely. I bet you could teach everyone here a thing or two about navigating the park."
    show tibbs 
    show dustin talk 
    play voice1 "Dustin_Interest_1.ogg" volume 2.0
    du "Wait, really?!"
    stop voice1
    show dustin 
    show alby talk 
    al "Well, I'll be! Way to go, little guy!"
    show alby 
    "My cheeks burn as Alby ruffles my hair. Dustin gives me a firm clap on the back."
    show ty talk 
    ty "I'd be honored."
    show ty smile 
    show tibbs talk 
    ti "We’ll add it to the agenda."
    show tibbs
    show dustin talk 
    du "Woohoo!"
    show dustin 
    show alby talk 
    al "Alright, I think we’ve had enough excitement for the day. It’s time we started closing up shop."
    show alby 
    show tibbs talk 
    ti "I couldn't agree more."
    show tibbs behind marsh
    show marsh talk 
    ma "Anyone hungry? Let’s all meet up at the Honey Pot for dinner!"
    show marsh 
    show dustin talk 
    du "Hell yeah!!"
    show dustin 
    show alby talk 
    al "You read my mind, bossman."
    show alby 
    pause 0.1
    define moveSpeed=1
    show alby at moveAndUnFlip(1.4,moveSpeed)
    show dustin at moveAndFlip(1.2,moveSpeed)
    show marsh at move(1.3,moveSpeed)
    show ty at moveAndFlip(0.8,moveSpeed)
    pause moveSpeed
    show tibbs talk 
    ti "Hey, um, before you go."
    show ty at moveAndUnFlip(0.75,0.2)
    pause 0.2
    show ty talk
    ty "Yeah?"
    show ty 
    show tibbs talk 
    ti "I just wanted to thank you properly for getting us back safely."
    show tibbs smile 
    show ty talk 
    ty "Oh! I-it was nothing."
    show ty smile 
    show tibbs talk 
    ti "You jumped into action and kept a level head in a crisis. That’s a whole lot more than nothing. You know, you would make a pretty good park ranger. Better than me, anyway."
    show tibbs smile 
    stop soundLoop1 fadeout 1
    play music "DEER DIARY - Empathy -Two One Another-.ogg" fadein 1
    "Better than me..."
    "My mouth hangs open in shock at Tibbs’ words. Better than him? Me? I’d never put myself on the same level as someone like Tibbs, let alone above him."
    "And yet…hearing that from him gives me a little bit of courage. Just enough to share my dream with Ranger Tibbs."
    show ty talk 
    ty "That’s actually been a goal of mine. I want to be a park ranger just like you."
    show ty smile 
    show tibbs talk 
    ti "Like me? Ha ha…"
    show tibbs smile
    "Tibbs lets out a long, sardonic laugh."
    show tibbs talk
    ti "You don’t want to be like me."
    show tibbs 
    show ty talk 
    ty "Huh? Why not?"
    show ty 
    show tibbs 
    show cg9
    with dissolve
    ti "It’s a long, complicated story. But to make it brief, I messed up."
    ti "My last job didn’t go so well, and this was just about the only assignment that would take me."
    ty "I didn’t know that."
    ti "I try not to talk about it much."
    ti "I used to think having to work this job was the end of the world. I put all that baggage on Marsh and nearly made everything worse for both of us."
    ti "I might look like I’ve got everything under control, but I’ve made my fair share of mistakes. Heh, today’s pretty good evidence of that."
    ti " You can’t be perfect all the time. If we could, then I wouldn’t even be here."
    "Tibbs looks off towards the sunset, his eyes distant."
    "All this time, I’ve been thinking of Tibbs as this untouchable image of the perfect park ranger. But when he turns back to me, he steps off that pedestal and looks at me as an equal."
    ty "Tibbs, I’m glad you made that mistake."
    "Tibbs grimaces, and my brows shoot up as I realize what I just said."
    ty "What I mean is: I’m glad you’re here."
    ti "To be honest, it’s nice to have someone like you around, too."
    ty "R-really?"
    ti "You’re smart, resourceful, and a hell of a lot easier to deal with than the rest of those knuckleheads. And after today, I know that you’re dependable, too."
    ti "One day, when I eventually move on…I know the park will be left in capable hands."
    "A warmth fills my chest, bringing a smile to my face that refuses to leave."
    ty "I’ll do my best."
    hide cg9
    with dissolve
    pause 0.5
    show ty at moveAndFlip(0.75,0.1)
    du "Hey, guys! Are you coming or what?"
    "We turn towards the rest of the crew, where Dustin bounces up and down while waving his arms."
    show ty talk at moveAndUnFlip(0.75,0.1)
    ty "Do you want to join us?"
    show ty 
    show tibbs talk  
    ti "I’ve, uh, actually got somewhere to be and…"
    show tibbs 
    show ty frown 
    "Tibbs trails off as he stares into my wide, pleading eyes."
    show tibbs talk
    show ty smile 
    ti "Ah, what the hell. I’ll get a coffee or something."
    show tibbs smile at move (1.3,2) 
    show ty smile at moveAndFlip(1.5,2)
    with None
    jump sceneCreditsFake

label sceneCreditsFake:

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg10 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg10
    show c10EndDoodle zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show tyWriting at cgTyDisappear(2)
    show c10EndDoodle at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker
    jump sceneEnd

label sceneCredits:

    show table zorder 10 onlayer AboveEverything
    show darkeningLayer zorder 150 onlayer AboveEverything
    with dissolve
    show screen inputBlocker
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show cg10 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    show tyWriting zorder 200 onlayer AboveEverything at cgTyAppear(0.5,0.5,3)
    pause 4
    show continueButton zorder 200 onlayer AboveEverything
    #below scene code goes here
    #below scene code ends here
    hide screen inputBlocker
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg10
    show c10EndDoodle zorder 100 onlayer AboveEverything
    with dissolve
    pause 1 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    hide continueButton
    show tyWriting at cgTyDisappear(2)
    show c10EndDoodle at diaryMove(0.5,-1.0,2)
    pause 2
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg10 
    show cg10page2 zorder 100 onlayer AboveEverything at diaryAppear(0.5,0.5,4)
    with dissolve
    pause 4 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg10page2 
    show cg10page3 zorder 100 onlayer AboveEverything
    with dissolve
    pause 2 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg10page3 
    show cg10page4 zorder 100 onlayer AboveEverything
    with dissolve
    pause 2 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    hide continueButton
    show screen inputBlocker
    hide cg10page4 
    show cg10page5 zorder 100 onlayer AboveEverything
    with dissolve
    pause 2 
    hide screen inputBlocker
    show continueButton zorder 200 onlayer AboveEverything
    ""
    $ renpy.play(getRandomPageNoise(),channel="sound1")
    show screen inputBlocker
    hide continueButton
    hide table
    hide darkeningLayer
    with dissolve
    show cg10page5 at diaryMove(0.5,-1.0,2)
    with ease
    pause 2.0
    hide screen inputBlocker

    scene bg black 
    with fade
    jump sceneEnd

label sceneEnd:
    scene bg black
    with fade