
label Waiting:
    # обработчик ожидания, запускает события по времени
    # "ждем [spent_time]"
    $ renpy.block_rollback()
    $ renpy.dynamic('name_label')

    $ prevday = day
    $ prevtime = tm

    if alarm_time != '':
        $ d2 = TimeDifference(prevtime, alarm_time)
        if spent_time == 0 or d2 < spent_time:
            $ spent_time = d2

    $ Wait(spent_time)

    # ищем стартующее по времени событие
    $ name_label = ''
    $ cut_event = events_by_tm.upcoming()
    if cut_event is not None:
        $ name_label = cut_event.label
        $ tm = cut_event.tm
        if prevtime > tm and prevtime < cut_event.tm < '23:59':
            $ day = prevday

    $ spent_time = TimeDifference(prevtime, tm) ## реально прошедшее время (до будильника или кат-события)

    # если прошло какое-то время, проверим необходимость смены одежды
    $ ChoiceClothes()

    if prevtime[:2] != tm[:2]:
        # почасовой сброс
        python:
            for char in chars:
                chars[char].hourly.reset()

        $ mgg.flags.hourly_reset()

        # позы обновляются каждый час
        $ pose3_1 = renpy.random.choice(['01', '02', '03'])
        $ pose3_2 = renpy.random.choice(['01', '02', '03'])
        $ pose3_3 = renpy.random.choice(['01', '02', '03'])
        $ pose3_4 = renpy.random.choice(['01', '02', '03'])
        $ pose2_1 = renpy.random.choice(['01', '02'])
        $ pose2_2 = renpy.random.choice(['01', '02'])
        $ pose2_3 = renpy.random.choice(['01', '02'])
        $ tv_scene = '' # renpy.random.choice(['', 'bj', 'hj'])

    # начисление влияния и другие события по времени
    if 'eric' in chars:
        call eric_time_settings from _call_eric_time_settings

    if prevtime < '12:00' <= tm:
        call Noon from _call_Noon
    if day != prevday:
        call Midnight from _call_Midnight
    if prevtime < "04:30" < tm:
        call NewDay from _call_NewDay

    if day != prevday and GetWeekday(day) == 0:
        # с субботы на воскресение начинается новая неделя
        # в том числе для еженедельного понижения влияния и/или отношения
        call NewWeek from _call_NewWeek

    $ delt = TimeDifference(prevtime, tm) # вычислим действительно прошедшее время

    if status_sleep:
        # если это сон, тогда энергия восстанавливается

        if delt >= 360:
            $ mgg.energy = 100 # за 6 часов сна Макс полностью восстанавливает свои силы
        elif delt >= 300:
            $ mgg.energy += delt * 0.25 # (15% в час)
        elif delt >= 240:
            $ mgg.energy += delt * 0.2 # (12% в час)
        else:
            $ mgg.energy += delt * 1 / 6 # (10% в час)
        $ mgg.cleanness -= delt * 0.5 * cur_ratio / 60.0

    else: # в противном случае - расходуется
        $ mgg.energy -= delt * 3.5 * cur_ratio / 60.0
        $ mgg.cleanness -= delt * 2.5 * cur_ratio / 60.0

    $ mgg.energy = clip(mgg.energy, 0.0, 100.0)
    $ mgg.cleanness = clip(mgg.cleanness, 0.0, 100.0)
    $ mgg.massage = clip(mgg.massage, 0.0, 100.0)
    $ mgg.social = clip(mgg.social, 0.0, 100.0)
    $ mgg.stealth = clip(mgg.stealth, 0.0, 100.0)

    if not at_comp:
        call after_buying from _call_after_buying

    if name_label != '' and renpy.has_label(name_label):
        # "запуск [name_label]"
        # если есть кат-событие - запускаем его
        if 'notebook_on_terrace' in cam_flag:
            $ cam_flag.remove('notebook_on_terrace')
        $ at_comp = False
        $ spent_time = 0
        $ prevday = day
        $ prevtime = tm
        $ CamShow()
        $ cur_ratio = 1
        if status_sleep:
            $ status_sleep = False
            with fade
        $ alarm_time = ''
        jump expression name_label

    # иначе запускаем блок 'после ожидания'
    if at_comp:
        jump cam_after_waiting
    else:
        jump AfterWaiting


