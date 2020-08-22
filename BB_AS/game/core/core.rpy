

label Waiting:
    # обработчик ожидания, запускает события по времени
    # "ждем [spent_time]"
    $ renpy.block_rollback()

    $ prevday = day
    $ prevtime = tm

    if alarm_time != '':
        $ d2 = TimeDifference(prevtime, alarm_time)
        if spent_time == 0 or d2 < spent_time:
            $ spent_time = d2

    $ Wait(spent_time)

    # ищем стартующее по времени событие
    $ cut_id = GetCutEvents(prevtime, tm, status_sleep)

    # и устанавливаем время на начало кат-события, если оно есть
    if cut_id != '':
        $ __name_label = EventsByTime[cut_id].label
        if prevtime > tm:
            if prevtime <= EventsByTime[cut_id].tm < '23:59':
                $ day = prevday
        $ tm = EventsByTime[cut_id].tm
    else:
        $ __name_label = ''

    $ spent_time = TimeDifference(prevtime, tm) ## реально прошедшее время (до будильника или кат-события)

    # если прошло какое-то время, проверим необходимость смены одежды
    $ ChoiceClothes()

    if prevtime[:2] != tm[:2]:
        # почасовой сброс
        $ flags['little_energy'] = False
        $ peeping['alice_sleep'] = 0
        $ peeping['ann_sleep'] = 0
        $ peeping['ann_dressed'] = 0
        $ peeping['lisa_dressed'] = 0
        $ peeping['alice_dressed'] = 0
        # позы обновляются каждый час
        $ pose3_1 = renpy.random.choice(['01', '02', '03'])
        $ pose3_2 = renpy.random.choice(['01', '02', '03'])
        $ pose3_3 = renpy.random.choice(['01', '02', '03'])
        $ pose3_4 = renpy.random.choice(['01', '02', '03'])
        $ pose2_1 = renpy.random.choice(['01', '02'])
        $ pose2_2 = renpy.random.choice(['01', '02'])
        $ pose2_3 = renpy.random.choice(['01', '02'])
        $ tv_scene = '' # renpy.random.choice(['', 'bj', 'hj'])
        $ talk_var['alice_sun'] = 0 # прдложить Алисе нанести масло можно пробовать каждый час (пока не нанес)
    if prevtime < '12:00' <= tm:
        call Noon from _call_Noon
    if day != prevday:
        call Midnight from _call_Midnight
    if prevtime < "04:00" < tm:
        call NewDay from _call_NewDay


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

    # обновим extra-info для сохранений
    $ NewSaveName()

    if __name_label != '' and renpy.has_label(__name_label):
        # "запуск [__name_label]"
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
        jump expression __name_label

    # иначе запускаем блок 'после ожидания'
    if at_comp:
        jump cam_after_waiting
    else:
        jump AfterWaiting


label Midnight:
    # "Полночь"
    $ random_loc_ab = renpy.random.choice(['a', 'b'])
    $ random_sigloc = renpy.random.choice(['n', 't'])

    if 'smoke' in talk_var:
        $ talk_var['smoke'] = 0
        if flags['smoke.request'] == 'money':
            $ flags['smoke'] = None
            $ flags['smoke.request'] = None
        elif flags['smoke']=='nojeans': # если требование не носить джинсы, оно не может быть нарушено
            pass
        elif flags['smoke.request'] is not None and (flags['smoke'] is None or flags['smoke'][:3] != 'not'):
            # Если требование Макса было и это не деньги
            $ __chance = GetDisobedience()  # шанс, что Алиса не будет соблюдать договоренность
            if RandomChance(__chance):
                $ flags['smoke'] = 'not_' + flags['smoke.request']
                $ flags['noted'] = False  # нарушение ещё не замечено Максом
                if flags['smoke.request'] == 'nopants':
                    $ alice.nopants = False
                elif flags['smoke.request'] == 'sleep':
                    $ alice.sleeptoples = False
            else:
                $ flags['smoke'] = flags['smoke.request']
                if flags['smoke.request'] == 'nopants':
                    $ alice.nopants = True
                elif flags['smoke.request'] == 'sleep':
                    $ alice.sleeptoples = True
    $ GetDeliveryList()

    if peeping['ann_eric_tv'] and flags['ae.tv.hj'] > 0:
        $ ae_tv_order.pop(0)
        if not ae_tv_order:
            $ ae_tv_order = ['01', '02', '03', '04', '05', '06']
            $ renpy.random.shuffle(ae_tv_order)  # перемешаем список случайным образом
    python:
        # уменьшение счетчика событий, зависимых от прошедших дней
        for i in dcv:  #
            if dcv[i].enabled and not dcv[i].done:
                dcv[i].set_lost(dcv[i].lost-1)

        # сбросим подглядывания
        for key in peeping:
            peeping[key] = 0

        if SpiderResp > 0:
            SpiderResp -= 1

        for char in sorry_gifts:
            if sorry_gifts[char].owe and sorry_gifts[char].left > 0:
                sorry_gifts[char].left -= 1

        # для каждого типа одежды каждого персонажа запустим рандомную смену
        for char in clothes:
            l = clothes[char].GetList()
            for cl_t in l:
                if eval('clothes[char].'+cl_t+'.rand'):
                    eval('clothes[char].'+cl_t+'.SetRand()')
    return


