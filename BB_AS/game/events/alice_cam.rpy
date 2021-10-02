
label cam0_alice_sleep_night:
    if 'sleep_fun' not in cam_flag and 'sleep_no_fun' not in cam_flag:
        $ cam_flag.append('sleep_fun' if all([alice.daily.massage==3, random_outcome(75), not alice.hourly.sleep, 'kira' in chars]) else 'sleep_no_fun')

    $ renpy.show('Alice cams sleep night '+cam_poses_manager(alice, ['01', '02', '03']), at_list=[laptop_screen])
    if not alice.sleepnaked:
        $ renpy.show('other Alice cams sleep night '+cam_poses_manager(alice, ['01', '02', '03'])+alice.dress, at_list=[laptop_screen])

    if flags.eric_jerk and '02:00'<=tm<'02:30':
        # показываем дрочащего Эрика
        if alice.sleepnaked:
            show Eric cams Alice-room 02 at laptop_screen
        else:
            show Eric cams Alice-room 01 at laptop_screen

    show FG cam-shum-act at laptop_screen

    if all(['sleep_fun' in cam_flag, tm < '2:00', 'alice_sleep_fun' not in cam_flag]):
        $ cam_flag.append('alice_sleep_fun')
        $ cam_flag.append('alice_sleep')
        # день веселья. начало
        hide other
        show Alice cams fun-in-bed 01 at laptop_screen
        Max_07 "Похоже, Алиса перед сном решила что-то посмотреть... Интересно, что?"

        $ renpy.show('Alice cams fun-in-bed 02'+renpy.random.choice(['a', 'b']), at_list=[laptop_screen])
        Max_02 "Ага! Теперь ясно... Порнушку она решила посмотреть... посасывая заодно свою игрушку..."

        $ renpy.show('Alice cams fun-in-bed 03'+renpy.random.choice(['a', 'b', 'c']), at_list=[laptop_screen])
        Max_06 "Ого! Видимо, массаж ног с конфетами очень завёл мою сестрёнку! Может, мне попробовать помассировать ей не только ноги в следующий раз?!"
        if not alice.flags.hip_mass:
            $ alice.flags.hip_mass = 1
            $ poss['naughty'].open(4)
        $ Wait(20)

    elif all(['sleep_fun' in cam_flag, 'alice_sleep_fun' in cam_flag, 'alice_end_sleep_fun' not in cam_flag]):
        $ cam_flag.append('alice_end_sleep_fun')
        # день веселья. интресное закончилось
        if alice.req.result == 'sleep':
            Max_04 "Ночное шоу закончилось. Теперь Алиса спит... без лифчика... Умничка!"
        elif alice.req.result == 'not_sleep' and not alice.req.noted:
            Max_09 "Ночное шоу закончилось. Теперь Алиса спит... но не всё так, как должно быть... Кое-что она забыла с себя снять!"
        else:
            Max_01 "Ночное шоу закончилось. Теперь Алиса спит..."

    elif all([flags.eric_jerk, '02:00'<=tm<'02:30', not eric.stat.mast, not flags.eric_noticed, 'eric_jerk' not in cam_flag]):
        # Эрик дрочит на Алису первый раз
        $ cam_flag.append('eric_jerk')
        $ flags.eric_noticed = True
        if prenoted:
            # уже заглядывали к Ане
            Max_09 "Эй, так вот же он! Что это он там делает, дрочит что ли? Да... Ого! Эрик стоит посреди ночи и дрочит на спящую Алису! А я и не знал, что Эрик любитель такого..."
        else:
            Max_09 "Опа, Эрик! Что это он там делает, дрочит что ли? Да... Ого! Эрик стоит посреди ночи и дрочит на спящую Алису! А я и не знал, что Эрик любитель такого..."

        menu:
            Max_03 "Может, попробовать осторожно подсмотреть за ним с балкона, а то как-то даже не верится?!"
            "{i}Конечно{/i}":
                jump first_jerk_balkon

    elif all([flags.eric_jerk, '02:00'<=tm<'02:30', eric.stat.mast, not flags.eric_noticed, 'eric_jerk'not in cam_flag]):
        # Эрик повторно дрочит на Алису
        $ cam_flag.append('eric_jerk')
        $ flags.eric_noticed = True
        if alice.sleepnaked:
            # Алиса спит голой, Эрик в комнате

            if 'eric.photo2' > 0:
                Max_03 "Ага! Эрик опять дрочит на Алису... Только теперь уже прямо в её комнате, перед ней! Вот же извращенец какой..."
            else:
                menu:
                    Max_03 "Ага! Эрик опять дрочит на Алису... Только теперь уже прямо в её комнате, перед ней! Вот же извращенец какой..."
                    "{i}Взять фотоаппарат и пойти к окну Алисы{/i}" ('lucky', 50):
                        jump jerk_photohant2
                    "{i}Да и хрен с ним, пусть дрочит{/i}":
                        pass
        else:
            # Алиса спит в белье, Эрик на балконе
            if 'eric.photo1' > 0:
                Max_09 "Эрик опять дрочит на Алису... В чём прикол?! Даже я до такого не опускаюсь..."
            else:
                menu:
                    Max_09 "Эрик опять дрочит на Алису... В чём прикол?! Даже я до такого не опускаюсь..."
                    "{i}Взять фотоаппарат и пойти на балкон{/i}" ('lucky', 50):
                        jump jerk_photohant1
                    "{i}Да и хрен с ним, пусть дрочит{/i}":
                        pass

    elif 'alice_sleep' not in cam_flag:
        $ cam_flag.append('alice_sleep')
        if alice.req.result == 'sleep':
            Max_04 "Алиса сейчас спит... без лифчика... Умничка!"
        elif alice.req.result == 'naked':
            Max_04 "Алиса сейчас спит... совсем голенькая и прекрасная..."
        elif alice.req.result in ['not_sleep', 'not_naked'] and not alice.req.noted:
            Max_09 "Алиса сейчас спит... но не всё так, как должно быть... Кое-что она забыла с себя снять!"
        else:
            Max_01 "Алиса сейчас спит..."
    return

