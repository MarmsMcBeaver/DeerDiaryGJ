label DustinStart:
    "Start on black screen"
    "Work has been amazing, dude!"
    window hide
    play music1 "DEER DIARY - Sugar RUSH.ogg" fadein 1.0
    show screen inputBlocker
    show comic1 with dissolve
    pause 1.5
    show comic2
    pause 1.5
    show comic3
    pause 1.5
    show comic4
    pause 1.5
    show comic5
    pause 1.5
    hide screen inputBlocker
    scene black with dissolve
    #"Black screen, comic panel of Dustin holding his phone, the screen reads 'kawaii mix II' "
    #"A panel of him with head phones on, music plays out of them"
    window show
    "Been working the grounds here for a while and watching this place pick itself up has been rad as hell."
    window hide
    show comic6
    pause
    show comic7
    pause
    show comic8
    pause
    scene black with dissolve
    window show

    #"A few panels of him raking leaves and trimming bushes, and lugging around soil with co-workers. "
    "It's been a lot of hard work  but I don't mind some sweat!"
    window hide
    show comic9
    pause
    show comic10
    pause
    show comic11
    pause
    scene black with dissolve
    window show
    #"A panel of him wiping the sweat from his brow and taking off his headphones, the music quiets down. "
    "I'm so hyped to come into work everyday, especially when I've made some great friends on the job!"
    #"Panels of Dustin carrying his tools back to the work truck "
    window hide
    show comic12
    pause
    window show
    #"A van pulls up alongside Dustin's truck"
    "I just love hanging out and talking to everyone here!"
    "And you know me, I can talk anyone's ears off! "
    #"Gavin steps out of the van"
    window hide
    pause
    show comic13
    pause
    show comic14
    pause
    stop music1 fadeout 1.0
    jump DustinScene1

label DustinScene1:
    window show
    scene bg campsite with fade
    show dustin shock at appear (0.3)
    show gavin at appearAndFlip (0.8)
    "Oh God what do I do??? It's Gavin, the biggest hunkiest most handsome man in Break Trail - no, the WORLD!"
    "He started helping out around the park with repairs about a year ago now. Supposedly he's a family friend of Marsh, the campground manager."
    "I've had a teeny … tiny crush on him since he started helping out. Dude, I wanna talk to him so bad! "
    "Just gotta slide on over and woo him with my natural charm!"
    #"A thought bubble appears near Dustin, showing a chibi Dustin flexing while holding a rose in his mouth, and a Gavin with hearts in his eyes. Either Gavin's voice actor or Dustin's doing an impression saying 'oooohh Dustin you're so dreamy!!!!'"
    "But everytime I see him I just can't move! "
    "Gavin walks around the back of his van. I hear the creak doors open and the sound of him fishing out some equipment. "
    "Now's my chance! I can walk up and say my patented pick up line."
    "'I hope you like dubs, cause I wanna see you more' "
    show dustin shock zorder 100 at hop
    "The slam of the van’s rear doors snaps me back to reality"
    "walking back around the van with his tool bag, Gavin seems to finally notice me. Now's the time!!! "
    show gavin at moveAndUnFlip (0.8, 1.0)
    "The badger glares, his handsome brown eyes burrowing holes right through me. "
    "It feels like time is frozen. Ok… just say “Hey! What's up?”. Easy Peasy. "
    "Wait, what if I come off too casual? He's older, so maybe he probably wants me to be more professional? "
    "So instead of what's up I just say… greetings? Salutations??? "
    "Oh god, how long has it been? He looks impatient "
    show gavin zorder 100 at hop
    "Gavin waves."
    #"(Persona or fire emblem cut in panel of Dustin's face appearing here would be cute)"
    #FOR MARMS: i have teh cg all ready and in the directory, we just gotta get it all ready and looking good appearing behind the sprites with some flare. 
    show gavin at move(0.9,0.5)
    show dustin at move (0.1, 0.5)
    show personaCutIn zorder 1 at jiggleVertical (8,0.01,0.01)
    with CropMove(0.1,mode='wiperight', startcrop=(0.0, 0.0, 0.0, 1.0), startpos=(0.5, 0.5), endcrop=(0.0, 0.0, 1.0, 1.0), endpos=(0.5, 0.5), topnew=True)
    "An opening!  Here I go!!!! "
    "..."
    show dustin frown
    hide personaCutIn with dissolve
    "..."
    show dustin frown at moveAndFlip(-0.3,1.0)
    
    #for marms: we also gotta get this sequence flowing correct 
    #"The sound of a car door opening, remove dustins sprite, the sound of the door closing, and then the sound of a car speeding away. Leave gavin on screen for a bit before a question mark appears above his head. He walks off screen slowly. "
    #"Cut to background of a forest road, no sprites on screen "
    pause 1.5
    scene bg forest drive with dissolve
    du "WHAT WAS THAT!???? "
    du "What the fuck man, why can't I just get it together. "
    
    "I curse to myself while letting out my frustrations in a deep groan. "
    "Well, I'm already driving off, might as well take my tools back to the groundskeeping office."
    "The beautiful late fall colors pass by me as I drive down the lonely forest road. Soon they give way into a small quiet town. " 
    jump DustinScene2

