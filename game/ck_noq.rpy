
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Noq Kriesk Lask

label ck_noq:
    show noq at char_pos

    if plot_state.noq_vl_plan_info == InfoGet.FAIL:
        noq '[[I told you not to bother me.]'
        hide noq
        return

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
            '[[ask about VL]' if plot_state.stage == PlotStage.VL_INFO or plot_state.stage == PlotStage.VL_PLANS:
                jump noq_VL_tree_start
            '[[ask for advice from Noq]':
                call noq_advice
            '[[ask Noq his opinions on recent events]':
                call noq_events
            '[[ask Noq about his background]':
                call noq_background
            '[[ask Noq about his interests]'  if plot_state.stage == PlotStage.VL_PLANS and plot_state.noq_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump noq_interests_tree_start
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

        label noq_VL_tree_start:
            p '[[you ask Noq about VL]'
            $last_dialog = '[[Does not know the group or what they want - only that they are going about it all wrong. If they want to accomplish anything, they have to bring down the system from the inside out. Threats are not going to get them anywhere]'
            if plot_state.stage == PlotStage.VL_PLANS and plot_state.noq_vl_plan_info == InfoGet.NO_ATTEMPT:
                menu:
                    noq '[last_dialog]'
                    '[[ask again]':
                        $ plot_state.noq_vl_plan_info = InfoGet.FAIL
                        jump noq_VL_tree_ask_again
                    '[[drop the topic]':
                        jump menu_noq

            else:
                noq '[last_dialog]'
                $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
                jump menu_noq

            label noq_VL_tree_ask_again:
                p '[[ask Noq again]'
                menu:
                    noq '[[He again asserts he knows nothing, seems frustrated]'
                    '[[Assert that he must know something]':
                        jump noq_VL_tree_assert
                    '[[drop the topic]':
                        jump menu_noq

                label noq_VL_tree_assert:
                    p '[[Assert that he must know something right in Noq\'s pretty face]'
                    noq '[[You annoy me very much. Remove yourself or I will have security remove you for you.]'
                    hide noq
                    return

        label noq_interests_tree_start:
            p '[[ask Noq about his interests]'
            noq '[[He tells you about his love for engineering and mathematics]'
            p '[[How did you become interested?]'
            noq '[[Tell you about his schooling on Qolisk]'
            p '[[And what happened after that?]'
            menu:
                noq '[[Tells you about his background and his failure in the military]'
                '[[ask about opinions of military]':
                    jump noq_interests_tree_opinions
                '[[sympathize]':
                    jump noq_interests_tree_sympathize

            label noq_interests_tree_opinions:
                p '[[ask about opinions of military]'
                menu:
                    noq '[[Happily tells you his dislike for the military. Slips that Alkay shares many of his opinions on the unfairness of kaldrean military and life in general]'
                    '[[Ask about Alkay]':
                        jump noq_interests_tree_opnions_alkay
                    '[[Agree with his opinions]':
                        jump noq_interests_tree_opinions_agree

                label noq_interests_tree_opnions_alkay:
                    p '[[ask about Alkay]'
                    noq '[[Becomes quiet, realizing he has already said too much. Will not talk to you in depth anymore]'
                    $ plot_state.noq_vl_plan_info = InfoGet.SUCCESS
                    $ last_dialog = '[What else?]'
                    jump menu_noq

                label noq_interests_tree_opinions_agree:
                    p '[[agree with his opinions]'
                    noq '[[He suggests you talk to Alkay and Jonathan]'
                    $ plot_state.noq_vl_plan_info = InfoGet.SUCCESS
                    $ last_dialog = '[What else?]'
                    jump menu_noq

            label noq_interests_tree_sympathize:
                p '[[sympathize]'
                noq '[[Becomes frustrated, thinking you are being patronizing. Will tell you no more about his background]'
                $ plot_state.noq_vl_plan_info = InfoGet.SUCCESS
                $ last_dialog = '[You begin to frustrate me.]'
                jump menu_noq

