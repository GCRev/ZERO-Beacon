
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Adam Demeter

label ch_adam:
    show adam at char_pos
    if plot_state.adam_met:
        $ last_dialog = 'Hello again, ' + alias.first + '. What can I do for you?'
        adam '[last_dialog]'

    else:
        adam "Hello! Or as the kaldreans say \"kevey\"! Welcome to my humble living space and please make yourself comfortable. I'm always happy to meet new people! I'm Adam by the way."
        p "It's a pleasure to meet you Adam. I'm [alias.full]. But if we're on a first name basis, you can just call me [alias.first]."
        adam "Likewise, [alias.first]. If there is anything I can get you just let me know, or perhaps you just want to ask some questions? 
        I'm always open to converse. I haven't seen you around... are you a new arrival?"
        p "I am."
        $ last_dialog =  "Even better! I'm sure you have some questions about Concord then. Please, ask away"

        adam '[last_dialog]'

        $ plot_state.adam_met = True

    label menu_adam:
        menu:
            adam '[last_dialog]'
            'Ask Adam for advice':
                call adam_advice
            'Ask Adam about his opinions on recent events':
                call adam_events
            'Ask Adam about Valak Lideri' if plot_state.stage == PlotStage.VL_INFO:
                jump adam_VL_tree_start
            'Ask Adam about his background' if plot_state.stage == PlotStage.VL_INFO:
                jump adam_Bg_tree_start
            'Alkay sent me' if plot_state.alkay_talk_adam == True:
                call adam_alkay_dialog
            'Done talking to Adam':
                hide adam
                return
        jump menu_adam

        label adam_advice:
            p 'Do you have any advice for a citizen new to Concord - particularly a diplomat?'

            adam 'To us, here, the person that you were before you arrived does not necessarily shape you. I have learned slowly but surely that the dynamic 
            here is far different than Earth, the wonderful planet upon which I grew up. There, you are what you were – the person that is you becomes what
            others can gather by looking at your past.'
            
            p 'And the dynamic here is far different.'

            adam "Exactly. Simply by saying that you've shown how it impresses upon you. Here, you are what you make yourself – we have the kaldreans to thank for this. 
            They judge based on ends rather than means. Not the best, but certainly different. But you can see that it has rubbed off on us. Asking about one's past is 
            generally regarded as very personal information to kaldreans – so be careful when jumping into this topic... anyone. Some will be ready and willing to share, others... 
            not so much."

            p "And how do you find this - exchange?"

            adam "Personally, I do not mind it. I think it suits this new beacon of hope to have an entirely new culture to both races."

            p "Of course."

            $last_dialog = 'Is there anything else I can help you with?'
            return

        label adam_events:
            p "You seem like you're in the know about recent events. What do you think about these tensions?"

            adam 'It seems like a ploy to me - someone is looking for problems and they are eager to place blame wherever it may settle.'

            p 'You think that someone is creating this tension on purpose.'

            adam "There is such a thing as ambient tension, but then there is the reek of hate that clings to what we call \"rumors.\" I can smell it - and believe me,
            I know it because I've experienced it before. Concord, while a beacon for galactic peace, is equally fragile. Only fifty years a settlement - if I can remember 
            its inception and creation, then it is NOT old enough to be entirely stable. I only hope that this tension passes quickly, because the last thing we need now
            is another conflict we cannot weasel our way out of."

            $last_dialog = "Any time! Now, what else would you like to talk about?"
            return

        label adam_alkay_dialog:
            p "Actually, Alkay wanted me to talk to you."
            
            adam "Yes, of course, any friend of Alkay is a friend of mine! What would you like to know, [alias.first]?"
            
            p "Well, he mentioned a little bit about how you two met, what was your perspective?"
            
            adam "That's not something I'd normally share with strangers, but if Alkay sent you, I'm sure that I can trust you."
            
            adam 'Where to begin... Ah yes. The operation.'
            
            adam "I'll try to keep this as brief as I can so I don't bore you to death."
            
            adam "So I was part of the team that made first contact with the kaldreans. I was and engineer on the TSS Armada. When we first saw the aliens, the whole ship was dead silent for a long time. Seeing another intelligent being was... Wow. I can\'t even describe the emotion."
            
            adam "But I digress! Anyways, then the fighting broke out. Neither side wanted to fight, but eventually someone pulled the trigger. Attempting to communicate was practically futile because of the language and culture barriers."
            
            adam "Through the process though, I befriended Alkay. He was one of the first kaldreans to learn the human standard."
            
            adam "We were practically the emissaries of the time."
            
            adam "He was taking a huge risk doing this though. He was going against his leaders to try to stop the fighting. It was very brave of him. Some could argue foolish, but either way he was successful and we live in peace because of it."
            
            adam "Alkay and I have been friends ever since."
            
            $last_dialog = "Is there anything else I can help you with, today?"
            $ plot_state.adam_alkay_info = InfoGet.SUCCESS
            $ plot_state.alkay_talk_adam = False
            return

        label adam_VL_tree_start:
            p 'What can you tell me about Valak Lideri?'

            adam "Well, that\'s certainly an ambitious question for someone so new to Concord. How did you come across this rumor? I have been here for nearly my
            entire life and I\'ve only heard whispers of this group's existence. And I have a careful ear."

            p "I will remind you that I am a diplomat - I was chosen because I have a careful ear."

            adam "Ah yes, I see."

            p "Probably also a coincidence."

            menu:
                adam "I can relate to that - I have been involved in my fair share of coincidences throughout my life. So what do you think about this group, based off what you know? 
                I\'ve heard some conflicting and slanting viewpoints on them so I'm curious to know what you think."

                'Sympathize with Valak Lideri':
                    jump adam_VL_tree_sympathize
                'Disapprove of Valak Lideri':
                    jump adam_VL_tree_disapprove
            jump menu_adam

            label adam_VL_tree_sympathize:  
                p "I think that Valak Lideri have a stronger set of morals than the rest of us give them credit. I still think that they are risking a lot, especially now. 
                I still need to understand them better though, I\'m basically just going with what I've been told."
                        
                menu:   
                    adam "It all depends on what you\'ve been told, of course. I agree with you; they are taking a huge risk right now, but they definitely do have a strong moral heading.
                    Although, assuming they do want to spark a revolution, their apparent itch for chaos does not really make sense. They don't seem like they would be such a violent group, 
                    given their morals."       
                    'Violence will get them nowhere':
                        jump adam_VL_tree_nowhere
                    'Care less about their methods':
                        jump adam_VL_tree_care_less

                label adam_VL_tree_nowhere:
                    p "Hopefully they don\'t resort to violence - the change they want to impart on this scale... it is still too fragile."

                    adam "What you have to understand, is that there is always a time for peace and for violence. If my experiences during the first contact conflict 
                    and the years following were anything to go by... Look, you\'ll be told that a peaceful resolution is always the best answer. But when you come down with a disease, 
                    let's say, you terminate with medicine because it is a pest. The same goes for establishments. How many have shattered under the scope of a sniper rifle?"

                    p "I can see your point, but establishments and actual people are two completely different things."

                    adam "[alias.first], you did not live through the conflict the way I did. Peace works very, very well in the long term. But violence is a quick way 
                    to solve immediate problems - strategy versus tactics. You don\'t have to agree with me, we all have our separate opinions and backg
                    rounds to inform them,
                    but this is the way I have seen it work in the past."

                    $ last_dialog = "Valak Lideri, if could make any guesses, have found their way and they are willing to pursue it with great force. For a rebel group to \
                    even become a rumor they must have good cause and powerful people in the background. Is there anything else that you want to ask me?"
                
                    jump menu_adam

                label adam_VL_tree_care_less:
                    p "I don't care too much about how they go about pulling this off. As long as their intentions are strong and directed, what will come of it will be good."

                    adam "Sometimes we have to make concessions for the greater good - I found that out the hard way during the first contact conflict. 
                    You begin to question what you know about morality when lives are called into question."

                    p "I understand."

                    $ plot_state.adam_vl_info = InfoGet.SUCCESS
                    $ last_dialog = "Valak Lideri, if could make any guesses, have found their way and they are willing to pursue it with great force. For a rebel group to even \
                    become a rumor they must have good cause and powerful people in the background. Is there anything else that you want to ask me?"
                    jump menu_adam

            label adam_VL_tree_disapprove:

                p "I don\'t really know what to think of them, I haven\'t heard too much. In general, though, rebel groups like these compromise the peace that we all work so hard to keep
                afloat. While they all have their justifications and sometimes they make perfect sense, ultimately their very existence counteracts the change they seek."

                adam "Hm... there are many examples where history supports your assertion, but sometimes these groups have noticed something fundamentally wrong, and they are simply
                trying to do what is best. During first contact there were suddenly many of these rebel cells who were all fighting for what they thought was right. Some worked to 
                push us away, others to bring us together."

                p "So what exactly is your point?"

                adam "My point is that these rebel groups are not something that you simply sympathize or disagree with - they lie in a moral gray zone in which our own sense of ethics 
                begins to affect our perceptions of them."

                p "Right, that I can agree with."

                $ last_dialog = "Now you get it. Is there anything else I answer for you?"

                jump menu_adam

        label adam_Bg_tree_start:

            p "What can you tell me about your past? I don\'t mean to offend, but you look like you\'ve seen quite a great deal of change here."

            adam "That I have. But actually, I was there when we made first contact. I was a chief engineer aboard the TSS Armada, flagship of Operation Bridge - I can still 
            remember by heart swelling with pride seeing her lift off from Terra for the first time. Space was not foreign to us, but the distance from home was. Nowhere in our
             minds was the possibility that we could come into contact with another highly-intelligent biped species like our own."

            p "I imagine it was pandemonium when you first saw them?"

            adam "Boy, that moment when we stopped over bridge and saw their fleet, it was silent for a straight ten minutes. From that point on it\'s history - but I need to be 
            completely clear that neither their commander nor ours wanted the fight to break out. The warning shots eventually turned into full-on fighting. The Verdict was shot 
            down... we took down their ship the Krona... it was a disaster."

            p "So how did you end up resolving tensions with the kaldreans?"

            adam "It was certainly difficult trying to communicate  with one another. As I\'m sure you can guess it was like being thrust into a completely different culture. We 
            landed here and then we tried to establish some form of communications. Throughout the process I became friends with a kaldrean, Alkay - wonderful character that one."

            p "So I take it you were around when Concord was constructed."

            adam "For the first decade I was actually back on Terra. But I decided to come back here and do my best to facilitate the friendship between the kaldreans and humans."

            p "Clearly your work paid off."

            menu:
                adam "You could certainly say that."
                "Ask Adam about Alkay":
                    jump adam_Bg_tree_Alkay
                "Ask Adam about the first contact conflict":
                    jump adam_Bg_tree_conflict

            label adam_Bg_tree_Alkay:
                p "You mentioned Alkay?"

                adam "Oh he\'s been a friend of mine for many years now. He was actually instrumental in resolving the conflict because he was one of the first kaldreans to learn 
                human standard -  probably THE first, actually. When I was... when I was working alongside them during the war he and I were unofficial emissaries. When you next stop 
                by Oasis tell him I sent you - he\'ll be happy to know."

                $ plot_state.adam_talk_alkay = True
                $ last_dialog = 'Is there anything else I can help you with?'
                jump menu_adam

            label adam_Bg_tree_conflict:
                p "So, could you explain your experience in the first contact conflict a little more?"

                adam "I suppose... although the events that transpired affected quite a few people, including a number of those who live here on Concord. I\'ll try to keep this brief 
                because you really don\'t need to hear about all the problems. With the Verdict and the Krona damaged beyond repair the rest of our ships landed planet-side because we 
                needed to make repairs. Fire was exchanged on the ground despite explicit orders on boths sides not to. Some of our scouts went missing at about the same time that our
                people made hostages out of their scouts. It was all quite tense - lives were unnecessarily lost."

                p "Are you okay?"

                adam "Yeah. I'm still upset by how much pain we could have avoided if we had been better prepared. So just always remember, [alias.first], go prepared; you\'ll never know
                quite what to expect out there."

                p "I'll do my best."

                $ last_dialog = "Hopefully your best is better that ours was. Anything else I can help you with today?"
                jump menu_adam

