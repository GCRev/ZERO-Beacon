
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Benjamin Columbus

label ch_ben:
    show ben at char_pos
    if plot_state.ben_met:
        if plot_state.ben_talk_lida:
            ben "Good to see you again, [alias.first]. Have you spoken with Miss Ezekeri yet?"
            if plot_state.lida_convinced == InfoGet.NO_ATTEMPT:
                p "Sorry, I haven\’t done that yet."
                ben "Take your time. I will be awaiting news of your success."
                hide ben
                return
            elif plot_state.lida_convinced == InfoGet.FAIL:
                p "I did talk to her but…"
                ben "Let me guess, she was too difficult."
                p "Unfortunately, yes."
                ben "Well, thank you for trying at any rate. Perhaps we\’ll talk about that information another time. 
                Until then, is there anything else you would like to ask me?"
                $plot_state.ben_kald_govt_info = InfoGet.FAIL
                $plot_state.ben_talk_lida = False
                hide ben
                return

            else:
                p '[[She will meet with you.]'
                ben '[[Wonderful. Ben gives you the infos.]'
                ben '[[You can come back and talk any time.]'
                $plot_state.ben_kald_govt_info = InfoGet.SUCCESS
                $plot_state.ben_talk_lida = False
                hide ben
                return

        else:
            $ last_dialog = 'How may I be of service ' + alias.first + '?'
            ben '[last_dialog]'
            jump menu_ben

    else:
        ben "I was told we were going to have a new team-member. You must be [alias.first]."
        p "That is me."
        ben "Wonderful. I\’m, as you might already know, Ambassador Columbus. But please, just call me Ben. I hope that your time on Concord thus far has been pleasant."
        p "I\t’s a beautiful city."
        ben "It certainly is. Now, everyone has a reason to end up here, what can I do for you today?"
        p "Actually, I need some information on the state of the kaldrean government so that I can better understand the political climate."
        ben "I see. Well, if we are talking favors I\’ll cut you a deal -  I have been trying to meet with the Senior Operations manager for some time now, 
        but she will only respond to the kaldrean Ambassador\’s requests. If you can convince her to meet up with me, then we can talk."
        p "Any reason why you think she has been avoiding you? Or why she can in the first place?"
        ben "As a kaldrean she is only obligated to respond to meeting requests with other kaldreans. On top of that she is an older woman who has a certain… disdain for humans. 
        However, she is partial to new faces and I am confident that you can pull this off. So… do we have a deal?"
        p "Of course, but why exactly are you so confident in me? You only met me a few minutes ago."
        ben "I can just tell that you are going to have an impact here - perhaps you don\’t recognize it yet."
        p "I’ll take your word for it. It was nice to meet you, Ben."
        $last_dialog = "Likewise, " + alias.first + "."
        $plot_state.ben_met = True
        $plot_state.ben_talk_lida = True
        ben '[last_dialog]'
        hide ben
        return

    label menu_ben:
        menu:
            ben '[last_dialog]'
            '[[ask for advice from Ben]':
                call ben_advice
            '[[ask Ben his opinions on recent events]':
                call ben_events
            '[[ask Ben about his background]':
                call ben_background
            '[[done talking to Ben]':
                hide ben
                return
        jump menu_ben

        label ben_advice:
            p "What advice can you offer, from one diplomat to another?"
 
            ben "Ah yes, of course. What often happens to the greenhorns who arrive here from Earth and Qolisk alike, 
            is that they forget that they are entering an environment they have never before experienced. 
            You have to drop your prejudices and fabrications and simply observe. If you can\’t, then you struggle."
             
            p "I respect your advice, Ambassador –"
             
            ben "Call me Ben, please"
             
            p "ben, but doesn\’t it seem like a lot to ask of anyone to simply, \‘drop their prejudices?\’"
             
            ben "Of course it is. It\’s completely unreasonable – everyone will remain with their judgment 
            tailored by their experiences. I never claimed it was possible simply, up and become judgment-free. 
            That does not mean that you can\’t try. The closer you come to being spotless, the more those around you will accept you."
             
            ben "if only… (muttered)"
             
            p "What?"
             
            ben "Nevermind then! Anything else?" 
            return

        label ben_events:
            p "You probably know all about the rumors of racial tensions that have been circulating. Care to elaborate?"

            ben "Rumors are but rumors - they are innocuous little flies that eventually die down. No need to concern yourself with these 
            \“rumors\” my friend. I can assure that both I and my colleague, Ambassador Irridiss are on quite even terms. 
            The peace that we maintain here is secure so there is really no need to worry."

            p "If you insist…"

            ben "I have no reason to be dishonest with you."

            p "No, I believe you. Thank you for the reassurance, Ben."

            Ben "Not a problem, [alias.first]. Is there anything else you would like to know?"
            return

        label ben_background:
            p '[[you ask Ben on his background]'
            ben '[[offers little information. Sounds canned to you.]'
            return