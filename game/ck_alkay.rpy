
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Alkay Volk Kladir

label ck_alkay:
    show alkay at char_pos
    if plot_state.alkay_met:
        $ last_dialog = 'Hello again, ' + alias.first + ', what can I get you?'
        alkay '[last_dialog]'

    else:
        alkay "Welcome to my humble eatery. Ah! A new face, you must be a new arrival, are you not?"

        p "I am."

        alkay "Of course, of course. I am Alkay Volk, although some affectionately refer to me as \"Uncle Al\", or \"Uncle Klay.\""
        alkay "You humans have this interesting way of informally incorporating everyone into your families, a custom of which I have become quite fond."
        alkay "I apologize for running a tangent, I believe I lack your name."

        p "[alias.full]"

        alkay "[alias.first]. It is my pleasure. Please, have a seat. The first meal is always on the house. We\'ll talk over some good food. Feel free to ask me anything."
        
        $last_dialog = "Just be wary, I do like to talk and ramble. Stop me if I go off-subject."
        alkay '[last_dialog]'

        $ plot_state.alkay_met = True

    label menu_alkay:
        menu:
            alkay '[last_dialog]'
            '[[ask for advice]':
                call alkay_advice
            '[[ask about opinions on events]':
                call alkay_events
            '[[Ask about VL]' if plot_state.stage == PlotStage.VL_INFO:
                jump alkay_VL_tree_start
            '[[Ask about background]' if plot_state.stage == PlotStage.VL_INFO:
                jump alkay_Bg_tree_start
            '[[Adam sent me]' if plot_state.adam_talk_alkay == True and plot_state.stage == PlotStage.VL_INFO:
                jump alkay_adam_tree_start
            '[[show sympathy with VL]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.adam_alkay_info == InfoGet.SUCCESS and plot_state.alkay_vl_plan_info == InfoGet.NO_ATTEMPT:
                call alkay_VL_plan_sympathy
            '[[accuse Alkay of being involved with VL]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.adam_alkay_info == InfoGet.SUCCESS and plot_state.alkay_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump alkay_VL_accuse_tree_start
            '[[lie about what you know]' if plot_state.stage == PlotStage.VL_PLANS and plot_state.adam_alkay_info == InfoGet.SUCCESS and plot_state.alkay_vl_plan_info == InfoGet.NO_ATTEMPT:
                jump alkay_VL_plan_lie

            '[[Done talking]':
                hide alkay
                return
        jump menu_alkay

        label alkay_advice:
            p "Do you have any pieces of wisdom you would be willing to share?"
 
            alkay "Certainly! In Vivarioss, or \"Concord\" as you know it, and indeed throughout of this wonderful planet there exists an entirely infant world - 
            and she is still learning to crawl."
            
            alkay "I am an old man, and not to \"toot my own horn\" as you humans say, but I have seen my fair share of conflict, 
            suffering, violence, camaraderie, hope, and strength to know a thing or two about living and breathing creatures."
            
            alkay "We are all the same - over simplified and cliché as it may sound."

            alkay "But I have spent many, many years amongst my people, your people, 
            and the entirely new people that live here on Bridge."

            alkay "They are neither human, nor kaldrean - but something novel, unique, miraculous even."

            p "I\'m not entirely sure I follow."
            
            alkay "think of it like this: you are not the same person as your mother and father. You are separate and you are independent."
            
            alkay "They gave you life and they brought you up, but ultimately you shape yourself."

            p "But I am still a human."
             
            alkay "Ah, but you see, we are still living beings. The people who live here may appear kaldrean or human, 
            but they are a new people with a new culture."

            alkay "You must be prepared to navigate this place with an open mind -
            and you must try. I cannot promise that my words will miraculously change you - that takes years."
            
            alkay "I simply hope that I can provide you with an idea of what lies ahead."

            p "Of course. Thank you so much."

            $last_dialog = '[is there anything else I can help you with?]'
            return

        label alkay_events:
            p "Have you heard rumors of racial tension here on Concord."

            alkay "When you run a business where it is practically your job to know people, you certainly do have a chance to hear all the talk."

            alkay "So yes, I have heard about this \"tension,\" as you refer to it." 
            
            alkay "However, I think that the terminology is all wrong - \"tension\" 
            comes across so poorly that people are afraid to speak about it... so I commend you [alias.first] for your bravery to broach the subject." 
            
            alkay "But this is no ordinary \"tension.\""

            p "You\'re going to have to elaborate, how do you mean this is not simply tension? What more do you think this is?"

            alkay "Its a change. I remember back when our first dark-energy craft were created, how you could smell the ozone and the distinct and 
            the scent of dark-energy in the atmosphere." 

            alkay "You could feel the drives buzzing like beatles inside your very bones. 
            The energy became a volume that you were suddenly within."

            alkay "You can feel that energy here - it is not \"tension\" 
            because that implies that things are pulling apart, but it is union, when you can sense them becoming closer."

            p "Are you always this well-spoken?"

            alkay "Ha! I have had many years to develop that talent. But, I find that I can only really let loose when it is something that I am passionate for."

            p "So you\'re passionate about whatever this \"union\" is that you referred to."

            alkay "Definately. I think that we, as separate races, are about to recognize a fundamental similarity and overcome a great deal of the separation we\'ve self-imposed."

            p "I see. I\'m grateful for your wise words."

            $last_dialog =  "It was my pleasure. Is there anything else you want to know?"
            return

        label alkay_adam_tree_start:
            p "I talked to Adam Demeter and he said that you would be enthusiastic to meet a friend."
            $ plot_state.alkay_adam_info = InfoGet.SUCCESS
            
            alkay "You know Adam? Ha! Any friend of Adam is a friend of mine!"

            alkay "He and I are very close, he frequents my restaurant when he is not working or enjoying is rather comfortable retirement."

            alkay "We go way back as you might already know. Adam does like to talk as much as I do! Anyway we met under rather strange circumstances..."

            alkay "but for his sake, I think I will leave most of that story up to him to tell. His experiences during the conflict were... traumatic."

            p "How do you mean? Was he tortured or did he lose someone close to him?"

            alkay "I wont divulge that information for his sake. He has sole rights to it."

            p "I see."

            alkay "I still have regrets about... nevermind. If our military had been more organized at the 
            time we could have avoided a great deal of the pain inflicted upon both sides"

            alkay "I fear for the kaldrean people often, especially when I see the triumphs of humanity\'s democratic unions. The thought of Qolisk\'s controllers grinds my plating."

            $last_dialog = "However, like we saw throughout the first contact conflict and the construction of this wonderful city, our future then was bright as it is now."
            
            menu:
                alkay "[last_dialog]"
                '[[ask about Alkay\'s bitterness]':
                    jump alkay_adam_tree_bitterness
                '[[ask about Alkay\'s hopefulness]':
                    jump alkay_adam_tree_hopefulness

            label alkay_adam_tree_bitterness:
                p "You seem quite bitter when you refer to Qolisk's government. Why exactly is that?"

                alkay "Bitter... me? You do not know the half of it. During the conflict the government was difficult to say the least."

                alkay "Had I not stepped in when and where I did the conflict would not have ended as it did, and the chances of alliance would be virtually nonexistent." 

                $last_dialog = "Disobedience is dishonorable, but disobeying fundamentally wrong orders is another matter altogether. I chose to do what was right over what was obedient."

                menu:
                    alkay '[last_dialog]'
                    '[[ask about VL]':
                        jump alkay_adam_tree_bitterness_VL
                    '[[Will things change?]':
                        jump alkay_adam_tree_bitterness_change

                label alkay_adam_tree_bitterness_VL:
                    p "Do you think that the Valak Lideri share a similar viewpoint?"
                    
                    alkay "That was an awfully rapid change of subject there, [alias.first]."

                    p "I\'m just trying to get a better idea. From what I\'ve heard the Valak Lideri are a threat - so naturally that has me asking questions."

                    alkay "I understand. Everyone calls the Valak Lideri a threat and a group of dangerous terrorists with terrorist intent."

                    alkay "While this may have some basis in reality I feel we are misrepresenting them. Like most rebellious groups they have a cause and they are willing to fight for it."

                    alkay "Although, the manner with which they desire to accomplish their goals is questionable. But sometimes, we have to make concessions to serve a greater purpose."

                    p "Right. If we didn\'t then there wouldn\'t be any progress. Thank you for answering my questions Alkay."

                    $last_dialog = "It was my pleasure "+alias.first+". Is there anything else you would like to know?"
                    jump menu_alkay

                label alkay_adam_tree_bitterness_change:
                    p "Do you think things are about to change?"
                    
                    alkay "I know what you mean, despite how general that question was. Yes, change is inevitable - great change. 
                    When Concord was Constructed they literally had to move mountains."

                    alkay "This place is capable of what can only be called miracles - when that kind of power is 
                    condensed into a single point, there is no stopping its impetus."
                    
                    p "With conviction like that you should probably be doing my job."

                    $last_dialog = "Ha. I'm much happier here than I have ever been. Do you have any other questions you would like me to consider?"
                    jump menu_alkay

            label alkay_adam_tree_hopefulness:
                p '[[ask about hopefulness]'
                alkay '[[explains that things are not as bad as they used to be, and perhaps a great change is on the horizon.]'
                $last_dialog = '[We are close. Now, is there anything else I can do for you?]'
                jump menu_alkay

        label alkay_VL_tree_start:
            p '[[ask about VL]'
            menu:
                alkay '[[seems perturbed by the question. But answers that he has heard of this group.]'
                '[[What does VL mean?]':
                    jump alkay_VL_tree_translate
                '[[Ask about kaldrean history]':
                    jump alkay_VL_tree_history

            label alkay_VL_tree_translate:
                p '[[What does VL mean?]'
                alkay '[[Translates VL for you. Mentions kalaras dialect. Finds it odd that a group should name themselves strangely. Jokes about and won\'t really offer more info]'
                $plot_state.alkay_vl_info = InfoGet.SUCCESS
                $last_dialog = '[Is there anything else you would like to know?]'
                jump menu_alkay

            label alkay_VL_tree_history:
                p '[[Ask about kaldrean history]'
                alkay '[[explains brief history, leaving out how the capital used to be called \"Beacon.\" Mentions something about a \"sovereign paradise.\"]'
                $last_dialog = '[Is there anything else you would like to know?]'
                jump menu_alkay

        label alkay_Bg_tree_start:
            p '[[ask about Alkay\'s background]'
            menu:
                alkay '[[smiles and shares his history, clearly leaving something out - corrupt kaldrean gov\'t]'
                '[[ask about Adam]':
                    jump alkay_Bg_tree_adam
                '[[ask about experiences]':
                    jump alkay_Bg_tree_experiences

            label alkay_Bg_tree_adam:
                p '[[ask about Adam]'
                alkay '[[mentions that he is a dear friend for many years. Mention my name when you talk to Adam]'
                $plot_state.alkay_talk_adam  =True
                $last_dialog = '[He is a good man. What else would you like to know?]'
                jump menu_alkay

            label alkay_Bg_tree_experiences:
                p '[[ask about experiences]'
                alkay '[[smiles and shares more history, still leaving out opinions regarding gov\'t.]'
                $last_dialog = '[What else would you like to know?]'
                jump menu_alkay

        label alkay_VL_plan_sympathy:
            p '[[show sympathy with VL]'
            alkay '[[Alkay suspects something is up when you suddenly show support for the VL]'
            $last_dialog = '[Be careful what you say to others, son. Is there anything else you would like to know?]'
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            return

        label alkay_VL_plan_lie:
            p '[[lie about what you know]'
            alkay '[[immediately spots your lie and will assume that you are liar. Won\'t give information away to liars]'
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            hide alkay
            return

    label alkay_VL_accuse_tree_start:
        p '[[accuse Alkay of being involved with VL]'
        menu:
            alkay  '[[Alkay begins to speak quieter, but doesn\'t deny being VL straight on. 
            You must coerce him to give you more information. If successful, you learn the VL\'s assassination plan.]'
            '[[I\'ve been told what this hardship is like. I want to help things change]':
                jump alkay_VL_accuse_tree_hardship
            '[[threaten to reveal his intent if he does not tell you his plans]':
                jump alkay_VL_accuse_tree_threaten

        label alkay_VL_accuse_tree_threaten:
            p '[[threaten to reveal his intent if he does not tell you his plans]'
            alkay '[[you cannot scare me. Do not make me laugh]'
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            $last_dialog = '[You are holding up the line. Be brief.]'
            jump menu_alkay

        label alkay_VL_accuse_tree_hardship:
            p '[[I\'ve been told what this hardship is like. I want to help things change]'
            if plot_state.lorisk_vl_plan_info == InfoGet.SUCCESS:
                $last_dialog = '[nods in approval, recognizing authenticity. Pauses. I trust you, kid. I can see the spark of change in your eye. By mid morning tomorrow that change will be realized.]'
                jump alkay_VL_accuse_tree_hardship_approval
            else:
                $last_dialog = '[applauds your apparent passion. Detects that you have no basis for this assertion. Questions you.]'
                jump alkay_VL_accuse_tree_hardship_question

        label alkay_VL_accuse_tree_hardship_approval:
            menu:
                alkay '[last_dialog]'
                '[[ask if there is a way to spur revolution without killing Vatrisk]':
                    jump alkay_VL_accuse_tree_hardship_approval_vatrisk
                '[[if you could do it differently how would you?]':
                    jump alkay_VL_accuse_tree_hardship_approval_different

            label alkay_VL_accuse_tree_hardship_approval_vatrisk:
                p '[[ask if there is a way to spur revolution without killing Vatrisk]'
                alkay '[[Chuckles, saying the only way that would ever happen is if Vatrisk came out one day and publicly denounced the kaldrean government. 
                But that\'s not likely to happen any time this millennium.]'
                $last_dialog = '[You have my trust. Is there anything else you want to know?]'
                $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                jump menu_alkay

            label alkay_VL_accuse_tree_hardship_approval_different:
                p '[[if you could do it differently how would you?]'
                alkay '[[You cannot solve problems effectively by simply shooting your way through it. You can only solve them quickly. 
                We have no choice now, but in my years of experience, even the deepest wounds are healed when words close wars]'
                $last_dialog = '[You have my trust. Is there anything else you want to know?]'
                $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                jump menu_alkay

        label alkay_VL_accuse_tree_hardship_question:
            menu:
                alkay '[last_dialog]'
                '[[lie and push that you know what you are talking about]':
                    jump alkay_VL_plan_lie
                '[[admit that you were embellishing, but pursue the change]':
                    jump alkay_VL_accuse_tree_hardship_embellishing

            label alkay_VL_accuse_tree_hardship_embellishing:
                p '[[admit that you were embellishing, but pursue the change]'
                menu:
                    alkay '[[Believes you, but requires further convincing.]'
                    '[[trust me when I say this is important to me]':
                        jump alkay_VL_accuse_tree_hardship_embellishing_important
                    '[[you don\'t have to believe me. But I AM on speaking terms with Irridiss. That is a fact.]':
                        jump alkay_VL_accuse_tree_hardship_embellishing_irridiss

                label alkay_VL_accuse_tree_hardship_embellishing_irridiss:
                    p '[[you don\'t have to believe me. But i AM on speaking terms with Irridiss]'
                    alkay '[[Alkay: laughs. I suppose you know then that the Ambassador always takes a stroll through the grove at sunrise. 
                    Sometimes we talk. Now be on your way. I have a line out the door]'
                    $last_dialog = '[You have my trust. Is there anything else you want to know?]'
                    $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                    jump menu_alkay

                label alkay_VL_accuse_tree_hardship_embellishing_important:
                    p '[[trust me when I say this is important to me]'
                    alkay '[[It is important to us too. That does not suddenly gain you access a change you cannot comprehend.]'
                    $last_dialog = '[Keep your head down. Is there anything else you want to know?]'
                    $plot_state.alkay_vl_plan_info = InfoGet.FAIL
                    jump menu_alkay
