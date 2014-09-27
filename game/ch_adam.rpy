
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman
# Dialog for Adam Demeter


label ch_adam:
    
    if plot_state.adam_met:
        adam 'Hello again, [[player character name]'

    else:
        adam 'Hello, or as the kaldreans say: \"kevey\"! I haven\'t seen you around Concord yet so you must be new here. Welcome! I\'m always happy to meet new people.'
        p '[[Introduce yourself]'
        adam '[[friendly response]'
        $ plot_state.adam_met=True

    label menu_adam:
        menu:
            '[[ask for advice]':
                call adam_advice
            '[[ask about opinions on events]':
                call adam_events
            '[[Ask about VL]':
                call adam_VLTreeStart
            '[[Done talking]':
                jump menu_res
        jump menu_adam

    label adam_advice:
        adam 'In my many years... [[and then gives you useful advice]'
        return

    label adam_events:
        adam '[[Adam offers you his opinions on recent events]'
        return

    label adam_VLTreeStart:
        return

    hide adam
    return
