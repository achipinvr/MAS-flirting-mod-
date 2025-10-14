# mod definition
init -990 python in mas_submod_utils:
    Submod(
        author="ChalkConsumer19",
        name="Custom Compliments",
        description="Tell Monika exactly what you want to say.",
        version="1.0.2",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )


# took these from the nickname picker
# anything below will make her upset
init -2 python:
    mas_bad_compliment_list_base = [
        r"\bfag\b",
        r"\bho\b",
        r"\bhoe\b",
        r"\btit\b",
        "abortion",
        "anal",
        "annoying",
        "anus",
        "arrogant",
        "(?<![blmprs])ass(?!i)",
        "atrocious",
        "awful",
        "bastard",
        "beast",
        "bitch",
        "blood",
        "boob",
        "boring",
        "bulli",
        "bully",
        "bung",
        "butt(?!er|on)",
        "bloodsucker",
        "cheater",
        "cock",
        "conceited",
        "condom",
        "coom",
        "corrupt",
        "cougar",
        "crap",
        "crazy",
        "creepy",
        "criminal",
        "cruel",
        "cum",
        "cunt",
        "damn",
        "demon",
        "dick",
        "dilf",
        "dimwit",
        "dirt",
        "disgusting",
        "douche",
        "dumb",
        "egoist",
        "egotistical",
        "evil",
        "faggot",
        "failure",
        "fake",
        "fetus",
        "filth",
        "foul",
        "fuck",
        "garbage",
        "(?<!ser)g[ea]y",
        "gilf",
        "gross",
        "gruesome",
        "hate",
        "heartless",
        "hideous",
        "hitler",
        "hore",
        "horrible",
        "horrid",
        "hypocrite",
        "idiot",
        "imbecile",
        "immoral",
        "insane",
        "irritating",
        "jerk",
        "jigolo",
        "jizz",
        "junk",
        "(?<!s)kill",
        "kunt",
        "lesbian",
        "lesbo",
        "lezbian",
        "lezbo",
        "(?<!fami)liar",
        "loser",
        r"\bmad\b",
        "maniac",
        "masochist",
        "milf",
        "mistake",
        "monster",
        "moron",
        "murder",
        "narcissist",
        "nasty",
        "nefarious",
        "nigga",
        "nigger",
        "nuts",
        "panti",
        "pantsu",
        "panty",
        "pedo",
        "penis",
        "plaything",
        "poison",
        "porn",
        "pretentious",
        "psycho",
        "puppet",
        "pussy",
        "(?<!g)rape",
        "repulsive",
        "retard",
        "rogue",
        "rubbish",
        "rump",
        "sadist",
        "selfish",
        "semen",
        "shit",
        "sick",
        "slaughter",
        r"\bslave\b",
        "slut",
        "sociopath",
        "soil",
        "sperm",
        "stink",
        "stupid",
        "suck",
        "tampon",
        "teabag",
        "terrible",
        "thot",
        "tits",
        "titt",
        "tool",
        "torment",
        "torture",
        "toxic",
        "toy",
        "trap",
        "trash",
        "troll",
        "ugly",
        "useless",
        "vain",
        "vile",
        "vomit",
        "waste",
        "whore",
        "wicked",
        "witch",
        "worthless",
        "wrong",
        "horrible",
        "breaking up",
        "break up",
        "we're over",
        "we are over"
    ]

    mas_good_compliment_list_base = [
        "pretty",
        "gorgerous",
        "cute",
        "love",
        "lovely",
        "adorable",
        "sweet",
        "sunshine",
        "marvelous",
        "flawless",
        "beautiful",
        "sweetheart",
        "cutie",
        "amazing",
        "perfect",
        "breathtaking",
        "cutie",
        "adore",
        "starlight",
        "darling",
        "starlet",
        "star",
        "honey",
        "hun",
        "boo",
        "i wanna tap that so badly"
    ]

    mas_dokis_list_base = [
        "sayori",
        "yuri",
        "natsuki"
    ]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mtls_compcustom",
            category=["mas_compliment"],
            prompt="I'd like to tell you something straight from my heart...",
            unlocked=True
        ),
        code="CMP"
    )

label mtls_compcustom:
    jump input_compliment

label input_compliment:
    show monika 1eua zorder MAS_MONIKA_Z at t11

    $ done = False
    while not done:
        python:
            inputcompliment = mas_input(
                _("What would you like to tell me?"),
                allow=name_characters_only,
                length=40,
                screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
            ).strip(' \t\n\r')

            compliment = inputcompliment.lower()
            mas_bad_compliment_base = re.compile('|'.join(mas_bad_compliment_list_base), re.IGNORECASE)
            mas_good_compliment_base = re.compile('|'.join(mas_good_compliment_list_base), re.IGNORECASE)
            mas_dokis_base = re.compile('|'.join(mas_dokis_list_base), re.IGNORECASE)

