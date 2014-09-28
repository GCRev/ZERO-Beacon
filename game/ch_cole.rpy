
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Cole DeMarc

label ch_cole:
    show cole at char_pos
    if plot_state.cole_met:
    	$ last_dialog = '[[introduction]'
    	adam '[last_dialog]'

    else:
    	cole '[Cold intro, who are you?]'
    	p '[[introduce self]'
        cole '[[that\'s nice, what do you want?]'
        p 'what can you tell me about your past?'
        $last_dialog '[cold response]'
   		cole '[last_dialog]'

    	$ plot_state.cole_met = true

    label menu_cole
    	menu:
    		adam '[last_dialog]'
    		'[[pursue]'
                call cole_pursue
            '[[apologize for prying]'
                call cole_apologize
        jump menu_cole        

    label cole_pursue:
        p '[[pursue]'       
        cole '[[Get out bro]'
        $cole_background_info = InfoGet.FAIL
        return

    label cole_apologize
        p '[[apologizes for prying]'
        cole '[[It\'s cool bro]'
        menu:
            cole '[[what do you want to know?]'
            '[[pursue again]'
            call cole_mad
            '[[offer confidentiallity]'
            call cole_offer_background

        label cole_mad
            p '[[pursue again]'
            cole '[[get out]'
            $cole_background_info = InfoGet.FAIL
            return

        label cole_offer_background
            p '[[offer confidentiallity]'        
            cole '[[offers background gains trust]'
            $cole_background_info = InfoGet.SUCCESS
            return