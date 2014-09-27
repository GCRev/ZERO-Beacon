
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman
# Dialog for Adam Demeter


label ch_adam:
    show adam at char_pos
    if plot_state.adam_met:
        adam 'Hello again, $ALIAS_FIRST_NAME'

    else:
        adam 'Hello, or as the kaldreans say: \"kevey\"! I haven\'t seen you around Concord yet so you must be new here. Welcome! I\'m always happy to meet new people.'
        p '[[Introduce yourself]'
        adam '[[friendly response]'
        $ plot_state.adam_met = True

    label menu_adam:
        menu:
            '[[ask for advice]':
                call adam_advice
            '[[ask about opinions on events]':
                call adam_events
            '[[Ask about VL]':
                jump adam_VL_tree_start
            '[[Ask about background]':
                jump adam_Bg_tree_start
            '[[Done talking]':
                return
        jump menu_adam

    label adam_advice:
        adam 'In my many years... [[and then gives you useful advice]'
        return

    label adam_events:
        adam '[[Adam offers you his opinions on recent events]'
        return

    label adam_VL_tree_start:
        p '[[ask about VL]'
        adam '[[Recognizes that they are indeed in existence. Asks you what you think about this so-called group]'
        menu:
            'Sympathize':
                jump adam_VL_tree_sympathize
            'Disapprove':
                jump adam_VL_tree_disapprove
        jump menu_adam

        label adam_VL_tree_sympathize:
            p '[[express sympathy with VL]'
            adam '[[agrees that their goals are just, perhaps their methods are not]'
            menu:
                'Violence will get them nowhere':
                    jump adam_VL_tree_nowhere
                'Care less about their methods':
                    jump adam_VL_tree_care_less

            jump menu_adam
            label adam_VL_tree_nowhere:
                p '[[Violence will get them nowhere]'
                adam '[[pensive. Offers perspective from the contact war about that]'
                jump menu_adam
            label adam_VL_Tree_care_less:
                p '[[care less about their methods]]'
                adam '[[sometimes we have to make concessions for the greater good. VL are simply trying to do what is best.]'
                $ plot_state.adam_vl_info = "success"
                jump menu_adam

        label adam_VL_tree_disapprove:
            p '[[express disapproval of VL]'
            adam '[[affirms that their goals are just, and that the kaldrean government won\'t change without some force]'
            jump menu_adam

    label adam_Bg_tree_start:
        adam '[[speaks about his history, leaving out any details from the first contact conflict. Mentions Alkay]'
        menu:
            '[[ask about Alkay]':
                jump adam_Bg_tree_Alkay
            '[[ask about contact conflict]':
                jump adam_Bg_tree_conflict
        jump menu_adam

        label adam_Bg_tree_Alkay:
            adam '[[mentions that he is a dear friend for many years. Mention my name when you talk to Alkay]'
            $ plot_state.adam_talk_alkay = True
            jump menu_adam

        label adam_Bg_tree_conflict:
            adam '[[explains more about the conflict but really waters down detail. You sense he is holding information back]'
            jump menu_adam

    hide adam
    return
