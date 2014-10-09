
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lida Ezekeri Skar

label ck_lida:
    show lida at char_pos
    
    if plot_state.lida_met:
        lida 'Yes?'
        p 'Uh, hello, ma’am. I’m [alias.full]. I -'
        $last_dialog = 'Very good, ' + alias.title_last + '.  If you wish to converse please be concise. I have neither time nor patience for frivolity.'
        lida '[last_dialog]'

    else:
        $last_dialog = 'Yes, ' + alias.title_last + '. Please be brief.'
        lida '[last_dialog]'

    label menu_lida:
        menu:
            lida '[last_dialog]'
            '[[meet with Ben dammit]' if plot_state.ben_talk_lida and plot_state.lida_convinced == InfoGet.NO_ATTEMPT and plot_state.stage == PlotStage.KALD_GOVT_INFO:
                jump lida_convince_tree
            '[[ask for advice from Lida]':
                call lida_advice
            '[[ask Lida her opinions on recent events]':
                call lida_events
            '[[ask Lida about her background]':
                call lida_background
            '[[done talking to Lida]':
                hide lida
                return
        jump menu_lida

        label lida_advice:
            p 'Is there any advice that you could offer me?'
            lida 'Keep your mouth closed unless you have something intelligent to say.'
            p 'Alright. Thank you I suppose.'
            lida 'Anything else?'
            return

        label lida_events:
            p '[[you ask Lida her opinion on recent events]'
            lida '[[Very obvious politician speak here. Avoids speaking directly about events.]'
            return

        label lida_background:
            p '[[you ask Lida about her background]'
            lida '[[offers little information. She sounds like she does not want to talk to you.]'
            return


        label lida_convince_tree:
            p '[[meet with Ben dammit]'
            menu:
                lida '[[He has no authority to tell me to meet with him. Convince me or I won\'t]'
                '[[intimidate]':
                    jump lida_convince_tree_intimidate
                '[[flatter]':
                    jump lida_convince_tree_flatter

            label lida_convince_tree_intimidate:
                lida '[[you didn\'t convince me]'
                $plot_state.lida_convinced = InfoGet.FAIL
                $last_dialog = '[you thin my patience.]'
                jump menu_lida


            label lida_convince_tree_flatter:
                lida '[[you convinced me… very nice]'
                $plot_state.lida_convinced = InfoGet.SUCCESS
                $last_dialog = '[Your respects are kind.]'
                jump menu_lida