label NewDay:
    # "Новый день"
    $ talk_var['ask_money'] = 0 # просили денег у Анны
    $ talk_var['lisa_dw']   = 0 # разговор о помывке посуды
    $ talk_var['alice_dw']  = 0 # разговор о помывке посуды
    $ talk_var['ann_tv']    = 0 # смотрели тв с Анной
    $ talk_var['alice_tv']  = 0 # смотрели тв с Алисой
    $ talk_var['al.tv.mas'] = 0 # предлагали Алисе массаж у тв
    if talk_var['lisa.handmass']>0:
        $ talk_var['lisa.handmass']=0

    python:
        # сбросим подглядывания
        for key in peeping:
            peeping[key] = 0

    if 0 < GetWeekday(prevday) < 6:
        if poss['sg'].stn > 0 and not flags['lisa_hw']:  # был разговор с Лизой по поводу наказаний и не помогал
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
            0,  # Макс шантажировал Алису (1-передумал, 2-неудачно, 3-деньги, 4-перекур топлес, 5-лифчик, 6-трусики)
            0,  # Макс подставлял Алису
            0,  # Макс заступился за Алису перед наказанием
            0,  # Ализа понесла наказание
            0,  # подозрительность
            ])
        $ del punalice[14:]

    $ flags['lisa_hw'] = False

    if clothes[lisa].learn.rand:
        if 'kira' not in chars:
            $ clothes[lisa].casual.cur = 1 if all(['bathrobe' in lisa.gifts, lisa.GetMood()[0] > 1]) else 0
        else:
            $ __r1 = renpy.random.randint(1, 2)
            $ clothes[lisa].casual.cur = __r1 if all(['bathrobe' in lisa.gifts, lisa.GetMood()[0] > 1]) else 2 if 'bathrobe' in lisa.gifts else 1
        #     if all(['bathrobe' in lisa.gifts, lisa.GetMood()[0] > 1]):
        #         $ print('rand '+str(__r1))
        #     else:
        #         $ print('max clot '+str(2 if 'bathrobe' in lisa.gifts else 1))

    if mgg.credit.debt > 0:        # если кредит не погашен
        $ mgg.credit.left -= 1       # уменьшим счетчик дней
        if mgg.credit.left == 0:   # если счетчик дней кончился
            $ mgg.credit.charge()    # начислим штраф

    $ talk_var['sun_oiled'] = 0  # Алиce можно намазать кремом
    $ flags['alice.drink'] = 0   # Алиса протрезвела

    $ cam_flag = []  # обнулим подсматривания через камеры
    $ ann_eric_scene = ''
    $ cam_poses.clear()  # обнулим список поз для камер
    return


label Noon:
    $ __new_items = False
    if day > 12 and not ('nightie' in ann.gifts or items['nightie'].have or items['nightie'].InShop):
        $ items['nightie'].InShop = True
        $ __new_items = True
    if ('secretbook' in dcv and dcv['secretbook'].done
        and 'erobook_'+str(dcv['secretbook'].stage) in items
        and not items['erobook_'+str(dcv['secretbook'].stage)].InShop): # прошел откат после дарения книги, можно купить следующую
        # dcv['secretbook'].stage += 1
        $ items['erobook_'+str(dcv['secretbook'].stage)].InShop = True
        $ __new_items = True

    if __new_items:
        $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    return


