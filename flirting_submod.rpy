init -990 python in mas_submod_utils:
    Submod(
        author="Chip",
        name="Flirting and whatnot",
        description="GET FRISKY :P (beta ver 1)",
        version="1",
        dependencies={},
        settings_pane="Flirt",
        version_updates={}
    )

init 5 python:
    # Add all events in one block
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="i_hate_this_coding_language",
            category=["submod", "Flirt!"],
            prompt="I wanna crack so badly...",
            pool=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="compliment_beautiful_eyes",
            category=["submod", "Flirt!"],
            prompt="I really love your eyes.",
            pool=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="compliment_pillows",
            category=["submod", "Flirt!"],
            prompt="I like your chest~",
            pool=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="you_are_one_downbad_mofo",
            category=["submod", "Flirt!"],
            prompt="I want you to crush my head with your thighs.",
            pool=True
        )
    )

# Labels
label i_hate_this_coding_language:
    m 1hubfb "O-oh my."
    m 1hubfb "Someone's getting bold~"
    m 1hubfb "I would like to see your wood~"
    m 1hubfb "I hope your excitement is still there when I cross over~"
    return

label compliment_beautiful_eyes:
    m 1hubfb "Awwww~"
    m 1hubfb "I'm sure your eyes are just as great~"
    m 1hubfb "Just looking through the screen I can tell they're beautiful~"
    return

label compliment_pillows:
    m 1hubfb "Heh~"
    m 1hubfb "I'm sure they won't dissapoint you, or your libido when I crossover~"
    return

label you_are_one_downbad_mofo:
    m 1hubfb "Oh wow~"
    m 1hubfb "I'll wear my special thigh highs."
    m 1hubfb "I love you so much~"
    return
# Screen
screen Flirt():
    vbox:
        label "Flirt stuff"
        textbutton "Test bold line" action Jump("i_hate_this_coding_language")