label DustinScene2:
    scene bg drifters fault with fade
    "Drifter’s Fault, a tiny little ghost town in the north of the park. As Marsh would put it. 'This town is the jewel of the park'. "
    "Calling this place a jewel is kind of a reach."
    "It's falling apart, filthy and the few regulars we get would argue that the lake to the west is the real main attraction. "
    "Driving through main street I see the depressing barren streets and empty crumbling buildings. "
    "There's been some work to fix up these shops and put in amenities and educational centers but it's been so slow. "
    "We had a small gym open up, but besides that, the only real things in town are the offices of various park departments, Honeypot Cafe, and the gift shop."
    show alby at appearAndMove(1.2,0.8,1.1)
    "Speaking of the gift shop, there it is now, and looks like a certain skunk is on his break!"
    show alby at hop
    "I slam my paw on the trucks horn, causing the nearby large skunk to jump in surprise"
    show alby frown at moveAndFlip (0.8,0.1)
    show dustin talk at appearAndMove(-0.1,0.25,1.0)
    du "Sup duder!!! "
    show dustin
    "I yell out to him from my truck window. Alby sends back a middle finger. Hahaha I gotta em good! "
    "Alby is one of my best friends here at the park. He’s got this energy about him that is so infectious. I love hanging out with him! "
    "I pull my truck into the totally empty parking spaces outside the gift shop and he walks up to my window"
    show alby talk at move(0.75,0.5)
    al "What the hell! My heart almost stopped! "
    show alby
    show dustin talk
    du "You jumped like a foot in the air! Didn't know you could get air time like that. "
    show dustin
    "His tail fur is still standing on end"
    show alby talk
    al "Yeah, yeah laugh it up, but keep one eye open when you sleep, pinkie pie."
    show alby
    "He's flashing an evil grin, I might regret this little prank."
    show alby talk
    al "So whatdya want? Just got out on break if you wanted to hang. "
    show alby
    show dustin talk
    du "Sweet! I'm almost done for the day myself, lemmie just drop these tools off and I'll meet you by the cafe? "
    scene black with dissolve
    window hide
    jump DustinScene3