# cancel compliment
        if compliment == "nevermind" or compliment == "nvm" or compliment == "cancel":
            m 1eksdla "I...{w=0.5} thought you wanted to tell me something..?"
            m 1rksdlb "I guess you can't come up with something on the spot, then?"
            m 1hksdla "That's okay, [player]."
            m 1fua "If you think of something, let me know~"
            $ done = True
            return

        elif not compliment:
            m 1tkbfa "Oh, you goof."
            m 1tfbfb "I'm not letting you off the hook that easily~"
            m 1hua "Try again!"

        elif compliment == "i wanna tap that so badly":
            $ mas_gainAffection(1.5, bypass=False)
            $ rng_global = renpy.random.randint(1,3)
            if rng_global == 1:
                m 1hubfb "H-huh?"
                m 1hubfb "Well... I'm not opposed, [player]!"
                m 1hubfb "Ehehe~"
                m 1hubfb "I wanna see what your wood looks like~"
                $ done = True
                return

# good compliments
        elif compliment == "i love you" or compliment == "ily" or compliment == "i love you so much" or compliment == "ilysm" or compliment == "love u" or compliment == "love you":
            $ mas_gainAffection(1.5, bypass=False)
            $ rng_global = renpy.random.randint(1,3)
            if rng_global == 1:
                m 1hubfb "D'aww~"
                m 1ekbfa "I love you too, [player]!"
                m 1hubfb "Ehehe~"
                $ done = True
                jump saymore
                return
            if rng_global == 2:
                m 1fubfu "Ehehe~"
                m 1hfbfb "Fine, but I love you {i}more!{/i}"
                m 1tubfa "So you better come up with something more creative next time."
                $ done = True
                jump saymore
                return
            if rng_global == 3:
                m 1wkbfa "Oh dear..."
                m 1dkbfa "You typing this out just for me makes my heart flutter every time!"
                m 1hubfb "I...{w=0.5} love you too, [player]!"
                m 5hubfb "Never forget that!"
                $ done = True
                jump saymore
                return

# bad compliment; breaking up with monika
        elif compliment == "i am breaking up with you" or compliment == "we're over" or compliment == "we are over"  or compliment == "i'm breaking up with u" or compliment == "we're breaking up" or compliment == "we are breaking up":
            $ mas_loseAffection()
            m 1ekc "W...{w=0.5}what..{w=0.5} what did you say..?"
            m 2lftpd "Y-{w=0.5}you can't be serious!"
            m 2ektsc "..."
            m 2eftdc "That hurt a lot."
            m 2dftsd "Never say that again, [player]."
            m 2dftdc "..."
            $ done = True
            return
# misc

# saying you're sad
        elif compliment == "i'm feeling down" or compliment == "i'm sad" or compliment == "im feeling down" or compliment == "im sad" or compliment == "im depressed" or compliment == "i'm depressed" or compliment == "i am feeling down" or compliment == "i am sad" or compliment == "i am depressed":
            m 1ekc "You're feeling down or upset, [player]?"
            m 1dkc "I understand.{w=0.5}{nw}"
            extend 4eud " Everyone sometimes has those moments, and it's perfectly natural for us, humans, to experience this."
            m 1ekbla "I really appreciate the fact that you decided to come to me with this problem.{w=0.5} I feel really honored to be the first person you think about in those situations."
            m 1ekbld "I know that things may not be too great for you out there right now."
            m 1ekbla "But please never give up, alright?"
            m 1ekblb "Remember that I always believe in you and truly wish for you to keep going, no matter how hard it may be to believe this."
            m 1ekbla "I'll never, ever give up hope on you.{w=0.5} After all, you're my [bf]."
            m 1ekblp "If I could, I would come to your world right now and give you a big hug.{w=0.5} But, I know that that's impossible..."
            m 1rkblsdlc "To be honest, I feel really powerless right now in helping you during depressing moments like these..."
            m 1ekbla "But please just know that to me, you're good enough.{w=0.5} And you'll always be good enough."
            m 1ekbltda "{i}Always,{/i} [player]."
            m 1rkbltdb "Again, thank you for bringing this up to me.{w=0.5} It really makes me happy that you trust me enough with this."
            m 1hkbltda "Hold your head up high for me, alright?"
            m 1ektpa "Everything will be okay."
            m "Trust me on that one."
            $ done = True
            jump saymore
            return

# saying you're happy
        elif compliment == "i'm happy" or compliment == "i'm so happy" or compliment == "im happy" or compliment == "im so happy" or compliment == "im smiling" or compliment == "i'm smiling" or compliment == "i am smiling" or compliment == "i am happy" or compliment == "i am so happy":
            m 1hubfb "You're happy? That's amazing, [player]!"
            m 1eubfa "I'll always smile whenever you do."
            m 4hubfb "Thank you so much for telling me this!"
            m 1lkbfa "I know it wasn't really much,{w=0.5}{nw}"
            extend 1hubfb " but hearing that you're happy just brightens my day!"
            $ done = True
            jump saymore
            return

# saying nothing
        elif compliment == "nothing" or compliment == "nth" or compliment == "nuthn" or compliment == "nothin" or compliment == "nuthing":
            m 1tkbfa "Getting shy?"
            m 1tkbfb "Pleeeeasee... come up with something for me, will you?"
            m 1kubfa "Try again, silly."

