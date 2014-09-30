
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Vatrisk Irridiss Kier
   
label ck_vatrisk:
    show vatrisk at char_pos
    if plot_state.vatrisk_met:
        $ last_dialog = 'Hello again, $ALIAS_FIRST_NAME'
        vatrisk '[last_dialog]'

    else:
        vatrisk'[[Welcome to Vivarioss, or as you may know it, Concord. It is absolutely a pleasure to meet you.]'
        p '[[Introduce self]'
        $last_dialog = '[Wonderful. How may my colleague and I be of assistance to you, Mr. $AGENT_LAST_NAME?]'
        vatrisk '[last_dialog]'

        $plot_state.vatrisk_met = True

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
#               ending 4!!!
