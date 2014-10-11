
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

        alkay "[alias.first]. It is my pleasure. Please, have a seat. The first meal is always on the house. We’ll talk over some good food. Feel free to ask me anything."
        
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

            p "I’m not entirely sure I follow."

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

            p "You’re going to have to elaborate, how do you mean this is not simply tension? What more do you think this is?"

            alkay "Its a change. I remember back when our first dark-energy craft were created, how you could smell the ozone and the distinct and 
            the scent of dark-energy in the atmosphere." 

            alkay "You could feel the drives buzzing like beatles inside your very bones. 
            The energy became a volume that you were suddenly within."

            alkay "You can feel that energy here - it is not \"tension\" 
            because that implies that things are pulling apart, but it is union, when you can sense them becoming closer."

            p "Are you always this well-spoken?"

            alkay "Ha! I have had many years to develop that talent. But, I find that I can only really let loose when it is something that I am passionate for."

            p "So you’re passionate about whatever this \"union\" is that you referred to."

            alkay "Definately. I think that we, as separate races, are about to recognize a fundamental similarity and overcome a great deal of the separation we’ve self-imposed."

            p "I see. I’m grateful for your wise words."

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

            alkay "I fear for the kaldrean people often, especially when I see the triumphs of humanity's democratic unions. The thought of Qolisk's controllers grinds my plating."

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
                    p "Do you think that Valak Lideri share a similar viewpoint?"
                    
                    alkay "That was an awfully rapid change of subject there, [alias.first]."

                    p "I'm just trying to get a better idea. From what I've heard Valak Lideri are a threat - so naturally that has me asking questions."

                    alkay "I understand. Everyone calls Valak Lideri a threat and a group of dangerous terrorists with terrorist intent."

                    alkay "While this may have some basis in reality I feel we are misrepresenting them. Like most rebellious groups they have a cause and they are willing to fight for it."

                    alkay "Although, the manner with which they desire to accomplish their goals is questionable. But sometimes, we have to make concessions to serve a greater purpose."

                    p "Right. If we didn't then there wouldn't be any progress. Thank you for answering my questions Alkay."

                    $last_dialog = "It was my pleasure "+alias.first+". Is there anything else you would like to know?"
                    jump menu_alkay

                label alkay_adam_tree_bitterness_change:
                    p "Do you think things are about to change?"
                    
                    alkay "I know what you mean, despite how general that question was. Yes, change is inevitable - great change. 
                    When Concord was Constructed they literally had to move mountains."

                    alkay "This place is capable of what can only be called miracles - when that kind of power is 
                    condensed into a single point, there is no stopping its impetus."
                    
                    p "With conviction like that you should probably be doing my job."

                    $last_dialog = "Ha. I'm much happier here in my restaurant than I have ever been. Do you have any other questions you would like me to consider?"
                    jump menu_alkay

            label alkay_adam_tree_hopefulness:
                p "You think the future is bright? That is quite the opposite from what I've heard."
                
                alkay "I can feel the pressure building - I know I am not the only one who feels it either. 
                You can sense it in the way that everyone carries themselves."

                alkay "They walk with increasing strength when the sun rises every morning. Their eyes have a new vitality and their voices carry just a little farther."

                alkay "Soon enough, paradigms will shift and changes will sweep over all of us."

                p "Your conviction is inspiring. Thank you for your sincerity. It's not exactly easy to come by."
                
                $last_dialog = 'And thank you for your kind words. Now, is there anything else I can do for you?'
                jump menu_alkay

        label alkay_VL_tree_start:
            p "Can you tell me about these \"Valak Lideri?\" I've heard about them but the lack of information makes me uneasy."
            menu:
                alkay "Yes, well, I HAVE heard of this group. But they are just shadows and whispers. I cannot really offer more than my opinions."
                '[[What does VL mean?]':
                    jump alkay_VL_tree_translate
                '[[Ask about kaldrean history]':
                    jump alkay_VL_tree_history

            label alkay_VL_tree_translate:
                p "Well, perhaps you could tell me more about the title itself? I am curious to know what it means."
                
                alkay "Of course. \"Valak Lideri\" is a very, very old phrase from centuries ago. It is a member of the now-deceased {i}kalaras{/i} dialect.
                Perhaps it is like your Latin dialect."

                alkay "Literally translated it means \"Sovereign Paradise,\" which is a reference to the settling and construction of Qolisk's capital, Citadel."

                alkay "Personally I find it quite strange that a rebel group should name themselves with such an obscure phrase."

                alkay "It does fit within a modern context so it does not speak to most of the younger, and likely more rebellious crowd."

                p "Thank you for elaborating, Alkay."

                $plot_state.alkay_vl_info = InfoGet.SUCCESS
                $last_dialog = "It was my pleasure "+alias.first+". Is there anything else you would like to ask?"
                jump menu_alkay

            label alkay_VL_tree_history:
                p "Could you explain some of the kaldrean history? What were some key turning points for the kaldrean people? 
                I think knowing more about the past could put them into context."

                alkay "That is quite a broad-spectrum question, so I'll do my best to generate a concise answer."

                alkay "Just around two and a half millennia ago the Sovereign Paradise which is the largest fertile region on Qolisk. It was their beacon of hope - the could finally settle in one place."

                p "Like Mesopotamia."

                alkay "Yes, exactly."

                alkay "Following settlement, there was a sustained period of development through which multiple industrial 
                revolutions occurred and many technological boundaries were broken."

                alkay "Wars were waged, nations rose and fell, but eventually a unified government began to consolidate control."

                alkay "They quickly spread their power and their control through industry and eventually created a planet-wide union."

                alkay "They but blinders on their people and gave them comfortable access to resources to suppress chances of rebellion. The people became complacent."

                alkay "Nothing much has changed since then - a few centuries with a stable, albeit corrupted government. 
                The advent of first contact has started to change things, however."

                p "I see. So do you think that Valak Lideri want to overthrow the Qolisk's government?"

                alkay "It is entirely possible. Although that level of ambition is quite absurd."

                p "I agree. Thank you for talking with me, Alkay."

                $last_dialog = "I always have time to talk. Is there anything more you would like to ask me?"
                jump menu_alkay

        label alkay_Bg_tree_start:
            p "So how do you get here Alkay? I can tell that there is more to you than just a humble restaurant owner."

            alkay "Then your perception is sharp, because I do have a rather... colorful history. I used to be a rather high-raking individual in the kaldrean military."

            alkay "Now don't go telling everyone about this but - I was the Superior Commandant of the KAU Forerunner {i}Ardelisk{/i}: the flagship of our fleet."

            alkay "My position was the culmination of a lifetime living in a poor family without a high social status. For my family I worked and stove to reach my ambitious goals."

            alkay "I was and still am the record holder for the youngest Superior Commandant this century."

            p "What does that role entail?"

            alkay "It is like your military's \"general\" rank."

            p "Got it. Sorry for interrupting."

            alkay "Not at all. I would rather you listen and ask questions than check out and pay me no attention. So when the conflict began, none of us wanted to fight."

            alkay "However, misunderstandings between us and within our own ranks resulted in a conflict we had desperately hoped to avoid. And corruption finds it way into everything..."

            alkay "It opened my eyes to see just how infested our own military really was. I began to challenge direct orders in favor of protecting my people and yours."

            p "That's quite commendable."

            alkay "Hah! Commendable? When you are brought up believing that disobedience is the greatest weakness you may possess it was nearly impossible to weight my options."

            alkay "But I could see that times and paradigms were about to change. The men and women under my command supported me."

            alkay "Along with a great deal of help from some of your people like Elder Demeter, we were able to avert complete chaos."

            alkay "Promptly following my service to the military I resigned myself, and decided to become scarce. I wanted to leave behind the government that had lied to me."

            alkay "I spent many, many years surviving by myself. As a result I have picked up some valuable skills and learned some quite valuable lessons."

            p "I can tell. You can clearly read people."

            alkay "Yes. It is one of the skills I take pride in possessing. It is invaluable. I can see that you are learning as well."

            menu:
                alkay "I got a little carried away for a moment there. Is there anything else you would like to ask about?"
                '[[ask about Elder Demeter]':
                    jump alkay_Bg_tree_adam
                '[[ask about experiences]':
                    jump alkay_Bg_tree_experiences

            label alkay_Bg_tree_adam:
                p "I noticed that you mentioned an \"Elder Demeter\"? Who exactly is that?"

                alkay "Ah yes, Adam Demeter as you may or may not know him. We became close friends during the first contact conflict."

                p "\"Elder?\""

                alkay "Once a man or woman reaches a certain age and degree of experience they become an elder. It does not matter whether they are human or kaldrean."

                p "Of course. Please continue."

                alkay "It is thanks to him that the the humans and kadreans are speaking to one another, quite literally. In the time that he was working with us he learned to speak kaldrean common."

                alkay "I, in turn, learned human common. He is a good man and he has endured quite a lot. Quite. I think no one should have to experience what he did."

                if plot_state.alkay_talk_adam == False:
                    alkay "If you go talk to him tell him I sent you, he will be happy to know what we have met. I advise that you avoid the topic of his past in the conflict, however."
                    $plot_state.alkay_talk_adam  =True

                $last_dialog = "I think that about covers it. What else would you like to know?"
                jump menu_alkay

            label alkay_Bg_tree_experiences:
                p "You mentioned a period of time after the military where you were on your own? What were you doing?"

                alkay "So after I stepped down from my position of high rank, I stayed with my family and settled them into a more comfortable property and lifestyle."

                alkay "I dumped all the money I had into their accounts and then took my leave into the wilderness of Qolisk, craving escape."

                alkay "I built myself a cabin in a small oasis I discovered and stayed there in complete solitude. I became stronger, smarter, and more intelligent through my meditations."

                p "How did you decide when to stop?"

                alkay "I felt it. The same year that I made my journey back to Citadel was year one of Concord's construction. I was able to secure transportation from Qolisk to Bridge."

                alkay "Once I arrived I found that many of my former subordinates and some of my old friends were working on the Concord project."
                
                alkay "Instead of settling down I actually walked to the other edge of the continent and back."

                p "You're pulling my leg."

                alkay "It took me a decade - and as a result we have vital information on the flora and fauna variation that exists on this continent."

                p "That is ridiculous."

                alkay "But it is true. I was offered residence here and helped direct operations until construction was completed. At that point I just... decided to start a restaurant."

                alkay "I have the best location in the marketplace, and I content here in my elder years."

                p "I'm impressed, I can't say I've met anyone else with a history as decorated as yours."

                $last_dialog = "You would be surprised. I think I have about talked your ears off. If you have anything else to ask, I will try to brief."
                jump menu_alkay

        label alkay_VL_plan_sympathy:
            p "Listen, Alkay, I think that Valak Lideri is striving for a just cause. The corruption on Qolisk makes me sick if not uneasy."

            alkay "Hmm... you are quite convicted in your assertion there. What changed so quickly?"

            p "I've just, been listening around to these rumors."

            alkay "And why are you coming to me about this?"

            p "You seem like you would have a strong moral alignment with them, based on your opinions about the kaldrean government."
            
            alkay "While they do seem to share viewpoints with me, I do not think that I am a good source of information about them."
            
            $last_dialog = "Be careful what you say to others, [alias.first], because others might respond quite negatively to your sentiments. Is there anything else you would like to know?"
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            return

        label alkay_VL_plan_lie:
            p "Listen, Alkay, I know what Valak Lideri is and what they are planning. I want to help."
            
            alkay "Perhaps you have ingested some illegal substances, but I see that you are lying. Your voice says one thing but your mind, body, and essence say another."

            alkay "I do not know what has changed so quickly, because it seemed that moments ago you were entirely trustworthy."

            p "That's not-"

            alkay "Come back when you have decided to stop lying through your teeth, [alias.first]."
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            hide alkay
            return

    label alkay_VL_accuse_tree_start:
        p "Alkay, I can tell that you are part of Valak Lideri. If there is one thing that I have learned from you, it is how to read people."

        p "You talk big, but you cannot hide your intent from me."

        menu:
            alkay "That is quite the accusation, [alias.first]. I strongly recommend against going about and riddling this city with accusations. Take care when treading about this subject."
            '[[I\'ve been told what this hardship is like. I want to help things change]':
                jump alkay_VL_accuse_tree_hardship
            '[[threaten to reveal his intent if he does not tell you his plans]':
                jump alkay_VL_accuse_tree_threaten

        label alkay_VL_accuse_tree_threaten:
            p "Alkay, I will call in authorities if you do not tell what Valak Lideri are planning to do."

            alkay "Hah! You cannot scare me [alias.first]. Make all the threats you want, I guarantee none are as grave or intense as those I have dealt with previously."
            
            alkay "I would like to stay level with you, [alias.first]. I will pretend like you did not just accuse me of terrorist associations."
            $plot_state.alkay_vl_plan_info = InfoGet.FAIL
            $last_dialog = "If you have any more questions, please be brief - I have a line out the door."
            jump menu_alkay

        label alkay_VL_accuse_tree_hardship:
            p "I have talked with the people here - I know what kind of hardship they are enduring to see things change."
            if plot_state.lorisk_vl_plan_info == InfoGet.SUCCESS:
                
                alkay "I trust you, [alias.first]. I can see the spark of change in your eye."

                alkay "The struggle that some face is far greater than you can understand, but I can tell that you know this. I can see that you genuinely want to understand it."

                $last_dialog = "We are approaching the horizon, and by mid morning tomorrow we will cross it. The new day will be wonderful -  it will breathe life into us."
                jump alkay_VL_accuse_tree_hardship_approval
            else:
                $last_dialog = "I want to believe you, "+alias.first+", but something is irking me about your tone."
                jump alkay_VL_accuse_tree_hardship_question

        label alkay_VL_accuse_tree_hardship_approval:
            menu:
                alkay '[last_dialog]'
                '[[ask if there is a way to spur revolution without killing Vatrisk]':
                    jump alkay_VL_accuse_tree_hardship_approval_vatrisk
                '[[if you could do it differently how would you?]':
                    jump alkay_VL_accuse_tree_hardship_approval_different

            label alkay_VL_accuse_tree_hardship_approval_vatrisk:
                p "Surely you can accomplish this change without killing the Ambassador."

                alkay "Violence is never a good solution to a problem, but sometimes it is entirely necessary."

                alkay "But honestly, hah, the only way around the his death would be if Vatrisk himself came out and denounced the kaldrean government."
                
                alkay "But that is not likely to happen any time this millennium."
                $last_dialog = "You have my trust, "+alias.first+". Is there anything else you want to know?"
                $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                jump menu_alkay

            label alkay_VL_accuse_tree_hardship_approval_different:
                p "If you could go about this whole... situation differently how would you?"

                alkay "You cannot solve problems effectively by simply shooting your way through it. You can only solve them quickly."
                
                alkay "We have no choice now, but in my years of experience, even the deepest wounds are healed when words close wars."

                p "But sometimes..."

                alkay "...we have to make concessions when faced with the greater good. We have no choice, and no amount of hoping things were different can make them change."

                $last_dialog = "You have my trust. Is there anything else you want to know in the meantime?"
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
                p "Alright I admit that I was embellishing the truth a little. I still want to see this change through, however. I can tell that we are close to accomplishing this goal."

                menu:
                    alkay "I believe you, [alias.first], but your conviction falters. You are playing at the edge of the fire here on a scale you cannot possibly understand yet."
                    '[[trust me when I say this is important to me]':
                        jump alkay_VL_accuse_tree_hardship_embellishing_important
                    '[[you don\'t have to believe me. But I AM on speaking terms with Irridiss. That is a fact.]':
                        jump alkay_VL_accuse_tree_hardship_embellishing_irridiss

                label alkay_VL_accuse_tree_hardship_embellishing_irridiss:
                    p "Alright then, I won't pretend that I can understand just how vast and important this change is. That does not change the fact that I'm on speaking terms with Irridiss."
                    
                    alkay "Then I suppose you know  that the Ambassador always takes a stroll through the grove at sunrise?
                    Sometimes we talk."

                    p "I see."

                    $last_dialog = "Now be on your way; I have a line out the door. If you have any more questions I will do my best to be quick."
                    $plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
                    jump menu_alkay

                label alkay_VL_accuse_tree_hardship_embellishing_important:
                    p "I have invested myself in this cause, Alkay. This is important to me. Trust me when I say I want to help Valak Lideri bring about this revolution."
                    
                    alkay "It is important to us too. That does not suddenly gain you access a change you cannot comprehend. A few days on Concord is not long enough to grasp it."

                    p "What does that even mean? You aren't even giving me chance!"

                    alkay "Anger will not improve your chances of convincing me, [alias.first]. I do not know you well-enough to believe that you can simply \"understand\" on command."

                    $last_dialog = "So keep your head down and allow time to pass. In the meantime if you have any more questions feel free to ask."
                    $plot_state.alkay_vl_plan_info = InfoGet.FAIL
                    jump menu_alkay
