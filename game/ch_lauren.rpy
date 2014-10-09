
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lauren Gray

label ch_lauren:
    show lauren at char_pos
    if plot_state.lauren_met:
        $ last_dialog = 'Yes? Oh, it\'s you again.'        
    else:
        lauren "You must be the recent arrival. My director mentioned you. What was your name, [alias.last]? [alias.full]?"
        p "You got it."
        lauren "I\'m Lauren Gray, manager of logistics here."
        p "It\'s a pleasure to meet you."
        $ last_dialog = "Right. If you have anything you would like to ask, please be snappy."
        $ plot_state.lauren_met = True

    label menu_lauren:
        menu:
            lauren '[last_dialog]'
            'You notice she is reading something. Show interest' if plot_state.stage == PlotStage.VL_INFO:
                jump lauren_info_tree_start
            'Ask about her background':
                call lauren_background
            'Ask for advice':
                call lauren_advice
            'Ask her opinion on recent events':
                call lauren_events
            'Done talking':
                hide lauren
                return
        jump menu_lauren

        label lauren_background:
            p '[[ask about her background]'
            lauren '[[replies that she does not have time to speak with you about non job-related things]'
            $last_dialog = '[Please keep further inquiry to yourself.]'
            return

        label lauren_advice:
            p "Excuse me... sorry, but would you be willing to offer me any advice as I start my work here?"
            lauren "..."             
            p "Ms. Gray?"
             
            lauren "I heard you, I just don\'t really have anything to say."
            lauren "(pauses)"
            lauren "Alright, I suppose I can offer a few words. I work with numbers all day long and I don\'t get out much so I\'m probably not the best
            person to ask. But after working here for a while I\'ve noticed a pattern, like a bell curve in a distribution graph – those who talk too
            much or too little are more or less shut away by society. Like me."
             
            p "Don\'t be too—"
             
            lauren "I wasn\'t done talking. Those who know just when and what to say make it very far very fast. It doesn\'t matter what your race may be,
            it\'s the same for everyone."
             
            p "So— actually, thank you for your advice. I\'ll let you get back to your work."

            $ last_dialog = 'Please keep further inquiry to yourself.'
            return

        label lauren_events:
            p "What is your opinion on this alleged racial tension within Concord?"

            lauren "Do you think that I am going to have a good answer for you?"

            p "I had hoped."

            lauren "Hah! About all I can tell you is that it is silly. I know plenty of kaldreans, none of whom are bothered or riled up by any of this so-called 
            \"tension.\" I would almost think that you\tve been lied to about this, because honestly, I haven\'t noticed anything particularly out of the ordinary. 
            And I work in upper-level management!"

            p "(muttered) Yeah, but upper-level management has pulled the wool over your eyes."

            lauren "What was that?"

            p "Don\'t worry about it. Thank you for your time. I\'ll let you get back to work."

            $last_dialog = "Alright. If you have anything else you want to say, please be brief." 
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
