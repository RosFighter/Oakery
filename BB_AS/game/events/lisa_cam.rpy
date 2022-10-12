
label cam0_lisa_sleep_night:
    $ renpy.show('Lisa cams sleep night '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    # $ renpy.show('Lisa cams sleep night '+random_choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_sleep' not in cam_flag:
        $ cam_flag.append('lisa_sleep')
        Max_01 "{m}Лиза сладко спит...{/m}"
    return

label cam0_lisa_sleep_morning:
    $ renpy.show('Lisa cams sleep morning '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    # $ renpy.show('Lisa cams sleep morning '+random_choice(['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_sleep' not in cam_flag:
        $ cam_flag.append('lisa_sleep')
        Max_01 "{m}Лиза ещё спит...{/m}"
    return

label cam0_lisa_shower:
    if tm[-2:] < '20' and lisa.dress_inf != '00a':
        show FG cam-shum-noact at laptop_screen
        if 'lisa_not_shower' not in cam_flag:
            $ cam_flag.append('lisa_not_shower')
            if len(house[3].cams)>1:
                Max_09 "{m}Лизы не видно через эту камеру... Может посмотреть через другую?{/m}"
            else:
                Max_09 "{m}Лизы не видно через эту камеру...{/m}"
    else:
        $ lisa.dress_inf = '00a'
        $ renpy.show('Lisa cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_04 "{m}Младшая сестрёнка принимает душ... Прекрасная Лиза - прекрасное утро!{/m}"
    return

label cam1_lisa_shower:
    if tm[-2:] < '20' and lisa.dress_inf != '00a':
        # назначим или определим одёжку
        if lisa.dress_inf != '04a':
            $ __r1 = {'04c':'a', '04d':'b', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
        else:
            $ __list = ['a', 'b', 'c', 'd'] if 'bathrobe' in lisa.gifts else ['c', 'd']
            $ __r1 = random_choice(__list)
            $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[__r1]

        $ renpy.show('Lisa cams bath-mirror '+random_choice(['01', '02', '03'])+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath_mirror' not in cam_flag:
            $ cam_flag.append('lisa_bath_mirror')
            Max_03 "{m}Лиза, прежде чем принять душ, любуется собой перед зеркалом. И мы этим со зрителями тоже полюбуемся...{/m}"

    else:
        show FG cam-shum-noact at laptop_screen
        if 'lisa_shower1' not in cam_flag:
            $ cam_flag.append('lisa_shower1')
            Max_09 "{m}Лизы не видно через эту камеру... Может посмотреть через другую?{/m}"
    return

label cam0_lisa_read:
    $ renpy.show('Lisa cams reading '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_read' not in cam_flag:
        $ cam_flag.append('lisa_read')
        Max_07 "{m}Люблю смотреть, как Лиза читает. Вернее, люблю позы, в которых она читает...{/m}"
    return

label cam0_lisa_repeats_homework:
    $ renpy.show('Lisa cams lessons '+cam_poses_manager(lisa, ['01', '02'])+'e', at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_repeats' not in cam_flag:
        $ cam_flag.append('lisa_repeats')
        Max_01 "{m}Лиза готовится к сегодняшним урокам в школе. Какая умничка...{/m}"
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
            '14':'01aa',
            '15':'01ea',
            '16':'01ea',
            '17':'01e',
            '18':'01e',
        }[r1]
    return

# label cam0_lisa_dressed_school:
#
#     if 'lisa_dressed' in cam_flag:
#         $ renpy.show('Lisa cams dressed 13', at_list=[laptop_screen])
#         show FG cam-shum-act at laptop_screen
#         $ lisa.dress_inf = '01d'
#         if 'lisa_dressed_txt' not in cam_flag:
#             $ cam_flag.append('lisa_dressed_txt')
#             Max_09 "Ничего интересного я здесь уже не увижу, Лиза полностью оделась."
#         return
#
#     $ cam_flag.append('lisa_dressed')
#     # $ Wait(10)
#
#     # $ __r1 = random_choice(['00', '01', '02'])
#     # call lisa_cam_dress_inf(__r1) from _call_lisa_cam_dress_inf
#     # $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
#     # show FG cam-shum-act at laptop_screen
#     # menu:
#     #     Max_07 "Отлично! Лиза наряжается, чтобы отправиться в школу..."
#     #     "{i}продолжать смотреть{/i}":
#     #         pass
#     #     "{i}достаточно{/i}":
#     #         jump open_site
#     #
#     # $ __r1 = random_choice(['03','04','05','06'])
#     # call lisa_cam_dress_inf(__r1) from _call_lisa_cam_dress_inf_1
#     # $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
#     # show FG cam-shum-act at laptop_screen
#     # menu:
#     #     Max_02 "Ухх! Сейчас она такая голенькая и милая..."
#     #     "{i}продолжать смотреть{/i}":
#     #         pass
#     #     "{i}достаточно{/i}":
#     #         jump open_site
#
#     $ __r1 = random_choice(['07','08','09'])
#     call lisa_cam_dress_inf(__r1) from _call_lisa_cam_dress_inf_2
#     $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
#     show FG cam-shum-act at laptop_screen
#
#     Max_04 "Как классно, что моя сестрёнка - такая соблазнительная школьница. Уверен, зрителям это нравится!"
#     # jump open_site
#     return

# label cam0_lisa_dressed_shop:
#
#     if 'lisa_dressed' in cam_flag:
#         $ renpy.show('Lisa cams dressed 14', at_list=[laptop_screen])
#         show FG cam-shum-act at laptop_screen
#         $ lisa.dress_inf = '01'
#         if 'lisa_dressed_txt' not in cam_flag:
#             $ cam_flag.append('lisa_dressed_txt')
#             Max_09 "Ничего интересного я здесь уже не увижу, Лиза полностью оделась."
#         return
#
#     $ cam_flag.append('lisa_dressed')
#     # $ spent_time += 10
#     $ Wait(10)
#
#     $ __r1 = random_choice(['00', '01', '02'])
#     call lisa_cam_dress_inf(__r1) from _call_lisa_cam_dress_inf_3
#     $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
#     show FG cam-shum-act at laptop_screen
#     menu:
#         Max_07 "Отлично! Лиза наряжается, чтобы отправиться на шопинг..."
#         "{i}продолжать смотреть{/i}":
#             pass
#         "{i}достаточно{/i}":
#             jump open_site
#
#     $ __r1 = random_choice(['03','04','05','06'])
#     call lisa_cam_dress_inf(__r1) from _call_lisa_cam_dress_inf_4
#     $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
#     show FG cam-shum-act at laptop_screen
#     menu:
#         Max_02 "Ухх! Сейчас она такая голенькая и милая..."
#         "{i}продолжать смотреть{/i}":
#             pass
#         "{i}достаточно{/i}":
#             jump open_site
#
#     # $ spent_time += 10
#     $ Wait(10)
#     $ __r1 = random_choice(['10','11','12'])
#     call lisa_cam_dress_inf(__r1) from _call_lisa_cam_dress_inf_5
#     $ renpy.show('Lisa cams dressed '+__r1, at_list=[laptop_screen])
#     show FG cam-shum-act at laptop_screen
#
#     Max_04 "Повезло мне с сестрёнкой! Обворожительна в любой одежде и ещё больше - без неё..."
#     return


label cam0_lisa_dressed:
    # $ renpy.dynamic('r1', 'st')
    if 'lisa_dressed' in cam_flag:
        if not weekday:
            $ r1 = '15' if lisa.clothes.weekend.GetCur().suf == 'w' else '17'
            $ lisa.dress_inf = lisa.clothes.weekend.GetCur().info
        elif weekday == 6:
            $ r1 = '14'
            $ lisa.dress_inf = '01aa'
        else:
            $ r1 = '13'
            $ lisa.dress_inf = '01d'
        $ renpy.show('Lisa cams dressed ' + r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        call lisa_cam_dress_inf(r1) from _call_lisa_cam_dress_inf
        if 'lisa_dressed_txt' not in cam_flag:
            $ cam_flag.append('lisa_dressed_txt')
            Max_09 "{m}Ничего интересного я здесь уже не увижу, Лиза полностью оделась.{/m}"
        return

    $ cam_flag.append('lisa_dressed')

    if 'lisa_dr0' in cam_flag:
        # Макс взял ноутбук до переодеваний, может быть любая одежда
        $ r1 = random_choice(['00', '01', '02'])
        $ st = 0
    else:
        $ r1 = {'02a':'00', '02b':'01', '02c':'02', '00':'03', '02h':'07',
                '02d':'08', '02e':'09', '02i':'10', '02f':'11', '02g':'12',
                '01ea':'16'}[lisa.dress_inf]
        $ st = 0 if r1 in ['00', '01', '02'] else 1 if r1 in ['03','04','05','06'] else 2

    if st < 1:
        $ renpy.show('Lisa cams dressed '+ r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        call lisa_cam_dress_inf(r1) from _call_lisa_cam_dress_inf_1
        if 6 > weekday > 0:
            Max_07 "{m}Отлично! Лиза наряжается, чтобы отправиться в школу...{/m}" nointeract
        elif weekday == 6:
            Max_07 "{m}Отлично! Лиза наряжается, чтобы отправиться на шопинг...{/m}" nointeract
        elif lisa.dcv.battle.stage in [2, 4, 5]:
            Max_07 "{m}Отлично! Лиза наряжается, чтобы отправиться к репетитору...{/m}" nointeract
        else:
            Max_07 "{m}Отлично! Лиза наряжается, чтобы отправиться на прогулку...{/m}" nointeract
        menu:
            "{i}продолжать смотреть{/i}":
                $ r1 = random_choice(['03','04','05','06'])
            "{i}достаточно{/i}":
                jump open_site

    if st < 2:
        $ renpy.show('Lisa cams dressed '+ r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        call lisa_cam_dress_inf(r1) from _call_lisa_cam_dress_inf_2
        menu:
            Max_02 "{m}Ухх! Сейчас она такая голенькая и милая...{/m}"
            "{i}продолжать смотреть{/i}":
                if not weekday:
                    $ r1 = random_choice(['15', '16'])
                elif weekday == 6:
                    $ r1 = random_choice(['10','11','12'])
                else:
                    $ r1 = random_choice(['07','08','09'])
            "{i}достаточно{/i}":
                jump open_site

    $ renpy.show('Lisa cams dressed '+ r1, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    call lisa_cam_dress_inf(r1) from _call_lisa_cam_dress_inf_3
    if 6 > weekday > 0:
        Max_04 "{m}Как классно, что моя сестрёнка - такая соблазнительная школьница. Уверен, зрителям это нравится!{/m}"
    else:
        Max_04 "{m}Повезло мне с сестрёнкой! Обворожительна в любой одежде и ещё больше - без неё...{/m}"
    return

label cam0_lisa_sun:
    $ renpy.show('Lisa cams sun '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_sun' not in cam_flag:
        $ cam_flag.append('lisa_sun')
        Max_01 "{m}Лиза загорает и радует этим моих зрителей! И меня, конечно же...{/m}"
    return

label cam1_lisa_sun:
    show FG cam-shum-noact at laptop_screen
    if 'lisa_sun1' not in cam_flag:
        $ cam_flag.append('lisa_sun1')
        Max_09 "{m}Через эту камеру ничего не видно... Может посмотреть через другую?{/m}"
    return

label cam0_lisa_swim:
    show FG cam-shum-noact at laptop_screen
    if 'lisa_swim0' not in cam_flag:
        $ cam_flag.append('lisa_swim0')
        if len(house[6].cams)>1:
            Max_09 "{m}Ничего толком не видно... Стоит взглянуть через другую камеру...{/m}"
        else:
            Max_09 "{m}Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн...{/m}"
    return

label cam1_lisa_swim:
    $ renpy.show('Lisa cams swim '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_swim1' not in cam_flag:
        $ cam_flag.append('lisa_swim1')
        Max_01 "{m}Приятно наблюдать за младшей сестрёнкой у водички...{/m}"
    return

label cam0_lisa_dishes:
    $ renpy.show('Lisa cams crockery 01'+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'lisa_dishes' not in cam_flag:
        $ cam_flag.append('lisa_dishes')
        Max_01 "{m}Лиза моет посуду. А ведь я мог бы ей помочь...{/m}"
    return

label cam0_lisa_phone:
    $ renpy.show('BG-cam house myroom-0 evening', at_list=[laptop_screen,])
    $ renpy.show('Max cams patch evening', at_list=[laptop_screen,])
    $ renpy.show('Lisa cams phone '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_phone' not in cam_flag:
        $ cam_flag.append('lisa_phone')
        Max_01 "{m}Сестрёнка бездельничает и залипла в свой телефон. Но лежит красиво...{/m}"
    return

label cam0_lisa_bath:
    if tm[-2:] < '10':
        # набирает воду
        show Lisa cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath0_st0' not in cam_flag:
            $ cam_flag.append('lisa_bath0_st0')
            Max_01 "{m}Лиза почти набрала воду, хотя я смотрю на кое-что другое...{/m}"
    elif tm[-2:] > '40':
        # вытирается
        show Lisa cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath0_st1' not in cam_flag:
            $ cam_flag.append('lisa_bath0_st1')
            Max_04 "{m}Эх, Лиза... Не вытирайся! Ты мокренькая тоже обалденная...{/m}"
    else:
        $ renpy.show('Lisa cams bath '+cam_poses_manager(lisa, ['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'lisa_bath0_st0' not in cam_flag:
            $ cam_flag.append('lisa_bath0_st0')
            Max_05 "{m}Давай, сестрёнка, не стесняйся показать как можно больше всего интересного...{/m}"
    return

label cam1_lisa_bath:
    show FG cam-shum-act at laptop_screen
    if 'lisa_bath1' not in cam_flag:
        $ cam_flag.append('lisa_bath1')
        Max_09 "{m}Лизы не видно через эту камеру... Может посмотреть через другую?{/m}"
    return

label cam0_lisa_homework:
    $ renpy.show('Lisa cams lessons '+cam_poses_manager(lisa, ['01', '02'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-noact at laptop_screen
    if 'lisa_lessons' not in cam_flag:
        $ cam_flag.append('lisa_lessons')
        Max_01 "{m}Лиза учит уроки. Может, стоило ей помочь?!{/m}"
    return
