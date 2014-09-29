
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Scripted sequences

label intro:

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

    comm 'And this is why I have called you here today, Agent $AGENT_NAME. The great city 
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

    comm 'Go now, Agent. You have not failed me yet. Do not let this be the first time you do.'

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
    "[[You incorrectly identified the rebels' plans]"
    jump result1

label ending_correct_plans:
    "[[You correctly identified the rebels' plans]"
    jump result2

label ending_too_many_wrong_rebels_identified:
    "[[You identified too many people as rebels that weren't]"
    jump result1

label ending_not_enough_rebels_identified:
    "[[You didn't identify enough rebels]"
    jump result1

label ending_correct_rebels:
    "[[You correctly identified enough rebels]"
    jump result2


# None of the below labels should be called directly. Instead, the program should call ending_ labels,
#   which will call these appropriately

label result1:
    scene bg result1
    $ plot_state.stage = PlotStage.GAME_OVER
    $ renpy.pause()
    return

label result2:
    scene bg result2
    $ plot_state.stage = PlotStage.GAME_OVER
    $ renpy.pause()
    return

label result3:
    scene bg result3
    $ plot_state.stage = PlotStage.GAME_OVER
    $ renpy.pause()
    return

label result4:
    scene bg result4
    $ plot_state.stage = PlotStage.GAME_OVER
    $ renpy.pause()
    return
