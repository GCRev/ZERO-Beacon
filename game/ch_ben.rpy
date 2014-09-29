
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Benjamin Columbus

label ch_ben:
    show ben at char_pos
    if plot_state.ben_met:
        if plot_state.ben_talk_lida:
            ben '[[Good to see you again, $AGENT_FIRST_NAME, have you spoken with Lida yet?]'
            if plot_state.lida_convinced == InfoGet.NO_ATTEMPT:
                p '[[I have not]'
                ben '[[Please do, else I cannot hold up my end of our bargain.]'
                return
            elif plot_state.lida_convinced == InfoGet.FAIL:
                p '[[She was too difficult.]'
                ben '[[Then I am sorry, my friend, can\'t give you infos.]'
                ben '[[You can come back and talk any time.]'
                $plot_state.ben_kald_govt_info = InfoGet.FAIL
                $plot_state.ben_talk_lida = False
                return

            else:
                p '[[She will meet with you.]'
                ben '[[Wonderful. Ben gives you the infos.]'
                ben '[[You can come back and talk any time.]'
                $plot_state.ben_kald_govt_info = InfoGet.SUCCESS
                $plot_state.ben_talk_lida = False
                return

        else:
            $ last_dialog = 'How may I be of service $ALIAS_FIRST_NAME?'
            ben '[last_dialog]'
            jump menu_ben

    else:
        ben 'Hello there, I don\'t believe we\'ve met. I\'m Benjamin Columbus, Ambassador of the humans, but you can just call me Benjamin Columubus. And you are?'
        p '$ALIAS_FIRST_NAME'
        ben 'Ah, yes. Welcome to Concord. What can I do for you today?'
        p 'Sarah has informed me about some mysterious underground information, care to elaborate?'
        $last_dialog = '[Go to Lida, see if you can earn her trust and convince her to meet with me]'
        $plot_state.ben_met = True
        $plot_state.ben_talk_lida = True
        ben '[last_dialog]'
        hide ben
        return

    label menu_ben:
        menu:
            ben '[last_dialog]'
            '[[ask for advice from Ben]':
                call ben_advice
            '[[ask Ben his opinions on recent events]':
                call ben_events
            '[[ask Ben about his background]':
                call ben_background
            '[[done talking to Ben]':
                hide ben
                return
        jump menu_ben

        label ben_advice:
            p '[[you ask Ben for advice]'
            ben '[[offers his advice]'
            return

        label ben_events:
            p '[[you ask Ben his opinion on recent events]'
            ben '[[Very obvious politician speak here. Avoids speaking directly about events.]'
            return

        label ben_background:
            p '[[you ask Ben on his background]'
            ben '[[offers little information. Sounds canned to you.]'
            return