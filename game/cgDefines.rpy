#IMAGES
image blackScreen = "blackScreen.png"
image journalBase = "CGs/journal cg 2.webp"

image cg1Text = Text("   Ranger Tibbs is everything I aspire to be\n and more! He keeps our little campground \noperation running like a well-oiled machine. \n\n\n   Marsh might be the leader and the heart \nof our group, but Tibbs is absolutely the \nbrains. He’s smart, cool, competent, and \nwith a wit as sharp as a knife! ",slow=None)
image cg1Page2Text = Text("  But, unfortunately, that’s exactly why I \nfind it so hard to approach him. I want a \nchance to talk to him about his career, \nbut he’s the spitting image of the perfect \npark ranger, and I’m just the intern. \n\n\n   We’re in totally different worlds, and I’m \nnot so sure he’s got the time to waste \non someone like me. \n\n\n   Needless to say, I decided against \nasking Tibbs if he needed any help today \nbecause he’s Tibbs! He’s got everything \nhandled.")
image cg2Text = Text("I can’t help but envy Dustin sometimes. \nHis boundless energy and upbeat \npersonality just draws everyone to him. \nHe’s the life of any party, and striking up \nconversations comes naturally to him. \nHe even manages to pull me into the \nconversation with ease. \n\nThe way he manages to befriend anyone \nhe meets almost feels like a superpower \nto me.")
image cg3Text = Text("I’m gonna level with you, journal, \nI don’t really know much about Gavin. \nHe’s only at the park when he needs to be, \nand when he does come around he keeps \nto himself. \n\nHe seems nicer than he looks, though.")
image cg4Text = Text("Alby is one of the oldest employees at \nBreak Trail, and he’s got the experience to \nshow for it. Dustin is always asking for \nhis advice on just about everything. \n\nI’ve even caught Marsh occasionally leaning \non him from time to time. Whatever the \nproblem, Alby’s got the solution. \n\nI can only hope to one day be as wise and \nresourceful as he is.")
image cg5Text = Text("Stepping into the shoes of someone who \nhas already achieved everything I set out \nto do… The idea feels impossible to me. \n\nTibbs is a fully realized park ranger, a man \nliving the life I’ve only dreamed of. I’m still \ntoo green to even see myself in that role, \nlet alone act it out. I’m still just clay \nwaiting to be molded, or wood waiting to \nbe carved. \n\nAnd I can’t help but wonder…when that \nday comes when I feel complete, will I \nlook like this little wooden Tibbs? \nThese thoughts followed me all morning, \neven as Dustin and Alby treated me \nto lunch at the Honey Pot.")
image cg6Text = Text("I want nothing more than to talk to Tibbs \nabout his position as a park ranger. I want \nto ask him all these questions about his \nexperience and his responsibilities—heck—\nmaybe even shadow him for a day. But \nTibbs is like a stone wall. \n\nHe doesn’t stick around long, and when he \ndoes, he doesn’t leave himself open for \nsmall talk. \n\nToday, while talking about how tough it is \nto get through to him, I felt my stomach \ntwisting in knots just thinking about \nbuilding up the courage to attempt it.")
image cg6Page2Text = Text("Little chances popped up throughout the \nday, moments where I had little exchanges \nwith Ranger Tibbs. They were always brief \nand always about work, usually about \nMarsh’s whereabouts. \n\nEvery time, I felt myself lingering on my \nwords, silently debating if there was time \nto say more. Tibbs was always gone before \nI could make any second guesses. \n\nBut as the sun started to hang low in an \nincreasingly orange sky, an opportunity I \nwould have never expected arose. There \nwas an emergency at the campground.")
image cg7Text = Text("Thinking back, I don’t know where I found \nthe courage to make that decision. \nWhenever I run through the events of this \nevening in my head, I see myself following \nAlby and Dustin over and over again. \n\nBut I didn’t! I saw what I needed to do \nand acted on it before my bravado could \npass. I chased Ranger Tibbs into the \nwoods as fast as my legs could take me.")
image cg8Text = Text("")
image cg8Page2Text = Text("I couldn’t believe it! I thought I’d just be \nfollowing Ranger Tibbs’ lead, but he \nwanted me to take charge! \n\nTo have someone like him rely on me, it \ngave me a rush I couldn’t even begin to \ndescribe. With my knowledge of the local \necology, we reached the river in record \ntime.")
image cg10Text = Text("Since I started my internship at \nBreak Trail, I’ve always seen the other \nstaff members as something a little bit \nbigger than they are. As the newbie, I’ve \nalways seen them as the people I need to \nrely on. I never once thought that any \nof them would come to rely on me.")
image cg10Page2Text = Text("But after today, I know that’s not true. \nI have something to give to this \ncommunity, so I’m going to give it my all. \n\nIt starts with this presentation at our \nstaff meeting, but tomorrow I’m going to \nstart asking Marsh and Tibbs what else I \ncan do to make Break Trail the best \ncampground it can be.")
image cg11Text = Text("Dear diary,\n\nI can barely contain my excitement! \nSorry if my handwriting is shaky, but I can \nhardly wait to tell you about my day. \n\nMost days at my new internship have been \npretty uneventful. My boss usually just \nhas me doing busywork or helping out \nsome of the staff at the campground. \n\nToday was supposed to be no different, \nbut it ended up being a day I don’t think \nI’ll ever forget.")
image cg12Text = Text("Marsh is more than just my boss. He’s the \nmanager of the entire campground. It’s a \nhuge responsibility to take on, and he \nused to handle it all by himself! \n\nMarsh was the one who revitalized this \nplace when it was on the verge of being \nclosed down, but little by little, he built up \na community in this place until it became \nthe campground it is today.")
image cg12Page2Text = Text("Some call him the heart of Camp \nMarshmallow, and whenever he greets the \nmorning with a smile, you can feel that \nheart beating. No matter what happens, \nMarsh is always there to brighten our days.")

