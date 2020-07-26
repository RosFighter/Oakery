
label cam0_alice_read:
    $ renpy.show('Alice cams reading '+renpy.random.choice(['01', '02', '03'])+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_read' not in cam_flag:
        $ cam_flag.append('alice_read')
        Max_07 "Так, Алиса просто читает. Не особо интересно."
        if poss['secretbook'].stn > 2:
            Max_09 "Хотя, книжки она читает эротического жанра, может она возбудится и начнёт себя трогать..."
    return

label cam0_alice_sun:
    if talk_var['sun_oiled'] == 2:
        show Alice cams sun-alone 00a at laptop_screen
    elif talk_var['sun_oiled'] > 0:
        show Alice cams sun-alone 00 at laptop_screen
    else:
        $ renpy.show('Alice cams sun '+renpy.random.choice(['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_sun0' not in cam_flag:
        $ cam_flag.append('alice_sun0')
        Max_00 "Загорающая Алиска радует глаза зрителей! Ну и мои заодно..."
    return

label cam1_alice_sun:
    if talk_var['sun_oiled'] == 2:
        show Alice cams sun-alone 00a at laptop_screen
    elif talk_var['sun_oiled'] > 0:
        show Alice cams sun-alone 00 at laptop_screen

    show FG cam-shum-act at laptop_screen
    if 'alice_sun1' not in cam_flag:
        $ cam_flag.append('alice_sun1')
        if talk_var['sun_oiled']:
            Max_00 "Загорающая Алиска радует глаза зрителей! Ну и мои заодно..."
        else:
            Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_alice_rest_morning:
    $ renpy.show('Alice cams morning 01'+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_morning' not in cam_flag:
        $ cam_flag.append('alice_morning')
        Max_00 "Алиска валяется с ноутбуком. Ничего интересного пока..."
    return

label cam0_alice_rest_evening:
    $ renpy.show('Alice cams evening 01'+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_evening' not in cam_flag:
        $ cam_flag.append('alice_evening')
        Max_00 "Алиска что-то делает за ноутбуком. Пока ничего интересного..."
    return

label cam0_alice_swim:
    show FG cam-shum-act at laptop_screen
    if 'alice_swim0' not in cam_flag:
        $ cam_flag.append('alice_swim0')
        if len(house[6].cams)>1:
            Max_00 "Ничего толком не видно... Стоит взглянуть с другой камеры..."
        else:
            Max_00 "Ничего не разглядеть... Нужно установить камеру охватывающую бассейн..."
    return

label cam1_alice_swim:
    $ renpy.show('Alice cams swim '+renpy.random.choice(['01', '02', '03', '04']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_swim1' not in cam_flag:
        $ cam_flag.append('alice_swim1')
        Max_00 "На старшую сестрёнку всегда приятно взглянуть..."
    return

label cam0_alice_dressed_shop:
    $ __list = {
            'a':['01', '02', '03'],
            'b':['02',],
            'c':['02','03'],
            'd':['02','03','05']
        }[alice.dress]
    $ __ran1 = renpy.random.choice(__list)

    $ __suf = 'a' if all([__ran1 != '01', 'smoke' in talk_var, flags['smoke'] == 'nopants']) else ''
    if flags['smoke'] == 'not_nopants':
        $ flags['noted'] = True

    $ alice.dress_inf = {
            '01':'02b',
            '02':'02a' if __suf else '02d',
            '03':'02c' if __suf else '02e',
            '05':'02h',
        }[__ran1]

    $ renpy.show('Alice cams dressed '+__ran1+__suf, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_dressed' not in cam_flag:
        $ cam_flag.append('alice_dressed')
        if flags['smoke'] == 'not_nopants' and __ran1 not in ['01', '05']:
            # на Алисе трусики, когда их быть не должно
            Max_01 "Ага! Алиса одевается на шопинг. И похоже, пойдёт она в трусиках, а не должна... Считай, сестрёнка, ты попала!"
        elif flags['smoke'] == 'nopants' and __ran1 not in ['01', '05']:
            # Макс видит, что Алиса соблюдает договоренность
            Max_05 "Ого! Алиса даже на шопинг пойдёт без трусиков! Интересно, что она скажет маме в кабинке для переодевания, если та это заметит?"
        elif __ran1 in ['02', '03']:
            # Если нет договоренности по поводу трусов
            Max_04 "Алиса переодевается... Какая соблазнительная попка у неё... Уверен, зрителям это нравится!"
        else:
            # Сиськи , однако
            Max_03 "О, какой вид! Да, сестрёнка, такими классными и голыми сиськами грех не покрасоваться перед зеркалом... Зрители, наверное, без ума от них!"
    return

label cam0_alice_dressed_friend:
    $ __list = {
            'a':['01', '02', '03'],
            'b':['02',],
            'c':['02','03'],
            'd':['02','03','05']
        }[alice.dress]
    $ __ran1 = renpy.random.choice(__list)

    $ __suf = 'a' if all([__ran1 != '01', 'smoke' in talk_var, flags['smoke'] == 'nopants']) else ''
    if flags['smoke'] == 'not_nopants':
        $ flags['noted'] = True

    $ alice.dress_inf = {
            '01':'02b',
            '02':'02a' if __suf else '02d',
            '03':'02c' if __suf else '02e',
            '05':'02h',
        }[__ran1]

    $ renpy.show('Alice cams dressed '+__ran1+__suf, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_dressed' not in cam_flag:
        $ cam_flag.append('alice_dressed')
        if flags['smoke'] == 'not_nopants' and __ran1 not in ['01', '05']:
            # на Алисе трусики, когда их быть не должно
            Max_01 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала!"
        elif flags['smoke'] == 'nopants' and __ran1 not in ['01', '05']:
            # Алиса соблюдает договоренность
            Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Надеюсь, кто-то это заметит там, куда она идёт..."
        elif __ran1 in ['02', '03']:
            # нет договоренности по поводу трусов
            Max_04 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Но без них было бы лучше..."
        else:
            # Сиськи , однако
            Max_03 "О, какой вид! Да, сестрёнка, такими классными и голыми сиськами грех не покрасоваться перед зеркалом..."
    return

label cam0_alice_dressed_club:
    if 'smoke' in talk_var and flags['smoke'] == 'nopants':
        $ __suf = 'a'
        $ alice.dress_inf = '06b'
    else:
        $ __suf = ''
        $ alice.dress_inf = '06a'
    if 'smoke' in talk_var and flags['smoke'] == 'not_nopants':
        $ flags['noted'] = True
    $ renpy.show('Alice cams dressed 04'+__suf, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_dressed' not in cam_flag:
        $ cam_flag.append('alice_dressed')
        if flags['smoke'] == 'not_nopants':
            ## Алиса в трусиках, но их быть не должно
            Max_01 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала!"
        elif flags['smoke'] == 'nopants':
            ## Алиса без трусиков, как и должна
            Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Это платье без трусиков смотрится гораздо лучше... Интересно, в клубе на это кто-нибудь обратит внимание?"
        else:
            ## Алиса в трусиках. Договоренностей нет
            Max_04 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Но без них это платье смотрелось бы гораздо лучше..."
    return