label AfterWaiting:

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

    $ persone_button1 = None
    $ persone_button2 = None
    $ persone_button3 = None

    $ Distribution() # распределяем персонажей по комнатам и устанавливаем фоны для текущей локации

    # отключение возможности помыть посуду, если её вымыли Лиза или Алиса
    if not dishes_washed:
        if tm > '20:00':
            $ dishes_washed = True
        elif (day+2) % 7 != 6:
            $ __name_label = ''
            if (day+2) % 7 == 0:
                $ __cur_plan = alice.get_plan(day, '10:00')
                if __cur_plan is not None:
                    $ __name_label = __cur_plan.label
            else:
                $ __cur_plan = alice.get_plan(day, '11:00')
                if __cur_plan is not None:
                    $ __name_label = __cur_plan.label

            if __name_label == 'alice_dishes':
                if (GetWeekday(day) == 0 and tm >= '11:00') or tm >= '12:00':
                    $ dishes_washed = True

    # обновим extra-info для сохранений
    $ NewSaveName()

    $ __name_label = ''
    # поиск управляющего блока для персонажа, находящегося в текущей комнате
    if len(current_room.cur_char) > 0:
        $ __cur_plan = chars[current_room.cur_char[0]].get_plan()
        if __cur_plan is not None:
            $ __name_label = __cur_plan.label

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

    if __name_label != '' and renpy.has_label(__name_label):
        # управляющий блок найден и существует
        call expression __name_label from _call_expression
    else:
        # устанавливаем фон комнаты без персонажей
        if current_room.cur_bg.find('_') >= 0:
            scene image(current_room.cur_bg.replace('_', ''))
        else:
            scene image(current_room.cur_bg)

    if status_sleep:
        $ status_sleep = False
        with fade
    if mgg.energy < 10 and not flags['little_energy']:
        Max_00 "Я слишком устал. Надо бы вздремнуть..."
        $ flags['little_energy'] = True

    if mgg.energy < 5:
        jump LittleEnergy
    call screen room_navigation


label night_of_fun:

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
            if not house[5].cur_char and not flags['warning']:
                # на веранде никого, разговора про веранду ещё не было
                $ flags['warning'] = True
                menu:
                    Max_09 "Думаю, просматривать сейчас камеры не самая лучшая идея. Не хватало ещё, чтобы Лиза что-то заметила... Может, стоит пойти на веранду? Там сейчас не должно никого быть..."
                    "{i}идти на веранду{/i}":
                        $ current_room = house[5]
                        $ cam_flag.append('notebook_on_terrace')
                    "{i}не сейчас{/i}":
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
            if not house[5].cur_char and not flags['warning']:
                # на веранде никого, разговора про веранду ещё не было
                $ flags['warning'] = True
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

        $ __cur_plan = chars[view_cam[0].cur_char[0]].get_plan()
        $ __cam_label = 'cam'+str(view_cam[2])+'_'+__cur_plan.label if __cur_plan is not None else ''

        if __cam_label!='' and renpy.has_label(__cam_label):
            call cam_background
            call expression __cam_label
        else:
            call cam_background

        # show FG cam-shum-act at laptop_screen

        call screen cam_show
    elif current_room == view_cam[0]:
        ## камера текущей локации. Макс сидит за компом
        call cam_background

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
        call cam_background
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


