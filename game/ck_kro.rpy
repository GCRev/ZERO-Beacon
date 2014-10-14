
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Kro Zalva Ross

label ck_kro:
    show kro at char_pos
    if plot_state.kro_met:
        $ last_dialog = "Greetings, " + alias.title_last + "."
        kro '[last_dialog]'

    else:
        kro "Salutations. I am Flight Commander Kro Zalva. Welcome to Vivarioss."

        p "Nice to meet you Commander, I\'m [alias.full]."

        $last_dialog = "Likewise. Now, if there is anything you would like to know, please ask. Else move on."
        $plot_state.kro_met = True
        kro '[last_dialog]'

    label menu_kro:
        menu:
            kro '[last_dialog]'
            'Jon sent me' if plot_state.jon_talk_kro and plot_state.stage == PlotStage.VL_INFO:
                jump kro_jon_tree_start
            ##'Flatter Kro' if plot_state.stage == PlotStage.VL_INFO:
            ##    call kro_flatter
            'Ask Kro for advice':
                call kro_advice
            'Ask Kro on her opinions on recent events':
                call kro_events
            'Ask Kro about her background':
                call kro_background
            'Ask Kro about Valak Lideri' if plot_state.stage == PlotStage.VL_PLANS:
                call kro_VL_tree_start
            'Done talking to Kro':
                hide kro
                return
        jump menu_kro

        label kro_flatter:
            p '[[your ship is so big.]'
            kro '[[slightly amused. Thanks you for your attempt. Schools you a bit on Kaldrean culture and flattery.]'
            $last_dialog = '[Keep the sweet-talk to a minimum.]'
            $plot_state.kro_flatter_info = True
            return

        label kro_advice:
            p "Could you offer any advice to someone new to Concord?"

            kro "I will tell you what I have told others before you, and what I was told early on in my training: By choosing to come here you have agreed to change yourself." 
            kro "You will be judged by a new set of rules and regulations, and who you become will be no one like who you left behind."

            p "That seems a little intense."

            kro "It is quite true. I recognize it in myself and those close to me."

            p "And how does that affect you?"

            kro "I have yet to understand."

            p "Well... thank you for your words of advice."

            $last_dialog = 'Is there anything else I can help you with?'
            return

        label kro_events:
            p "Have you heard about this so-called tension between the humans and kaldreans here?"

            kro "I do not spend too much of my operational time actually on Concord, I am simply here for the remainder of the week 
            as my starship receives routine maintenance." 
            kro "You are likely much better informed that I am on these matters."

            p "You\'re probably right."

            kro "Just ask around, if you have heard of these \"rumors\" then I am sure others have come into contact with the same fleeting words."
            kro "If you have not already talked to Elder Volk in the Grand Marketplace then I recommend you do so. If not then perhaps Elder Demeter in the residences."

            p "Thanks for the direction."

            $last_dialog =  "No need to thank me. Do you have any other questions?"
            return

        label kro_background:
            p "Could you tell me about yourself Commander? How did you gain your rank?"
            kro "I was born on Qolisk to a family of high political standing - surprisingly so."

            kro "The Ross clan is put off for its support of the progressives, so it becomes increasingly difficult to work our way up the social ladder to high-ranking positions."

            kro "Still, concrete results and hard numbers easily best a silly viewpoint. I was able to prove my worth and even surprise my conservative superiors."

            kro "Eventually I could outdo even the best of them."

            p "What do you do as a Flight Commander?"

            kro "I do exactly what my title dictates - I keep operational order over the flight crew on my ship, the KAU Voidrunner {i}Triekri{/i}."

            kro "If something is not running smoothly I am responsible to see that the problem is solved."

            $last_dialog = "Is there anything else I can help you with?"
            return

        label kro_jon_tree_start:
            p "I was talking with Jon and he referred me to you. I think that seems like a good idea."

            kro "Officer Caise, yes. He is quite diligent. Whenever we dock for maintenance he makes sure everything on his end runs smoothly."

            kro "However, I have noted from conversations with him that he is quite obsessed with weaponry. It worries me."
            $plot_state.jon_hobby_info = InfoGet.SUCCESS

            p "The obsession or specifically the weaponry?"

            menu:
                kro "The obsession. What did you and Officer Caise discuss that prompted a referral to me?"
                "Ask Kro about Valak Lideri":
                    jump kro_jon_tree_VL
                "Ask why obsession worries Kro":
                    jump kro_jon_tree_obsession

            label kro_jon_tree_VL:
                p "I had asked Jon about Valak Lideri and he sent me to talk to you - he said you might know more about them."
                
                kro "I am familiar with the group, but unfortunately the extent of my knowledge does not continue beyond just that."

                kro "So I apologize. Perhaps you should find a linguist or an Elder - \"Valak Lideri\" sounds like a phrase from a traditional dialect."

                p "Thank you for your help, Commander."

                $last_dialog = "If there is anything you need, I am at your service, "+ alias.title_last
                $plot_state.kro_obsession_info = InfoGet.FAIL
                jump menu_kro

            label kro_jon_tree_obsession:
                p "You said obsession worries you. Why is that?"

                kro "Throughout my career I have encountered a wide spectrum of both humans and kaldreans. Those with obsessions have usually caused me trouble."

                kro "That does not apply to everyone, for instance Officer Caise is very restrained and very professional about his obsessive hobby."

                kro "However, the troubled individuals with darker compulsions are obsessed because they are burying information where the hope no one can find it."

                kro "They can become reckless or paranoid, and then they begin to propagate disorder."

                p "Interesting. Thank you for the insight, Commander."
                $last_dialog = "If there is anything you need, I am at your service, "+ alias.title_last
                $plot_state.kro_obsession_info = InfoGet.SUCCESS
                jump menu_kro

        label kro_VL_tree_start:
            p "What can you tell me about Valak Lideri?"

            menu:
                kro "We may or may not have had this discussion already, but I am not as familiar with this group I assume you expect me to be."
                "Ask Kro what she thinks of the group":
                    jump kro_VL_tree_idea
                "Ask Kro who she thinks could be involved":
                    jump kro_VL_tree_who

            label kro_VL_tree_idea:
                p "I just need an idea of what this group might be."

                lorisk "Clearly they are a rebel group with an obsession for change. I fear that they are going to lose sight of their pursuit, however, and turn their revolution in to bloodbath."

                lorisk "If they find assassination a proper method to make their statements, they are likely to overlook the fallout it would cause."

                $last_dialog = "Take care what you say, not all will be so willing to speak on sensitive matters. If you require anything further, "+ alias.title_full + ", Let me know."
                jump menu_kro


            label kro_VL_tree_who:
                p "In your expert opinion, who do you think could be involved with this group?"

                kro "I would prefer not to make enemies out my acquaintances."

                p "I won't go around telling everyone what it you've said. I don't see the point to that."

                kro "Well, I suppose if I could make any guesses it Mr. Demarc, Mr. Kriesk, and Ms. Nidaria."

                kro "Mr. Demarc underwent some profound changes and suffered substantial losses during the first contact conflict, he is troubled as a result."

                kro "Mr. Kriesk has a deep-seated hatred from our military, despite the praise he received for his prowess with a ranged linear rifle."

                kro "Ms. Nidaria has a generally progressive and sympathetic attitude. I could easily see her involved with Valak Lideri."
                
                $last_dialog = "Take care what you say, not all will be so willing to speak on sensitive matters. If you require anything further, " + alias.title_full + ", Let me know."
                jump menu_kro

            
            