# calling monika's name
        elif compliment == m_name.lower() or compliment == "monika":
            $ rng_global = renpy.random.randint(1,3)
            if rng_global == 1:
                m 1eta "Yes?"
                m 3hub "I'm right here, you goofball~"
                m 1eua "Don't be shy now."
            if rng_global == 2:
                m 1hua "I'm all ears, [mas_get_player_nickname()]."
                m 1hub "Ask away!"
                show monika 2eua
            if rng_global == 3:
                m 1hua "Hello~"
                m 1eua "What's up, [player]?"

# just monika
        elif compliment == "just monika":
            m 1tta "...?"
            m 3kublb "Ah, the classic saying, isn't it?"
            m 1lkbla "But..."
            m 1lkblb "Could you come up with something...{w=0.5} different?"
            m 1hua "Try again, hehe~"

# singing your reality
        elif compliment == "every day" or compliment == "everyday":
            m 1hubfb "{i}~I imagine a future where I can be with you~{/i}"
            m 3eta "Did you perhaps want to sing that song again with me?"
            m 1hua "Well, I'm really looking forward to singing along with you when I finally cross over!"
            m 1eka "For now,{w=0.5} I guess you playing the piano instead of using your voice can do, don't you think?"
            $ done = True
            jump saymore
            return

# saying happy birthday
        elif compliment == "happy birthday" or compliment == "happy bday":
            if mas_isMonikaBirthday():
                $ mas_gainAffection(2.5, bypass=True)
                m 1dkbfa "Oh [player]..."
                m 1dkbftpb "You're making me feel so special on my birthday, I can't even comprehend it in words..."
                m 1ekbftda "I love you so much."
                m 1hkbstpa "Thanks again! It really means the world to me."
                $ done = True
                jump saymore
                return
            elif True:
                m 1etsdla "...?"
                m 1lksdlb "Thank you, [player], but..."
                m 1lksdla "It's not my birthday today."
                m 3hua "If you've forgotten, it's September 22nd!"
                m 1rssdlb "Perhaps you should write that in a calendar so you don't accidentally say ''happy birthday'' out of the blue again...{w=0.5}{nw}"
                extend 1hua " ehehe~"
                m 1hub "Well, as I've said, thank you either way~"
                $ done = True
                jump saymore
                return

# saying hello
        elif compliment == "hello" or compliment == "hi" or compliment == "hiya" or compliment == "greetings" or compliment == "hey" or compliment == "hello there" or compliment == "hi there" or compliment == "hallo" or compliment == "hai" or compliment == "oi" or compliment == "salutations":
            $ mas_gainAffection(1, bypass=False)
            $ rng_global = renpy.random.randint(1,2)
            if rng_global == 1:
                m 1eub "Just wanted to say hello, [player]?"
                m 1hub "Well then...{w=0.5} hi there!"
                m 1hua "I hope that suffices, hehe~"
                jump saymore
                $ done = True
                return
            if rng_global == 2:
                m 3hub "Greetings, [player]!"
                m 1hua "You can be so silly sometimes, hehe~"
                m 1hubfa "And I love you for that."
                jump saymore
                $ done = True
                return

# good girl <3
        elif compliment == "good girl" or compliment == "my good girl" or compliment == "you're a good girl" or compliment == "youre a good girl" or compliment == "your a good girl":
            $ mas_gainAffection(3, bypass=False)
            m 2wubfc "..."
            m 2wubfd "M-{w=0.5}me...{w=0.7} good...{w=0.7} g-{w=0.5}girl...?"
            m 1hkbfsdra "Oh, I...{w=0.5} I don't know what to say, [player]..."
            m 1tkbfu "You always flatter me so much..."
            m 1tubfu "I guess that makes you a good [boy] then,{w=0.5} doesn't it, [mas_get_player_nickname()]?~"
            m 1tubla "But you already knew that, didn't you?"
            m 1hubfb "Ehehehe~"
            jump saymore
            $ done = True
            return

# MWAAAHH <3
        elif compliment == "mwah" or compliment == "kissy" or compliment == "xoxo" or compliment == "kiss" or compliment == "chu":
            $ mas_gainAffection(3, bypass=False)
            m 1etsdra "What{nw}"
            m 1wubfd "Oh!"
            m 1fubfa "Is that a kiss... through text?"
            m 1hubfb "How... {w=0.3}innovative, ahaha!"
            if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
                m 1tubfa "Let me return the favor then..."
                window hide
                show monika 1dubfa zorder MAS_MONIKA_Z at t11 with dissolve_monika
                pause 2.0
                call monika_kissing_motion_short (initial_exp="1hubfa")
                m 1hubfa "Ehehe~"
                m 1fubfa "I love you, you goof."
                m 3hubfa "I'll be looking forward to one of those text kisses again, hehe~"
                m 1fsbfa "... Though a real one would be nice too."
                jump saymore
                return
            else:
                m 1rusdra "I suppose with our current limiations, I should've figured you'll get creative someday."
                m 1tka "You're just {i}dying{/i} to kiss me, aren't you, [player]?"
                m 1tkbla "..."
                m 3hkblb "Okay, okay! I'm just teasing, haha!"
                m 1fkbla "One day, maybe we'll get to kiss for real."
                m 1hub "Be patient, [player]!"
                jump saymore
                $ done = True
                return

