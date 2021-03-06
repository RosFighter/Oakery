

###############################################################################

init: # трансформации для кнопок

    transform power_zoom:
        size (50, 50)

    transform book_marks:
        on idle:
            zoom 1.0
        on hover:
            zoom 1.02

    transform close_zoom:
        xanchor 25
        size (75, 25)

    transform close_zoom_var_small:
        xanchor 35
        size (105, 35)

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

    transform small_menu_mobile:
        size (100, 100)
        on idle, selected_idle:
            yanchor 0 alpha 0.4
        on hover, selected_hover:
            yanchor 1 alpha 1.0

    transform disable_menu:
        size (80, 80)
        yanchor 0 alpha 0.2

    transform disable_menu_mobile:
        size (100, 100)
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
        size (1475, 829)
        xpos 221, ypos 93

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

################################################################################

screen choice_lang():
    tag menu
    modal True
    style_prefix 'lang'
    imagebutton anchor (0.5, 0.5) xpos 0.5 ypos 465 idle 'interface/ENG.webp' action [Language('english'), Function(renpy.full_restart)] focus_mask True at lang
    imagebutton anchor (0.5, 0.5) xpos 0.5 ypos 825 idle 'interface/RUS.webp' action [Language(None), Function(renpy.full_restart)] focus_mask True at lang

################################################################################

screen PowerBack():
    frame xalign 0.5 ypos 985 xsize 200:# background None:
        if '06:00' <= tm < '22:00':
            if current_room == house[5]:
                background 'interface laptop keys-bg-dayt'
            else:
                background 'interface laptop keys-bg-day'
        else:
            if current_room == house[5]:
                background 'interface laptop keys-bg-nightt'
            elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
                background 'interface laptop keys-bg-day'
            else:
                background 'interface laptop keys-bg-night'
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        hbox spacing 100:
            imagebutton:
                auto 'interface laptop back %s'
                action [Hide('Search'), SetVariable('at_comp', False), Jump('Laptop')] at power_zoom
            imagebutton:
                auto 'interface laptop power %s'
                action [Hide('Search'), SetVariable('at_comp', False), Jump('Waiting')] at power_zoom
    key 'K_ESCAPE' action [Hide('Search'), SetVariable('at_comp', False), Jump('Laptop')]
    key 'mouseup_3' action [Hide('Search'), SetVariable('at_comp', False), Jump('Laptop')]
    if not _in_replay:
        # key 'K_F5' action [SetVariable('number_quicksave', number_quicksave+1), NewSaveName(), QuickSave()]
        key 'K_F8' action QuickLoad()

screen PowerBack2():
    frame xalign 0.5 ypos 985 xsize 200:# background None:
        if '06:00' <= tm < '22:00':
            if current_room == house[5]:
                background 'interface laptop keys-bg-dayt'
            else:
                background 'interface laptop keys-bg-day'
        else:
            if current_room == house[5]:
                background 'interface laptop keys-bg-nightt'
            elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
                background 'interface laptop keys-bg-day'
            else:
                background 'interface laptop keys-bg-night'
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        hbox spacing 100:
            imagebutton:
                auto 'interface laptop back %s'
                action [Hide('Withdraw'), Hide('SEO'), Jump('open_site')] at power_zoom
            imagebutton:
                auto 'interface laptop power %s'
                action [Hide('Withdraw'), Hide('SEO'), Jump('Waiting')] at power_zoom
    key 'K_ESCAPE' action [Hide('Withdraw'), Hide('SEO'), Jump('open_site')]
    key 'mouseup_3' action [Hide('Withdraw'), Hide('SEO'), Jump('open_site')]
    if not _in_replay:
        # key 'K_F5' action [SetVariable('number_quicksave', number_quicksave+1), NewSaveName(), QuickSave()]
        key 'K_F8' action QuickLoad()

screen PowerBack3():
    frame xalign 0.5 ypos 985 xsize 200:# background None:
        if '06:00' <= tm < '22:00':
            if current_room == house[5]:
                background 'interface laptop keys-bg-dayt'
            else:
                background 'interface laptop keys-bg-day'
        else:
            if current_room == house[5]:
                background 'interface laptop keys-bg-nightt'
            elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
                background 'interface laptop keys-bg-day'
            else:
                background 'interface laptop keys-bg-night'
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        hbox spacing 100:
            imagebutton:
                auto 'interface laptop back %s'
                action [Hide('Withdraw'), Hide('Bank'), Jump('Laptop')] at power_zoom
            imagebutton:
                auto 'interface laptop power %s'
                action [Hide('Withdraw'), Hide('Bank'), Jump('Waiting')] at power_zoom
    key 'K_ESCAPE' action [Hide('Withdraw'), Hide('Bank'), Jump('Laptop')]
    key 'mouseup_3' action [Hide('Withdraw'), Hide('Bank'), Jump('Laptop')]
    if not _in_replay:
        # key 'K_F5' action [SetVariable('number_quicksave', number_quicksave+1), NewSaveName(), QuickSave()]
        key 'K_F8' action QuickLoad()

screen PowerButton():
    imagebutton:
        pos (935, 985) auto 'interface laptop power %s'
        action [Hide('Search'), Jump('Waiting')] at power_zoom
    key 'K_ESCAPE' action [Hide('Search'), Jump('Waiting')]
    key 'mouseup_3' action [Hide('Search'), Jump('Waiting')]
    if not _in_replay:
        # key 'K_F5' action [SetVariable('number_quicksave', number_quicksave+1), NewSaveName(), QuickSave()]
        key 'K_F8' action QuickLoad()

