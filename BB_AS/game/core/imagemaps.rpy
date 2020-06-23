
screen show_dynamic_tooltip():
    timer .02 repeat True action Show('dynamic_tooltip')


screen dynamic_tooltip():
    $ tt = GetTooltip()
    $ x, y = renpy.get_mouse_pos()
    if tt:
        label "[tt!t]" text_text_align 0.5:
            xalign 0.5  text_size 36
            if renpy.game.preferences.physical_size[1] < 900:
                pos (x, y+45)
            else:
                pos (x, y+65)
            xminimum 40
            xmaximum 300
            text_color gui.text_color
            text_drop_shadow[(3, 3)]
            text_font 'segoeprb.ttf'


screen search_cigarettes():
    tag menu

    use show_dynamic_tooltip
    imagemap:
        ground 'BG char Max cigarettes-00'
        hotspot (0, 700, 400, 380) action [Hide('dynamic_tooltip'), Cursor(None), Jump('SearchCigarettes.no')]:
            hovered Cursor('find')
            unhovered Cursor(None)
            tooltip _("{i}искать под кроватью{/i}")
        hotspot (0, 310, 615, 330) action [Hide('dynamic_tooltip'), Cursor(None), Jump('SearchCigarettes.bedside')]:
            hovered Cursor('find')
            unhovered Cursor(None)
            tooltip _("{i}искать в тумбочке{/i}")
        hotspot (1370, 400, 570, 680) action [Hide('dynamic_tooltip'), Cursor(None), Jump('SearchCigarettes.table')]:
            hovered Cursor('find')
            unhovered Cursor(None)
            tooltip _("{i}искать в столе{/i}")

    key 'mouseup_3' action NullAction()
    key 'K_ESCAPE' action NullAction()
    key 'K_MENU' action NullAction()


screen choice_zone_sunscreen():
    tag menu

    use show_dynamic_tooltip
    imagemap:
        if talk_var['sun_oiled'] == 2:
            ground 'BG char Alice sun-alone 01-01a'
        else:
            ground 'BG char Alice sun-alone 01-01'
        add 'Max sun-alone 01'+mgg.dress
        hotspot (78, 358, 132, 108) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.left_foot')]:
            hovered Cursor('palms')
            unhovered Cursor(None)
            tooltip _("{i}массировать ступни{/i}")

        hotspot (0, 576, 158, 132) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.right_foot')]:
            hovered Cursor('palms')
            unhovered Cursor(None)
            tooltip _("{i}массировать ступни{/i}")

        hotspot (224, 349, 348, 118) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.shin')]:
            hovered Cursor('palms')
            unhovered Cursor(None)
            tooltip _("{i}массировать голени{/i}")

        hotspot (181, 552, 391, 122) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.shin')]:
            hovered Cursor('palms')
            unhovered Cursor(None)
            tooltip _("{i}массировать голени{/i}")


        if False: # if len(online_cources) > 1 and online_cources[1].current > 0:
            hotspot (594, 358, 316, 316) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.hips')]:
                hovered Cursor('palms')
                unhovered Cursor(None)
                tooltip _("{i}массировать бёдра{/i}")

        hotspot (1536, 358, 116, 255) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.shoulders')]:
            hovered Cursor('palms')
            unhovered Cursor(None)
            tooltip _("{i}массировать плечи{/i}")

        hotspot (1146, 363, 374, 250) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.spine')]:
            hovered Cursor('palms')
            unhovered Cursor(None)
            tooltip _("{i}массировать спину{/i}")

        if False:
            hotspot (924, 348, 206, 326) action [Hide('dynamic_tooltip'), Cursor(None), Jump('massage_sunscreen.ass')]:
                hovered Cursor('palms')
                unhovered Cursor(None)
                tooltip _("{i}массировать попку{/i}")


    key 'mouseup_3' action NullAction()
    key 'K_ESCAPE' action NullAction()
    key 'K_MENU' action NullAction()
