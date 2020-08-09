
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
    $ tod = 'day ' if '06:00' < tm < '22:00' else 'night'
    $ renpy.show('Kira cams swim '+tod+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_00 "На тётю Киру всегда приятно посмотреть..."
    return

label cam0_kira_alice_shower:
    # выбор, кто из персонажей принимает душ
    if 'alice_sh' in cam_flag:
        $ __var = 'alice'
    elif 'kira_sh' in cam_flag:
        $ __var = 'kira'
    else:
        $ __var = renpy.random.choice(['alice', 'kira'])
        $ cam_flag.append(__var+'_sh')

    if __var == 'alice':
        # в душе Алиса, тётя Кира перед умывальниками
        $ renpy.show('Alice cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen

        if 'alice_shower' not in cam_flag:
            $ cam_flag.append('alice_shower')
            Max_00 "Старшая сестрёнка в душе... Это зрелище, которое никогда не надоедает..."
            if 'lisa_shower' not in cam_flag:
                # Киру ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Тётя Кира, наверное, перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Тётя Кира, наверное, перед зеркалом, но отсюда не разглядеть..."
            else:
                # Киру перед зеркалом уже видели. Не знаю, нужно ли это как-то комментировать при взгляде через камеру душа
                pass
    else:
        # в душе тётя Кира, перед умывальниками Алиса
        $ renpy.show('Kira cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen

        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_00 "Тётя Кира принимает душ... Зрелище, способное отнять разум у любого мужчины..."
            if 'alice_shower' not in cam_flag:
                # Алису ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Алиса, должно быть, красуется перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Алиса, должно быть, красуется перед зеркалом, но отсюда не разглядеть..."
            else:
                # Алису перед зеркалом уже видели. Не знаю, нужно ли это как-то комментировать при взгляде через камеру душа
                pass

    return

label cam1_kira_alice_shower:
    return

label cam0_kira_lisa_shower:
    # выбор, кто из персонажей принимает душ
    if 'lisa_sh' in cam_flag:
        $ __var = 'lisa'
    elif 'kira_sh' in cam_flag:
        $ __var = 'kira'
    else:
        $ __var = renpy.random.choice(['lisa', 'kira'])
        $ cam_flag.append(__var+'_sh')

    if __var == 'lisa':
        # в душе Лиза, тётя Кира перед умывальниками
        $ renpy.show('Lisa cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen

        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_00 "Младшая сестрёнка в душе... Это зрелище, которое никогда не надоедает..."
            if 'lisa_shower' not in cam_flag:
                # Киру ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Тётя Кира, наверное, перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Тётя Кира, наверное, перед зеркалом, но отсюда не разглядеть..."
            else:
                # Киру перед зеркалом уже видели. Не знаю, нужно ли это как-то комментировать при взгляде через камеру душа
                pass
    else:
        # в душе Кира, перед умывальниками Лиза
        $ renpy.show('Kira cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen

        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_00 "Тётя Кира принимает душ... Зрелище, способное отнять разум у любого мужчины..."
            if 'alice_shower' not in cam_flag:
                # Лизу ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Лиза, должно быть, красуется перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Лиза, должно быть, красуется перед зеркалом, но отсюда не разглядеть..."
            else:
                # Лизу перед зеркалом уже видели. Не знаю, нужно ли это как-то комментировать при взгляде через камеру душа
                pass

    return

label cam1_kira_alice_shower:
    return
