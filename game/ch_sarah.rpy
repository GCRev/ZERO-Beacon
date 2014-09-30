
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Sarah Liu

label ch_sarah:
    show sarah at char_pos
    if plot_state.stage == PlotStage.ARRIVE:
        call sarah_arrive
    elif plot_state.stage == PlotStage.KALD_GOVT_INFO:
        call sarah_kald_govt_info
    elif plot_state.stage == PlotStage.VL_INFO:
        call sarah_vl_info
    elif plot_state.stage == PlotStage.VATRISK_MEET:
        call sarah_vatrisk_meet
    elif plot_state.stage == PlotStage.ATTACK_JUST_HAPPENED:
        call sarah_attack_just_happened
    elif plot_state.stage == PlotStage.VL_PLANS:
        call sarah_vl_plans
    hide sarah
    return

label sarah_arrive:

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

label sarah_kald_govt_info:

    sarah "Have you talked to both Ambassadors yet?"

    if plot_state.ben_kald_govt_info == InfoGet.NO_ATTEMPT or plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
        p "No, not yet."
        sarah "Well, what are you waiting for? Come back when you have."
        return

    p "Yes, I have."

    sarah "And?"

    if plot_state.ben_kald_govt_info == InfoGet.SUCCESS:
        p "I was able to get some useful information for Ambassador Columbus."
        p "[[tell Sarah what you've learned about kaldrean gov't from Columbus]"
        sarah "Very interesting! And Kier?"
        if plot_state.vatrisk_kald_govt_info == InfoGet.SUCCESS:
            call sarah_kald_govt_info_vatrisk_tell
            sarah "Yes, this is very good to know. Excellent work, Agent."
        else:
            p "I didn't have the same luck with him... he wasn't willing to tell me anything of use."
            sarah "Hmmm, that is unfortunate. At least we have something, though."
    else:
        p "I wasn't able to get any information from Ambassador Columbus, unfortunately."
        sarah "Yes, that is very unfortunate. I assume you had better luck with Vatrisk, at least?"
        if plot_state.vatrisk_kald_govt_info == InfoGet.SUCCESS:
            p "Yes, I did."
            call sarah_kald_govt_info_vatrisk_tell
            sarah "Yes, this is very good to know. Good work."
        else:
            p "Well... he wasn't very willing to divulge much information either."
            sarah "Dammit. I expected more of you, Agent. Oh well."

    sarah "For your next task: As you know, there are rumors of Ambassador Kier's life being
    in danger. As you know, the asssissination of such an important kaldrean figure would surely
    destabilize our already-fragile inter-racial relations."

    sarah "Unfortunately, Kier does not seem to be aware of these rumors, and if he is, he
    does not seem to be taking them seriously. He's been seen walking around the city, unguarded,
    as if there is nothing to fear. We must convince him otherwise."

    sarah "So, I want you to go around the city, and find out information about this mysterious
    rebel group that calls themselves the Valak Lideri. Try to learn as much as you can about them,
    finding out whether or not this grave rumor is true."

    sarah "When you've talked to several people and think you're ready, I'll set up an exclusive
    meeting between you and Ambassador Kier. By then, you'll hopefully have enough information to 
    convince him to lay low until this threat has passed."

    p "Sounds good."

    $ plot_state.stage = PlotStage.VL_INFO

    return

    label sarah_kald_govt_info_vatrisk_tell:
        p "[[tell Sarah what you've learned about kaldrean gov't from Ben]"
        return

label sarah_vl_info:
    menu:
        sarah "Have you gathered enough information to talk to Ambassador Kier yet?"
        "Yes, I'm ready.":
            sarah "Okay, I'll arrange for you to meet with him. Head
            to the High Embassy and ask to speak with him."
            p "Will do."
            $ plot_state.stage = PlotStage.VATRISK_MEET
        "No, I still need to talk to some more people.":
            sarah "Okay."
    return

label sarah_vatrisk_meet:
    sarah "Shouldn't you be meeting with Ambassador Kier?"
    return

label sarah_attack_just_happened:
    sarah "[[I heard what happened. panic panic panic panic]"
    p "[[We needa find out who is in the VL and what their plans are ASAP]"
    sarah "[[Good idea. Go around the city and do that. When you think you've
    figured out who they are or what their plans are, come back to me, and I'll organize
    a raid]"
    $  plot_state.stage = PlotStage.VL_PLANS
    return