label eric_time_settings:

    if prevtime < '14:00' <= tm:
        if all([GetWeekday(day)==6, 'sexbody2' not in alice.gifts, alice.dcv.intrusion.enabled, alice.dcv.intrusion.done, alice.dcv.intrusion.stage<7]):
            # Макс не успел вовремя подарить Алисе кружевное бельё
            $ alice.dcv.intrusion.stage = 8
            $ items['sexbody2'].block()
            # $ alice.gifts.append('sexbody2')
            $ poss['blog'].OpenStage(15)

    if prevtime < '15:00' <= tm:
        if all([GetWeekday(day)==0, flags.add_training, lisa.dcv.battle.stage in [2, 4, 5]]):
                # если у Лизы репетитор
                $ infl[lisa].add_e(60)

    if prevtime < '17:00' <= tm:
        if GetWeekday(day) in [1, 2, 3, 4, 5]:
            $ infl[ann].add_e(12)  # Ане начисляем каждый день, когда она на работе

            if lisa.dcv.battle.stage == 6:
                # если у Лизы курсы в школе
                $ infl[lisa].add_e(20)

    if prevtime < '22:00' <= tm:
        if alice.dcv.battle.stage and alice.dcv.battle.stage!=2:
            if GetWeekday(day)==3:
                $ infl[alice].add_e(50)
            elif GetWeekday(day)!=5:
                $ infl[alice].add_e(20)

    if prevtime < '22:30' <= tm:
        if all([GetWeekday(day)==1, lisa.dcv.intrusion.stage, flags.lisa_sexed<4]):
            # если начаты секс.уроки Лизы у АиЭ
            $ infl[lisa].add_e(40)

            # отмечаем урок пройденным
            $ flags.lisa_sexed += 1

            # сбрасываем флаг диалога с Лизой
            $ flags.l_ab_sexed = False

    if day != prevday:
        # полночь
        if check_is_home('eric'):
            # после секса с Эриком
            $ infl[ann].add_e(20)

        if not check_is_home('ann'):
            # Аня ночует у Эрика
            $ infl[ann].add_e(20)

    return


label Midnight:
    # "Полночь"
    $ renpy.dynamic("chance", "char")
    $ random_loc_ab = renpy.random.choice(['a', 'b'])
    $ random_sigloc = renpy.random.choice(['n', 't'])

    if alice.dcv.special.enabled:
        $ alice.daily.smoke = 0
        $ alice.nopants     = False
        $ alice.sleeptoples = False
        $ alice.sleepnaked  = False
        if alice.req.req == 'money':
            $ alice.req.reset()
        elif alice.req.result=='nojeans': # если требование не носить джинсы, оно не может быть нарушено
            pass
        elif alice.req.req and (not alice.req.result or alice.req.result[:3] != 'not'):
            # Если требование Макса было и это не деньги
            $ chance = GetDisobedience()  # шанс, что Алиса не будет соблюдать договоренность
            if RandomChance(chance):
                $ alice.req.result = 'not_' + alice.req.req
                $ alice.req.noted = False  # нарушение ещё не замечено Максом
            else:
                $ alice.req.result = alice.req.req
                if alice.req.req == 'nopants':
                    $ alice.nopants = True
                elif alice.req.req == 'sleep':
                    $ alice.sleeptoples = True
                elif alice.req.req == 'naked':
                    $ alice.sleepnaked = True

    $ GetDeliveryList()

    if 'eric' in chars and all([eric.daily.tv_sex, eric.stat.handjob > 0]):
        # если подсматривали за АиЭ у ТВ, меняем фильм
        $ ae_tv_order.pop(0)
        if not ae_tv_order:
            $ ae_tv_order = ['01', '02', '03', '04', '05', '06']
            $ renpy.random.shuffle(ae_tv_order)  # перемешаем список случайным образом

    if 'sexbody2' in alice.gifts and check_is_home('eric'):
        if ((GetWeekday(day)==4 and RandomChance(700))
            or (GetWeekday(day)==5 and RandomChance(350))):
            # Эрик дрочит на спящую Алису
            $ flags.eric_jerk = True
        else:
            $ flags.eric_jerk = False
    else:
        $ flags.eric_jerk = False
    $ flags.eric_noticed = False
    $ prenoted = 0

    python:
        # уменьшение счетчика событий, зависимых от прошедших дней
        for ch in chars:
            char = chars[ch]
            if char.id == 'lisa':
                # фильм-наказание сбрасывается позже, при наступлении нового игрового дня
                char.dcv.countdown(['special'])
            else:
                char.dcv.countdown()

        dcv.countdown()

        if SpiderResp > 0:
            SpiderResp -= 1

    return


