
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Adam Demeter

label ch_adam:
    show adam at char_pos
    if plot_state.adam_met:
        $ last_dialog = 'Hello again, $ALIAS_FIRST_NAME.'
        adam '[last_dialog]'

    else:
        adam 'Hello, or as the kaldreans say: \"kevey\"! I haven\'t seen you around Concord yet so you must be new here. Welcome! I\'m always happy to meet new people.'
        p '[[Introduce yourself]'
        $ last_dialog = '[friendly response]'
        adam '[last_dialog]'

        $ plot_state.adam_met = True

    label menu_adam:
        menu:
            adam '[last_dialog]'
            '[[ask for advice]':
                call adam_advice
            '[[ask about opinions on events]':
                call adam_events
            '[[Ask about VL]' if plot_state.stage == PlotStage.VL_INFO:
                jump adam_VL_tree_start
            '[[Ask about background]' if plot_state.stage == PlotStage.VL_INFO:
                jump adam_Bg_tree_start
            '[[Alkay sent me]' if plot_state.alkay_talk_adam == True:
                call adam_alkay_dialog
            '[[Done talking]':
                hide adam
                return
        jump menu_adam

        label adam_advice:
            p '[[ask adam for advice]'
            adam 'In my many years... [[and then gives you useful advice]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label adam_events:
            p '[[ask adam about recent events]'
            adam '[[Adam offers you his opinions on recent events]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label adam_alkay_dialog:
            p '[[Alkay sent me]'
            adam '[[enthusiastic. Launches into a story about how they met. More information. Specifically mentions Alkay\'s sacrifices to go against his leaders and stop the fighting.]'
            $last_dialog = '[is there anything else I can help you with?]'
            $ plot_state.adam_alkay_info = InfoGet.SUCCESS
            $ plot_state.alkay_talk_adam = False
            return

        label adam_VL_tree_start:
            p '[[ask about VL]'
            menu:
                adam '[[Recognizes that they are indeed in existence. Asks you what you think about this so-called group]'
                'Sympathize':
                    jump adam_VL_tree_sympathize
                'Disapprove':
                    jump adam_VL_tree_disapprove
            jump menu_adam_vl_info

            label adam_VL_tree_sympathize:  
                p '[[express sympathy with VL]'
                menu:
                    adam '[[agrees that their goals are just, perhaps their methods are not]'               
                    'Violence will get them nowhere':
                        jump adam_VL_tree_nowhere
                    'Care less about their methods':
                        jump adam_VL_tree_care_less

                label adam_VL_tree_nowhere:
                    p '[[Violence will get them nowhere]'
                    adam '[[pensive. Offers perspective from the contact war about that]'
                    $last_dialog = '[is there anything else I can help you with?]'
                    jump menu_adam_vl_info

                label adam_VL_tree_care_less:
                    p '[[care less about their methods]'
                    adam '[[sometimes we have to make concessions for the greater good. VL are simply trying to do what is best.]'
                    $last_dialog = '[is there anything else I can help you with?]'
                    $ plot_state.adam_vl_info = InfoGet.SUCCESS
                    jump menu_adam_vl_info

            label adam_VL_tree_disapprove:
                p '[[express disapproval of VL]'
                adam '[[affirms that their goals are just, and that the kaldrean government won\'t change without some force]'
                $last_dialog = '[is there anything else I can help you with?]'
                jump menu_adam_vl_info

        label adam_Bg_tree_start:
            menu:
                adam '[[speaks about his history, leaving out any details from the first contact conflict. Mentions Alkay]'
                '[[ask about Alkay]':
                    jump adam_Bg_tree_Alkay
                '[[ask about contact conflict]':
                    jump adam_Bg_tree_conflict

            label adam_Bg_tree_Alkay:
                adam '[[mentions that he is a dear friend for many years. Mention my name when you talk to Alkay]'
                $last_dialog = '[is there anything else I can help you with?]'
                $ plot_state.adam_talk_alkay = True
                jump menu_adam_vl_info

            label adam_Bg_tree_conflict:
                adam '[[explains more about the conflict but really waters down detail. You sense he is holding information back]'
                $last_dialog = '[is there anything else I can help you with?]'
                jump menu_adam_vl_info

