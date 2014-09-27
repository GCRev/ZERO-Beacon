
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman
# Main script file

label start:
    call intro
    jump loc_port


####################################################
#############        Python Code       #############
####################################################

init -2 python:

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

    PlotStage = enum('ARRIVE', 'KALD_GOVT_INFO', 'VL_INFO', 'VATRISK_MEET', 'VL_PLANS')
    InfoGet = enum('NO_ATTEMPT', 'FAIL', 'SUCCESS')


    class PlotState:
        
        stage = PlotStage.ARRIVE
        high_emb_tried_bribe = False
        
    #Adam's flags
        adam_met = False
        adam_talk_alkay = False
        adam_alkay_info = InfoGet.NO_ATTEMPT
        adam_vl_info = InfoGet.NO_ATTEMPT

    #Alkay's flags
        alkay_met = False
        alkay_talk_adam = False
        alkay_adam_info = InfoGet.NO_ATTEMPT
        alkay_vl_info = InfoGet.NO_ATTEMPT

    #Ben's flags
        ben_met = False
        ben_kald_govt_info = InfoGet.NO_ATTEMPT

    #Cole's flags
        cole_met = False
        cole_background_info = InfoGet.NO_ATTEMPT

    #Jon's flags
        jon_met = False
        jon_vl_info = InfoGet.NO_ATTEMPT

    #Kro's flags
        kro_met = False
        kro_obsession_info = InfoGet.NO_ATTEMPT
        kro_flatter_info = InfoGet.NO_ATTEMPT

    #Lauren's flags
        lauren_met = False
        lauren_lorsk_info = InfoGet.NO_ATTEMPT

    #Lida's flags
        lida_met = False

    #Lorisk's flags
        lorisk_met = False
        lorisk_flatter = False
        lorisk_vl_info = InfoGet.NO_ATTEMPT

    #Noq's flags
        noq_met = False
        noq_refuse_dialog = False
        noq_illegal_info = False

    #Sarah's flags

    #Vatrisk's flags
        vatrisk_met = False
        vatrisk_kald_govt_info = InfoGet.NO_ATTEMPT



####################################################
#############     Global Variables     #############
####################################################

# Non-characters
define char_pos = Position(xpos = 0.8, xanchor = 'right', ypos = config.screen_height - 150)
define plot_state = PlotState()

# Non-pictured characters
define p = Character('You')
define comm = Character('Commander')
define guard = Character('Embassy Guard')

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

image bg bridge = png('bg_map')
image bg map = png('bg_map')
image bg landing_pad = png('bg_landing-pad')
image bg result1 = png('result_1-inaction')
image bg result2 = png('result_2-apprehend')
image bg result3 = png('result_3-assist')
image bg result4 = png('result_4-dipolomacy')


####################################################
###############      Locations       ###############
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

label loc_market:
    scene bg market
    'You are at the Grand Marketplace. [[describe]'
    label market_menu:
        menu:
            'Talk to Cole Demarc':
                call ch_cole
            'Talk to Alkay Volk Kladir':
                call ck_alkay
            '(Back to Map)':
                jump map_screen
    jump market_menu

label loc_high_emb:
    scene bg high_emb
    'You are at the High Embassy. [[describe]'
    label menu_high_emb:
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
                        '[[lie that you have appt]':
                            guard '[[don\'t see you on appt list]'
                            jump high_emb_guard_menu
                        '[[try to bribe]':
                            guard '[[offended; tells you to screw off]'
                            $ plot_state.high_emb_tried_bribe = True
                            jump map_screen
        else:
            menu:
                'Talk to Benjamin Columbus':
                    call ch_ben
                'Talk to Vatrisk Irridiss Kier':
                    call ck_vatrisk
                '(Back to Map)':
                    jump map_screen
    jump menu_high_emb

label loc_human_emb:
    scene bg human_emb
    'You are at the Human Embassy. [[describe]'
    label menu_human_emb:
        menu:
            'Talk to Lauren Gray':
                call ch_lauren
            '(Back to Map)':
                jump map_screen
    jump menu_human_emb
    
label loc_kald_emb:
    scene bg kald_emb
    'You are at the Kaldrean Embassy. [[describe]'
    label menu_kald_emb:
        menu:
            'Talk to Lorisk Nidaria Kol':
                call ck_lorisk
            'Talk to Lida Ezekeri Skar':
                call ck_lida
            '(Back to Map)':
                jump map_screen
    jump menu_kald_emb
    
label loc_res: 
    scene bg res
    'You are at the Residences. [[describe]'
    label menu_res:
        menu:
            'Talk to Sarah Liu':
                call ch_sarah
            'Talk to Adam Demeter':
                call ch_adam
            'Talk to Noq Kriesk Lask':
                call ck_noq
            '(Back to Map)':
                jump map_screen
    jump menu_res
    
label loc_port:
    scene bg port
    'You are at the Spaceport. [[describe]'
    label menu_port:
        menu:
            'Talk to Jonathan Caise':
                call ch_jon
            'Talk to Kro Zalva Ross':
                call ck_kro
            '(Back to Map)':
                jump map_screen
    jump menu_port
       