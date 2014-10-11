
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lorisk Nideria Kol

label ck_lorisk:
    show lorisk at char_pos

    if plot_state.lorisk_vl_plan_info == InfoGet.SUCCESS:
        $last_dialog = '[[Thank you so much, ' + alias.first + '. I really needed to talk to someone about this. Is there anything you still want to ask?]'
        jump menu_lorisk
    if plot_state.lorisk_vl_plan_info == InfoGet.FAIL:
        lorisk 'I do not wish to speak with you again. Take your bigotry elsewhere.'
        hide lorisk
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
            "Ask for advice":
                call lorisk_advice
            "Ask about her opinion on recent events":
                call lorisk_events
            'Ask about her background' if plot_state.stage == PlotStage.VL_INFO and not plot_state.lorisk_flatter_offend:
                jump lorisk_VL_tree_start
            'Ask about Valak Lideri' if plot_state.stage == PlotStage.VL_INFO:
                jump lorisk_personal_reasons
            'Question her about her parents' if plot_state.stage == PlotStage.VL_PLANS and plot_state.lauren_lorisk_info:
                jump lorisk_VL_plans_tree_start
            'Done talking':
                hide lorisk
                return
        jump menu_lorisk

        label lorisk_advice:
            p 'Do you have any —'
            lorisk 'Advice? Always!'
            p 'How did you —'
           
            lorisk "I talk to and interpret people for a living. You\'d find that after doing something like that for so long,
            you develop an intuition to predict what someone is going to say."
            lorisk "Anyway, I\'ll tell you that acceptance is a big deal here. The more you find yourself seeing through someone\'s skin and into their
            being, the more your definition of \"person\" will change." 
            lorisk "While you may recognize someone as kaldrean in passing, when you get to know 
            them you begin to identify them based on their presence in the room, their cadence of speech, the energy they project."

            p "I can see what you mean. Thanks for your advice, Lorisk."
            $last_dialog = 'Any time!'
            return

        label lorisk_events:
            p '[[ask her opinion on recent events]'
            lorisk '[[gives you her opinion on recent events]'
            $last_dialog = '[is there anything else I can help you with?]'
            return

        label lorisk_personal_reasons:
            p 'Can you tell me anything about Valak Lideri?'
            lorisk 'Sorry, but for personal reasons, I\'d rather not.'
            $ last_dialog = 'Is there any thing else I can help you with?'
            $ plot_state.lorisk_vl_info = InfoGet.FAIL
            jump menu_lorisk

        label lorisk_VL_tree_start:
            p 'You seem like you have quite a bit of interesting knowledge and experience. 
            Can you tell me more about yourself and your background?'
            menu:
                lorisk "Well, there isn't much to tell. Both my parents were linguists, and they passed their loves for their
                profession on to me."
                "Ask about her love for linguistics":
                    jump lorisk_VL_tree_languages
                "Flatter her with praise for her passion and intelligence" if not plot_state.lorisk_flatter:
                    jump lorisk_VL_tree_flatter 
                "Stop pursing the topic":
                    p "Interesting."
                    $ last_dialog = "Anything else you'd like to ask?"
                    jump menu_lorisk

            label lorisk_VL_tree_languages:
                p 'So you have love for linguistics?'
                $ last_dialog = 'Yes!! I speak a multitude of languages.'
                if plot_state.alkay_vl_info == InfoGet.SUCCESS:
                    menu:
                        lorisk '[last_dialog]'
                        'Ask about traditional dialects':
                            jump lorisk_VL_tree_dialects
                        'Ask which ones':
                            jump lorisk_VL_tree_list_languages
                else:
                    lorisk '[last_dialog]'
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
                    p 'Which ones?'
                    lorisk '(laughs)'
                    menu:
                        lorisk 'Do you really want me to list off all the languages I speak?'
                        'Yes':
                            p 'Actually, I do!'
                            lorisk "Let's see..."
                            lorisk "English (obviously), "
                            lorisk "Spanish,"
                            lorisk "Mandarin,"
                            lorisk "Chichewa,"
                            lorisk "Latin,"
                            lorisk "French,"
                            lorisk "Japanese,"
                            lorisk "Nepali,"
                            lorisk "Hindi,"
                            lorisk "Italian,"
                            lorisk "Kaldrean Common,"
                            lorisk "Ekitri,"
                            lorisk "Koroa,"
                            lorisk "Katrs,"
                            lorisk "Akliko,"
                            lorisk "Qorosk,"
                            lorisk "(takes a breath)"
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
                            lorisk "and... Elvish. Just for fun."
                            "(you both laugh)"
                            p "Wow, that's quite an impressive repertoire!"
                            $ last_dialog = "Why thank you. Anything else I can help you with?"
                        'No, thanks':
                            p 'On second thought, I\'ll pass.'
                            '(you both laugh together)'
                    $ last_dialog = 'Is there anything else I can help you with?'
                    $ plot_state.lorisk_vl_info = InfoGet.FAIL
                    jump menu_lorisk

            label lorisk_VL_tree_flatter:
                p "I can tell. There aren't many people I've met as smart and passionate as you."
                $ plot_state.lorisk_flatter = True
                lorisk "(laughs)"
                menu:
                    lorisk "Why thank you, [alias.first]. You\'re quite the charmer, aren\'t you?"
                    'Mention her radiance and beauty':
                        p "Well, it's hard not to be a charmer around someone of your radiance and beauty."
                        lorisk "(sighs)"
                        lorisk "Alright, it was cute at first, but now I can tell you're just using me."
                        lorisk "Come back when you've calmed down a bit."
                        $ plot_state.lorisk_flatter_offend = True
                        hide lorisk
                        return
                    "Ask about her passion for languages":
                        jump lorisk_VL_tree_languages

        label lorisk_VL_plans_tree_start:
            p '[[you tell Lorisk that you know about her mixed-race parents]'
            menu:
                lorisk '[[Oh. You know about that? What do you care?]'
                '[[show sympathy]':
                    jump lorisk_VL_plans_tree_sympathy
                '[[show disgust]':
                    jump lorisk_VL_plans_tree_disgust

            label lorisk_VL_plans_tree_sympathy:
                p '[[respond with sympathy]'
                menu:
                    lorisk '[[breaks down and reveals just how badly she wants this revolution to go through.]'
                    '[[offer trust and confidentiality]':
                        jump lorisk_VL_plans_tree_sympathy_confidentiality
                    '[[the rebels are going to ruin your chances with their ways]':
                        jump lorisk_VL_plans_tree_disgust

                label lorisk_VL_plans_tree_sympathy_confidentiality:
                    p '[[offer trust and confidentiality]'
                    menu:
                        lorisk '[[reveals that she  is a part of the VL and that she is willing to go to any length to make a difference.]'
                        '[[peace is slow but more stable]':
                            jump lorisk_VL_plans_tree_sympathy_confidentiality_peace
                        '[[important to only punish those responsible]':
                            jump lorisk_VL_plans_tree_sympathy_confidentiality_reason
                        '[[quick violence will solve problem quickly]':
                            jump lorisk_VL_plans_tree_sympathy_confidentiality_violence

                    label lorisk_VL_plans_tree_sympathy_confidentiality_peace:
                        p '[[peace is slow but more stable]'
                        lorisk '[[agrees, but does not like that her people would have to wait any longer]'
                        $plot_state.lorisk_vl_plan_info = InfoGet.SUCCESS
                        $last_dialog = '[Thank you for talking to me about this. Let me know if you need anything else.]'
                        jump menu_lorisk

                    label lorisk_VL_plans_tree_sympathy_confidentiality_violence:
                        p '[[quick violence will solve problem quickly]'
                        lorisk '[[agrees, but hopes that if it does come to violence, that it is minimal.]'
                        $plot_state.lorisk_vl_plan_info = InfoGet.SUCCESS
                        $last_dialog = '[Thank you for talking to me about this. Let me know if you need anything else.]'
                        jump menu_lorisk


                    label lorisk_VL_plans_tree_sympathy_confidentiality_reason:
                        p '[[important to only punish those responsible]'
                        lorisk '[[agrees. Those who were caught up, including those under corrupt control, may not have wholeheartedly agreed.]'
                        $plot_state.lorisk_vl_plan_info = InfoGet.SUCCESS
                        $last_dialog = '[Thank you for talking to me about this. Let me know if you need anything else.]'
                        jump menu_lorisk

            label lorisk_VL_plans_tree_disgust:
                p '[[don\'t you find that wrong?]'
                lorisk '[[blows up in your face about hardship and how you have no idea. Ceases conversation]'
                hide lorisk 
                return