label NewDay:
    # "Новый день"
    $ ann.daily.ask_money = 0 # просили денег у Анны

    python:
        for ch in chars:
            char = chars[ch]
            # сбросим подглядывания, диалоги и состояния
            char.daily.reset()

            # срок извинительных подарков
            if char.sorry.owe and char.sorry.left > 0:
                char.sorry.left -= 1

            # для каждого типа одежды каждого персонажа запустим рандомную смену
            lst = char.clothes.GetList()
            for cl_t in lst:
                if eval('char.clothes.'+cl_t+'.rand'):
                    eval('char.clothes.'+cl_t+'.SetRand()')

        # сброс фильма-наказания
        lisa.dcv.countdown(only=['special'])
        # if lisa.dcv.special.enabled and not lisa.dcv.special.done:
        #     lisa.dcv.special.set_lost(lisa.dcv.special.lost-1)

    if 'spider' in NightOfFun:
        $ NightOfFun.remove('spider') # если ночная забава не состоялась, паука из списка забав удаляем - он сбежал

    if 0 < GetWeekday(prevday) < 6:
        if poss['sg'].stn > 0 and not lisa.daily.homework:  # был разговор с Лизой по поводу наказаний и не помогал
            $ punlisa.insert(0, [  # вставляем в начало
                0,  # помощь Макса с д/з (0, 1, 2, 3, 4) (не помогал / допустил ошибку / неудачно попросил услугу / помог безвозмездно / помог за услугу)
                0,  # получена двойка в школе (0, 1)
                0,  # Макс заступился за Лизу перед наказанием (0, 1, 2)
                0,  # Лиза понесла наказание (0, 1)
                0,  # подозрительность
                ])
            $ del punlisa[10:]

    if poss['smoke'].stn > 1:  # Макс видел курящую Алису
        $ punalice.insert(0, [  # вставляем в начало
            0,  # Макс шантажировал Алису (1-передумал, 2-неудачно, 3-деньги, 4-перекур топлес, 5-лифчик, 6-трусики, 7-джинсы, 8-голая)
            0,  # Макс подставлял Алису
            0,  # Макс заступился за Алису перед наказанием
            0,  # Ализа понесла наказание
            0,  # подозрительность
            ])
        $ del punalice[14:]


    if lisa.clothes.learn.rand:
        if 'kira' not in chars:
            $ lisa.clothes.casual.cur = 1 if all(['bathrobe' in lisa.gifts, lisa.GetMood()[0] > 1]) else 0
        else:
            if all(['bathrobe' in lisa.gifts, lisa.GetMood()[0] > 1]):
                $ lisa.clothes.casual.cur = renpy.random.randint(1, 2)
            else:
                $ lisa.clothes.casual.cur = 2 if 'bathrobe' in lisa.gifts else 1

    if mgg.credit.debt > 0:        # если кредит не погашен
        $ mgg.credit.left -= 1       # уменьшим счетчик дней
        if mgg.credit.left == 0:   # если счетчик дней кончился
            $ mgg.credit.charge()    # начислим штраф

    $ cam_flag = []  # обнулим подсматривания через камеры
    $ ann_eric_scene = ''

    $ cam_poses.clear()  # обнулим список поз для камер
    # if 'black_linderie' in alice.gifts:
    #     $ cur_blog_lingerie = ''
    #     $ cam_pose_blog = []

    return


label Noon:
    $ renpy.dynamic("new_items")
    $ new_items = False
    if day > 12 and not ('nightie' in ann.gifts or items['nightie'].have or items['nightie'].InShop):
        $ items['nightie'].unblock()
        $ new_items = True
    if (alice.dcv.gifts.done and 'erobook_'+str(alice.dcv.gifts.stage) in items and
        not items['erobook_'+str(alice.dcv.gifts.stage)].InShop): # прошел откат после дарения книги, можно купить следующую
        $ items['erobook_'+str(alice.dcv.gifts.stage)].unblock()
        $ new_items = True
    if (GetWeekday(day)==1 and kira.dcv.feature.stage>6
            and not ('sexbody1' in alice.gifts or items['sexbody1'].have or items['sexbody1'].InShop)):
        $ items['sexbody1'].unblock()
        $ new_items = True

        # если не активирован счетчик на фотосессию с Кирой - активировать его
        if not kira.dcv.photo.enabled:
            $ kira.dcv.photo.stage = 1
            $ kira.dcv.photo.set_lost(8)

    if new_items:
        $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    return


label NewWeek:
    $ kira.sleepnaked = False # сбрасываем флаг стриптиза Киры

    if all(['sexbody2' in alice.gifts, flags.lisa_sexed>0]):
        # отношения с Эриком по сёстрам определены
        # активируем еженедельный счетчик на спаливание Киры и Макса Эриком
        $ wcv.catch_Kira.enabled = True  # теперь можно сдать Киру Эрику (при дружбе), либо Эрик может сам спалить Макса и Киру

    $ flags.noclub = False

    python:
        # уменьшение счетчика событий, зависимых от прошедших дней
        for i in wcv:
            if wcv[i].enabled and not wcv[i].done:
                wcv[i].set_lost(wcv[i].lost-1)

        # еженедельное снижения влияния
        for __char in infl:
            infl[__char].sub_m(40)
            infl[__char].sub_e(40)

    return


