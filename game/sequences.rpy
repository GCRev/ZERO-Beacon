
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Scripted sequences

label intro:

    play music "assets/mu_intro.ogg"
    scene bg stars
    show planet_bridge at Position(xpos = 0.5, ypos = 0.75)

    'This is the planet Bridge.'
    'Fifty years ago, humans made first contact there with the kaldreans, an advanced 
    race of insect-like beings.  At first, there was fighting between the two races, 
    but later that year, the two signed a treaty of friendship and peace. '

    'Bridge was settled and the capital city of Concord was constructed. Since then, Concord 
    has served as a shining beacon of peace in which humans and kaldreans live as one.'

    'The peace of Bridge is essential to the peace of the rest of the galaxy. If human-kaldrean 
    relations on the planet break down, then the rest of the galaxy is bound to follow suit.'

    hide planet_bridge

    comm 'And this is why I have called you here today, Agent. The great city 
    of Concord has of late been troubled by political unrest. A mysterious group of rebels known 
    as “Valak Lideri” has infiltrated Bridge’s government, and it has come to my attention that 
    the life of the kaldrean High Ambassador is under threat. '

    comm 'On this assignment, you shall travel to Concord. You will act under alias a diplomat, 
    investigating the situation and learning about Valak Lideri. You will work with Agent Redmont,
    a well-respected special agent such as yourself, who is currently stationed in the city under 
    alias as the scientist Sarah Liu.'

    comm 'Then, when you are ready, it is up to you to take action and apprehend those who plan to 
    cause mayhem in the great city.'

    comm 'Do not take this mission lightly. The people of Bridge will not be so willing to answer 
    the prying questions of an Earthling diplomat. How you decide to act may very well be the difference 
    between order in chaos on Bridge. And if the peace of Bridge should be broken, then it is only a 
    matter of time before the rest of the galaxy falls with it. '

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

    scene bg map

    'After a month-long journey through space, you finally arrive on Bridge. As you come to
    land at the Spaceport, you see Concord below you. The city looks utopian-like, set between a
    shimmering coast and an luscious woodland.'

    scene bg port

    'You dismount your spacecraft, stumbling a bit as you readjust to the feeling of gravity. 
    You emerge in a bustling, noisy port. People mill about all around.'

    'You open your assignment notes, which tell you to meet Agent Redmont in the residences as 
    soon as you arrive.'

    return

label ending_incorrect_plans:
    hide sarah
    "[[Sarah goes to initiate the raid.]"
    "[[Later you find out that you incorrectly identified the rebels' plans. You have failed to apprehend
    the rebels in time]"
    scene bg result1
    jump game_over

label ending_correct_plans:
    stop music
    hide sarah
    "[[Sarah goes to initiate the raid.]"
    scene bg result2
    jump game_over

label ending_too_many_wrong_rebels_identified:
    stop music
    hide sarah
    "[[Sarah goes to initiate the raid.]"
    "[[Later you find out that you identified too many people as rebels that weren't. 
    You have failed to apprehend the rebels in time]"
    scene bg result1
    jump game_over

label ending_not_enough_rebels_identified:
    stop music
    hide sarah
    "[[Sarah goes to initiate the raid.]"
    "[[Later you find out that you didn't identify enough rebels 
    You have failed to apprehend the rebels in time]"
    scene bg result1
    jump game_over

label ending_correct_rebels:
    stop music
    "[[You correctly identified enough rebels]"
    scene bg result2
    jump game_over

label ending_vatrisk_denounce_govt:
    stop music
    scene bg result4
    jump game_over

label ending_vatrisk_lure:
    stop music
    scene black
    "[[Vatrisk trustingly follows you out to the grove, unguarded]"
    play sound "assets/sf_assassination1.ogg"
    "[[After talking for a short time, you hear the blast of a plasma gun]"
    play sound "assets/sf_assassination2.ogg"
    "[[Vatrisk falls to the ground, fatally wounded]"
    scene bg result3
    jump game_over

label game_over:
    stop sound
    $ plot_state.stage = PlotStage.GAME_OVER
    $ renpy.pause()
    return
