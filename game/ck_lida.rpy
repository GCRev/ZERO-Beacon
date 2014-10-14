
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lida Ezekeri Skar

label ck_lida:
    $ show_ch('lida', 'right')
    
    if plot_state.lida_met:
        lida 'Yes?'
        p 'Uh, hello, ma’am. I’m [alias.full]. I -'
        $last_dialog = 'Very good, ' + alias.title_last + '.  If you wish to converse please be concise. I have neither time nor patience for frivolity.'
        lida '[last_dialog]'

    else:
        $last_dialog = 'Yes, ' + alias.title_last + '. Please be brief.'
        lida '[last_dialog]'

    label menu_lida:
        menu:
            lida '[last_dialog]'
            'Mention meeting with Ben' if plot_state.ben_talk_lida and plot_state.lida_convinced == InfoGet.NO_ATTEMPT and plot_state.stage == PlotStage.KALD_GOVT_INFO:
                jump lida_convince_tree
            'Ask Lida for advice':
                call lida_advice
            'Ask Lida about her opinions on recent events':
                call lida_events
            'Done talking to Lida':
                $ hide_ch('lida', 'right')
                return
        jump menu_lida

        label lida_advice:
            p 'Is there any advice that you could offer me?'
            lida 'Keep your mouth closed unless you have something intelligent to say.'
            p 'Alright. Thank you I suppose.'
            $last_dialog = 'Anything else?'
            return

        label lida_events:
            p "Can you tell me anything about the political tension here on bridge?"
            lida "Pay it no mind. Those rumors are nothing but rumors. It is a waste of your time to pay mind to something so absurd."
            p "Okay then."
            $last_dialog = "Make your questions brief."
            return

        label lida_convince_tree:
            p "Ms. Ezekeri, I would implore you to meet with Ambassador Columbus. I cannot understand why you decline such a simple request."

            lida "Oh so I see he's found another fresh one to do whatever he asks? That is just rich."

            menu:
                lida "He has no authority to order me to meet with him. But I'll humor you - so go ahead and make your case [alias.title_last]."
                "Attempt to intimidate Lida":
                    jump lida_convince_tree_intimidate
                "Attempt to flatter Lida":
                    jump lida_convince_tree_flatter

            label lida_convince_tree_intimidate:
                p "Ms. Ezekeri I know that Ambassador Irridiss has called you to meet with Ambassador Columbus. If you refuse to meet with Columbus you are disobeying Irridiss."

                p "That puts you under threat of insubordination charges."
                
                lida "Ha! A threat! You clearly know little about how our system of obligations functions. Please do not make me laugh with your lack of intelligence."
                $plot_state.lida_convinced = InfoGet.FAIL
                $last_dialog = "You thin my patience."
                jump menu_lida


            label lida_convince_tree_flatter:
                p "Ms. Ezekeri I can see that you are very wise - Ambassador Columbus, on of the most important figures in the galaxy, requires your professional input."

                p "He and I both have a deep respect for our elders."

                lida "Hm... very well. You are a sharp one [alias.title_last]. I will accept Ambassador Columbus' request on your word."

                p "On behalf of Columbus and myself, I would like to thank you."
                $plot_state.lida_convinced = InfoGet.SUCCESS
                $last_dialog = "Your respects are kind, "+alias.title_last+". A properly respectful diplomat will be a wonderful addition to Concord. Is there anything else you would like ask?"
                jump menu_lida
