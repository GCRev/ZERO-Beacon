
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lorisk Nideria Kol

label ck_lorisk:
    $ show_ch('lorisk', 'left')

    if plot_state.lorisk_vl_plan_info == InfoGet.SUCCESS:
        $last_dialog = '[[Thank you so much, ' + alias.first + '. I really needed to talk to someone about this. Is there anything you still want to ask?]'
        jump menu_lorisk
    if plot_state.lorisk_vl_plan_info == InfoGet.FAIL:
        lorisk 'I do not wish to speak with you again. Take your bigotry elsewhere.'
        $ hide_ch('lorisk', 'left')
        return

    if plot_state.lorisk_met:
        $last_dialog = 'Hello again, ' + alias.first + '. How can I help you?'
    else:
        lorisk "Hello, hola, ciao, bonjour, nǐ hǎo, konnichiwa, zdravstvuyte. Welcome to Concord!"
        lorisk "I\'m Lorisk Nidaria, the senior linguist and interpreter here in Concord. But please, just call me Lorisk."
        p "Nice to meet you, Lorisk. I\'m [alias.full], a recently-deployed diplomat."
        $plot_state.lorisk_met = True
        $last_dialog = "It\'s wonderful to meet you, " + alias.first + "! You probably have questions, so feel free to ask away. I\'m always open to talk."
    jump menu_lorisk

    label menu_lorisk:
        menu:
            lorisk '[last_dialog]'
            "Ask Lorisk for advice":
                call lorisk_advice
            "Ask Lorisk about her opinion on recent events":
                call lorisk_events
            'Ask Lorisk about her background' if plot_state.stage == PlotStage.VL_INFO and not plot_state.lorisk_flatter_offend:
                jump lorisk_VL_tree_start
            'Ask Lorisk about Valak Lideri' if plot_state.stage == PlotStage.VL_INFO and plot_state.lorisk_vl_info != InfoGet.FAIL:
                jump lorisk_personal_reasons
            'Question Lorisk about her parents' if plot_state.stage == PlotStage.VL_PLANS and plot_state.lauren_lorisk_info:
                jump lorisk_VL_plans_tree_start
            'Done talking to Lorisk':
                $ hide_ch('lorisk', 'left')
                return
        jump menu_lorisk

        label lorisk_advice:
            p 'Do you have any —'

            lorisk 'Advice? Always!'

            p 'How did you —'
           
            lorisk "I talk to and interpret people for a living. You\'d find that after doing something like that for so long,
            you develop an intuition to predict what someone is going to say."
            
            lorisk "Anyway, I\'ll tell you that acceptance is a big deal here." 

            lorisk "The more you find yourself seeing through someone\'s skin and into their being, the more your definition of \"person\" will change." 
           
            lorisk "While you may recognize someone as kaldrean in passing, when you get to know 
            them you begin to identify them based on their presence in the room."

            lorisk "You can understand a great deal about people based on their cadence of speech and energy they project."

            p "I can see what you mean. Thanks for your advice, Lorisk."

            $last_dialog = "Any time! If you have any more questions don't hesitate to ask."
            return

        label lorisk_events:
            p "What do you make of the political tension building here on Concord?"

            lorisk "All I know is that we're working as hard as we can to keep tensions from building up any more. I'm afraid it's become increasingly difficult."

            p "Why is that?"

            lorisk "Kaldreans and humans are just... more bitter recently and I'm not sure why. I have plenty of human friends and they haven't changed their attitudes."

            lorisk "So I am confused. Perhaps it is because the ambassadors are relatively new and young - it seems kaldreans and humans share a distrust for youth without much life experience."

            p "I can see why they'd think that. I had to really struggle against that viewpoint to make it to where I am now."

            lorisk "We are all doing our best to break down that disposition. I'm glad to see another young diplomat who projects the same charisma and authority as an Elder."

            $last_dialog = "Is there anything else I can help you with "+alias.first+"?"
            return

        label lorisk_personal_reasons:
            p 'Can you tell me anything about Valak Lideri?'

            lorisk "Sorry I'd rather not."

            p "Personal reasons?"

            lorisk "...yes. I apologize."

            p "Please, don't apologize to me. I was prying."

            $ last_dialog = "You could not have known about that. Anyway, is there anything else you want to ask?"
            $ plot_state.lorisk_vl_info = InfoGet.FAIL
            jump menu_lorisk

        label lorisk_VL_tree_start:
            p 'You seem like you have quite a bit of interesting knowledge and experience. 
            Can you tell me more about yourself and your background?'
            menu:
                lorisk "Well, there isn't much to tell. Both my parents were linguists, and they made quite sure that I was prepared to communicate with anyone I met."
                "Ask about linguistics":
                    jump lorisk_VL_tree_languages
                "Praise her dedication" if not plot_state.lorisk_flatter:
                    jump lorisk_VL_tree_flatter 
                "Stop pursing the topic":
                    p "Interesting."
                    $ last_dialog = "Anything else you'd like to ask?"
                    jump menu_lorisk

            label lorisk_VL_tree_languages:
                p "So as the Senior Linguist here I assume you have a penchant for linguistics?"
                $ last_dialog = "Yes! Linguistics are fascinating to me. The history and evolution of a language can reveal so much to us. In our changing world, it is useful to know languages and their histories."
                if plot_state.alkay_vl_info == InfoGet.SUCCESS:
                    menu:
                        lorisk '[last_dialog]'
                        'Ask about traditional dialects':
                            jump lorisk_VL_tree_dialects
                        'Ask which languages she speaks':
                            jump lorisk_VL_tree_list_languages
                else:
                    lorisk '[last_dialog]'
                    jump lorisk_VL_tree_list_languages  

                label lorisk_VL_tree_dialects:
                    p "Can you tell me about the traditional dialects? Alkay mentioned them so he got me wondering about them."
                    menu:
                        lorisk "I actually know how to read and write in four of the many traditional dialects. Of those four I can speak and understand two: Kalaras and Takress."
                        "ask what \"Valak Lideri\" means":
                            jump lorisk_personal_reasons
                        "ask about dialect history":
                            jump lorisk_VL_tree_dialect_history

                    label lorisk_VL_tree_dialect_history:
                        p "Could you talk about the history of those two languages?"

                        lorisk "Actually the reason I can speak and understand Kalaras and Takress is because they are still spoken, just barely anymore."

                        lorisk "They are the more recent of the traditional languages that were prominent around the settlement of Sovereign Paradise."

                        lorisk "Although \"Sovereign Paradise\" is a modern adaptation of the original phrase, which would have meant \"Beacon\" back then."

                        lorisk "Kalaras and Takress were quite similar and eventually they were unified and enforced in education. This was the first iteration of Kaldrean Common."

                        lorisk "Different subcultures still spoke in their native dialects and still do today. Kaldrean Common has evolved quite a bit as a result of all the cultural input."

                        p "Thank you for the information, Lorisk, this is really quite interesting."

                        $last_dialog = "Not at all. I'm happy to spread the knowledge around. Please speak up if you have anything more you would like to ask."
                        $plot_state.lorisk_vl_info = InfoGet.SUCCESS
                        jump menu_lorisk

                label lorisk_VL_tree_list_languages:
                    p "So how many languages can you speak?"

                    lorisk "I can speak thirty languages. Nineteen kaldrean and eleven human."

                    p "Thirty languages? Can you name each one?"
                    menu:
                        lorisk 'Do you really want me to list off all the languages I speak? Because I can.'
                        'Yes':
                            jump lorisk_VL_tree_list_all_lauguages
                        'No, thanks':
                            jump lorisk_VL_tree_list_languages_cancel
                            
                label lorisk_VL_tree_list_all_lauguages:
                    p "Actually yes, I would."
                    lorisk "Let's see..."
                    lorisk "English,"
                    lorisk "Spanish,"
                    lorisk "French,"
                    lorisk "Italian,"
                    lorisk "Mandarin,"
                    lorisk "Chichewa,"
                    lorisk "Latin,"
                    lorisk "Japanese,"
                    lorisk "Russian,"
                    lorisk "German,"
                    lorisk "Hindi,"
                    lorisk "Kaldrean Common,"
                    lorisk "Ekitri,"
                    lorisk "Koroa,"
                    lorisk "Katrs,"
                    lorisk "Akliko,"
                    lorisk "Qorosk,"
                    lorisk "Niesk,"
                    lorisk "Laerek,"
                    lorisk "Ruas,"
                    lorisk "Tolaer,"
                    lorisk "Alkor,"
                    lorisk "Senteares,"
                    lorisk "Seleksis,"
                    lorisk "Qalokalra,"
                    lorisk "Roaq,"
                    lorisk "Tarakres,"
                    lorisk "Viridi,"
                    lorisk "Irradae,"
                    lorisk "Valakri,"
                    lorisk "and... Elvish. Just for fun."
                    p "Wow, that's quite an impressive repertoire! Elvish really?"
                    lorisk "No, not really. Just joking."
                    $ last_dialog = "Anything else I can help you with... provided it doesn't require me to list off an enormous quantity of languages?"
                    $ plot_state.lorisk_vl_info = InfoGet.FAIL
                    jump menu_lorisk

                label lorisk_VL_tree_list_languages_cancel:
                    p "No I was only joking."

                    lorisk "Good... I'm sure I would have bored you to tears with a long list."

                    $ last_dialog = 'Is there anything else I can help you with?'
                    $ plot_state.lorisk_vl_info = InfoGet.FAIL
                    jump menu_lorisk

            label lorisk_VL_tree_flatter:
                p "You come across as very intelligent. I can see how it would be easy for you to pick up so many languages."

                lorisk "Why thank you, [alias.first]. You're quite the charmer, aren't you?"

                lorisk "Thank you for the compliment. I don't think it's often that anyone realizes how much work it is to maintain command over thirty languages."
                $ plot_state.lorisk_flatter = True
                menu:
                    lorisk "I detect another statement - I'll warn you though, compliments and flattery are two very different concepts. I don't appreciate flattery."
                    "Discontinue conversation":
                        jump lorisk_VL_tree_flatter_more
                    "Ask about her passion for languages":
                        jump lorisk_VL_tree_languages

                label lorisk_VL_tree_flatter_more:
                    p "I did mean what I said, Lorisk. I know a few linguists back on Earth, none of whom possess the same repertoire that you do."
                    
                    lorisk "Alright. Let me give you some advice, [alias.first]: Be extremely cautious about compliments and flattery around kaldreans."

                    lorisk "I've been tempered by my upbringing on Concord, but other kaldreans might be very easily offended by what you might consider an inane compliment."

                    p "I'll bear that in mind. Thank you Lorisk."

                    $last_dialog = "No problems "+alias.first+". If there is anything else you need please ask."

                    #$ plot_state.lorisk_flatter_offend = True
                    jump menu_lorisk

        label lorisk_VL_plans_tree_start:
            p "Lorisk I know about your parents. I know that they are mixed-race."
            menu:
                lorisk "Oh. You know about that? What do you care? Are you going to scorn me and my family for doing what they feel is right?"
                "show sympathy":
                    jump lorisk_VL_plans_tree_sympathy
                "show skepticism":
                    jump lorisk_VL_plans_tree_disgust

            label lorisk_VL_plans_tree_sympathy:
                p "I just wanted to say that I think you and you're family are very courageous to be strong against the controversy you likely received."

                p "You and others like you deserve better than that."

                lorisk "I-"

                lorisk "You have no idea how hard it's been for us. For all of us. I just... can't stand to see anyone else go through what we have."

                p "I'm doing my best to help."

                menu:
                    lorisk "Thank you. I cannot express enough just how much this means to me. I am desperate for this revolution to occur - it is the only way we have a chance to make it stop."
                    "Assure Lorisk that she can trust you":
                        jump lorisk_VL_plans_tree_sympathy_confidentiality
                    "Warn Lorisk about the truth of revolution":
                        jump lorisk_VL_plans_tree_disgust

                label lorisk_VL_plans_tree_sympathy_confidentiality:
                    p "You can trust me Lorisk. I want to help this rebellion to make the change it promises."

                    lorisk "I am willing to go to any length to make sure that we have a chance. Any measure..."

                    lorisk "Any means will justify the ends provided that those like my family can be rid of the oppression and the slander and the hatred."

                    lorisk "Valak Lideri is our Beacon. When we restore it... not only will we spawn another golden age for kaldreans, but break down the barriers between our races."

                    menu:
                        lorisk "It will be a new age for all of us."
                        "Peace is slow but more stable":
                            jump lorisk_VL_plans_tree_sympathy_confidentiality_peace
                        "It is important to punish only those responsible":
                            jump lorisk_VL_plans_tree_sympathy_confidentiality_reason
                        "Violence will create the necessary spark":
                            jump lorisk_VL_plans_tree_sympathy_confidentiality_violence

                    label lorisk_VL_plans_tree_sympathy_confidentiality_peace:
                        p "Just remember that peaceful uprising will ultimately be the most effective. Minimize the grudges and the vengeance."

                        lorisk "We cannot wait any longer, [alias.first]. We have already struggled for so long to give the progressive movement the ability to take down the corruption."

                        lorisk "It never works. While I agree that peace minimizes the collateral damage, I simply do not think that we have a choice but to use force."
                        
                        p "You may be correct. But if you must use the barrel of a rifle to argue your point, make sure you are aiming at the right people."
                        $plot_state.lorisk_vl_plan_info = InfoGet.SUCCESS
                        $last_dialog = "Thank you for talking to me about this. Let me know if you need anything else."
                        jump menu_lorisk

                    label lorisk_VL_plans_tree_sympathy_confidentiality_violence:
                        p "Make your point with the barrel of a linear rifle. From what I understand the progressive movement is extremely volatile - it would take little to set them off."
                        
                        lorisk "That's what we are planning - I just with that there was a better way. I do not want my fellow kaldreans to perish for the corrupted controllers."

                        lorisk "Their lives are worthless. They do not deserve to have soldiers fight and die for them."

                        p "You know that Vatrisk is doing his best to help you right?"

                        lorisk "I... I know. But this is out of my hands now. If we turn back now we may never accomplish what we have set out to change."

                        p "Then be very careful. I might not be able to help you once this gets going."
                        $plot_state.lorisk_vl_plan_info = InfoGet.SUCCESS
                        $last_dialog = "I know. I'm sorry. Is there anything else you want to ask?"
                        jump menu_lorisk


                    label lorisk_VL_plans_tree_sympathy_confidentiality_reason:
                        p "When you bring the movement to Qolisk, make sure that the ones under the rifle scope are truly the ones responsible for the corruption."

                        lorisk "I cannot agree with you more, [alias.first]. I cannot imagine how many poor souls are bent to do the bidding of our controllers. They should not trade their lives for leaders'."

                        lorisk "I'm afraid, however, that this will get out of hand."

                        p "The it is up to you to keep it under control. You can - you know strength better that most and I definitely know that you can communicate better than most."
                        $plot_state.lorisk_vl_plan_info = InfoGet.SUCCESS
                        $last_dialog = "Thank you so much "+alias.first+". Let me know if you need anything else."
                        jump menu_lorisk

            label lorisk_VL_plans_tree_disgust:
                p "How exactly does that work? How does a kaldrean and a human fall into a relationship?"

                lorisk "I cannot believe you really just asked me that? You did not really think that question through before you blurted it did you?"

                p "No I'm actually -"

                lorisk "Stop. Stop before you say something even worse than that. You have no idea how much they have had to stand against to be together and to raise me."
                
                lorisk "They are happier together than most kaldrean or human couples. So not only did they have to face the fire, but I did as well."

                lorisk "I was shunned throughout my schooling and denied military service and the respect that kaldreans gain by going through it."

                lorisk "So do not try to tell me that you understand, or that you want to. No words can express what we have gone through."

                lorisk "I thought I could trust you, [alias.title_last], but I guess I couldn't recognize your deceitful tone. I do not want to talk to you anymore."
                $ plot_state.lorisk_vl_plan_info = InfoGet.FAIL
                $ hide_ch('lorisk', 'left')
                return
