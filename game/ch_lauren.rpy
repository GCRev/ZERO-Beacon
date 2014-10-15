
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Lauren Gray

label ch_lauren:
    $ show_ch('lauren', 'right')
    if plot_state.lauren_met:
        $ last_dialog = 'Yes? Oh, it\'s you again.'        
    else:
        lauren "You must be the recent arrival. My director mentioned you. What was your name, [alias.last]? [alias.full]?"
        p "You got it."
        lauren "I\'m Lauren Gray, manager of logistics here."
        p "It\'s a pleasure to meet you."
        $ last_dialog = "Right. If you have anything you would like to ask, please be snappy."
        $ plot_state.lauren_met = True

    label menu_lauren:
        menu:
            lauren '[last_dialog]'
            'Ask Lauren what she is reading' if plot_state.stage == PlotStage.VL_INFO:
                jump lauren_info_tree_start
            ##'Ask Lauren about her background':
            ##    call lauren_background
            'Ask Lauren for advice':
                call lauren_advice
            'Ask Lauren about her opinion on recent events':
                call lauren_events
            'Done talking to Lauren':
                $ hide_ch('lauren', 'right')
                return
        jump menu_lauren

        label lauren_background:
            p 'So what can you tell me about your past?'
            lauren "I don't really have time for this chit-chat right now."
            $last_dialog = 'Please keep further inquiry to yourself.'
            return

        label lauren_advice:
            p "Excuse me... sorry, but would you be willing to offer me any advice as I start my work here?"
            lauren "..."             
            p "Ms. Gray?"
             
            lauren "I heard you, I just don\'t really have anything to say."
            lauren "Alright, I suppose I can offer a few words. I work with numbers all day long and I don\'t get out much so I\'m probably not the best person to ask."
            lauren "But after working here for a while I\'ve noticed a pattern, like a bell curve in a distribution graph – those who talk too
            much or too little are more or less shut away by society."
             
            p "Don\'t be too—"
             
            lauren "I wasn\'t done talking. Those who know just when and what to say make it very far very fast. It doesn\'t matter what your race may be, it\'s the same for everyone."
             
            p "So— actually, thank you for your advice. I\'ll let you get back to your work."

            $ last_dialog = 'Please keep further inquiry to yourself.'
            return

        label lauren_events:
            p "What is your opinion on this alleged racial tension within Concord?"

            lauren "Do you think that I am going to have a good answer for you?"

            p "I had hoped."

            lauren "Hah! About all I can tell you is that it is silly. I know plenty of kaldreans, none of whom are bothered or riled up by any of this so-called \"tension.\"" 
            
            lauren "I would almost think that you've been lied to about this, because honestly, I haven\'t noticed anything particularly out of the ordinary. And I work in upper-level management!"

            p "{size=-10}Yeah, but upper-level management has pulled the wool over your eyes.{/size}"

            lauren "What was that?"

            p "Don\'t worry about it. Thank you for your time. I\'ll let you get back to work."

            $last_dialog = "Alright. If you have anything else you want to say, please be brief." 
            return
        
        label lauren_info_tree_start:
            p "I am quite into literature myself. Might I ask what you are reading?"

            menu:
                lauren "This is a novel by a progressive kaldrean author. It's called {i}Through the Void{/i}."
                "Ask Lauren her opinion on progressives":
                    jump lauren_info_tree_progressives
                "Ask Lauren about the novel":
                    jump lauren_info_tree_novel

            label lauren_info_tree_progressives:
                p "A progressive author? What is your opinion on these progressive kaldreans?"

                lauren "I do think that the progressive movement is beneficial to the kaldrean people. Their government is so corrupt that it is really time for a change."

                lauren "I don't approve of how their government treats their people. It has me both angry and sorry at once - one of the few things that can actually make me emotional."

                p "It must be worse than I've been told."

                lauren "They don't tell us anything."

                p "Thank you for answering my question."

                $last_dialog = "Please keep further inquiry to yourself."
                jump menu_lauren

            label lauren_info_tree_novel:
                p "That must be a recent novel, because I haven't heard of it. Can you tell me about it?"

                lauren "It's not normally a genre I read, I prefer more philosophical works, but this was so highly recommended that I had to pick up a copy."

                lauren "It is based off a true story of a kaldrean and a human who entered into a relationship during the first contact conflict."

                lauren "It raises a lot of questions about what makes us human and what makes them kaldrean. The author smartly decided to focus on themes rather than details."
                menu:
                    lauren "It reminds me of someone I grew up with - Nidaria. I imagine this novel does a pretty good job portraying her family's situation."
                    "Show sympathy":
                        jump lauren_info_tree_sympathize
                    "Show disapproval":
                        jump lauren_info_tree_disapproval

                label lauren_info_tree_sympathize:
                    p "I feel sorry for those humans and kaldreans who have to face that kind of oppression. It seems like an unnecessary barrier."

                    lauren "Lorisk would certainly know about that. She was always picked on at school by the kaldreans especially, who did not approve of her human mother and kaldrean father."

                    lauren "And on top of that she was adopted, which did not sit well with the humans. She really did not deserve that kind of treatment."

                    p "I'm sorry to hear that."

                    $ plot_state.lauren_lorisk_info = InfoGet.SUCCESS
                    $last_dialog = "Right. Well, that doesn't change the fact that it happened. I got sidetracked; if you have any other questions, keep them brief."
                    jump menu_lauren

                label lauren_info_tree_disapproval:
                    p "I don't think that kaldreans and humans should have that kind of relationship."

                    lauren "That's narrow-minded of you, [alias.title_full]. I honestly would not have expected that kind of response from you. Or at least you would have kept it to yourself."

                    $ plot_state.lauren_lorisk_info = InfoGet.FAIL
                    $last_dialog = "If you have something open-minded to say, then you can ask me. Otherwise, I would prefer it if I could get back to my break."
                    jump menu_lauren
