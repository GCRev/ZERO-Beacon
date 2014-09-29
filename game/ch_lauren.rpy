
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lauren Gray

label ch_lauren:
    show lauren at char_pos
    if plot_state.lauren_met:
        $ last_dialog = 'Yes? Oh, it\'s you again.'
        lauren '[last_dialog]'
        
    else:
        lauren 'Welcome. What do you need?'
        p '[[Introduce yourself]'
        lauren 'I\'m Lauren Gray, Manager of Logistics here on Concord [[more canned/dismissive response]'
        p '[[apologies for what appears to be irritation]'

        $ last_dialog = '[If it\'s not related to job-related matters, then please don\'t bother me. I barely get any time off so I try to make the most of it.]'
        lauren '[last_dialog]'
        $ plot_state.lauren_met = True

    label menu_lauren:
        menu:
            lauren '[last_dialog]'
            '[[You notice she is reading something. Show interest]' if plot_state.stage == PlotStage.VL_INFO:
                jump lauren_info_tree_start
            '[[Ask about background]':
                call lauren_background
            '[[ask for advice]':
                call lauren_advice
            '[[ask about opinions on events]':
                call lauren_events
            '[[Done talking]':
                hide lauren
                return
        jump menu_lauren

        label lauren_background:
            p '[[ask about her background]'
            lauren '[[replies that she does not have time to speak with you about non job-related things]'
            $last_dialog = '[Please keep further inquiry to yourself.]'
            return

        label lauren_advice:
            p '[[ask lauren for advice]'
            lauren '[[replies that she does not have time to speak with you about non job-related things]'
            $last_dialog = '[Please keep further inquiry to yourself.]'
            return

        label lauren_events:
            p '[[ask lauren about recent events]'
            lauren '[[replies that she does not have time to speak with you about non job-related things]'
            $last_dialog = '[Please keep further inquiry to yourself.]'
            return
        
        label lauren_info_tree_start:
            p '[[I am quite into literature myself. Might I ask what you are reading?]'
            menu:
                lauren '[[This is a novel by a progressive kaldrean author.]'
                '[[ask her opinion on progressives]':
                    jump lauren_info_tree_progressives
                '[[ask about novel]':
                    jump lauren_info_tree_novel

            label lauren_info_tree_progressives:
                p '[[what is your opinion on these progressive kaldreans?]'
                lauren '[[approves of the movement, but saddened by the force of the oppressing government.]'
                $last_dialog = '[Please keep further inquiry to yourself.]'
                jump menu_lauren

            label lauren_info_tree_novel:
                p '[[ask about novel]'
                menu:
                    lauren '[[Not normally a genre she reads, but highly rated novel. It\'s based off a true story of a kaldrean and human who entered into a relationship during the first contact conflict and had to overcome adversity to stay with one another. Reminds her of of a kaldrean she grew up with: Lorisk]'
                    '[[sympathize]':
                        jump lauren_info_tree_sympathize
                    '[[disapproval]':
                        jump lauren_info_tree_disapproval

                label lauren_info_tree_sympathize:
                    p '[[sympathize with perspective]'
                    lauren '[[Lauren reveals that Lorisk has a human mother and a kaldrean father.]'
                    $ plot_state.lauren_lorisk_info = InfoGet.SUCCESS
                    $last_dialog = '[Please keep further inquiry to yourself.]'
                    jump menu_lauren

                label lauren_info_tree_disapproval:
                    p '[[disapprove]'
                    lauren '[[criticizes you for your thoughlessness]'
                    $ plot_state.lauren_lorisk_info = InfoGet.FAIL
                    $last_dialog = '[Something dismissive that Lauren would say]'
                    jump menu_lauren