label AfterWaiting:

    $ renpy.dynamic('name_label', 'cur_plan')

    ## расчет притока/оттока зрителей для каждой камеры и соответствующего начисления
    $ CamShow()

    $ MoodNeutralize()

    if any([prevday!=day, prevtime!=tm]):
        # если прошло какое-то время, проверим необходимость смены одежды
        $ ChoiceClothes()

        # если сменилось время суток - нужно остановить текущую музыку
        if any([prevtime < '06:00' <= tm,
                prevtime < '11:00' <= tm,
                prevtime < '18:00' <= tm,
                prevtime < '22:00' <= tm]):
            stop music fadeout 1.0

    $ spent_time = 0
    $ prevday = day
    $ prevtime = tm
    $ cur_ratio = 1
    $ alarm_time = ""

    $ persone_button1 = None
    $ persone_button2 = None
    $ persone_button3 = None

    $ Distribution() # распределяем персонажей по комнатам и устанавливаем фоны для текущей локации

    # отключение возможности помыть посуду, если её вымыли Лиза или Алиса
    if not dishes_washed:
        if tm > '20:00':
            $ dishes_washed = True
        elif (day+2) % 7 != 6:
            $ name_label = ''
            if (day+2) % 7 == 0:
                $ cur_plan = alice.get_plan(day, '10:00')
                if cur_plan is not None:
                    $ name_label = cur_plan.label
            else:
                $ cur_plan = alice.get_plan(day, '11:00')
                if cur_plan is not None:
                    $ name_label = cur_plan.label

            if name_label == 'alice_dishes':
                if (GetWeekday(day) == 0 and tm >= '11:00') or tm >= '12:00':
                    $ dishes_washed = True

    $ name_label = ''
    # поиск управляющего блока для персонажа, находящегося в текущей комнате
    if len(current_room.cur_char) > 0:
        $ cur_plan = chars[current_room.cur_char[0]].get_plan()
        if cur_plan is not None:
            $ name_label = cur_plan.label

    # Отключим ноутбук на веранде, если Макс переходит в другую комнату
    # за исключением момента, когда Лиза переодевается, в этом случае кнопка ноутбука продолжает оставаться активной
    if all([lisa.plan_name!='dressed', current_room!=house[5], 'notebook_on_terrace' in cam_flag]):
        $ cam_flag.remove('notebook_on_terrace')
    if current_room.id == 'terrace' and current_room.cur_char:
        # в комнате появился кто-то, кроме Макса, нужно закрыть ноутбук
        $ at_comp = False
        if 'notebook_on_terrace' in cam_flag:
            $ cam_flag.remove('notebook_on_terrace')
    $ SetAvailableActions()

    if name_label != '' and renpy.has_label(name_label):
        # управляющий блок найден и существует
        call expression name_label from _call_expression
    else:
        # устанавливаем фон комнаты без персонажей
        if current_room.cur_bg.find('_') >= 0:
            scene image(current_room.cur_bg.replace('_', ''))
        else:
            scene image(current_room.cur_bg)

    if status_sleep:
        $ status_sleep = False
        with fade
    if mgg.energy < 10 and not mgg.flags.tired:
        Max_00 "Я слишком устал. Надо бы вздремнуть..."
        $ mgg.flags.tired = True

    if mgg.energy < 5:
        jump LittleEnergy

    $ music_starter()

    if all([current_room == house[6], flags.eric_jerk, '02:00'<=tm<'02:30', not flags.eric_noticed, not prenoted]):
        if not eric.stat.mast:
            jump first_jerk_yard
        else:
            jump jerk_yard

    window hide
    call screen room_navigation


label night_of_fun:

    if not len(NightOfFun):
        return

    $ renpy.random.shuffle(NightOfFun)

    # "Выбор из списка ночных забав"
    $ _fun = NightOfFun.pop() # последний из перемешанного списка - событие на сегодня

    if _fun != 'spider' and 'spider' in NightOfFun:
        $ NightOfFun.remove('spider') # если выпала забава, отличная от паука в постели Алисы, паука из списка удаляем - он сбежал

    ## Запуск выпавшей забавы
    if _fun == 'spider':
        call spider_in_bed from _call_spider_in_bed

    $ mgg.energy -= spent_time * 3.5 * cur_ratio / 60.0
    $ mgg.cleanness -= spent_time * 2.5 * cur_ratio / 60.0

    $ mgg.energy = clip(mgg.energy, 0.0, 100.0)
    $ mgg.cleanness = clip(mgg.cleanness, 0.0, 100.0)

    $ Wait(spent_time)

    ## теперь отправим Макса досыпать
    $ prevtime = tm
    $ status_sleep = True
    $ cur_ratio = 1
    $ spent_time = clip_time(int(round((100. - mgg.energy)/10, 0)) * 60, '06:00', '08:00')
    scene BG char Max bed-night-01
    $ renpy.show('Max sleep-night '+pose3_3)
    Max_19 "Теперь можно спокойно спать и ничего больше..."
    jump Waiting


