
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman
# Dialog for 

label ck_lorisk:
    show lorisk at char_pos

    if plot_state.lorisk_met:
        $last_dialog = '[Hello again, $PLAYER_FIRST_NAME, how can I help you?]'
        lorisk '[last_dialog]'

    else:
        lorisk '[[happy to see a new face. Greets in several human languages.]'
        p '[[introduce yourself to lorisk]'
        $plot_state.lorisk_met = True
        $last_dialog = '[still beaming. Introduces herself as a senior linguist and interpreter. Welcomes you to Concord.]'
        lorisk '[last_dialog]'

    label menu_lorisk:
        menu:
            lorisk '[last_dialog]'

            '[[ask for advice]':
                call lorisk_advice
            '[[ask about opinions on events]':
                call lorisk_events
            '[[Ask about her background]':
                jump lorisk_VL_tree_start
            '[[Ask about VL]':
                jump lorisk_personal_reasons
            '[[Done talking]':
                hide lorisk
                return
        jump menu_lorisk

        label lorisk_advice:
            p '[[ask lorisk for advice]'
            lorisk '[[gives you some useful advice]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label lorisk_events:
            p '[[ask her opinion on recent events]'
            lorisk '[[gives you her opinion on recent events]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label lorisk_personal_reasons:
            p '[[ask about VL]'
            lorisk '[[does not want to talk about them for personal reasons]'
            $plot_state.lorisk_vl_info = InfoGet.FAIL
            jump menu_lorisk

        label lorisk_VL_tree_start:
            p '[[Ask about lorisk\'s background]'
            menu:
                lorisk '[[steers the conversation away from her backgrounds. Mentions that her parents were both linguists]'
                '[[ask about languages]':
                    jump lorisk_VL_tree_languages
                '[[flatter or something]':
                    jump lorisk_VL_tree_flatter

            label lorisk_VL_tree_languages:
                p '[[ask about languages]'
                menu:
                    lorisk '[[says that she speak a multitude of languages]'
                    '[[ask about traditional dialects]':
                        jump lorisk_VL_tree_dialects
                    '[[ask about which languages]':
                        jump lorisk_VL_tree_list_languages

                label lorisk_VL_tree_dialects:
                    p '[[ask about traditional dialects]'
                    menu:
                        lorisk '[[says that she speak two traditional dialects]'
                        '[[ask what \"Valak Lideri\" means]':
                            jump lorisk_personal_reasons
                        '[[ask about dialect history]':
                            jump lorisk_VL_tree_dialect_history

                    label lorisk_VL_tree_dialect_history:
                        p '[[ask lorisk about dialect history]'
                        lorisk '[[gives a history on the two dialects she knows. Mentions the founding of Beacon and sovereign paradise.]'
                        $last_dialog = '[please ask if you need anything]'
                        $plot_state.lorisk_vl_info = InfoGet.SUCCESS
                        jump menu_lorisk

                label lorisk_VL_tree_list_languages:
                    p '[[ask which languages she speaks]'
                    menu:
                        lorisk '[[do you really want me to list off all the languages I speak]'
                        '[[actually I do]':
                            jump lorisk_VL_tree_list_all_languages
                        '[[no, only joking]':
                            jump lorisk_VL_tree_only_joking

                    label lorisk_VL_tree_list_all_languages:
                        p '[[actually I do]'
                        lorisk '[[lists off all modern languages she speaks excluding traditional dialects]'
                        $last_dialog = '[is there anything else I can help you with?]'
                        $ plot_state.lorisk_vl_info = InfoGet.FAIL
                        jump menu_lorisk

                    label lorisk_VL_tree_only_joking:
                        p '[[I was only joking]'
                        lorisk '[[laughs with you]'
                        $last_dialog = '[is there anything else I can help you with?]'
                        $ plot_state.lorisk_vl_info = InfoGet.FAIL
                        jump menu_lorisk

            label lorisk_VL_tree_flatter:
                p '[[try to charm her]'
                $ plot_state.lorisk_flatter = True
                menu:
                    lorisk '[[finds your attempts to flatter adorable but does not offer any info]'
                    '[[pursue more flattery]':
                        lorisk '[[Alright, that\'s enough. Come back when you\'ve calmed down some.]'
                        hide lorisk
                        return

                    '[[ask about langauges]':
                        jump lorisk_VL_tree_languages