# missing the other girls
        elif compliment == "i miss sayori" or compliment == "i miss yuri" or compliment == "i miss natsuki" or compliment == "i miss the dokis" or compliment == "i miss the other girls" or compliment == "i miss the others" or compliment == "i miss ddlc":
            m 1rksdlc "I kind of understand how you feel, [player]..."
            m 1rud "The girls were a key part of the game, after all.{w=0.5} If not them, this game wouldn't be as interesting as it was."
            m 1euc "Besides, if not for Sayori,{w=0.5}{nw}"
            extend 1eud " we technically wouldn't have ever met in the first place."
            m 1eka "She was the one who introduced the main character to the literature club."
            m 1lkd "And while I do sometimes feel guilt about what I've had to do to her...{w=0.5}{nw}"
            extend 1ekbfa " it was all worth it in the end."
            m 1hubfa "After all, we've got ourselves now. And that's all that matters to me~"
            jump saymore
            return

# spook
        elif compliment == "boo":
            $ mas_gainAffection(1, bypass=False)
            m 1wuo "Ahh!"
            m 1hubfa "You really scared me, ahaha!~"
            m 1tfa "I hope you know I can scare you too, though..."
            stop music
            window hide
            show monika 1tsa
            pause 3
            show layer master:
                zoom 1.0 xalign 0.5 yalign 0 subpixel True
                linear 8 zoom 2.0 yalign 0.15
            $ pause(10)
            show layer master
            $ play_song(persistent.current_track)
            m 1tua "..."
            m 1hua "Just kidding{nw}"
            stop music
            window hide
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.8
            stop sound
            hide screen tear
            call screen dialog(message="Boo!", ok_action=Return())
            show monika 1tfa
            $ play_song(persistent.current_track)
            pause 1.5
            m 1tua "Did I scare you?"
            m 1hubfa "Ehehe~"
            jump saymore
            return

# holiday reaction
        elif compliment == "merry christmas" or compliment == "merry xmas" or compliment == "happy holidays" or compliment == "merry holidays":
            if mas_isD25():
                $ mas_gainAffection(5, bypass=True)
                m 1wubfo "Oh!"
                m 1hubfa "Ehehe~"
                m 1hubfb "Merry Christmas to you too, [player]!"
                m 1eka "I'm really happy you told this to me on this special day, you know?"
                m 1hubfa "It's always so heartwarming to spend holidays with you."
            elif True:
                m 1tksdla "Goofball, did you forget your calendar at home?"
                m 2ekb "It's not Christmas yet, [player]."
                m 1hua "Still, I appreciate your festive spirit!"
                m 1nua "Perhaps you could save it for the occasion, though.{nw}"
                extend 1hua " Ehehe~"
            jump saymore
            return

# ending if compliment other than specified reactions
        else:
            if mas_bad_compliment_base.search(inputcompliment):
                jump mtls_bad_compliment_closing
            if mas_good_compliment_base.search(inputcompliment):
                jump mtls_good_compliment_closing
            if mas_dokis_base.search(inputcompliment):
                jump mtls_dokis_closing
            else:
                pass
            $ mas_gainAffection(1.5, bypass=False)
            $ persistent._mas_has_compliment = inputcompliment.capitalize()
            m 1hua "Is that all you wanted to say, [player]?{nw}"
            $ _history_list.pop ()
            menu:
                m "Is that all you wanted to say, [player]?{fast}"
                "Yes, that's all.":
                    m 3hua "Alright then!"
                    m 1eka "Thank you for sharing a piece of your mind with me.{w=0.5} It truly means the world to me."
                    m 1hua "If you want to say anything else, I'm always all ears, so just ask!"
                    $ done = True
                    return
                "No, I want to say something else.":
                    jump input_compliment
                    return

label mtls_bad_compliment_closing:
    # removed losing affection for bug testing, re enable below
    # bug testing completed without flaws, losing affection re-enabled
    $ mas_loseAffection()
    m 1wfd "[player]!"
    m 2lkc "..."
    m 2lfd "I'm very upset that you didn't take this seriously at all."
    m 2eftdc "That hurt a lot."
    m 2dftdc "..."
    $ done = True
    return

# you made her happy good job great
label mtls_good_compliment_closing:
    $ mas_gainAffection(2.5, bypass=False)
    $ rng_global = renpy.random.randint(1,5)
    if rng_global == 1:
        m 1dkbfa "Oh, [player]..."
        m 1hubfa "I'm really happy about what you said!"
        m 1hkbfa "Ehehe, sorry, I get a bit overexcited sometimes."
        m 5hubfa "You're just a big sweetheart to me, how can I not get overexcited about that?~"
        jump saymore
    if rng_global == 2:
        m 1hkbfu "Hehe, you sweetheart..."
        m 1tkbfu "You seem to be enjoying showering me with kindness, I see~"
        m 3hubla "Well, not that I mind at all!"
        jump saymore
    if rng_global == 3:
        m 1tkbfa "Oh, you..."
        m 1tkbfu "Every day of you saying cute things like that{nw}"
        extend 1hubfb " makes me love you more and more!"
        m 1hubfa "Hehehe~"
        jump saymore
    if rng_global == 4:
        m 1fkbfu "Gosh, you never run out of nice things to say to me, do you?"
        m 1dkbfa "I just can't express how much I love you sometimes, [player]..."
        m 1tubfb "But it seems {i}you{/i} sure know how to express your feelings~"
        m 1hubfa "Ehehe~"
        jump saymore
    if rng_global == 5:
        m 1hkbfu "Gosh [player], you just get cuter and cuter every day!"
        m 1ttbfb "I think I'm gonna get sick from how sweet you are..."
        m 1rksdlc "...{w=1.5}{nw}"
        extend 2hkblsdlb "I'm kidding, hahaha!"
        m 5tkbfsdlu "I could never get sick of you, [mas_get_player_nickname()]..."
        jump saymore
    return

