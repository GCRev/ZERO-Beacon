
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

        p "Actually, I just arrived here so I’m still adjusting to the climate and getting to know people. I’m [alias.full]. Nice to meet you."

        $last_dialog = "Nice to meet you too, " + alias.title_last + ", and welcome to Concord. If you have any questions or comments, don’t hesitate to speak up. I’m always happy to talk."
        
        cole '[last_dialog]'

        $ plot_state.cole_met = True

    label menu_cole:
        menu:
            cole '[last_dialog]'
            'Ask About Cole\'s Background]' if plot_state.stage == PlotStage.VL_INFO:
                jump cole_Bg_tree_start
            'Ask for Advice From Cole]':
                call cole_advice
            'Ask Cole about His Opinions on Recent Events':
                call cole_events
            'Done Talking to Cole':
                hide cole
                return
        jump menu_cole

        label cole_advice:
            p 'Do you have any advice for a citizen new to Concord?'
            cole 'Give me a moment (pauses) alright, I’m going to try to keep this concise because no one likes a rambler. 
            Make friends here and give them your trust. Trust is a "give first and receive later" game, so you have to be 
            the one to stick out your neck and offer it.'
            p 'And what happens if they betray you?'
            cole 'C’mon now, I never said you just walk around with your head down and your hands at your sides. 
            You aren’t asking them marry you. You just have to make some concessions in order to gain something out of 
            an acquaintance. Test the waters before you leap in head-first.'
            p 'I can understand that. Thank you Mr. Demarc.'
            cole 'It\'s just Cole.'
            p 'Right, thanks Cole.'
            $ last_dialog = "Anything else, friend?"
            return

        label cole_events:
            p 'So I’ve heard rumors of tensions between the kaldreans and humans here, what do you think is going on?'
            cole 'Rumors don’t speak loudly, son, and in with my older age I do not have the best of hearing any more. 
            So I can’t say that I’ve heard much... Well, actually I have heard some rather harsh things about Irridiss lately.'
            cole 'I don’t really know what to make of it, but I don’t think I’m in much of a place to do anything about it, to 
            be honest. (Chuckles a little bit).' 
            cole 'Why would you ask such a question, just out of curiosity?'
            p 'Oh, just getting a feel for the community is all. Rumors make me uneasy, and I do not like being out of the know'
            cole 'OK then [alias.title_last]. Anything else I can help you with today'
            return      

        label cole_Bg_tree_start:
            p 'So what can you tell me about your past? You seem like you are full of rich stories.'
            cole 'I\’d prefer not to talk about the past - it’s not really something I like to share, 
            and I do not want anyone’s pity. So I really don’t talk about it.'
            p 'Everything alright, Cole?'
            menu:
                cole 'Yes. I’m fine. Anything else I can help you with today'
                'Ask Again':
                    jump cole_Bg_tree_pursue
                'Apologize':
                    jump cole_Bg_tree_apologize

            label cole_Bg_tree_pursue:
                p 'Well, is there anything else you can tell me about the history of this planet? 
                Maybe, when you got here, or what it was like being exposed to the Kaldreans for the first time?'
                $last_dialog = 'Quit your prying! Didn’t they ever teach you any manners growing up? Anyways I think we’re done here.'
                $plot_state.cole_background_info = InfoGet.FAIL
                jump menu_cole

            label cole_Bg_tree_apologize:
                p 'I apologize, I didn’t realize that it was a delicate topic for you.'
                menu:
                    cole 'It\’s ok, I didn’t mean to snap at you. Things weren’t always as easy for you kids. 
                    As my great grandpappy would say, \'Walking to the Academy was uphill, both ways!\' Oh, how he cracked me up.'
                    'Ask Again':
                        jump cole_Bg_tree_pursue
                    'Offer Confidentiality':
                        jump cole_Bg_tree_confidentiality


                label cole_Bg_tree_confidentiality:
                    p 'Well, if you ever have anything you want to share with me, you have my complete confidentiality. 
                    I’d be happy to listen!'        
                    cole 'Well, you seem like a well mannered kid. Here’s a little about Old Cole.'
                    cole 'I was part of Operation Bridge, on the TSS Destroyer Verdict. I was the Gunnery Officer on board. 
                    It was that operation we made first contact with the Kaldreans, actually. Then the fighting began…'
                    cole 'For the most part the Kaldreans were the ones trying to stop the fighting.'
                    cole '...'
                    cole 'But that\’s all water under the bridge, right?'
                    p 'Right! Well thank you very much for sharing on such a fragile topic.'
                    $last_dialog = 'Thank you for listening. Anything else I can help you with today?'
                    $cole_background_info = InfoGet.SUCCESS
                    jump menu_cole
