

###############################################################################

init: # трансформации для кнопок

    transform power_zoom:
        size (50, 50)

    transform close_zoom:
        size (25, 25)

    transform middle_wait:
        size (136, 136)
        on idle, selected_idle:
            yanchor 0 alpha 1.0
        on hover, selected_hover:
            yanchor 1 alpha 0.9

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
        size (80, 80)
        on idle, selected_idle:
            yanchor 0 alpha 0.4
        on hover, selected_hover:
            yanchor 1 alpha 1.0

    transform disable_menu(enable=True):
        size (80, 80)
        yanchor 0 alpha 0.2

    transform lang:
        on idle, selected_idle:
            size (160, 160) alpha 0.85
        on hover, selected_hover:
            size (180, 180) alpha 1.0

################################################################################

screen choice_lang():
    tag menu
    modal True
    style_prefix "lang"
    imagebutton anchor (0.5, 0.5) xpos 0.5 ypos 465 idle "interface/ENG.webp" action [Language("english"), Return()] focus_mask True at lang
    imagebutton anchor (0.5, 0.5) xpos 0.5 ypos 825 idle "interface/RUS.webp" action [Language(None), Return()] focus_mask True at lang

################################################################################

screen PowerButton():
    imagebutton:
        pos (935, 985) auto "interface laptop power %s"
        action [Hide("Search"), Jump("Waiting")] focus_mask True at power_zoom

################################################################################
screen LaptopScreen():

    tag menu
    modal True

    $ bookmarks = 2
    use PowerButton

    frame area(321, 93, 1275, 829) background None:
        viewport:
            xfill True
            ypos 30
            ysize 770
            mousewheel "change"
            draggable True

            vbox:
                xfill True
                spacing 30
                if len(search_theme) > 0:
                    imagebutton xalign .5 idle "interface laptop search" action Show("Search") focus_mask True
                else:
                    imagebutton xalign .5 idle "interface laptop search" action Call("nothing_search") focus_mask True


                vpgrid cols 3 xalign .5:

                    xspacing 50
                    yspacing 40

                    frame xysize(365, 270) background None:
                        vbox:
                            imagebutton idle "interface laptop shop" action Jump("LaptopShop")
                            text _("ИНТЕРНЕТ-МАГАЗИН") xalign 0.5 color "#000000"

                    frame xysize(365, 270) background None:
                        vbox:
                            imagebutton idle "interface laptop courses" action Jump("courses_start")
                            text _("ОНЛАЙН-КУРСЫ") xalign 0.5 color "#000000"

################################################################################
screen Search():
    modal True
    use PowerButton
    style_prefix "search"
    frame area(634, 150, 696, 450) background "#FFFFFF":
        vbox:
            spacing 10
            text _("Что будем искать?") color "#000000"
            hbox spacing 5:
                frame background None:
                    ysize 340
                    xfill True
                    viewport spacing 0 draggable True mousewheel True id "vp_choice":
                        ysize 330
                        vbox xsize 675 spacing 0:
                            $yy = 0
                            for i in search_theme:
                                $yy+=1
                                button action [Hide("Search"), Jump(i[1])] style "search_but":
                                    textbutton i[0] action [Hide("Search"), Jump(i[1])] yalign .0
                                key str(yy) action [Hide("Search"), Jump(i[1])]
                    vbar value YScrollValue("vp_choice") style "search_vscroll"
            button action Hide("Search") style "search_but":
                textbutton _("{i}назад{/i}") action Hide("Search") yalign .0
    key "K_ESCAPE" action Hide("Search")

style search_vscroll is vscrollbar:
    unscrollable "hide"

style search_but:
    xpadding 0 ypadding 0 xmargin 0 ymargin 0
    xsize 675
    foreground "interface marker black"

style search_button:
    xsize 675
    xpadding 30
    hover_background "gui/button/search_hover_background.png"

style search_button_text:
    idle_color "#000000"
    hover_color "#ffbe00"

################################################################################