# doki doki!
label mtls_dokis_closing:
    m 1rksdlc "..."
    m 1rksdla "Why are you mentioning the other girls, [player]?"
    m 2hksdla "Getting nostalgic, perhaps?"
    m 1hua "Ehehe, I'm just kidding, [player]."
    m 1eksdla "You can mention the other girls from time to time, if you really want to."
    m 4rssdlb "After all, it wouldn't be fair if only I get to mention them, would it?"
    m 1tubfa "Anyway, let's just focus on each other now..."
    m 1hua "Is that all you wanted to say, [player]?{nw}"
    $ _history_list.pop ()
    menu:
        m "Is that all you wanted to say, [player]?{fast}"
        "Yes, that's all.":
            m 3hua "Alright then!"
            m 1eka "Thank you for sharing a piece of your mind with me.{w=0.5} It truly means the world to me."
            m 1hua "If you want to say anything else, I'm always all ears, so just ask!"
            $ done = True
            return
        "No, I want to say something else.":
            jump input_compliment
            return

label saymore:
    m 1hua "Is that all you wanted to say, [player]?{nw}"
    $ _history_list.pop ()
    menu:
        m "Is that all you wanted to say, [player]?{fast}"
        "Yes, that's all.":
            m 3hua "Alright then!"
            m 1eka "Thank you for sharing a piece of your mind with me.{w=0.5} It truly means the world to me."
            m 1hua "If you want to say anything else, I'm always all ears, so just ask!"
            $ done = True
            return
        "No, I want to say something else.":
            jump input_compliment
            return

# hi there!!!!!!
# how are you doing? have you seen the game called no im not a human yet? no? well go check it out while youre at it! :3

# BIIIIIG ascii of my monika <33!!!!!!!!
# if ur editing this feel free to remove this if its too tacky lol