label sarah_vl_plans:

    menu:

        sarah "Have you found out who the rebels are or what their plan is?"

        "I think I've figured out what their plan is.":
            $ sarah_vl_plans_scenario = -1
            $ sarah_vl_plans_time = -1
            menu:
                sarah "Excellent! So what is it?"
                "[[option # 0 (incorrect)]":
                    $ sarah_vl_plans_scenario = 0
                "[[option # 1 (incorrect)]":
                    $ sarah_vl_plans_scenario = 1
                "[[option # 2 (correct)]":
                    $ sarah_vl_plans_scenario = 2
                "[[option # 3 (incorrect)]":
                    $ sarah_vl_plans_scenario = 3
                "[[option # 4 (incorrect)]":
                    $ sarah_vl_plans_scenario = 4
                "[[option # 5 (incorrect)]":
                    $ sarah_vl_plans_scenario = 5
                "[[option # 6 (incorrect)]":
                    $ sarah_vl_plans_scenario = 6
                "[[option # 7 (incorrect)]":
                    $ sarah_vl_plans_scenario = 7
                "[[option # 8 (incorrect)]":
                    $ sarah_vl_plans_scenario = 8
                "[[option # 9 (incorrect)]":
                    $ sarah_vl_plans_scenario = 9
                "On second thought, I'm not sure.":
                    jump sarah_vl_plans_unsure
            menu:
                sarah "And when do they plan to do this?"
                "Five O'Clock this afternoon.":
                    $ sarah_vl_plans_time = 0
                "Seven O'Clock tonight.":
                    $ sarah_vl_plans_time = 1
                "Midnight tonight.":
                    $ sarah_vl_plans_time = 2
                "Five O'Clock tomorrow afternoon.":
                    $ sarah_vl_plans_time = 3
                "Seven O'Clock tomorrow night.":
                    $ sarah_vl_plans_time = 4
                "Midnight tomorrow.":
                    $ sarah_vl_plans_time = 5
                "On second thought, I'm not sure.":
                    jump sarah_vl_plans_unsure
            menu:
                sarah "[[are you completely sure? you can't guess again.]"
                "Yes.":
                    if sarah_vl_plans_scenario == 2 and sarah_vl_plans_time == 0:
                        jump ending_correct_plans
                    else:
                        jump ending_incorrect_plans
                "On second thought, no, I'm not.":
                    jump sarah_vl_plans_unsure

        "I think I know who they are.":
            python:
                char_names = [
                    "Benjamin Columbus",
                    "Cole Demarc",
                    "Jonathan Caise",
                    "Lauren Gray",
                    "Adam Demeter",
                    "Kro Zalva Ross",
                    "Alkay Volk Kladir",
                    "Noq Kriesk Lask",
                    "Lorisk Nidaria Kol",
                    "Lida Ezekeri Skar"
                ]
                num_chars = len(char_names)
                char_check_states = [(c, False) for c in char_names]
                while True:
                    char_menu_strs = [("[[x] " if cs[1] else "[[ ] ") + cs[0] for cs in char_check_states]
                    menu_items = zip(char_menu_strs, range(num_chars))
                    menu_items.append(("On second thought, I'm not sure.", "cancel"))
                    if len(filter(lambda x: x[1], char_check_states)) >= 2:
                        menu_items.append(("Done", "done"))
                    else: 
                        menu_items.append(("Click to select the suspected rebels.", None))
                    sel_ix = menu(menu_items)
                    if sel_ix == "cancel":
                        renpy.jump('sarah_vl_plans_unsure')
                    elif sel_ix == "done":
                        break
                    else:
                        char_check_states[sel_ix] = (char_check_states[sel_ix][0], not char_check_states[sel_ix][1])
                rebel_indexes = [2, 4, 6, 8]    
                sel_indexes = [i for i in range(len(char_check_states)) if char_check_states[i][1]]
                num_correct_ids = len([i for i in sel_indexes if rebel_indexes.count(i) > 0])
                num_incorrect_ids = len(sel_indexes) - num_correct_ids
                if num_correct_ids < 3:
                    renpy.call('ending_not_enough_rebels_identified')
                elif num_incorrect_ids > 1:
                    renpy.call('ending_too_many_wrong_rebels_identified')
                else:
                    renpy.call('ending_correct_rebels')
        "No, I haven't.":
            sarah "Well, what are you waiting for? We haven't much time."   

    return

    label sarah_vl_plans_unsure:
        sarah "Well come back to me when you are sure. And be quick about it; 
        we don't have much time." 
        return


