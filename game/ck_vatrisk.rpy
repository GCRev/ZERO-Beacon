
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