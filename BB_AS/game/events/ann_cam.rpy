
label cam0_ann_sleep:
    $ renpy.show('Ann cams sleep night '+renpy.random.choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sleep' not in cam_flag:
        $ cam_flag.append('ann_sleep')
        Max_07 "Обалденно! Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!"
    return

label cam0_ann_shower:
    if tm[-2:] < '20' and ann.dress_inf != '00a':
        show FG cam-shum-act at laptop_screen
        if 'ann_not_shower' not in cam_flag:
            $ cam_flag.append('ann_not_shower')
            if len(house[3].cams)>1:
                Max_00 "Мамы не видно, скорее всего она возле зеркала... Но отсюда не видно, нужно посмотреть через другую камеру..."
            else:
                Max_00 "Мамы не видно, скорее всего она возле зеркала... Но через эту камеру не разглядеть..."
    else:
        $ ann.dress_inf = '00a'
        $ renpy.show('Ann cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_shower' not in cam_flag:
            $ cam_flag.append('ann_shower')
            Max_00 "Моя горячая мама в душе... Это зрелище, которое никогда не надоедает..."
    return

label cam1_ann_shower:
    if tm[-2:] < '20' and ann.dress_inf != '00a':
        # назначим или определим одёжку
        if ann.dress_inf != '04a':
            $ __r1 = {'04c':'a', '04d':'b', '02b':'c', '00':'d', '00a':'d'}[ann.dress_inf]
        else:
            $ __r1 = renpy.random.choice(['a', 'b', 'c', 'd'])
            $ ann.dress_inf = {'a':'04c', 'b':'04d', 'c':'02b', 'd':'00'}[__r1]

        $ renpy.show('Ann cams bath-mirror '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath_mirror' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror')
            if __r1 in ['a', 'b']:
                Max_02 "Да-а... Может мама и в халатике, но сиськи её видны просто замечательно! А они у неё - что надо..."
            elif __r1 == 'c':
                Max_04 "Прекрасно! Мамочка сегодня без халатика... в одних трусиках... Глядя на эту красоту, можно мечтать лишь об одном!"
            else:
                Max_06 "Вау! Мамочка сегодня совершенно голая!"

    else:
        show FG cam-shum-act at laptop_screen
        if 'ann_shower1' not in cam_flag:
            $ cam_flag.append('ann_shower1')
            Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

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

label cam1_ann_yoga:
    show FG cam-shum-act at laptop_screen
    if 'ann_yoga1' not in cam_flag:
        $ cam_flag.append('ann_yoga1')
        Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_ann_cooking:
    $ renpy.show('Ann cams cooking 01'+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'ann_cooking' not in cam_flag:
        $ cam_flag.append('ann_cooking')
        if tm < '12:00':
            Max_00 "Как всегда в это время, мама готовит завтрак, ничего интересного..."
        else:
            Max_00 "Как всегда в это время, мама готовит ужин, ничего интересного..."
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
        show FG cam-shum-act at laptop_screen
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
        show FG cam-shum-act at laptop_screen
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

label cam0_ann_read:
    $ renpy.show('Ann cams reading '+renpy.random.choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_read' not in cam_flag:
        $ cam_flag.append('ann_read')
        Max_01 "Мама увлечённо читает... Вроде бы ничего особенного, а смотреть на её округлые формы приятно, чтобы она не делала!"
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

label cam0_ann_bath:
    if tm[-2:] < '10':
        # набирает воду
        show Ann cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st0' not in cam_flag:
            $ cam_flag.append('ann_bath0_st0')
            Max_00 "Мама ещё только набирает воду, самое интересное впереди..."
    elif tm[-2:] > '40':
        # вытирается
        show Ann cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st1' not in cam_flag:
            $ cam_flag.append('ann_bath0_st1')
            Max_00 "Эх, мама уже вытирается, самое интересное позади..."
    else:
        $ renpy.show('Ann cams bath '+renpy.random.choice(['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st0' not in cam_flag:
            $ cam_flag.append('ann_bath0_st0')
            Max_00 "Мама принимает ванну, заглядение..."
    return

label cam1_ann_bath:
    show FG cam-shum-act at laptop_screen
    if 'ann_bath1' not in cam_flag:
        $ cam_flag.append('ann_bath1')
        Max_00 "Через эту камеру ничего не видно, нужно воспользоваться другой..."
    return

label cam0_ann_tv:
    $ renpy.show('Ann cams tv '+renpy.random.choice(['01', '02', '03'])+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'ann_tv' not in cam_flag:
        $ cam_flag.append('ann_tv')
        Max_00 "Мама, как всегда, смотрит какой-то сериал, ничего особенного..."
    return