################################################################################
screen LaptopScreen():

    tag menu
    modal True

    use PowerButton
    use notify_check

    $ bookmarks = 2
    if dcv['buyfood'].stage == 1:
        $ bookmarks += 1
    if poss['cams'].stn == 3 and mgg.money >= 100:
        $ bookmarks += 1
    if poss['cams'].stn >= 4:
        $ bookmarks += 1
    if mgg.credit.level > 0:
        $ bookmarks += 1

    frame area(221, 93, 1475, 829) background None:
        viewport:
            xfill True
            ypos 30
            ysize 770
            mousewheel 'change'
            draggable True
            if bookmarks > 6:
                scrollbars 'vertical'

            vbox:
                xfill True
                spacing 30
                if len(search_theme) > 0:
                    imagebutton xalign .5 idle 'interface laptop search' action [Hide('PowerButton'), Show('Search')] focus_mask True
                else:
                    imagebutton xalign .5 idle 'interface laptop search' action Call('nothing_search') focus_mask True

                vpgrid cols 3 xalign .5 xsize 1260:
                    xspacing 50
                    yspacing 40

                    frame xysize(370, 295) background None:
                        imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop shop' action Jump('LaptopShop') at book_marks
                        text _("{b}ИНТЕРНЕТ-МАГАЗИН{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)]

                    frame xysize(370, 295) background None:
                        imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop courses' action Jump('courses_start') at book_marks
                        text _("{b}ОНЛАЙН-КУРСЫ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)]

                    if dcv['buyfood'].stage == 1:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop grocery' action Jump('buyfood') at book_marks
                            text _("{b}КУПИТЬ ПРОДУКТЫ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)]

                    if poss['cams'].stn == 3 and mgg.money >= 100:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop CreateSite' action Jump('create_site') at book_marks
                            text _("{b}ЗАНЯТЬСЯ СВОИМ САЙТОМ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5

                    if poss['cams'].stn >= 4:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop bb cam' action Jump('open_site') at book_marks
                            text _("{b}СВОЙ САЙТ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5

                    if mgg.credit.level > 0:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop online bank' action Show('Bank') at book_marks
                            text _("{b}CYBER-БАНК{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5


            if len(search_theme) > 0:
                frame  xpos 1055 ypos 25 background None:
                    add 'interface marker blue' at mark


screen LaptopDouble():
    tag menu
    modal True

    use PowerButton
    use notify_check

    $ bookmarks = 2
    if dcv['buyfood'].stage == 1:
        $ bookmarks += 1
    if poss['cams'].stn == 3 and mgg.money >= 100:
        $ bookmarks += 1
    if poss['cams'].stn >= 4:
        $ bookmarks += 1
    if mgg.credit.level > 0:
        $ bookmarks += 1

    frame area(221, 93, 1475, 829) background None:
        vbox: # деньги
            align(0.985, 0.015)
            text "$[mgg.money]" xalign(1.0) font 'hermes.ttf' size 48 drop_shadow[(2, 2)]
        viewport:
            xfill True
            ypos 30
            ysize 770
            mousewheel 'change'
            draggable True
            if bookmarks > 6:
                scrollbars 'vertical'

            vbox:
                xfill True
                spacing 30
                if len(search_theme) > 0:
                    imagebutton xalign .5 idle 'interface laptop search' action NullAction() focus_mask True
                else:
                    imagebutton xalign .5 idle 'interface laptop search' action NullAction() focus_mask True

                vpgrid cols 3 xalign .5 xsize 1260:
                    xspacing 50
                    yspacing 40

                    frame xysize(370, 295) background None:
                        imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop shop' action NullAction()
                        text _("{b}ИНТЕРНЕТ-МАГАЗИН{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)]

                    frame xysize(370, 295) background None:
                        imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop courses' action NullAction()
                        text _("{b}ОНЛАЙН-КУРСЫ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)]

                    if dcv['buyfood'].stage == 1:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop grocery' action NullAction()
                            text _("{b}КУПИТЬ ПРОДУКТЫ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)]

                    if poss['cams'].stn == 3 and mgg.money >= 100:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop CreateSite' action NullAction()
                            text _("{b}ЗАНЯТЬСЯ СВОИМ САЙТОМ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5

                    if poss['cams'].stn >= 4:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop bb cam' action NullAction()
                            text _("{b}СВОЙ САЙТ{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5

                    if mgg.credit.level > 0:
                        frame xysize(370, 295) background None:
                            imagebutton anchor (0.5, 0.5) pos (185, 115) idle 'interface laptop online bank' action NullAction()
                            text _("{b}CYBER-БАНК{/b}") xanchor 0.5 xpos 185 ypos 232 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5


################################################################################
screen Bank():
    tag menu2
    modal True
    use LaptopDouble
    use PowerBack3
    frame align(0.5, 0.42) xsize 1000:
        xmargin 0 ymargin 0 xpadding 50 ypadding 30
        vbox spacing 10:
            frame xysize(900, 300) background 'interface laptop banner bank'
            text _("ВЫГОДНЫЕ ЗАЙМЫ ИНТЕРНЕТ-ПРЕДПРИНИМАТЕЛЯМ") font 'trebucbd.ttf' color '#FFFFFF' size 28 xalign 0.5
            if mgg.credit.debt > 0:
                hbox xfill True:
                    if mgg.credit.fines:
                        $ _col = red
                    else:
                        $ _col = orange
                    text _("Задолженность: {color=[_col]}$[mgg.credit.debt]{/color}")
                    text _("[mgg.credit.left] дней на погашение") xalign 1.0
                if mgg.money >= mgg.credit.debt:
                    textbutton _("ПОГАСИТЬ ЗАДОЛЖЕННОСТЬ"):
                        action Function(mgg.credit_repay)
                        style 'green_button'
                if mgg.money > 50:
                    textbutton _("ПОГАСИТЬ ЧАСТЬ ДОЛГА"):
                        action Jump("return_part_loan")
                        style 'green_button'
                else:
                    textbutton _("ПОГАСИТЬ ЧАСТЬ ДОЛГА"):
                        action NullAction()
                        style 'red_button'
            else:
                textbutton _("ВЗЯТЬ КРЕДИТ"):
                    action Jump('getting_load')
                    style 'green_button'

style green_button:
    idle_background Frame('interface button green', 12, 12)
    hover_background Frame('interface button green', 12, 12)
    xalign .5
    xpadding 30 ypadding 10 ymargin 5
style green_button_text:
    font 'trebuc.ttf'
    text_align 0.5
    size 30
    idle_color '#000000'
    hover_color '#FFFFFF'
style red_button:
    idle_background Frame('interface button red', 12, 12)
    hover_background Frame('interface button red', 12, 12)
    xalign .5
    xpadding 30 ypadding 10 ymargin 5
style red_button_text:
    font 'trebuc.ttf'
    text_align 0.5
    size 30
    idle_color '#000000'
    hover_color '#FFFFFF'

################################################################################
screen Search():
    modal True
    use PowerBack
    style_prefix 'search'
    frame area(635, 150, 694, 450) background '#FFFFFF':
        vbox:
            spacing 10
            text _("Что будем искать?") color '#000000'
            hbox spacing 5:
                frame background None:
                    ysize 340
                    xfill True
                    viewport spacing 0 draggable True mousewheel True id 'vp_choice':
                        ysize 330
                        vbox xsize 675 spacing 0:
                            $yy = 0
                            for i in search_theme:
                                $yy+=1
                                button action [Hide('Search'), Jump(i[1])] style 'search_but':
                                    textbutton i[0] action [Hide('Search'), Jump(i[1])] yalign .0
                                key str(yy) action [Hide('Search'), Jump(i[1])]
                    vbar value YScrollValue('vp_choice') style 'search_vscroll'

style search_vscroll is vscrollbar:
    unscrollable 'hide'
style search_but:
    xpadding 0 ypadding 0 xmargin 0 ymargin 0
    xsize 675
    foreground 'interface marker black'
style search_button:
    xsize 675
    xpadding 30
    hover_background 'gui/button/search_hover_background.png'
style search_button_text:
    idle_color '#000000'
    hover_color '#ffbe00'

################################################################################

screen OnlineShop():
    tag menu
    modal True
    use PowerBack
    default CurCat = 0
    frame area(221, 93, 1475, 829) background None:
        hbox:
            frame xsize 295 yfill True background None:
                xpadding 15 ypadding 15
                ## список категорий
                style_prefix 'cat'
                vbox:
                    for i in ShopCat:
                        button background None action SetScreenVariable('CurCat', i) xsize 390 style 'cat_but':
                            textbutton ShopCat[i] action SetScreenVariable('CurCat', i) selected CurCat == i

            frame xsize 1175 yfill True background None:
                xpadding 10 ypadding 15 #xmargin 0 ymargin 15
                ## список товаров категории
                style_prefix 'goods'
                $ items_in_cat = 0

                hbox xsize 1135 spacing 5:
                    viewport mousewheel 'change' draggable True id 'vp1':
                        vbox spacing 15:
                            for i in items:
                                if items[i].InShop and items[i].category == CurCat:
                                    $ items_in_cat += 1
                                    frame xfill True background Frame('interface items-shop bg2', 10, 10):
                                        xpadding 10 ypadding 10 xmargin 5 ymargin 5
                                        hbox xsize 1120 spacing 15:
                                            add 'interface items-shop '+items[i].img
                                            # frame xfill True:
                                            vbox spacing 5:
                                                frame xpos 50 xsize 400 background None:
                                                    text items[i].name style 'item_header'
                                                frame xsize 700 background None:
                                                    text items[i].desc color gui.accent_color
                                                if items[i].bought:
                                                    textbutton _("{i}{b}КУПЛЕНО{/b}{/i}") style 'buy_button':
                                                        idle_background Frame('interface button green', 12, 12)
                                                        hover_background Frame('interface button green', 12, 12)
                                                        text_idle_color gui.hover_color
                                                        text_hover_color gui.hover_color
                                                        action NullAction()
                                                elif items[i].have and not all([kol_cream < 7, i == 'solar']):
                                                    textbutton "{i}{b}$ "+str(items[i].price)+"{/b}{/i}" style 'buy_button':
                                                        idle_background Frame('interface button gray', 12, 12)
                                                        hover_background Frame('interface button gray', 12, 12)
                                                        text_hover_color '#000000'
                                                        action NullAction()
                                                elif items[i].price > mgg.money:
                                                    textbutton "{i}{b}$ "+str(items[i].price)+"{/b}{/i}" style 'buy_button':
                                                        idle_background Frame('interface button red', 12, 12)
                                                        hover_background Frame('interface button red', 12, 12)
                                                        text_hover_color '#000000'
                                                        action NullAction()
                                                else:
                                                    textbutton "{i}{b}$ "+str(items[i].price)+"{/b}{/i}" style 'buy_button':
                                                        idle_background Frame('interface button orange', 12, 12)
                                                        hover_background Frame('interface button green', 12, 12)
                                                        # action [AddToSet(purchased_items, items[i]), Function(items[i].buy)]
                                                        action Function(items[i].buy)

                    vbar value YScrollValue('vp1') style 'shop_vscroll'

style shop_vscroll is vscrollbar:
    unscrollable 'hide'
style cat_but:
    xpadding 0 ypadding 0 xmargin 0 ymargin 0
    xsize 270
    foreground 'interface marker'
style cat_button:
    xsize 270
    xpadding 30
style cat_button_text is default:
    font 'trebucbd.ttf'
    # xpos 30
    yalign .5
    size 28
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color
style item_header:
    font 'trebucbd.ttf'
    color '#FFFFFF'
    size 28
style price:
    font 'trebucbd.ttf'
    color '#000000'
    size 36
style buy_button:
    xalign 1.0
    xpadding 30
    ypadding 10
    ymargin 5
style buy_button_text:
    font 'trebuc.ttf'
    min_width 100
    text_align 0.5
    size 30
    idle_color '#000000'
    hover_color '#FFFFFF'

################################################################################
screen OnlineCources():
    tag menu
    modal True
    use PowerBack
    # default CurCource = online_cources[0]
    frame area(221, 93, 1475, 829) background Frame('interface items bg', 10, 10):
        vbox:
            hbox:
                xfill True
                label _("ОНЛАЙН-КУРСЫ") xalign 0.02 text_color gui.accent_color text_size 36 text_font 'hermes.ttf'
                label "$[mgg.money]" xalign 0.98 text_size 36 text_font 'hermes.ttf' text_drop_shadow[(2, 2)] text_color gui.text_color
            hbox:
                frame xsize 395 yfill True background None:
                    xpadding 35 ypadding 15
                    ## список курсов
                    style_prefix 'cat'
                    vbox:
                        for i in online_cources:
                            button background None action SetVariable('CurCource', i) xsize 390 style 'cat_but':
                                textbutton i.name action SetVariable('CurCource', i) selected CurCource == i

                frame xsize 1075 yfill True background None:
                    xpadding 10 ypadding 0 #xmargin 0 ymargin 15
                    vbox spacing 10:
                        if CurCource.current == len(CurCource.cources): # CurCource.cources[CurCource.current].less == CurCource.cources[CurCource.current].total:
                            frame xfill True background None:
                                add 'interface laptop '+CurCource.img+'-header-'+str(CurCource.current-1) xalign 0.5 size(900,450)
                            label _("Вы прошли все доступные курсы и занятия из этой категории. Возможно, новые уроки появятся в следующей версии игры."):
                                xsize 900 xalign 0.5 text_size 24
                                text_color gui.accent_color
                        else:
                            frame xfill True background None:
                                add 'interface laptop '+CurCource.img+'-header-'+str(CurCource.current) xalign 0.5 size(900,450)
                            $ text2 = CurCource.cources[CurCource.current].total
                            label CurCource.cources[CurCource.current].header:
                                xalign 0.5 text_xalign 0.5 text_size 36
                                text_text_align 0.5
                                text_font 'hermes.ttf' text_color gui.text_color
                            if CurCource.cources[CurCource.current].bought:
                                label _("Вы уже оплатили этот курс и можете в любой момент включить следующий доступный видеоурок."):
                                    xsize 900 xalign 0.5 text_size 26
                                    text_color gui.accent_color
                                $ text1 = CurCource.cources[CurCource.current].less + 1
                                label _("Занятие [text1] из [text2]"):
                                    xsize 900 xalign 0.5 text_size 28
                                    text_color gui.text_color
                                if ItsTime(cooldown['learn']):  # таймаут прошел, можно учится дальше
                                    textbutton _("{i}{b}НАЧАТЬ ПРОСМОТР ВИДЕОУРОКА{/b}{/i}") style 'buy_button2':
                                        idle_background Frame('interface button green', 12, 12)
                                        hover_background Frame('interface button green', 12, 12)
                                        action Jump('ViewLesson')
                                else:  # таймаут ещё не кончился
                                    textbutton _("{i}{b}ВЫ УЧИЛИСЬ СОВСЕМ НЕДАВНО. СДЕЛАЙТЕ ПЕРЕРЫВ!{/b}{/i}") style 'buy_button2':
                                        idle_background Frame('interface button orange', 12, 12)
                                        hover_background Frame('interface button orange', 12, 12)
                                        text_hover_color '#000000'
                                        action NullAction()
                            else:
                                label CurCource.cources[CurCource.current].desc:
                                    xsize 900 xalign 0.5 text_size 26
                                    text_color gui.accent_color

                                label _("Количество занятий: [text2]"):
                                    xsize 900 xalign 0.5 text_size 28
                                    text_color gui.text_color

                                $ price = CurCource.cources[CurCource.current].price
                                if price > mgg.money:
                                    textbutton _("{i}{b}ПРИОБРЕСТИ ЭТОТ КУРС ЗА: $[price]{/b}{/i}") style 'buy_button2':
                                        idle_background Frame('interface button red', 12, 12)
                                        hover_background Frame('interface button red', 12, 12)
                                        text_hover_color '#000000'
                                        action NullAction()
                                else:
                                    textbutton _("{i}{b}ПРИОБРЕСТИ ЭТОТ КУРС ЗА: $[price]{/b}{/i}") style 'buy_button2':
                                        idle_background Frame('interface button green', 12, 12)
                                        hover_background Frame('interface button green', 12, 12)
                                        action Function(CurCource.cources[CurCource.current].buy)

style buy_button2:
    xalign 0.5
    xpadding 30
    ypadding 10
    ymargin 5
style buy_button2_text:
    font 'trebuc.ttf'
    min_width 600
    text_align 0.5
    size 30
    idle_color '#000000'
    hover_color '#FFFFFF'

################################################################################

screen Withdraw():
    tag menu2
    modal True
    use PowerBack2
    $ paid = int(mgg.account)
    frame align(0.5, 0.5) xsize 1000:
        xmargin 0 ymargin 0 xpadding 50 ypadding 30
        vbox spacing 10:
            frame xysize(900, 300) background 'interface laptop revenue views'
            text _("ДОХОД ОТ ПРОСМОТРОВ") font 'trebucbd.ttf' color '#FFFFFF' size 28 xalign 0.5
            text _("Каждое посещение страниц вашего сайта приносит небольшой доход. Увеличивайте аудиторию и зарабатывайте на рекламе!\n\nМинимальная сумма единоразового снятия: $100.") color gui.accent_color
            text _("На вашем счете $[paid]") color '#FFFFFF'
            if paid >= 100:
                textbutton _("Забрать $[paid]"):
                    idle_background Frame('interface button green', 12, 12)
                    hover_background Frame('interface button green', 12, 12)
                    xalign .5
                    xpadding 30 ypadding 10 ymargin 5
                    text_font 'trebuc.ttf'
                    text_align 0.5
                    text_size 30
                    text_idle_color '#000000'
                    text_hover_color '#FFFFFF'

                    action Function(mgg.withdraw)
            else:
                textbutton _("НЕДОСТАТОЧНАЯ СУММА ДЛЯ СНЯТИЯ"):
                    idle_background Frame('interface button red', 12, 12)
                    hover_background Frame('interface button red', 12, 12)
                    xalign .5
                    xpadding 30 ypadding 10 ymargin 5
                    text_font 'trebuc.ttf'
                    text_align 0.5
                    text_size 30
                    text_idle_color '#000000'
                    text_hover_color '#FFFFFF'
                    action NullAction()

screen SEO():
    tag menu2
    modal True
    use notify_check
    use PowerBack2
    frame align(0.5, 0.5) xsize 1000:
        xmargin 0 ymargin 0 xpadding 50 ypadding 30
        vbox spacing 10:
            frame xysize(900, 300) background 'interface laptop banner adverticing'
            text _("СЕТЬ БАННЕРНОЙ РЕКЛАМЫ") font 'trebucbd.ttf' color '#FFFFFF' size 28 xalign 0.5
            text _("Уникальное предложение только для вас! Наша баннерная сеть предназначена для клиентов с особыми запросами и готова донести вашу рекламу до целевой аудитории.\n\nЗа каждый пакет, который вы оплачиваете сейчас, мы гарантируем 10000 показов рекламы вашего сайта в ближайшем будущем!") color gui.accent_color
            if mgg.money >= 50:
                textbutton _("КУПИТЬ ПАКЕТ РЕКЛАМЫ ЗА $50"):
                    action Function(mgg.buy_promoution)
                    idle_background Frame('interface button green', 12, 12)
                    hover_background Frame('interface button green', 12, 12)
                    xalign .5
                    xpadding 30 ypadding 10 ymargin 5
                    text_font 'trebuc.ttf'
                    text_align 0.5
                    text_size 30
                    text_idle_color '#000000'
                    text_hover_color '#FFFFFF'
            else:
                textbutton _("КУПИТЬ ПАКЕТ РЕКЛАМЫ ЗА $50"):
                    action NullAction()
                    idle_background Frame('interface button red', 12, 12)
                    hover_background Frame('interface button red', 12, 12)
                    xalign .5
                    xpadding 30 ypadding 10 ymargin 5
                    text_font 'trebuc.ttf'
                    text_align 0.5
                    text_size 30
                    text_idle_color '#000000'
                    text_hover_color '#FFFFFF'

screen MySite():
    tag menu
    modal True
    use notify_check
    use PowerBack
    if (len(cam_list) >= 6) and(len(cam_list) % 3 != 0):
        $ dobavka = 3 - (len(cam_list) % 3)
    elif len(cam_list) < 6:
        $ dobavka = 6 - len(cam_list)
    else:
        $ dobavka = 0

    default t_loc    = Tooltip("")
    default t_public = Tooltip("")
    default t_total  = Tooltip("")
    default t_today  = Tooltip("")


    frame area(221, 93, 1475, 829) background None:
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        vbox: # деньги
            align(0.98, 0.03)
            text "$[mgg.money]" xalign(1.0) font 'hermes.ttf' size 48 drop_shadow[(2, 2)]
        frame pos(0, 100) xysize (1475, 585) background None:
            xmargin 0 ymargin 0 ypadding 25
            viewport:
                xsize 1230
                xalign .5
                yfill True
                if len(cam_list) > 6:
                    mousewheel 'change'
                    draggable True
                    scrollbars 'vertical'
                    if view_cam is not None and view_cam[4] > 5:  # зададим стартовое положение
                        yinitial 540
                frame xpadding 27 background None:
                    vpgrid cols 3:
                        xspacing 30
                        yspacing 30
                        mousewheel 'change'
                        draggable True

                        for cam in cam_list:
                            frame area(0, 0, 370, 240) background None:
                                xmargin 0 ymargin 0 xpadding 0 ypadding 0
                                button xysize(362, 235) align(0.5, 0.5) background None:
                                    action [SetVariable('at_comp', True), SetVariable('view_cam', cam), Jump('Waiting')]
                                    xmargin 0 ymargin 0 xpadding 0 ypadding 0
                                    if '06:00' <= tm < '11:00':
                                        add 'location '+str(cam[3])+' '+cam[0].id.replace('_', '')+' cam-morning-'+str(cam[2])
                                    elif '11:00' <= tm < '19:00':
                                        add 'location '+str(cam[3])+' '+cam[0].id.replace('_', '')+' cam-day-'+str(cam[2])
                                    elif '19:00' <= tm < '22:00':
                                        add 'location '+str(cam[3])+' '+cam[0].id.replace('_', '')+' cam-evening-'+str(cam[2])
                                    else:
                                        if len(cam[0].cur_char) > 0 and chars[cam[0].cur_char[0]].plan_name not in ['sleep', 'sleep2']:
                                            add 'location '+str(cam[3])+' '+cam[0].id.replace('_', '')+' cam-evening-'+str(cam[2])
                                        else:
                                            add 'location '+str(cam[3])+' '+cam[0].id.replace('_', '')+' cam-night-'+str(cam[2])
                                    if len(cam[0].cur_char) > 0 or cam[0] == current_room:
                                        add 'interface laptop cam act'
                                    else:
                                        add 'interface laptop cam noact'
                                    hovered [
                                        t_loc.Action(cam[0].cam_name),
                                        t_public.Action(str(int(cam[1].public))),
                                        t_total.Action("$"+str(int(cam[1].total))),
                                        t_today.Action("$"+str(int(cam[1].today)))
                                        ]

                        # дополним пустыми местами
                        for i in range(dobavka):
                            frame area(0, 0, 370, 240) background None:
                                xmargin 0 ymargin 0 xpadding 0 ypadding 0
                                frame xysize(362, 235) align(0.5, 0.5) background Frame('interface items bg', 10, 10)

        frame ysize 145 xfill True yalign 1.0 background None:
            xmargin 0 ymargin 0 xpadding 0 ypadding 0
            button xysize(380, 144) xalign 0.0 background None action Show('SEO'):
                imagebutton anchor (0.5, 0.5) xalign 0.5 yalign 0.5 idle 'interface laptop seo' action Show('SEO') at book_marks
                text _("{b}РЕКЛАМА{/b}") xanchor 0.5 xalign 0.5 yalign 0.98 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5
            button xysize(380, 144) xalign 1.0 background None action Show('Withdraw'):
                imagebutton anchor (0.5, 0.5) xalign 0.5 yalign 0.5 idle 'interface laptop withdraw' action Show('Withdraw') at book_marks
                text _("{b}ВЫВОД СРЕДСТВ{/b}") xanchor 0.5 xalign 0.5 yalign 0.98 color '#FFFFFF' drop_shadow[(2, 2)] text_align 0.5
            if t_loc.value != "":
                frame ysize 170 xpos 380 xsize 665 background None:
                    hbox xalign 0.5 spacing 50:
                        vbox:
                            text _("Расположение:") style 'text1'
                            text _("Зрителей:") style 'text1'
                            text _("Общий доход:") style 'text1'
                            text _("Доход сегодня:") style 'text1'
                        vbox:
                            text t_loc.value style 'text2'
                            text t_public.value style 'text2'
                            text t_total.value style 'text2'
                            text t_today.value style 'text2'

style text1:
    size 24
    color gui.accent_color

style text2:
    size 24
    bold True


################################################################################
screen room_navigation():

    tag menu
    modal True

    use notify_check

    if not _in_replay:
        key 'K_F5' action [SetVariable('number_quicksave', number_quicksave+1), NewSaveName(), QuickSave()]
        key 'K_F8' action QuickLoad()
    if _preferences.language is None:
        key 'l' action Language('english')
        key 'д' action Language('english')
    else:
        key 'l' action Language(None)
        key 'д' action Language(None)
    key 'mouseup_3' action [Cursor(None), ShowMenu('save')]
    key 'K_ESCAPE' action [Cursor(None), ShowMenu('save')]
    key 'K_MENU' action [Cursor(None), ShowMenu('save')]

    $ renpy.block_rollback()

    $  i = 0
    $ public = 0
    for cam in current_room.cams:
        $ public += cam.public
    $ public = int(public)

    if persone_button1 and exist_btn_image():
        imagebutton idle persone_button1:
            focus_mask True
            if have_dialog():
                hovered Cursor('talk')
                unhovered Cursor(None)
                action [Cursor(None), Jump('StartDialog')]
            else:
                action NullAction()

    $ wait = 60 - int(tm[-2:])
    key 'K_SPACE' action [Cursor(None), Hide('wait_navigation'), SetVariable('spent_time', wait), Jump('Waiting')]
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
            $ char = ''
            for ch in room.cur_char:
                $ char += ch+', '
            if len(char) !=0:
                $ char = ' ('+char[:-2]+')'

            button xysize (126, 190) action [Hide('wait_navigation'), SetVariable('prev_room', current_room), SetVariable('current_room', room), Jump('AfterWaiting')]:
                vbox xsize 126 spacing 0:
                    frame xysize (126, 140) background None:
                        imagebutton align (0.5, 0.0) idle room.icon selected_idle room.icon + ' a' selected_hover room.icon + ' a':
                                    selected room == current_room focus_mask True at middle_zoom
                                    action [Hide('wait_navigation'), SetVariable('prev_room', current_room), SetVariable('current_room', room), Jump('AfterWaiting')]
                        if room != current_room:
                            # вывод миниатюр персонажей внизу миниатюры локации
                            if len(room.cur_char) > 0:
                                hbox ypos 73 xalign 0.5 spacing - 30:
                                    for char in room.cur_char:
                                        if char == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                            imagebutton idle chars[char].pref+' icon a' focus_mask True at small_face:
                                                action [Hide('wait_navigation'), SetVariable('prev_room', current_room), SetVariable('current_room', room), Jump('AfterWaiting')]
                                        else:
                                            imagebutton idle chars[char].pref+' icon' focus_mask True at small_face:
                                                action [Hide('wait_navigation'), SetVariable('prev_room', current_room), SetVariable('current_room', room), Jump('AfterWaiting')]
                        else:
                            # если же это текущая локация - вывод над миниатюрой
                            # более крупных значков персонажей. положение зависит от количества
                            if len(current_room.cur_char) == 1:
                                if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                    imagebutton ypos -120 xalign 0.5 idle chars[current_room.cur_char[0]].pref+' icon a' focus_mask True:
                                                action NullAction() at middle_face
                                else:
                                    imagebutton ypos -120 xalign 0.5 idle chars[current_room.cur_char[0]].pref+' icon' focus_mask True:
                                                action NullAction() at middle_face
                            elif len(current_room.cur_char) == 2:
                                # Если в локации два персонажа, дополнительно проверяется не является ли тек.локация крайней слева
                                if current_room == current_location[0]:
                                    # и если да, то первая миниатюра отображается не слева, а над локацией
                                    if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                        imagebutton ypos -120 xalign 0.5 idle chars[current_room.cur_char[0]].pref+' icon a':
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -120 xalign 0.5 idle chars[current_room.cur_char[0]].pref+' icon':
                                                    focus_mask True action NullAction() at middle_face
                                    if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                        imagebutton ypos -100 xpos 63 idle chars[current_room.cur_char[1]].pref+' icon a':
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -100 xpos 63 idle chars[current_room.cur_char[1]].pref+' icon':
                                                    focus_mask True action NullAction() at middle_face
                                else:
                                    if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                        imagebutton ypos -100 xpos -63 idle chars[current_room.cur_char[0]].pref+' icon a':
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -100 xpos -63 idle chars[current_room.cur_char[0]].pref+' icon':
                                                    focus_mask True action NullAction() at middle_face
                                    if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                        imagebutton ypos -100 xpos 63 idle chars[current_room.cur_char[1]].pref+' icon a':
                                                    focus_mask True action NullAction() at middle_face
                                    else:
                                        imagebutton ypos -100 xpos 63 idle chars[current_room.cur_char[1]].pref+' icon':
                                                    focus_mask True action NullAction() at middle_face
                            elif len(current_room.cur_char) == 3:
                                if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                    imagebutton ypos -100 xpos -63 idle chars[current_room.cur_char[0]].pref+' icon a':
                                                focus_mask True action NullAction() at middle_face
                                else:
                                    imagebutton ypos -100 xpos -63 idle chars[current_room.cur_char[0]].pref+' icon':
                                                focus_mask True action NullAction() at middle_face
                                if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                    imagebutton ypos -120 align (0.5, 0.0) idle chars[current_room.cur_char[1]].pref+' icon a':
                                                focus_mask True action NullAction() at middle_face
                                else:
                                    imagebutton ypos -120 align (0.5, 0.0) idle chars[current_room.cur_char[1]].pref+' icon':
                                                focus_mask True action NullAction() at middle_face
                                if current_room.cur_char[0] == 'alice' and (tm < '09:00' or tm >= '20:00'):
                                    imagebutton ypos -100 xpos 63 idle chars[current_room.cur_char[2]].pref+' icon':
                                                focus_mask True action NullAction() at middle_face
                                else:
                                    imagebutton ypos -100 xpos 63 idle chars[current_room.cur_char[2]].pref+' icon':
                                                focus_mask True action NullAction() at middle_face
                            elif len(current_room.cur_char) == 4:
                                pass
                    text room.name font 'trebucbd.ttf' size 18 drop_shadow[(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
            key str(i) action [Hide('wait_navigation'), SetVariable('prev_room', current_room), SetVariable('current_room', room), Jump('AfterWaiting')]

    hbox:
        align(.99, .99)  # правый нижний угол
        # располагаем клавиши действий

        for id in ListButton:  # добавим последовательно все доступные действия (ключи берем из списка кнопок)
            $ act = AvailableActions[id] # а сами кнопки из словаря
            if act.active and act.enabled:
                button xysize (126, 190) action [Hide('wait_navigation'), Jump(act.label)]: # Поговорить
                    vbox xsize 126 spacing 0:
                        frame xysize (126, 140) background None:
                            imagebutton idle act.icon align (0.5, 0.0) focus_mask True:
                                        action [Hide('wait_navigation'), Jump(act.label)] at middle_zoom
                        text act.sing font 'trebucbd.ttf' size 18 drop_shadow[(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2

        button xysize (136, 190) action [Hide('wait_navigation'), SetVariable('spent_time', wait), Jump('Waiting')]: # ждать час
            vbox xsize 136 spacing 0:
                frame xysize (136, 140) background None:
                    imagebutton idle 'interface wait 60' hover 'interface wait 60 a':# hovered Show('wait_navigation'):
                                align (0.5, 0.0) focus_mask True action [Hide('wait_navigation'), SetVariable('spent_time', wait), Jump('Waiting')] at middle_wait
                text _("ЖДАТЬ") font 'trebucbd.ttf' size 18 drop_shadow[(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2

    vbox:  # Время и день недели
        align(0.5, 0.01)
        text tm xalign(0.5) font 'hermes.ttf' size 60 drop_shadow[(2, 2)]
        text weekdays[(day+2) % 7][1] xalign(0.5) font 'hermes.ttf' size 24 drop_shadow[(2, 2)] line_leading -16

    vbox: # деньги и зрители
        align(0.99, 0.01)
        text "$[mgg.money]" xalign(1.0) font 'hermes.ttf' size 60 drop_shadow[(2, 2)]
        if len(current_room.cams) > 0:
            text _("Зрителей: [public]") xalign(1.0) font 'hermes.ttf' size 24 drop_shadow[(2, 2)] line_leading -16

    $ kol = 0

    for ps in poss:
        if poss[ps].stn >= 0: # количество открытых возможностей
            $ kol += 1

    hbox:  # верхнее меню
        align(0.01, 0.01)
        spacing 2
        imagebutton idle 'interface menu userinfo' focus_mask True action [Hide('wait_navigation'), Show('menu_userinfo')]:
            if renpy.variant('small'):
                at small_menu_mobile
            else:
                at small_menu
        imagebutton idle 'interface menu inventory' focus_mask True action [Hide('wait_navigation'), Show('menu_inventory')]:
            if renpy.variant('small'):
                at small_menu_mobile
            else:
                at small_menu
        imagebutton idle 'interface menu opportunity' focus_mask True:
            if kol > 0:
                action [Hide('wait_navigation'), Show('menu_opportunity')]
                if renpy.variant('small'):
                    at small_menu_mobile
                else:
                    at small_menu
            else:
                action NullAction()
                if renpy.variant('small'):
                    at disable_menu_mobile
                else:
                    at disable_menu
        imagebutton idle 'interface menu help' focus_mask True action [Hide('wait_navigation'), Show('menu_my_help')]:
            if renpy.variant('small'):
                at small_menu_mobile
            else:
                at small_menu
        if renpy.loadable('extra/extra.webp'):
            imagebutton idle 'extra/extra.webp' focus_mask True action [Hide('wait_navigation'), Show('menu_gallery')]:
                if renpy.variant('small'):
                    at small_menu_mobile
                else:
                    at small_menu
        imagebutton idle 'interface menu main' focus_mask True action ShowMenu('save'):
            if renpy.variant('small'):
                at small_menu_mobile
            else:
                at small_menu
        imagebutton idle 'interface menu patreon' focus_mask True action [Hide('wait_navigation'), OpenURL('https://www.patreon.com/aleksey90artimages')]:
            if renpy.variant('small'):
                at small_menu_mobile
            else:
                at small_menu


screen wait_navigation(): # дополнительные кнопки для ожидания в 10 и 30 минут
    frame align(.99, .99) xysize(123, 395) background None:
        vbox:
            spacing 5
            imagebutton idle 'interface wait 10' focus_mask True action [Hide('wait_navigation'), SetVariable('spent_time', 10), Jump('Waiting')] at small_zoom
            imagebutton idle 'interface wait 30' focus_mask True action [Hide('wait_navigation'), SetVariable('spent_time', 30), Jump('Waiting')] at small_zoom
    timer 2.0 action Hide('wait_navigation')

################################################################################
screen menu_my_help():
    tag menu
    style_prefix 'my_help'

    add 'interface phon'
    frame area(150, 95, 350, 50) background None:
        text _("ПОЛЕЗНОЕ") color gui.accent_color size 28 font 'hermes.ttf'
    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
        if not renpy.variant('small'):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_var_small

    default CurHP = 0

    hbox pos (300, 180) spacing 30:
        frame xsize 250 ysize 850 background None:
            hbox:
                viewport mousewheel 'change' draggable True id 'vp1':
                    vbox spacing 5:
                        for i in range(len(helps)):
                            button background None action SetScreenVariable('CurHP', i) xsize 240:
                                xpadding 0 ypadding 0 xmargin 0 ymargin 0
                                textbutton helps[i].id action SetScreenVariable('CurHP', i) selected CurHP == i
                                foreground 'interface marker'
                vbar value YScrollValue('vp1') style 'hp_vscroll'
        frame area (0, 0, 1040, 850) background None:
            vbox spacing 20:
                frame xsize 1030 xalign 0.5 background None:
                    text helps[CurHP].name size 30 font 'hermes.ttf' xalign 0.5
                frame xsize 1040 xalign 0.5 background None:
                    hbox:
                        viewport mousewheel 'change' draggable True id 'vp2':
                            vbox spacing 30:
                                text helps[CurHP].desc size 24  color gui.accent_color
                        vbar value YScrollValue('vp2') style 'hp_vscroll'

    key 'K_ESCAPE' action Jump('AfterWaiting')
    key 'mouseup_3' action Jump('AfterWaiting')

style my_help_button_text is default:
    font 'trebucbd.ttf'
    xpos 30
    yalign .0
    size 28
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color

style hp_vscroll is vscrollbar:
    unscrollable 'hide'


################################################################################
screen menu_opportunity():

    tag menu
    style_prefix 'opportunity'

    $ kol = 0
    $ all = len(poss) # Общее количество введенных в игру 'возможностей'
    $ lst_stage = []

    for ps in poss:
        if poss[ps].stn >= 0: # количество открытых возможностей
            $ kol += 1
            if CurPoss == '':
                $ CurPoss = ps

    if CurPoss != '':
        default view_stage = poss[CurPoss].stn
        for i, st in enumerate(poss[CurPoss].stages):
            if st.used:
                $ lst_stage.append(i)


    add 'interface phon'
    frame area(150, 95, 350, 50) background None:
        text _("ВОЗМОЖНОСТИ ([kol] / [all])") color gui.accent_color size 28 font 'hermes.ttf'
    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
        if not renpy.variant('small'):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_var_small


    hbox pos (150, 150) spacing 30:
        frame  ypos 25 xsize 400 ysize 850 background None:
            hbox:
                viewport mousewheel 'change' draggable True id 'vp1':
                    vbox spacing 5:
                        for ps in poss:
                            if poss[ps].stn >= 0:
                                if CurPoss == '':
                                    $ CurPoss = ps
                                    $ view_stage = poss[ps].stn
                                button background None action [SetVariable('CurPoss', ps), SetScreenVariable('view_stage', poss[ps].stn)] xsize 390:
                                    xpadding 0 ypadding 0 xmargin 0 ymargin 0
                                    textbutton poss[ps].name action [SetVariable('CurPoss', ps), SetScreenVariable('view_stage', poss[ps].stn)] selected CurPoss == ps
                                    foreground 'interface marker'
                vbar value YScrollValue('vp1') style 'poss_vscroll'
        if CurPoss != '':
            frame area (0, 30, 1190, 850) background None:
                vbox spacing 20:
                    frame xsize 800 ysize 400 pos (195, 0) background None:
                        if poss[CurPoss].stages[view_stage].image != '':
                            add poss[CurPoss].stages[view_stage].image
                    frame xsize 1180 xalign 0.5 background None:
                        text poss[CurPoss].name size 30 font 'hermes.ttf' xalign 0.5
                    frame area (0, 0, 1190, 400) background None:
                        hbox:
                            viewport mousewheel 'change' draggable True id 'vp2':
                                vbox spacing 30:
                                    text poss[CurPoss].stages[view_stage].desc size 24  color gui.accent_color
                                    text poss[CurPoss].stages[view_stage].ps size 28
                            vbar value YScrollValue('vp2') style 'poss_vscroll'
    if len(lst_stage) > 1:
        imagebutton pos (690, 360) auto 'interface prev %s':
            focus_mask True
            sensitive view_stage > min(lst_stage)
            action SetScreenVariable('view_stage', lst_stage[lst_stage.index(view_stage)-1] if lst_stage.index(view_stage) >= 0 else lst_stage[0])
        imagebutton pos (1570, 360) auto 'interface next %s':
            focus_mask True
            sensitive view_stage < max(lst_stage)
            action SetScreenVariable('view_stage', lst_stage[lst_stage.index(view_stage)+1] if lst_stage.index(view_stage)<len(lst_stage)-1 else lst_stage[len(lst_stage)-1])

    key 'K_ESCAPE' action Jump('AfterWaiting')
    key 'mouseup_3' action Jump('AfterWaiting')

style opportunity_button_text is default:
    font 'trebucbd.ttf'
    xpos 30
    yalign .0
    size 28
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color

style poss_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

################################################################################
screen menu_inventory():

    tag menu

    add 'interface phon2'
    style_prefix 'inventory'
    frame area(150, 95, 350, 50) background None:
        text _("ВЕЩИ") color gui.accent_color size 28 font 'hermes.ttf'

    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
        if not renpy.variant('small'):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_var_small

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
                    scrollbars 'vertical'

                if tabrows < 3:
                    $ tabrows = 3
                hbox:
                    spacing 2
                    for cur_col in range(5):
                        vbox:
                            spacing 4
                            for id in items_list[cur_col]:
                                $ im_name = 'interface/items/' + items[id].img + '.webp'
                                if items[id].cells == 2:
                                    frame area(0, 0, 286, 456) background 'interface items bg2':
                                        imagebutton align (0.5, 0.5) idle im.Scale(im.MatrixColor(im_name, im.matrix.desaturate()), 224, 360) hover 'interface items '+items[id].img:
                                            action NullAction()
                                            hovered [tl.Action(items[id].name), tdesc.Action(items[id].desc)]
                                else:
                                    frame area(0, 0, 286, 226) background 'interface items bg':
                                        imagebutton align (0.5, 0.5) idle im.Scale(im.MatrixColor(im_name, im.matrix.desaturate()), 252, 198) hover 'interface items '+items[id].img:
                                            action NullAction()
                                            hovered [tl.Action(items[id].name), tdesc.Action(items[id].desc)]

                            $ addcells = tabrows - listrows[cur_col]
                            if addcells > 0:
                                for i in range(addcells):
                                    frame area(0, 0, 286, 226) background 'interface items bg':
                                        button align (0.5, 0.5) action NullAction():
                                            hovered [tl.Action(''), tdesc.Action(desc)]


        frame area(200, 0, 1220, 50) background None:
            text tl.value xalign 0.5 size 28 font 'hermes.ttf'  color gui.text_color

        frame area(300, 0, 1020, 180) background None:
            text tdesc.value xalign 0.5 size gui.text_size font gui.text_font color gui.accent_color

    key 'K_ESCAPE' action Jump('AfterWaiting')
    key 'mouseup_3' action Jump('AfterWaiting')

################################################################################
screen menu_userinfo():

    tag menu
    add 'interface phon'
    style_prefix 'userinfo'

    frame area(150, 95, 350, 50) background None:
        text _("ПЕРСОНАЖИ") color gui.accent_color size 28 font 'hermes.ttf'

    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
        if not renpy.variant('small'):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_var_small

    hbox pos (150, 150) spacing 30:
        hbox ypos 25 xsize 190 spacing 5:
            viewport mousewheel 'change' draggable True id 'vp':
                vbox spacing 5:
                    button background None  action SetVariable('CurChar', 'max') xsize 180:
                        # xpadding 0 ypadding 0 xmargin 0 ymargin 0
                        textbutton _("Макс") action SetVariable('CurChar', 'max') selected CurChar == 'max' text_selected_color gui.text_color
                        foreground 'interface marker'
                    for char in sorted(chars.keys()):
                        button background None action SetVariable('CurChar', char) xsize 180:
                            # xpadding 0 ypadding 0 xmargin 0 ymargin 0
                            textbutton chars[char].name action SetVariable('CurChar', char) selected CurChar == char text_selected_color gui.text_color
                            foreground 'interface marker'
            vbar value YScrollValue('vp') style 'info_vscroll'

        if CurChar == 'max': ## временное определение на стадии вывода изображения
            add 'Max info '+clothes[mgg].casual.GetCur().info size (550, 900) xpos -50 ypos 10

        else:
            frame xysize(550, 900) background None:
                if chars[CurChar].dress_inf == '':
                    add chars[CurChar].pref+' info-00' size (550, 900) xpos -50 ypos 10
                else:
                    add chars[CurChar].pref+' info '+chars[CurChar].dress_inf size (550, 900) xpos -50 ypos 10

        viewport area (0, 30, 880, 800):
            vbox spacing 20:
                frame xsize 850 background None:
                    if CurChar == 'max':
                        text mgg.desc size 24
                    else:
                        text chars[CurChar].desc size 24

                frame pos (50, 20) xsize 800 background None:
                    if CurChar == 'max':
                        vbox spacing -1:
                            for char in sorted(chars.keys()):
                                # relmax
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        $ char_name = chars[char].name_4
                                        text _("Отношения с [char_name!t]") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text GetRelMax(char)[1] size 24
                            frame area (0, 0, 350, 25):
                                background None

                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Запас сил") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text str(round(mgg.energy, 1))+"%" size 24
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Тренированность") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text str(round(mgg.training, 1))+"%" size 24
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Чистота") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text str(round(mgg.cleanness, 1))+"%" size 24

                            frame area (0, 0, 350, 25):
                                background None
                            frame xsize 350 background None:
                                text _("Навыки:") size 26 font 'trebucbd.ttf'
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Навык убеждения") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text str(round(mgg.social*10, 1)) size 24
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Навык скрытности") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text str(round(mgg.stealth*10, 1)) size 24
                            if mgg.massage > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык массажа") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(round(mgg.massage*10, 1)) size 24
                            if mgg.ero_massage > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык эро.массажа") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(round(mgg.ero_massage*10, 1)) size 24
                            if mgg.kissing > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык поцелуев") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(round(mgg.kissing*10, 1)) size 24
                            if mgg.sex > 0:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Сексуальный опыт") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(round(mgg.sex*10, 1)) size 24


                    elif CurChar == 'eric':
                        pass
                    else:
                        vbox spacing -1:
                            # mood
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Настроение") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text chars[CurChar].GetMood()[1] size 24
                            # relmax
                            hbox xfill True:
                                frame xsize 350 background None:
                                    text _("Уровень отношений") size 24 color gui.accent_color
                                frame xfill True background None:
                                    text GetRelMax(CurChar)[1] size 24

                            # free
                            if not chars[CurChar].free is None:
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Раскрепощенность") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(chars[CurChar].free) size 24
                            if not chars[CurChar].releric is None:
                                # releric
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Отношения с Эриком") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text GetRelEric(CurChar)[1] size 24

                                # inf_eric
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Влияние Эрика") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(chars[CurChar].free)+"%" size 24

    frame area(1350, 1000, 450, 50) background None:
        textbutton _("Задать одежду персонажа") xalign 1.0:
            text_size gui.text_size
            if CurChar == 'max':
                action [SetVariable('cloth', clothes[mgg]), Hide('menu_userinfo'), Show('ClothesSelect')]
                sensitive clothes[mgg].Opens()
            elif chars[CurChar] in clothes:
                action [SetVariable('cloth', clothes[chars[CurChar]]), Hide('menu_userinfo'), Show('ClothesSelect')]
                sensitive clothes[chars[CurChar]].Opens()
            else:
                action NullAction()
                sensitive False

    key 'K_ESCAPE' action Jump('AfterWaiting')
    key 'mouseup_3' action Jump('AfterWaiting')

style userinfo_button is default:
    xpadding 0 ypadding 1
    xmargin 0 ymargin 2
    left_padding 30
    yalign .5

style userinfo_button_text is default:
    font 'trebucbd.ttf'
    # xpos 30
    yalign .0
    size 30
    idle_color gui.accent_color
    hover_color gui.text_color
    insensitive_color gui.insensitive_color

style userinfo_button_text:
    variant "small"
    font 'trebucbd.ttf'
    yalign .0
    size 36
    idle_color gui.accent_color
    hover_color gui.text_color
    insensitive_color gui.insensitive_color

style info_vscroll is vscrollbar:
    unscrollable 'hide'

screen ClothesSelect():
    tag menu
    add 'interface phon'
    style_prefix 'clothesselect'
    frame area(150, 95, 750, 50) background None:
        text _("ЗАДАТЬ ОДЕЖДУ ПЕРСОНАЖА") color gui.accent_color size 28 font 'hermes.ttf'

    imagebutton pos (1740, 100) auto 'interface close %s' action [Hide('ClothesSelect'), Show('menu_userinfo')]:
        if not renpy.variant('small'):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_var_small

    $ lst1 = cloth.GetList()
    $ list = []
    for l in lst1:
        if eval('cloth.'+l).Opens():
            $ list.append(l)
    default cur_cl = list[0]
    $ list_var = eval('cloth.'+cur_cl).GetOpen()
    default cur_var = 0
    hbox pos (150, 150) spacing 30:
        hbox ypos 25 xsize 400 spacing 5:
            viewport mousewheel 'change' draggable True id 'vp':
                vbox spacing 5:
                    for l in list:
                        button background None action [SetScreenVariable('cur_cl', l), SetScreenVariable('cur_var', 0)] xsize 380:
                            xpadding 0 ypadding 0 xmargin 0 ymargin 0
                            textbutton eval('cloth.'+l).name action [SetScreenVariable('cur_cl', l), SetScreenVariable('cur_var', 0)] selected cur_cl == l
                            foreground 'interface marker'
            vbar value YScrollValue('vp') style 'info_vscroll'

        imagebutton pos (0, 360) auto 'interface prev %s':
            focus_mask True
            sensitive cur_var > 0
            action SetScreenVariable('cur_var', cur_var-1)

        imagebutton:
            action NullAction()
            # focus_mask True
            xysize (550, 900)
            ypos 30
            if CurChar == 'max':
                idle 'Max clot '+eval('cloth.'+cur_cl).sel[list_var[cur_var]].info
                hover 'Max clot '+eval('cloth.'+cur_cl).sel[list_var[cur_var]].info+'a'
            else:
                idle chars[CurChar].pref+' clot '+eval('cloth.'+cur_cl).sel[list_var[cur_var]].info
                hover chars[CurChar].pref+' clot '+eval('cloth.'+cur_cl).sel[list_var[cur_var]].info+'a'



        imagebutton pos (0, 360) auto 'interface next %s':
            focus_mask True
            sensitive cur_var < len(list_var)-1
            action SetScreenVariable('cur_var', cur_var+1)

    vbox pos (1420, 900) spacing 15:
        textbutton _("Автосмена каждые 2 дня"):
            xsize 400
            action ToggleVariable('cloth.'+cur_cl+'.rand', True, False)
            text_idle_color gui.idle_color
            text_hover_color gui.hover_color
            text_selected_color gui.selected_color
            text_insensitive_color gui.insensitive_color
            if eval('cloth.'+cur_cl).rand:
                foreground 'gui/button/check_selected_foreground.png'


        textbutton _("Сделать текущей"):
            xsize 400
            text_size 30
            if eval('cloth.'+cur_cl).rand:
                action [SetVariable('cloth.'+cur_cl+'.cur', list_var[cur_var]), SetVariable('cloth.'+cur_cl+'.left', 1)]
            else:
                action SetVariable('cloth.'+cur_cl+'.cur', list_var[cur_var])
            sensitive eval('cloth.'+cur_cl).cur != list_var[cur_var]
            text_selected_color gui.selected_color
            text_insensitive_color gui.insensitive_color
            text_idle_color gui.accent_color
            text_hover_color gui.text_color

    key 'K_ESCAPE' action [Hide('ClothesSelect'), Show('menu_userinfo')]
    key 'mouseup_3' action [Hide('ClothesSelect'), Show('menu_userinfo')]

style clothesselect_button is default:
    padding (30, 7, 6, 7)

style clothesselect_button_text is default:
    font 'trebucbd.ttf'
    yalign .0
    size 24
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color
    insensitive_color gui.insensitive_color

style clothesselect_vscroll is vscrollbar:
    unscrollable 'hide'

################################################################################

screen cam_show():

    hbox pos(350, 800):
        xalign 0.0
        text tm font 'bedel.otf' size 30  #drop_shadow[(2, 2)]

    hbox pos(1560, 800):
        xalign 1.0
        spacing 10
        text _("[view_cam[1].public]") font 'bedel.otf' size 30  #drop_shadow[(2, 2)]
        add 'interface laptop cam audience' ypos 5

    if len(cam_list) > 1:
        imagebutton pos (135, 490) auto 'interface prev %s':
            focus_mask (None if renpy.variant('small') else True)
            action [Function(prev_cam), Jump('Waiting')]
        imagebutton pos (1672, 490) auto 'interface next %s':
            focus_mask (None if renpy.variant('small') else True)
            action [Function(next_cam), Jump('Waiting')]


    frame xalign 0.5 ypos 985 xsize 200:# background None:
        if '06:00' <= tm < '22:00':
            if current_room == house[5]:
                background 'interface laptop keys-bg-dayt'
            else:
                background 'interface laptop keys-bg-day'
        else:
            if current_room == house[5]:
                background 'interface laptop keys-bg-nightt'
            else:
                background 'interface laptop keys-bg-night'
        xmargin 0 ymargin 0 xpadding 0 ypadding 0
        hbox spacing 100:
            imagebutton:
                auto 'interface laptop back %s'
                action [SetVariable('at_comp', False), Jump('open_site')] at power_zoom
            imagebutton:
                auto 'interface laptop wait %s'
                action [SetVariable('spent_time', 10), Jump('Waiting')] at power_zoom
    key 'K_SPACE' action [SetVariable('spent_time', 10), Jump('Waiting')]

    key 'K_ESCAPE' action [SetVariable('at_comp', False), Jump('open_site')]
    key 'mouseup_3' action [SetVariable('at_comp', False), Jump('open_site')]
    if len(cam_list) > 1:
        key 'K_LEFT' action [Function(prev_cam), Jump('Waiting')]
        key 'K_RIGHT' action [Function(next_cam), Jump('Waiting')]
    if not _in_replay:
        # key 'K_F5' action [SetVariable('number_quicksave', number_quicksave+1), NewSaveName(), QuickSave()]
        key 'K_F8' action QuickLoad()

################################################################################

screen watermark():
    layer 'wm'
    if str(renpy.get_mode())=='start' and not renpy.get_screen(['main_menu','game_menu','about','help','save','load','preferences']):
            imagebutton:
                anchor (0.5, 0.5)
                pos (0.9, 0.95)
                idle 'interface BBAS'
                action OpenURL('https://www.patreon.com/aleksey90artimages')
                at main_logo2

screen notify_check():
    timer .3 repeat True action Function(notify_queue)
    # $ tt = GetTooltip()
    # if tt:
    #     text "[tt!t]" pos renpy.get_mouse_pos()
