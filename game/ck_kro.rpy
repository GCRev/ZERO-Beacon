
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Kro Zalva Ross

label ck_kro:
    show kro at char_pos
    if plot_state.kro_met:
        $last_dialog = '[(Mr. or Ms.) $AGENT_LAST_NAME, greetings]'
        kro '[last_dialog]'

    else:
        kro '[[Salutations. I am Flight Commander Kro Zalva.]'
        p '[[introduce yourself to Kro]'
        $plot_state.kro_met = True
        $last_dialog = '[If there is anything you would like to know, please ask. Else move on.]'
        kro '[last_dialog]'

    label menu_kro:
        menu:
            kro '[last_dialog]'
            '[[Jon sent me]' if plot_state.jon_talk_kro:
                jump kro_jon_tree_start
            '[[flatter]':
                call kro_flatter
            '[[ask for advice]':
                call kro_advice
            '[[ask about opinions on events]':
                call kro_events
            '[[Ask about her background]':
                call kro_background
            '[[Done talking]':
                hide kro
                return
        jump menu_kro

        label kro_flatter:
            p '[[your ship is so big.]'
            kro '[[slightly amused. Thanks you for your attempt. Schools you a bit on Kaldrean culture and flattery.]'
            $last_dialog = '[Keep the sweet-talk to a minimum.]'
            $plot_state.kro_flatter_info = True
            return

        label kro_advice:
            p '[[ask Kro for advice]'
            kro '[[gives you some useful advice]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label kro_events:
            p '[[ask her opinion on recent events]'
            kro '[[gives you her opinion on recent events]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label kro_background:
            p '[[ask Kro about her background]'
            kro '[[explains about her military history, her position as a Flight Commander, and what that means.]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label kro_jon_tree_start:
            p '[[Jon sent me]'
            menu:
                kro '[[Acknowledges that Jon is a diligent and respectable man. Kro notes that she is worried about his obsession with weapons.]'
                '[[Jon mentioned something about VL. Ask Kro about VL.]':
                    jump kro_jon_tree_VL
                '[[why does obsession worry Kro?]':
                    jump kro_jon_tree_obsession

            label kro_jon_tree_VL:
                p '[[Jon mentioned something about VL. Ask Kro about VL.]'
                kro '[[responds genuinely that she is not familiar with the word\'s meaning. Ask an elder or talk to Lorisk]'
                $last_dialog = '[If there is anything you need, I am at your service (Mr. or Ms.) $AGENT_LAST_NAME].'
                jump menu_kro

            label kro_jon_tree_obsession:
                p '[[why does obsession worry you?]'
                kro '[[in my experience, obsessions are the result of a buried information]'
                $last_dialog = '[If there is anything you need, I am at your service (Mr. or Ms.) $AGENT_LAST_NAME].'
                $plot_state.kro_obsession_info = True
                jump menu_kro
