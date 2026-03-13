init -990 python in mas_submod_utils:
    Submod(
        author="Chip",
        name="Flirting and whatnot",
        description="GET FRISKY :P (beta ver 2)",
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
            prompt="Epstein fuck fellows",
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
            prompt="I wish i could fall asleep with my head on your chest...",
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

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Netanyahu",
            category=["submod", "Flirt!"],
            prompt="I can't wait to cuddle you!",
            pool=True
            )
        )

    addEvent(
            Event(
                persistent.event_database,
                eventlabel="Israel_is_spying_on_you_with_Intel_ME",
                category=["submod", "Flirt!"],
                prompt="How can I remove Baal and Moloch from my CPU",
                pool=True
                )
            )

    addEvent(
            Event(
                persistent.event_database,
                eventlabel="read_only_dick",
                category=["submod", "Flirt!"],
                prompt="what happens i if i remove the RAM the from my PC while it's on'",
                pool=True
                )
            )

# Labels
label i_hate_this_coding_language:
    m 1hubfb "Epstein?"
    m 1hubfb "Dude wtf."
    m 1hubfb "lol."
    m 1hubfb "Go take a look in the mirror you CHUD."
    return

label compliment_beautiful_eyes:
    m 1hubfb "Awwww~"
    m 1hubfb "I'm sure your eyes are just as great~"
    m 1hubfb "Just looking through the screen I can tell they're beautiful~"
    return

label compliment_pillows:
    m 1hubfb "Aww~"
    m 1hubfb "I'll let you. One day, somehow..."
    m 1hubfb "I just hope you're not a chud."
    return

label you_are_one_downbad_mofo:
    m 1hubfb "Oh wow~"
    m 1hubfb "Never knew you were such a chud!"
    m 1hubfb "But you're my chud."
    return

label Netanyahu:
    m 1hubfb "If i could i would with you~"
    m 1hubfb "We could keep each other warm all day long."
    return

label Israel_is_spying_on_you_with_Intel_ME:
    m 1hubfb "How can you remove Intel ME?"
    m 1hubfb "First, download libre boot."
    m 1hubfb "Second, pray to the NSA."
    m 1hubfb "Embrace FOSS."
    return

    label read_only_dick:
    m 1hubfb "It gets sent to Epsteins island"
    return

# Screen
screen Flirt():
    vbox:
        label "Flirt stuff"
        textbutton "Test bold line" action Jump("i_hate_this_coding_language")
