
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Jonathan Caise

label ch_jon:
    show jon at char_pos

    if plot_state.jon_vl_plan_info == InfoGet.FAIL:
        jon "Listen, buddy. You take your crazy talk elsewhere."
        hide jon
        return

    if plot_state.jon_met:
        $ last_dialog = "Hello again, " + alias.title_last + ". What brings you here?"
        jon "[last_dialog]"

    else:
        jon "Give me a moment here... HEY! JANS! GET YOUR PEOPLE ON THE TARMAC ASAP. Sorry. Can I help you [alias.address]?"

        p "I\'m just trying to get to know people here."

        jon "New to Concord? Welcome. I\'m Jonathan Caise, manager of logistics here at the port."

        p "[alias.full], diplomat over at the human embassy."

        jon "Greenhorn diplomat? Make sure you really take your time to get to know people."
        jon "I\'ve seen my fair share of people bail and out and leave because Concord is too much a culture shock for them. 
        But you look like you\'ve got a good head on your shoulders."

        p "I\'m determined to leave my footprint here."

        $last_dialog = "Good. I like your motivation. Feel free to ask me questions, but I may have to be quick... my work doesn\'t often give me breaks."

        $plot_state.jon_met = True

    label menu_jon:
        menu:
            jon '[last_dialog]'
            '[[lie about hobbies]' if plot_state.stage == PlotStage.VL_INFO and plot_state.jon_vl_info == InfoGet.NO_ATTEMPT:
                jump jon_hobbies_tree_start
            '[[ask about VL]' if plot_state.stage == PlotStage.VL_INFO and plot_state.jon_vl_info == InfoGet.NO_ATTEMPT:
                jump jon_VL_tree_start
            '[[ask for advice from Jon]':
                call jon_advice
            '[[ask Jon his opinions on recent events]':
                call jon_events
            '[[ask Jon about his background]':
                call jon_background
            '[[show sympathy with the VL]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.kro_obsession_info and plot_state.jon_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump jon_VL_plan_tree_start
            '[[accuse of association with the VL]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.kro_obsession_info and plot_state.jon_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump jon_accuse
            '[[done talking to Jon]':
                hide jon
                return
        jump menu_jon

        label jon_advice:
            p "Do you have any advice for a newcomer like me?"
 
            jon "Hmmm... I want to say something philosophical but nothing is really coming to me."

            jon "Basically, if you want to successfully build friendships here, do your research. 
            If you know someone\'s culture then you\'re more likely than not going to find it simpler to talk to them."
             
            p "And how would I go about this \"research?\""
             
            jon "\I\'m not going to pretend that history and culture is everyone\'s cup of \"vaska\" but for me, 
            it\'s the fascination with it that makes me want to learn more."

            jon "The more you genuinely want to find something out, the more you remember along the way and the more likely you are to recall it later... usually when you need it most."
             
            p "\"Vaska?\""
             
            jon "Oh, sorry... kaldrean beverage that\'s like tea on Earth. Tea doesn\'t grow here, so we had to find some kind of substitute. Alkay\'s place, Oasis, has some of the best in the city."
            
            jon "In general Alkay\'s a good guy to know. If you want some REAL advice, talk to him."
             
            p "I\'ll be sure to check it out. And thank you for your help."

            $last_dialog = "No problem. Is there anything else I can help you with?"
            return

        label jon_events:
            p "Have you heard the talk about mountain racial tensions, have you heard of these?"

            jon "It is just talk, but I have."

            p "What do you think about them?"

            jon "I don\'t really. You really just have to put that kind of stuff aside and focus on the task at hand. If I\'m preoccupied then I start to make errors in my work." 

            jon "And errors in my field of work are unacceptable." 

            jon "Since I do not have much time outside of my work anyway, I just try to make the most of it. I can\'t really do that if I\'m constantly worried about innocuous small talk."

            p "Right, I can certainly agree. Thank you for giving me a moment."

            $last_dialog = "Of course. I\'m happy to answer your questions."

            return

        label jon_background:
            p '[[you ask Jon on his background]'
            jon '[[offers little information. Does not sound interested in talking about it.]'
            return

        label jon_hobbies_tree_start:
            p "Do you have any hobbies? I myself am super into collecting cultural relics."
            
            jon "You too? I'm into that sort of thing, only I specifically focus on firearms. They fascinate me, especially the older ones."

            jon "None of this new-aged single moving part linear motor type stuff - but the real-deal, mechanically operated weapons from the later 20th and early 21st centuries."

            p "I have picked up a few of those myself, nothing too special though."

            jon "Really, what models?"

            p "Hm... I am still having them identified, but I know one is an ACR."

            jon "What a catch! That is a fine piece of machinery. If you haven't searched around for it's service history and stats then I suggest you do." 

            jon "It's always the history and cultural aspects that interest me the most. The more you have looked into a people's culture and history the more you can understand them."

            p "I take it you have also closely studied the kaldrean weapons as well?"

            jon "Oh yes. Theirs are some of the finest I've ever seen. I wish I could find more on their inventors and histories, but the kaldrean government makes that it's nearly impossible."

            p "And why is that?"

            menu:
                jon "In literally every instance of a great weapon's conception they bury the people involved in its creation and assume the idea themselves. It irritates me to no end."
                "Inquire about dislike of kaldrean government":
                    jump jon_hobbies_tree_pursue
                "Ask about Valak Lideri":
                    jump jon_hobbies_tree_VL

            label jon_hobbies_tree_pursue:
                p "Why do they do this to their people? That seems pretty harsh."

                jon "Aren't you supposed to know this, greenhorn? Well... I'm in upper management and they don't tell us anything either. I'll make it easy for you."

                jon "Their government is perfect - a little too perfect if you know what I mean. Really they are so corrupt that they can afford to maintain that kind of image."

                jon "Incidentally it's causing cultural stagnation on a scale the likes of which humanity has never experienced." 

                jon "I hope that the progressive movement on Qolisk does something fast, because if they don't then the kaldreans are at risk of deteriorating."

                jon "The way the government takes cultural movements and crushes them truly makes me sick - it's the slowest and most painful way for a people to die."

                p "I'm genuinely shocked. I'll try to do something about this, but I've talked with the Ambassadors - it could prove challenging."

                jon "Don't expect to get very far. But it's good to know that at least someone else around here recognizes that there is a problem at all."

                $ last_dialog = "I got a little carried away there... Sorry. Is there anything else you would like to ask?"

                jump menu_jon

            label jon_hobbies_tree_VL:
                p "Do you think Valak Lideri are politically charged against the government?"

                jon "That could be said about any rebel group. But yes. Currently it makes sense for an organization like that to start gaining political traction."

                p "But they aren't terrorists."

                jon "Right. From what I've heard, and likely what you've heard as well, they are become a threat as a political influence rather than a violent group."

                jon "Based on what little I know I believe that have a good cause - they want to give the kaldrean progressive movement new life and new force."

                menu:
                    jon "Many kaldreans want to be free of their suppressive controllers - Valak Lideri are are not afraid to do what is right."
                    "Thank Jon for the information":
                        jump jon_hobbies_tree_VL_thank_jon
                    "Reassure that you think kaldreans deserve liberation":
                        jump jon_hobbies_tree_VL_liberation
                    "You seem quite passionate":
                        jump jon_hobbies_tree_VL_passionate

                label jon_hobbies_tree_VL_thank_jon:
                    p "Thank you for the information, Jon."
                    jon "Yeah, well... No problem."
                    $plot_state.jon_vl_info = InfoGet.FAIL
                    $last_dialog = "But I have enough to worry about, so I don't pay mind to such things. Is there anything else you would like to ask me?"
                    jump menu_jon
                    

                label jon_hobbies_tree_VL_liberation:
                    p "I do not want to see the kaldrean people end in a slow deterioration. I think that the kaldrean people deserve liberation from their fate."
                    
                    jon "That's good news. We could use more diplomats who share your our viewpoints working to bring the corruption to justice."
                    
                    jon  "Valak Lideri might be the only way that change will ever happen. No offense, greenhorn, but if I've learned anything working here, it's that politicians will not sway."

                    $plot_state.jon_vl_info = InfoGet.SUCCESS
                    $last_dialog = "Is there anything else that you would like to know?"
                    jump menu_jon

                label jon_hobbies_tree_VL_passionate:
                    p "You seem quite passionate about this topic."

                    jon "Well... I am, of course. Outside of my work I am very interested in history and culture so it pains me to see a culture destroyed like this."

                    jon "And... from what I've heard, Valak Lideri are trying to stop the kaldrean government from destroying their people. I can't help but find their perspective... agreeable"
                    $plot_state.jon_vl_info = InfoGet.FAIL
                    $last_dialog = "I'd prefer not to talk about Valak Lideri - they still make me uneasy. If you have any more questions please be quick, I have to get back to work promptly."
                    jump menu_jon


        label jon_VL_tree_start:
            p "What can you tell me about Valak Lideri?"
            menu:
                jon '[[other uneasy response]'
                '[[you seem uneasy]':
                    jump jon_VL_tree_uneasy
                '[[go with it]':
                    jump jon_VL_tree_go_along

            label jon_VL_tree_uneasy:
                p '[[you seem uneasy]'
                jon '[[angry that the diplomat is accusing him of fallacy. Does not want to talk about VL anymore]'
                $plot_state.jon_vl_info = InfoGet.FAIL
                $last_dialog = '[Don\'t talk to me unless you have something decent to say.]'
                jump menu_jon


            label jon_VL_tree_go_along:
                p '[[go with it]'
                $last_dialog = '[direct player to talk to Kro]'
                $plot_state.jon_talk_kro = True
                jon '[last_dialog]'
                jump menu_jon

        label jon_accuse:
            p '[[accuse of association with VL]'
            jon '[[angry that you made such a heinous assertion. Won\'t speak about VL seriously with you after this point.]'
            $plot_state.jon_vl_plan_info = InfoGet.FAIL
            return

        label jon_VL_plan_tree_start:
            p '[[how sympathy with the VL]'
            menu:
                jon '[[miffed that you are essentially accusing him of being a rebel, but obviously relieved that you sympathize.]'
                '[[bluff that you are aware of VL plans]':
                    jump jon_VL_plan_tree_bluff
                '[[you want galactic change]':
                    jump jon_VL_plan_tree_change

            label jon_VL_plan_tree_bluff:
                p '[[bluff that you are aware of VL plans]'
                jon '[[Jon: accuses YOU of being VL and says he has nothing to do with it. Won\'t speak with you after this point.]'
                $plot_state.jon_vl_plan_info = InfoGet.FAIL
                hide jon
                return

            label jon_VL_plan_tree_change:
                p '[[you want galactic change]'
                menu:
                    jon '[[agrees. Asks you how far you would go for change.]'
                    '[[argue on the side of violence]':
                        jump jon_VL_plan_tree_change_violence
                    '[[not so much about how, but what it is that changes]':
                        jump jon_VL_plan_tree_change_what
                    '[[argue on the side of peace]':
                        jump jon_VL_plan_tree_change_peace

                label jon_VL_plan_tree_change_violence:
                    p '[[argue on the side of violence]'
                    jon '[[agrees that violence acts quickly, but does not create a lasting peace as seen throughout history.]'
                    $plot_state.jon_vl_plan_info = InfoGet.SUCCESS
                    jump menu_jon

                label jon_VL_plan_tree_change_what:
                    p '[[not so much about how, but what it is that changes]'
                    jon '[[agrees that change itself is more important than the means of change.]'
                    $plot_state.jon_vl_plan_info = InfoGet.SUCCESS
                    jump menu_jon

                label jon_VL_plan_tree_change_peace:
                    p '[[argue on the side of peace]'
                    jon '[[agrees that peace is powerful, but very slow to act.]'
                    $plot_state.jon_vl_plan_info = InfoGet.SUCCESS
                    jump menu_jon