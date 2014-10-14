
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# Main script file

label start:
    $ plot_state = PlotState() # necessary to initialize this here, because it signals Ren'Py to save plot_state
    call tests
    if debug_skip_intro and config.developer:
        $ alias = Alias(Gender.NEUT, 'Dev', 'Eloper')
    else:
        call intro

    $ plot_state.set_stage(debug_init_stage if config.developer else PlotState.ARRIVE)

    if debug_skip_intro and config.developer:
        jump loc_port
    else:
        jump loc_port_no_fade


####################################################
#############        Python Code       #############
####################################################

init -2 python:

    # char_img : string -> Image
    # Helper function for loading & scaling our character images
    def char_img(fname):
        return im.FactorScale('assets/' + fname + '.png', config.screen_width / 1350.0)
 
    # bkg_img : string -> Image
    # Helper function for loading & scaling our background images
    def bkg_img(fname):
        return im.Scale('assets/' + fname + '.png', config.screen_width, config.screen_height)

    # show_ch : Image, string -> void
    def show_ch(img, direction):
        trans = None
        if direction == 'left':
            trans = moveinleft
        elif direction == 'right':
            trans = moveinright
        else:
            raise ValueError("invalid direction: " + direction)
        renpy.show('text_frame')
        renpy.with_statement(None)
        renpy.show(img, at_list=[char_pos])
        renpy.with_statement(trans)
        renpy.hide('text_frame')

    # hide_ch : string, string -> void
    def hide_ch(char_name, direction):
        trans = None
        if direction == 'left':
            trans = moveoutleft
        elif direction == 'right':
            trans = moveoutright
        else:
            raise ValueError("invalid direction: " + direction)
        renpy.show('text_frame')
        renpy.with_statement(None)
        renpy.hide(char_name)
        renpy.with_statement(trans)
        renpy.hide('text_frame')

    # enum : string ... -> type
    # Creates an enumerated type from a list of strings. Used to add support for
    #   simple enumerated types.
    def enum(*values):
        enums = dict(zip(values, range(len(values))))
        return type('Enum', (), enums)

    PlotStage = enum('INTRO', 'ARRIVE', 'KALD_GOVT_INFO', 'VL_INFO', 'VATRISK_MEET', 'ATTACK_JUST_HAPPENED', 'VL_PLANS', "GAME_OVER")
    InfoGet = enum('NO_ATTEMPT', 'FAIL', 'SUCCESS')
    TrustLevel = enum('LOW', 'MEDIUM', 'HIGH', 'VERY_HIGH')

    class PlotState:
        
        def set_stage(self, stage):
            self.stage = stage
            obj = None
            if stage == PlotStage.INTRO:
                obj = None
            elif stage == PlotStage.ARRIVE:
                obj = "Speak with Sarah Liu in the Residences."
            elif stage == PlotStage.KALD_GOVT_INFO:
                obj = "Ask the high ambassadors about the kaldrean government; then, return to Sarah."
            elif stage == PlotStage.VL_INFO:
                obj = "Gather information about the Valak Lideri; then, return to Sarah."
            elif stage == PlotStage.VATRISK_MEET:
                obj = "Meet with Ambassador Irridiss in the High Embassy; then, return to Sarah."
            elif stage == PlotStage.ATTACK_JUST_HAPPENED:
                obj = None
            elif stage == PlotStage.VL_PLANS:
                obj = "Try to uncover the rebels' plans and/or identities; then, return to Sarah."
            elif stage == PlotStage.GAME_OVER:
                obj = None
            else:
                raise ValueError("invalid stage: " + str(stage))
            if obj is None:
                renpy.hide_screen('objective')
            else:
                renpy.show_screen('objective', obj)

        stage = PlotStage.INTRO
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
        alkay_vl_plan_info = InfoGet.NO_ATTEMPT

    #Ben's flags
        ben_met = False
        ben_kald_govt_info = InfoGet.NO_ATTEMPT
        ben_talk_lida = False
        ben_trust = TrustLevel.MEDIUM

    #Cole's flags
        cole_met = False
        cole_background_info = InfoGet.NO_ATTEMPT

    #Jon's flags
        jon_met = False
        jon_vl_info = InfoGet.NO_ATTEMPT
        jon_talk_kro = False
        jon_vl_plan_info = InfoGet.NO_ATTEMPT
        jon_hobby_info = InfoGet.NO_ATTEMPT

    #Kro's flags
        kro_met = False
        kro_obsession_info = InfoGet.NO_ATTEMPT
        kro_flatter_info = InfoGet.NO_ATTEMPT

    #Lauren's flags
        lauren_met = False
        lauren_lorisk_info = InfoGet.NO_ATTEMPT

    #Lida's flags
        lida_met = False
        lida_convinced = InfoGet.NO_ATTEMPT

    #Lorisk's flags
        lorisk_met = False
        lorisk_flatter = False
        lorisk_flatter_offend = False
        lorisk_vl_info = InfoGet.NO_ATTEMPT
        lorisk_vl_plan_info = InfoGet.NO_ATTEMPT

    #Noq's flags
        noq_met = False
        noq_refuse_dialog = False
        noq_vl_plan_info = InfoGet.NO_ATTEMPT

    #Sarah's flags

    #Vatrisk's flags
        vatrisk_met = False
        vatrisk_kald_govt_info = InfoGet.NO_ATTEMPT
        vatrisk_trust = TrustLevel.MEDIUM

    def gend_to_str(gender):
        if gender == Gender.FEM:
            return "Feminine"
        elif gender == Gender.MASC:
            return "Masculine"
        elif gender == Gender.NEUT:
            return "Neutral"
        else:
            raise ValueError('illegal value of gender')

    Gender = enum('FEM', 'MASC', 'NEUT')
    class Alias:
        def __init__(self, gender, first, last):
            self.gender = gender
            if self.gender == Gender.FEM:
                self.title = 'Ms.'
                self.address = "ma'am"
            elif self.gender == Gender.MASC:
                self.title = 'Mr.'
                self.address = 'sir'
            elif self.gender == Gender.NEUT:
                self.title = 'Mx.'
                self.address = 'ser'
            else:
                raise ValueError('illegal value of gender')
            self.first = first
            self.last = last
            self.full = first + ' ' + last
            self.title_full = self.title + ' ' + self.full
            self.title_last = self.title + ' ' + self.last