image ty cg= "CGs/ty desk cg 2.webp"
image border="ty desk cg border.webp"
image darkeningLayer = "CGs/darkenedLayer.webp"
image table = "CGs/CGTable.webp"
image continueButton:
    "continueMarker.webp"
    pause 1.0 
    alpha 0.0
    pause 0.5 
    alpha 1.0
    repeat
    
image tyWriting=Composite(
    (1920,1080),
    (0,0), "border",
    (0,0), "ty cg",
    (0,20), "writing1",
    (-150,0), "writing2"
)

#comic panels
image comic1 = "CGs/SW panel 1.webp"
image comic2 = "CGs/SW panel 2.webp"
image comic3 = "CGs/SW panel 3.webp"
image comic4 = "CGs/SW panel 4.webp"
image comic5 = "CGs/SW panel 5.webp"
image comic6 = "CGs/SW panel 6.webp"
image comic7 = "CGs/SW panel 7.webp"
image comic8 = "CGs/SW panel 8.webp"
image comic9 = "CGs/SW panel 9.webp"
image comic10 = "CGs/SW panel 10.webp"
image comic11 = "CGs/SW panel 11.webp"
image comic12= "CGs/SW panel 12.webp"
image comic13= "CGs/SW panel 13.webp"
image comic14= "CGs/SW panel 14.webp"
image comic15= "CGs/SW panel 15.webp"
image comic16= "CGs/SW panel 16.webp"
image comic17= "CGs/SW panel 17.webp"


#DOODLES 
image tibbsDoodle = "CGs/journal doodle tibbs.webp"
image dustinDoodle = "CGs/journal doodle dustin.webp"
image gavinDoodle = "CGs/journal doodle gavin.webp"
image albyDoodle = "CGs/journal doodle alby.webp"
image tyDoodle = "CGs/journal doodle ranger ty.webp"
image tyDoodle2 = "CGs/journal doodle cant talk.webp"
image tyDoodle3 = "CGs/journal doodle run.webp"
image marshDoodle = "CGs/journal doodle marsh.webp"
image dollDoodle = "CGs/journal doodle statue.webp"
image leaveDoodle = "CGs/journal doodle leave.webp"
image endDoodle1 = "CGs/credits 1.webp"
image endDoodle2 = "CGs/credits 2.webp"
image endDoodle3 = "CGs/credits 3.webp"
image endDoodle4 = "CGs/journal doodle the end.webp"
image endDoodle5 = "CGs/credits 4.webp"

#ANIMATED IMAGES
image writing1:
    "writing1_1.png"
    pause 1
    "writing1_2.png"
    pause 1
    "writing1_3.png"
    pause 1
    repeat

image writing2:
    "writing2_1.png"
    pause 1.1
    "writing2_2.png"
    pause 1.1
    "writing2_3.png"
    pause 1.1
    repeat

#Misc
image personaCutIn = "CGs/dustinCutIn.webp"

#THE ACTUAL CGs

image cg1 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tibbsDoodle",
    (1100,100), "cg1Text"
)

image cg1page2 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tibbsDoodle",
    (1100,100), "cg1Page2Text"
)

image cg2 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "dustinDoodle",
    (1100,100), "cg2Text"
)


image cg3 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (80,-30), "gavinDoodle",
    (1100,100), "cg3Text"
)

image cg4 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "albyDoodle",
    (1100,100), "cg4Text"
)

image cg5 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tyDoodle",
    (0,0), "dollDoodle",
    (1100,100), "cg5Text"
)

image cg6 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tyDoodle2",
    (1100,100), "cg6Text"
)

image cg6page2 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tyDoodle2",
    (1100,100), "cg6Page2Text"
)

image cg7 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tyDoodle3",
    (1100,100), "cg7Text"
)

image cg8 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "leaveDoodle",
    (1100,100), "cg8Text"
)

image cg8page2 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tibbsDoodle",
    (1100,100), "cg8Page2Text"
)

image cg9 = "CGs/tibbs cg.webp"

image cg10 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (350,100), "cg10Text",
    (1100,100), "cg10Page2Text"
)

image c10EndDoodle = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "endDoodle4"
)

image cg10page2 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (350,100), "cg10Text",
    (1100,100), "cg10Page2Text"
)

image cg10page2 = Composite(
    (1920,1080),
    (0,0), "endDoodle1"
)

image cg10page3 = Composite(
    (1920,1080),
    (0,0), "endDoodle2"
)

image cg10page4 = Composite(
    (1920,1080),
    (0,0), "endDoodle3"
)

image cg10page5 = Composite(
    (1920,1080),
    (0,0), "endDoodle5"
)

image cg11 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (1100,100), "cg11Text"
)

image cg12 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "marshDoodle",
    (1100,100), "cg12Text"
)

image cg12page2 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "marshDoodle",
    (1100,100), "cg12Page2Text"
)

