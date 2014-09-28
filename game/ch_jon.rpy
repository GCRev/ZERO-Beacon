
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Jonathan Caise

label ch_jon:
    show jon at char_pos
    if plot_state.jon_met
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
            adam '[last_dialog]'
            '[[lie about hobbies]'
                call jon_hobbies
            '[[ask about VL]'
                call jon_vl
            '[[done talking]'
                hide jon
                return
        jump menu_jon

    label jon_hobbies
        p '[[lies about hobbies]'
        jon '[[speaks about cultural interests and a little about his past]'
        label menu_jon_2
            menu:
                '[[pursue topic of disliking kaldrean govt]'
                    call jon_kald_gov_opinion
                '[[ask about VL]'
                  call jon_actual_vl_info

        label jon_kald_gov_opinion
            p '[[pursue topic of disliking kaldrean govt'
            jon '[[talks about ho they are corrupt]'
            jump menu_jon_2

        label jon_actual_vl_info
            p '[[ask about VL]'
            jon '[[speaks passionately for VL]'
            menu:
                jon '[[speaks passionately for VL]'
                '[[Thanks jon for infos]'
                    call jon_finish
                '[[reassure that you think kaldreans deserve liberation]'
                    call jon_reassure
                '[[you seem quite passionate]'
                    call jon_evade

            label jon_finish
                p '[[Thanks Jon for infos]'
                jon '[[ceases coversation]'
                $jon_vl_info = InfoGet.FAIL

                hide jon
                return

            label jon_evade
                p '[[You seem quite passionate]'
                jon 'I think we\'re done here'
                $jon_vl_info = InfoGet.FAIL

                hide jon
                return

            label jon_reassure
                p '[[reassure that you think kaldreans deserve liberation]'
                jon '[[gives info on VL, and exits]'
                $jon_vl_info = InfoGet.SUCCESS

                hide jon
                return

    label jon_VL
        p '[[ask about VL]'
        jon '[[other uneasy response]'
        menu:
            '[[you seem uneasy]'
                call_jon_uneasy
            '[[go with it]'
                call_jon_go_with_it

        label jon_uneasy
            p '[[you seem uneasy]'
            jon '[[Ceases conversation]'
            $jon_vl_info = InfoGet.FAIL

            hide jon
            return

        label call_jon_go_with_it
            p '[[go with it]'
            jon '[[direct player to talk to kro]'

            hide jon
            return