screen OnlineShop():
    tag menu
    modal True
    use PowerButton
    default CurCat = 0
    frame area(221, 93, 1475, 829) background None:
        hbox:
            frame xsize 295 yfill True background None:
                xpadding 15 ypadding 15
                ## список категорий
                style_prefix "cat"
                vbox:
                    for i in ShopCat:
                        button background None action SetScreenVariable("CurCat", i) xsize 390 style "cat_but":
                            textbutton ShopCat[i] action SetScreenVariable("CurCat", i) selected CurCat == i

            frame xsize 1175 yfill True background None:
                xpadding 10 ypadding 15 #xmargin 0 ymargin 15
                ## список товаров категории
                style_prefix "goods"
                $ items_in_cat = 0

                hbox xsize 1135 spacing 5:
                    viewport mousewheel "change" draggable True id "vp1":
                        vbox spacing 15:
                            for i in items:
                                if items[i].InShop and items[i].category == CurCat:
                                    $ items_in_cat += 1
                                    frame xfill True background Frame("interface items-shop bg2", 10, 10):
                                        xpadding 10 ypadding 10 xmargin 5 ymargin 5
                                        hbox xsize 1120 spacing 15:
                                            add "interface items-shop "+items[i].img
                                            # frame xfill True:
                                            vbox spacing 5:
                                                frame xpos 50 xsize 400 background None:
                                                    text items[i].name style "item_header"
                                                frame xsize 700 background None:
                                                    text items[i].desc color gui.accent_color
                                                textbutton "{i}{b}$ "+str(items[i].price)+"{/b}{/i}" style "buy_button":
                                                    action NullAction()

                    vbar value YScrollValue("vp1") style "shop_vscroll"



style shop_vscroll is vscrollbar:
    unscrollable "hide"

style cat_but:
    xpadding 0 ypadding 0 xmargin 0 ymargin 0
    xsize 270
    foreground "interface marker"
style cat_button:
    xsize 270
    xpadding 30
style cat_button_text is default:
    font "trebucbd.ttf"
    # xpos 30
    yalign .5
    size 28
    idle_color gui.choice_button_text_idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style item_header:
    font "trebucbd.ttf"
    color "#FFFFFF"
    size 28

style price:
    font "trebucbd.ttf"
    color "#000000"
    size 36

style buy_button:
    xalign 1.0
    idle_background Frame("interface items-shop glossy idle", 12, 12)
    hover_background Frame("interface items-shop glossy hover", 12, 12)
    insensitive_background Frame("interface items-shop glossy insensitive", 12, 12)
    xpadding 30
    ypadding 10
    ymargin 5

style buy_button_text:
    font "trebuc.ttf"
    min_width 100
    text_align 0.5
    size 30
    idle_color "#000000"
    hover_color "#FFFFFF"

