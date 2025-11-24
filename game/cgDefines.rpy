#IMAGES
image blackScreen = "blackScreen.png"
image journalBase = "CGs/journal cg 2.webp"
image cg1Text = Text("Ranger Tibbs is everything I aspire to be \nand more! \nHe keeps our little campground operation \nrunning like a well-oiled machine. \nMarsh might be the leader and the heart of \nour group, but Tibbs is absolutely the \nbrains. He’s smart, cool, competent, and \nwith a wit as sharp as a knife! \nBut, unfortunately, that’s exactly why I \nfind it so hard to approach him. \nHe’s the spitting image of the perfect \npark ranger, and I’m just the intern. \nWe’re in totally different worlds, and I’m \nnot so sure he’s got the time to waste on \nsomeone like me.\nNeedless to say, I decided against asking \nTibbs if he needed any help today because \nhe’s Tibbs! He’s got everything handled.",slow=None)
image cg2Text = Text("I can’t help but envy Dustin sometimes. \nHis boundless energy and upbeat \npersonality just draws everyone to him. \nHe’s the life of any party, and striking up \nconversations comes naturally to him. \nHe even manages to pull me into the \nconversation with ease. \nDustin really does have the power to \nbefriend anyone he wants.")
image cg3Text = Text("I’m gonna level with you, journal, \nI don’t really know much about Gavin. \nHe’s only at the park when he needs to be, \nand when he does come around he keeps \nto himself. \nHe seems nicer than he looks, though.")
image cg4Text = Text("Alby is one of the oldest employees at \nBreak Trail, and he’s got the experience to \nshow for it. Dustin is always asking for \nhis advice on just about everything. \n\nI’ve even caught Marsh occasionally leaning \non him from time to time. Whatever the \nproblem, Alby’s got the solution. \n\nI can only hope to one day be as wise and \nresourceful as he is.")
image ty cg= "CGs/ty desk cg 2.webp"
image border="ty desk cg border.webp"
image tyWriting=Composite(
    (1920,1080),
    (0,0), "border",
    (0,0), "ty cg",
    (0,20), "writing1",
    (-150,0), "writing2"
)

#DOODLES 
image tibbsDoodle = "CGs/journal doodle tibbs.webp"
image dustinDoodle = "CGs/journal doodle dustin.webp"
image gavinDoodle = "CGs/journal doodle gavin.webp"
image albyDoodle = "CGs/journal doodle alby.webp"

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

#THE ACTUAL CGs

image cg1 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "tibbsDoodle",
    (1100,100), "cg1Text"
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
    (0,0), "gavinDoodle",
    (1100,100), "cg3Text"
)

image cg4 = Composite(
    (1920,1080),
    (0,0), "journalBase",
    (0,0), "albyDoodle",
    (1100,100), "cg4Text"
)