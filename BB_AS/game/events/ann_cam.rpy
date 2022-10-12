
label cam0_ann_sleep:
    if all([ann.flags.showdown_e > 1, flags.eric_wallet > 4, ann.flags.truehelp > 4, not ann.dcv.drink.stage, '02:00'>tm>='01:00']):
        # состоялся за завтраком разговор об изгнании Эрика
        # Макс набрал 5 успешных расширенных йог
        show FG cam-shum-noact at laptop_screen
        Max_09 "Хм... Мамы нет. Где же она?"
        return

    $ renpy.show('Ann cams sleep '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    # $ renpy.show('Ann cams sleep night '+random_choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sleep' not in cam_flag:
        $ cam_flag.append('ann_sleep')
        Max_01 "{m}Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!{/m}"
    return

label cam0_ann_shower:
    if tm[-2:] < '20' and ann.dress_inf != '00a':
        show FG cam-shum-noact at laptop_screen
        if 'ann_not_shower' not in cam_flag:
            $ cam_flag.append('ann_not_shower')
            if len(house[3].cams)>1:
                Max_09 "{m}Мамы не видно через эту камеру... Может посмотреть через другую?{/m}"
            else:
                Max_09 "{m}Мамы не видно через эту камеру...{/m}"
    else:
        $ ann.dress_inf = '00a'
        $ renpy.show('Ann cams shower 0'+str(cam_poses_manager(ann, [x for x in range(1, 10)])), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_shower' not in cam_flag:
            $ cam_flag.append('ann_shower')
            Max_04 "{m}Зрелище просто потрясающее... У меня очень горячая мама!{/m}"
    return

label cam1_ann_shower:
    if tm[-2:] < '20' and ann.dress_inf != '00a':
        # назначим или определим одёжку
        if ann.dress_inf != '04a':
            $ __r1 = {'04c':'a', '04d':'b', '02b':'c', '00':'d', '00a':'d'}[ann.dress_inf]
        else:
            $ __r1 = random_choice(['a', 'b', 'c', 'd'])
            $ ann.dress_inf = {'a':'04c', 'b':'04d', 'c':'02b', 'd':'00'}[__r1]

        $ renpy.show('Ann cams bath-mirror '+cam_poses_manager(ann, ['01', '02', '03'], 1)+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath_mirror' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror')
            # if __r1 in ['a', 'b']:
            #     Max_02 "Да-а... Может мама и в халатике, но сиськи её видны просто замечательно! А они у неё - что надо..."
            # elif __r1 == 'c':
            #     Max_04 "Прекрасно! Мамочка сегодня без халатика... в одних трусиках... Глядя на эту красоту, можно мечтать лишь об одном!"
            # else:
            #     Max_06 "Вау! Мамочка сегодня совершенно голая!"
            Max_03 "{m}Мама, перед тем, как принять душ, красуется перед зеркалом. Глядя на эту красоту, можно мечтать лишь об одном!{/m}"

    else:
        show FG cam-shum-noact at laptop_screen
        if 'ann_shower1' not in cam_flag:
            $ cam_flag.append('ann_shower1')
            Max_09 "{m}Мамы не видно через эту камеру... Может посмотреть через другую?{/m}"
    return

label cam0_ann_yoga:
    if int(tm[3:4])%3 == 0: # смена позы каждые 10 минут
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(1, 3))+ann.dress, at_list=[laptop_screen])
    elif int(tm[3:4])%3 == 1:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(4, 6))+ann.dress, at_list=[laptop_screen])
    else:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(7, 9))+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_yoga' not in cam_flag:
        $ cam_flag.append('ann_yoga')
        Max_02 "{m}Мама, как и всегда в это время, занимается йогой. Здесь, хоть в какой позе, она выглядит очень сексуально...{/m}"
    return

label cam1_ann_yoga:
    show FG cam-shum-noact at laptop_screen
    if 'ann_yoga1' not in cam_flag:
        $ cam_flag.append('ann_yoga1')
        Max_09 "{m}Через эту камеру ничего не видно... Может посмотреть через другую?{/m}"
    return

