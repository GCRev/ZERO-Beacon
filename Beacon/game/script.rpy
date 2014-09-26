
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garret Holman

label start:
    jump intro


####################################################
#############        Python Code       #############
####################################################

init python:
    def png(fname):
        return im.FactorScale("assets/" + fname + ".png", config.screen_width / 1600.0)


####################################################
###############    Character Defs    ###############
####################################################

define p = Character('Player')
define comm = Character('Commander')

define ben = Character('Benjamin Columbus')
define cole = Character('Cole Demarc')
define jon = Character('Jonathan Caise')
define lauren = Character('Lauren Gray')
define adam = Character('Adam Demeter')
define sarah = Character('Sarah Liu')

define vatrisk = Character('Vatrisk Irridiss Kier')
define alkay = Character('Alkay Volk Kladir')
define lorisk = Character('Lorisk Nidaria Kol')
define kro = Character('Kro Zalva Ross')
define noq = Character('Noq Kriesk Lask')
define lida = Character('Lida Ezekeri Skar')


####################################################
###############        Images        ###############
####################################################

image ben = png("ch_ben")
image cole = png("ch_cole")
image jon = png("ch_jon") 
image lauren = png("ch_lauren")
image adam = png("ch_adam")
image sarah = png("ch_sarah")

image vatrisk = png("ck_vatrisk")
image alkay = png("ck_alkay") 
image lorisk = png("ck_lorisk") 
image kro = png("ck_kro") 
image noq = png("ck_noq")
image lida = png("ck_lida")

image bg market = png("bg_market")
image bg high_emb = png("bg_high-emb")
image bg human_emb = png("bg_human-emb")
image bg kald_emb = png("bg_kald-emb")
image bg res = png("bg_res")
image bg port = png("bg_port")

image bg map = png("bg_map")
image bg landing_pad = png("bg_landing-pad")
image bg result1 = png("result_1-inaction")
image bg result2 = png("result_2-apprehend")
image bg result3 = png("result_3-assist")
image bg result4 = png("result_4-dipolomacy")


####################################################
###############      Locations       ###############
####################################################
        
label loc_market:
    scene bg market
    "You are at the Grand Marketplace. (describe)"
    menu:
        "Talk to Cole Demarc":
            jump ch_cole
        "Talk to Alkay Volk Kladir":
            jump ck_alkay
        "(Back to Map)":
            jump map_screen

label loc_high_emb:
    scene bg high_emb
    "You are at the High Embassy. (describe)"
    menu:
        "Talk to Benjamin Columbus":
            jump ch_ben
        "Talk to Vatrisk Irridiss Kier":
            jump ck_vatrisk
        "(Back to Map)":
            jump map_screen
    jump map_screen
    
label loc_human_emb:
    scene bg human_emb
    "You are at the Human Embassy. (describe)"
    menu:
        "Talk to Lauren Gray":
            jump ch_lauren
        "(Back to Map)":
            jump map_screen
    jump map_screen
    
label loc_kald_emb:
    scene bg kald_emb
    "You are at the Kaldrean Embassy. (describe)"
    menu:
        "Talk to Lorisk Nidaria Kol":
            jump ck_lorisk
        "Talk to Lida Ezekeri Skar":
            jump ck_lida
        "(Back to Map)":
            jump map_screen
    jump map_screen
    
label loc_res: 
    scene bg res
    "You are at the Residences. (describe)"
    menu:
        "Talk to Sarah Liu":
            jump ch_sarah
        "Talk to Adam Demeter":
            jump ch_adam
        "Talk to Noq Kriesk Lask":
            jump ck_noq
        "(Back to Map)":
            jump map_screen
    jump map_screen
    
label loc_port:
    scene bg port
    "You are at the Spaceport. (describe)"
    menu:
        "Talk to Jonathan Caise":
            jump ch_jon
        "Talk to Kro Zalva Ross":
            jump ck_kro
        "(Back to Map)":
            jump map_screen
    jump map_screen
        

####################################################
#############     Menus / Cutscenes    #############
####################################################

label map_screen:
    scene bg map
    "Choose a destination."
    menu:
        "Grand Marketplace":
            jump loc_market
        "High Embassy":
            jump loc_high_emb
        "Human Embassy":
            jump loc_human_emb
        "Kaldrean Embassy":
            jump loc_kald_emb
        "Residences":
            jump loc_res
        "Spaceport":
            jump loc_port

label intro:
    scene black
    "blah blah blah narration"
    comm "blah blah blah more narration"
    jump loc_port


####################################################
#############     Character Dialog     #############
####################################################

label ch_ben:
    show ben
    "(blah blah blah)"
    hide ben
    jump loc_high_emb

label ch_cole:
    show cole
    "(blah blah blah)"
    hide cole
    jump loc_market

label ch_jon:
    show jon
    "(blah blah blah)"
    hide jon
    jump loc_port

label ch_lauren:
    show lauren
    "(blah blah blah)"
    hide lauren
    jump loc_human_emb

label ch_adam:
    show adam
    "(blah blah blah)"
    hide adam
    jump loc_res

label ch_sarah:
    show sarah
    "(blah blah blah)"
    hide sarah
    jump loc_res    

label ck_vatrisk:
    show vatrisk
    "(blah blah blah)"
    hide vatrisk
    jump loc_high_emb

label ck_kro:
    show kro
    "(blah blah blah)"
    hide kro
    jump loc_port
    
label ck_alkay:
    show alkay
    "(blah blah blah)"
    hide alkay
    jump loc_market
    
label ck_noq:
    show noq
    "(blah blah blah)"
    hide noq
    jump loc_res
    
label ck_lorisk:
    show lorisk
    "(blah blah blah)"
    hide lorisk
    jump loc_kald_emb
    
label ck_lida:
    show lida
    "(blah blah blah)"
    hide lida
    jump loc_kald_emb
