
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Noq Kriesk Lask

label ck_noq:
    show noq at char_pos
    if plot_state.noq_met:
        $ last_dialog = 'Hello again, $ALIAS_FIRST_NAME'
        noq '[last_dialog]'

    else:
        noq'[[Yes?]'
        p '[[Introduce self]'
        $last_dialog = '[Very good. Now please be snappy. I am very busy at the moment.]'
        noq '[last_dialog]'

        $plot_state.noq_met = True

    label menu_noq:
        menu:
            noq '[last_dialog]'
            '[[ask about his designs]' if plot_state.stage == PlotStage.VL_INFO:
                call noq_designs
            '[[ask about VL]' if plot_state.stage == PlotStage.VL_INFO:
                call noq_VL
            '[[ask for advice from Noq]':
                call noq_advice
            '[[ask Noq his opinions on recent events]':
                call noq_events
            '[[ask Noq about his background]':
                call noq_background
            '[[done talking to noq]':
                hide noq
                return
        jump menu_noq

        label noq_advice:
            p '[[you ask Noq for advice]'
            noq '[[offers his advice]'
            $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
            return

        label noq_events:
            p '[[you ask Noq his opinion on recent events]'
            noq '[[A rather uninterested discussion about recent events]'
            $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
            return

        label noq_background:
            p '[[you ask Noq on his background]'
            noq '[[offers little information. Does not sound interested in talking about it.]'
            $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
            return

        label noq_designs:
            p '[[you ask Noq about his designs]'
            noq '[[Lightens up and talks for a while about his latest structure.]'
            $last_dialog = '[It\'s refreshing when someone takes an interest in this stuff. I could talk forever about it.]'
            return

        label noq_VL:
            p '[[you ask Noq about VL]'
            noq '[[Does not know the group or what they want - only that they are going about it all wrong. If they want to accomplish anything, they have to bring down the system from the inside out. Threats are not going to get them anywhere]'
            $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
            return
 