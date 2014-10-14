
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Sarah Liu

label ch_sarah:
    $ show_ch('sarah', 'left')
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
    $ hide_ch('sarah', 'left')
    return

label sarah_arrive:

    sarah "Greetings. I'm Agent Redmont, but I prefer to stay in character whenever possible, 
    so call me Sarah. I've heard that you\'re quite the sharp one."

    p "If my record is anything to go by."

    sarah "If your record can impress me, then you are definitely fit for this mission."

    p "Diplomat? Ha! It should be a learning experience for all of us."

    sarah "Before we\'re able to quell the political unrest, we need to understand it." 

    sarah "I\'ve arranged it so that you now have access to the High Embassy, where 
    you\'ll find High Ambassadors Ben Columbus and Vatrisk Irridiss Kier."

    sarah "I want you to go talk to them and learn about the state of the kaldrean government. They may not be very 
    willing to divulge in-depth information, so speak carefully."

    $ plot_state.set_stage(PlotStage.KALD_GOVT_INFO)

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
        p "Columbus told me that the kaldrean government is incredibly controlling."

        p "That's why they don't seem to have any problems..."
        sarah "Very interesting! And Irridiss?"
        if plot_state.vatrisk_kald_govt_info == InfoGet.SUCCESS:
            call sarah_kald_govt_info_vatrisk_tell
            sarah "Yes, this is very good to know. Excellent work, Agent."
        else:
            p "I didn't have the same luck with him... he wasn't willing to tell me anything of use."
            sarah "Hmmm, that is unfortunate. At least we have something, though."
    else:
        p "Ambassador Columbus wasn't willing to give me any in-depth information, unfortunately."
        sarah "Yes, that is very unfortunate. I assume you had better luck with Vatrisk, at least?"
        if plot_state.vatrisk_kald_govt_info == InfoGet.SUCCESS:
            p "Yes, I did."
            call sarah_kald_govt_info_vatrisk_tell
            sarah "Yes, this is very good to know. Good work."
        else:
            p "Well... he wasn't very willing to divulge much information either."
            sarah "Dammit. I expected more of you, Agent. Oh well."

    sarah "For your next task: As you know, there are rumors of Ambassador Irridiss' life being
    in danger. The assassination of such an important kaldrean figure would surely
    destabilize our already-fragile inter-racial relations."

    sarah "Unfortunately, Irridiss does not seem to be aware of these rumors, and if he is, he
    does not seem to be taking them seriously. He's been seen walking around the city, unguarded,
    as if there is nothing to fear. We must convince him otherwise."

    sarah "So, I want you to go around the city, and find out information about this mysterious
    rebel group that calls themselves Valak Lideri. Try to learn as much as you can about them,
    finding out whether or not this grave rumor is true."

    sarah "When you've talked to several people and think you're ready, I'll set up an exclusive
    meeting between you and Ambassador Irridiss. By then, you'll hopefully have enough information to 
    convince him to lay low until this threat has passed."

    p "Sounds good."

    $ plot_state.set_stage(PlotStage.VL_INFO)

    return

    label sarah_kald_govt_info_vatrisk_tell:
        p "Vatrisk told me about how the main priority of their government is to keep the people safe."

        p "But to them that means sacrificing their happiness."
        return

label sarah_vl_info:
    menu:
        sarah "Have you gathered enough information to talk to Ambassador Irridiss yet?"
        "Yes, I'm ready.":
            sarah "Okay, I'll arrange for you to meet with him. Head
            to the High Embassy and ask to speak with him."
            p "Will do."
            $ plot_state.set_stage(PlotStage.VATRISK_MEET)
        "No, I still need to talk to some more people.":
            sarah "Okay."
    return

label sarah_vatrisk_meet:
    sarah "Shouldn't you be meeting with Ambassador Irridiss?"
    return

label sarah_attack_just_happened:
    sarah "I heard what happened! Is Vatrisk alright? Is he safe?"
    
    p "Yes, the ambassador is f.ine. We have to find out who the Valak Lideri are and what they are going to do next."

    p "Before it's too late"
   
    sarah "Good idea. You go question people in the city and I'll go prepare a squad to take down the Valak Lideri."

    sarah "Talk to me when you've figured out their plans."
    $  plot_state.set_stage(PlotStage.VL_PLANS)
    return

label sarah_vl_plans:

    menu:

        sarah "Have you found out who the rebels are or what their plan is?"

        "I think I've figured out what their plan is." if plot_state.alkay_vl_plan_told:
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