label cam0_ann_cooking:
    $ renpy.show('Ann cams cooking 01'+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'ann_cooking' not in cam_flag:
        $ cam_flag.append('ann_cooking')
        if tm < '12:00':
            Max_01 "{m}Как и всегда, мама готовит завтрак. Вроде, ничего интересного, но она всё равно лучшая...{/m}"
        else:
            Max_01 "{m}Мама сегодня готовит ужин. Будет очень вкусно...{/m}"
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

label cam0_ann_dressed:
    if GetWeekday < 6:
        call cam0_ann_dressed_work from _call_cam0_ann_dressed_work
    else:
        call cam0_ann_dressed_shop from _call_cam0_ann_dressed_shop

label cam0_ann_dressed_work:
    if 'ann_dressed' in cam_flag:
        $ renpy.show('Ann cams dressed 11', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ ann.dress_inf = '01d'
        if 'ann_dressed_txt' not in cam_flag:
            $ cam_flag.append('ann_dressed_txt')
            Max_09 "{m}Ничего интересного я здесь уже не увижу, мама полностью оделась.{/m}"
        return

    $ cam_flag.append('ann_dressed')
    # $ spent_time += 10
    $ Wait(10)
    $ __list = ['03', '03a', '04'] if ann.dress=='d' else ['01', '01a', '02', '02a', '02b']  # частично одета. Может быть как с нижним бельём, так и без
    $ __ran1 = random_choice(__list)
    call ann_cam_dress_inf(__ran1) from _call_ann_cam_dress_inf

    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "{m}Вот и мама наряжается, чтобы отправиться на работу...{/m}"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __ran1 = random_choice(['05','06','07','08'])
    $ ann.dress_inf = '00'
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "{m}Ох! Голая мама - это восхитительное зрелище...{/m}"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    # $ spent_time += 10
    $ Wait(10)
    $ __ran1 = random_choice(['09', '09a'])
    call ann_cam_dress_inf(__ran1) from _call_ann_cam_dress_inf_1
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    Max_04 "{m}Да уж, её округлости равнодушным не оставят никого!{/m}"
    # jump open_site
    return

label cam0_ann_dressed_shop:
    if 'ann_dressed' in cam_flag:
        $ renpy.show('Ann cams dressed 11', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ ann.dress_inf = '01d'
        if 'ann_dressed_txt' not in cam_flag:
            $ cam_flag.append('ann_dressed_txt')
            Max_09 "{m}Ничего интересного я здесь уже не увижу, мама полностью оделась.{/m}"
        return

    $ cam_flag.append('ann_dressed')
    # $ spent_time += 10
    $ Wait(10)
    $ __list = ['03', '03a', '04'] if ann.dress=='d' else ['01', '01a', '02', '02a', '02b']  # частично одета. Может быть как с нижним бельём, так и без
    $ __ran1 = random_choice(__list)
    call ann_cam_dress_inf(__ran1) from _call_ann_cam_dress_inf_2

    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "{m}Вот и мама наряжается, чтобы отправиться на шопинг...{/m}"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __ran1 = random_choice(['05','06','07','08'])
    $ ann.dress_inf = '00'
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "{m}Ох! Голая мама - это восхитительное зрелище...{/m}"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    # $ spent_time += 10
    $ Wait(10)
    $ __ran1 = '10'
    call ann_cam_dress_inf(__ran1) from _call_ann_cam_dress_inf_3
    $ renpy.show('Ann cams dressed '+__ran1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    Max_04 "{m}Да уж, её округлости равнодушным не оставят никого!{/m}"
    return

label cam0_ann_resting:
    if tm < '19:00':
        $ renpy.show('Ann cams relax-morning '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    else:
        $ renpy.show('Ann cams relax-evening '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_resting' not in cam_flag:
        $ cam_flag.append('ann_resting')
        Max_01 "{m}Мама даже когда отдыхает, выглядит очень сексуально...{/m}"
    return

label cam0_ann_read:
    $ renpy.show('Ann cams reading '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_read' not in cam_flag:
        $ cam_flag.append('ann_read')
        Max_01 "{m}Мама увлечённо читает. Вроде бы ничего особенного, а смотреть на её округлые формы всё равно приятно!{/m}"
    return

label cam0_ann_sun:
    $ renpy.show('Ann cams sun '+cam_poses_manager(ann, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sun' not in cam_flag:
        $ cam_flag.append('ann_sun')
        Max_01 "{m}Самая горячая мама на свете загорает! Не повезло тем зрителям, которые это пропускают...{/m}"
    return

label cam1_ann_sun:
    show FG cam-shum-noact at laptop_screen
    if 'ann_sun1' not in cam_flag:
        $ cam_flag.append('ann_sun1')
        Max_09 "{m}Через эту камеру ничего не видно... Может посмотреть через другую?{/m}"
    return

label cam0_ann_swim:
    show FG cam-shum-noact at laptop_screen
    if 'ann_swim0' not in cam_flag:
        $ cam_flag.append('ann_swim0')
        if len(house[6].cams)>1:
            Max_09 "{m}Ничего толком не видно... Стоит взглянуть через другую камеру...{/m}"
        else:
            Max_09 "{m}Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн...{/m}"
    return

label cam1_ann_swim:
    $ renpy.show('Ann cams swim '+cam_poses_manager(ann, ['01', '02', '03', '04']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_01 "{m}На маму во дворе всегда приятно посмотреть...{/m}"
    return

label cam0_ann_alice_sun:
    $ renpy.show('Alice cams sun '+cam_poses_manager(alice, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    $ renpy.show('Ann cams sun '+cam_poses_manager(ann, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sun' not in cam_flag:
        $ cam_flag.append('ann_sun')
        $ cam_flag.append('alice_sun')
        Max_01 "{m}Две загорающих красотки - лучше чем одна...{/m}"
    return

label cam1_ann_alice_sun:
    show FG cam-shum-noact at laptop_screen
    if 'ann_sun1' not in cam_flag:
        $ cam_flag.append('ann_sun1')
        Max_09 "{m}Ничего толком не видно... Стоит взглянуть через другую камеру...{/m}"
    return

label cam0_ann_alice_swim:
    show FG cam-shum-noact at laptop_screen
    if 'ann_swim0' not in cam_flag:
        $ cam_flag.append('ann_swim0')
        if len(house[6].cams)>1:
            Max_09 "{m}Ничего толком не видно... Стоит взглянуть через другую камеру...{/m}"
        else:
            Max_09 "{m}Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн...{/m}"
    return

label cam1_ann_alice_swim:
    # Несовместимые спрайты с Алисой и Анной в бассейне:
    # alice-01 & ann-02
    # alice-01 & ann-04
    # alice-02 & ann-02
    # alice-02 & ann-04
    # alice-03 & ann-03
    $ __alice_pose = cam_poses_manager(alice, ['01', '02', '03', '04'])
    $ __ann_pose_list = {
            '01' : ['01', '03'],
            '02' : ['01', '03'],
            '03' : ['01', '02', '04'],
            '04' : ['01', '02', '03', '04'],
        }[__alice_pose]
    $ renpy.show('Alice cams swim '+__alice_pose, at_list=[laptop_screen])
    $ renpy.show('Ann cams swim '+cam_poses_manager(ann, __ann_pose_list), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim' not in cam_flag:
        $ cam_flag.append('ann_swim')
        $ cam_flag.append('alice_swim')
        Max_01 "{m}Две соблазнительные дамочки в бассейне, что может быть лучше? Только если бы они были ещё и голые!{/m}"
    return

label cam0_ann_bath:
    if tm[-2:] < '10':
        # набирает воду
        show Ann cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st0' not in cam_flag:
            $ cam_flag.append('ann_bath0_st0')
            Max_01 "{m}Такой шикарной попке, как у моей мамы, любая женщина может позавидовать...{/m}"
    elif tm[-2:] > '40':
        # вытирается
        show Ann cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st1' not in cam_flag:
            $ cam_flag.append('ann_bath0_st1')
            Max_04 "{m}Не вытирайся, мам, ходи мокренькая...{/m}"
    else:
        $ renpy.show('Ann cams bath '+cam_poses_manager(ann, ['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath0_st0' not in cam_flag:
            $ cam_flag.append('ann_bath0_st0')
            Max_05 "{m}И зачем нужны все эти эротические ролики в интернете, когда можно посмотреть на мою маму в ванне?!{/m}"
    return

label cam1_ann_bath:
    show FG cam-shum-noact at laptop_screen
    if 'ann_bath1' not in cam_flag:
        $ cam_flag.append('ann_bath1')
        Max_09 "{m}Мамы не видно через эту камеру... Может посмотреть через другую?{/m}"
    return

label cam0_ann_tv:
    $ renpy.show('Ann cams tv '+cam_poses_manager(ann, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'ann_tv' not in cam_flag:
        $ cam_flag.append('ann_tv')
        if check_is_home('eric'):
            Max_01 "{m}Как приятно видеть маму без Эрика. Может составить ей компанию, чтобы она не скучала?{/m}"
        else:
            Max_01 "{m}Мама, как всегда, отдыхает за просмотром сериала или фильма.{/m}"
    return
