
label cam0_lisa_sun:
    $ renpy.show('Lisa cams sun '+renpy.random.choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_sun' not in cam_flag:
        $ cam_flag.append('lisa_sun')
        Max_00 "Младшая сестрёнка загорает..."
    return

label cam1_lisa_sun:
    show FG cam-shum-act at laptop_screen
    if 'lisa_sun1' not in cam_flag:
        $ cam_flag.append('lisa_sun1')
        Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_lisa_swim:
    show FG cam-shum-act at laptop_screen
    if 'lisa_swim0' not in cam_flag:
        $ cam_flag.append('lisa_swim0')
        if len(house[6].cams)>1:
            Max_00 "Ничего толком не видно... Стоит взглянуть с другой камеры..."
        else:
            Max_00 "Ничего не разглядеть... Нужно установить камеру охватывающую бассейн..."
    return

label cam1_lisa_swim:
    $ renpy.show('Lisa cams swim '+renpy.random.choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_swim1' not in cam_flag:
        $ cam_flag.append('lisa_swim1')
        Max_00 "Приядно наблюдать за младшей сестрёнкой..."
    return
