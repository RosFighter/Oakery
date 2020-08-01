
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

label lisa_cam_dress_inf(r1):
    $ lisa.dress_inf = {
            '01':'02b',
            '02':'02c',
            '03':'00',
            '04':'00',
            '05':'00',
            '06':'00',
            '07':'02h',
            '08':'02d',
            '09':'02e',
            '10':'02i',
            '11':'02f',
            '12':'02g',
            '13':'01b',
            '14':'01',
        }[r1]
    return

label cam0_lisa_dressed_school:

    if 'lisa_dressed' in cam_flag:
        $ renpy.show('Lisa cams dressed 13', at_list=[laptop_screen])
        $ lisa.dress_inf = '01d'
        if 'lisa_dressed_txt' not in cam_flag:
            $ cam_flag.append('lisa_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('lisa_dressed')
    $ spent_time += 10

    $ __r1 = renpy.random.choice(['01', '02'])
    call lisa_cam_dress_inf(__r1)
    $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Сестрёнка одевается в школу..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['03','04','05','06'])
    call lisa_cam_dress_inf(__r1)
    $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого, вот это вид!!!"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['07','08','09'])
    call lisa_cam_dress_inf(__r1)
    $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    Max_00 "Эх, самое интересное уже закончилось..."
    # jump open_site
    return

label cam0_lisa_dressed_shop:

    if 'lisa_dressed' in cam_flag:
        $ renpy.show('Lisa cams dressed 14', at_list=[laptop_screen])
        $ lisa.dress_inf = '01'
        if 'lisa_dressed_txt' not in cam_flag:
            $ cam_flag.append('lisa_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('lisa_dressed')
    $ spent_time += 10

    $ __r1 = renpy.random.choice(['01', '02'])
    call lisa_cam_dress_inf(__r1)
    $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Сестрёнка одевается на шопинг..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['03','04','05','06'])
    call lisa_cam_dress_inf(__r1)
    $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого, вот это вид!!!"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['10','11','12'])
    call lisa_cam_dress_inf(__r1)
    $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    Max_00 "Эх, самое интересное уже закончилось..."
    # jump open_site
    return
