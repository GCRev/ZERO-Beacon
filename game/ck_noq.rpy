
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Noq Kriesk Lask

label ck_noq:
    $ show_ch('noq', 'left')

    if plot_state.noq_vl_plan_info == InfoGet.FAIL:
        noq '[[I told you not to bother me.]'
        $ hide_ch('noq', 'left')
        return

    if plot_state.noq_met:
        $ last_dialog = 'Kevey, ' + alias.title_last + '. Please make your questions quick.'
        noq '[last_dialog]'
    else:
        noq "Yes?"
        p "I\'m [alias.full]. Nice to meet you."
        noq "Very good. Now please be snappy. I am very busy at the moment."
        p "Alright. I simply wanted to—"
        $ last_dialog = "My apologies for my irritability. I have to meet deadlines; I wish I had more time to talk. If you have any questions just make them quick." 
        noq '[last_dialog]'
        $plot_state.noq_met = True

    label menu_noq:
        menu:
            noq '[last_dialog]'
            'Ask Noq about his designs' if plot_state.stage == PlotStage.VL_INFO:
                call noq_designs
            'Ask about Valak Lideri' if plot_state.stage == PlotStage.VL_INFO or plot_state.stage == PlotStage.VL_PLANS:
                jump noq_VL_tree_start
            'Ask Noq for advice':
                call noq_advice
            'Ask Noq about his opinions on recent events':
                call noq_events
            'Ask Noq about his background':
                call noq_background
            'Ask Noq about his interests'  if plot_state.stage == PlotStage.VL_PLANS and plot_state.noq_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump noq_interests_tree_start
            'Done talking to Noq':
                $ hide_ch('noq', 'left')
                return
        jump menu_noq

        label noq_advice:
            p "Would you mind sharing some advice?"
            noq "Normally I wouldn\'t, but right now I am very busy. I have a deadline that I need to meet and right now I\'m in the zone."
            p "Perhaps later then."
            noq "Perhaps"
            p "Alright"
            $last_dialog = 'Anything else? Or shall I be on my way?'
            return

        label noq_events:
            p "What do you think about the whole \"tension between kaldreans and humans\" supposedly here on Concord?"
            
            noq "Ha. I was not aware of this. But that is probably because I do not pay mind to such matters. Clearly it is so obscure that it is not a real problem."

            p "Alright then. I think that's clear enough. I'll let you get back to work."

            $last_dialog = "I really am quite busy. I would appreciate it if you returned later."

            return

        label noq_background:
            p '[[you ask Noq on his background]'
            noq '[[offers little information. Does not sound interested in talking about it.]'
            $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
            return

        label noq_designs:
            p '[[you ask Noq about his designs]'
            noq '[[Lightens up and talks for a while about his latest structure.]'
            $last_dialog = '[It\'s refreshing when someone takes an interest in my work. I could talk forever about it.]'
            return

        label noq_VL_tree_start:
            p "Would you happen to know anything about Valak Lideri?"

            noq "You could ask anyone and they would be likely to give you a better answer than I."

            noq "Everyone knows about them just no one knows who they are or what they want. Kind of impractical for what is deemed a \"rebel group\" if you ask me."

            noq "What was their most recent thing? A threat? Are they going to kill someone to make their point? How elementary."

            noq "If they want to accomplish anything, they will have to re-think their strategy."

            noq "All I see right now are tactical decisions - they might work in the short term, but they will fail long term."

            noq "Our government has a strong outer shell but a weak internal structure - they should really focus on that instead."

            p "You seem like you know quite a lot this."

            noq "I dislike our government. But I'll deal with it as long as they no longer force obligations down my throat and then mock me when I am incapable."

            p "I'm sorry I asked."

            noq "Just don't ask. Let's avoid talking about my not-so-spectacular military past."

            $last_dialog = "If you have anything else to say, make it fast. I have to finish up these designs."
            if plot_state.stage == PlotStage.VL_PLANS and plot_state.noq_vl_plan_info == InfoGet.NO_ATTEMPT:
                menu:
                    noq '[last_dialog]'
                    '[[ask again]':
                        $ plot_state.noq_vl_plan_info = InfoGet.FAIL
                        jump noq_VL_tree_ask_again
                    '[[drop the topic]':
                        jump menu_noq

            else:
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
                    $ hide_ch('noq', 'left')
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

