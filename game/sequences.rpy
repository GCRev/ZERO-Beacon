
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Scripted sequences

label intro:
    stop music
    play music "assets/mu_intro.ogg"
    scene bg stars with squares
    show planet_bridge at Position(xpos = 0.5, ypos = 0.75)

    'This is the planet Bridge.'
    'Fifty years ago, humans made first contact there with the kaldreans, an advanced 
    race of insect-like beings.'

    'At first, there was fighting between the two races, 
    but later that year, the two signed a treaty of friendship and peace. '

    'Bridge was settled and the capital city of Concord was constructed. Since then, Concord 
    has served as a shining beacon of peace in which humans and kaldreans live as one.'

    'The peace of Bridge is essential to the peace of the rest of the galaxy. If human-kaldrean 
    relations on the planet break down, then the rest of the galaxy is bound to follow suit.'

    hide planet_bridge

    comm 'And this is why I have called you here today, Agent. The great city 
    of Concord has of late been troubled by political unrest.'

    comm 'A mysterious group of rebels known as \"Valak Lideri\" has infiltrated Bridge\'s government and has induced tensions between humans and kaldreans.'

    comm 'It has come to my attention that the life of the kaldrean High Ambassador may be under threat from this group.'

    comm 'On this assignment, you shall travel to Concord. You will act under alias a diplomat, 
    investigating the situation and learning about Valak Lideri.'

    comm 'You will work with Agent Redmont, a well-respected special agent such as yourself, who is currently stationed in the city under 
    alias as the scientist Sarah Liu.'

    comm 'Then, when you are ready, it is up to you to take action and apprehend those who plan to 
    cause mayhem in the great city.'

    comm 'Do not take this mission lightly. The people of Bridge will not be so willing to answer 
    the prying questions of an Earthling diplomat.' 

    comm 'How you decide to act may very well be the difference 
    between order in chaos on Bridge.' 

    comm 'And if the peace of Bridge should be broken, then it is only a 
    matter of time before the rest of the galaxy falls with it.'

    comm 'Before you go, you must complete your alias as a diplomat.'

    python:
        menu_items = [(gend_to_str(gend), gend) for gend in [Gender.FEM, Gender.MASC, Gender.NEUT]]
        while True:
            renpy.say(comm, 'What gender will your alias be?')
            gender = renpy.display_menu(menu_items)
            renpy.say(comm, 'And what will your first and last name be?')
            first = renpy.input('First name: ')
            last = renpy.input('Last name: ')
            alias = Alias(gender, first, last)
            if "professor" in first.lower() or "moriarty" in first.lower() or "professor" in last.lower() or "moriarty" in last.lower():
                renpy.say(comm, 'Sorry, that codename is reserved for one of our top stealth couriers. You will have choose another alias.')
            else:
                renpy.say(comm, 'So, to confirm, you will be the diplomat [alias.title_full]. Yes?')
                if renpy.display_menu([("That's correct.", True), ("No; I've changed my mind.", False)]):
                    break
    comm 'Very good. It is time for you to get going, then, Agent.'
    comm 'You have not failed me yet. Do not let this be the first time you do.'

    scene bg map with squares

    'After a month-long journey through space, you finally arrive on Bridge. As you come to
    land at the Spaceport, you see Concord below you.' 

    'The city appears Utopian, set between a shimmering coast and an luscious jungle.'
    'Your ship descends to the Spaceport.'

    play music "assets/mu_port.ogg"
    scene bg port with fade

    'You dismount your spacecraft, stumbling a bit as you readjust to the feeling of gravity. 
    You emerge in the bustling, noisy spaceport. People mill about all around.'

    'You open your assignment notes, which tell you to meet Agent Redmont in the Residences as 
    soon as you arrive.'

    return

label ending_incorrect_plans:
    $ hide_ch('sarah', 'left')
    "[[Sarah goes to initiate the raid.]"
    "[[Later you find out that you incorrectly identified the rebels' plans. You have failed to apprehend
    the rebels in time]"
    jump result_1

label ending_correct_plans:
    $ hide_ch('sarah', 'left')
    "[[Sarah goes to initiate the raid.]"
    jump result_2

label ending_too_many_wrong_rebels_identified:
    $ hide_ch('sarah', 'left')
    "[[Sarah goes to initiate the raid.]"
    "[[Later you find out that you identified too many people as rebels that weren't. 
    You have failed to apprehend the rebels in time]"
    jump result_1

label ending_not_enough_rebels_identified:
    $ hide_ch('sarah', 'left')
    "[[Sarah goes to initiate the raid.]"
    "[[Later you find out that you didn't identify enough rebels 
    You have failed to apprehend the rebels in time]"
    jump result_1

label ending_correct_rebels:
    "[[You correctly identified enough rebels]"
    jump result_2

label ending_vatrisk_lure:
    stop music
    scene black
    "[[Vatrisk trustingly follows you out to the grove, unguarded]"
    play sound "assets/sf_assassination1.ogg"
    "[[After talking for a short time, you hear the blast of a plasma gun]"
    play sound "assets/sf_assassination2.ogg"
    "[[Vatrisk falls to the ground, fatally wounded]"
    jump result3

label ending_vatrisk_denounce_govt:
    jump result_4

label result_1:
    $ plot_state.set_stage(PlotStage.GAME_OVER)
    stop music
    play music "assets/mu_title.ogg"
    scene bg result1 with squares
    "[[text]"
    jump credits

label result_2:
    $ plot_state.set_stage(PlotStage.GAME_OVER)
    stop music
    play music "assets/mu_title.ogg"
    scene bg result2 with squares
    "[[text]"
    jump credits

label result_3:
    $ plot_state.set_stage(PlotStage.GAME_OVER)
    stop music
    play music "assets/mu_title.ogg"
    scene bg result3 with squares
    "[[text]"
    jump credits

label result_4:
    $ plot_state.set_stage(PlotStage.GAME_OVER)
    stop music
    play music "assets/mu_title.ogg"
    "[[text]"
    scene bg result4 with squares
    jump credits

label credits:
    "Thank you for playing Beacon."
    "Made by ZERO Studios:\n
    Graham Held -- Art, world design, dialog.\n
    Garret Holman -- Sound, design, dialog.\n
    Kyle McCormick -- Programming, game design, dialog."
    "Additional contributions:\n
    Jesse Colford -- Introduction and Grand Marketplace music\n
    Calum Briggs, Thomas Brown IV -- Design advice"
    "Created using The Ren'Py Visual Novel Engine (http://www.renpy.org)."
    "Please see documentation for citations to non-original assets."
    return