label after_load:
    # срабатывает каждый раз при загрузке сохранения или начале новой игры
    # проверяем на версию сохранения, при необходимости дописываем/исправляем переменные

    # "ver [current_ver]"
    if current_ver == 'v0.01.TechDemo':
        scene BG villa-door
        "Сохранения версии техно-демо не поддерживаются. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    elif current_ver[:5] == 'v0.02':
        scene BG villa-door
        "К сожалению сохранения этой версии не поддерживаются из-за большого количества внутренних изменений. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    elif current_ver < '0.03.5.000':
        scene BG villa-door
        "К сожалению сохранения этой версии не поддерживаются из-за большого количества внутренних изменений. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    else:
        if current_ver < "0.03.5.002":
            $ current_ver = "0.03.5.002"

            $ poss['seduction'].stages[1].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['Schoolmate'].stages[0].ps = _("Да, и похоже о своём мальчике Лиза разговаривает только, когда у неё хорошее настроение... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['blog'].stages[0].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['Swimsuit'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['Swimsuit'].stages[4].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['nightclub'].stages[2].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['nightclub'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['nightclub'].stages[4].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['smoke'].stages[1].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['smoke'].stages[2].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['sg'].stages[4].ps = _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['sg'].stages[5].ps = _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['sg'].stages[6].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['sg'].stages[6].ps = _("Сомневаюсь, что теперь получится её подставить, уж слишком большое недоверие она ко мне испытывает. \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['spider'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['alpha'].stages[0].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['SoC'].stages[8].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ poss['risk'].stages[8].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        if current_ver < "0.03.5.003":
            $ current_ver = "0.03.5.003"

            $ poss['sg'].stages.append(PossStage("interface poss lessons ep01", _("Я помогал Лизе с уроками какое-то время, причём безвозмездно, но это стало довольно скучным делом и я намеренно стал делать ошибки так, чтобы ей ставили двойки и наказывали... И вот, после очередной двойки и наказания от мамы, она обратилась ко мне за помощью. Я согласился, но с условием, что она будет спать только в футболке и трусиках. И думаю, что мне удастся её ещё на что-нибудь раскрутить..."),
                        _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")))

        if current_ver < "0.03.9.001":
            $ current_ver = "0.03.9.001"

            $ poss['seduction'].stages[1].ps = ""
            $ poss['seduction'].stages.extend([
                PossStage("interface poss mentor ep02", _("Лиза снова увидела мой утренний стояк. На этот раз маму она не позвала, что уже хорошо. Хотя, смотрела она на мой член не только с подозрением, но ещё и с интересом. По крайней мере, мне так показалось. Думаю, нужно с ней об этом поговорить...")),
                PossStage("interface poss mentor ep03", _("Это, конечно, не точно, но Лиза хотела потрогать мой член, думая, что я спал. И судя по её реакции на то, что я это увидел, даже она сама с себя удивилась. Посмотрим, что она потом об этом скажет..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),
                ])

            $ EventsByTime['MorningWoodCont'] = CutEvent('06:30', label='MorningWoodCont', desc='утренний стояк продолжение', variable="all([day>=7, dcv['mw'].done, flags['morning_erect']%2==0, poss['seduction'].stn > 0])", sleep=True, cut=True)
            $ dcv['mw'] = Daily(done=True, enabled=True)

        if current_ver < "0.03.9.002":
            $ current_ver = "0.03.9.002"

            $ lisa.add_schedule(Schedule((0, 1, 2, 3, 4, 5, 6), '8:0', '8:59', 'read', _("читает в нашей комнате"), 'house', 0, 'lisa_read', talklabel='lisa_read_closer', glow=105))
            $ flags['alice.tv.mass'] = 0
            $ talk_var['al.tv.mas'] = 0
            $ poss['seduction'].stages[3].ps = ""
            $ poss['seduction'].stages.append(PossStage("interface poss mentor ep04", _("Похоже, интерес Лизы к противоположному полу и всему, что связано со взрослой жизнью, растёт не по дням, а по часам. Не знаю уж, мой стоящий по утрам член так её раззадорил или ещё что-то, но она согласилась меня слушаться по вопросам о мальчиках и всем этим взрослым штучкам... Вот только прежде, чем учить, может быть стоит самому чему-то научиться? А самое главное - при этом ничего не испортить, а то она снова откажется..."), _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")))

            $ kol_choco = 0
            $ items['choco'] = Item(_("КОНФЕТЫ С ЛИКЁРОМ"), _("Шоколадные конфеты с ликёром. Уникальные ароматизаторы скрывают вкус алкоголя. Отлично поднимают настроение. Очень крепкие."), "choco", 2, 20)
            $ dcv['tvchoco'] = Daily(done=True, enabled=True)
            $ tier = 0

        if current_ver < "0.03.9.003":
            $ current_ver = "0.03.9.003"

            $ alice_good_mass = _("{color=#E59400}{i}Алисе понравился массаж!{/i}{/color}\n")
            $ alice_bad_mass  = _("{color=#E59400}{i}Алисе не понравился массаж!{/i}{/color}\n")
            $ poss['nightclub'].stages[2].ps = ""
            $ poss['nightclub'].stages[3].ps = ""
            $ poss['nightclub'].stages[4].ps = ""
            $ poss['nightclub'].stages[6].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ dcv['alice.secret'] = Daily(done=True, enabled=True)

        if current_ver < "0.03.9.004":
            $ current_ver = "0.03.9.004"

            python:
                clothes = {
                    lisa  : Clothing(),
                    alice : Clothing(),
                    ann   : Clothing(),
                    mgg   : Clothing(),
                    }

                clothes[lisa].casual = Clothes(_("Повседневная"), [
                        Garb('a', '01a', 'Обычная одежда'),
                    ])
                clothes[lisa].learn = Clothes(_("За уроками"), [
                        Garb('a', '01a', 'Обычная одежда'),
                        Garb('c', '04b', 'Полотенце', True),
                    ])
                if 'bathrobe' in lisa.gifts:
                    clothes[lisa].casual.sel.insert(1, Garb('b', '04', _("ШЕЛКОВЫЙ ХАЛАТ"), True))
                    clothes[lisa].learn.sel.insert(1, Garb('b', '04', 'Халатик', True))

                clothes[lisa].swimsuit = Clothes(_("КУПАЛЬНИК"), [
                        Garb('a', '03', 'Закрытый купальник'),
                    ])
                if 'bikini' in lisa.gifts:
                    clothes[lisa].swimsuit.sel.insert(1, Garb('b', '03b', 'КУПАЛЬНИК КРАСНЫЙ', True))
                    clothes[lisa].swimsuit.cur = 1

                clothes[lisa].sleep = Clothes(_("Для сна"), [
                        Garb('a', '02', 'Обычная одежда'),
                        Garb('b', '02a', 'Маечка и трусики'),
                    ])
                if poss['sg'].stn > 2:
                    clothes[lisa].sleep.cur = 1

                clothes[alice].casual = Clothes(_("Повседневная"), [
                        Garb('a', '01a', 'Обычная одежда', True),
                    ])
                if 'pajamas' in alice.gifts:
                    clothes[alice].casual.sel.insert(1, Garb('b', '01c', 'Пижама', True))

                clothes[ann].casual = Clothes(_("Повседневная"), [
                        Garb('a', '01a', 'Обычная одежда', False, True),
                        Garb('b', '01b', 'Футболка', False, True),
                    ])
                clothes[ann].casual.rand = True
                clothes[ann].cook_morn = Clothes(_("Для приготовления завтрака"), [
                        Garb('a', '05b', 'Спортивная форма + фартук', False, True),
                        Garb('b', '01c', 'Футболка + фартук', False, True),
                    ])
                clothes[ann].cook_morn.rand = True
                clothes[ann].cook_eve = Clothes(_("Для приготовления ужина"), [
                        Garb('b', '01c', 'Футболка + фартук', False, True),
                    ])
                clothes[ann].rest_eve = Clothes(_("Для вечернего отдыха"), [
                        Garb('a', '01b', 'Футболка', False, True),
                        Garb('b', '04b', 'Полотенце', False, True),
                    ])
                clothes[ann].rest_eve.rand = True
                clothes[ann].sleep = Clothes(_("Для сна"), [
                        Garb('a', '02', 'Обычная одежда для сна', True),
                    ])
                if 'nightie' in ann.gifts:
                    clothes[ann].sleep.sel.append(Garb('b', '02f', 'НОЧНУШКА', True))
                    clothes[ann].sleep.rand = True

                clothes[mgg].casual = Clothes(_("Повседневная"), [
                        Garb('a', '01a', 'Обычная одежда', True),
                    ])
                if items['max-a'].have:
                    clothes[mgg].casual.sel.append(Garb('b', '01b', 'МУЖСКИЕ МАЙКА И ШОРТЫ', True))
                    clothes[mgg].casual.cur = 1

                del globals()['cloth_type']

        if current_ver < "0.03.9.005":
            $ current_ver = "0.03.9.005"

            $ clothes[lisa].learn.name = _("За уроками")
            $ clothes[ann].casual.sel[0].change = False
            $ clothes[ann].casual.sel[1].change = False
            $ clothes[ann].cook_morn.sel[0].change = False
            $ clothes[ann].cook_morn.sel[1].change = False
            $ clothes[ann].cook_eve.sel[0].change = False
            $ clothes[ann].rest_eve.sel[0].change = False
            $ clothes[ann].rest_eve.sel[1].change = False
            if 'bikini' in lisa.gifts:
                $ clothes[lisa].swimsuit.cur = 1

        if current_ver < "0.03.9.007":
            $ current_ver = "0.03.9.007"

            if 'nightie' in ann.gifts:
                $ clothes[ann].sleep.sel[1] = Garb('b', '02f', 'НОЧНУШКА', True)

            $ ann.add_schedule(Schedule((0, ), '12:0', '13:59', 'read', _("читает на веранде"), 'house', 5, 'ann_read', talklabel='ann_read_closer', glow=110))
            $ alice.add_schedule(
                    Schedule((0,), '10:0', '10:59', 'dishes', _("моет посуду"), 'house', 4, 'alice_dishes', variable='not dishes_washed', talklabel='alice_dishes_closer'),
                    Schedule((0,), '10:0', '10:59', 'read', _("читает на веранде"), 'house', 5, 'alice_read', talklabel='alice_read_closer', variable='dishes_washed', glow=110),
                    Schedule((1, 2, 3, 4, 5), '11:0', '11:59', 'dishes', _("моет посуду"), 'house', 4, 'alice_dishes', variable='not dishes_washed', talklabel='alice_dishes_closer'),
                    Schedule((1, 2, 3, 4, 5), '11:0', '11:59', 'read', _("читает на веранде"), 'house', 5, 'alice_read', talklabel='alice_read_closer', variable='dishes_washed', glow=110),
                    Schedule((1, 2, 3, 4, 5), '16:0', '17:59', 'read', _("читает на веранде"), 'house', 5, 'alice_read', talklabel='alice_read_closer', glow=110),
                    Schedule((0, 6), '18:0', '18:59', 'read', _("читает на веранде"), 'house', 5, 'alice_read', talklabel='alice_read_closer', glow=110),
                )

        if current_ver < "0.03.9.008":
            $ current_ver = "0.03.9.008"

            $ ann.add_schedule(Schedule((3, 6, 0), '0:0', '5:59', 'None', 'у Эрика дома'))
            $ talk_var['al.tvgood'] = 0
            if day > 5:
                $ talk_var['breakfast'] = 5
            if day > 4:
                $ talk_var['dinner'] = 4

            $ poss['alpha'].stages[0].ps = ""
            $ poss['alpha'].stages[2].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
            $ poss['alpha'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ flags['alice.drink'] = 0
            $ talk_var['lisa.sh_br'] = 0
            $ talk_var['lisa.footmass'] = -1
            $ talk_var['lisa.handmass'] = -1

            $ lisa.add_schedule(
                    Schedule((0, 1, 2, 3, 4, 5, 6), '21:0', '21:59', 'phone', _("лежит с телефоном в нашей комнате"), 'house', 0, 'lisa_phone', talklabel='lisa_phone_closer', glow=105),
                    Schedule((0, 6), '23:0', '23:59', 'phone', _("лежит с телефоном в нашей комнате"), 'house', 0, 'lisa_phone', talklabel='lisa_phone_closer', glow=105),
                    Schedule((6, ), '14:0', '14:59', 'read', _("читает в нашей комнате"), 'house', 0, 'lisa_read', talklabel='lisa_read_closer', glow=105),
                    Schedule((0, 6), '17:0', '18:59', 'read', _("читает в нашей комнате"), 'house', 0, 'lisa_read', talklabel='lisa_read_closer', glow=105),
                )


            $ poss['nightclub'].stages[6].ps = ""
            $ poss['nightclub'].stages[7].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

            $ flags['talkaboutbath'] = 0

        if current_ver < "0.03.9.009":
            $ current_ver = "0.03.9.009"

            $ EventsByTime['Kira arrival'] = CutEvent('08:40', label='Kira_arrival', desc='приезд Киры', variable="all([day>=18, GetWeekday(day)==6, talk_var['breakfast']==12, talk_var['dinner']==17])", cut=True)
            $ ann.add_schedule(Schedule((0, 6), '16:0', '16:59', 'read', _("читает на веранде"), 'house', 5, 'ann_read', talklabel='ann_read_closer', glow=110))

        if current_ver < "0.03.9.010":
            $ current_ver = "0.03.9.010"
            $ dcv['new_pun'] = Daily(done=True, enabled=True)
            if 'bathrobe' in lisa.gifts and len(clothes[lisa].casual.sel)<2:
                $ clothes[lisa].casual.sel.insert(1, Garb('b', '04', _("ШЕЛКОВЫЙ ХАЛАТ"), True))

        if current_ver < "0.03.9.011":
            $ current_ver = "0.03.9.011"
            $ clothes[ann].rest_morn = Clothes(_("Для утреннего отдыха"), [
                    Garb('a', '01b', 'Футболка', False, True),
                ])

        if current_ver < "0.03.9.012":
            $ current_ver = "0.03.9.012"
            $ talk_var['teachkiss'] = 0
            $ talk_var['ask.teachkiss'] = []
            $ dcv['lizamentor'] = Daily(done=True, enabled=True) # обучение Лизы
            $ poss['seduction'].stages[4].ps = ""
            $ poss['seduction'].stages.extend([
                PossStage("interface poss mentor ep05", _("Итак, Лиза поинтересовалась, чему же я собираюсь её учить. И сразу же поставила меня в глупую ситуацию. Я вроде бы должен её учить, но сам не умею даже целоваться! Нужно срочно найти кого-то, кто бы мне помог в этом... Да, легко сказать...")),
                PossStage("interface poss mentor ep06", _("Кажется, я нашёл ту, которая научит меня целоваться. И это... моя тётя! Это так странно... Ну она точно в этом вопросе понимает достаточно. Да я был бы рад любому учителю, но такой - идеален! Да, тётя Кира сказала, что лучше об этом поговорить в более интимной обстановке. Например, когда она ночью смотрит телек.")),
                PossStage("interface poss mentor ep06", _("Тётя Кира превосходный учитель поцелуев! Она согласилась меня иногда учить. Кто знает, может быть она научит и чему-то ещё?\n\nНу всё. Теперь нужно практиковаться в поцелуях с тётей Кирой и передавать полученные знания Лизе... Только вот её ещё нужно убедить..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}"))])
            if 'kira' in chars:
                $ kira.add_schedule(Schedule((0, 3), '3:00', '3:59', 'night_tv', 'ночной просмотр порно', 'house', 4, 'kira_night_tv', enabletalk=False, glow=110))
                $ peeping['kira_sleep'] = 0
                $ talk_var['kira.porn'] = 0
                $ talk_var['kira.bath.mass'] = 0

        if current_ver < "0.03.9.013":
            $ current_ver = "0.03.9.013"
            if 'kira' in chars:
                $ kira.add_schedule(Schedule((0, 3, 6), '8:00', '8:59', 'shower', 'в душе с Алисой', 'house', 3, 'kira_alice_shower', enabletalk=False, glow=140))

        if current_ver < "0.03.9.014":
            $ current_ver = "0.03.9.014"
            if 'bikini' in lisa.gifts:
                if not 'gift_swimsuit.swimsuit_show' in persistent.memories:
                    $ persistent.memories['gift_swimsuit.swimsuit_show'] = renpy.seen_label('gift_swimsuit.swimsuit_show')

            if renpy.seen_label('gift_pajamas'):
                if not 'gift_pajamas' in persistent.memories:
                    $ persistent.memories['gift_pajamas'] = flags['alice_hugs'] > 3

            if renpy.seen_label('Lisa_HomeWork.first_foot_mass'):
                if not 'Lisa_HomeWork.first_foot_mass' in persistent.memories:
                    $ persistent.memories['Lisa_HomeWork.first_foot_mass'] = True

            $ peeping['kira_bath'] = 0

        if current_ver < "0.03.9.015":
            $ current_ver = "0.03.9.015"

            $ talk_var['kira.tv.touch'] = 0

        if current_ver < "0.03.9.016":
            $ current_ver = "0.03.9.016"

            $ flags['kira.bath.fj'] = False
            $ flags['kira.tv.bj'] = False

        if current_ver < "0.03.9.017":
            $ current_ver = "0.03.9.017"

            $ peeping['kira_shower'] = 0

        if current_ver < "0.04.0.02":
            $ current_ver = "0.04.0.02"

            if GetRelMax('eric')[0] < -1:
                $ poss['alpha'].stages[2].used = False
                $ poss['alpha'].SetStage(3)

        if current_ver < "0.04.0.03":
            $ current_ver = "0.04.0.03"

            $ EventsByTime['night_of_fun'].tm = '02:30'

        if current_ver < "0.04.0.04":
            $ current_ver = "0.04.0.04"

            if items['max-a'].have:
                $ items['max-a'].InShop = False
            if poss['nightclub'].stn >= 5 and kol_choco == 0:
                $ items['choco'].InShop = True
            if 'kira' in chars:
                $ flags['hint.cources'] = False

            if talk_var['dinner'] > talk_var['breakfast']+4:
                $ talk_var['breakfast'] = 4
                $ talk_var['dinner'] = 4

        if current_ver < "0.04.0.05":
            $ current_ver = "0.04.0.05"
            if 'talkaboutbath' not in flags:
                $ flags['talkaboutbath'] = 0

            if flags['talkaboutbath'] > 0 and not poss['nightclub'].stages[5].used:
                $ flags['talkaboutbath'] = 0
                $ poss['nightclub'].stages[7].used = False
                if poss['nightclub'].stages[4].used:
                    $ poss['nightclub'].stn = 4
                elif poss['nightclub'].stages[3].used:
                    $ poss['nightclub'].stn = 3
                else:
                    $ poss['nightclub'].stn = 2

            if all([kol_choco == 0, items['choco'].have]):
                $ items['choco'].have = False

        if current_ver < "0.04.0.06":
            $ current_ver = "0.04.0.06"

            if all([kol_choco == 0, items['choco'].have]):
                $ items['choco'].have = False

            python:
                for mem in persistent.memories:
                    if persistent.memories[mem] == True:
                        persistent.memories[mem] = 1
                    elif persistent.memories[mem] == False:
                        persistent.memories[mem] = -1

            if 'kira' in chars:
                $ added_mem_var('kira')
            if items['max-a'].have:
                $ added_mem_var('max-a')
            if 'pajamas' in alice.gifts:
                $ added_mem_var('pajamas')
            if 'bathrobe' in lisa.gifts:
                $ added_mem_var('bathrobe')

            if renpy.seen_label('kira_bath.kira_mass_bath_first'):
                $ added_mem_var('kira_mass_bath_first')

            if flags['kira.tv.bj']:
                $ added_mem_var('kira.tv.bj')

            if talk_var['al.tvgood'] > 0 and 'alice_talk_tv' not in persistent.memories:
                $ persistent.memories['alice_talk_tv'] = 1
            elif renpy.seen_label('alice_talk_tv.choco') and 'alice_talk_tv' not in persistent.memories:
                $ persistent.memories['alice_talk_tv'] = 0

            if renpy.seen_label('kira_night_tv.second_lesson') and 'kira_night_tv.first_lesson' not in persistent.memories:
                $ persistent.memories['kira_night_tv.first_lesson'] = 1
            if renpy.seen_label('kira_night_tv.repeat_lesson') and 'kira_night_tv.second_lesson' not in persistent.memories:
                $ persistent.memories['kira_night_tv.first_lesson'] = 1
                $ persistent.memories['kira_night_tv.second_lesson'] = 1

            if 'massage_sunscreen.spider' not in persistent.memories:
                $ persistent.memories['massage_sunscreen.spider'] = 0

        if current_ver < "0.04.1.00":
            $ current_ver = "0.04.1.00"

            $ at_comp = False
            $ view_cam = Null

        if current_ver < "0.04.1.03":
            $ current_ver = "0.04.1.03"

            $ dcv.update({
                    'lisa_sweets' : Daily(done=True, enabled=True), # дарение сладости Лизе
                    'alice_sweets': Daily(done=True, enabled=True), # дарение сладости Алисе
                    'ann_sweets'  : Daily(done=True, enabled=True), # дарение сладости Анне
                })

            if 4 in sorry_gifts['alice'].give and sorry_gifts['alice'].owe:
                $ sorry_gifts['alice'].owe = False
                $ sorry_gifts['alice'].valid = {'ferrero-b', 'ferrero-m'}

        if current_ver < "0.04.1.04":
            $ current_ver = "0.04.1.04"

            if 'warning' not in flags:
                $ flags['warning'] = False

        if current_ver < "0.04.1.05":
            $ current_ver = "0.04.1.05"

            if 'cam_fun_alice' not in flags:
                $ flags['cam_fun_alice'] = False
            if not flags['cam2bath']:
                $ house[3].max_cam = 2
                if len(house[3].cams) > 1:
                    $ house[3].cams.pop(1)

        if current_ver < "0.04.1.06":
            $ current_ver = "0.04.1.06"

            $ cam_poses = {}

        if current_ver < config.version:
            $ current_ver = config.version
