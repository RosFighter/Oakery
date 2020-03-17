
screen search_cigarettes:
    tag menu

    imagemap:
        ground "BG char Max cigarettes-00"
        hotspot (0, 700, 400, 380) action [Cursor(None), Jump('SearchCigarettes.no')]:
            hovered Cursor("find")
            unhovered Cursor(None)
        hotspot (0, 310, 615, 330) action [Cursor(None), Jump('SearchCigarettes.bedside')]:
            hovered Cursor("find")
            unhovered Cursor(None)
        hotspot (1370, 400, 570, 680) action [Cursor(None), Jump('SearchCigarettes.table')]:
            hovered Cursor("find")
            unhovered Cursor(None)
    key 'mouseup_3' action NullAction()
    key 'K_ESCAPE' action NullAction()
    key 'K_MENU' action NullAction()