################################################################################
screen room_navigation():

    tag menu
    modal True
    key "K_F5" action [SetVariable("number_quicksave", number_quicksave+1), NewSaveName(), QuickSave()]
    key "K_F8" action QuickLoad()
    if _preferences.language is None:
        key "l" action Language("english")
        key "д" action Language("english")
    else:
        key "l" action Language(None)
        key "д" action Language(None)

    $ renpy.block_rollback()
    # $ renpy.fix_rollback()

    $  i = 0

    $ wait = 60 - int(tm.split(":")[1])
    hbox: # Кнопки комнат текущей локации
        yalign 0.99
        if current_room == current_location[0] and len(current_room.cur_char) > 2:
            xpos 76
        else:
            xalign 0.01
        #ysize 200
        spacing 2
        for room in current_location:
            $ i += 1
            $ char = ""
            for ch in room.cur_char:
                $ char += ch+", "
            if len(char) !=0:
                $ char = " ("+char[:-2]+")"

            button xysize (126, 190) action [Hide("wait_navigation"), SetVariable("prev_room", current_room), SetVariable("current_room", room), Jump("AfterWaiting")]:
                vbox xsize 126 spacing 0:
                    frame xysize (126, 140) background None:
                        imagebutton align (0.5, 0.0) idle room.icon selected_idle room.icon + " a" selected_hover room.icon + " a":
                                    selected room == current_room focus_mask True at middle_zoom
                                    action [Hide("wait_navigation"), SetVariable("prev_room", current_room), SetVariable("current_room", room), Jump("AfterWaiting")]
                        if room != current_room:
                            # вывод миниатюр персонажей внизу миниатюры локации
                            if len(room.cur_char) > 0:
                                hbox ypos 73 xalign 0.5 spacing - 30:
                                    for char in room.cur_char:
                                        if char == "alice" and (tm < "09:00" or tm >= "20:00"):
                                            imagebutton idle characters[char].pref+" icon a" focus_mask True at small_face:
                                                action [Hide("wait_navigation"), SetVariable("prev_room", current_room), SetVariable("current_room", room), Jump("AfterWaiting")]
                                        else:
                                            imagebutton idle characters[char].pref+" icon" focus_mask True at small_face:
                                                action [Hide("wait_navigation"), SetVariable("prev_room", current_room), SetVariable("current_room", room), Jump("AfterWaiting")]
                        else:
                            # если же это текущая локация - вывод над миниатюрой
                            # более крупных значков персонажей. положение зависит от количества
                            if len(current_room.cur_char) == 1:
                                if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                    imagebutton ypos -120 xalign 0.5 idle characters[current_room.cur_char[0]].pref+" icon a" focus_mask True:
                                                action NullAction() at middle_face
                                else:
                                    imagebutton ypos -120 xalign 0.5 idle characters[current_room.cur_char[0]].pref+" icon" focus_mask True:
                                                action NullAction() at middle_face
                            elif len(current_room.cur_char) == 2:
                                # Если в локации два персонажа, дополнительно проверяется не является ли тек.локация крайней слева
                                if current_room == current_location[0]:
                                    # и если да, то первая миниатюра отображается не слева, а над локацией
                                    if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                        imagebutton ypos -120 xalign 0.5 idle characters[current_room.cur_char[0]].pref+" icon a":
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -120 xalign 0.5 idle characters[current_room.cur_char[0]].pref+" icon":
                                                    focus_mask True action NullAction() at middle_face
                                    if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                        imagebutton ypos -100 xpos 63 idle characters[current_room.cur_char[1]].pref+" icon a":
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -100 xpos 63 idle characters[current_room.cur_char[1]].pref+" icon":
                                                    focus_mask True action NullAction() at middle_face
                                else:
                                    if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                        imagebutton ypos -100 xpos -63 idle characters[current_room.cur_char[0]].pref+" icon a":
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -100 xpos -63 idle characters[current_room.cur_char[0]].pref+" icon":
                                                    focus_mask True action NullAction() at middle_face
                                    if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                        imagebutton ypos -100 xpos 63 idle characters[current_room.cur_char[1]].pref+" icon a":
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -100 xpos 63 idle characters[current_room.cur_char[1]].pref+" icon":
                                                    focus_mask True action NullAction() at middle_face
                            elif len(current_room.cur_char) == 3:
                                if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                    imagebutton ypos -100 xpos -63 idle characters[current_room.cur_char[0]].pref+" icon a":
                                                focus_mask True action NullAction() at middle_face
                                else:
                                    imagebutton ypos -100 xpos -63 idle characters[current_room.cur_char[0]].pref+" icon":
                                                focus_mask True action NullAction() at middle_face
                                if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                    imagebutton ypos -120 align (0.5, 0.0) idle characters[current_room.cur_char[1]].pref+" icon a":
                                                focus_mask True action NullAction() at middle_face
                                else:
                                    imagebutton ypos -120 align (0.5, 0.0) idle characters[current_room.cur_char[1]].pref+" icon":
                                                focus_mask True action NullAction() at middle_face
                                if current_room.cur_char[0] == "alice" and (tm < "09:00" or tm >= "20:00"):
                                    imagebutton ypos -100 xpos 63 idle characters[current_room.cur_char[2]].pref+" icon":
                                                focus_mask True action NullAction() at middle_face
                                else:
                                    imagebutton ypos -100 xpos 63 idle characters[current_room.cur_char[2]].pref+" icon":
                                                focus_mask True action NullAction() at middle_face
                            elif len(current_room.cur_char) == 4:
                                pass
                    text room.name font "trebucbd.ttf" size 18 drop_shadow[(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
            key str(i) action [Hide("wait_navigation"), SetVariable("prev_room", current_room), SetVariable("current_room", room), Jump("AfterWaiting")]

    hbox:
        align(.99, .99)  # правый нижний угол
        # располагаем клавиши действий

        for id in ListButton:  # добавим последовательно все доступные действия (ключи берем из списка кнопок)
            $ act = AvailableActions[id] # а сами кнопки из словаря
            if act.active and act.enabled:
                button xysize (126, 190) action [Hide("wait_navigation"), Jump(act.label)]: # Поговорить
                    vbox xsize 126 spacing 0:
                        frame xysize (126, 140) background None:
                            imagebutton idle act.icon align (0.5, 0.0) focus_mask True:
                                        action [Hide("wait_navigation"), Jump(act.label)] at middle_zoom
                        text act.sing font "trebucbd.ttf" size 18 drop_shadow[(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2

        button xysize (136, 190) action [Hide("wait_navigation"), SetVariable("spent_time", wait), Jump("Waiting")]: # ждать час
            vbox xsize 136 spacing 0:
                frame xysize (136, 140) background None:
                    imagebutton idle "interface wait 60" hover "interface wait 60 a":# hovered Show("wait_navigation"):
                                align (0.5, 0.0) focus_mask True action [Hide("wait_navigation"), SetVariable("spent_time", wait), Jump("Waiting")] at middle_wait
                text _("ЖДАТЬ") font "trebucbd.ttf" size 18 drop_shadow[(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2

    vbox:  # Время и день недели
        align(0.5, 0.01)
        text tm xalign(0.5)
        text weekdays[(day+2) % 7][1] xalign(0.5)


    $ kol = 0

    for poss in possibility:
        if possibility[poss].stage_number >= 0: # количество открытых возможностей
            $ kol += 1

    hbox:  # верхнее меню
        align(0.02, 0.01)
        spacing 2
        imagebutton idle "interface menu userinfo" focus_mask True action [Hide("wait_navigation"), Show("menu_userinfo")] at small_menu
        imagebutton idle "interface menu inventory" focus_mask True action [Hide("wait_navigation"), Show("menu_inventory")] at small_menu
        if kol > 0:
            imagebutton idle "interface menu opportunity" focus_mask True action [Hide("wait_navigation"), Show("menu_opportunity")] at small_menu
        else:
            imagebutton idle "interface menu opportunity" focus_mask True action [Hide("wait_navigation"), Show("menu_opportunity")] at disable_menu
        imagebutton idle "interface menu help" focus_mask True action [Hide("wait_navigation"), Show("menu_my_help")] at small_menu
        imagebutton idle "interface menu main" focus_mask True action ShowMenu("save") at small_menu
        imagebutton idle "interface menu patreon" focus_mask True action [Hide("wait_navigation"), OpenURL("https://www.patreon.com/aleksey90artimages")] at small_menu

screen wait_navigation(): # дополнительные кнопки для ожидания в 10 и 30 минут
    frame align(.99, .99) xysize(123, 395) background None:
        vbox:
            spacing 5
            imagebutton idle "interface wait 10" focus_mask True action [Hide("wait_navigation"), SetWarilable("spent_time", 10), Jump("Waiting")] at small_zoom
            imagebutton idle "interface wait 30" focus_mask True action [Hide("wait_navigation"), SetVariable("spent_time", 30), Jump("Waiting")] at small_zoom
    timer 2.0 action Hide("wait_navigation")

################################################################################
screen menu_my_help():
    tag menu
    style_prefix "my_help"

    add "interface phon"
    frame area(150, 95, 350, 50) background None:
        text _("ПОЛЕЗНОЕ") color gui.choice_button_text_idle_color size 28 font "hermes.ttf"
    imagebutton pos (1740, 100) auto "interface close %s" action Jump("AfterWaiting") focus_mask True at close_zoom

    default CurHP = 0

    hbox pos (300, 180) spacing 30:
        frame xsize 250 ysize 850 background None:
            hbox:
                viewport mousewheel "change" draggable True id "vp1":
                    vbox spacing 5:
                        for i in range(len(helps)):
                            button background None action SetScreenVariable("CurHP", i) xsize 240:
                                xpadding 0 ypadding 0 xmargin 0 ymargin 0
                                textbutton helps[i].id action SetScreenVariable("CurHP", i) selected CurHP == i
                                foreground "interface marker"
                vbar value YScrollValue("vp1") style "hp_vscroll"
        frame area (0, 0, 1040, 850) background None:
            vbox spacing 20:
                frame xsize 1030 xalign 0.5 background None:
                    text helps[CurHP].name size 30 font "hermes.ttf" xalign 0.5
                frame xsize 1040 xalign 0.5 background None:
                    hbox:
                        viewport mousewheel "change" draggable True id "vp2":
                            vbox spacing 30:
                                text helps[CurHP].desc size 24  color gui.choice_button_text_idle_color
                        vbar value YScrollValue("vp2") style "hp_vscroll"

    key "K_ESCAPE" action Jump("AfterWaiting")
    key "mouseup_3" action Jump("AfterWaiting")

style my_help_button_text is default:
    font "trebucbd.ttf"
    xpos 30
    yalign .0
    size 28
    idle_color gui.choice_button_text_idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style hp_vscroll is vscrollbar:
    unscrollable "hide"


################################################################################
screen menu_opportunity():

    tag menu
    style_prefix "opportunity"

    $ kol = 0
    $ all = len(possibility) # Общее количество введенных в игру "возможностей"
    $ list_stage = []

    for poss in possibility:
        if possibility[poss].stage_number >= 0: # количество открытых возможностей
            $ kol += 1
            if CurPoss == "":
                $ CurPoss = poss

    if CurPoss != "":
        default view_stage = possibility[CurPoss].stage_number
        for i in range(len(possibility[CurPoss].stages)-1):
            if possibility[CurPoss].stages[i].used:
                $ list_stage.append(i)


    add "interface phon"
    frame area(150, 95, 350, 50) background None:
        text _("ВОЗМОЖНОСТИ ([kol] / [all])") color gui.choice_button_text_idle_color size 28 font "hermes.ttf"
    imagebutton pos (1740, 100) auto "interface close %s" action Jump("AfterWaiting") focus_mask True at close_zoom


    hbox pos (150, 150) spacing 30:
        frame  ypos 25 xsize 400 ysize 850 background None:
            hbox:
                viewport mousewheel "change" draggable True id "vp1":
                    vbox spacing 5:
                        for poss in possibility:
                            if possibility[poss].stage_number >= 0:
                                if CurPoss == "":
                                    $ CurPoss = poss
                                    $ view_stage = possibility[poss].stage_number
                                button background None action [SetVariable("CurPoss", poss), SetScreenVariable("view_stage", possibility[poss].stage_number)] xsize 390:
                                    xpadding 0 ypadding 0 xmargin 0 ymargin 0
                                    textbutton possibility[poss].name action [SetVariable("CurPoss", poss), SetScreenVariable("view_stage", possibility[poss].stage_number)] selected CurPoss == poss
                                    foreground "interface marker"
                vbar value YScrollValue("vp1") style "poss_vscroll"
        if CurPoss != "":
            frame area (0, 30, 1190, 850) background None:
                vbox spacing 20:
                    frame xsize 800 ysize 400 pos (195, 0) background None:
                        if possibility[CurPoss].stages[view_stage].image != "":
                            add possibility[CurPoss].stages[view_stage].image
                    frame xsize 1180 xalign 0.5 background None:
                        text possibility[CurPoss].name size 30 font "hermes.ttf" xalign 0.5
                    frame area (0, 0, 1190, 400) background None:
                        hbox:
                            viewport mousewheel "change" draggable True id "vp2":
                                vbox spacing 30:
                                    text possibility[CurPoss].stages[view_stage].desc size 24  color gui.choice_button_text_idle_color
                                    text possibility[CurPoss].stages[view_stage].ps size 28
                            vbar value YScrollValue("vp2") style "poss_vscroll"
    if len(list_stage) > 1:
        imagebutton pos (690, 360) auto "interface prev %s":
            focus_mask True
            action SetScreenVariable("view_stage", list_stage.index(view_stage)-1)
            sensitive view_stage > min(list_stage)
        imagebutton pos (1570, 360) auto "interface next %s":
            focus_mask True
            action SetScreenVariable("view_stage", list_stage.index(view_stage)+1)
            sensitive view_stage < max(list_stage)

    key "K_ESCAPE" action Jump("AfterWaiting")
    key "mouseup_3" action Jump("AfterWaiting")

style opportunity_button_text is default:
    font "trebucbd.ttf"
    xpos 30
    yalign .0
    size 28
    idle_color gui.choice_button_text_idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style poss_vscroll is vscrollbar:
    xsize 7
    unscrollable "hide"

################################################################################
screen menu_inventory():

    tag menu

    add "interface phon2"
    style_prefix "inventory"
    frame area(150, 95, 350, 50) background None:
        text _("ВЕЩИ") color gui.choice_button_text_idle_color size 28 font "hermes.ttf"

    imagebutton pos (1740, 100) auto "interface close %s" action Jump("AfterWaiting") focus_mask True at close_zoom

    $ cells = 0
    $ items_list = {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : []
    }
    $ listrows = [0, 0, 0, 0, 0]

    $ cur_col = 0
    for id in items:
        if items[id].have:
            $ cells += items[id].cells
            if items[id].cells > 1:
                $ listrows[cur_col] += items[id].cells
                $ items_list[cur_col].append(id)
                $ cur_col += 1
                if cur_col > 4:
                    $ cur_col = 1


    if cells % 5 > 0:
        $ tabrows = cells // 5 + 1
    else:
        $ tabrows = cells // 5

    for id in items:
        if items[id].have and items[id].cells == 1:
            $ cur_col = 5
            for i in range(5):
                if cur_col == 5 and listrows[i] == min(listrows):
                    $ cur_col = i

            $ added = False
            if listrows[cur_col] + items[id].cells <= tabrows:
                $ added = True
                $ listrows[cur_col] += items[id].cells
                $ items_list[cur_col].append(id)

    if cells > 0:
        $ desc = _("Ни один предмет не выбран")
    else:
        $ desc = _("В данный момент в инвентаре ничего нет")

    default tl = Tooltip("")
    default tdesc = Tooltip(desc)

    vbox:
        xalign 0.5
        xsize 1620
        ypos 170
        spacing 15
        frame xsize 1460 ysize 650 xalign 0.5 background None: #"#ffffff":
            viewport:
                xalign 0.5
                draggable True
                mousewheel True
                if tabrows > 2:
                    scrollbars "vertical"

                if tabrows < 3:
                    $ tabrows = 3
                hbox:
                    spacing 2
                    for cur_col in range(5):
                        vbox:
                            spacing 4
                            for id in items_list[cur_col]:
                                $ im_name = "interface/items/" + items[id].img + ".webp"
                                if items[id].cells == 2:
                                    frame area(0, 0, 286, 456) background "interface items bg2":
                                        imagebutton align (0.5, 0.5) idle im.Scale(im.MatrixColor(im_name, im.matrix.desaturate()), 224, 360) hover "interface items "+items[id].img:
                                            action NullAction()
                                            hovered [tl.Action(items[id].name), tdesc.Action(items[id].desc)]
                                else:
                                    frame area(0, 0, 286, 226) background "interface items bg":
                                        imagebutton align (0.5, 0.5) idle im.Scale(im.MatrixColor(im_name, im.matrix.desaturate()), 252, 198) hover "interface items "+items[id].img:
                                            action NullAction()
                                            hovered [tl.Action(items[id].name), tdesc.Action(items[id].desc)]

                            $ addcells = tabrows - listrows[cur_col]
                            if addcells > 0:
                                for i in range(addcells):
                                    frame area(0, 0, 286, 226) background "interface items bg":
                                        button align (0.5, 0.5) action NullAction():
                                            hovered [tl.Action(""), tdesc.Action(desc)]


        frame area(200, 0, 1220, 50) background None:
            text tl.value xalign 0.5 size 28 font "hermes.ttf"  color gui.text_color

        frame area(300, 0, 1020, 180) background None:
            text tdesc.value xalign 0.5 size gui.text_size font gui.text_font color gui.accent_color

    key "K_ESCAPE" action Jump("AfterWaiting")
    key "mouseup_3" action Jump("AfterWaiting")

################################################################################
screen menu_userinfo():

    tag menu
    add "interface phon"
    style_prefix "userinfo"

    frame area(150, 95, 350, 50) background None:
        text _("ПЕРСОНАЖИ") color gui.choice_button_text_idle_color size 28 font "hermes.ttf"

    imagebutton pos (1740, 100) auto "interface close %s" action Jump("AfterWaiting") focus_mask True at close_zoom

    hbox pos (150, 150) spacing 30:
        hbox ypos 25 xsize 190 spacing 5:
            viewport mousewheel "change" draggable True id "vp":
                vbox spacing 5:
                    button background None  action SetVariable("CurChar", "max") xsize 180:
                        xpadding 0 ypadding 0 xmargin 0 ymargin 0
                        textbutton _("Макс") action SetVariable("CurChar", "max") selected CurChar == "max"
                        foreground "interface marker"
                    for char in characters:
                        button background None action SetVariable("CurChar", char) xsize 180:
                            xpadding 0 ypadding 0 xmargin 0 ymargin 0
                            textbutton characters[char].name action SetVariable("CurChar", char) selected CurChar == char
                            foreground "interface marker"
            vbar value YScrollValue("vp") style "info_vscroll"

        if CurChar == "max": ## временное определение на стадии вывода изображения
            if dress_suf["max"] == "a":
                add "Max info 01" size (550, 900) xpos -50 ypos 10
            else:
                add "Max info 01b" size (550, 900) xpos -50 ypos 10

        else:
            frame xysize(550, 900) background None:
                if characters[CurChar].sufix == "":
                    add characters[CurChar].pref+" info-00" size (550, 900) xpos -50 ypos 10
                else:
                    add characters[CurChar].pref+" info "+eval(CurChar+"_dress[\""+characters[CurChar].sufix+"\"]") size (550, 900) xpos -50 ypos 10


        viewport area (0, 30, 880, 850):
            vbox spacing 20:
                frame xsize 850 background None:
                    if CurChar == "max":
                        text max_profile.desc size 24
                    else:
                        text characters[CurChar].desc size 24

                # romantic interest

                frame pos (50, 20) xsize 800 background None:
                    if CurChar == "max":
                        vbox spacing -1:
                            for char in characters:
                                # relmax
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        $ char_name = characters[char].name_4
                                        text _("Отношения с [char_name!t]") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        if characters[char].mood == -200:
                                            text _("Война") size 24
                                        elif -200 < characters[char].mood <= -100 :
                                            text _("Враждебные") size 24
                                        elif -100 < characters[char].mood < 0 :
                                            text _("Плохие") size 24
                                        elif 0 <= characters[char].mood < 100 :
                                            text _("Прохладные") size 24
                                        elif 100 <= characters[char].mood < 250 :
                                            text _("Неплохие") size 24
                                        elif 250 <= characters[char].mood < 400 :
                                            text _("Хорошие") size 24
                                        elif 400 <= characters[char].mood < 700 :
                                            text _("Тёплые") size 24
                                        elif 700 <= characters[char].mood < 1000 :
                                            text _("Дружеские") size 24
                                        else:
                                            text _("Близкие") size 24
                            frame:
                                area (0, 0, 350, 25)
                                background None

                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Запас сил") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    text str(int(max_profile.energy))+"%" size 24
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Тренированность") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    text str(max_profile.training)+"%" size 24
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Чистота") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    text str(max_profile.cleanness)+"%" size 24

                            frame:
                                area (0, 0, 350, 25)
                                background None
                            frame xsize 350 background None:
                                text _("Навыки:") size 26 font "trebucbd.ttf"
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Навык убеждения") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    text str(max_profile.persuade) size 24
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Навык скрытности") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    text str(max_profile.stealth) size 24
                            if max_profile.massage > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык массажа") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        text str(max_profile.massage) size 24
                            if max_profile.ero_massage > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык эро.массажа") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        text str(max_profile.ero_massage) size 24
                            if max_profile.kissing > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык поцелуев") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        text str(max_profile.kissing) size 24


                    elif CurChar == "eric":
                        pass
                    else:
                        vbox spacing -1:
                            # mood
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Настроение") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    if characters[CurChar].mood == -100:
                                        text _("Ужасное") size 24
                                    elif -100 < characters[CurChar].mood <= -72 :
                                        text _("Очень плохое") size 24
                                    elif -72 < characters[CurChar].mood <= -44 :
                                        text _("Плохое") size 24
                                    elif -44 < characters[CurChar].mood <= -16 :
                                        text _("Не очень") size 24
                                    elif -16 < characters[CurChar].mood <= 16 :
                                        text _("Нейтральное") size 24
                                    elif 16 < characters[CurChar].mood <= 44 :
                                        text _("Неплохое") size 24
                                    elif 44 < characters[CurChar].mood <= 72 :
                                        text _("Хорошее") size 24
                                    elif 72 < characters[CurChar].mood < 100 :
                                        text _("Очень хорошее") size 24
                                    else:
                                        text _("Прекрасное") size 24
                            # relmax
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Уровень отношений") size 24 color gui.choice_button_text_idle_color
                                frame xfill True background None:
                                    if characters[CurChar].relmax == -200:
                                        text _("Война") size 24
                                    elif -200 < characters[CurChar].relmax <= -100 :
                                        text _("Враждебные") size 24
                                    elif -100 < characters[CurChar].relmax < 0 :
                                        text _("Плохие") size 24
                                    elif 0 <= characters[CurChar].relmax < 100 :
                                        text _("Прохладные") size 24
                                    elif 100 <= characters[CurChar].relmax < 250 :
                                        text _("Неплохие") size 24
                                    elif 250 <= characters[CurChar].relmax < 400 :
                                        text _("Хорошие") size 24
                                    elif 400 <= characters[CurChar].relmax < 700 :
                                        text _("Тёплые") size 24
                                    elif 700 <= characters[CurChar].relmax < 1000 :
                                        text _("Дружеские") size 24
                                    else:
                                        text _("Близкие") size 24

                            # mindedness
                            if not characters[CurChar].mindedness is None:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Раскрепощенность") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        text str(characters[CurChar].mindedness) size 24
                            if not characters[CurChar].releric is None:
                                # releric
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Отношения с Эриком") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        if characters[CurChar].releric == -3:
                                            text _("Война") size 24
                                        elif characters[CurChar].releric == -2:
                                            text _("Враждебные") size 24
                                        elif characters[CurChar].releric == -1:
                                            text _("Плохие") size 24
                                        elif characters[CurChar].releric == 0:
                                            text _("Прохладные") size 24
                                        elif characters[CurChar].releric == 1:
                                            text _("Неплохие") size 24
                                        elif characters[CurChar].releric == 2:
                                            text _("Хорошие") size 24
                                        elif characters[CurChar].releric == 3:
                                            text _("Тёплые") size 24
                                        elif characters[CurChar].releric == 4:
                                            text _("Дружеские") size 24
                                        else:
                                            text _("Близкие") size 24

                                # influence
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Влияние Эрика") size 24 color gui.choice_button_text_idle_color
                                    frame xfill True background None:
                                        text str(characters[CurChar].mindedness)+"%" size 24
    key "K_ESCAPE" action Jump("AfterWaiting")
    key "mouseup_3" action Jump("AfterWaiting")

style userinfo_button_text is default:
    font "trebucbd.ttf"
    xpos 30
    yalign .0
    size 30
    idle_color gui.choice_button_text_idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style info_vscroll is vscrollbar:
    unscrollable "hide"
