

################################################################################
##   переходы
################################################################################


define dis1 = Dissolve(.1)
define dis2 = Dissolve(.2)
define dis3 = Dissolve(.3)
define dis4 = Dissolve(.4)
define dis5 = Dissolve(.5)
define dis6 = Dissolve(.6)
define dis7 = Dissolve(.7)
define dis8 = Dissolve(.8)
define dis9 = Dissolve(.9)
define dis10 = Dissolve(1.0)
define dis11 = Dissolve(1.1)
define dis12 = Dissolve(1.2)
define dis13 = Dissolve(1.3)
define dis14 = Dissolve(1.4)
define dis15 = Dissolve(1.5)
define dis16 = Dissolve(1.6)
define dis17 = Dissolve(1.7)
define dis18 = Dissolve(1.8)
define dis19 = Dissolve(1.9)
define dis20 = Dissolve(2.0)


# Если нужно, чтобы текст появлялся без задержки
define diss1 = { "master" : Dissolve(.1) }
define diss2 = { "master" : Dissolve(.2) }
define diss3 = { "master" : Dissolve(.3) }
define diss4 = { "master" : Dissolve(.4) }
define diss5 = { "master" : Dissolve(.5) }
define diss6 = { "master" : Dissolve(.6) }
define diss7 = { "master" : Dissolve(.7) }
define diss8 = { "master" : Dissolve(.8) }
define diss9 = { "master" : Dissolve(.9) }
define diss10 = { "master" : Dissolve(1.0) }
define diss11 = { "master" : Dissolve(1.1) }
define diss12 = { "master" : Dissolve(1.2) }
define diss13 = { "master" : Dissolve(1.3) }
define diss14 = { "master" : Dissolve(1.4) }
define diss15 = { "master" : Dissolve(1.5) }
define diss16 = { "master" : Dissolve(1.6) }
define diss17 = { "master" : Dissolve(1.7) }
define diss18 = { "master" : Dissolve(1.8) }
define diss19 = { "master" : Dissolve(1.9) }
define diss20 = { "master" : Dissolve(2.0) }


define fade4 = Fade(0.4, 0, 0.3)

################################################################################
##   трансформации gl2
################################################################################

transform saturate:             # обесцвеченное, при наведении оранжевым
    on idle:
        matrixcolor TintMatrix('#FFBE00')
    on hover:
        matrixcolor SaturationMatrix(1.0)

transform my_color(n_color):    # назначаем свой цвет (пока не используется)
    matrixcolor TintMatrix(n_color)

transform desaturate:           # обесцвечиваем
    matrixcolor SaturationMatrix(0.0)

transform blurred:              # размываем
    blur 12

transform things:               # для инвентаря. обесцвеченное разм.90%, при наведении цвет и 100%
    on idle, selected_idle:
        matrixcolor SaturationMatrix(0.0)
        zoom 0.9
    on hover, selected_hover:
        matrixcolor SaturationMatrix(1.0)
        zoom 1.0

transform mark_alt:             # меняющий цвета маркер (ноутбук)
    anchor (0.5, 0.5)
    rotate 90
    pos (19, 14)

    block:
        linear 0.3 matrixcolor TintMatrix('#FF0000')
        pause 0.3
        linear 0.3 matrixcolor TintMatrix('#FFBE00')
        pause 0.3
        linear 0.3 matrixcolor TintMatrix('#008000')
        pause 0.3
        linear 0.3 matrixcolor TintMatrix('#0000FF')
        pause 0.3
        repeat

################################################################################
##   трансформации
################################################################################

transform book_marks:
    on idle:
        zoom 1.0
    on hover:
        zoom 1.02

transform close_zoom:
    size ((105, 35) if renpy.variant("small") else (75, 25))
    xanchor (35 if renpy.variant("small") else 25)

transform middle_zoom:
    size (136, 136)
    on idle, selected_idle:
        yanchor 0 alpha 1.0
    on hover, selected_hover:
        yanchor 1 alpha 0.9

transform small_zoom:
    size (100, 100)
    on idle, selected_idle:
        yanchor 0 alpha 1.0
    on hover, selected_hover:
        yanchor 1 alpha 0.9

transform middle_face:
    size (120, 120)
    on idle, selected_idle:
        yanchor 0 alpha 1.0
    on hover, selected_hover:
        yanchor 1 alpha 0.9

transform small_face:
    size (60, 60)
    on idle, selected_idle:
        yanchor 0 alpha 1.0
    on hover, selected_hover:
        yanchor 1 alpha 0.93

transform small_menu:
    size ((100, 100) if renpy.variant('small') else (80, 80))
    on idle, selected_idle:
        yanchor 0 alpha 0.4
    on hover, selected_hover:
        yanchor 1 alpha 1.0

transform main_menu_btn:
    size (100, 100)
    on idle, selected_idle:
        yanchor 0 alpha 0.8
    on hover, selected_hover:
        yanchor 1 alpha 1.0

transform disable_menu:
    size ((100, 100) if renpy.variant('small') else (80, 80))
    yanchor 0 alpha 0.2

transform lang:
    on idle, selected_idle:
        size (160, 160) alpha 0.85
    on hover, selected_hover:
        size (180, 180) alpha 1.0

transform zoom_out(x, y):
    size (x, y)

transform mark:
    'interface marker red'
    0.5
    'interface marker yellow'
    0.5
    'interface marker blue'
    0.5
    'interface marker green'
    0.5
    'interface marker red'
    0.5
    'interface marker blue'
    0.5
    repeat

transform main_logo2:
    on idle:
        zoom 0.95
    on hover:
        zoom 1.0

transform tv_screen:
    xpos 63, ypos 48

transform laptop_screen:
    size (1476, 831)
    xpos 221, ypos 92

transform left_shift:
    xpos -200

transform right_shift:
    xpos 200

transform alt_left_shift:
    xpos -75

transform alt_right_shift:
    xpos 300

transform ladder_left_shift:
    ypos -100

transform ladder_right_shift:
    xpos 370
    ypos 50

transform cam_shower_right:
    size (1475, 829)
    xpos 360
    ypos 65

transform cam_shower_left:
    size (1475, 829)
    xpos 100
    ypos 110

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform stay_in_room:
    zoom 1.1
    align (.5, 0)

transform cookies(sc=1.0, al=1.0):
    on idle, selected_idle:
        alpha 0.8 * al zoom sc * 1.0

    on hover, selected_hover:
        alpha 1.0 zoom sc * 1.0

transform cookies_events(sc=1.0, al=1.0):
    on idle, selected_idle:
        alpha al * 1.0 zoom sc * 1.0

    on hover, selected_hover:
        alpha 1.0 zoom sc * 1.1


################################################################################
##   трансформации главного меню
################################################################################

transform main_logo:
    on idle:
        zoom 0.8#1.0
    on hover:
        zoom 0.82#1.02

transform eye_movement:
    alpha 1.0
    pause 2.0
    alpha 0.0
    pause 2.0
    repeat


################################################################################
##   трансформации-эффекты
################################################################################


transform trans_zoom_out(from_zoom=1.03, time_zoom=.3, xyalign=[.5,.5]):
    align(xyalign[0], xyalign[1]) zoom from_zoom
    linear time_zoom zoom 1.0

transform trans_zoom_vibr(xyalign=[.5,.5]):
    align(xyalign[0], xyalign[1]) zoom 1
    linear .2 zoom 1.15
    linear .15 zoom 1.0
    linear .1 zoom 1.1
    linear .08 zoom 1.0
    linear .07 zoom 1.05
    linear .05 zoom 1.0
