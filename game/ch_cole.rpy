
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Cole DeMarc

label ch_cole:
    show cole at char_pos
    if plot_state.cole_met:
        $ last_dialog = "Hey there. How are you faring today " + alias.title_last + "?"
        cole '[last_dialog]'

    else:
        cole "Welcome to my store, what are you looking for today?"

        p "Actually, I just arrived here so I\’m still adjusting to the climate and getting to know people. I\’m [alias.full]. Nice to meet you."

        $last_dialog = "Nice to meet you too, " + alias.title_last + ", and welcome to Concord. If you have any questions or comments, don\’t hesitate to speak up. I\’m always happy to talk."
        
        cole '[last_dialog]'

        $ plot_state.cole_met = True

    label menu_cole:
        menu:
            cole '[last_dialog]'
            '[[ask about Cole\'s background]' if plot_state.stage == PlotStage.VL_INFO:
                jump cole_Bg_tree_start
            '[[ask for advice from Cole]':
                call cole_advice
            '[[ask Cole his opinions on recent events]':
                call cole_events
            '[[done talking to cole]':
                hide cole
                return
        jump menu_cole

        label cole_advice:
            p '[[you ask Cole for advice]'
            cole '[[offers his advice]'
            return

        label cole_events:
            p '[[you ask Cole his opinion on recent events]'
            cole '[[Earnest opinion on recent events.]'
            return      

        label cole_Bg_tree_start:
            p '[[you ask Cole about his backgrounds]'
            menu:
                cole '[[irritated that you asked about background.]'
                '[[Please tell me. Perhaps you can tell me about this other part of your background.]':
                    jump cole_Bg_tree_pursue
                '[[apologize for prying]':
                    jump cole_Bg_tree_apologize

            label cole_Bg_tree_pursue:
                p '[[Please tell me. Perhaps you can tell me about this other part of your background.]'
                cole '[[They shoulda taught you some respet boy.]'
                $last_dialog = '[don\'t you keep tryin to pry.]'
                $plot_state.cole_background_info = InfoGet.FAIL
                jump menu_cole

            label cole_Bg_tree_apologize:
                p '[[apologize for prying]'
                menu:
                    cole '[[sympathetic. Hints that his past was not a happy one]'
                    '[[pursue again]':
                        jump cole_Bg_tree_pursue
                    '[[offer confidentiality]':
                        jump cole_Bg_tree_confidentiality


                label cole_Bg_tree_confidentiality:
                    p '[[offer confidentiality]'        
                    cole '[[offers some info on his background - just regarding his involvement in OpBridge. Mentions how much some kaldreans tried to stop the fighting and failed.]'
                    $last_dialog = '[Not much else I want to tell you. But thank you for time.]'
                    $cole_background_info = InfoGet.SUCCESS
                    jump menu_cole
