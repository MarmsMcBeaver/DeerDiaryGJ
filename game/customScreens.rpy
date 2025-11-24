init python:
    def changeNoteChar(charToChange):
        persistent.currentCharNote = charToChange
    def doNothing():
        someNewVariable = 1

init:
    default persistent.currentCharNote = "Tibbs"

image notesPopUp = ConditionSwitch(
    "persistent.currentCharNote=='Dustin'","noteDustin.png",
    "persistent.currentCharNote=='Tibbs'","noteTibbs.png",
    "True","tibbsNote.png")

screen emoteHandler:
    frame:
        xpadding 10
        ypadding 10
        xalign 0.0
        yalign 0.0
        textbutton "Test emote" action [Show("emoteView", emoteName="emote_urgay@2.png")]

screen emoteView(emoteName):
    add emoteName at emotePath
    timer 1.5 action [Hide("emoteView")]
    on "show" action Play("channelEmote","objection.mp3")

screen inputBlocker:
    key "mouseup_1" action NullAction()

screen notesHandler:
    frame:
        xpadding 10
        ypadding 10
        xalign 0.0
        yalign 0.4
        textbutton "notes" action Show("notesMenu",_zorder=150)


screen notesMenu:
    modal True
    imagebutton idle "buttonClose.png" action [Hide("notesHandler"), Hide("notesMenu")] at customXOffsetHover(30):
        pos (0.65,0.2)
    imagebutton idle "buttonTibbs.png" action Function(changeNoteChar,charToChange="Tibbs") at customXOffsetHover(30):
        pos (0.65,0.3)
    imagebutton idle "buttonDustin.png" action Function(changeNoteChar,charToChange="Dustin") at customXOffsetHover(30):
        pos (0.65,0.4)
    add "notesPopUp" at center