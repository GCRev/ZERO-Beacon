
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Vatrisk Irridiss Kier
   
label ck_vatrisk:
    $ show_ch('vatrisk', 'right')

    if plot_state.stage == PlotStage.VATRISK_MEET:
        call vatrisk_meeting
        return

    elif plot_state.vatrisk_met:
        
        vatrisk "Hello again, [alias.first], with what may I help you?"
        
        p "I am doing well. I actually have a few more questions for you, if you have the time."
        
        $ last_dialog = "Yes, of course. What do you need?"
        vatrisk '[last_dialog]'

    else:
        vatrisk "[alias.full], welcome to Vivarioss! Or as you may know it, Concord. It is an absolute pleasure to make your acquaintance. 
        I hope that another bright mind at work can make the cooperation and peace here even more resilient."

        p "I am going to do my best."

        vatrisk "And we will support you. Ambassador Columbus and I are committed to your success. Because your successes contribute to all of our successes."
        
        $last_dialog = "So as new arrival I trust you have some questions to ask?"
        vatrisk '[last_dialog]'

        $ plot_state.vatrisk_met = True

    label menu_vatrisk:
        menu:
            vatrisk '[last_dialog]'
            'Ask Vatrisk for advice':
                call vatrisk_advice
            
            'Ask Vatrisk about his opinion on recent events':
                call vatrisk_events
            
            'Ask about Vatrisk\'s background':
                call vatrisk_background
            
            'Flatter Vatrisk for information' if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
                call vatrisk_flatter
            
            'Bribe Vatrisk for information' if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
                jump vatrisk_bribe
            
            'Intimidate Vatrisk for information' if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.vatrisk_kald_govt_info == InfoGet.NO_ATTEMPT:
                jump vatrisk_intimidate
            
            'Inform Vatrisk of Valak Lideri' if plot_state.stage == PlotStage.VL_PLANS:
                jump vatrisk_VL_inform_tree_start
            
            'Suggest that Vatrisk publicly denounce kaldrean government' if plot_state.stage == PlotStage.VL_PLANS:
                jump vatrisk_VL_denounce
            
            'Attempt to lure Vatrisk to assassination' if plot_state.alkay_vl_plan_info == InfoGet.SUCCESS:
                jump vatrisk_VL_lure
            
            'Done talking to Vatrisk':
                $ hide_ch('vatrisk', 'right')
                return
        jump menu_vatrisk

        label vatrisk_advice:
            
            p 'What advice would you have for someone like me?'
            
            vatrisk 'I definitely recommend going to Alkay\'s restaurant. You\'d probably know it as Oasis. He makes the most delicious vaska.'
            
            p 'Good to know, I\'ll keep that in mind. Anything else you could tell me?'
            
            vatrisk 'Don\'t believe everything you hear. I\'ve ran into many liars in my life, and they can destroy people. I\'ve seen good people have their careers get destroyed by a single lie, and I believe it shouldn\'t happen to anyone.'
            
            p 'Thank you for the advice.'
            
            $ last_dialog = 'Anytime, anything else I can help you with today?'
            
            return

        label vatrisk_events:
            
            p 'So what\'s your take on all of this tension in the city?'
            
            vatrisk 'I can assure you that all of this tension is just plain hype. This is just some people getting used to the different cultures, and they will be used to it soon.'
            
            $last_dialog = 'Anything else?'
            return

        label vatrisk_background:
            
            p 'What can you tell me about your past?'
            
            vatrisk 'Well, I was born and raised on Qolisk, went through school just like everyone else, and joined the military. They had me installed in Concord a few years back and I made my way up the rankings. Not much of a story, but that\'s me.'
            
            return

        label vatrisk_flatter:
            
            p 'I don\'t think that anyone understands how hard you work to achieve peace here.'
            
            vatrisk 'Finally someone who understands. It\'s not easy being this kind of leader. Sure, our government is a little strict, but that\'s how it has always been!'
            
            vatrisk 'It\'s hard with all of these rules and everything, but it works. Crime rates are low as ever. You wouldn\'t believe how hard it is to balance happiness with safety these days.'
            
            $ last_dialog = 'Anyways, what else can I do for you?'
            $plot_state.vatrisk_kald_govt_info = InfoGet.SUCCESS
            return

        label vatrisk_intimidate:
            
            p 'Tell me. Why are you making the government so harsh?'
            
            vatrisk 'Excuse me?'
            
            p 'You heard me.'
            
            $ last_dialog = 'Talk to me when you have calmed down.'
            $plot_state.vatrisk_kald_govt_info = InfoGet.FAIL
            $ hide_ch('vatrisk', 'right')
            return

        label vatrisk_bribe:
            p 'Here, a gift from our embassy to yours.'
        
            'You give Vatrisk a lot of money in attempt to bribe him for the truth.'
            
            if plot_state.high_emb_tried_bribe:
                $ last_dialog = 'I know your type. Bribes cannot phase me.'
                $plot_state.vatrisk_kald_govt_info = InfoGet.FAIL
                return
            
            else:
                vatrisk 'Oh my... I can buy a lot of vaska with this...'
                
                vatrisk 'Please feel free to ask me anything.'

                p 'Well I was hoping you could tell me why there would be all of these rumors about the kaldreans feeling oppressed'

                vatrisk 'Ok, look. It\'s not easy being me. I have to deal with the pressure of being blamed for everything that this government does.'

                vatrisk 'Even though I don\'t agree with it all the time.'

                vatrisk 'I wish there was a way to keep everyone happy AND safe. It\'s practically impossible. Have you ever read Vel Kerriss\' \"Dystopia\"?'

                p 'I am not familiar.'

                vatrisk 'Well it basically describes our government. How we keep everyone safe with rules and law.'

                vatrisk 'I feel what people fail to understand is that safety is more of a priority than happiness.'

                p 'I kind of see what you mean.'

                $plot_state.vatrisk_kald_govt_info = InfoGet.SUCCESS
                $last_dialog = 'Is there anything else I can help you with today?'
                jump menu_vatrisk

        label vatrisk_VL_denounce:
            p 'You should denounce the kaldrean government.'
            
            vatrisk 'What?'
            
            p 'You heard me.'

            $ last_dialog = 'Come back when you have something intelligent to say.'
        
            $plot_state.vatrisk_trust = TrustLevel.LOW
            $ hide_ch('vatrisk', 'right')
            return

        label vatrisk_VL_inform_tree_start:
            p 'Irridiss, your life is in grave danger! Valak Lideri plan to kill you and take down the government.'
            menu:
                vatrisk 'Come again?'
               
                'Ask Vatrisk to denounce government':
                    jump vatrisk_VL_denounce
               
                'Ask Vatrisk what is best for is his people':
                    jump vatrisk_VL_inform_tree_ask

            label vatrisk_VL_inform_tree_ask:
              
                p 'You need to think. What is best for your people?'
               
                vatrisk 'The entire point of a government is to keep it\'s people safe, not happy. Sure, we may oppress them in some ways, but look at the crime rates. We prevent war!'
              
                if plot_state.vatrisk_trust == TrustLevel.LOW or plot_state.vatrisk_trust == TrustLevel.MEDIUM:
                    jump vatrisk_VL_inform_tree_no_change

                if plot_state.vatrisk_trust == TrustLevel.HIGH:
                    jump vatrisk_VL_inform_tree_not_sure

                if plot_state.vatrisk_trust == TrustLevel.VERY_HIGH:
                    jump vatrisk_VL_inform_tree_persuade

            label vatrisk_VL_inform_tree_no_change:
                
                vatrisk 'There is no way that you can change my mind. I will never let this government fall.'
               
                $last_dialog = 'Thank you for talking to me, ' + alias.title_last + '.'
                jump menu_vatrisk

            label vatrisk_VL_inform_tree_not_sure:
               
                menu:
                    
                    vatrisk 'But now I\'m not so sure. With the my life in danger, I\'m not sure who I can trust anymore.'
                    
                    'Tell Vatrisk that the government is weak right now':
                        
                        p 'The kaldrean government is weak right now. This rebellion will guarantee the change that your people seek.'
                       
                        vatrisk 'I cannot risk the stability of the government for these rebels.'
                      
                        jump vatrisk_VL_inform_tree_no_change
                  
                    'Tell Vatrisk that his people need him now more than ever':
                  
                        p 'Your people are depending on you to fix this. Those rebels are just like you and I. They do not really want to kill you, but they will if they must.'
                    
                        jump vatrisk_VL_inform_tree_persuade

            label vatrisk_VL_inform_tree_persuade:
              
                p 'Your people are depending on you to fix this. Those rebels are just like you and I. They do not really want to kill you, but they will if they must.'
               
                'He thinks for a long moment.'
                
                vatrisk 'You are right. \"It\'s time for me to act.\"]'

                call ending_vatrisk_denounce_govt
                return

        label vatrisk_VL_lure:
           
            p 'Allow me to accompany you on your morning walk tomorrow. It would be my pleasure.'
           
            if plot_state.vatrisk_trust == TrustLevel.HIGH or plot_state.vatrisk_trust == TrustLevel.VERY_HIGH:

                vatrisk 'Ah, of course my friend. I\'d be happy to show you around my garden.'

                p 'Actually, I was hoping that you could show me around the grove.'
           
                vatrisk 'That seems like a lovely place for a walk. Ordinarily my guards ask me to stay away from that area, but I trust you. I will meet you there at 08:00 tomorrow.'
           
                call ending_vatrisk_lure
           
                return
           
            else:
            
                vatrisk 'I am terribly sorry, but I will not be going out tomorrow morning as I will be busy.'
            
                $last_dialog = 'Perhaps another time. Until then, are there any other questions I may answer?'
            
                jump menu_vatrisk
                
    label vatrisk_meeting:

        vatrisk "Hello, Diplomat [alias.last]. How can I help you?"
       
        p "I want to talk about recent political unrest in the city."
      
        vatrisk "Oh. I see. But I was told you were here to discuss interstellar trade laws."
      
        p "I am sorry but that was not true. I'm actually here to discuss Valak Lideri. I have evidence that your life may be in danger."

        vatrisk "Really? And what is this evidence?"

        if plot_state.adam_vl_info == InfoGet.SUCCESS:
        
            p "Valak Lideri want to start a progressive revolution, and they are willing to go to any means necessary to accomplish that."

            p "Which includes assassinating you."
        
            vatrisk "I find that quite unlikely, [alias.last]. I am perfectly safe here."
        
        
        if plot_state.jon_vl_info == InfoGet.SUCCESS:
        
            p "They think that the kaldrean people deserve liberation from the corrupted government. They see you as a figurehead for it. I can't argue with that."
        
            vatrisk "Well... I cannot quite argue with that either. There was a tumult for a while when I was first given office as Ambassador."
        
        if plot_state.alkay_vl_info == InfoGet.SUCCESS:
        
            p "Valak Lideri wish to bring back what was previously known as \"Beacon.\" They want to restore the golden age and make sure it lasts."
        
            vatrisk "That sounds unrealistic. Do they not realize how unstable they would make our people?"

        if plot_state.lorisk_vl_info == InfoGet.SUCCESS:
        
            p "If you weren't aware, \"Valak Lideri\" {i}means{/i} \"Beacon.\" They are going to be the beacon for this revolution, 
            and they are likely going to make an example out of you to start it."
            
            p "Your death would be the wind underneath the wings of the progressive movement."

            p "I have no reason to lie to you, Ambassador. And I am quite assured that the evidence all points to this. You won't regret this."

        $ possible_infos = [plot_state.adam_vl_info, plot_state.alkay_vl_info, plot_state.jon_vl_info, plot_state.lorisk_vl_info]
        $ gotten_infos = [info_state for info_state in possible_infos if info_state == InfoGet.SUCCESS]
        $ pct_gotten_infos = float(len(gotten_infos)) / len(possible_infos)

        if pct_gotten_infos == 0:
        
            p "Well, I don't actually have any proof but please, you have to believe me!"

        if pct_gotten_infos < 1.0 / 3.0:
        
            vatrisk "Well, idle talk will not convince me of any threats."
        
            jump vatrisk_meeting_fail
        
        elif pct_gotten_infos > 2.0 / 3.0:
        
            vatrisk "Are you sure that all of this is true?"
        
            p "Absolutely."
        
            jump vatrisk_meeting_success
        
        else:
        
            menu:
        
                vatrisk "This information is definitely unnerving, but I'm still not entirely convinced. Tell me,
                why should I trust you, an Earthling diplomat who seems to have turned vigilante?"
        
                "Tell Vatrisk that his people need him":
        
                    p "Your people need you more than ever now. You shouldn't take any risks that would leave them helpless in such a time of need."
        
                    vatrisk "You're right."
        
                    jump vatrisk_meeting_success
        
                "Tell Vatrisk that he must trust you":
        
                    p "You need to trust us. We're only looking out for your best interests."
        
                    vatrisk "Humans never have had our best interests in mind!"
        
                    jump vatrisk_meeting_fail
        
                "Tell Vatrisk that the rebels are dangerous":
        
                    p "These rebels are dangerous enemies of the peace. You should fear them."
        
                    vatrisk "I don't need to fear those silly rebels."
        
                    jump vatrisk_meeting_fail

        label vatrisk_meeting_fail:

            vatrisk "Now, If you would excuse me, I have a transport to board."

            "The ambassador leaves the room and walks to his personal landing pad to board his transport. 
            You follow him, still trying to dissuade him from leaving the safety of the High Embassy without guard."

            scene bg landing_pad with move
            
            "Ignoring your protests, he boards the transport. Soon after it takes off, you hear a deafening blast."
            
            play sound "assets/sf_attack1.ogg"
            
            $ renpy.pause(delay=6)
            
            "The ships seems to have been shot! It begins falling."
            
            play sound "assets/sf_attack2.ogg"
            
            "Miraculously, the pilot manages to safely land the critically wounded pod on the landing pad."
            
            $ renpy.pause(delay=6)
            
            "Ambassador Kier steps out, clearly shaken, but seemingly uninjured."
            
            if pct_gotten_infos < 1.0 / 3.0:
            
                vatrisk "You were right! They tried to kill me. But how did you know? This makes no sense..."
                $ plot_state.vatrisk_trust = TrustLevel.MEDIUM
            
            else:
            
                vatrisk "You were right! Thank you for trying to save my life."
            
                p "We need to get you to safety!"
            
                vatrisk "Right away! Guards!"
            
                $ plot_state.vatrisk_trust = TrustLevel.HIGH
            jump vatrisk_meeting_end

        label vatrisk_meeting_success:
            
            vatrisk "Well, I was about to leave to board a transport, but I'm not sure anymore. My life could be in danger. I trust you, [alias.full]."
            
            "You and the ambassador sit and talk about Valak Lideri for a bit longer. Then, you hear a sudden,
            deafening blast from outside Kier\'s office."

            play sound "assets/sf_attack1.ogg"
            
            $ renpy.pause(delay=6)
            
            "The sounds of an aircraft plummeting to the ground come from outside."
            
            play sound "assets/sf_attack2.ogg"
            
            $ renpy.pause(delay=6)
            
            vatrisk "That was my transport! You saved my life. I am eternally grateful. If you need anything, you have my full trust."
            
            $ plot_state.vatrisk_trust = TrustLevel.VERY_HIGH
            jump vatrisk_meeting_end

        label vatrisk_meeting_end:
            
            "You return to Sarah to discuss what you've witnessed."
            
            stop sound
            
            $ plot_state.stage = PlotStage.ATTACK_JUST_HAPPENED
            return
