

screen s1_cheat_warning():
    tag menu2
    modal True
    use LaptopScreen
    button:
        background None
        area(0, 0, 1920, 1080)
        action NullAction()

    frame:
        align(0.5, 0.42) xsize 1000
        xmargin 0 ymargin 0 xpadding 70 ypadding 50
        vbox spacing 10:
            xalign .5
            text _("ПРЕДУПРЕЖДЕНИЕ!") xalign 0.5 color red font 'hermes.ttf' size 36
            null height 20
            text _("С осторожностью используйте чит-меню - это может привести к ошибкам в прохождении.") xalign 0.5 text_align 0.5 color gui.accent_color
            text _("Доступ к части читов будет открыт после достижения некоторого прогресса для минимизации последствий вмешательства в переменные игры.") xalign 0.5 text_align 0.5 color gui.accent_color
            null height 40
            textbutton "{color=#0f0}✔{/color} {b}Ок{/b}":
                action [SetVariable('cheats_warning', True), Hide('s1_cheat_warning'), Show('s1_cheat_screen')]
                style 'ch_warn_btn'

style ch_warn_btn:
    xalign 0.5
    xpadding 50 ypadding 15
    background "#4b4c4c"

style ch_warn_btn_text:
    size 30
    idle_color gui.accent_color
    hover_color gui.text_color
    font gui.interface_text_font


