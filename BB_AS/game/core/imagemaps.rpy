
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
            text_font "segoeprb.ttf"


screen search_cigarettes:
    tag menu

    use show_dynamic_tooltip
    imagemap:
        ground "BG char Max cigarettes-00"
        hotspot (0, 700, 400, 380) action [Hide('dynamic_tooltip'), Cursor(None), Jump('SearchCigarettes.no')]:
            hovered Cursor("find")
            unhovered Cursor(None)
            tooltip _("{i}искать под кроватью{/i}")
        hotspot (0, 310, 615, 330) action [Hide('dynamic_tooltip'), Cursor(None), Jump('SearchCigarettes.bedside')]:
            hovered Cursor("find")
            unhovered Cursor(None)
            tooltip _("{i}искать в тумбочке{/i}")
        hotspot (1370, 400, 570, 680) action [Hide('dynamic_tooltip'), Cursor(None), Jump('SearchCigarettes.table')]:
            hovered Cursor("find")
            unhovered Cursor(None)
            tooltip _("{i}искать в столе{/i}")

    key 'mouseup_3' action NullAction()
    key 'K_ESCAPE' action NullAction()
    key 'K_MENU' action NullAction()
