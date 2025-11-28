init -1 python:
    def appear_transform(trans, st, at):
        #trans.xanchor = 0.5
        #trans.yanchor = 1.0
        if st > 4.0:
            trans.xpos = valueNum
            return None
        else:
            trans.xpos = 0.2
            return 0
    
    def playWoodNoise(trans,st,at):
        renpy.play("SFX_Wood_Hits_5.ogg",channel="sound1")
    def stopWoodNoise(trans,st,at):
        renpy.music.stop(channel="sound1",fadeout=None)


transform itemFight(xToOffset):
    
    easeout 0.1 xoffset xToOffset
    function stopWoodNoise
    function playWoodNoise
    easeout 0.3 xoffset 0
    pause 0.5
    easeout 0.1 xoffset xToOffset
    function stopWoodNoise
    function playWoodNoise
    easeout 0.2 xoffset 0
    pause 0.1
    easeout 0.1 xoffset xToOffset
    function stopWoodNoise
    function playWoodNoise
    easeout 0.2 xoffset 0
    pause 0.8
    repeat

#---Normal transforms---#
transform testTransform:
    xalign 0.0
    linear 2 xalign 0.5
    pause 20
    repeat

transform reset:
    linear 0.1 offset (0,0)

transform appear(xValue):
    anchor (0.5,1.0)
    pos (xValue,1.0)

transform appearAndFlip(xValue):
    anchor (0.5,1.0)
    pos (xValue,1.0)
    xzoom -1

transform appearAndMove(xStarting, xToMove, speed):
    anchor (0.5,1.0)
    pos (xStarting,1.0)
    linear speed xpos xToMove

transform moveAndFlip(xToMove,speed):
    parallel:
        linear 0.1 xzoom -1
    parallel:
        linear speed xpos xToMove

transform moveAndUnFlip(xToMove,speed):
    linear 0.1 xzoom 1
    linear speed xpos xToMove

transform moveAndFlipWithVertical(xToMove,yToMove,speed):
    xzoom -1
    linear speed pos (xToMove,yToMove)

transform move(xToMove,speed):
    linear speed xpos xToMove

transform moveWithVertical(xToMove,yToMove,speed):
    linear speed pos (xToMove,yToMove)
    pos (xToMove,yToMove)

transform moveWithArc(xToMove,yToOffset,speed):
    parallel:
        linear speed xpos xToMove
    parallel:
        easein (speed/2) yoffset yToOffset
        easeout (speed/2) yoffset 0

transform toAndBackAgain(xToOffset,yToOffset, speed):
    easein speed offset(xToOffset,yToOffset)
    easeout speed offset(0, 0)

transform jiggle(intensity, speedMultiplier, waitTime):
    ease 0.5*speedMultiplier xoffset intensity
    ease 1*speedMultiplier xoffset -intensity
    ease 0.5*speedMultiplier xoffset 0
    pause waitTime
    repeat

transform jiggleVertical(intensity, speedMultiplier, waitTime):
    ease 0.5*speedMultiplier yoffset intensity
    ease 1*speedMultiplier yoffset -intensity
    ease 0.5*speedMultiplier yoffset 0
    pause waitTime
    repeat

transform hop:
    easein 0.05 yoffset -80
    easeout 0.05 yoffset 0

transform lookAround(numberOfRepeats,startingDirection=1):
    linear 0.1 xzoom startingDirection*-1
    pause 1
    linear 0.1 xzoom startingDirection
    pause 1.0
    repeat numberOfRepeats

transform middleRight:
    xalign 1.0
    linear 2 xalign 0.7

transform middleLeft:
    xalign 0.0
    linear 2 xalign 0.3

transform itemAppear (newPosX,newPosY,speed):
    anchor(0.5,0.5)
    zoom 0.1
    pos(0.5,1.3)
    parallel:
        linear speed pos(newPosX,newPosY)
    parallel:
        linear speed zoom 1

transform itemDisappear(speed):
    parallel:
        linear speed pos(0.5,1.3)
    parallel:
        linear speed zoom 0.1


#---Diary transforms---#

transform bookSequence1:
    zoom 3.0
    anchor (0.5,0.5)
    xpos 2.0
    ypos 0.5
    linear 3 xpos 0.6
    pause 3
    linear 5 pos (0.3,0.7)
    pause 3

transform diaryAppear(newPosX,newPosY,time):
    anchor (0.5,0.5)  
    pos (0.5,-1.0)
    easein time pos (newPosX,newPosY)

transform cgTyAppear(newPosX,newPosY,time):
    anchor (0.5,0.5)  
    pos (0.5,1.5)
    easein time pos (newPosX,newPosY)

transform cgTyDisappear(time):
    easeout time pos(0.5,1.5)

transform diaryMove(newPosX,newPosY,time):
    linear time pos (newPosX,newPosY)

transform testDiary1_1:
    zoom 3.0
    anchor (0.5,0.5)
    pos(0.5,3.0)
    linear 2 pos (0.5,0.5)
    pause 0.5
    linear 1 zoom 4.0 pos (0.25,0.75)
    pause 2

transform testDiary1_2:
    linear 2 pos (0.6, 0.75)

transform testDiary1_3:
    linear 2 pos (0.6, 0.25)

transform emotePath:
    align (0.0,0.75)
    alpha 1.0
    parallel:
        linear 1 pos (0.05,0.6)
    parallel:
        linear 0.5 alpha 0.0



#------MENUS TRANSFORMS-------#

transform titleMenuHover:
    ysize 130
    on hover:
        xoffset -60
    on idle:
        xoffset 0

transform customXOffsetHover(offsetValue):
    on hover:
        xoffset offsetValue
    on idle:
        xoffset 0

#------UNIQUE TRANSFORMS-------#
transform albyFuckingDies:
    linear 1 rotate -45 ypos 2.3
