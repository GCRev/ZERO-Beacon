
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman

label start:
    jump intro


####################################################
#############        Python Code       #############
####################################################

init python:

    # png : string -> Image
    # Helper function for loading & scaling our background and character images
    def png(fname):
        return im.FactorScale('assets/' + fname + '.png', config.screen_width / 1600.0)

    # enum : string ... -> type
    # Creates an enumerated type from a list of strings. Used to add support for
    #   simple enumerated types.
    def enum(*values):
        enums = dict(zip(values, range(len(values))))
        return type('Enum', (), enums)

    PlotStage = enum('ARRIVE', 'KALD_GOVT_INFO', 'VL_INFO', 'VATRISK_MEET', 'VL_PLANS', 'CONCLUSION')

    class PlotState(object):
        stage = PlotStage.ARRIVE
        high_emb_tried_bribe = False

define plot_state = PlotState()


####################################################
###############    Character Defs    ###############
####################################################

define p = Character('You')

# Humans
define ben = Character('Benjamin Columbus')
define cole = Character('Cole Demarc')
define jon = Character('Jonathan Caise')
define lauren = Character('Lauren Gray')
define adam = Character('Adam Demeter')
define sarah = Character('Sarah Liu')

# Kaldreans
define vatrisk = Character('Vatrisk Irridiss Kier')
define alkay = Character('Alkay Volk Kladir')
define lorisk = Character('Lorisk Nidaria Kol')
define kro = Character('Kro Zalva Ross')
define noq = Character('Noq Kriesk Lask')
define lida = Character('Lida Ezekeri Skar')

# Non-pictured 
define comm = Character('Commander')
define guard = Character('Embassy Guard')


####################################################
###############        Images        ###############
####################################################

image ben = png('ch_ben')
image cole = png('ch_cole')
image jon = png('ch_jon') 
image lauren = png('ch_lauren')
image adam = png('ch_adam')
image sarah = png('ch_sarah')

image vatrisk = png('ck_vatrisk')
image alkay = png('ck_alkay') 
image lorisk = png('ck_lorisk') 
image kro = png('ck_kro') 
image noq = png('ck_noq')
image lida = png('ck_lida')

image bg market = png('bg_market')
image bg high_emb = png('bg_high-emb')
image bg human_emb = png('bg_human-emb')
image bg kald_emb = png('bg_kald-emb')
image bg res = png('bg_res')
image bg port = png('bg_port')

image bg map = png('bg_map')
image bg landing_pad = png('bg_landing-pad')
image bg result1 = png('result_1-inaction')
image bg result2 = png('result_2-apprehend')
image bg result3 = png('result_3-assist')
image bg result4 = png('result_4-dipolomacy')

define char_pos = Position(xpos = 0.7, xanchor = 'right', ypos = config.screen_height - 122)


####################################################
###############      Locations       ###############
####################################################
        
label loc_market:
    scene bg market
    'You are at the Grand Marketplace. (describe)'
label loc_market_return:
    menu:
        'Talk to Cole Demarc':
            jump ch_cole
        'Talk to Alkay Volk Kladir':
            jump ck_alkay
        '(Back to Map)':
            jump map_screen

label loc_high_emb:
    scene bg high_emb
    'You are at the High Embassy. (describe)'
label loc_high_emb_return:
    if plot_state.stage == PlotStage.ARRIVE:
        if plot_state.high_emb_tried_bribe:
            guard 'Haven\'t we already talked to you? Unless you have official business here, you may not enter the high embassy.'
            jump map_screen
        else:
            guard 'Hi. What business do you have here?'
            label high_emb_guard_menu:
                menu:
                    'None, actually. I\'ll be on my way.':
                        jump map_screen
                    '(lie that you have appt)':
                        guard '(don\'t see you on appt list)'
                        jump high_emb_guard_menu
                    '(try to bribe)':
                        guard '(offended; tells you to screw off)'
                        $ plot_state.high_emb_tried_bribe = True
                        jump map_screen
    else:
        menu:
            'Talk to Benjamin Columbus':
                jump ch_ben
            'Talk to Vatrisk Irridiss Kier':
                jump ck_vatrisk
            '(Back to Map)':
                jump map_screen
    
label loc_human_emb:
    scene bg human_emb
    'You are at the Human Embassy. (describe)'
label loc_human_emb_return:
    menu:
        'Talk to Lauren Gray':
            jump ch_lauren
        '(Back to Map)':
            jump map_screen
    jump map_screen
    
label loc_kald_emb:
    scene bg kald_emb
    'You are at the Kaldrean Embassy. (describe)'
label loc_kald_emb_return:
    menu:
        'Talk to Lorisk Nidaria Kol':
            jump ck_lorisk
        'Talk to Lida Ezekeri Skar':
            jump ck_lida
        '(Back to Map)':
            jump map_screen
    jump map_screen
    
label loc_res: 
    scene bg res
    'You are at the Residences. (describe)'
label loc_res_return: 
    menu:
        'Talk to Sarah Liu':
            jump ch_sarah
        'Talk to Adam Demeter':
            jump ch_adam
        'Talk to Noq Kriesk Lask':
            jump ck_noq
        '(Back to Map)':
            jump map_screen
    jump map_screen
    
label loc_port:
    scene bg port
    'You are at the Spaceport. (describe)'
label loc_port_return:
    menu:
        'Talk to Jonathan Caise':
            jump ch_jon
        'Talk to Kro Zalva Ross':
            jump ck_kro
        '(Back to Map)':
            jump map_screen
    jump map_screen
        

####################################################
#############     Menus / Cutscenes    #############
####################################################

label map_screen:
    scene bg map
    menu:
        '1. High Embassy':
            jump loc_high_emb
        '2. Human Embassy':
            jump loc_human_emb
        '3. Kaldrean Embassy':
            jump loc_kald_emb
        '4. Residences':
            jump loc_res
        '5. Grand Marketplace':
            jump loc_market
        '6. Spaceport':
            jump loc_port

label intro:
    scene black
    'blah blah blah narration'
    comm 'blah blah blah more narration'
    jump loc_port


####################################################
#############     Character Dialog     #############
####################################################

label ch_ben:
    show ben at char_pos
    '(blah blah blah)'
    hide ben
    jump loc_high_emb_return

label ch_cole:
    show cole at char_pos
    '(blah blah blah)'
    hide cole
    jump loc_market_return

label ch_jon:
    show jon at char_pos
    '(blah blah blah)'
    hide jon
    jump loc_port_return

label ch_lauren:
    show lauren at char_pos
    '(blah blah blah)'
    hide lauren
    jump loc_human_emb_return

label ch_adam:
    show adam at char_pos
    '(blah blah blah)'
    hide adam
    jump loc_res_return

label ch_sarah:
    show sarah at char_pos
    '(blah blah blah)'
    hide sarah
    jump loc_res_return    

label ck_vatrisk:
    show vatrisk at char_pos
    '(blah blah blah)'
    hide vatrisk
    jump loc_high_emb_return

label ck_kro:
    show kro at char_pos
    '(blah blah blah)'
    hide kro
    jump loc_port_return
    
label ck_alkay:
    show alkay at char_pos
    '(blah blah blah)'
    hide alkay
    jump loc_market_return
    
label ck_noq:
    show noq at char_pos
    '(blah blah blah)'
    hide noq
    jump loc_res_return
    
label ck_lorisk:
    show lori at char_pos
    '(blah blah blah)'
    hide lorisk
    jump loc_kald_emb_return
    
label ck_lida:
    show lida at char_pos
    '(blah blah blah)'
    hide lida
    jump loc_kald_emb_return
