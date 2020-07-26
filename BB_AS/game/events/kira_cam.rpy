
label cam0_kira_sun:
    $ renpy.show('Kira cams sun '+renpy.random.choice(['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'kira_swim1' not in cam_flag:
        $ cam_flag.append('kira_swim1')
        Max_00 "Ух, тётя Кира загорает..."
    return

label cam1_kira_sun:
    show FG cam-shum-act at laptop_screen
    if 'kira_sun1' not in cam_flag:
        $ cam_flag.append('kira_sun1')
        Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_kira_swim:
    show FG cam-shum-act at laptop_screen
    if 'kira_swim0' not in cam_flag:
        $ cam_flag.append('kira_swim0')
        if len(house[6].cams)>1:
            Max_00 "Ничего толком не видно... Стоит взглянуть с другой камеры..."
        else:
            Max_00 "Ничего не разглядеть... Нужно установить камеру охватывающую бассейн..."
    return

label cam1_kira_swim:
    $ renpy.show('Kira cams swim '+renpy.random.choice(['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_00 "На тётю Киру всегда приятно посмотреть..."
    return
