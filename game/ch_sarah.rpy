
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman
# Dialog for Sarah Liu

label ch_sarah:
    show sarah at char_pos
    if plot_state.stage == PlotStage.ARRIVE:
        call ch_sarah_arrive
    elif plot_state.stage == PlotStage.KALD_GOVT_INFO:
        call ch_sarah_kald_govt_info
    elif plot_state.stage == PlotStage.VL_INFO:
        call ch_sarah_vl_info
    elif plot_state.stage == PlotStage.VATRISK_MEET:
        call ch_sarah_vatrisk_meet
    elif plot_state.stage == PlotStage.VL_PLANS:
        call ch_sarah_vl_plans
    hide sarah
    return

label ch_sarah_arrive:

    sarah "Greetings, $ALIAS_FIRST_NAME. I’m Agent Redmont, but I prefer to stay in character whenever possible, 
    so call me Sarah. I’ve heard that you’re quite the sharp one."

    p "[[Respone; some banter]"

    sarah "[[More idle chat/banter]"

    p "[[More idle chat/banter]"

    sarah "Before we’re able to quell the political unrest, we need to understand it. I’ve arranged it so that you
    now have access to the High Embassy, where you’ll find High Ambassadors Ben Columbus and Vatrisk Irridiss Kier."

    sarah "I want you to go talk to them and learn about the state of the kaldrean government. They may not be very 
    willing to divulge in-depth information, so speak carefully."

    $ plot_state.stage = PlotStage.KALD_GOVT_INFO

    return

label ch_sarah_kald_govt_info:

    sarah "Have you talked to both Ambassadors yet?"

    if plot_state.ben_kald_govt_info == InfoGet.NO_ATTEMPT or plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
        p "No, not yet."
        sarah "Well, what are you waiting for? Come back when you have."
        return

    p "Yes, I have."

    sarah "And?"

    if plot_state.ben_kald_govt_info == InfoGet.SUCCESS:
        p "I was able to get some useful information for Benjamin Columbus."
        p "[[tell Sarah info]"
        sarah "Very interesting. "
    else:
        p "I wasn't able to [[TODO FINISH]"
    return

label ch_sarah_vl_info:
    sarah "[[TODO]"
    return

label ch_sarah_vatrisk_meet:
    sarah "[[TODO]"
    return

label ch_sarah_vl_plans:
    sarah "[[TODO]"
    return