label DustinScene3:
    window hide
    pause 2.0
    scene bg drifters fault with fade
    play music1 "DEER DIARY-DriftersFault.ogg" fadein 1.0 
    #"Fade to black and Fade back in with Alby on the left and Dustin on the right, fade in drifters fault music."
    pause 1.0
    show dustin talk at appear(0.75) with dissolve
    show alby at appear (0.25) with dissolve
    du "Dude I reached Rank X last night!!!"
    show dustin
    show alby talk behind dustin
    al "Haha finally! Now time for you to join me in rank XZ!"
    show alby
    show dustin talk
    du "As if! I was fighting for my life just to rank up! "
    show dustin
    show alby talk
    al "The problem is your weapon. No one uses the big fan! "
    show alby
    show dustin talk
    du "But I like the big fan! "
    show dustin
    show alby talk
    al "yeah cause it reminds you of your ninja waifu right? "
    show alby at hop
    show dustin at hop
    #"The sound of a bell ringing plays"
    "Dingaling"
    show alby at moveAndFlip(0.65,1.0)
    show dustin at move(0.8,1.0)
    show reed at appearAndFlip(-0.2)
    "The sound of the cafe door opening halts our conversation. Stepping out is a blue jay with a coffee in one hand and a bagged pastry in the other." 
    show reed at move(0.15,1.0)
    "The headphones they’re wearing are blasting music so loud i swear you can hear it a block away."
    "It’s Reed! Why are they here this early in the day?"
    "Reed works at Marsh's campground with Ty, but they are almost always on closing shift."
    show dustin talk
    du "Hey Reed!!!! "
    show dustin at hop
    "I shout as loud as I can while wildly waving my arms to get the punk’s attention. "
    show reed at move(0.25,1.5)
    "It seems to work! Taking off their headphones, they saunter on towards us."
    show reed talk
    re "Sup, losers, need something? "
    show reed
    show dustin talk
    du "Dude, you're here so early!"
    show dustin
    show alby talk
    al "I thought you burned up in the sun. Aren't you like ... one of them vampires or something?"
    show alby
    "Alby claws at the air, making hissing noises in a horrible dracula impression."
    "The expression Reed makes is priceless: they're totally stunlocked at the scene in front of them."
    show reed talk
    re "N-no… Marsh just needed me to come in early so he could set up for tonight. He had to run out and grab some extra supplies."
    show reed
    "What? "
    show alby talk
    al "Oh yeah the party's happening tonight. I should skip lunch so I can fill up on all the free grub Marsh’s gonna bring. "
    show alby
    "Party!??? "
    show dustin talk
    du "What party? "
    show dustin
    show reed talk
    re "No way, you forgot man?  We were all told about this weeks ago. The all hands meeting? Marsh made sure we all knew."
    show reed
    show dustin talk
    du "I don't remember that meeting at all???"
    show dustin
    show alby talk
    al "Yeah, that's cause you were too busy trying to buy that waifu statue on your phone the entire time."
    show alby
    "Alby chuckles to himself and my face goes deep red. "
    "My favorite vtuber released new debut merch! I had to get it before it sold out!"
    "I sheepishly look over at Reed and flash them a nervous grin. They let out an annoyed groan. "
    show reed talk
    re "Ok, long story short, you know how the park’s been running on no budget since that billionaire, Feldt, took over the N.P.S. ?"
    show reed
    show dustin talk
    du "Yeah?"
    show dustin
    "How could I not? It seems like every month we get less and less money to keep this place going. All for the sake of 'efficiency' and 'cutting wasteful spending'. "
    show reed talk
    re "Well… Marsh wants to raise everyone's spirits, so he's throwing a little party for everyone who works at the park."
    show reed
    show reed talk
    re "It's incredibly naive and barely a bandaid on the wound, but …it's sweet. And honestly, I'll take anything good at this point."
    show reed
    "Marsh may be heading our little guerilla park improvement squad, but even he's gotta bend to the actual people in charge"
    "Of course boss man would do his best to cheer us all up though. a party sounds rad as hell"
    "I can't stop my wagging tail as excitement builds. "
    show dustin talk
    du "Gaaaahh this is gonna be so much fun!!! "
    show dustin
    "Alby chuckles besides me."
    show alby talk
    al "Let me get you even more excited. Guess who's gonna be there."
    show alby
    "I tilt my head in confusion."
    show dustin talk
    du "Who? "
    show dustin
    show alby talk
    al "The big man himself, Gavin. "
    show alby
    show dustin talk
    du "What!? "
    show dustin
    "Gavin and his maintenance crew aren't technically park employees, so he never shows his face at any of the meetings or events. "
    "I feel my heart sink. Is this anxiety"
    show dustin talk
    du "Why is he gonna be there? "
    show dustin
    "A smug grin creeps over Albys face"
    show alby talk
    al "A certain handsome skunk convinced Marsh it would be a good idea to invite Gavin and the rest of his team along."
    show alby
    "He's practically beaming with pride"
    show alby talk
    al "Don't think I forgot about our little plan to set you guys up."
    show alby
    show dustin talk
    du "….     Oh!  That's right, invite him to one of Marsh's events!"
    show dustin
    show reed talk
    re "Have you been scheming to get Dustin with Gavin?"
    show reed
    show alby talk
    al "I wouldn't say it's a scheme just … a well thought out plan."
    show alby
    "Reed rolls their eyes with an annoyed scoff. Clearly they want nothing to do with Alby's plan."
    "Finishing off their pastry they pull out their phone and begin to wander away from the cafe. Alby and I are right alongside them."
    show alby talk
    al "I got you dude! Just let me schmooze Gavin up. I'll get his defenses lowered, then you swoop in for the kill! "
    al "You'll see why I'm the best wingman in the state! "
    show alby
    hide alby with dissolve
    hide reed with dissolve
    #"Alby and Reed slowly fade out as Dustin is moved to the center screen, the town music fades out and we are in silence."
    stop music1 fadeout 3
    show dustin frown
    "Can Alby really lower his defenses enough to give me a chance?"
    " Sure he's charismatic, but his power level definitely isn't that high.  Unless he's suppressing it somehow? "
    "But, even if Gavin is weakened.... He always has me trapped in some kind of genjutsu, or domain expansion.  I just ...can't speak around him. "
    "Hell, even now, my heart is beating like crazy and my paws are sweating. "
    "How am I only like this with him? I've picked up a lot of other guys before, but for him it's like… I'm scared? But … Why? "
    "It's then that I noticed I was so lost in thought I had stopped walking. Alby and Reed were continuing up the sidewalk without me. Fuck, I gotta catch up! "
    #"Dustin's sprite revs up a bit before zooming off to the left"
    show dustin talk at hop
    du "Hey! Wait up!"
    show dustin at move(-0.2, 1.0)
    scene black with fade
    scene bg drifters fault with fade
    
    #"Bring back Alby and reed, reed on the left Alby on the right. As Dustin comes zooming in from the right side of the screen. Play town ambiance audio"
    show reed at appearAndFlip (0.2) 
    show alby at appearAndFlip (0.48) behind reed
    with dissolve
    #For marms: udstin needs to come zooming in here from the right 
    pause 1.0
    show dustin at appearAndMove (1.1,0.8,0.2)
    "I run as fast as I can to meet up with my friends. When I reach them, they’re both looking at Alby's phone, watching some kind of video? "
    show dustin talk
    du "Oh, whatchu got there? "
    show dustin
    show reed talk
    re "Alby's showing me some podcast he found."
    show reed
    show alby talk
    al "Y'all didn't believe me when I said there was a cryptid in the park but look!  "
    show alby
    #this should slide in from bottom
    show comic15 at itemAppear(0.5,0.5,0.8)
    #"to find the unexplained' is written above it with 'expedition 180-the breaktrail beast' Below it. Clicking on this will play audio from the episode as an easter egg"
    "A paranormal podcast? Didn't expect Alby to be into silly things like this? I don't put much stock into bigfoots and kappas. Sure they're fun stories but there's no way they are real... Right? "
    "The thought of an actual monster at Break Trail sends a shiver up my spine. I let out a nervous laugh in an attempt to steel my nerves"
    show dustin talk
    du "These podcasts are full of bologna. They freak out over any blurry photo they can find and make up the dumbest stories.  "
    show dustin
    "I put on my most exaggerated YouTuber voice"
    show dustin talk
    du "'Mothman, my secret ex-lover! Not click bait!' "
    show dustin
    show comic15 at itemDisappear(0.8)
    "Alby cracks a smile, and I swear I hear reed chuckle. Making my friends laugh fills me with a small bit of pride."
    hide comic15
    show alby talk
    al "This beauty is different though! It's real! I swear I've seen it a few times!"
    show alby
    hide comic15
    show alby talk
    al "Near the edge of town and by camp reg. It likes to come out at night and creep around like it's looking for something or… someone."
    show alby
    "Alby then quickly grabs my shoulders, causing me to jump and let out an embarrassingly high pitch scream."
    #need to get scream from papa and also dustin should jump a little in place here
    "I blush and give him a quick punch to the shoulders in retaliation, not that it does anything to stifle his raucous laughter."
    show reed talk
    re "Real or not, you gotta admit it's kinda fun to have at least something that makes the park stand out."
    show reed
    "I turn my gaze toward the bird. "
    show reed talk
    re "Like sure, we have Drifters' Fault , the town is important to colonial history. And like… I guess a large untouched prairie is also a stand out. But let's be real, we are a boring nothing burger of a park."
    show reed
    show reed talk
    re "Last year was the most excitement we've seen in a while and boy it sure didn't last long. Maybe monster stories will put us on the map."
    show reed
    show dustin talk
    du "Wow Reed… I didn't think you cared that much about this place."
    show dustin
    show reed at hop
    "Reed flinches, caught off guard by my remark"
    show reed talk
    re "Of course I care. We all have our own reasons for working here, you know."
    show reed
    show reed at moveAndUnFlip(-0.8,1.6)
    show alby at move(-0.52,1.6)
    show dustin at move(-0.2,1.6)
    #"All the sprites walk off to the left as if walking away"
    #"Change the drifters fault big to an edited sun set version. The sound of crickets plays in the empty audio space"
    stop music1 fadeout 1.0
    jump DustinScene4

