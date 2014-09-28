
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Dialog for Benjamin Columbus

label ch_ben:
    show ben at char_pos
    if plot_state.ben_met:
        $ last_dialog = ‘Greetings, $ALIAS_FIRST_NAME.’
        ben ‘[last_dialog]’

    else:
        ben ‘Hello there, I don\’t believe we’ve met. I\’m Benjamin Columbus, Ambassador of the humans, but you can just call me Benjamin Columubus. And you are?’
        p ‘$ALIAS_FIRST_NAME’
        ben ‘Ah, yes. Welcome to Concord. What can I do for you today?’
	p ‘Sarah has informed me about some mysterious underground information, care to elaborate?’
        ben ‘[[sends player to Lida, see if you can earn her trust?]’
        
    hide ben

label ch_lida:
    show lida at char_pos
    
    lida ‘[[introduction, now what do you want?]’
    p ‘[[meet with ben dammit]’
    linda ‘[[convince me or I won\’t]’

    label menu_lida
        menu:
            lida ‘[[same convince me or I won\’t line]’
            ‘[[intimidate]’
                call lida_intimidate
            ‘[[flatter]’
                call lida_flatter
        jump menu_lida

    label lida_intimidate
        lida ‘[[you didn\’t convince me]’
    hide lida

    show ben at char_pos

    ben ‘[[Sorry, you screwed that up. no info for you]’
    $ben_kald-govt-info = InfoGet.Fail

    jump menu_lida

    label lida_flatter
        lida ‘[[you convinced me… very nice]’
    hide lida
    show ben at char_pos
    ben ‘[[Good job, here is my information on the Kaldrean Government. Blah blah blah]’
    $ben_kald-govt-info = InfoGet.Success


    hide ben
    return
