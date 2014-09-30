
# Beacon
# ZERO Studios
# Kyle McCormick, Graham Held, Garrett Holman
# A place to put testing code that will be run at the beginning of the program

label tests:
##    $ plot_state.stage = PlotStage.VL_PLANS
##    $plot_state.lauren_lorisk_info = InfoGet.SUCCESS
##    $plot_state.adam_alkay_info = InfoGet.SUCCESS
##    $plot_state.kro_obsession_info = InfoGet.SUCCESS
    $ skip_intro = True
    $ plot_state.alkay_vl_plan_info = InfoGet.SUCCESS
    $ plot_state.stage = PlotStage.VL_PLANS 
    $ plot_state.vatrisk_trust = TrustLevel.HIGH
    return
