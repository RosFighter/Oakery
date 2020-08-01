
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

label alice_cam_dress_inf(r1):
    $ alice.dress_inf = {
            '01':'02b',
            '02':'02e',
            '02a':'02c',
            '03':'02h',
            '04':'02fa',
            '05':'00',
            '06':'00',
            '07':'00',
            '08':'00a',
            '09':'02d',
            '09a':'02a',
            '10':'06a',
            '10a':'06b',
            '11':'01',
            '12':'06',
        }[r1]
    return

label cam0_alice_dressed_shop:

    if 'alice_dressed' in cam_flag:
        $ renpy.show('Alice cams dressed 11', at_list=[laptop_screen])
        $ alice.dress_inf = '01'
        if 'alice_dressed_txt' not in cam_flag:
            $ cam_flag.append('alice_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('alice_dressed')
    $ spent_time += 10

    if alice.dress in ['a', 'c']:
        $ __r1 = renpy.random.choice(['01', '02a']) if alice.nopants else renpy.random.choice(['01', '02'])
    elif alice.dress = 'b':
        $ __r1 = '04' # нет спрайта, временно ставим в одних
    elif alice.dress = 'd':
        $ __r1 = '03'
    call alice_cam_dress_inf(__r1)

    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ага! Алиса одевается на шопинг..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['05','06','07'])
    call alice_cam_dress_inf(__r1)
    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого, вот это вид!!!"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    if flags['smoke'] == 'not_nopants':
        $ renpy.show('Alice cams dressed 09', at_list=[laptop_screen])
        call alice_cam_dress_inf('09')
        Max_01 "Похоже, пойдёт она в трусиках, а не должна... Считай, сестрёнка, ты попала!"
    elif flags['smoke'] == 'nopants':
        $ renpy.show('Alice cams dressed 09a', at_list=[laptop_screen])
        call alice_cam_dress_inf('09a')
        Max_05 "Ого! Алиса даже на шопинг пойдёт без трусиков! Интересно, что она скажет маме в кабинке для переодевания, если та это заметит?"
    else:
        $ renpy.show('Alice cams dressed 09', at_list=[laptop_screen])
        call alice_cam_dress_inf('09')
        Max_04 "Какая соблазнительная попка у неё... Уверен, зрителям это нравится!"
    return

label cam0_alice_dressed_friend:
    if 'alice_dressed' in cam_flag:
        $ renpy.show('Alice cams dressed 11', at_list=[laptop_screen])
        $ alice.dress_inf = '01'
        if 'alice_dressed_txt' not in cam_flag:
            $ cam_flag.append('alice_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('alice_dressed')
    $ spent_time += 10

    if alice.dress in ['a', 'c']:
        $ __r1 = renpy.random.choice(['01', '02a']) if alice.nopants else renpy.random.choice(['01', '02'])
    elif alice.dress = 'b':
        $ __r1 = '04' # нет спрайта, временно ставим в одних
    elif alice.dress = 'd':
        $ __r1 = '03'
    call alice_cam_dress_inf(__r1)

    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Алиса переодевается..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['05','06','07'])
    call alice_cam_dress_inf(__r1)
    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого, вот это вид!!!"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    if flags['smoke'] == 'not_nopants':
        $ renpy.show('Alice cams dressed 09', at_list=[laptop_screen])
        call alice_cam_dress_inf('09')
        Max_01 "Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала!"
    elif flags['smoke'] == 'nopants':
        $ renpy.show('Alice cams dressed 09a', at_list=[laptop_screen])
        call alice_cam_dress_inf('09a')
        Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Надеюсь, кто-то это заметит там, куда она идёт..."
    else:
        $ renpy.show('Alice cams dressed 09', at_list=[laptop_screen])
        call alice_cam_dress_inf('09')
        Max_04 "Трусики хорошо смотрятся на её попке. Но без них было бы лучше..."
    return

label cam0_alice_dressed_club:
    if 'alice_dressed' in cam_flag:
        $ renpy.show('Alice cams dressed 12', at_list=[laptop_screen])
        $ alice.dress_inf = '06'
        if 'alice_dressed_txt' not in cam_flag:
            $ cam_flag.append('alice_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('alice_dressed')
    $ spent_time += 10

    $ __r1 = '04'
    call alice_cam_dress_inf(__r1)

    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Алиса собирается в клуб..."
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    $ __r1 = renpy.random.choice(['05','06','07'])
    call alice_cam_dress_inf(__r1)
    $ renpy.show('Alice cams dressed '+__r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    menu:
        Max_00 "Ого, вот это вид!!!"
        "{i}продолжать смотреть{/i}":
            pass
        "{i}достаточно{/i}":
            jump open_site

    if flags['smoke'] == 'not_nopants':
        $ renpy.show('Alice cams dressed 10', at_list=[laptop_screen])
        call alice_cam_dress_inf('10')
        Max_01 "Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала!"
    elif flags['smoke'] == 'nopants':
        $ renpy.show('Alice cams dressed 10a', at_list=[laptop_screen])
        call alice_cam_dress_inf('10a')
        Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Это платье без трусиков смотрится гораздо лучше... Интересно, в клубе на это кто-нибудь обратит внимание?"
    else:
        $ renpy.show('Alice cams dressed 10', at_list=[laptop_screen])
        call alice_cam_dress_inf('10')
        Max_04 "Трусики хорошо смотрятся на её попке. Но без них это платье смотрелось бы гораздо лучше..."
    return