label cam0_alice_sleep_morning:
    $ renpy.show('Alice cams sleep morning '+cam_poses_manager(alice, ['01', '02', '03']), at_list=[laptop_screen])
    if not alice.sleepnaked:
        $ renpy.show('other Alice cams sleep morning '+cam_poses_manager(alice, ['01', '02', '03'])+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_sleep' not in cam_flag:
        $ cam_flag.append('alice_sleep')
        if alice.req.result == 'sleep':
            Max_04 "Алиса ещё спит... без лифчика... Умничка!"
        elif alice.req.result == 'naked':
            Max_04 "Алиса сейчас спит... совсем голенькая и прекрасная..."
        elif alice.req.result in ['not_sleep', 'not_naked']:
            Max_09 "Алиса ещё спит... но не всё так, как должно быть... Кое-что она забыла с себя снять!"
        else:
            Max_01 "Алиса ещё спит..."
    return

label cam0_alice_shower:
    if tm[-2:] < '20' and alice.dress_inf != '00aa':
        show FG cam-shum-noact at laptop_screen
        if 'alice_not_shower' not in cam_flag:
            $ cam_flag.append('alice_not_shower')
            if len(house[3].cams)>1:
                Max_09 "Алисы не видно через эту камеру... Может посмотреть через другую?"
            else:
                Max_09 "Алисы не видно через эту камеру..."

    else:
        $ alice.dress_inf = '00aa'
        $ renpy.show('Alice cams shower 0'+str(cam_poses_manager(alice, [x for x in range(1, 10)])), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'alice_shower' not in cam_flag:
            $ cam_flag.append('alice_shower')
            Max_04 "Старшая сестрёнка принимает душ... Это зрелище, которое никогда мне не надоест..."
    return

label cam1_alice_shower:
    if tm[-2:] < '20' and alice.dress_inf != '00aa':
        # назначим или определим одёжку
        if alice.dress_inf != '04aa':
            $ __r1 = {'04ca':'a', '04da':'b', '02fa':'c', '00a':'d'}[alice.dress_inf]
        else:
            if alice.nopants:
                $ __r1 = renpy.random.choice(['b', 'd'])
            else:
                $ __r1 = renpy.random.choice(['a', 'c'])
            $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[__r1]

        $ renpy.show('Alice cams bath-mirror '+cam_poses_manager(alice, ['01', '02', '03'], 1)+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'alice_bath_mirror' not in cam_flag:
            $ cam_flag.append('alice_bath_mirror')
            Max_03 "Алиса, прежде чем принять душ, любуется собой перед зеркалом. А я и мои зрители с радостью полюбуемся этим через камеру..."

    else:
        show FG cam-shum-noact at laptop_screen
        if 'alice_shower1' not in cam_flag:
            $ cam_flag.append('alice_shower1')
            Max_09 "Алисы не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_alice_lisa_shower:
    # выбор, кто из персонажей принимает душ
    if 'alice_sh' in cam_flag:
        $ __var = 'alice' if tm[-2:] < '30' else 'lisa' # в первой половине часа в душе Алиса
    elif 'lisa_sh' in cam_flag:
        $ __var = 'lisa' if tm[-2:] < '30' else 'alice' # в первой половине часа в душе Лиза
    elif 'lisa_alice_sh' in cam_flag:
        $ __var = 'lisa_alice'
    else:
        $ __var = renpy.random.choice(['alice', 'lisa_alice', 'lisa', 'lisa_alice'])
        if __var == 'alice':
            $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'lisa_sh')
        elif __var == 'lisa':
            $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'alice_sh')
        else:
            $ cam_flag.append('lisa_alice_sh')

    if __var == 'alice':
        # в душе Алиса, Лиза перед умывальниками
        $ alice.dress_inf != '00aa'
        $ renpy.show('Alice cams shower 0'+str(cam_poses_manager(alice, [x for x in range(1, 10)])), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'alice_shower' not in cam_flag:
            $ cam_flag.append('alice_shower')
            Max_04 "Старшая сестрёнка принимает душ... Это зрелище, которое никогда мне не надоест..."
            if 'lisa_mirror' not in cam_flag:
                # Лизу ещё не видели
                if len(house[3].cams)>1:
                    Max_09 "Лиза, должно быть, красуется перед зеркалом. Надо взглянуть через другую камеру..."
                else:
                    Max_09 "Лиза, должно быть, красуется перед зеркалом, но здесь этого не увидеть..."
    elif __var == 'lisa':
        # в душе Лиза, перед умывальниками Алиса
        $ lisa.dress_inf != '00a'
        $ renpy.show('Lisa cams shower 0'+str(cam_poses_manager(lisa, [x for x in range(1, 10)])), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_05 "Младшая сестрёнка принимает душ... На её прелести я мог бы смотреть часами..."
            if 'alice_mirror' not in cam_flag:
                # Алису ещё не видели
                if len(house[3].cams)>1:
                    Max_09 "Алиса, должно быть, красуется перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_09 "Алиса, должно быть, красуется перед зеркалом, но здесь этого не увидеть..."
    else:
        # обе девчонки в душе, у зеркал никого
        $ lisa.dress_inf != '00a'
        $ alice.dress_inf != '00aa'
        $ renpy.show('Alice cams shower 0'+str(cam_poses_manager(alice, [x for x in range(1, 9)])), at_list=[cam_shower_right])
        $ renpy.show('Lisa cams shower 0'+str(cam_poses_manager(lisa, [x for x in range(1, 8)])), at_list=[cam_shower_left])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_05 "Обе мои сестрёнки сейчас принимают душ. Глаз не отвести..."
    return

label cam1_alice_lisa_shower:
    # выбор, кто из персонажей принимает душ
    if 'alice_sh' in cam_flag:
        $ __var = 'lisa' if tm[-2:] < '30' else 'alice' # в первой половине часа перед зеркалом Лиза
    elif 'lisa_sh' in cam_flag:
        $ __var = 'alice' if tm[-2:] < '30' else 'lisa' # в первой половине часа перед зеркалом Алиса
    elif 'lisa_alice_sh' in cam_flag:
        $ __var = 'lisa_alice'
    else:
        $ __var = renpy.random.choice(['alice', 'lisa_alice', 'lisa', 'lisa_alice'])
        if __var == 'alice':
            $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'alice_sh')
        elif __var == 'lisa':
            # перед умывальниками первые полчаса Лиза
            $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'lisa_sh')
        else:
            $ cam_flag.append('lisa_alice_sh')


    if __var == 'lisa':
        # перед умывальниками Лиза, Алису не видно, она сейчас в душе
        if tm[-2:] < '10' and lisa.dress_inf != '00a' and 'bathrobe' in lisa.gifts: # начало часа, Лизу в душе не видели, у нее есть халат
            $ __r1 = 'a'
        elif tm[-2:] < '20' and lisa.dress_inf not in ['00a', '00']: # Лизу не видели голой
            $ __r1 = 'c'
        else:
            $ __r1 = 'd'
        $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[__r1]
        $ renpy.show('Lisa cams bath-mirror '+cam_poses_manager(alice, ['01', '02', '03'], 1)+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'lisa_mirror' not in cam_flag:
            $ cam_flag.append('lisa_mirror')
            Max_03 "Лиза внимательно разглядывает себя в зеркало... А я и мои зрители с радостью полюбуемся на это через камеру..."
    elif __var == 'alice':
        # перед умывальниками Алиса, Лизу не видно, она сейчас в душе
        if tm[-2:] < '10' and alice.dress_inf != '00aa': # первая треть часа, Алису в душе не видели
            $ __r1 = 'a'
        elif tm[-2:] < '20' and alice.dress_inf not in ['00a', '00aa']:
            $ __r1 = 'c'
        else:
            $ __r1 = 'd'
        $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[__r1]
        $ renpy.show('Alice cams bath-mirror '+cam_poses_manager(alice, ['01', '02', '03'], 1)+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'alice_mirror' not in cam_flag:
            $ cam_flag.append('alice_mirror')
            Max_05 "Ух, старшая сестрёнка просто сногсшибательна..."
    else:
        show FG cam-shum-noact at laptop_screen
        if 'alice_shower1' not in cam_flag:
            $ cam_flag.append('alice_shower1')
            Max_09 "Через эту камеру никого не видно... Может посмотреть через другую?"

    return

label alice_cam_dress_inf(r1):
    $ alice.dress_inf = {
            '01':'02b',
            '02':'02e',
            '02a':'02c',
            '03':'01h',
            '04':'02h',
            '05':'02fa',
            '06':'00',
            '07':'00',
            '08':'00',
            '09':'00a',
            '10':'02d',
            '10a':'02a',
            '11':'06a',
            '11a':'06b',
            '12':'01',
            '13':'06',
        }[r1]
    return

label cam0_alice_dressed_shop:

    if 'alice_dressed' in cam_flag:
        $ renpy.show('Alice cams dressed 12', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ alice.dress_inf = '01'
        if 'alice_dressed_txt' not in cam_flag:
            $ cam_flag.append('alice_dressed_txt')
            Max_09 "Ничего интересного я здесь уже не увижу, Алиса полностью оделась."
        return

    $ cam_flag.append('alice_dressed')
    # $ spent_time += 10
    $ Wait(10)

    if alice.dress in ['a', 'c']:
        $ __r1 = renpy.random.choice(['01', '02a']) if alice.nopants else renpy.random.choice(['01', '02'])
    elif alice.dress == 'b':
        $ __r1 = '03' # нет спрайта, временно ставим в одних
    elif alice.dress == 'd':
        $ __r1 = '04'
    call alice_cam_dress_inf(__r1) from _call_alice_cam_dress_inf

    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "Ага! Алиса наряжается, чтобы отправиться на шопинг..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['06','07','08'])
    call alice_cam_dress_inf(__r1) from _call_alice_cam_dress_inf_1
    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "О да! Сейчас она совсем голенькая..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    # $ spent_time += 10
    $ Wait(10)
    if alice.req.result == 'not_nopants':
        $ renpy.show('Alice cams dressed 10', at_list=[laptop_screen])
        call alice_cam_dress_inf('10') from _call_alice_cam_dress_inf_2
        Max_01 "Похоже, пойдёт она в трусиках, а не должна... Считай, сестрёнка, ты попала!"
    elif alice.req.result == 'nopants':
        $ renpy.show('Alice cams dressed 10a', at_list=[laptop_screen])
        call alice_cam_dress_inf('10a') from _call_alice_cam_dress_inf_3
        Max_05 "Ого! Алиса даже на шопинг пойдёт без трусиков! Интересно, что она скажет маме в кабинке для переодевания, если та это заметит?"
    else:
        $ renpy.show('Alice cams dressed 10', at_list=[laptop_screen])
        call alice_cam_dress_inf('10') from _call_alice_cam_dress_inf_4
        Max_04 "Какая соблазнительная попка у неё... Уверен, зрителям это нравится!"
    return

label cam0_alice_dressed_friend:
    if 'alice_dressed' in cam_flag:
        $ renpy.show('Alice cams dressed 12', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ alice.dress_inf = '01'
        if 'alice_dressed_txt' not in cam_flag:
            $ cam_flag.append('alice_dressed_txt')
            Max_09 "Ничего интересного я здесь уже не увижу, Алиса полностью оделась."
        return

    $ cam_flag.append('alice_dressed')
    # $ spent_time += 10
    $ Wait(10)

    if alice.dress in ['a', 'c']:
        $ __r1 = renpy.random.choice(['01', '02a']) if alice.nopants else renpy.random.choice(['01', '02'])
    elif alice.dress == 'b':
        $ __r1 = '03' # нет спрайта, временно ставим в одних
    elif alice.dress == 'd':
        $ __r1 = '04'
    call alice_cam_dress_inf(__r1) from _call_alice_cam_dress_inf_5

    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "Ага! Алиса наряжается, чтобы куда-то отправиться..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['06','07','08'])
    call alice_cam_dress_inf(__r1) from _call_alice_cam_dress_inf_6
    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "О да! Сейчас она совсем голенькая..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    # $ spent_time += 10
    $ Wait(10)
    if alice.req.result == 'not_nopants':
        $ renpy.show('Alice cams dressed 10', at_list=[laptop_screen])
        call alice_cam_dress_inf('10') from _call_alice_cam_dress_inf_7
        Max_01 "Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала!"
    elif alice.req.result == 'nopants':
        $ renpy.show('Alice cams dressed 10a', at_list=[laptop_screen])
        call alice_cam_dress_inf('10a') from _call_alice_cam_dress_inf_8
        Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Надеюсь, кто-то это заметит там, куда она идёт..."
    else:
        $ renpy.show('Alice cams dressed 10', at_list=[laptop_screen])
        call alice_cam_dress_inf('10') from _call_alice_cam_dress_inf_9
        Max_04 "Трусики хорошо смотрятся на её попке. Но без них было бы лучше..."
    return

label cam0_alice_dressed_club:
    if 'alice_dressed' in cam_flag:
        $ renpy.show('Alice cams dressed 13', at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        $ alice.dress_inf = '06'
        if 'alice_dressed_txt' not in cam_flag:
            $ cam_flag.append('alice_dressed_txt')
            Max_09 "Ничего интересного я здесь уже не увижу, Алиса полностью оделась."
        return

    $ cam_flag.append('alice_dressed')
    $ Wait(10)

    $ __r1 = '05'
    call alice_cam_dress_inf(__r1) from _call_alice_cam_dress_inf_10

    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_07 "Ага! Алиса наряжается, чтобы отправиться в клуб..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['06','07','08'])
    call alice_cam_dress_inf(__r1) from _call_alice_cam_dress_inf_11
    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_02 "О да! Сейчас она совсем голенькая..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ Wait(10)
    if alice.req.result == 'not_nopants':
        $ renpy.show('Alice cams dressed 11', at_list=[laptop_screen])
        call alice_cam_dress_inf('11') from _call_alice_cam_dress_inf_12
        Max_01 "Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала!"
    elif alice.req.result == 'nopants':
        $ renpy.show('Alice cams dressed 11a', at_list=[laptop_screen])
        call alice_cam_dress_inf('11a') from _call_alice_cam_dress_inf_13
        Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Это платье без трусиков смотрится гораздо лучше... Интересно, в клубе на это кто-нибудь обратит внимание?"
    else:
        $ renpy.show('Alice cams dressed 11', at_list=[laptop_screen])
        call alice_cam_dress_inf('11') from _call_alice_cam_dress_inf_14
        Max_04 "Трусики хорошо смотрятся на её попке. Но без них это платье смотрелось бы гораздо лучше..."
    return

label cam0_alice_rest_morning:
    $ renpy.show('Alice cams morning 01'+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_morning' not in cam_flag:
        $ cam_flag.append('alice_morning')
        Max_01 "Алиса валяется со своим ноутбуком. Смотрится неплохо..."
    return

label cam0_alice_dishes:
    $ renpy.show('Alice cams crockery 01'+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_dishes' not in cam_flag:
        $ cam_flag.append('alice_dishes')
        Max_01 "Алиса моет посуду. Правильно, нечего весь день прохлаждаться во дворе и за ноутбуком..."
    return

label cam0_alice_read:
    $ renpy.show('Alice cams reading '+cam_poses_manager(alice, ['01', '02', '03'])+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_read' not in cam_flag:
        $ cam_flag.append('alice_read')
        Max_07 "Так, Алиса просто читает. Не особо интересно."
        if poss['secretbook'].st() > 2:
            Max_09 "Хотя, книжки она читает эротического жанра, может она возбудится и начнёт себя трогать..."
    return

label cam0_alice_smoke:
    show FG cam-shum-noact at laptop_screen
    if 'alice_smoke' not in cam_flag:
        $ cam_flag.append('alice_smoke')
        if alice.dcv.special.stage < 1:
            Max_09 "Алиса должна быть во дворе, но через камеру её не видно... Интересно, где она?!"
        else:
            Max_01 "Алиса должна быть во дворе, но через камеру её не видно... Наверное, опять курит..."
    return

label cam1_alice_smoke:
    show FG cam-shum-noact at laptop_screen
    return

label cam0_alice_sun:
    if alice.daily.oiled == 2:
        show Alice cams sun-alone 00a at laptop_screen
    elif alice.daily.oiled > 0:
        show Alice cams sun-alone 00 at laptop_screen
    else:
        $ renpy.show('Alice cams sun '+cam_poses_manager(alice, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_sun0' not in cam_flag:
        $ cam_flag.append('alice_sun0')
        Max_01 "Загорающая Алиса радует глаза зрителей! Ну и мои заодно..."
    return

label cam1_alice_sun:
    if alice.daily.oiled == 2:
        show Alice cams sun-alone 01a at laptop_screen
    elif alice.daily.oiled > 0:
        show Alice cams sun-alone 01 at laptop_screen

    if alice.daily.oiled:
        show FG cam-shum-act at laptop_screen
    else:
        show FG cam-shum-noact at laptop_screen

    if 'alice_sun1' not in cam_flag:
        $ cam_flag.append('alice_sun1')
        if alice.daily.oiled:
            if 'alice_sun0' not in cam_flag:
                Max_01 "Загорающая Алиса радует глаза зрителей! Ну и мои заодно..."
        else:
            Max_09 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_alice_swim:
    show FG cam-shum-noact at laptop_screen
    if 'alice_swim0' not in cam_flag:
        $ cam_flag.append('alice_swim0')
        if len(house[6].cams)>1:
            Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
        else:
            Max_09 "Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн..."
    return

label cam1_alice_swim:
    $ renpy.show('Alice cams swim '+cam_poses_manager(alice, ['01', '02', '03', '04']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'alice_swim1' not in cam_flag:
        $ cam_flag.append('alice_swim1')
        Max_01 "На мокренькую старшую сестрёнку всегда приятно взглянуть..."
    return

label cam0_alice_cooking_dinner:
    $ renpy.show('Alice cams cooking 01'+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_cooking' not in cam_flag:
        $ cam_flag.append('alice_cooking')
        Max_01 "Алиса готовит ужин. А могла бы и попкой покрутить заодно..."
    return

label cam0_alice_rest_evening:

    if 'blog_fun' not in cam_flag and 'blog_no_fun' not in cam_flag:
        if weekday in [0, 2]:
            $ cam_flag.append('blog_fun' if all([random_outcome(50), poss['blog'].st()>1, 'kira' in chars]) else 'blog_no_fun')
        elif all([weekday == 6, poss['blog'].st()>1, 'kira' in chars]):
            $ cam_flag.append('blog_fun')
        else:
            $ cam_flag.append('blog_no_fun')

    $ renpy.show('Alice cams evening 01'+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if all([tm > '21:00', 'alice_evening' in cam_flag, 'blog_fun' in cam_flag, 'alice_blog_fun' not in cam_flag]):
        $ cam_flag.append('alice_blog_fun')
        # день развлечения. Развлечение начинается
        $ __suf = 'a' if alice.dress =='a' and alice.nopants else ''
        $ renpy.show('Alice cams fun-at-desk 02'+alice.dress+__suf, at_list=[laptop_screen])
        Max_03 "Ого! Похоже, начинается что-то интересненькое! Алиса решила снять лишнюю одежду и поразвлечься?!"

        $ __suf = 'a' if alice.dress in ['a', 'c'] else alice.dress
        $ renpy.show('Alice cams fun-at-desk '+renpy.random.choice(['03', '04'])+__suf, at_list=[laptop_screen])
        Max_05 "Вот так, сестрёнка! То, как ты ласкаешь киску и посасываешь свою игрушку что мне, что зрителям, однозначно нравится..."

        if not alice.stat.mast:
            Max_02 "А ведь Алиса прекрасно бы смотрелась в роли тех девчонок, которые развлекают народ тем, что раздеваются на камеру и ласкают себя... Всё прибыльнее, чем эта её косметика! Надо бы ей на это как-то легонько намекнуть..."
            $ alice.dcv.feature.set_lost(1)

        $ alice.stat.mast += 1
        $ Wait(20)

    elif all([tm >= '21:00', 'alice_blog_fun' in cam_flag, 'alice_end_blog_fun' not in cam_flag]):
        $ cam_flag.append('alice_end_blog_fun')
        # день развлечения. развлечение закончилось
        Max_07 "К сожалению, шоу закончилось и теперь Алиса просто занимается своим блогом..."

    elif 'alice_evening' not in cam_flag:
        #
        $ cam_flag.append('alice_evening')
        if 'blog_fun' in cam_flag:
            Max_07 "Алиса занимается своим блогом. Ничего интересного не намечается. Хотя... как знать, может стоит подождать..."
        else:
            Max_07 "Алиса занимается своим блогом. Ничего интересного не намечается..."

    return

label cam0_alice_tv:
    $ renpy.show('Alice cams tv '+cam_poses_manager(alice, ['01', '02', '03'])+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'alice_tv' not in cam_flag:
        $ cam_flag.append('alice_tv')
        Max_01 "Алиса смотрит ТВ. Наверняка залипла в какие-нибудь сериалы..."
    return

label cam0_alice_bath:
    if tm[-2:] < '10':
        # набирает воду
        show Alice cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'alice_bath0_st0' not in cam_flag:
            $ cam_flag.append('alice_bath0_st0')
            Max_01 "Алиса ещё только набирает воду, а вид уже классный!"
    elif tm[-2:] > '40':
        # вытирается
        show Alice cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'alice_bath0_st1' not in cam_flag:
            $ cam_flag.append('alice_bath0_st1')
            Max_04 "Не спеши, Алиса. Вытирайся помедленнее..."
    else:
        $ renpy.show('Alice cams bath '+cam_poses_manager(alice, ['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'alice_bath0_st0' not in cam_flag:
            $ cam_flag.append('alice_bath0_st0')
            Max_05 "Это самый лучший ракурс, чтобы понаблюдать за тем, как Алиса принимает ванну! Заглядение..."
    return

label cam1_alice_bath:
    show FG cam-shum-noact at laptop_screen
    if 'alice_bath1' not in cam_flag:
        $ cam_flag.append('alice_bath1')
        Max_09 "Алисы не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_alice_blog_lingerie:
    if not alice.dcv.feature.done:
        call cam0_alice_rest_evening from _call_cam0_alice_rest_evening
        return

    $ renpy.dynamic('cur_pose')
    if not len(cam_pose_blog):
        # заполняем список поз
        $ cam_pose_blog = ['01', '02', '03', '04', '05', '06']
        $ renpy.random.shuffle(cam_pose_blog)
    $ cur_pose = cam_poses_manager(alice, cam_pose_blog)
    $ alice.dress_inf = {'a':'02', 'b':'02ia', 'c':'02ka', 'd':'02la'}[alice.dress]
    $ renpy.show('Alice cams blog '+cur_pose+alice.dress, at_list=[laptop_screen,])
    show FG cam-shum-act at laptop_screen
    if cur_pose in cam_pose_blog:
        $ cam_pose_blog.remove(cur_pose)
        if not len(cam_pose_blog):
            $ cam_pose_blog.append('01')
    if 'alice_blog' not in cam_flag:
        $ cam_flag.append('alice_blog')
        if cur_pose == '01':
            Max_02 "Сегодня Алиса занимается блогом в нижнем белье! Это уже поинтереснее..."
        else:
            Max_04 "Правильно, сестрёнка! Нужно хорошенько попозировать... А если бы ты ещё и раздевалась, вот это было бы шоу!"
    return

label cam0_alice_after_club:
    if tm[-2:] < '20':
        show FG cam-shum-noact at laptop_screen
        if 'alice_not_bath' not in cam_flag:
            $ cam_flag.append('alice_not_bath')
            if len(house[3].cams)>1:
                Max_09 "Алисы не видно через эту камеру... Может посмотреть через другую?"
            else:
                Max_09 "Алисы не видно через эту камеру..."
    elif tm[-2:] > '30':
        # вытирается
        show Alice cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'alice_bath0_st1' not in cam_flag:
            $ cam_flag.append('alice_bath0_st1')
            Max_04 "Не спеши, Алиса. Вытирайся помедленнее..."
    else:
        $ renpy.show('Alice cams bath '+cam_poses_manager(alice, ['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'alice_bath0_st0' not in cam_flag:
            $ cam_flag.append('alice_bath0_st0')
            Max_05 "Это самый лучший ракурс, чтобы понаблюдать за тем, как Алиса принимает ванну! Заглядение..."
    return

label cam1_alice_after_club:
    if tm[-2:] < '20':
        # Алиса перед зеркалом
        $ __r1 = 'b' if alice.nopants else 'a'
        $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[__r1]

        $ renpy.show('Alice cams bath-mirror '+cam_poses_manager(alice, ['01', '02', '03'], 1)+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'alice_bath_mirror' not in cam_flag:
            $ cam_flag.append('alice_bath_mirror')
            Max_01 "Алиса вернулась из клуба."
    else:
        show FG cam-shum-noact at laptop_screen
        if 'alice_bath1' not in cam_flag:
            $ cam_flag.append('alice_bath1')
            Max_09 "Алисы не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_blog_with_Eric:
    if alice.dcv.intrusion.stage == 8:
        #если Эрик купил Алисе чёрное кружевное боди вперёд Макса

        # cam-blog-desk-eric-(03/03a) + cam-blog-dresses-alice-(02a/02b/02c или 03a/03b/03c)
        $ renpy.show('Eric cams blog 03'+eric.dress, at_list=[laptop_screen])
        $ renpy.show('Alice cams blog dresses 0'+str(renpy.random.randint(2, 3))+alice.dress, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen

        Max_09 "{m}Эрик о чём-то разговаривает с Алисой. И развалился так, как будто это его комната...{/m}"

        # cam-blog-desk-eric-(03/03a) + cam-blog-dresses-alice-(04a/04b/04c или 05a/05b/05c)
        $ renpy.show('Alice cams blog dresses 0'+str(renpy.random.randint(4, 5))+alice.dress, at_list=[laptop_screen])
        Max_08 "{m}Ого! Да она при нём, похоже, переодеваться вздумала! Что сказать, Эрик умеет добиваться своего...{/m}"

        # cam-blog-desk-eric-(04/04a) + cam-blog-dresses-alice-(07a/07b)
        $ renpy.show('Eric cams blog 04'+eric.dress, at_list=[laptop_screen])
        $ renpy.show('Alice cams blog dresses 07'+renpy.random.choice(['a', 'b']), at_list=[laptop_screen])
        Max_01 "{m}Голая и прекрасная Алиса! Сказала Эрику не подглядывать, только вот он точно во всю глазеет сквозь пальцы... Я бы уж точно рискнул так близко поглазеть на голую Алису!{/m}"

        # cam-blog-desk-eric-(04/04a) + cam-blog-dresses-alice-(08a/08b)
        $ renpy.show('Alice cams blog dresses 08'+renpy.random.choice(['a', 'b']), at_list=[laptop_screen])
        Max_07 "{m}Ухх... Алиса не спешит спрятать свои аппетитные сисечки под боди! Хм, а может она заметила, что Эрик всё равно подглядывает и таким образом дразнит его?! И не подозревает, что заодно и меня...{/m}"

        # cam-blog-desk-eric-(03/03a) + cam-blog-dresses-alice-(09a/09b)
        $ renpy.show('Eric cams blog 03'+eric.dress, at_list=[laptop_screen])
        $ renpy.show('Alice cams blog dresses 09'+renpy.random.choice(['a', 'b']), at_list=[laptop_screen])
        Max_09 "{m}Понятно всё с вами, Алиса села на шею Эрику, а он и рад. Эх, Алиса... надеюсь, ты знаешь, что делаешь...{/m}"
        #после этого через камеру можно увидеть 2 варианта того, что делают Алиса и Эрик, либо она сидит он стоит рядом, либо она позирует он сидит на кровати

        $ alice.dcv.intrusion.stage = 9  # бельё Алисе подарил Эрик
        # $ alice.dress = 'd'
        # $ alice.dress_inf = '02la'
        # $ blog_lingerie = ['d', 'd', 'd']
        $ alice.gifts.append('sexbody2')
        $ setting_clothes_by_conditions()
        $ infl[alice].add_e(40)
        $ poss['blog'].open(16)
        $ spent_time = max((60 - int(tm[-2:])), 30)
        jump Waiting
    else:
        # cam-blog-desk-alice-(01d/01e/01f/01g - после дарения) + cam-blog-desk-eric-(01(a) или 02(a))
        if alice.dcv.intrusion.stage>4:
            # кружевное боди подарено
            $ __r = renpy.random.randint(1, 2)
            $ renpy.show('Eric cams blog 0'+str(__r)+eric.dress, at_list=[laptop_screen])
            if __r<2:
                $ renpy.show('Alice cams blog 01'+alice.dress, at_list=[laptop_screen])
            else:
                $ renpy.show('Alice cams blog 0'+str(renpy.random.randint(1, 6))+alice.dress, at_list=[laptop_screen])
        else:
            $ renpy.show('Eric cams blog 01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Alice cams blog 01'+alice.dress, at_list=[laptop_screen])

        show FG cam-shum-act at laptop_screen

        Max_08 "{m}Эрик сегодня в комнате Алисы. Похоже, пытается помогать с блогом... Но в действительности же, чтобы поглазеть на Алису в белье, по себе знаю...{/m}"

        if not poss['blog'].used(14):
            $ poss['blog'].open(13)

        return
