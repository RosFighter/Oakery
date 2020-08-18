
label cam0_kira_sleep_morning:
    $ renpy.show('Kira cams sleep '+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'kira_sleep' not in cam_flag:
        $ cam_flag.append('kira_sleep')
        Max_00 "Очаровательная тётя спит..."
    return

label cam0_kira_shower:
    if tm[-2:] < '20' and kira.dress_inf != '00a':
        show FG cam-shum-act at laptop_screen
        if 'kira_not_shower' not in cam_flag:
            $ cam_flag.append('kira_not_shower')
            if len(house[3].cams)>1:
                Max_00 "Тёти не видно, скорее всего она возле зеркала... Нужно посмотреть через другую камеру..."
            else:
                Max_00 "Тёти не видно, скорее всего она возле зеркала... Но через эту камеру не разглядеть..."
    else:
        $ kira.dress_inf = '00a'
        if 'kira_shower' not in cam_flag:
            $ __pose = renpy.random.randint(1, 8)
        else:
            $ __pose = renpy.random.randint(1, 6) if __pose < 7 else renpy.random.randint(7, 8)
        $ renpy.show('Kira cams shower 0'+str(__pose), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            if __pose < 7 :
                Max_00 "Тётя в душе... Это зрелище, которое никогда не надоедает..."
            else:
                Max_00 "О, тётя решила поразвлечься... "
    return

label cam1_kira_shower:
    if tm[-2:] < '20' and kira.dress_inf != '00a':
        # назначим или определим одёжку
        if peeping['kira_shower'] > 1:
            $ __r1 = {'04a':'b', '02a':'c', '00':'d', '00a':'d'}[kira.dress_inf]
        else:
            $ __r1 = renpy.random.choice(['b', 'c', 'd'])
            $ kira.dress_inf = {'b':'04a', 'c':'02a', 'd':'00'}[__r1]

        $ __pose = renpy.random.choice(['01', '02', '03']) if __r1 != 'd' else renpy.random.choice(['01', '02', '03', '04', '05'])
        $ renpy.show('Kira cams bath-mirror '+__pose+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_bath_mirror' not in cam_flag:
            $ cam_flag.append('kira_bath_mirror')
            if __r1 == 'b':
                Max_00 "Тётя Кира красуется перед зеркалом... Жаль, но всё самое вкусное прикрыто полотенцем..."
            elif __r1 == 'c':
                Max_00 "Здорово, тётя Кира в одних трусиках любуется собой!"
            elif __pose in ['01', '02', '03']:
                Max_00 "Здорово, тётя Кира любуется собой в костюме Евы!"
            else:
                Max_00 "Ого! А тёте Кире явно не хватает секса, раз она решила пошалить перед душем..."

    else:
        show FG cam-shum-act at laptop_screen
        if 'kira_shower1' not in cam_flag:
            $ cam_flag.append('kira_shower1')
            Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_kira_alice_shower:
    # выбор, кто из персонажей принимает душ
    if 'alice_sh' in cam_flag:
        $ __var = 'alice' if tm[-2:] < '30' else 'kira' # в первой половине часа в душе Алиса
    elif 'kira_sh' in cam_flag:
        $ __var = 'kira' if tm[-2:] < '30' else 'alice' # в первой половине часа в душе Кира
    elif 'kira_alice_sh' in cam_flag:
        $ __var = 'kira_alice'
    else:
        $ __var = renpy.random.choice(['alice', 'kira_alice', 'kira', 'kira_alice'])
        if __var == 'alice':
            $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'kira_sh')
        elif __var == 'kira':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'alice_sh')
        else:
            $ cam_flag.append('kira_alice_sh')

    if __var == 'alice':
        # в душе Алиса, тётя Кира перед умывальниками
        $ renpy.show('Alice cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'alice_shower' not in cam_flag:
            $ cam_flag.append('alice_shower')
            Max_00 "Старшая сестрёнка в душе... Это зрелище, которое никогда не надоедает..."
            if 'kira_mirror' not in cam_flag:
                # Киру ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Тётя Кира, наверное, перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Тётя Кира, наверное, перед зеркалом, но отсюда не разглядеть..."
    elif __var == 'kira':
        # в душе тётя Кира, перед умывальниками Алиса
        $ renpy.show('Kira cams shower 0'+str(renpy.random.randint(1, 6)), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_00 "Тётя Кира принимает душ... Зрелище, способное отнять разум у любого мужчины..."
            if 'alice_mirror' not in cam_flag:
                # Алису ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Алиса, должно быть, красуется перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Алиса, должно быть, красуется перед зеркалом, но отсюда не разглядеть..."
    else:
        # обе девчонки в душе, у зеркал никого
        $ kira.dress_inf != '00a'
        $ alice.dress_inf != '00aa'
        $ renpy.show('Alice cams shower 0'+str(renpy.random.randint(1, 8)), at_list=[cam_shower_right])
        $ renpy.show('Kira cams shower 0'+str(renpy.random.randint(1, 6)), at_list=[cam_shower_left])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_07 "Ого... Две очень плохие девочки сегодня моются вместе... тётя Кира и Алиса! Как же они хороши..."

    return

label cam1_kira_alice_shower:
    # выбор, кто из персонажей принимает душ
    if 'alice_sh' in cam_flag:
        $ __var = 'kira' if tm[-2:] < '30' else 'alice' # в первой половине часа перед зеркалом Кира
    elif 'kira_sh' in cam_flag:
        $ __var = 'alice' if tm[-2:] < '30' else 'kira' # в первой половине часа перед зеркалом Алиса
    elif 'kira_alice_sh' in cam_flag:
        $ __var = 'kira_alice'
    else:
        $ __var = renpy.random.choice(['alice', 'kira_alice', 'kira', 'kira_alice'])
        if __var == 'alice':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'alice_sh')
        elif __var == 'kira':
            # перед умывальниками первые полчаса Кира
            $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'kira_sh')
        else:
            $ cam_flag.append('kira_alice_sh')

    if __var == 'kira':
        # перед умывальниками Кира, Алису не видно, она сейчас в душе
        if tm[-2:] < '10' and kira.dress_inf != '00a': # начало часа, Киру в душе не видели, у нее есть халат
            $ __r1 = 'b'
        elif tm[-2:] < '20' and kira.dress_inf not in ['00a', '00']: # Киру не видели голой
            $ __r1 = 'c'
        else:
            $ __r1 = 'd'
        $ kira.dress_inf = {'b':'04a', 'c':'02a', 'd':'00'}[__r1]
        $ renpy.show('Kira cams bath-mirror '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_mirror' not in cam_flag:
            $ cam_flag.append('kira_mirror')
            Max_00 "Тётя Кира красуется перед зеркалом..."
    elif __var == 'alice':
        # перед умывальниками Алиса, Киру не видно, она сейчас в душе
        if tm[-2:] < '10' and alice.dress_inf != '00aa': # первая треть часа, Алису в душе не видели
            $ __r1 = 'a'
        elif tm[-2:] < '20' and alice.dress_inf not in ['00a', '00aa']:
            $ __r1 = 'c'
        else:
            $ __r1 = 'd'
        $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[__r1]
        $ renpy.show('Alice cams bath-mirror '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'alice_mirror' not in cam_flag:
            $ cam_flag.append('alice_mirror')
            Max_00 "Ух, вот это вид..."
    else:
        show FG cam-shum-act at laptop_screen
        if 'alice_shower1' not in cam_flag:
            $ cam_flag.append('alice_shower1')
            Max_00 "Через эту камеру никого не видно... Может посмотреть через другую?"

    return

label cam0_kira_lisa_shower:
    # выбор, кто из персонажей принимает душ
    if 'lisa_sh' in cam_flag:
        $ __var = 'lisa' if tm[-2:] < '30' else 'kira' # в первой половине часа в душе Лиза
    elif 'kira_sh' in cam_flag:
        $ __var = 'kira' if tm[-2:] < '30' else 'lisa' # в первой половине часа в душе Кира
    elif 'kira_lisa_sh' in cam_flag:
        $ __var = 'kira_lisa'
    else:
        $ __var = renpy.random.choice(['lisa', 'kira_lisa', 'kira', 'kira_lisa'])
        if __var == 'lisa':
            $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'kira_sh')
        elif __var == 'kira':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'lisa_sh')
        else:
            $ cam_flag.append('kira_lisa_sh')

    if __var == 'lisa':
        # в душе Лиза, тётя Кира перед умывальниками
        $ lisa.dress_inf != '00a'
        $ renpy.show('Lisa cams shower 0'+str(renpy.random.randint(1, 9)), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_00 "Младшая сестрёнка в душе... На ее прелести я могу смотреть часами..."
            if 'kira_mirror' not in cam_flag:
                # Киру ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Тётя Кира, должно быть, перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Тётя Кира, должно быть, перед зеркалом, но отсюда не разглядеть..."
    elif __var == 'kira':
        # в душе тётя Кира, перед умывальниками Лиза
        $ renpy.show('Kira cams shower 0'+str(renpy.random.randint(1, 6)), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_00 "Тётя Кира принимает душ... Зрелище, способное отнять разум у любого мужчины..."
            if 'lisa_mirror' not in cam_flag:
                # Лизу ещё не видели
                if len(house[3].cams)>1:
                    Max_00 "Лиза, должно быть, красуется перед зеркалом... Надо взглянуть через другую камеру..."
                else:
                    Max_00 "Лиза, должно быть, красуется перед зеркалом, но отсюда не разглядеть..."
    else:
        # обе девчонки в душе, у зеркал никого
        $ kira.dress_inf != '00a'
        $ lisa.dress_inf != '00a'
        $ renpy.show('Lisa cams shower 0'+str(renpy.random.randint(1, 8)), at_list=[cam_shower_right])
        $ renpy.show('Kira cams shower 0'+str(renpy.random.randint(1, 6)), at_list=[cam_shower_left])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_07 "Ого... Тётя и младшая сестрёнка сегодня моются вместе... Как же они хороши..."

    return

label cam1_kira_lisa_shower:
    # выбор, кто из персонажей принимает душ
    if 'lisa_sh' in cam_flag:
        $ __var = 'kira' if tm[-2:] < '30' else 'lisa' # в первой половине часа перед зеркалом Кира
    elif 'kira_sh' in cam_flag:
        $ __var = 'lisa' if tm[-2:] < '30' else 'kira' # в первой половине часа перед зеркалом Лиза
    elif 'kira_lisa_sh' in cam_flag:
        $ __var = 'kira_lisa'
    else:
        $ __var = renpy.random.choice(['lisa', 'kira_lisa', 'kira', 'kira_lisa'])
        if __var == 'lisa':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'lisa_sh')
        elif __var == 'kira':
            # перед умывальниками первые полчаса Кира
            $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'kira_sh')
        else:
            $ cam_flag.append('kira_lisa_sh')

    if __var == 'kira':
        # перед умывальниками Кира, Лизу не видно, она сейчас в душе
        if tm[-2:] < '10' and kira.dress_inf != '00a': # начало часа, Киру в душе не видели, у нее есть халат
            $ __r1 = 'b'
        elif tm[-2:] < '20' and kira.dress_inf not in ['00a', '00']: # Киру не видели голой
            $ __r1 = 'c'
        else:
            $ __r1 = 'd'
        $ kira.dress_inf = {'b':'04a', 'c':'02a', 'd':'00'}[__r1]
        $ __pose = renpy.random.choice(['01', '02', '03'])
        $ renpy.show('Kira cams bath-mirror '+__pose+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_mirror' not in cam_flag:
            $ cam_flag.append('kira_mirror')
            Max_00 "Тётя Кира красуется перед зеркалом..."
    elif __var == 'lisa':
        # перед умывальниками Лиза, Киру не видно, она сейчас в душе
        if tm[-2:] < '10' and lisa.dress_inf != '00a' and 'bathrobe' in lisa.gifts: # начало часа, Лизу в душе не видели, у нее есть халат
            $ __r1 = 'a'
        elif tm[-2:] < '20' and lisa.dress_inf not in ['00a', '00']: # Лизу не видели голой
            $ __r1 = 'c'
        else:
            $ __r1 = 'd'
        $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[__r1]
        $ renpy.show('Lisa cams bath-mirror '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'lisa_mirror' not in cam_flag:
            $ cam_flag.append('lisa_mirror')
            Max_00 "Сестрёнка внимательно разглядывает себя в зеркало... А я и мои зрители с большим удовольствием любуемся ей..."
    else:
        show FG cam-shum-act at laptop_screen
        if 'kira_shower1' not in cam_flag:
            $ cam_flag.append('kira_shower1')
            Max_00 "Через эту камеру никого не видно... Может посмотреть через другую?"

    return

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
    $ renpy.show('Kira cams swim day '+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_00 "На тётю Киру всегда приятно посмотреть..."
    return

label cam0_kira_bath:
    if tm[-2:] < '10':
        # набирает воду
        show Kira cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_bath0_st0' not in cam_flag:
            $ cam_flag.append('kira_bath0_st0')
            Max_00 "Тётя Кира ещё только набирает воду, самое интересное впереди..."
    elif tm[-2:] > '40':
        # вытирается
        show Kira cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_bath0_st1' not in cam_flag:
            $ cam_flag.append('kira_bath0_st1')
            Max_00 "Эх, тётя Кира уже вытирается, самое интересное позади..."
    else:
        $ renpy.show('Kira cams bath '+renpy.random.choice(['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'kira_bath0_st0' not in cam_flag:
            $ cam_flag.append('kira_bath0_st0')
            Max_00 "Тётя Кира принимает ванну, заглядение..."
    return

label cam1_kira_bath:
    show FG cam-shum-act at laptop_screen
    if 'kira_bath1' not in cam_flag:
        $ cam_flag.append('kira_bath1')
        Max_00 "Через эту камеру ничего не видно, нужно воспользоваться другой..."
    return

label cam0_kira_night_tv:
    if tm[-2:] < '10':
        $ renpy.show('Kira cams tv '+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_tv' not in cam_flag:
            $ cam_flag.append('kira_tv')
            if talk_var['kira.porn']:
                Max_00 "Похоже, тётя Кира смотрит какой-то сериал... Может, стоит заглянуть чуть позже?"
            else:
                Max_00 "Похоже, тётя Кира смотрит какой-то сериал... А мне приятней смотреть на тётю..."
    elif talk_var['kira.porn']:
        if 'kira_tv1' not in cam_flag:
            $ cam_flag.append('kira_tv1')
            $ __pose = renpy.random.choice(['01', '02', '03'])
            $ renpy.show('Kira cams tv m-'+__pose, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            Max_00 "А вот это уже интересней! Тётя Кира настолько возбудилась, что начала ласкать свою киску..."
        else:
            $ renpy.show('Kira cams tv m-'+__pose, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
    else:
        $ renpy.show('Kira cams tv '+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen

    return

label cam0_kira_night_swim:
    show FG cam-shum-act at laptop_screen
    if 'kira_swim0' not in cam_flag:
        $ cam_flag.append('kira_swim0')
        if len(house[6].cams)>1:
            Max_00 "Ничего толком не видно... Стоит взглянуть с другой камеры..."
        else:
            Max_00 "Ничего не разглядеть... Нужно установить камеру охватывающую бассейн..."
    return

label cam1_kira_night_swim:
    $ renpy.show('Kira cams swim night '+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_00 "Тётя кира плавает одетая лишь в лунный свет... Класс!!!"
    return
