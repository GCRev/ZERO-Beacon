
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Noq Kriesk Lask

label ck_noq:
    $ show_ch('noq', 'left')

    if plot_state.noq_vl_plan_info == InfoGet.FAIL:
        noq '[[I told you not to bother me.]'
        $ hide_ch('noq', 'left')
        return

    if plot_state.noq_met:
        $ last_dialog = 'Kevey, ' + alias.title_last + '. Please make your questions quick.'
        noq '[last_dialog]'
    else:
        noq "Yes?"
        p "I\'m [alias.full]. Nice to meet you."
        noq "Very good. Now please be snappy. I am very busy at the moment."
        p "Alright. I simply wanted to—"
        $ last_dialog = "My apologies for my irritability. I have to meet deadlines; I wish I had more time to talk. If you have any questions just make them quick." 
        noq '[last_dialog]'
        $plot_state.noq_met = True

    label menu_noq:
        menu:
            noq '[last_dialog]'
            'Ask Noq about his designs' if plot_state.stage == PlotStage.VL_INFO:
                call noq_designs
            'Ask about Valak Lideri' if plot_state.stage == PlotStage.VL_INFO or plot_state.stage == PlotStage.VL_PLANS:
                jump noq_VL_tree_start
            'Ask Noq for advice':
                call noq_advice
            'Ask Noq about his opinions on recent events':
                call noq_events
            ##'Ask Noq about his background':
            ##    call noq_background
            'Ask Noq about his interests'  if plot_state.stage == PlotStage.VL_PLANS and plot_state.noq_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump noq_interests_tree_start
            'Done talking to Noq':
                $ hide_ch('noq', 'left')
                return
        jump menu_noq

        label noq_advice:
            p "Would you mind sharing some advice?"
            noq "Normally I wouldn't, but right now I am very busy. I have a deadline that I need to meet and right now I'm in the zone."
            p "Perhaps later then."
            noq "Perhaps"
            p "Alright"
            $last_dialog = 'Anything else? Or shall I be on my way?'
            return

        label noq_events:
            p "What do you think about the whole \"tension between kaldreans and humans\" supposedly here on Concord?"
            
            noq "Ha. I was not aware of this. But that is probably because I do not pay mind to such matters. Clearly it is so obscure that it is not a real problem."

            p "Alright then. I think that's clear enough. I'll let you get back to work."

            $last_dialog = "I really am quite busy. I would appreciate it if you returned later."

            return

        label noq_background:
            p '[[you ask Noq on his background]'
            noq '[[offers little information. Does not sound interested in talking about it.]'
            $last_dialog = '[I really am quite busy. I would appreciate it if you returned later.]'
            return

        label noq_designs:
            p '[[you ask Noq about his designs]'
            noq '[[Lightens up and talks for a while about his latest structure.]'
            $last_dialog = '[It\'s refreshing when someone takes an interest in my work. I could talk forever about it.]'
            return

        label noq_VL_tree_start:
            p "Would you happen to know anything about Valak Lideri?"

            noq "You could ask anyone and they would be likely to give you a better answer than I."

            noq "Everyone knows about them just no one knows who they are or what they want. Kind of impractical for what is deemed a \"rebel group\" if you ask me."

            noq "What was their most recent thing? A threat? Are they going to kill someone to make their point? How elementary."

            noq "If they want to accomplish anything, they will have to re-think their strategy."

            noq "All I see right now are tactical decisions - they might work in the short term, but they will fail long term."

            noq "Our government has a strong outer shell but a weak internal structure - they should really focus on that instead."

            p "You seem like you know quite a lot this."

            noq "I dislike our government. But I'll deal with it as long as they no longer force obligations down my throat and then mock me when I am incapable."

            p "I'm sorry I asked."

            noq "Just don't ask. Let's avoid talking about my not-so-spectacular military past."

            $last_dialog = "If you have anything else to say, make it fast. I have to finish up these designs."
            if plot_state.stage == PlotStage.VL_PLANS and plot_state.noq_vl_plan_info == InfoGet.NO_ATTEMPT:
                menu:
                    noq '[last_dialog]'
                    "Ask Noq again if he knows something about Valak Lideri":
                        $ plot_state.noq_vl_plan_info = InfoGet.FAIL
                        jump noq_VL_tree_ask_again
                    "Drop the topic":
                        jump menu_noq

            else:
                jump menu_noq

            label noq_VL_tree_ask_again:
                p "Are you sure, Noq? I feel like you might have something more to say about Valak Lideri."
                menu:
                    noq "I do not understand why you keep questioning me about this. I already told you that I do not know anything about Valak Lideri."
                    "Assert that Noq must know something":
                        jump noq_VL_tree_assert
                    "Drop the topic":
                        jump menu_noq

                label noq_VL_tree_assert:
                    p "Surely you must know something. I can tell that you do."
                    noq "You are irritating me with your ridiculous questioning. Remove yourself or I will have security remove you for you."
                    $ hide_ch('noq', 'left')
                    return

        label noq_interests_tree_start:
            p "What interests you Noq? I'm guessing it's not a question you are asked often."

            noq "You are correct. I have a passion for mathematics and engineering - I can see these shapes and images that translate into numbers and measurements."

            noq "When I put them into software everything simply works. I feel liberated when I am given architectural design work."

            p "How did you become interested? I assume you had a good education if you have such an expansive knowledge of this material."

            noq "I did. My family and my clan is wealthy. When my parents saw that I had a bent for engineering they put into the best educational system that money can buy."

            noq "Citadel's Academy is the most difficult school to get into, but I was practically invited."

            p "So you're a savant basically."

            noq "I suppose. That may also explain why I'm so socially and physically inept."

            p "Based on that I can infer that you had some troubles afterwards?"

            noq "Military training... was absolutely terrible to me. I was unable to perform most of the tasks they asked of me, and I was ridiculed as a result."

            noq "I managed to regain some respect by becoming the youngest decorated master marksman in the last two centuries."
            menu:
                noq "The math skills really do come in handy when you can calculate projectile trajectories in your head and hit the center of the target every time."
                "Ask about opinions of the kaldrean military":
                    jump noq_interests_tree_opinions
                "Show sympathy":
                    jump noq_interests_tree_sympathize

            label noq_interests_tree_opinions:
                p "So you dislike the military? I suppose that's obvious... Can you be more specific? What is it about the military that turned you away?"

                noq "They have a certain expectation for every rookie soldier, even though it may be completely obvious that expectations are unreasonable."

                noq "You get burned even though it is not your fault you were born with a physical defect."

                noq "They are not permitted to kill you but they will try. They will have you within inches of death simply because they are trying to teach you \"strength.\""

                noq "Their system would work much better if it sought to put those with the right skills in the right training. But they do not. So they waste everyone's time."

                menu:
                    noq "Alkay seems to think this accurate. I can definitely see why there are so many kaldreans out there who dislike the military and service to it."
                    "Ask about Alkay":
                        jump noq_interests_tree_opnions_alkay
                    "Agree with his opinions":
                        jump noq_interests_tree_opinions_agree

                label noq_interests_tree_opnions_alkay:
                    p "You mentioned Alkay?"

                    noq "Right well, I think I got carried away."
                    $ plot_state.noq_vl_plan_info = InfoGet.SUCCESS
                    $ last_dialog = "What else?"
                    jump menu_noq

                label noq_interests_tree_opinions_agree:
                    p "I agree. Our military, while not compulsory like the kaldrean's, does uphold the same operational standards for everyone."

                    p "I feel like the way that they run things around there is inefficient and unbalanced as well."

                    noq "You might talk to Officer Caise and Elder Volk. They know quite a bit about this as well."

                    p "Thank you"
                    $ plot_state.noq_vl_plan_info = InfoGet.SUCCESS
                    $ last_dialog = "What else?"
                    jump menu_noq

            label noq_interests_tree_sympathize:
                p "I'm sorry that you had to go through that. I don't think any military should treat their own people that way."

                noq "Do not patronize me, you do not truly understand how bad it was for some of us."

                p "I'm sorry I said anything then."

                noq "Good."
                $ plot_state.noq_vl_plan_info = InfoGet.FAIL
                $ last_dialog = "If you want ask anything else, be snappy about it."
                jump menu_noq