label cam_after_waiting:

    $ renpy.dynamic('cam_label', 'cur_plan')

    ## расчет притока/оттока зрителей для каждой камеры и соответствующего начисления
    $ CamShow()

    $ MoodNeutralize()

    if any([prevday!=day, prevtime!=tm]):
        # если прошло какое-то время, проверим необходимость смены одежды
        $ ChoiceClothes()

    $ spent_time = 0
    $ prevday = day
    $ prevtime = tm
    $ cur_ratio = 1
    $ alarm_time = ""

    $ Distribution() # распределяем персонажей по комнатам и устанавливаем фоны для текущей локации

    if current_room.id == 'my_room' and check_is_room('lisa'):
        if lisa.plan_name != 'sleep':
            # Лиза не спит
            if not house[5].cur_char and not flags.warning:
                # на веранде никого, разговора про веранду ещё не было
                $ flags.warning = True
                menu:
                    Max_09 "Думаю, просматривать сейчас камеры не самая лучшая идея. Не хватало ещё, чтобы Лиза что-то заметила... Может, стоит пойти на веранду? Там сейчас не должно никого быть..."
                    "{i}идти на веранду{/i}":
                        $ current_room = house[5]
                        $ cam_flag.append('notebook_on_terrace')
                    "{i}не сейчас{/i}":
                        jump open_site
            elif house[5].cur_char:
                Max_09 "Лиза сейчас в комнате... И на веранде место занято! Лучше не рисковать и подождать с просмотром камер."
                jump open_site
            else:
                # речь про веранду уже была
                menu:
                    Max_09 "Лучше просматривать камеры в другом месте! Не хватало ещё, чтобы Лиза что-то заметила..."
                    "{i}идти на веранду{/i}" if not house[5].cur_char:
                        $ current_room = house[5]
                        $ cam_flag.append('notebook_on_terrace')
                    "{i}не сейчас{/i}":
                        jump open_site
        else:
            # Лиза спит
            if not house[5].cur_char and not flags.warning:
                # на веранде никого, разговора про веранду ещё не было
                $ flags.warning = True
                menu:
                    Max_09 "Пожалуй, не стоит сейчас просматривать камеры. Лиза может проснуться и заметить, что я делаю... Может, стоит пойти на веранду? Там сейчас не должно никого быть..."
                    "{i}идти на веранду{/i}":
                        $ current_room = house[5]
                        $ cam_flag.append('notebook_on_terrace')
                    "{i}не сейчас{/i}":
                        jump open_site
            elif house[5].cur_char:
                Max_09 "Лиза сейчас в комнате... И на веранде место занято! Лучше не рисковать и подождать с просмотром камер."
                jump open_site
            else:
                # речь про веранду уже была или там сейчас кто-то есть
                menu:
                    Max_09 "Лучше просматривать камеры в другом месте! Лиза может проснуться и заметить, что я делаю..."
                    "{i}идти на веранду{/i}" if not house[5].cur_char:
                        $ current_room = house[5]
                        $ cam_flag.append('notebook_on_terrace')
                    "{i}не сейчас{/i}":
                        jump open_site
    elif current_room.id == 'terrace' and current_room.cur_char:
        # в комнате появился кто-то, кроме Макса, нужно закрыть ноутбук
        $ at_comp = False
        if 'notebook_on_terrace' in cam_flag:
            $ cam_flag.remove('notebook_on_terrace')
        # Max_00 "Упс..."
        jump Waiting

    # поиск управляющего блока для персонажа, находящегося в текущей комнате
    if len(view_cam[0].cur_char) > 0:

        $ cur_plan = chars[view_cam[0].cur_char[0]].get_plan()
        $ cam_label = 'cam'+str(view_cam[2])+'_'+cur_plan.label if cur_plan is not None else ''

        if cam_label!='' and renpy.has_label(cam_label):
            call cam_background from _call_cam_background
            call expression cam_label from _call_expression_12
        else:
            call cam_background from _call_cam_background_1

        # show FG cam-shum-act at laptop_screen

        call screen cam_show
    elif current_room == view_cam[0]:
        ## камера текущей локации. Макс сидит за компом
        call cam_background from _call_cam_background_2

        $ time_of_day = {
                '06:00' <= tm < '11:00': 'morning',
                '11:00' <= tm < '19:00': 'day',
                '19:00' <= tm < '22:00': 'evening',
                '22:00'<=tm or tm<'06:00': 'night'
            }[True]

        if current_room == house[5]:
            $ renpy.show('Max cams terrace '+time_of_day+'-01'+mgg.dress, at_list=[laptop_screen])
        elif current_room == house[0]:
            $ renpy.show('Max cams myroom 01'+mgg.dress, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        call screen cam_show

    else:
        call cam_background from _call_cam_background_3
        show FG cam-shum-noact at laptop_screen
        ## сообщаем об отсутствии интересного и возвращаемся к выбору камеры
        # "[view_cam[0].id] [view_cam[2]]"
        if view_cam[0].id+'-'+str(view_cam[2]) not in cam_flag:
            $ cam_flag.append(view_cam[0].id+'-'+str(view_cam[2]))
            ## случайная фраза
            Max_00 "Сейчас здесь ничего не происходит."
        call screen cam_show


label cam_background:
    ### показываем пустой фон локации
    if '06:00' <= tm < '22:00':
        if current_room == house[5]:
            scene BG char Max laptop-day-01t
        else:
            scene BG char Max laptop-day-01
    else:
        if current_room == house[5]:
            scene BG char Max laptop-night-01t
        else:
            scene BG char Max laptop-night-01
    $ tod = {
        '06:00'<=tm<'11:00':' morning',
        '11:00'<=tm<'19:00':' day',
        '19:00'<=tm<'22:00':' evening',
        tm<'06:00'or'22:00'<=tm:' night'}[True]
    if tod in [' night', ' evening'] and len(view_cam[0].cur_char)>0 and chars[view_cam[0].cur_char[0]].plan_name not in ['sleep', 'sleep2']:
        $ tod = ' tv-evening' if chars[view_cam[0].cur_char[0]].plan_name in ['tv', 'tv2', 'night_tv'] else ' evening'
    $ renpy.show('BG-cam house '+view_cam[0].id.replace('_', '')+'-'+str(view_cam[2])+tod, at_list=[laptop_screen,])
    if current_room == house[5] and view_cam[0].id == 'my_room':
        $ renpy.show('Max cams patch '+tod, at_list=[laptop_screen,])

    return


label after_buying:
    while len(purchased_items) > 0:
        $ buying_item = purchased_items.pop()

        if buying_item==items['photocamera']:
            Max_01 "{i}( Так, фотокамеру я заказал, осталось дождаться доставки... ){/i}"
            Max_07 "{i}( Интересно, а в чём тётя Кира будет фотографироваться из одежды? Ей это нужно для порно-портфолио... Так может мне стоит прикупить что-нибудь сексуальное для неё?! Например, более откровенную ночнушку! Это пойдёт мне только в плюс... ){/i}"
            $ poss['aunt'].stages[3].ps = _("А ещё, будет не лишним, купить для этой фотосессии сексуальную сорочку для моей любимой тёти!")
            $ items['nightie2'].unblock()
            $ notify_list.append(_("В интернет-магазине доступен новый товар."))

    return


label after_load:
    # срабатывает каждый раз при загрузке сохранения или начале новой игры
    # проверяем на версию сохранения, при необходимости дописываем/исправляем переменные

    if renpy.loadable('extra/extra.webp'):
        $ set_extra_album()

    if 'current_ver' in globals():
        "ver [current_ver], _ver [_version], conf.ver [config.version]"

        if _version < current_ver or current_ver < "0.06.0.999":
            call old_fix

    else:
        "_ver [_version], conf.ver [config.version]"

    if _version < config.version:
        call update_06_5

        call set_alice_schedule
        call set_ann_schedule
        call set_eric_schedule
        call set_kira_schedule
        call set_lisa_schedule

        $ checking_items()
        $ checking_clothes()

        $ _version = config.version

    return


label update_06_5:

    if _version < "0.06.4.01":
        # $ current_ver = "0.06.4.01"
        $ _version = "0.06.4.01"

        $ poss['ass'] = Poss(_("Забота о попках"), [
                PossStage("interface poss ass ep01", _("Интересно получилось! Я ради интереса сказал Алисе, что больше не хочу за неё заступаться, когда её наказывают, но готов это делать и дальше, если она согласится, чтобы её шлёпал я.\nОна сперва приняла такой уговор в штыки, но после нескольких наказаний от мамы всё же согласилась, чтобы её шлёпал я. По крайней мере, если получилось спасти Алису от маминой руки. Надо так же не забыть обсудить с ней, когда можно её отшлёпать.\n\nПравда есть небольшой нюанс, благодаря которому Алиса и согласилась на это... Я пообещал, что отшлёпаю её нежно. Да уж, будет не просто устоять и не влепить по её попке за то, как стервозно она себя вела...")),  #0
                PossStage("interface poss ass ep02", _("Зрелище действительно завораживающее! Умудриться раздеть и отшлёпать свою старшую сестрёнку не многим, наверно, доводилось...\nХоть она капризничает и сыпет угрозами при этом, но похоже моя настойчивость взяла верх. Любоваться её голой и упругой попкой одно удовольствие, как и шлёпать по ней.\n\nИ теперь мне понятно, как не перегибать палку, чтобы наслаждаться этим приватным наказанием как можно дольше..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),  #1
            ])

    if _version < "0.06.4.02":
        $ _version = "0.06.4.02"

        python:
            renpy.dynamic('flag', 'dcv_tmp', 'wcv_tmp')
            flag = Other_Flags_and_counters()

            mgg.id = 'mgg'
            mgg.reinit()

            for char in chars:
                chars[char].id = char
                chars[char].reinit()

                chars[char].gifts = list(set(chars[char].gifts))

            mgg.clothes   = clothes[mgg]
            lisa.clothes  = clothes[lisa]
            alice.clothes = clothes[alice]
            ann.clothes   = clothes[ann]

            for char in sorry_gifts:
                chars[char].sorry = sorry_gifts[char]

            ann.daily.bath          = peeping.pop('ann_bath', 0)
            ann.daily.shower        = peeping.pop('ann_shower', 0)
            ann.daily.tvwatch       = talk_var.pop('ann_tv', 0)
            ann.daily.ask_money     = talk_var.pop('ask_money', 0)
            ann.hourly.sleep        = peeping.pop('ann_sleep', 0)
            ann.hourly.dressed      = peeping.pop('ann_dressed', 0)
            ann.flags.erofilms      = talk_var.pop('ann_movie', 0)

            lisa.daily.bath         = peeping.pop('lisa_bath', 0)
            lisa.daily.shower       = peeping.pop('lisa_shower', 0)
            lisa.daily.dishes       = talk_var.pop('lisa_dw', 0)
            lisa.daily.homework     = int(flags.pop('lisa_hw', 0))
            lisa.hourly.dressed     = peeping.pop('lisa_dressed', 0)
            lisa.flags.nakedpunish  = flags.pop('lisa.nakedpunish', False)
            lisa.flags.hugs_type    = flags.pop('lisa_superhug', 0)
            lisa.flags.pun          = talk_var.pop('lisa.pun', 0)
            lisa.flags.m_foot       = talk_var.pop('lisa.footmass', 0)
            lisa.flags.kiss_lesson  = talk_var.pop('kiss_lessons', 0)
            lisa.flags.help         = talk_var.pop('help.hw', 0)
            lisa.flags.truehelp     = talk_var.pop('truehelp', 0)
            lisa.stat.kiss          = talk_var.pop('kiss_massage', 0)   # поцелуй во время массажа рук заносим ещё и в статистику поцелуев
            lisa.stat.sh_breast     = talk_var.pop('lisa.sh_br', 0) + lisa.flags.m_foot//2
            lisa.flags.promise      = flags.pop('promise_kiss', 0)
            lisa.flags.crush        = talk_var.pop('boy', 0)
            lisa.dcv.punpause       = dcv.pop('lisa.punpause', Daily())
            lisa.dcv.sweets         = dcv.pop('lisa_sweets', Daily())
            lisa.dcv.battle         = dcv.pop('lizamentor', Daily())
            lisa.dcv.battle.stage   = talk_var.pop('fight_for_Lisa', 0)
            lisa.dcv.intrusion      = dcv.pop('ae_ed_lisa', Daily())
            lisa.dcv.seduce         = dcv.pop('lisa_mentor', Daily())
            lisa.dcv.seduce.stage   = talk_var.pop('teachkiss', 0)
            lisa.dcv.other          = dcv.pop('lisa.ad', Daily())
            lisa.dcv.special        = dcv.pop('film_punish', Daily())

            if lisa.flags.m_foot < 0:
                lisa.flags.m_foot = 0

            if not talk_var['lisa.handmass']<0:
                lisa.flags.handmass = True
                lisa.daily.massage  = talk_var['lisa.handmass']

            talk_var.pop('lisa.handmass', 0)

            alice.daily.bath        = peeping.pop('alice_bath', 0)
            alice.daily.shower      = peeping.pop('alice_shower', 0)
            alice.daily.blog        = peeping.pop('alice_blog', 0)
            alice.daily.blog_we     = peeping.pop('blog_with_eric', 0)
            alice.daily.dishes      = talk_var.pop('alice_dw', 0)
            alice.daily.tvwatch     = talk_var.pop('alice_tv', 0)
            alice.daily.massate     = talk_var.pop('al.tv.mas', 0)
            alice.daily.oiled       = talk_var.pop('sun_oiled', 0)
            alice.daily.drink       = flags.pop('alice.drink', 0)
            alice.daily.smoke       = talk_var.pop('smoke', 0)
            alice.hourly.sleep      = peeping.pop('alice_sleep', 0)
            alice.hourly.dressed    = peeping.pop('alice_dressed', 0)
            alice.hourly.sun_cream  = talk_var.pop('alice_sun', 0)
            alice.flags.nakedpunish = flags.pop('alice.nakedpunish', False)
            alice.flags.hugs_type   = flags.pop('alice_hugs', 0)
            alice.flags.pun         = talk_var.pop('alice.pun', 0)
            alice.flags.m_foot      = flags.pop('alice.tv.mass', 0)
            alice.flags.hip_mass    = flags.pop('double_mass_alice', 0)
            alice.flags.private     = flags.pop('alice.privpunish', 0)
            alice.stat.footjob      = talk_var.pop('al.tvgood', 0)
            alice.stat.mast         = int(flags.pop('cam_fun_alice', 0))
            alice.req.req           = flags.pop('smoke.request', None)
            alice.req.result        = flags.pop('smoke', None)
            alice.req.noted         = flags.pop('noted', False)
            alice.flags.crush       = talk_var.pop('blog', 0)
            alice.flags.incident    = flags.pop('talkaboutbath', 0)
            alice.dcv.punpause      = dcv.pop('alice.punpause', Daily())
            alice.dcv.prudence      = dcv.pop('alice.prudence', Daily())
            alice.dcv.sweets        = dcv.pop('alice_sweets', Daily())
            alice.dcv.battle        = dcv.pop('eric_alice', Daily())
            alice.dcv.battle.stage  = talk_var.pop('fight_for_Alice', 0)
            alice.dcv.photo         = dcv.pop('gift.lingerie', Daily())
            alice.dcv.intrusion     = dcv.pop('eric.lingerie', Daily())
            alice.dcv.set_up        = dcv.pop('betray_smoke', Daily())
            alice.dcv.feature       = dcv.pop('alice.secret', Daily())
            alice.dcv.seduce        = dcv.pop('tvchoco', Daily())
            alice.dcv.other         = dcv.pop('about_blog', Daily())
            alice.dcv.special       = dcv.pop('smoke', Daily())
            alice.dcv.gifts         = dcv.pop('secretbook', Daily())
            alice.dcv.private       = dcv.pop('a.privpunished', Daily())

            mgg.flags.nakedpunish   = flags.pop('max.nakedpunish', False)
            mgg.flags.tired         = flags.pop('little_energy', False)

            if 'kira' in chars:
                kira.daily.bath         = peeping.pop('kira_bath', 0)
                kira.daily.shower       = peeping.pop('kira_shower', 0)
                kira.hourly.sleep       = peeping.pop('kira_sleep', 0)
                kira.flags.m_foot       = talk_var.pop('kira.bath.mass', 0)
                kira.flags.m_breast     = talk_var.pop('kira.tv.touch', 0)
                kira.flags.porno        = talk_var.pop('kira.porn', 0)
                kira.flags.promise      = flags.pop('promise.cuni.kira', False)
                kira.stat.handjob       = flags.pop('hj_in_pool', 0)
                kira.stat.footjob       = int(flags.pop('kira.bath.fj', 0))
                kira.stat.blowjob       = int(flags.pop('kira.tv.bj', 0))
                kira.sleepnaked         = flags.pop('strip.show', 0)
                kira.dcv.sweets         = dcv.pop('kiratalkcuni', Daily())
                kira.dcv.photo          = dcv.pop('kira.nextphoto', Daily())
                kira.dcv.feature        = dcv.pop('kiratalk', Daily())
                kira.dcv.battle.stage   = talk_var.pop('fight_for_Kira', 0)

                if kira.dcv.feature.stage > 7:
                    kira.dcv.photo = 2

            if 'eric' in chars:
                eric.daily.sex_ed       = peeping.pop('ael_sexed', 0)
                eric.daily.sex          = peeping.pop('ann_eric_sex1', 0)
                eric.daily.tv_sex       = peeping.pop('ann_eric_tv', 0)
                eric.flags.ladder       = talk_var.pop('ae.ladd', 0)
                eric.stat.handjob       = flags.pop('ae.tv.hj', 0)
                eric.stat.blowjob       = flags.pop('ae.tv.bj', 0)
                eric.stat.mast          = int(flags.pop('eric.firstjerk', 0)+int(flags['eric.photo1'])*2+int(flags['eric.photo2'])*2)
                eric.flags.crush        = talk_var.pop('empathic', 0)
                eric.daily.ask_money    = 1 if dcv.pop('eric.money', Daily()).lost else 0

            dcv['mw'].stage         = flags.pop('morning_erect', 0)

            dcv_tmp                 = Daily_list()
            dcv_tmp.clearpool       = dcv.pop('clearpool', Daily())
            dcv_tmp.buyfood         = dcv.pop('buyfood', Daily())
            dcv_tmp.mw              = dcv.pop('mw', Daily())
            dcv_tmp.new_pun         = dcv.pop('new_pun', Daily())

            wcv_tmp = Weekly_list()
            wcv_tmp.catch_Kira      = wcv.pop('catch.Kira', Weekly(4))

            flag.lisa_fd            = talk_var.pop('lisa_fd', 0)
            flag.back_shop          = EventsByTime['back_shoping'].stage
            flag.bonus_from_eric    = talk_var.pop('bonus_from_eric', [])
            flag.how_to_kiss        = talk_var.pop('ask.teachkiss', [])
            flag.lisa_sexed         = talk_var.pop('ae_lisa_number', -1)
            flag.breakfast          = talk_var.pop('breakfast', 0)
            flag.dinner             = talk_var.pop('dinner', 0)
            flag.courier1           = talk_var.pop('courier1', 0)
            flag.courier2           = talk_var.pop('courier2', 0)
            flag.eric_jerk          = flags.pop('eric.jerk', False)
            flag.eric_noticed       = flags.pop('eric.noticed', False)
            flag.eric_photo1        = flags.pop('eric.photo1', 0)
            flag.eric_photo2        = flags.pop('eric.photo2', 0)
            flag.eric_fee           = talk_var.pop('eric.fee', 0)
            flag.voy_stage          = talk_var.pop('eric.voy.stage', 0)
            flag.ladder             = flags.pop('ladder', 0)
            flag.credit             = flags.pop('credit', 0)
            flag.warning            = flags.pop('warning', 0)
            flag.stopkiss           = flags.pop('lisa.stopkiss', 0)
            flag.add_training       = flags.pop('dinner_ab_lisa', 0)
            flag.about_earn         = flags.pop('dinner_ab_earn', False)
            flag.hint_cources       = flags.pop('hint.cources', False)
            flag.l_ab_sexed         = flags.pop('l.ab_aeed', False)
            flag.film_punish        = flags.pop('film_punish', False)
            flag.noclub             = flags.pop('noclub', False)
            flag.cur_series         = flags.pop('cur_series', 0)
            flag.cur_movies         = flags.pop('cur_movies', [])

            flags.pop('Lisa_bathrobe', 0)
            flags.pop('about_poss', 0)
            flags.pop('cam2bath', 0)

            del globals()['clothes']
            del globals()['sorry_gifts']
            del globals()['peeping']
            del globals()['EventsByTime']

            flags   = flag
            dcv     = dcv_tmp
            wcv     = wcv_tmp

        if alice.flags.nakedpunish:
            # Алису наказывали голой
            if alice.dcv.intrusion.stage in [5, 7]:
                # опередил Эрика с кружевным бельём
                $ alice.flags.defend = 3
            elif 'sexbody1' in alice.gifts:
                $ alice.flags.defend = 2

        if poss['risk'].stages[6].used:
            # были обнимашки за периодическое дарение сладостей
            if alice.dcv.intrusion.stage in [5, 7]:
                # опередил Эрика с кружевным бельём
                $ alice.flags.hugs = 4
            elif 'sexbody1' in alice.gifts:
                $ alice.flags.hugs = 3

    if _version < "0.06.4.03":
        $ items.pop('ann_movie', None)

    return