####################################################
#############     Global Variables     #############
####################################################

# Non-characters
define plot_state = None
define debug_init_stage = None
define debug_skip_intro = False 
define alias = None
define char_pos = Position(xpos=0.8, xanchor='right', ypos=config.screen_height-150)    

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

image ben = char_img('ch_ben')
image cole = char_img('ch_cole')
image jon = char_img('ch_jon') 
image lauren = char_img('ch_lauren')
image adam = char_img('ch_adam')
image sarah = char_img('ch_sarah')

image vatrisk = char_img('ck_vatrisk')
image alkay = char_img('ck_alkay') 
image lorisk = char_img('ck_lorisk') 
image kro = char_img('ck_kro') 
image noq = char_img('ck_noq')
image lida = char_img('ck_lida')

image bg market = bkg_img('bg_market')
image bg high_emb = bkg_img('bg_high-emb')
image bg human_emb = bkg_img('bg_human-emb')
image bg kald_emb = bkg_img('bg_kald-emb')
image bg res = bkg_img('bg_res')
image bg port = bkg_img('bg_port')

image planet_bridge = im.Scale('assets/bg_bridge.png', config.screen_width / 2.0, config.screen_width / 2.0)
image text_frame = im.Scale('assets/ui_text-frame.png', config.screen_width, style.window.yminimum)

image bg stars = bkg_img('bg_stars')
image bg map = bkg_img('bg_map_ground')
image bg landing_pad = bkg_img('bg_landing-pad')
image bg result1 = bkg_img('bg_result_1-inaction')
image bg result2 = bkg_img('bg_result_2-apprehend')
image bg result3 = bkg_img('bg_result_3-assist')
image bg result4 = bkg_img('bg_result_4-diplomacy')
image bg credits = bkg_img('bg_credits')