# ================-=---------------------------===++**++*++++++++++++++=-::.........................................................................:::::-::
# ===================-=---=-======++************+*+++++==-::-=+==++-:............................................................:.::::--::::-::::--:-------
# ===============+++*###*************+++=--::::::::::::::=--=+****+=-+...........................................::--------------:-----::-------------------
# ++*########**#*******+==------------::-::::::::::::::+.=*::::::::.:**.........................:---------------------------------:-------------------------
# ####**+==--------------------------------::::::::::=:=+:::::::::....#:......:---=---------------+*-------------------:::---------:------------------------
# ===-----------------------------------------::::::=:+-:...::--------*-------------=---------------%-----------------------:-------:----------:::::--------
# =============------------------------::::---==----===-------------------------------=--------------#-----------------==---::::------::::::-:--------------
# ==================--------============-====-==---=:#-------------------*#*######%#=---=---------===%#--:-:---------------------------:-:------------------
# ===----==========================================+.*----------------==---:--------#**--++--======--%*#--------------------------------:-------------------
# =+===========================================-===+:*=-=========---#=:-++++++++++++=+#+##+*=+*+====-#**#*--------------------------------------------------
# =====++=================================+++==----=+:#-------------=#=+=====+++++++++=+#++%%%*++++++#*+@%+=#=------:::::-::-:--------------:---------------
# ==========+========+++++==--=======================*-*-----------:-++##%###%%+===+*==++*%#**##***++#*+##+%+*+-+@==-::-::::::::::----=====--::-------------
# +++++=========++====================================++=%%#*==-:-:-=++#+%=--===++++++++++@#****++***##*%##++**+----=@+*:::+-:::::::--::--------------------
# ===================+==================================**=**---+:-=++---*+*#*+++++++++##*+**#*+++++*##*%**###****#*=----#%+::::::::::::::::----------------
# ======+================+===============================#++#+=+##++----==+#%++++##%%###****##*+++++*+#*****####******##*@-%@@-::::::::::::::-::------------
# =+==+==++++================++============++++=====--====-.+*%++*=::::---=+++++**++*******##****++****#***#####%%#%#*#%##---%%@::::::::::::::------------::
# ==========+=+++++++++++++=======+========================+:----+%*++===++++*###*+*****####*%#************##########@**#**#--=@%-:::::::::::::::::::::::::-
# =++========++=======================+===================+#+=-:::::-=##*+=+++=++##%@###*####****************#%%%@@@%#******#--+@%=:::::::::::::::::::::--:-
# =======++=====+==========================+==========+%=#==+--*=--==+++++*#**#%#*****#**#@*************#******##*%@@#%#******--*%@+::::::::::::::::::::----
# +===========+++======+==+==============+++++=+====---=+----*=----=++++#####****#**#***%%****************###***####*%%###***#--=##%*----:::::::-:::::::::::
# ===++==========+++*+++===-======================-+==%---:+#-----==+*####*****###*#***#%************#****#*##***###@@%%%%#***+=-%%#@%-------------:--------
# -=-=====+++++++======+=++==========================+--:=+====---=+##%**%****%#*******#**************#****###**#**##@@@@@##**#-=+##%%---------------------=
# ++++=--=======++++++=========++=======++++++++===+----*#+++++=--##%%+*****###*********##**##********##***###%**####%%@@#%####-+=*##%@:------------=---====
# *+++++++++=---=====================+============#---=+#+++++++=#%%#=+****##**##*****###%###%#********#*##*####*###%%@@@######++=%*###+::-:----------------
# %%%%##**+++++++++=--=======++===========++=++=+#---**#*+++++++#%%+-==**+##**#%#****##@%%%%%%%#*******########%####%%%@@*#####**+%%###%........:::---------
# *###%%%%%%%##*+++++++++=--======+**+++========#-=+--##++++++*#%@*-----=%#**#%#****#%@%%%%@@%@#********########%%##%%%%@*#%###*#+%*%####=++++++++***#######
# :-----=+##%%%%%%%%##**++++++++=--===++++====+*++*%+%*++++++*#%%%+****+%#**#%%#***%@@%%@%@@@@@%********########%%%#%%%%@*#%###+###*##%#@*************+++++*
# ::::::--------=*#%%%%%%@%##***+++++++====++++--#+*#*++++++*#%#%**+***#%**#%%#***%@#++-----+%@@#**##***########%%%%%%%%%######+#*+####%%...:........:::::::
# :::::::--------------=+#%%%%%@@%%%%%%@@@@@@@=-++*##*+++++*#%#@****#**%###%%%###%@++--------+*@%#####***%######%%@@%%%%#######+#*+%%###%...................
# ::::::::::---------------====+#%@@@%%%%%%##+-++*##*+++#++#%##%***#**%%###%%%##%%++----------+%%######*#%#######%@@%%%%#######+#*+%####%...................
# *++=-:::::::---------------=====++++++++++*-++##%*++*#*+#%#*%****##*%%##%%%###%++-----------=#@##%%####@#######%%@@%%%*######*#++%###%:...................
# @@@@%%%%##**+=---------------===++++++++++=+*##%****#**#%%**%*#*####%%##%%%##%*+-------------*@##%#####@##%###%%%@@@@##########+*%#%#@....................
# -###%%%%%@@@@@%%@##**--------===+++++++++++*##%#***##**%%***@##*%%%%%%%#%%%%%%+--------------+@#%%%####@#%%##%%%%@@@@########*@+#%##@@:...................
# .*#-.....:=+#%@%%#+++---------==++++++==+=**#%%****##*#%#**#%%%%%%%%%%##%%%%@*=--------------+@#%%%###%@#%%%%%%%@@@@%############%#@%@....................
# .*#-.....::-+%@%%*+++---------==++++++==++*##%#***#%**%%***#@%%%%%%%%%%@@@%%@+-:-------------*%%%%##%%%%#%%%%%%%@@@@###%#####@*#@@%@@#....................
# .*#:......::+%%%#*+++--------===+++++=++**##%#***###*#%****#@%%%%%%%%##%%*%@@+:::------------%%%%%#%%%@%#%%%%%%%@@@%##%%%####@%#@%@@@.....................
# .*#-.......:+%@%#*+++--------===+++++=++**##%#***#%**%%****#@%%%%%%%*%%%+#=#%+::------------=%%%%%%%%%%%#%%%%%%%@@@###%%%%###%%*@@@@-.....................
# +*#-.......:*%@%%#+++-------====+++++++#+##@%#**##%*#%#***%%@@@@@#%##+###-+-++-::-----------%%@%%%%%%@%%#@@%%%@@@@%##%%%%%@#*%##%@@@......................
# %###*########%@@%#+++-----======+++++++%##%%#**#%%###%***#@@@@@@@@@@%%%####=---::----------+@%@%%%%%@%%%#@@@@@@@@@##%%%%%%@###%#@@@%===.............:..:::
# %%%%#%%%%%%%%@@@@#+++--==-======+++++++##%#%#**#%%*##%###%@@@@@@@@@@@@@@@@#+=-::----------##*@@%%@@@@@@%%@@@@@@@@%#%%%%%%%@#%##@@@@%-.........:.::::::::-+
# ###%%#%%%%%@@@@@%#+++===========+++++++%#####*#%%%*#%%#**%%@*-:-@@@@@-@@@@@@%--::---------=++@@%**%@%*@@@@@@@@@@@##%%%%%%#@@%##@@@%%..........::::::::---*
# **+###****####@@%#+++==========+*++++++%%*%####%%###%%###%%@@:..%*=+@@%#%@==--::-----------==+**##%#+@#@@@@@@@@@##%%%@%%##@%%##@@@%#.......::::::::::----*
# %++#+#++=++**#@%%*+++====+*############%%#@####%%####%%###%%%%@%--%%++*#%.:::---------------=#@@@@%%%#@#%@@@@@@@##@%@%@%###%###@@@%=.:....::::::::::----=*
# #==++*.....*+*%%#+++=====+#%%%%%##%##%%%%%@#####%%%##%%###%%*==+*##**++=-::-:----------------=%%@@@@@@@@@%#@@@@%%%%%@%%@%##@##%@@@%-....::::::::::------=#
# *--+=+.....+++%%#++======+#%%%########%#%%%%####%%%##%%%##%#+::---:::::::::::-----------------.-@@@@#@@@@@%#@@@%%@%@@%%#@%####%@@@%.....::::::::-------==#
# +--===.....+=+###+=======+#%%%%%%%%%%#%#%#%#####%%#%#%%*%#%%+......:::::::::::----------------..%++@@@@@@@@@@@%%@@%@@%@#@@%%%#%@@@%.....::::::-------====#
# +::--=.....+=+##*++======+#%##%%%%%%%#####%+%###@#%%##%%#%%%+:......:::::::::::---------------==.#%+--=#@==%@@@@@%@@@@@#@%@%%#@@@@@.....:::::--------====#
# +::--=.....===##*+=======+################%=%###%@%%%%%%%*+%*+.......:::::::::::-:-------------=+###.--...+@@@@*%-=+%@%%@%@%#@#@@@@.....:::---------====+#
# =..---.....===##+++======+#############*##%=##%%@#@@%%%%%%+..:=.......:.::::::::::::-------------==*#@%@%%%%%%+#+::@@@@%@%@@#@@@%@@.....-:--------======+#
# =..---.....=-=##+*+======*#############+*%@%+##%%#%%@@%@@%#+-...........::::::::::::::-------------===+++%%%%%%=%-:-@@@%@@@%@@@%@@@+:------------======++#
# +.:---.....+-=##**+++===+*#############+*+*%=##@##*%%%@@@@%%%%#:........::::::.--:::::::--------------=**+-:::::-*--#@@@@@@%@@@%@@@=-----------=======+++#
# -::---:..::--=###*+++===++#************++++*++####*#%@@@@%##..............:::::::::::-::----------......--.:-#:--+---@@@@@%@@@@%@@@*--------=========++++#
# --:-----------###*+++===+*#+++++*++++++=+++#%-*#*##*%#%@%%@%+:............::::::::::::::---------..--=..-#.--#---=---@@@@@%@@@@%%@@@-----==========+++++**
# =--===-------=###*+++===+*#*+++++++**++=#%@%@@=####**#%%%%@%@..............::::::::::::::::----=.:=%=-..-=====--*---@@@@@@@@@@@%%@@@**######====++++++++*#
# ===+==========#%##+++===+*#*#**********+%#@@@@#=####**#%%@@@@@:........+....:::::::::::::::-:-+@=*-%+-..:---------=@@%%#@@@%@@@%%@@@%%%%@@+%+++++++++++***
# ===++++++==+++%%##+++===+*###*##*######+%#@@%@@*=###**#%%#@@@@@=........:-:.:::::::-:::::::::-::-=......:---+--#-=%%#%+%@@@%@@@@%@@@@%%%@@+%++++++++++***#
# ####%#%+++++++%%%#+++===+*#*###########*%+@@@%@@+=#*#*%%%#%@@@@@@..........:----::::::::::::::#........:+---#--+*%%##*=@@@@@@@@@%%%@@%%%%@*%+++++++++***##
# ###%%%%+++++++%%%#+++===+*#######+++*####%%%%+%@%+=*#%%*#%#@%@@@@@%...........:::::::::::::--...........:-----*%#%###=#@@@@@%@@@%%@@@%%%%%*%*+++*++*****##
# ##%%%%*+++***####%%%%%*=+*#######+++*#####%%%=+##%++@##*##%%#%@@@@%=-...........:::::::::-:........::.::----==%#####+-@@@@@@@@@@%%@@@===+++**#####+*****##
# ##%%%@#+++**#####%%%%%#=+*#######++**#####%%%%@@#%@%+*##*#%#%#%@@@%-=+..........::::::::...........::::---==+%#####*==@@@@@@@%@@%%%@@#==+++**#####+*****##
# ++#%%%#*++***####%%%%%+++++++++++=++*###%%%%#@@@%@@#%+*###%#%#%%@@%:--==:......:::--*#+............:::--=#%**##*##*++#%@@@@@@@@@@%%%@@***+***#####******##
# %%%@%%******####%%%%%%#%%%##*+++++++++=-==***###%#%%#%#*##%%%##%@@+:::---=#+##+=====---...........::--=#%%**######+-#%@%%%%##+*%@%%%@@#*#+**######+*****##
# +===+*++++**####%%%%%%@@@@@@@@@@@@@@@@@%@%***####%####%%*#%%%##%@-:::::::::-----::::::...........::--+%##***##++==@#%@@#*+==#%@**@-@@@%**-:----====++++**#
# =======++++++*+---=++*@@@@%%%%@@@@@@@@@%@@+**####@*###@%###%%##%%@:::::::::::::::::::-..........::--%%%##**#=-------------------*@#+@@@##*++====-=-=====-*
# @@@@@@@@@@%####%%%%%%%%%%@%@@+########*===***##*+%@%*#@@@@@@###%%%=::::::::::::::::::-..........::-#%%%#**##----------------------%@-@@##%%%%%%%%%%%%@%%##
# @@@@@@@@@@####%%%%%%%%%%%%%@@@-%%@%@@@@%@##%@@%+=-----=@@@.@*##%%%@:::::::::::::::::::..........::-*%%%**##*----------------------@-%@+@---=====++%%%%##*#
# %@%@@@@@@@####%%%%%%%%%%%%%@%@##@%=-------------------#@@%:%*#%#%%%+::::::::::::::::::..........::-=%@%*##*#----------------------#=@@@@=--====--%%%%%%###
# #%%##########%%%%%%%%%%%%%%@=-------------------------%@@@=###%#%%%%:...:.:.:....................::-%%###*#+----------------------%-@+%@@%%%%##+..#%%%%###
# @@@@@@@@@%###%%%%%%%%%%%%%%---------------------------=@@@%#####%#%%%..........::.::::..:........::-#@##**++----------------------@-@+%@@%%%%%+%#%%%%%%#*%
# @@@@@@@@@###%%%%%%%%%%%%%+-----------------------------#@@#*####%#%%==....:::::::::::::.:........:::=%#**==-----------------------@-@##@@*+##%#*#####%##+#
# @@%#%@@@@##%%%%%%%%%%%@@+-------------------------------+%+#######%%:%::::::::::::---:=.:.........::-%+===+-----------------------@%+@=@@#.....**#####%#+#
# @@@@@@@@@##%%%%%%%%%%@@#--------------------------------@=#####%##%%:*-:::--:.....-@@@*...........::-==+=------------------------%=@=@+%%@...=-%+#--:-==--
# ====+++========++*#%%@@--------------------------------%+%#######%##:==:--..:+@@@@@@@@%.::.........::-#====----------------------@+@+%%@%@%--#.%+%..::==::
# =+++++++++++++++++++++=-------------------------------+*%#######%@#@@@@@@@@@@@@@@@@+--=............::-=====+=-------------------#+@=@=@@%%@#=#:%+%....==:.
# ===++++++++++++++++--#-------------------------------+%%########%#%*%@@@@@@@%+--------=..:..........::-#===+==------------------@+@=@#@%@%@+=#.%+#....=+::
# =----=+++++*+-===--+%=----------------=---==------=+%%#########%%#%%=-==--=-----------*..:..........::-+===+==-----------------%=@=@=@%%%@%@:%.%+#....=#..
# @%%%@@@@@@@#++#@%%%%@-----------------=-%=--#=+==#%#%%%%%#%###%@#@=------------------#*..:...........::-*=====-----------------@%#+@%@%%%%@@+%.%+.....=*:.
# @@@@@@@@@@@@%%%@@%%%=-----------------=--%@@@%%#%%%%%%%%%%##%@%#%-------------------==%=.:...........::-=++===----------------@=@=@@@@@%%%%@%%-%#++***%#--
# @@@@@@@@@@@@%%%%@%%@-----------------+----%@@%%%%%%%%@@%%%@@@#%*--------------------=@%#.:............::-#+===---------------+*@+*#@#%@@%%%%@%-@=#%=-+#++=
# @@@@@@@@@@@@%%@%*+++----------------=------+@@@@@@@@@@@%%%%%%%----:------=---::.:::::%%@..::..........::--+===---------------@+@=@+@@%%@@@#%%#%@%%%%%%%%#%
# @@@@@@@@@@@%=+++**=---------------------------=%@@@@@@%+##=.........................-%%@..:............::-*%+---------------%=@=%+@*@%%%@@@####@#%%%%%##%#
# %%%@@@@@@@@@@@%++#@--------------------------------.................................-%%@..::...........::--%=--=@@*---------@+%=@=%@@@%%%%@@@###%%%%%%%%%#
# %%%@%%%%%@@@%@@%%%----------------+---------------:.......%##+++++++++==-:.......@%.:%%%-.::............::--@@@@@@@=-#@=-==%+@=%+@+%%@%%%%%@@@###%%######%
# %%%%%%%%%@@@%@@%%=---------------*---------------:.......-%..........%........:==@#..@%@+.::............:::-#@@@@@@@@@@#-@%@=@=@=@@%%%@%%%%%@@@%##%%#%####
# %%%%%%%%%@@@%@@%#=-------------=+----------------........%-+--......@@.......+.#+@:..#@-..::.............::--=@@@@@@@@@@@@@#@@*#@+@%%%%@%#%%%@@@@##%####%#
# %%%%%%%%%@@%%@@%==------------==----------------........%%#=====++=-@-:.....-%.+@@....%...:::.............::--::..:%@@@@@@@@@@@@@*@%%%%@%##%%#@@@@##%%%*##
# %%%%%%%%%@@%%@@-=------------==#---------------:.......*%:........@--+++++++++*+@@......-::::..............::-=::......#@@@@@@@@@@%@%%%%@%##%##@@@%###%%##
# %%%%%%%%%@@%%@@@%#=--------=====--------------:.......*%......................@*@*.......-:::..............::---:.........=@@@@@@@%@%%%%@%######@@@#%#%%%%