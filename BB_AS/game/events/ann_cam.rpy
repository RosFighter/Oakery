
label cam0_ann_yoga:
    if int(tm[3:4])%3 == 0: # смена позы каждые 10 минут
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(1, 3)), at_list=[laptop_screen])
    elif int(tm[3:4])%3 == 1:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(4, 6)), at_list=[laptop_screen])
    else:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(7, 9)), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_yoga' not in cam_flag:
        $ cam_flag.append('ann_yoga')
        Max_02 "Мама, как и всегда в это время, занимается йогой. Здесь, хоть в какой позе, она выглядит очень сексуально..."
    return

label cam0_ann_read:
    $ renpy.show('Ann cams reading '+renpy.random.choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_read' not in cam_flag:
        $ cam_flag.append('ann_read')
        Max_01 "Мама увлечённо читает... Вроде бы ничего особенного, а смотреть на её округлые формы приятно, чтобы она не делала!"
    return

label ann_cam_dress_inf(r1):
    $ ann.dress_inf = {
            '01':'02e',
            '01a':'02c',
            '02':'02',
            '02a':'02a',
            '02b':'02b',
            '03':'02i',
            '03a':'02h',
            '04':'02g',
            '05':'00',
            '06':'00',
            '07':'00',
            '08':'00',
            '09':'02j',
            '09a':'02d',
            '10':'01',
            '11':'01a',
            '12':'01',
        }[r1]
    return

label cam0_ann_dressed_work:
    if 'ann_dressed' in cam_flag:
        $ renpy.show('Ann cams dressed 11', at_list=[laptop_screen])
        $ ann.dress_inf = '01d'
        if 'ann_dressed_txt' not in cam_flag:
            $ cam_flag.append('ann_dressed_txt')
            Max_00 "Уже ничего интересного, мама полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('ann_dressed')
    $ spent_time += 10
    $ __list = ['03', '03a', '04'] if ann.dress=='d' else ['01', '01a', '02', '02a', '02b']  # частично одета. Может быть как с нижним бельём, так и без
    $ __ran1 = renpy.random.choice(__list)
    call ann_cam_dress_inf(__ran1)

    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Мама одевается на работу..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __ran1 = renpy.random.choice(['05','06','07','08'])
    $ ann.dress_inf = '00'
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого! Становится интересней..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __ran1 = renpy.random.choice(['09', '09a'])
    call ann_cam_dress_inf(__ran1)
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    Max_00 "Эх, самое интересное уже закончилось..."
    # jump open_site
    return

label cam0_ann_dressed_shop:
    if 'ann_dressed' in cam_flag:
        $ renpy.show('Ann cams dressed 11', at_list=[laptop_screen])
        $ ann.dress_inf = '01d'
        if 'ann_dressed_txt' not in cam_flag:
            $ cam_flag.append('ann_dressed_txt')
            Max_00 "Уже ничего интересного, мама полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('ann_dressed')
    $ spent_time += 10
    $ __list = ['03', '03a', '04'] if ann.dress=='d' else ['01', '01a', '02', '02a', '02b']  # частично одета. Может быть как с нижним бельём, так и без
    $ __ran1 = renpy.random.choice(__list)
    call ann_cam_dress_inf(__ran1)

    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Мама одевается на шопинг..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __ran1 = renpy.random.choice(['05','06','07','08'])
    $ ann.dress_inf = '00'
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого! Становится интересней..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __ran1 = '10'
    call ann_cam_dress_inf(__ran1)
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    Max_00 "Эх, самое интересное уже закончилось..."
    return

label cam0_ann_resting:
    if tm < '19:00':
        $ renpy.show('Ann cams relax-morning '+renpy.random.choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    else:
        $ renpy.show('Ann cams relax-evening '+renpy.random.choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    if 'ann_resting' not in cam_flag:
        $ cam_flag.append('ann_resting')
        Max_01 "Мама отдыхает..."
    return

label cam0_ann_sun:
    $ renpy.show('Ann cams sun '+renpy.random.choice(['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sun' not in cam_flag:
        $ cam_flag.append('ann_sun')
        Max_00 "Мама загорает..."
    return

label cam1_ann_sun:
    show FG cam-shum-act at laptop_screen
    if 'ann_sun1' not in cam_flag:
        $ cam_flag.append('ann_sun1')
        Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_ann_swim:
    show FG cam-shum-act at laptop_screen
    if 'ann_swim0' not in cam_flag:
        $ cam_flag.append('ann_swim0')
        if len(house[6].cams)>1:
            Max_00 "Ничего толком не видно... Стоит взглянуть с другой камеры..."
        else:
            Max_00 "Ничего не разглядеть... Нужно установить камеру охватывающую бассейн..."
    return

label cam1_ann_swim:
    $ renpy.show('Ann cams swim '+renpy.random.choice(['01', '02', '03', '04']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_00 "На маму всегда приятно посмотреть..."
    return

label cam0_ann_alice_sun:
    $ renpy.show('Alice cams sun '+renpy.random.choice(['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    $ renpy.show('Ann cams sun '+renpy.random.choice(['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sun' not in cam_flag:
        $ cam_flag.append('ann_sun')
        $ cam_flag.append('alice_sun')
        Max_00 "Две красотки лучше чем одна..."
    return

label cam1_ann_alice_sun:
    show FG cam-shum-act at laptop_screen
    if 'ann_sun1' not in cam_flag:
        $ cam_flag.append('ann_sun1')
        Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_ann_alice_swim:
    show FG cam-shum-act at laptop_screen
    if 'ann_swim0' not in cam_flag:
        $ cam_flag.append('ann_swim0')
        if len(house[6].cams)>1:
            Max_00 "Ничего толком не видно... Стоит взглянуть с другой камеры..."
        else:
            Max_00 "Ничего не разглядеть... Нужно установить камеру охватывающую бассейн..."
    return

label cam1_ann_alice_swim:
    # Несовместимые спрайты с Алисой и Анной в бассейне:
    # alice-01 & ann-02
    # alice-01 & ann-04
    # alice-02 & ann-02
    # alice-02 & ann-04
    # alice-03 & ann-03
    $ __alice_pose = renpy.random.choice(['01', '02', '03', '04'])
    $ __ann_pose_list = {
            '01' : ['01', '03'],
            '02' : ['01', '03'],
            '03' : ['01', '02', '04'],
            '04' : ['01', '02', '03', '04'],
        }[__alice_pose]
    $ renpy.show('Alice cams swim '+__alice_pose, at_list=[laptop_screen])
    $ renpy.show('Ann cams swim '+renpy.random.choice(__ann_pose_list), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim' not in cam_flag:
        $ cam_flag.append('ann_swim')
        $ cam_flag.append('alice_swim')
        Max_00 "Две красотки в бассейне, что может быть лучше? Только две голые красотки..."
    return