####################################################
###############      Locations       ###############
####################################################

     
label map_screen:
    stop music
    play music "assets/mu_menu.ogg"

    # Show an imagemap.
    window hide None
    call screen main_map
    scene bg map
    window show None

    # Call screen assigns the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.
    if _return == "high_emb":
        jump loc_high_emb
    elif _return == "human_emb":
        jump loc_human_emb
    elif _return == "kald_emb":
        jump loc_kald_emb
    elif _return == "residences":
        jump loc_res
    elif _return == "market":
        jump loc_market
    elif _return == "port":
        jump loc_port

label loc_market:
    stop music
    play music "assets/mu_market.ogg"
    scene bg market with fade
    'You are at the Grand Marketplace. [[describe]'
    label market_menu:
        menu:
            'Talk to Alkay Volk Kladir':
                call ck_alkay
            'Talk to Cole Demarc':
                call ch_cole
            '(Back to Map)':
                jump map_screen
    jump market_menu

label loc_high_emb:
    stop music
    play music "assets/mu_emb.ogg"
    scene bg high_emb with fade
    'You are at the High Embassy. [[describe]'
    label menu_high_emb:
        if plot_state.stage == PlotStage.ARRIVE:
            if plot_state.high_emb_tried_bribe:
                guard 'Haven\'t we already talked to you? Unless you have official business here, you may not enter the High Embassy.'
                jump map_screen
            else:
                guard 'Greetings.'
                $ last_dialog = 'What business do you have here?'
                label high_emb_guard_menu:
                    menu:
                        guard '[last_dialog]'
                        'Lie and say that you have an appointment':
                            guard 'An appointment? Let me check... what\'s your name?'
                            p '[alias.full].'
                            guard 'Sorry, but I don\'t see you on my list.'
                            jump high_emb_guard_menu
                        'Try to bribe him to let you in':
                            guard 'What do I look like, a criminal? Get lost.'
                            $ plot_state.high_emb_tried_bribe = True
                            jump map_screen
                        'None, actually. I\'ll be on my way.':
                            jump map_screen
        else:
            menu:
                'Talk to Benjamin Columbus':
                    call ch_ben
                'Talk to Vatrisk Irridiss Kier':
                    call ck_vatrisk
                    if plot_state.stage == PlotStage.ATTACK_JUST_HAPPENED:
                        scene bg res with squares
                        call ch_sarah
                        jump map_screen
                    elif plot_state.stage == PlotStage.GAME_OVER:
                        return
                '(Back to Map)':
                    jump map_screen
    jump menu_high_emb

label loc_human_emb:
    stop music
    play music "assets/mu_emb.ogg"
    scene bg human_emb with fade
    'You are at the Human Embassy. [[describe]'
    label menu_human_emb:
        menu:
            'Talk to Lauren Gray':
                call ch_lauren
            '(Back to Map)':
                jump map_screen
    jump menu_human_emb
    
label loc_kald_emb:
    stop music
    play music "assets/mu_emb.ogg"
    scene bg kald_emb with fade
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
    stop music
    play music "assets/mu_res.ogg"
    scene bg res with fade
    'You are at the Residences. [[describe]'
    label menu_res:
        menu:
            'Talk to Sarah Liu':
                call ch_sarah
                if plot_state.stage == PlotStage.GAME_OVER:
                    return
            'Talk to Adam Demeter':
                call ch_adam
            'Talk to Noq Kriesk Lask':
                call ck_noq
            '(Back to Map)':
                jump map_screen
    jump menu_res
    
label loc_port:
    stop music
    play music "assets/mu_port.ogg"
    scene bg port with fade
    'You are at the Spaceport. [[describe]'
label loc_port_no_fade:
    label menu_port:
        menu:
            'Talk to Jonathan Caise':
                call ch_jon
            'Talk to Kro Zalva Ross':
                call ck_kro
            '(Back to Map)':
                jump map_screen
    jump menu_port
       