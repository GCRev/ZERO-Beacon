
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Vatrisk Irridiss Kier
   
label ck_vatrisk:
    show vatrisk at char_pos

    if plot_state.stage == PlotStage.VATRISK_MEET:
        call vatrisk_meeting
        return

    elif plot_state.vatrisk_met:
        $ last_dialog = 'Hello again, $ALIAS_FIRST_NAME'
        vatrisk '[last_dialog]'

    else:
        vatrisk'[[Welcome to Vivarioss, or as you may know it, Concord. It is absolutely a pleasure to meet you.]'
        p '[[Introduce self]'
        $last_dialog = '[Wonderful. How may my colleague and I be of assistance to you, Mr. $AGENT_LAST_NAME?]'
        vatrisk '[last_dialog]'

        $ plot_state.vatrisk_met = True

    label menu_vatrisk:
        menu:
            vatrisk '[last_dialog]'
            '[[ask for advice from Vatrisk]':
                call vatrisk_advice
            '[[ask Vatrisk his opinions on recent events]':
                call vatrisk_events
            '[[ask Vatrisk about his background]':
                call vatrisk_background
            '[[flatter]' if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
                call vatrisk_flatter
            '[[bribe]' if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
                jump vatrisk_bribe
            '[[intimidate/lie/something]' if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
                jump vatrisk_intimidate
            '[[Tell him about VL and why they want to kill him]' if plot_state.stage == PlotStage.VL_PLANS:
                jump vatrisk_VL_inform_tree_start
            '[[Suggest that he publicly denounce kaldrean government]' if plot_state.stage == PlotStage.VL_PLANS:
                jump vatrisk_VL_denounce
            '[[Offer to join him when he goes for his walk in the grove.]' if plot_state.alkay_vl_plan_info == InfoGet.SUCCESS:
                jump vatrisk_VL_lure
            '[[done talking to Vatrisk]':
                hide vatrisk
                return
        jump menu_vatrisk

        label vatrisk_advice:
            p '[[you ask Vatrisk for advice]'
            vatrisk '[[offers his advice]'
            return

        label vatrisk_events:
            p '[[you ask Vatrisk his opinion on recent events]'
            vatrisk '[[A rather politically-minded dodge about those recent events.]'
            return

        label vatrisk_background:
            p '[[you ask Vatrisk on his background]'
            vatrisk '[[offers little information. Does not sound interested in talking about it.]'
            return

        label vatrisk_flatter:
            p '[[I do not think that anyone understands how hard you work to achieve peace here.]'
            vatrisk '[[Finally someone who understands. Gives you the infos]'
            $plot_state.vatrisk_kald_govt_info = InfoGet.SUCCESS
            return

        label vatrisk_intimidate:
            p '[[Intimidate Vatrisk]'
            vatrisk '[[Your words have no affect on me. Talk to me when you have calmed down, sir.]'
            $plot_state.vatrisk_kald_govt_info = InfoGet.FAIL
            hide vatrisk
            return

        label vatrisk_bribe:
            p '[[I will sex you if you give me info]'
            if plot_state.high_emb_tried_bribe:
                vatrisk '[[I know your type. Bribes cannot phase me.]'
                $plot_state.vatrisk_kald_govt_info = InfoGet.FAIL
                return
            else:
                vatrisk '[[Thank you for the money or something]'
                $plot_state.vatrisk_kald_govt_info = InfoGet.SUCCESS
                $last_dialog = '[Please do not hesitate to ask me anything.]'
                jump menu_vatrisk

        label vatrisk_VL_denounce:
            p '[[you should denounce the kaldrean government.]'
            vatrisk '[[You are crazy, don\'t come back here unless you have something intelligent to say.]'
            $plot_state.vatrisk_trust = TrustLevel.LOW
            hide vatrisk
            return

        label vatrisk_VL_inform_tree_start:
            p '[[Tell him about VL and why they want to kill him]'
            menu:
                vatrisk '[[He seems reluctant to believe you, but asks you to continue]'
                '[[suggest that he publicly denounce kaldrean government]':
                    jump vatrisk_VL_denounce
                '[[ask him about his government, ad what he thinks is best for his people]':
                    jump vatrisk_VL_inform_tree_ask

            label vatrisk_VL_inform_tree_ask:
                p '[[ask him about his government, ad what he thinks is best for his people]'
                vatrisk '[[He speaks about how he believes his government, while caring of the people\'s welfare, is very corrupt and oppressive. But they do keep war from breaking out.]'
                if plot_state.vatrisk_trust == TrustLevel.LOW or plot_state.vatrisk_trust == TrustLevel.MEDIUM:
                    jump vatrisk_VL_inform_tree_no_change

                if plot_state.vatrisk_trust == TrustLevel.HIGH:
                    jump vatrisk_VL_inform_tree_not_sure

                if plot_state.vatrisk_trust == TrustLevel.VERY_HIGH:
                    jump vatrisk_VL_inform_tree_persuade

            label vatrisk_VL_inform_tree_no_change:
                vatrisk '[[But he thinks it\'s best to keep things as they are instead of risking chaos and change.]'
                $last_dialog = '[thank you for talking to me, (Mr. or Ms.) $AGENT_LAST_NAME.]'
                jump menu_vatrisk

            label vatrisk_VL_inform_tree_not_sure:
                menu:
                    vatrisk '[[But he\'s not sure what to do.]'
                    '[[The kaldrean government is weak right now. This rebellion will guarantee the change that your people seek]':
                        vatrisk '[[Nothing is guaranteed. I cannot risk the stability of the government]'
                        jump vatrisk_VL_inform_tree_no_change
                    '[[Your people are depending on you to fix this. Those rebels are just like you and I. They do not really want to kill you, but they will if they must.]':
                        jump vatrisk_VL_inform_tree_persuade

            label vatrisk_VL_inform_tree_persuade:
                p '[[Your people are depending on you to fix this. Those rebels are just like you and I. They do not really want to kill you, but they will if they must.]'
                vatrisk '[[He thinks for a bit, then exclaims, \"It\'s time for me to act.\"]'

                call ending_vatrisk_denounce_govt
                return

        label vatrisk_VL_lure:
            p '[[I will accompany you on your morning walk. We should meet in the center of the grove]'
            if plot_state.vatrisk_trust == TrustLevel.HIGH or plot_state.vatrisk_trust == TrustLevel.VERY_HIGH:
                vatrisk '[[Of course. Ordinarily my guards ask me to stay away from that area, but I trust you.]'
                call ending_vatrisk_lure
                return
            else:
                vatrisk '[[I am sorry, but I will not be going out tomorrow morning as I will be busy.]'
                $last_dialog = '[Again, my apologies. Perhaps another time. Until then, are there any other questions I may answer?]'
                jump menu_vatrisk
                
    label vatrisk_meeting:

        vatrisk "[[Hello, Diplomat $ALIAS_LAST_NAME. How can I help you?]"
        p "[[I want to talk about recent political unrest in the city]"
        vatrisk "[[Oh. I see. But I was told you were here to discuss interstellar trade laws.]"
        p "[[I am sorry but that was not true. I'm here to actually discuss the Valak Lideri. I have evidence that your life may be in danger]"

        vatrisk "[[Really? And what is this evidence?]"

        if plot_state.adam_vl_info == InfoGet.SUCCESS:
            p "[[tell him about info from Adam]"
            vatrisk "[[respond]"
        if plot_state.alkay_vl_info == InfoGet.SUCCESS:
            p "[[tell him about info from Alkay]"
            vatrisk "[[respond]"
        if plot_state.jon_vl_info == InfoGet.SUCCESS:
            p "[[tell him about info from Jon]"
            vatrisk "[[respond]"
        if plot_state.lorisk_vl_info == InfoGet.SUCCESS:
            p "[[tell him about info from Lorisk]"
            vatrisk "[[respond]"

        $ possible_infos = [plot_state.adam_vl_info, plot_state.alkay_vl_info, plot_state.jon_vl_info, plot_state.lorisk_vl_info]
        $ gotten_infos = [info_state for info_state in possible_infos if info_state == InfoGet.SUCCESS]
        $ pct_gotten_infos = float(len(gotten_infos)) / len(possible_infos)

        if pct_gotten_infos == 0:
            p "[[Actually, I don't have any. But believe me anyway pl0x]"

        if pct_gotten_infos < 1.0 / 3.0:
            vatrisk "[[I don't believe you]"
            jump vatrisk_meeting_fail
        elif pct_gotten_infos > 2.0 / 3.0:
            vatrisk "[[I believe you; this is quite convincing]"
            jump vatrisk_meeting_success
        else:
            menu:
                vatrisk "This information is definitely unnerving, but I'm still not entirely convinced. Tell me,
                why should I trust you, an Earthling diplomat who seems to have turned vigilante?"
                "Your people need you more than ever now. You shouldn't take any risks that would leave them helpless in such a time of need.":
                    vatrisk "[[you're right!]"
                    jump vatrisk_meeting_success
                "[[Trust us; we only have your best interests in mind]":
                    vatrisk "[[humans never have had our best interests in mind!]"
                    jump vatrisk_meeting_fail
                "[[These rebels are dangerous enemies of the peace, and you should fear them]":
                    vatrisk "[[noo, I need not fear lawless scum such as them!]"
                    jump vatrisk_meeting_fail

        label vatrisk_meeting_fail:
            vatrisk "[[If you would excuse me, I have a transport to board now.]"
            "The ambassador leaves the room and walks to his personal landing pad to board his transport. 
            You follow him, still trying to dissuade him from leaving the safety of the High Embassy without guard."

            scene bg landing_pad
            "Ignoring your protests, he boards the transport. Soon after it takes off, you hear a deafening blast."
            play sound "assets/sf_attack1.ogg"
            $ renpy.pause(delay=6)
            "[[The ships seems to have been shot! It begins falling]"
            play sound "assets/sf_attack2.ogg"
            "[[Miraculously, the pilot manages to safely land the critically wounded pod on the landing pad.]"
            $ renpy.pause(delay=6)
            "[[Ambassador Kier steps out, clearly shaken, but seemingly uninjured]"
            if pct_gotten_infos < 1.0 / 3.0:
                vatrisk "[[zomg you were right. but how did you know? this makes no sense...]"
                $ plot_state.vatrisk_trust = TrustLevel.MEDIUM
            else:
                vatrisk "[[zomg you were right. thx for trying to save my life]"
                $ plot_state.vatrisk_trust = TrustLevel.HIGH
            jump vatrisk_meeting_end

        label vatrisk_meeting_success:
            vatrisk "[[Well, I was about to leave to board a transport, but based on what you've told me, that 
            doesn\'t seem like a very good idea.]"
            "You and the ambassador sit and talk about the Valak Lideri for a bit longer. Then, you hear a sudden,
            deafening blast from outside Kier\'s office"
            play sound "assets/sf_attack1.ogg"
            $ renpy.pause(delay=6)
            "[[Clearly, some sort of aircraft has been shot in mid-air, and is now plummeting towards the ground]"
            play sound "assets/sf_attack2.ogg"
            $ renpy.pause(delay=6)
            vatrisk "[[zomg that was my transport. you saved my life.]"
            $ plot_state.vatrisk_trust = TrustLevel.VERY_HIGH
            jump vatrisk_meeting_end

        label vatrisk_meeting_end:
            "[[You return to Sarah to discuss what you've witnessed]"
            stop sound
            $ plot_state.stage = PlotStage.ATTACK_JUST_HAPPENED
            return