screen s1_cheat_screen():
    tag menu2
    modal True
    use PowerBack

    $ cheat_char = ['max', 'alice', 'ann', 'lisa']
    if CurChar not in cheat_char:
        $ CurChar = 'max'
    default skip_days = 1 if tm >= '06:00' else 2

    add 'interface laptop CoverCheats' at laptop_screen
    hbox area(261, 123, 1395, 569) spacing 50:
        frame background '#00000060':
            vbox spacing 5:
                style_prefix 'cheat_lst'
                textbutton _("Макс"):
                    action SetVariable('CurChar', 'max')
                    selected CurChar == 'max'
                for char in sorted(chars.keys()):
                    if char in cheat_char:
                        textbutton chars[char].name:
                            action SetVariable('CurChar', char)
                            selected CurChar == char
        frame background '#00000060' ypos -30:
            if CurChar == 'max':
                add 'Max info '+mgg.clothes.casual.GetCur().info size (385, 630)
            else:
                if chars[CurChar].dress_inf == '':
                    add chars[CurChar].pref+' info-00' size (385, 630)
                else:
                    add chars[CurChar].pref+' info '+chars[CurChar].dress_inf size (385, 630)

        frame background '#00000060':
            xfill True yfill True
            style_prefix 'cheats'
            if CurChar == 'max':
                frame align(.5, .1) padding(50, 50) background None:
                    vbox spacing 5:
                        # деньги
                        hbox spacing 30:
                            frame xsize 360 ypadding 6 background None:
                                text _("Деньги:")
                            frame xsize 100 ypadding 6 background None:
                                text "$ [mgg.money]" color gui.text_color xalign .5

                            if dcv.ch_money.done and flags.credit == 2:
                                textbutton "+500":
                                    action Function(get_cheats_money)
                                    sensitive dcv.ch_money.done and flags.credit == 2
                                    if flags.credit < 2:
                                        tooltip _("Невозможно до открытия доступа к банку (открывается на 9 день)")
                                    else:
                                        tooltip _("Доступно один раз в день")
                            else:
                                textbutton "+500":
                                    action NullAction()
                                    text_color gui.insensitive_color
                                    if flags.credit < 2:
                                        tooltip _("Невозможно до открытия доступа к банку (открывается на 9 день)")
                                    else:
                                        tooltip _("Доступно один раз в день")

                        # навыки Макса
                        hbox spacing 30:
                            frame xsize 360 ypadding 6 background None:
                                text _("Запас сил:")
                            frame xsize 100 ypadding 6 background None:
                                text str(round(mgg.energy, 1))+"%" color gui.text_color xalign .5
                            textbutton _("Восстановить"):
                                action SetVariable('mgg.energy', 100)
                                sensitive mgg.energy < 100

                        frame xsize 350 background None top_padding 20:
                            text _("Навыки:") size 26 font 'trebucbd.ttf' color gui.text_color

                        hbox spacing 30:
                            frame xsize 260 padding(30, 6, 0, 6) background None:
                                text _("Навык убеждения:")
                            imagebutton auto 'interface prev %s':
                                action SetVariable('mgg.social', (round(mgg.social*10, 1) - 10) / 10)
                                sensitive mgg.social > 7
                            frame xsize 30 ypadding 6 background None:
                                text str(round(mgg.social*10, 1)) color gui.text_color xalign .5
                            imagebutton auto 'interface next %s':
                                if online_cources[0].cources[1].less > 0 or mgg.social < 18:
                                    action SetVariable('mgg.social', (round(mgg.social*10, 1) + 10) / 10)
                                    sensitive mgg.social < 58
                                else:
                                    action NullAction()
                                    tooltip _("Необходимо пройти первый урок онлайн-курса \"Общение\"")

                        hbox spacing 30:
                            frame xsize 260 padding(30, 6, 0, 6) background None:
                                text _("Навык скрытности:")
                            imagebutton auto 'interface prev %s':
                                action SetVariable('mgg.stealth', (round(mgg.stealth*10, 1) - 10) / 10)
                                sensitive mgg.stealth > 8
                            frame xsize 30 ypadding 6 background None:
                                text str(round(mgg.stealth*10, 1)) color gui.text_color xalign .5
                            imagebutton auto 'interface next %s':
                                action SetVariable('mgg.stealth', (round(mgg.stealth*10, 1) + 10) / 10)
                                sensitive mgg.stealth < 58

                        if learned_foot_massage():
                            hbox spacing 30:
                                frame xsize 260 padding(30, 6, 0, 6) background None:
                                    text _("Навык массажа:")
                                imagebutton auto 'interface prev %s':
                                    action SetVariable('mgg.massage', (round(mgg.massage*10, 1) - 10) / 10)
                                    sensitive mgg.massage > 3
                                frame xsize 30 ypadding 6 background None:
                                    text str(round(mgg.massage*10, 1)) color gui.text_color xalign .5
                                imagebutton auto 'interface next %s':
                                    action SetVariable('mgg.massage', (round(mgg.massage*10, 1) + 10) / 10)
                                    sensitive mgg.massage < 74

                        if 'lisa' in flags.how_to_kiss:
                            hbox spacing 30:
                                frame xsize 260 padding(30, 6, 0, 6) background None:
                                    text _("Навык поцелуев:")
                                imagebutton auto 'interface prev %s':
                                    action SetVariable('mgg.kissing', (round(mgg.kissing*10, 1) - 10) / 10)
                                    sensitive mgg.kissing > 3
                                frame xsize 30 ypadding 6 background None:
                                    text str(round(mgg.kissing*10, 1)) color gui.text_color xalign .5
                                imagebutton auto 'interface next %s':
                                    action SetVariable('mgg.kissing', (round(mgg.kissing*10, 1) + 10) / 10)
                                    sensitive mgg.kissing < 40

                        if mgg.sex > 0:
                            hbox spacing 30:
                                frame xsize 260 padding(30, 6, 0, 6) background None:
                                    text _("Сексуальный опыт:")
                                imagebutton auto 'interface prev %s':
                                    action SetVariable('mgg.sex', (round(mgg.sex*10, 1) - 10) / 10)
                                    sensitive mgg.sex > 1
                                frame xsize 30 ypadding 6 background None:
                                    text str(round(mgg.sex*10, 1)) color gui.text_color xalign .5
                                imagebutton auto 'interface next %s':
                                    action SetVariable('mgg.sex', (round(mgg.sex*10, 1) + 10) / 10)
                                    sensitive mgg.sex < 50

                        null height 50

                        # пропустить дни
                        hbox spacing 30:
                            textbutton _("{b}Пропустить дни:{/b}"):
                                xsize 260
                                action [Hide('s1_cheat_screen'),
                                SetVariable('at_comp', False),
                                SetVariable('cheat_skip', True),
                                SetVariable('skip_error', False),
                                Call('s1_cheat_skip', skip_days)]
                            imagebutton auto 'interface prev %s':
                                action SetScreenVariable('skip_days', skip_days - 1)
                                sensitive skip_days > (1 if tm >= '06:00' else 2)
                            frame xsize 30 ypadding 6 background None:
                                text str(skip_days) color gui.text_color xalign .5
                            imagebutton auto 'interface next %s':
                                action SetScreenVariable('skip_days', skip_days + 1)
                                sensitive skip_days < 7

            else:
                # для персонажей
                # настроение / отношение / влияние
                frame align(.5, .1) padding(50, 50) background None:
                    vbox spacing 5:
                        # настроение
                        hbox spacing 20:
                            frame xsize 300 padding(30, 6, 0, 6) background None:
                                text _("Настроение:")
                            imagebutton auto 'interface prev %s':
                                action Function(set_mood_lvl, CurChar, chars[CurChar].GetMood()[0] - 1)
                                sensitive chars[CurChar].GetMood()[0] > 0
                            frame xsize 150 ypadding 6 background None:
                                text chars[CurChar].GetMood()[1] color gui.text_color xalign .5
                            imagebutton auto 'interface next %s':
                                action Function(set_mood_lvl, CurChar, chars[CurChar].GetMood()[0] + 1)
                                sensitive chars[CurChar].GetMood()[0] < 4

                        # отношение
                        hbox spacing 20:
                            frame xsize 300 padding(30, 6, 0, 6) background None:
                                text _("Уровень отношений:")
                            imagebutton auto 'interface prev %s':
                                action Function(set_relation_lvl, CurChar, GetRelMax(CurChar)[0] - 1)
                                sensitive GetRelMax(CurChar)[0] > 0
                            frame xsize 150 ypadding 6 background None:
                                text GetRelMax(CurChar)[1] color gui.text_color xalign .5
                            imagebutton auto 'interface next %s':
                                action Function(set_relation_lvl, CurChar, GetRelMax(CurChar)[0] + 1)
                                sensitive GetRelMax(CurChar)[0] < 3

                        if chars[CurChar] in infl:
                            # влияние Макса
                            hbox spacing 20:
                                frame xsize 300 padding(30, 6, 0, 6) background None:
                                    text _("Влияние Макса:"):
                                        if infl[chars[CurChar]].balance[2] == 'm':
                                            color lime
                                imagebutton auto 'interface prev %s':
                                    action Function(set_influence, CurChar, 'm-')
                                    sensitive infl[chars[CurChar]].balance[0] > 0 and chars[CurChar].dcv.battle.stage > 0
                                frame xsize 150 ypadding 6 background None:
                                    text str(infl[chars[CurChar]].balance[0])+"%" color gui.text_color xalign .5
                                imagebutton auto 'interface next %s':
                                    action Function(set_influence, CurChar, 'm+')
                                    sensitive infl[chars[CurChar]].balance[0] < 100 and chars[CurChar].dcv.battle.stage > 0

                            # влияние Эрика
                            hbox spacing 20:
                                frame xsize 300 padding(30, 6, 0, 6) background None:
                                    text _("Влияние Эрика:"):
                                        if infl[chars[CurChar]].balance[2] == 'e':
                                            color lime
                                imagebutton auto 'interface prev %s':
                                    action Function(set_influence, CurChar, 'e-')
                                    sensitive infl[chars[CurChar]].balance[1] > 0 and chars[CurChar].dcv.battle.stage > 0
                                frame xsize 150 ypadding 6 background None:
                                    text str(infl[chars[CurChar]].balance[1])+"%" color gui.text_color xalign .5
                                imagebutton auto 'interface next %s':
                                    action Function(set_influence, CurChar, 'e+')
                                    sensitive infl[chars[CurChar]].balance[1] < 100 and chars[CurChar].dcv.battle.stage > 0





    $ tt_hint = GetTooltip()


    # открыть фотоальбомы и воспоминания предыдущей версии
    # открыть все воспоминания

    frame area(321, 793, 1275, 100):
        background '#00000060'
        if tt_hint:
            text tt_hint size 24 align(.5, .5) text_align .5 xsize 1000


style cheat_lst_button:
    xsize 180
    foreground 'interface marker'
    left_padding 40

style cheat_lst_button_text:
    font 'trebucbd.ttf'
    yalign .0
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color
    insensitive_color gui.insensitive_color

style cheats_text is default:
    size 24
    color gui.accent_color

style cheats_button_text:
    size 24
    idle_color gui.accent_color
    hover_color gui.text_color
    insensitive_color gui.insensitive_color


screen after_a_while():
    modal True

    button:
        background '#000'
        area(0, 0, 1920, 1080)
        action Return()

    frame align(.5, .5) background None:
        text _("ЧЕРЕЗ НЕКОТОРОЕ ВРЕМЯ...") color gui.accent_color size 38 font 'hermes.ttf'

screen after_some_minutes():
    modal True

    button:
        background '#000'
        area(0, 0, 1920, 1080)
        action Return()

    frame align(.5, .5) background None:
        text _("ЧЕРЕЗ НЕСКОЛЬКО МИНУТ...") color gui.accent_color size 38 font 'hermes.ttf'
