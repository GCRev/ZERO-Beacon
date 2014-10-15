
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Cole DeMarc

label ch_cole:
    $ show_ch('cole', 'right')
    if plot_state.cole_met:
        $ last_dialog = "Hey there. How are you faring today, " + alias.title_last + "?"

    else:
        cole "Welcome to my store. What are you looking for today?"
        p "Actually, I just arrived here, so I\'m still adjusting to the climate and getting to know people. I\'m [alias.full]. Nice to meet you."
        $ last_dialog = "Nice to meet you too, " + alias.title_last + ", and welcome to Concord. If you have any questions or comments, don\'t hesitate to speak up. I\'m always happy to talk."
        $ plot_state.cole_met = True

    label menu_cole:
        menu:
            cole '[last_dialog]'
            'Ask Cole about his background' if plot_state.stage == PlotStage.VL_INFO and plot_state.cole_background_info == InfoGet.NO_ATTEMPT:
                jump cole_Bg_tree_start
            'Ask Cole for advice':
                call cole_advice
            'Ask Cole about his opinions on recent events':
                call cole_events
            'Done talking to Cole':
                $ hide_ch('cole', 'right')
                return
        jump menu_cole

        label cole_advice:
            p 'Do you have any advice for a citizen new to Concord?'
            cole 'Give me a moment.'
            cole "Alright, I\'m going to try to keep this concise, because no one likes a rambler."
            cole "Make friends here and give them your trust. Trust is a \"give first and receive later\" game, so you have to be 
            the one to stick out your neck and offer it."
            p 'And what happens if they betray you?'
            cole 'C\'mon now, I never said you just walk around with your head down and your hands at your sides. 
            You aren\'t asking them marry you. You just have to make some concessions in order to gain something out of 
            an acquaintance. Test the waters before you leap in head-first.'
            p 'I can understand that. Thank you, Mr. Demarc.'
            cole 'It\'s just Cole.'
            p 'Right; thanks, Cole.'
            $ last_dialog = "Anything else, friend?"
            return

        label cole_events:
            p 'So I\'ve heard rumors of tensions between the kaldreans and humans here, what do you think is going on?'
            cole 'Rumors don\'t speak loudly, son, and in my older age I do not have the best of hearing any more. 
            So I can\'t say that I\'ve heard much...'

            cole "Well, actually I have heard some rather harsh things about Irridiss lately."
            cole 'I don\'t really know what to make of it, but I don\'t think I\'m in much of a place to do anything about it, to 
            be honest' 
            cole 'Why would you ask such a question, just out of curiosity?'
            p 'Oh, just getting a feel for the community is all. Rumors make me uneasy, and I do not like being out of the know.'
            cole 'Okay then, [alias.title_last]. Anything else I can help you with today?'
            return      

        label cole_Bg_tree_start:
            p 'So what can you tell me about your past? You seem like you are full of rich stories.'
            cole 'I\'d prefer not to talk about the past - it\'s not really something I like to share, 
            and I do not want anyone\'s pity.'
            p 'Everything alright, Cole?'
            menu:
                cole 'Yes. I\'m fine.'
                'Ask Cole about his background again':
                    jump cole_Bg_tree_pursue
                'Apologize':
                    jump cole_Bg_tree_apologize

            label cole_Bg_tree_pursue:
                p 'Well, is there anything else you can tell me about the history of this planet? 
                When you got here or what it was like being exposed to the kaldreans for the first time?'
                $last_dialog = 'Quit your prying! Didn\'t they ever teach you any manners growing up? Anyways ask me whatever you please, so long as it is not about my past.'
                $ plot_state.cole_background_info = InfoGet.FAIL
                jump menu_cole

            label cole_Bg_tree_apologize:
                p 'I apologize, I didn\'t realize that it was a delicate topic for you.'

                cole 'It\'s okay, I didn\'t mean to snap at you. Things weren\'t always as easy for us as kids. Even less so during the contact conflict.'
                menu:
                    cole "As my great granddad would say, \"Walking to the Academy was uphill, both ways!\" Oh, how he cracked me up. Never thought it would stick with me for all these years."
                    'Ask about his background again':
                        jump cole_Bg_tree_pursue
                    'Offer him your confidentiality':
                        jump cole_Bg_tree_confidentiality

                label cole_Bg_tree_confidentiality:
                    p 'Well, if you ever have anything you want to share with me, you have my complete confidentiality. 
                    I\'d be happy to listen.'        
                    cole 'Well, you seem like a well-mannered kid. Here\'s a little about Old Cole.'

                    cole "I was part of Operation Bridge, on the TSS Destroyer {i}Verdict{/i}. I was the Gunnery Officer on board. 
                    It was that operation we made first contact with the kaldreans, actually."

                    cole "Then the fighting began... I lost some of my closest friends that day. A lost some of myself as I watched the {i}Verdict{/i} lose its battle with gravity and fell to Bridge."

                    cole "It was a fight no one wanted, but it was a fight nonetheless. I was unable to forgive the kaldreans for many years."

                    cole "Eventually it became evident that we had both wronged one another, and that it was time I moved on. It was difficult, but I'm past it now."

                    cole "Took my mind off things by applying myself to electronics. Turns out I have a penchant for it. After Uncle Klay opened up his place I was second."

                    cole "I faced the problem head on, and I'm a better person now because of it. Remember not to turn away from your fears, because they will still be there."
                    p 'Right. Well thank you very much for sharing on such a fragile topic.'
                    $ last_dialog = 'Thank you for listening. Anything else I can help you with today?'
                    $ plot_state.cole_background_info = InfoGet.SUCCESS
                    jump menu_cole
