
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# A place to put testing code that will be run at the beginning of the program

label tests:
    if config.developer:
        $ debug_skip_intro = True
        $ debug_init_stage = PlotStage.KALD_GOVT_INFO
    return
