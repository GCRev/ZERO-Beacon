
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Alkay Volk Kladir

label ck_alkay:
    show alkay at char_pos
    if plot_state.alkay_met:
        $ last_dialog = 'Hello again, ' + alias.first + ', what can I get you?'
        alkay '[last_dialog]'

    else:
        alkay '[[Welcome to my humble eatery. You must be a new citizen, [alias.address].]'
        p '[[Introduce yourself]'
        $last_dialog = alias.full + '[[, of course! Have a seat, first meal is on the house. We\'ll talk over some good food.]'
        alkay '[last_dialog]'

        $ plot_state.alkay_met = True

    label menu_alkay:
        menu:
            alkay '[last_dialog]'
            '[[ask for advice]':
                call alkay_advice
            '[[ask about opinions on events]':
                call alkay_events
            '[[Ask about VL]' if plot_state.stage == PlotStage.VL_INFO:
                jump alkay_VL_tree_start
            '[[Ask about background]' if plot_state.stage == PlotStage.VL_INFO:
                jump alkay_Bg_tree_start
            '[[Adam sent me]' if plot_state.adam_talk_alkay == True and plot_state.stage == PlotStage.VL_INFO:
                jump alkay_adam_tree_start
            '[[show sympathy with VL]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.adam_alkay_info == InfoGet.SUCCESS and plot_state.alkay_vl_plan_info == InfoGet.NO_ATTEMPT:
                call alkay_VL_plan_sympathy
            '[[accuse Alkay of being involved with VL]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.adam_alkay_info == InfoGet.SUCCESS and plot_state.alkay_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump alkay_VL_accuse_tree_start
            '[[lie about what you know]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.adam_alkay_info == InfoGet.SUCCESS and plot_state.alkay_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump alkay_VL_plan_lie

            '[[Done talking]':
                hide alkay
                return
        jump menu_alkay

        label alkay_advice:
            p '[[ask Alkay for advice]'
            alkay 'In my many years... [[and then gives you useful advice]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label alkay_events:
            p '[[ask Alkay about recent events]'
            alkay '[[Alkay offers you his opinions on recent events]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label alkay_adam_tree_start:
            p '[[Adam sent me]'
            $ plot_state.alkay_adam_info = InfoGet.SUCCESS
            menu:
                alkay '[[enthusiastic. Launches into a story about how they met. More information.]'
                '[[ask about Alkay\'s bitterness]':
                    jump alkay_adam_tree_bitterness
                '[[ask about Alkay\'s hopefulness]':
                    jump alkay_adam_tree_hopefulness

            label alkay_adam_tree_bitterness:
                p '[[ask about Alkay\'s bitterness]'
                menu:
                    alkay '[[explains how the kaldrean gov\'t is difficult to deal with. He\'d much rather be in Vivarioss.]'
                    '[[ask about VL]':
                        jump alkay_adam_tree_bitterness_VL
                    '[[Will things change?]':
                        jump alkay_adam_tree_bitterness_change

                label alkay_adam_tree_bitterness_VL:
                    p '[[ask about VL]'
                    alkay '[[Does not think that VL are the terrorists that everyone thinks they are.]'
                    $last_dialog = '[Is there anything else I can do for you?]'
                    jump menu_alkay

                label alkay_adam_tree_bitterness_change:
                    p '[[Will things change?]'
                    alkay '[[With resolve. They must and they will.]'
                    $last_dialog = '[I think we are close. Now, is there anything else I can do for you?]'
                    jump menu_alkay

            label alkay_adam_tree_hopefulness:
                p '[[ask about hopefulness]'
                alkay '[[explains that things are not as bad as they used to be, and perhaps a great change is on the horizon.]'
                $last_dialog = '[We are close. Now, is there anything else I can do for you?]'
                jump menu_alkay

        label alkay_VL_tree_start:
            p '[[ask about VL]'
            menu:
                alkay '[[seems perturbed by the question. But answers that he has heard of this group.]'
                '[[What does VL mean?]':
                    jump alkay_VL_tree_translate
                '[[Ask about kaldrean history]':
                    jump alkay_VL_tree_history

            label alkay_VL_tree_translate:
                p '[[What does VL mean?]'
                alkay '[[Translates VL for you. Mentions kalaras dialect. Finds it odd that a group should name themselves strangely. Jokes about and won\'t really offer more info]'
                $plot_state.alkay_vl_info = InfoGet.SUCCESS
                $last_dialog = '[Is there anything else you would like to know?]'
                jump menu_alkay

            label alkay_VL_tree_history:
                p '[[Ask about kaldrean history]'
                alkay '[[explains brief history, leaving out how the capital used to be called \"Beacon.\" Mentions something about a \"sovereign paradise.\"]'
                $last_dialog = '[Is there anything else you would like to know?]'
                jump menu_alkay

        label alkay_Bg_tree_start:
            p '[[ask about Alkay\'s background]'
            menu:
                alkay '[[smiles and shares his history, clearly leaving something out - corrupt kaldrean gov\'t]'
                '[[ask about Adam]':
                    jump alkay_Bg_tree_adam
                '[[ask about experiences]':
                    jump alkay_Bg_tree_experiences

            label alkay_Bg_tree_adam:
                p '[[ask about Adam]'
                alkay '[[mentions that he is a dear friend for many years. Mention my name when you talk to Adam]'
                $plot_state.alkay_talk_adam  =True
                $last_dialog = '[He is a good man. What else would you like to know?]'
                jump menu_alkay

            label alkay_Bg_tree_experiences:
                p '[[ask about experiences]'
                alkay '[[smiles and shares more history, still leaving out opinions regarding gov\'t.]'
                $last_dialog = '[What else would you like to know?]'
                jump menu_alkay

        label alkay_VL_plan_sympathy:
            p '[[show sympathy with VL]'
            alkay '[[Alkay suspects something is up when you suddenly show support for the VL]'
            $last_dialog = '[Be careful what you say to others, son. Is there anything else you would like to know?]'
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            return

        label alkay_VL_plan_lie:
            p '[[lie about what you know]'
            alkay '[[immediately spots your lie and will assume that you are liar. Won\'t give information away to liars]'
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            hide alkay
            return

    label alkay_VL_accuse_tree_start:
        p '[[accuse Alkay of being involved with VL]'
        menu:
            alkay  '[[Alkay begins to speak quieter, but doesn\'t deny being VL straight on. 
            You must coerce him to give you more information. If successful, you learn the VL\'s assassination plan.]'
            '[[I\'ve been told what this hardship is like. I want to help things change]':
                jump alkay_VL_accuse_tree_hardship
            '[[threaten to reveal his intent if he does not tell you his plans]':
                jump alkay_VL_accuse_tree_threaten

        label alkay_VL_accuse_tree_threaten:
            p '[[threaten to reveal his intent if he does not tell you his plans]'
            alkay '[[you cannot scare me. Do not make me laugh]'
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            $last_dialog = '[You are holding up the line. Be brief.]'
            jump menu_alkay

        label alkay_VL_accuse_tree_hardship:
            p '[[I\'ve been told what this hardship is like. I want to help things change]'
            if plot_state.lorisk_vl_plan_info == InfoGet.SUCCESS:
                $last_dialog = '[nods in approval, recognizing authenticity. Pauses. I trust you, kid. I can see the spark of change in your eye. By mid morning tomorrow that change will be realized.]'
                jump alkay_VL_accuse_tree_hardship_approval
            else:
                $last_dialog = '[applauds your apparent passion. Detects that you have no basis for this assertion. Questions you.]'
                jump alkay_VL_accuse_tree_hardship_question

        label alkay_VL_accuse_tree_hardship_approval:
            menu:
                alkay '[last_dialog]'
                '[[ask if there is a way to spur revolution without killing Vatrisk]':
                    jump alkay_VL_accuse_tree_hardship_approval_vatrisk
                '[[if you could do it differently how would you?]':
                    jump alkay_VL_accuse_tree_hardship_approval_different

            label alkay_VL_accuse_tree_hardship_approval_vatrisk:
                p '[[ask if there is a way to spur revolution without killing Vatrisk]'
                alkay '[[Chuckles, saying the only way that would ever happen is if Vatrisk came out one day and publicly denounced the kaldrean government. 
                But that\'s not likely to happen any time this millennium.]'
                $last_dialog = '[You have my trust. Is there anything else you want to know?]'
                $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                jump menu_alkay

            label alkay_VL_accuse_tree_hardship_approval_different:
                p '[[if you could do it differently how would you?]'
                alkay '[[You cannot solve problems effectively by simply shooting your way through it. You can only solve them quickly. 
                We have no choice now, but in my years of experience, even the deepest wounds are healed when words close wars]'
                $last_dialog = '[You have my trust. Is there anything else you want to know?]'
                $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                jump menu_alkay

        label alkay_VL_accuse_tree_hardship_question:
            menu:
                alkay '[last_dialog]'
                '[[lie and push that you know what you are talking about]':
                    jump alkay_VL_plan_lie
                '[[admit that you were embellishing, but pursue the change]':
                    jump alkay_VL_accuse_tree_hardship_embellishing

            label alkay_VL_accuse_tree_hardship_embellishing:
                p '[[admit that you were embellishing, but pursue the change]'
                menu:
                    alkay '[[Believes you, but requires further convincing.]'
                    '[[trust me when I say this is important to me]':
                        jump alkay_VL_accuse_tree_hardship_embellishing_important
                    '[[you don\'t have to believe me. But I AM on speaking terms with Irridiss. That is a fact.]':
                        jump alkay_VL_accuse_tree_hardship_embellishing_irridiss

                label alkay_VL_accuse_tree_hardship_embellishing_irridiss:
                    p '[[you don\'t have to believe me. But i AM on speaking terms with Irridiss]'
                    alkay '[[Alkay: laughs. I suppose you know then that the Ambassador always takes a stroll through the grove at sunrise. 
                    Sometimes we talk. Now be on your way. I have a line out the door]'
                    $last_dialog = '[You have my trust. Is there anything else you want to know?]'
                    $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                    jump menu_alkay

                label alkay_VL_accuse_tree_hardship_embellishing_important:
                    p '[[trust me when I say this is important to me]'
                    alkay '[[It is important to us too. That does not suddenly gain you access a change you cannot comprehend.]'
                    $last_dialog = '[Keep your head down. Is there anything else you want to know?]'
                    $plot_state.alkay_vl_plan_info = InfoGet.FAIL
                    jump menu_alkay