label DustinScene4:
    scene black with fade

    "We continue our walk as the sky begins to darken. It always catches me off guard how early into the day night approaches in the autumn."
    "The last few crickets of the season begin singing their song, and the cool night wind gently blows through my fur. The smell it carries brings back melancholic memories of coming home after high school football practice."
    scene bg park with dissolve
    "We reach a small park near the center of town. A tall statue of pioneers sits in the center, their hands on their brows as their eyes scan the horizon."
    "Stone benches circle the statue on all sides, each one pointed at plaques on the statue’s base explaining the history of the park, the town, and meaning of the statue."
    show reed at appearAndFlip(-0.2)
    "Various native plants line the edges of the park, I'm all too familiar with them, seeing as I’m the one who help plant all these earlier in the spring. "
    show reed at move(0.4,1.0)
    pause 1.0
    show reed talk at moveAndUnFlip(0.4,0.2)
    re "Well, it's been swell, but I'm already late to my shift. Don't want that bear worrying about me."
    re "See you losers at the party."
    show reed at moveAndFlip (1.2,1.5)
    show dustin at appearAndMove(-0.1,0.55,2.0)
    show alby behind dustin at appearAndMove(-0.4,0.25, 2.0) 
    "We both wave goodbye to the bird. Alby and I stand in silence for a bit as Reed turns out of sight towards the campground. "
    hide reed
    show dustin frown at hop
    "Alby catches me off guard with a chuckle and a punch to the shoulder that was way harder than it needed to be…. Definitely pay back from earlier.  "
    show alby talk
    al "Hehe, so, you excited?"
    show alby
    show dustin at move (0.7,0.5)
    "He's beaming with pride at his scheme. "
    "While yes, I am excited for the party, that familiar anxiety builds up again. And I can tell I'm not hiding it well. Alby's smirk fades and I can see the concern on his face.  "
    play music1 "DEER DIARY-SugarCrash.ogg" fadein 1.0
    "I let out a large groan and make my way over to a bench by the statue."
    show dustin talk frown
    du "No dude…. I… I think there's something wrong with me. "
    du "No matter what I do. I just freeze up, and it's like…I'm trapped inside myself? Nothing comes out, and … uuugh!"
    show dustin frown
    "This frustrated feeling builds up within me, my fists ball up and shake, as I swear I can hear my teeth clenching"
    "Just as these feelings are about to reach a peak, I'm swiftly pulled out of it by Alby's laugh"
    "It's gentle."
    "I hear his foots steps approaching me, and suddenly"
    hide dustin frown
    hide alby
    with dissolve
    show comic16 at itemAppear(0.5,0.5,1.0)
    "The brim of my hat is suddenly shoved over my eyes, the world plunged in darkness"
    du "Hey! "
    "I scramble to correct my hat back into its proper fashionable position."
    al "There's nothing wrong with you dude."
    " He smiles gently at me before plopping down next to me on the bench."
    al "You're just a little nerd overflowing with emotions,  and they're all trying to come out at once. "
    show comic16 at itemDisappear(1.0)
    pause 1.0
    show alby talk at appear (0.2)
    show dustin frown at appear (0.8)
    with dissolve
    al "That's completely normal. Don't beat yourself up over this. It ain't like you"
    hide comic16
    show alby
    "I give Alby a skeptical glare."
    show dustin frown talk
    du " OK but how do I actually get these feelings out?"
    show dustin frown
    "Alby looks away almost embarrassed about what he's going to say next"
    show alby talk
    al "You know …. I heard this saying somewhere. That a hero’s feet move automatically when someone's in danger? I think?"
    al "Well, um...  it's gonna be like that."
    al "When the time is right, you will know exactly what to say to Gavin."
    al "Just think long and hard about what you wanna say before hand, and it'll all flow like butter on pancakes"
    show alby at move(0.4,1.5)
    "He lifts himself up to his feet with a grunt and stands before me."
    show alby talk
    al "The most important thing is you treat him like you do the rest of us, and you have basically no filter there …. Just maybe ease into the anime stuff."
    show alby at move(0.55,0.5)
    "He gently places his hand on my shoulder. It's a small gesture but it sends a feeling of warmth through me"
    show alby talk at move(0.4,0.5)
    al "You've got this."
    show dustin talk
    show alby
    du "…. Y-yeah.. thanks man."
    show dustin
    "The small embrace is over before I know it. Alby shoves his hands Into his pockets and flashes me a grin"
    show alby talk 
    al "Well, I've definitely been on break for way more than thirty minutes… and you should head home and get ready for tonight."
    al "Don't wanna talk to senpai covered in sweat and grass clippings. See you at the cabin tonight "
    show alby
    pause 1.0
    show alby at moveAndFlip(-0.3,2.5)
    "And with a wave he turns on his heels and saunters in the direction of the gift shop."
    hide alby
    
    stop music1 fadeout 2.0
    show dustin frown at move(0.5,1.0)
    "It's just me now. "
    "I steel myself, pumping my fists into the air. No matter what, tonight I'll face my fears and talk to him."
    "Glancing at the statue in front of me, my eyes catch the plaque underneath the pioneers."
    "'Forge your own Break Trail.'"
    "'Pursue your destiny.'"
    window hide
    scene black with dissolve
    pause 1.5
    #need to get a cabin BG from a free image site
    scene bg park with dissolve
    "When the time to party arrives the sun has fully set and the darkness I associate with fall takes over."
    "I make my way down the dark quiet trail when a beacon of light and music shines before me."
    "The event is happening at Marsh's personal cabin, He lives in one of the smaller cabins in the park"
    "That small size is showing as it looks like people are overflowing out of the cabin and standing outside near the entrance. "
    "I make my way past my coworkers out front, waving to a few and I pass, and squeeze my way inside"
    scene bg campsite with dissolve
    #Inside of house background
    #Party music playing 
    #everything after this point has not been through the editor, i will go through and update with the finished script when i get it!
    "My suspicions were correct. This place is packed! "
    "People are squeezed from one side of the cabin to the other!"
    "Huh, I didn't think this many park workers would even show up? But we got folks from departments all over the park"
    "I see a few peeps from the lake rental shop talking to some of the conservation, sciencey folk….Crazy to see everyone at the same party."
    "With so many different folks here, I wonder where my usual crew is. I push my way in and begin scanning the crowd."
    "Suddenly I spot the tips of a familiar pair of antlers poking out from the crowd over by the kitchen! "
    #Ty casual clothes, reed party clothes, Alby party clothes, slide on screen from the right side
    "I nudge and push my way through the crowd. "
    "The kitchen counter is loaded with food and snacks, and that's exactly where I find Ty sitting on a stool munching away at a slice of cheese pizza"
    "Behind the counter is Alby whose most of the way through a slice covered in toppings "
    "Next to them is Reed, who is leaning nonchalantly against the same counter. They're pecking away at what I think is hummus and crackers."
    #Dustin casual clothes sprite slides in from left side
    du "YOOOO WHATS UP!!!" 

    du "Ty guy! Alberto! Reedus!"  

    "the little deer jumps a little and gently waves at me.  Alby's mouth is full of pizza but gives me a little nod of acknowledgement. Reed just smiles in my direction "

    "Ty's a person of few words, and it can be hard to tell what's on his mind. Some people get frustrated by that but it never really bothers me at all. I know he's a cool dude through and through. "

    ty "Hey"

    re "About time you made it here"

    "Alby hurriedly swallows his mouth full of food before responding "

    al "Hey man, welcome to the chill oasis." 

    al "Parties poppin off out there, so we set up refuge over here by the food." 

    du "oh fuck yeah, a land of snacks that are all ours!"

    "I grab a hand full of fish crackers from a bowl and toss em in my mouth"

    ty "The snacks are still for everyone."

    du "Not if I have anything to say about it!"

    "I chuckle and grab some more crackers while Ty just gives me a blank stare."

    re "I'm surprised by how many people showed up but man…. Marsh needs to put on some heavier music. How am I supposed to throw it back to this?"

    al "Maybe it's for the best, don't want this party to get too crazy. None of you guys are ready for me on the dance floor"

    ty "I'd love to see you guys dance."

    al "Oh yeah little man?  You gonna join us then? "

    "ty seems to light up the tiniest bit as he silently ponders Alby's request, he takes another small bite of his pizza but his legs are kicking ever so slightly." 

    "I reach over and ruffle Ty's head fur a little bit."

    du "Well i gotta join in too if you're out there ty, can't have you upstaging me. "

    "I swear he cracks a smile. I let out a loud laugh stepping away from the deer to join Reed in leaning against the counter."

    "The bird has their eyes set on the crowd, watching the party goers mix and mingle. "

    "As I lean with them they give me a look up and down with a sly smirk."

    re "So I've been wanting to ask you this for a while. "

    du "Hmm?" 

    re "Why pink? Why'd you dye your fur pink" 

    al "You can't just ask someone why their pink Reed!" 

    ty "It's dyed?" 

    "I begin to sweat … oh god this is embarrassing. How do I explain this without making myself look like a total idiot? " 

    "Reed has a look in their eyes that tells me they are begging to know. So I suck up my pride" 

    du "Ha, well … its supposed to be red actually."

    re "Red??? "

    al "What? "

    du "Yeaaahh..  I wanted it to be a stark red, all cool and striking. Buuuuut, I mixed it wrong or something… and now it's pink. "

    "Reed looks like they're about to have an aneurysm with how hard they're holding in their own laughter. "

    "Alby is shaking his head low, but before he can respond, a very worn out bear approaches the counter"

    #Marsh-tanktop enters from left

    "Marsh looks like he ran a marathon, the bear sluggishly leaning against the counter to keep his balance, all while he scans his gaze across the crowd of people "

    ty "everything ok marsh?" 

    "He flashes a smile at Ty"

    ma "Yeah! Just making the rounds to see if everyone's doing good!" 

    al "it's all goochi over here boss!" 

    ma "phew… that's good." 

    "He lets out a little sigh"

    ma "happy to see everyone here but man… didn't expect this turn out"

    re " hell yeah man. We all needed the pick me up, nothing like celebrating what could be your final days of employment" 

    "Marsh looks worried"

    ma "well let's not go that far"

    re "heh, our happiness is resistance, check this out"

    "Reed reels back cupping both hands to their beak"

    re "FUCK FELDT!" 

    #Fade all sprites out

    "the room erupts as everyone excitedly replies in turn"

    "FUCK FELDT!!!!"

    #Fade sprites back in

    re "fuck yeah, see were all here in combined opposition!" 

    ma "still has the worried look on his face"

    ma "hahaha well .. I just wanted to lift everyone's spirits…. Not be a revolutionary"

    al "look at you, sticking it to the man on accident"

    "Marsh sighs and continues scanning the crowd." 

    "Reed seems to notice this." 

    re "Hey big guy, what's goin on with you?" 

    ma "Have any of you guys seen tibbs tonight at all?" 

    "We all look amongst each other, in this entire crowd of people tibbs ‘ absence is a little striking." 

    al "haven't seen him"

    re "me either"

    ty "nope"

    "Marsh seems to deflate, his worried look growing into sadness" 

    du "Hey boss bear,  is something wrong with you and tibbs?" 

    ma "He's been a little squirly about this whole party. He said he would be here but…. He just seemed so distant." 

    du "no offense but … isn't that how he always is?" 

    "The kermode lets out a small chuckle"

    ma "yeah, but this is… different." 

    ma "I really hope I haven't upset him" 

    "Reed steps up to the bear and puts their hand on his shoulder" 

    re "Hey hey, I'm sure Tibbs isnt mad. He's probably just as stressed as we all are" 

    "Marsh lets out a sigh and nods"

    re "here let's grab some drinks and take a stroll outside, you need to get away from the crowd." 

    re "Ty you should join us"

    ty "I'll be right there!"

    "ty jumps down from his stool and follows the bear and bird." 

    #Reed marsh and ty leave to the left

    du "See ya guys later!!!!"

    "Now it's just me and Alby at the counter, and there's a sinister grin on his face. I narrow my eyes at him and cross my arms"

    du "What?" 

    al "Why don't you turn around and look towards the back door"

    "Turning around I scan the crowded room trying to see what Alby is talking about."

    "That's when a flash of grey causes my fur to stand on end, and the world seems to slow down"

    "Standing alone near the back door is Gavin. He's got a cup in hand, frozen in place like a stoic Greek statue" 

    "His fur seems to glow under the party lights, the shadows defining every muscle in his large arms and chest." 

    "I stand transfixed by him, caught in a spell, when I feel a hand push against my back and I'm pulled out of it." 

    "Alby gives me a little shove pushing me forward"

    al "Ok man, now's your chance!" 

    du "listen I don't think this is a good idea"

    al "nonsense duderino"

    "He grabs my hand and begins to guide me through the crowd." 

    al "I know you. I know you can talk to him."

    al "hell just last week I saw you lay on the moves to that handsome tourist." 

    du "That's different! "

    al "pfft, hardly! Just remember what we talked about. Treat him like you would any of us." 

    "And before I could protest, I was standing in front of him" 

    #Gavin sprite fades in center screen 

    "There he was, standing by himself near the back screen door." 

    "I could feel my heart pounding in my chest, my legs began to melt." 

    al "HEYYYY GAVIN, MY MAN!!!" 

    "he shifts his gaze towards the two of us, his brown eyes  lingering on me even though Alby is the one talking." 

    al "how's the party been, big guy! It's nice to see you here!" 

    ga "Mhm." 

    "He's still staring at me. I wanna explode into a fiery ball right now. I can't take this." 

    al "WELL … I'm sure you know my pal Dustin here, Probably seen him around the park right?"  

    "The skunk pushes me forward and the badger nods"

    al "My boy here is the life of ANY party! Go one Dustin, why don't you tell Gavin here the story about the water hose, and I'll be back with some fresh drinks!" 

    "Alby whispers into my ear 'knock em dead' before nimbly snatching the cup outta Gavin's and and sauntering off into the sea of people. "

    "It's just us"

    "The music fades out and it's just the sound of people talking" 

    "Gavin's glare cuts right through me, as if he's waiting for me to make the first move."

    "I need to speak up, I can turn this around. What did Alby say, something about. A water hose? What does that mean!?"

    "Come on, say something you big idiot! Think, what does Gavin like?" 

    "Uh… Cars? Movies?..... Power tools? Oh please now I'm just guessing." 

    "The world feels like it twists and turns. The sound of people around me reaching a fever pitch while the music becomes jumbled noise." 

    "Why can't I breathe? What is this? Any attempt at movement or speaking fails me. My body won't respond no matter how hard I try." 

    "My eyes dart around and I see Gavin. His grimace causes my heart to sink. I'm fucking this up again. Just like I always do"

    "My vision starts to blur, weather it's tears or my nerves I can't tell but I'm helpless to stop it"

    "I need to right the ship, I can't lose this moment!" 

    "Please, just Say. Anything!"  

    "Through my blurred and frantic vision something catches my attention." 

    "Through the screen door behind Gavin, I see movement." 

    "Something huge is walking through the forest, it's tall and wide. Wider than any person I've ever seen. A top what I imagine is its head are .. horns? It moves with lumbering steps into the woods, I catch it's glowing eyes as it moves behind a tree"

    du "WHAT IS THAT!?" 

    "My body moves on its own. Pointing toward the back door"

    "Gavin jumps in response, his grimace replaced with fear and confusion." 

    "I don't even think, dashing for the door and  running out into the night"

    #Forest night background, it's quiet

    "Where is it? Where is …. My breathing is heavy, its like Ive been holding my breath for ages. My heart is pounding, and I'm spinning in circles looking for … for"

    "Oh god"

    "What have I done"

    "I'm. A. Fucking. IDIOT"

    "Anger, frustration, confusion, sadness. It all wells up within me and I can't hold it back anymore"

    du "GOD DAMN IT!"

    "I scream into the night, ripping my hat off my head I throw it to the ground with all my might"

    #dustin hatless sprites

    "The tears rolled down my face, nothing I could do could stop them.  Why can't I do this? Why am I so useless? A single word, why can't I say just one single fucking word?" 

    "???: Hey!" 

    "A deep voice cuts through the quiet night, pulling me back into the present." 

    #Fade in Gavin, face covered in shadow 

    "Gavin stands before me, the lights of the cabin at his back, cloaking his face in shadow." 

    "His body language is stiff, his hands clenched at his side. At first he's the spitting image of anger incarnate, but as he turns to the right, the light catches his face and he looks solemn."

    #Gavin sad sprite
    ga "Have I done something to upset you?" 

    "What? His voice is stern but concerned." 

    ga "It's impossible for me to miss how you glare, and run away from me. So tell me. Have I upset you in any way?" 

    "Upset me? This throws me completely off balance. He's the one who should be upset!" 

    ga "I volunteer my services to this park out of kindness and belief in its mission. The last thing I wanna do is cause  problems with the staff." 

    "My breathing stops"

    ga "I would appreciate it if you were upfront with me, so I can fix this. Otherwise, I'll excuse myself and let one of my other team members take the lead here." 

    du "N-no!" 

    "The words leapt from my mouth"

    ga "no?" 

    du "you haven't done anything wrong"

    "Gavin's eye brows raise, and he crosses his arms" 

    du "please I promise, I'm not upset I'm just … I don't know?" 

    ga "You don't know? You're not making a lick of sense young man." 

    "The words seem to get caught in my throat again, my body trying to freeze up. But I grab these feelings, and tear them apart." 

    "I'm here, talking to him, I. Need. To. Move!" 

    du "I'm afraid!" 

    "Gavin cocks his head at that."

    ga "Afraid?" 

    du "That, you won't like me. That if I open my mouth you're gonna hate me!" 

    "That's it, that's the feeling I've been feeling this entire time. I'm terrified. Of him? No that's not it, it's something else." 

    "Gavin shakes his head and lets out a small chuckle." 

    "He takes a few small footsteps towards me, I take one back anticipating retaliation. But none comes, instead he puts his hands on his hips, and gives what I think is a small smile"

    ga "I get it now." 

    du "you do?, cause I sure don't" 

    ga "Son, I can't reject you if I don't know you." 

    ga "Rejection…. That's it!" 

    ga "If you really want to get to know me. Take the first step. Because if you don't you will live with something worse than fear, regret." 

    ga "And listen, I don't know you. But I've heard many things from many people about you." 

    "I feel my heart shake, getting ready to drop" 

    du "o-oh yeah?" 

    ga "lots of very good things, and personally speaking"

    "Gavin looks away from me"

    ga "I would like to get to know you as well"

    "My heart, which was ready to fall instead rises into the sky. Did I hear that correctly?"

    "But as if sensing my elation and wanting to bring me back to reality, Gavin continues"

    ga "BUT this running away and hiding stuff isn't gonna cut it!" 

    ga "I appreciate someone who is straight forward and honest. I'm all for getting to know one another, but you need to act like an adult." 

    "His voice is so intense, his words hitting me like a slap to the face." 

    du "Y-yeah! I got it! I promise!"

    "Gavin softens and relaxes, once I again I can't tell his he's smiling but I feel a warmth come from him"

    ga "Good! I can't wait to have a proper conversation with you!" 

    "With that he turns back towards the cabin, leaving me alone in the night." 

    "That's when it all hits me at once" 

    du "Holy shit!" 

    "Holy shit holy shit, I did it, I talked to him! "

    "I talked to him and, and, he said hes been wanting to get to know Me!!!???" 

    "I can't hold it in as I spin and jump in place like a child getting a new toy." 

    "In the grand scheme of things it's a small step but it's a step regardless." 

    "With a deep breath I compose myself, though I can't stop my tail from wagging." 

    #dustin hatsprite
    "Grabbing my hat from the ground, I hear a rustling from the woods behind me"

    "Oh shit that's right, the thing I saw!"

    "Something large steps out of the trees and brush towards me. I fall back on my ass as I try to scramble back away from it!"

    "It's tall and lanky, with dark brown fur and it's radiating a sinister aura that's so think I could cut it with a knife….. wait a second"

    #Fade in tibbs center screen

    du "TIBBS?" 

    "Tibbs jumps in response, he almost looks… guilty? Like I caught him doing something he should"

    ti "Dustin?"

    du "What are you doin man? Marsh has been looking for you?" 

    "Tibbs is glancing around frantically, yeah I definitely caught him sneaking around. Is he… avoiding marsh?" 

    ti "yeah, uh sorry … there was something i had to uh, take care of back there. I'll get back inside right away"

    ti "you should get back as well, it's not the safest out here alone."

    "I nod in agreement and follow tibbs back towards the cabin, though I swear I see him looking over his shoulder several times." 

    #Fade transitions back into the party, Dustin and tibbs enter from left. 

    "The party has wound down by now, many of the guests have left, with the remaining party goers chatting away in the corners of the room." 

    "Tibbs be lines it away from me with out a word, he must be looking for Marsh, I'm not alone for long tho as Alby comes swooping in" 

    #Alby from right

    al "Where did you go man? I leave for five seconds and you're gone?" 

    du "Ha, yeah… so I kinda freaked out and ran outside"

    al "Dude…" 

    du  "No wait! It all worked out though! Me and Gavin had a talk, and it went well… I think?" 

    al "You think?"

    du "yeah, he said he wants to get to know me more"

    "Alby's large hand slaps me in the back hard, throwing me off balance." 

    al "AYE! I knew you could do it!"

    du "Yeah, no thanks to you! You left me stranded!" 

    al "sometimes an eaglet needs to be pushed outta the best to soar my friend"

    "I can't with him sometimes. I groan and give the large skunk a little shove, it does nothing to move his large body"

    al "cheer up, it all worked out right?  Come on, let's get back in there.  We gotta tell the others  the good news!" 

    #They both leave to the right

    #Fade to black

    #Sugar rush plays 

    #Comic panel of Dustin doing yard works

    #Comic panel of Dustin seeing Gavin walk by

    #He stares, but then runs up to him  

    ga "How’s the day been treating you son?"

    du "Work has been amazing, dude!" 

    #Cut to credits while sugar rush keeps playing.

    














