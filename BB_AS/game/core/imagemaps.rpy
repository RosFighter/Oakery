
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
        hotspot (0, 700, 400, 380) action [Hide('dynamic_tooltip'), Jump('SearchCigarettes.no')]:
            mouse 'find'
            tooltip _("{i}искать под кроватью{/i}")
        hotspot (0, 310, 615, 330) action [Hide('dynamic_tooltip'), Jump('SearchCigarettes.bedside')]:
            mouse 'find'
            tooltip _("{i}искать в тумбочке{/i}")
        hotspot (1370, 400, 570, 680) action [Hide('dynamic_tooltip'), Jump('SearchCigarettes.table')]:
            mouse 'find'
            tooltip _("{i}искать в столе{/i}")

    key 'mouseup_3' action NullAction()
    key 'K_ESCAPE' action NullAction()
    key 'K_MENU' action NullAction()


screen choice_zone_sunscreen():
    tag menu

    use show_dynamic_tooltip
    imagemap:
        ground 'BG char Alice sun-alone 01f'
        add 'Alice sun-alone 01-'+('01a' if talk_var['sun_oiled'] == 2 else '01')
        idle 'Alice sun-alone 01-'+('01a' if talk_var['sun_oiled'] == 2 else '01')
        hover 'Alice sun-alone 01-'+('01a' if talk_var['sun_oiled'] == 2 else '01')
        add 'Max sun-alone 01'+mgg.dress
        hotspot (78, 358, 132, 108) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.left_foot')]:
            mouse 'palms'
            tooltip _("{i}массировать ступни{/i}")

        hotspot (0, 576, 158, 132) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.right_foot')]:
            mouse 'palms'
            tooltip _("{i}массировать ступни{/i}")

        hotspot (224, 349, 348, 118) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.shin')]:
            mouse 'palms'
            tooltip _("{i}массировать голени{/i}")

        hotspot (181, 552, 391, 122) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.shin')]:
            mouse 'palms'
            tooltip _("{i}массировать голени{/i}")


        if all([len(online_cources)>1, online_cources[1].current>0, dcv['eric.lingerie'].stage in [5, 7]]):
            hotspot (594, 358, 316, 316) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.hips')]:
                mouse 'palms'
                tooltip _("{i}массировать бёдра{/i}")

        hotspot (1536, 358, 116, 255) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.shoulders')]:
            mouse 'palms'
            tooltip _("{i}массировать плечи{/i}")

        hotspot (1146, 363, 374, 250) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.spine')]:
            mouse 'palms'
            tooltip _("{i}массировать спину{/i}")

        if False:
            hotspot (924, 348, 206, 326) action [Hide('dynamic_tooltip'), Jump('massage_sunscreen.ass')]:
                mouse 'palms'
                tooltip _("{i}массировать попку{/i}")


    key 'mouseup_3' action NullAction()
    key 'K_ESCAPE' action NullAction()
    key 'K_MENU' action NullAction()
