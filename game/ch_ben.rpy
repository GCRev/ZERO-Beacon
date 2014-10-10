
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Benjamin Columbus

label ch_ben:
    show ben at char_pos

    if plot_state.ben_met:
        $ last_dialog = "Hello again, " + alias.first + ". What can I do for you?"
        jump menu_ben
    else:
        ben "I was told we were going to have a new team member. You must be [alias.first]."
        p "That is me."
        ben "Wonderful. As you might already know, I'm Ambassador Columbus. But please, just call me Ben. I hope that your time on Concord thus far has been pleasant."
        p "It\'s a beautiful city."
        $ plot_state.ben_met = True
        $ last_dialog = "It certainly is. Now, everyone who comes to the High Embassy has a reason to do so, so what can I do for you today?"
        jump menu_ben

    label menu_ben:
        menu:
            ben "[last_dialog]"
            "Ask for advice":
                call ben_advice
            "Ask for opinion on recent events":
                call ben_events
            "Ask about kaldrean government" if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.ben_kald_govt_info != InfoGet.SUCCESS:
                call ben_ask_kald_govt
            "Ask about his day" if plot_state.stage == PlotStage.KALD_GOVT_INFO  and plot_state.ben_kald_govt_info != InfoGet.SUCCESS and plot_state.ben_talk_lida == False:
                call ben_ask_day
            "Ask about Ben's past":
                call ben_Bg
            "Mention Lida" if plot_state.stage == PlotStage.KALD_GOVT_INFO and plot_state.ben_kald_govt_info != InfoGet.SUCCESS  and plot_state.ben_talk_lida == True:
                call ben_mention_lida
            "Done talking":
                hide ben
                return
        jump menu_ben

    label ben_ask_kald_govt: 
        p "I was wondering about your opinion on the state of the kaldrean government."
        ben "[[canned response]"

        menu:
            ben "Is that along the lines of what you were looking for?"

            "Yes":
                p "Yes, thank you."
                $ plot_state.ben_kald_govt_info = InfoGet.FAIL
                $ last_dialog = "I'm glad I could help. Now is there anything else you need?" 

            "Say you were looking for more depth":
                p "Well, to be honest, I was looking for something more... in depth."
                ben "Ahh, I see."
                "Ben looks a bit nervous, and hesitates before continuing to speak."
                ben "Well, [alias.first], as I'm sure you understand, someone in a position such as mine must be very careful with
                what he says and to whom he says it. Especially in such tense times such as these."
                
                if plot_state.ben_trust <= TrustLevel.MEDIUM:
                    ben "Now, as you seem to have already figured out, my opinion on the kaldreans govern themselves is not exactly positive. And
                    I would gladly talk about it with someone whom I knew I could trust."
                    $ last_dialog = "Unfortunately, while I would like to trust you, we have only just met."
                    $ plot_state.ben_kald_govt_info = InfoGet.FAIL
                    # note: even though the above line sets ben_kald_govt_info to FAIL, the player can still succeed in getting the info
                    #   later if they do the Lida favor. It's just we need to set it to FAIL here so that it registers that the player
                    #   has talked to Ben when they go talk to Sarah
                else:
                    ben "On the other hand, you have shown yourself to be a reliable and competent person, so maybe I could share with you some of my 
                    less... popular opinions on the kaldrean governmental system."
                    p "I\'m listening."
                    ben "The kaldrean government on Qolisk is a tad... shall we say, controlling. Have you read Vel Kerriss\' \"Dystopia\"?"
                    p "I can\'t say that I have."
                    ben "It was a controversial kaldrean novel that made it past the government\'s censors and was widely read and lauded as one of the greatest works of literature to date.
                    It may remind you of Fahrenheit 451 by Ray Bradbury."
                    ben "Simply put: their government is controlling, [alias.first], but what they take away from their people they seem to 
                    give back in other ways."
                    ben "They have the highest standards of living I have ever seen, crime rates are low, there are no apparent problems."
                    p "But they are blissfully ignorant."
                    ben "You could say that, yes. I think that about covers their situation without distorting the truth."
                    $ last_dialog = "Is there anything else you would like to ask me?"
                    $ plot_state.ben_kald_govt_info = InfoGet.SUCCESS
                    $ plot_state.ben_talk_lida = False
        return

    label ben_ask_day:
        p "How has your day been, Ambassador?"
        ben "Quite frustrating, actually."
        p "May I ask why?"
        ben "Well, I urgently need to speak with Lida Ezekeri Skar, the kaldrean Senior Operations manager, but she has been actively avoiding
        all my attempts to meet with her."
        p "Any reason why you think she has been avoiding you? Or why she can in the first place?"

        menu:
            ben "As a kaldrean she is only obligated to respond to meeting requests with other kaldreans. On top of that, Ms. Ezekeri is an older woman who is
            set in her says, and has a certain... distaste for human politicians such as myself."

            "Okay":
                p "Well, that is quite unfortunate."
                
                $ last_dialog = "It certainly is. Is there anything else I can help you with?"
          
            "Offer to try to persuade her":
          
                p "Is it possible she would be more willing to listen to a newcomer such as myself?"
    
                ben "Hmmm... what a novel idea. Yes, why don't you try to persuade her? I would be most appreciative of the favor."

                ben "Now that I think of it, I'm confident you'll be able to persuade her to meet with me. You'll find Ms. Ezekeri in the kaldrean embassy.

                Tell her that I need to discuss the new trade regulations with her."

                p "Of course, but why exactly are you so confident in me? You only met me a few minutes ago."

                ben "I can just tell that you are going to have an impact here - perhaps you don\'t recognize it yet."

                p "I'll take your word for it."

                $ last_dialog = "Before you leave, is there anything else you'd like to ask?"
                $ plot_state.ben_talk_lida = True
        return

    label ben_mention_lida:
        ben "Have you spoken to Ms. Ezekeri in kaldrean embassy yet?"

        if plot_state.lida_convinced == InfoGet.NO_ATTEMPT:

            p "Sorry, I haven\'t done that yet."

            ben "Take your time. I will be awaiting news of your success."

        elif plot_state.lida_convinced == InfoGet.FAIL:

            p "I did talk to her but..."

            ben "Let me guess: she was too difficult."

            p "Unfortunately, yes."

            $ last_dialog = "Well, thank you for trying at any rate. Perhaps we\'ll talk about that information another time. Until then, is there anything else you would like to ask me?"

            $ plot_state.ben_kald_govt_info = InfoGet.FAIL

        elif plot_state.lida_convinced == InfoGet.SUCCESS:

            p "I did, and she has decided to meet with you."

            ben "That is wonderful news! I knew that you could pull this off, [alias.first]."

            ben "Ah yes, she has sent me a message accepting my latest request."

            ben "Thank you very much for your help, [alias.first]. I will remember your helpfulness."
            $ plot_state.ben_talk_lida = False
            $ plot_state.ben_trust = TrustLevel.HIGH
        return

    label ben_advice:
        p "What advice can you offer, from one diplomat to another?"

        ben "Ah yes, of course. What often happens to the greenhorns who arrive here from Earth and Qolisk alike, 
        is that they forget that they are entering an environment they have never before experienced. 
        You have to drop your prejudices and fabrications and simply observe. If you can\'t, then you struggle."
         
        p "I respect your advice, Ambassador –"
         
        ben "Call me Ben, please"
         
        p "I respect your advice, Ben, but doesn\'t it seem like a lot to ask of anyone to simply \"drop their prejudices?\""
         
        ben "Of course it is. It\'s completely unreasonable – everyone will remain with their judgment 
        tailored by their experiences. I never claimed it was possible simply become judgment-free. 
        That does not mean that you can\'t try. The closer you come to being spotless, the more those around you will accept you."
         
        ben "If only... (muttered)"
         
        p "What?"
         
        $ last_dialog = "Nevermind that! Anything else?" 
        return

    label ben_events:
        p "You probably know all about the rumors of racial tensions that have been circulating. Care to elaborate?"

        ben "Rumors are but rumors - they are innocuous little flies that eventually die down. No need to concern yourself with these 
        \"rumors\" my friend. I can assure that both Ambassador Irridiss and I are on quite even terms. 
        The peace that we maintain here is secure so there is really no need to worry."

        p "If you insist..."

        ben "I have no reason to be dishonest with you."

        p "No, I believe you. Thank you for the reassurance, Ben."

        $ last_dialog = "Not a problem, [alias.first]. Is there anything else you would like to know?"
        return

    label ben_Bg:
        p "Tell me about yourself"

        ben "There is not much to tell. I was born and raised here in this beautiful city and grew up inspired by the previous human and kaldrean ambassadors." 
        
        ben "After graduate school I went into politics and I suppose you know how that turned out."

        $ last_dialog = "Anything else I can help you with today?"
        return
