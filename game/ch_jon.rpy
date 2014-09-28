
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Jonathan Caise

label ch_jon:
    show jon at char_pos
    if plot_state.jon_met:
        $ last_dialog = 'Hello again, $ALIAS_FIRST_NAME'
        jon '[last_dialog]'

    else:
        jon'[[typical intro stuff]'
        p '[[Introduce self]'
        $last_dialog = '[uneasy response]'
        jon '[last_dialog]'

        $plot_state.jon_met = True

    label menu_jon:
        menu:
            jon '[last_dialog]'
            '[[lie about hobbies]':
                jump jon_hobbies_tree_start
            '[[ask about VL]':
                jump jon_VL_tree_start
            '[[ask for advice from Jon]':
                call jon_advice
            '[[ask Jon his opinions on recent events]':
                call jon_events
            '[[ask Jon about his background]':
                call jon_background
            '[[done talking to jon]':
                hide jon
                return
        jump menu_jon

        label jon_advice:
            p '[[you ask Jon for advice]'
            jon '[[offers his advice]'
            return

        label jon_events:
            p '[[you ask Jon his opinion on recent events]'
            jon '[[A rather uninterested discussion about recent events]'
            return

        label jon_background:
            p '[[you ask Jon on his background]'
            jon '[[offers little information. Does not sound interested in talking about it.]'
            return

        label jon_hobbies_tree_start:
            p '[[lies about hobbies]'
            jon '[[speaks about cultural interests and a little about his past]'
            menu:
                '[[pursue topic of disliking kaldrean govt]':
                    jump jon_hobbies_tree_pursue
                '[[ask about VL]':
                    jump jon_hobbies_tree_VL

            label jon_hobbies_tree_pursue:
                p '[[pursue topic of disliking kaldrean govt'
                jon '[[talks about ho they are corrupt]'
                jump menu_jon

            label jon_hobbies_tree_VL:
                p '[[ask about VL]'
                menu:
                    jon '[[speaks passionately for VL]'
                    '[[Thanks jon for infos]':
                        jump on_hobbies_tree_VL_thank_jon
                    '[[reassure that you think kaldreans deserve liberation]':
                        jump jon_hobbies_tree_VL_liberation
                    '[[you seem quite passionate]':
                        jump jon_hobbies_tree_VL_passionate

                label jon_hobbies_tree_VL_thank_jon:
                    p '[[Thanks Jon for infos]'
                    jon '[[seems relieved that you have decided to end the conversation there. Does not want to speak about it more]'
                    $plot_state.jon_vl_info = InfoGet.FAIL
                    $last_dialog = '[I have enough to worry about. Thinking about VL stresses me out.]'
                    jump menu_jon
                    

                label jon_hobbies_tree_VL_liberation:
                    p '[[reassure that you think kaldreans deserve liberation]'
                    jon '[[seems excited that you think so. Offers a little more info on VL.]'
                    $plot_state.jon_vl_info = InfoGet.SUCCESS
                    $last_dialog = '[The VL are the only ones who seem to notice the corrupt kaldrean government.]'
                    jump menu_jon

                label jon_hobbies_tree_VL_passionate:
                    p '[[You seem quite passionate]'
                    jon '[[Evades and no longer wants to speak about VL.]'
                    $plot_state.jon_vl_info = InfoGet.FAIL
                    $last_dialog = '[I do no wish to talk about VL any more. It makes me uneasy.]'
                    jump menu_jon


        label jon_VL_tree_start:
            p '[[ask about VL]'
            menu:
                jon '[[other uneasy response]'
                '[[you seem uneasy]':
                    jump jon_VL_tree_uneasy
                '[[go with it]':
                    jump jon_VL_tree_go_along

            label jon_VL_tree_uneasy:
                p '[[you seem uneasy]'
                jon '[[angry that the diplomat is accusing him of fallacy. Does not want to talk about VL anymore]'
                $plot_state.jon_vl_info = InfoGet.FAIL
                $last_dialog = '[Don\'t talk to me unless you have something decent to say.]'
                jump menu_jon


            label jon_VL_tree_go_along:
                p '[[go with it]'
                $last_dialog = '[direct player to talk to kro]'
                jon '[last_dialog]'
                jump menu_jon








