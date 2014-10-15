
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Jonathan Caise

label ch_jon:
    $ show_ch('jon', 'left')

    if plot_state.jon_vl_plan_info == InfoGet.FAIL:
        jon "Was I not clear? Don't talk to me, [alias.last], unless you find spending time in confinement appealing."
        $ hide_ch('jon', 'left')
        return

    if plot_state.jon_met:
        $ last_dialog = "Hello again, " + alias.title_last + ". What brings you here?"
        jon "[last_dialog]"

    else:
        jon "Give me a moment here..."
        jon "HEY! JANS! GET YOUR PEOPLE ON THE TARMAC ASAP."
        jon "Sorry. Can I help you [alias.address]?"

        p "I\'m just trying to get to know people here."

        jon "New to Concord? Welcome. I\'m Jonathan Caise, manager of logistics here at the port."

        p "[alias.full], diplomat over at the Human Embassy."

        jon "Greenhorn diplomat? Make sure you really take your time to get to know people."
        jon "I\'ve seen my fair share of people bail and out and leave because Concord is too much a culture shock for them. 
        But you look like you\'ve got a good head on your shoulders."

        p "I\'m determined to leave my footprint here."

        $last_dialog = "Good. I like your motivation. Feel free to ask me questions, but I may have to be quick... my work doesn\'t often give me breaks."

        $plot_state.jon_met = True

    label menu_jon:
        menu:
            jon '[last_dialog]'
            "Lie about your hobbies" if plot_state.stage == PlotStage.VL_INFO and plot_state.jon_hobby_info == InfoGet.SUCCESS:
                jump jon_hobbies_tree_start
            "Ask about Valak Lideri" if plot_state.stage == PlotStage.VL_INFO and plot_state.jon_vl_info == InfoGet.NO_ATTEMPT:
                jump jon_VL_tree_start
            "Ask Jon for advice":
                call jon_advice
            "Ask Jon his opinions on recent events":
                call jon_events
            "Ask Jon about his background":
                call jon_background
            "Show sympathy with Valak Lideri" if plot_state.stage == PlotStage.VL_PLANS and plot_state.kro_obsession_info and plot_state.jon_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump jon_VL_plan_tree_start
            "Accuse Jon of association with the VL" if plot_state.stage == PlotStage.VL_PLANS and plot_state.kro_obsession_info and plot_state.jon_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump jon_accuse
            "Done talking to Jon":
                $ hide_ch('jon', 'left')
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
            p "Could you tell me about your background?"

            jon "I'm not really an interesting person, greenhorn. I was born and raised here on Concord - I visited Earth for a few years when I was eighteen then came back."

            jon "I have a pretty good memory and eye for detail so I was sought-after for this kind of number work. It's pretty repetitive, but I'll take it as long as it pays me well."

            jon "I am a little obsessed with history and cultures - and especially through the lens of weaponry. In my spare time I collect vintage fire arms and restore them."
            
            p "That sounds quite interesting actually."

            jon "It's fascinating. If you find me outside of work I'm most likely researching a weapon, repairing it, or maintaining it."

            p "And you said you weren't an interesting person..."

            jon "Well... not everyone is enthralled by tales of fire arms and how they reflect a people's culture and history. So I tend to leave it out of conversation unless explicitly asked."
            
            $last_dialog = "If you have any other questions, feel free to ask."
            if plot_state.jon_hobby_info == InfoGet.NO_ATTEMPT:
                $plot_state.jon_hobby_info = InfoGet.SUCCESS
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

            $last_dialog = "In literally every instance of a great weapon's conception they bury the people involved in its creation and assume the idea themselves. It irritates me to no end."
            if plot_state.jon_vl_info == InfoGet.NO_ATTEMPT:
                menu:
                    jon "[last_dialog]"
                    "Inquire about dislike of kaldrean government":
                        jump jon_hobbies_tree_pursue
                    "Ask about Valak Lideri":
                        jump jon_hobbies_tree_VL
            else:
                jon "[last_dialog]"
                jump jon_hobbies_tree_pursue

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
                $ plot_state.jon_hobby_info = InfoGet.FAIL
                jump menu_jon

            label jon_hobbies_tree_VL:
                p "Do you think Valak Lideri are politically charged against the government?"

                jon "That could be said about any rebel group. But yes. Currently it makes sense for an organization like that to start gaining political traction."

                p "But they aren't terrorists."

                jon "Right. From what I've heard, and likely what you've heard as well, they are become a threat as a political influence rather than a violent group."

                jon "Based on what little I know I believe that have a good cause - they want to give the kaldrean progressive movement new life and new force."

                menu:
                    jon "Many kaldreans want to be free of their suppressive controllers - Valak Lideri are not afraid to do what is right."
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

                    jon "Well... I am, of course. Outside of my work I am very interested in history and culture so it pains me to see one so rich ruined like this."

                    jon "And... from what I've heard, Valak Lideri are trying to stop the kaldrean government from destroying their people. I can't help but find their perspective... agreeable"
                    $plot_state.jon_vl_info = InfoGet.FAIL
                    $last_dialog = "I'd prefer not to talk about Valak Lideri - they still make me uneasy. If you have any more questions please be quick, I have to get back to work promptly."
                    jump menu_jon


        label jon_VL_tree_start:
            p "What can you tell me about Valak Lideri?"

            jon "I don't really have much to say about them other than they make me nervous and distract me from my work. So I don't like to think about them."
            menu:
                jon "I wish I could tell you more... but I can't."
                "Comment on Jon's uneasiness":
                    jump jon_VL_tree_uneasy
                "Play along with Jon's uneasiness":
                    jump jon_VL_tree_go_along

            label jon_VL_tree_uneasy:
                p "Is there something wrong? You seem a little... uneasy."
                jon "I feel like you are trying to accuse me of something when you barely know me or anything about who I am. So yes, it makes me very uneasy."

                jon "And I already told you that I do not want to speak about Valak Lideri."

                jon "Threats like that are better handled by professional agents rather than operational and civil agents like you and I."

                p "I apologize. I didn't mean to upset you."
                $plot_state.jon_vl_info = InfoGet.FAIL
                $last_dialog = "Yeah well, steer clear of that topic and I'll be your friend. Otherwise, I'll get irritated. If you have anything else to ask, make it something simple."
                jump menu_jon


            label jon_VL_tree_go_along:
                p "Right, well I'll just have to dig around some more. "
                jon "Perhaps you might talk to Flight Commander Zalva. She's younger, but she's seen a lot. She's a little... cold, but oddly friendly."
                $last_dialog = "If you tell her I sent you, she'll be a little more responsive."
                $plot_state.jon_talk_kro = True
                jump menu_jon

        label jon_accuse:
            p "You know what, Jon, you haven't done a very good job covering up the fact that you are part of Valak Lideri."
            jon "That is a very serious accusation -  I don't take {i}any{/i} accusations lightly. So get out of my face before I remove you myself."
            $plot_state.jon_vl_plan_info = InfoGet.FAIL
            $ hide_ch('jon', 'left')
            return

        label jon_VL_plan_tree_start:
            p "I know it makes you uncomfortable to talk about Valak Lideri, but I want you to know what I agree with their perspective."
            menu:
                jon "Don't make an accusation that you have no basis for, [alias.last]. I don't want to have to charge you for treasonous activity."
                "Bluff that you are aware of Valak Lideri plans" if plot_state.alkay_vl_plan_info != InfoGet.SUCCESS:
                    jump jon_VL_plan_tree_bluff
                "Assure Jon that you are aware of Valak Lideri plans" if plot_state.alkay_vl_plan_info == InfoGet.SUCCESS:
                    jump jon_VL_plan_tree_aware
                "You want to see galactic change":
                    jump jon_VL_plan_tree_change

            label jon_VL_plan_tree_bluff:
                p "I'm aware of Valak Lideri's plans, Jon."
                jon "Hah! You're pulling my leg here. Of the two of us, {i}you{/i} are exhibiting exactly the kind of dangerous behavior that Valak Lideri would expect."

                jon "If you keep talking to me I'll have you removed from this area. Be glad that I'm only sending you off with a warning, [alias.last]."
                $plot_state.jon_vl_plan_info = InfoGet.FAIL
                $ hide_ch('jon', 'left')
                return

            label jon_VL_plan_tree_change:
                p "Listen to me, Jon, I will not stand here and allow the kaldrean government to continue breaking down their own people or the human government to sit idly and let it happen."
                menu:
                    jon "You're walking on thin ice, greenhorn, but I agree with you. So answer me this: how far you would go to see this change through?"
                    "Argue on the side of violence":
                        jump jon_VL_plan_tree_change_violence
                    "Not so much about how, but what it is that changes":
                        jump jon_VL_plan_tree_change_what
                    "Argue on the side of peace":
                        jump jon_VL_plan_tree_change_peace

                label jon_VL_plan_tree_change_violence:
                    p "If we want to accomplish anything, we have to enforce it. Violence may not be the best strategic answer, but long-term effects do not spark revolutions."
                    
                    p "A bullet can both literally and figuratively create the spark that ignites a change."

                    jon "I can see why you would think that. But you need to understand that the long-term solutions have lasted longer in retrospect."

                    jon "Still, I agree that violence compliments peace in such a delicate balance that it's often broken. Because once you've started the fire, you have to put it out."
                    
                    jon "A well-placed bullet can mean the difference between chaotic disaster and effective victory - but at the same time, a well-timed armistice can decide the fate of a people."
                    
                    $last_dialog = "It's good to know that we have another supporter of our cause. I hope that you can provide both the impetus and the resolution that the rebellion needs."
                    $plot_state.jon_vl_plan_info = InfoGet.SUCCESS
                    jump menu_jon

                label jon_VL_plan_tree_change_what:
                    p "We have to focus on \"what\" we are trying to change more than \"how\". It's the \"what\" which gives us direction."

                    p "If we lose sight of what we are fighting to change, then it simply turns into a brawl. Once the goal has been achieved, there is no longer a reason to fight for it."

                    jon "Of course... because holding grudges against your enemies after a war is concluded has only ever proven counterproductive."

                    jon "I agree with you, [alias.first], you make a strong point."

                    p "I can't stress it enough. There is simply no need to fight another lengthy war when one isn't necessary or even logical."

                    $ last_dialog = "Your words are inspiring, "+alias.first+". Let me know if you need anything else."
                    $plot_state.jon_vl_plan_info = InfoGet.SUCCESS
                    jump menu_jon

                label jon_VL_plan_tree_change_peace:
                    p "We have to remember, though, that while violence may be able to trip off a revolution, it will not end it with a stable resolution."

                    p "Violence does nothing but alienate people, who forget what they are fighting for and simply that they must kill the enemy."

                    p "It may be powerful, but chaos ultimately creates more chaos. It's simply how the universe works as a closed system."

                    jon "But you have to remember, that while peace may be powerful and orderly, it does not come quickly. You may offend just as many people if you don't fight."
                    
                    jon "Kaldreans especially -  they'll lose respect for a force that attempts to avoid battle."

                    p "Unfortunately. But it's a small price to pay when you are going to drastically alter the course of a people's future."

                    jon "I suppose. But you'll have to really do some sweet-talking when you try to convince skeptical kaldreans of this."

                    $last_dialog = "Then again, it's for the benefit of the future generations. They would most likely agree. If you have anything else to ask, please do."
                    $plot_state.jon_vl_plan_info = InfoGet.SUCCESS
                    jump menu_jon

            label jon_VL_plan_tree_aware:
                p "I'm sure if you were to speak to Alkay, he would give his word that I am trustworthy."

                p "He and I have already had this discussion so I what you are going to do."

                jon "You're bluffing."

                p "Tomorrow morning is when everything is going to change - through the lens of a linear rifle scope."

                jon "And what are you going to do about it?"

                p "I assure you that I'm only trying to help."

                jon "I still don't believe you, [alias.last], but I don't know how else you would have obtained that information. I'll humor you."
                jump jon_VL_plan_tree_change

