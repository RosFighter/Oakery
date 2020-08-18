
label cam0_lisa_sleep_night:
    $ renpy.show('Lisa cams sleep night '+renpy.random.choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    # if 'lisa_sleep' not in cam_flag:
    #     $ cam_flag.append('lisa_sleep')
    #     Max_00 "Сестрёнка спит..."
    return

label cam0_lisa_sleep_morning:
    $ renpy.show('Lisa cams sleep morning '+renpy.random.choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    # if 'lisa_sleep' not in cam_flag:
    #     $ cam_flag.append('lisa_sleep')
    #     Max_00 "Сестрёнка спит..."
    return

label cam0_lisa_shower:
    if tm[-2:] < '20' and lisa.dress_inf != '00a':
        show FG cam-shum-act at laptop_screen
        if 'lisa_not_shower' not in cam_flag:
            $ cam_flag.append('lisa_not_shower')
            if len(house[3].cams)>1:
                Max_00 "Сестрёнки не видно, скорее всего она возле зеркала... Нужно посмотреть через другую камеру..."
            else:
                Max_00 "Сестрёнки не видно, скорее всего она возле зеркала... Но через эту камеру не разглядеть..."
    else:
        $ lisa.dress_inf = '00a'
        $ renpy.show('Lisa cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_00 "Моя младшая сестрёнка в душе... Это зрелище, которое никогда не надоедает..."
    return

label cam1_lisa_shower:
    if tm[-2:] < '20' and lisa.dress_inf != '00a':
        # назначим или определим одёжку
        if lisa.dress_inf != '04a':
            $ __r1 = {'04c':'a', '04d':'b', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
        else:
            $ __list = ['a', 'b', 'c', 'd'] if 'bathrobe' in lisa.gifts else ['c', 'd']
            $ __r1 = renpy.random.choice(__list)
            $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[__r1]

        $ renpy.show('Lisa cams bath-mirror '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath_mirror' not in cam_flag:
            $ cam_flag.append('lisa_bath_mirror')
            if __r1 in ['a', 'b']:
                Max_02 "Да-а... Может сестрёнка и в халатике, но её упругие сисечкики видны просто замечательно! А они у неё - что надо..."
            elif __r1 == 'c':
                Max_04 "Прекрасно! Сестрёнка сегодня в одних трусиках... Глядя на эту красоту, можно мечтать лишь об одном!"
            else:
                Max_06 "Вау! Лиза примеряет костюм Евы!"

    else:
        show FG cam-shum-act at laptop_screen
        if 'lisa_shower1' not in cam_flag:
            $ cam_flag.append('lisa_shower1')
            Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_lisa_read:
    $ renpy.show('Lisa cams reading '+renpy.random.choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_read' not in cam_flag:
        $ cam_flag.append('lisa_read')
        Max_00 "Лиза с таким увлечением читает..."
    return

label lisa_cam_dress_inf(r1):
    $ lisa.dress_inf = {
            '00':'02a',
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
        show FG cam-shum-act at laptop_screen
        $ lisa.dress_inf = '01d'
        if 'lisa_dressed_txt' not in cam_flag:
            $ cam_flag.append('lisa_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('lisa_dressed')
    $ spent_time += 10

    $ __r1 = renpy.random.choice(['00', '01', '02'])
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
        show FG cam-shum-act at laptop_screen
        $ lisa.dress_inf = '01'
        if 'lisa_dressed_txt' not in cam_flag:
            $ cam_flag.append('lisa_dressed_txt')
            Max_00 "Уже ничего интересного, сестрёнка полностью одета и просто любуется собой..."
        return

    $ cam_flag.append('lisa_dressed')
    $ spent_time += 10

    $ __r1 = renpy.random.choice(['00', '01', '02'])
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

label cam0_lisa_dishes:
    $ renpy.show('Lisa cams crockery 01'+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'lisa_dishes' not in cam_flag:
        $ cam_flag.append('lisa_dishes')
        Max_00 "Лиза моет посуду, ничего интересного..."
    return

label cam0_lisa_phone:
    $ renpy.show('BG-cam house myroom-0 evening', at_list=[laptop_screen,])
    $ renpy.show('Max cams patch evening', at_list=[laptop_screen,])
    $ renpy.show('Lisa cams phone '+renpy.random.choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_phone' not in cam_flag:
        $ cam_flag.append('lisa_phone')
        Max_00 "Сестрёнка бездельничает с телефоном..."
    return

label cam0_lisa_bath:
    if tm[-2:] < '10':
        # набирает воду
        show Lisa cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath0_st0' not in cam_flag:
            $ cam_flag.append('lisa_bath0_st0')
            Max_00 "Лиза ещё только набирает воду, самое интересное впереди..."
    elif tm[-2:] > '40':
        # вытирается
        show Lisa cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath0_st1' not in cam_flag:
            $ cam_flag.append('lisa_bath0_st1')
            Max_00 "Эх, Лиза уже вытирается, самое интересное позади..."
    else:
        $ renpy.show('Lisa cams bath '+renpy.random.choice(['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath0_st0' not in cam_flag:
            $ cam_flag.append('lisa_bath0_st0')
            Max_00 "Сестрёнка принимает ванну, заглядение..."
    return

label cam1_lisa_bath:
    show FG cam-shum-act at laptop_screen
    if 'lisa_bath1' not in cam_flag:
        $ cam_flag.append('lisa_bath1')
        Max_00 "Через эту камеру ничего не видно, нужно воспользоваться другой..."
    return

label cam0_lisa_homework:
    $ renpy.show('Lisa cams lessons '+renpy.random.choice(['01', '02'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_lessons' not in cam_flag:
        $ cam_flag.append('lisa_lessons')
        Max_00 "Лиза учит уроки..."
    return
