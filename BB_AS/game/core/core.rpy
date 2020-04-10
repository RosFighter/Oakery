

label Waiting:
    # обработчик ожидания, запускает события по времени
    $ renpy.block_rollback()

    $ prevday = day
    $ prevtime = tm

    if alarm_time != "":
        $ d2 = TimeDifference(prevtime, alarm_time)
        if spent_time == 0 or d2 < spent_time:
            $ spent_time = d2

    $ Wait(spent_time)

    # ищем стартующее по времени событие
    $ cut_id = GetCutEvents(prevtime, tm, status_sleep)

    # и устанавливаем время на начало кат-события, если оно есть
    if cut_id != "":
        $ __name_label = EventsByTime[cut_id].label
        if prevtime > tm:
            if prevtime <= EventsByTime[cut_id].tm < "23:59":
                $ day = prevday
        $ tm = EventsByTime[cut_id].tm
    else:
        $ __name_label = ""

    $ spent_time = TimeDifference(prevtime, tm) ## реально прошедшее время (до будильника или кат-события)

    if day != prevday:
        # здесь будет блок обработки ежедневно обнуляемых значений
        call NewDay from _call_NewDay

    # если прошло какое-то время, проверим необходимость смены одежды
    $ ChoiceClothes()

    if prevtime[:2] != tm[:2]:
        # почасовой сброс
        $ flags["little_energy"] = False
        $ peeping["alice_sleep"] = 0
        $ peeping["ann_sleep"] = 0
        $ peeping["ann_dressed"] = 0
        $ peeping["lisa_dressed"] = 0
        $ peeping["alice_dressed"] = 0
        # позы обновляются каждый час
        $ pose3_1 = renpy.random.choice(["01", "02", "03"])
        $ pose3_2 = renpy.random.choice(["01", "02", "03"])
        $ pose3_3 = renpy.random.choice(["01", "02", "03"])
        $ pose2_1 = renpy.random.choice(["01", "02"])
        $ pose2_2 = renpy.random.choice(["01", "02"])
        $ pose2_3 = renpy.random.choice(["01", "02"])
        # $ tv_scene = renpy.random.choice(["", "bj", "hj"])
        $ talk_var['alice_sun'] = 0 # прдложить Алисе нанести масло можно пробовать каждый час (пока не нанес)
    if prevtime < "12:00" <= tm:
        call Noon

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

    # обновим extra-info для сохранений
    $ NewSaveName()

    if __name_label != "" and renpy.has_label(__name_label):
        # если есть кат-событие - запускаем его
        $ spent_time = 0
        $ prevday = day
        $ prevtime = tm
        $ CamShow()
        $ cur_ratio = 1
        $ status_sleep = False
        $ alarm_time = ""
        jump expression __name_label

    # иначе запускаем блок "после ожидания"
    jump AfterWaiting


label NewDay:
    $ talk_var["ask_money"] = 0
    $ talk_var["lisa_dw"]   = 0 # разговор о помывке посуды
    $ talk_var["alice_dw"]  = 0
    $ talk_var["ann_tv"]    = 0
    $ talk_var["alice_tv"]  = 0
    if 'smoke' in talk_var:
        $ talk_var["smoke"] = 0
        if flags['smoke.request'] == 'money':
            $ flags['smoke'] = None
            $ flags['smoke.request'] = None
        elif flags['smoke.request'] is not None and (flags['smoke'] is None or flags['smoke'][:3] != 'not'):
            # Если требование Макса было и это не деньги
            $ __chance = GetDisobedience()  # шанс, что Алиса не будет соблюдать договоренность
            if RandomChance(__chance):
                $ flags['smoke'] = 'not_' + flags['smoke']
                $ flags['noted'] = False  # нарушение еще не замечено Максом
                if flags['smoke.request'] == 'nopants':
                    $ chars['alice'].nopants = False
                elif flags['smoke.request'] == 'sleep':
                    $ chars['alice'].sleeptoples = False
            else:
                $ flags['smoke'] = flags['smoke.request']
                if flags['smoke.request'] == 'nopants':
                    $ chars['alice'].nopants = True
                elif flags['smoke.request'] == 'sleep':
                    $ chars['alice'].sleeptoples = True

    $ random_loc_ab = renpy.random.choice(["a", "b"])
    $ random_sigloc = renpy.random.choice(["n", "t"])

    python:
        # уменьшение счетчика событий, зависимых от прошедших дней
        for i in dcv:  #
            if dcv[i].enabled and not dcv[i].done:
                dcv[i].lost -= 1
                if dcv[i].lost == 0:
                    dcv[i].done  = True

        # сбросим подглядывания
        for key in peeping:
            peeping[key] = 0

        if SpiderResp > 0:
            SpiderResp -= 1

        for char in sorry_gifts:
            if sorry_gifts[char].owe and sorry_gifts[char].left > 0:
                sorry_gifts[char].left -= 1

    $ GetDeliveryList()

    if 0 < GetWeekday(prevday) < 6:
        if possibility['sg'].stn > 0 and not flags["lisa_hw"]:  # был разговор с Лизой по поводу наказаний и не помогал
            $ punlisa.insert(0, [  # вставляем в начало
                0,  # помощь Макса с д/з (0, 1, 2, 3, 4) (не помогал / допустил ошибку / неудачно попросил услугу / помог безвозмездно / помог за услугу)
                0,  # получена двойка в школе (0, 1)
                0,  # Макс заступился за Лизу перед наказанием (0, 1, 2)
                0,  # Лиза понесла наказание (0, 1)
                0,  # подозрительность
                ])
            $ del punlisa[10:]
    if possibility['smoke'].stn > 1:  # Макс видел курящую Алису
        $ punalice.insert(0, [  # вставляем в начало
            0,  # Макс шантажировал Алису
            0,  # Макс подставлял Алису
            0,  # Макс заступился за Алису перед наказанием
            0,  # Ализа понесла наказание
            0,  # подозрительность
            ])
        $ del punalice[14:]
    $ flags["lisa_hw"] = False

    if credit.debt > 0:        # если кредит не погашен
        $ credit.left -= 1       # уменьшим счетчик дней
        if credit.left == 0:   # если счетчик дней кончился
            $ credit.charge()    # начислим штраф
    $ talk_var['sun_oiled'] = 0  # Алиce можно намазать кремом
    return


label Noon:
    $ __new_items = False
    if day > 12 and not ('nightie' in chars['ann'].gifts or items['nightie'].have or items['nightie'].InShop):
        $ items['nightie'].InShop = True
        $ __new_items = True
    if ('secretbook' in dcv and dcv['secretbook'].done
        and "erobook_"+str(dcv['secretbook'].stage) in items
        and not items["erobook_"+str(dcv['secretbook'].stage)].InShop): # прошел откат после дарения книги, можно купить следующую
        # dcv['secretbook'].stage += 1
        $ items["erobook_"+str(dcv['secretbook'].stage)].InShop = True
        $ __new_items = True

    if __new_items:
        $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    return


label AfterWaiting:

    ## расчет притока/оттока зрителей для каждой камеры и соответствующего начисления
    $ CamShow()

    $ MoodNeutralize()

    $ spent_time = 0
    $ prevday = day
    $ prevtime = tm
    $ cur_ratio = 1
    $ status_sleep = False
    $ alarm_time = ""

    $ persone_button1 = None
    $ persone_button2 = None
    $ persone_button3 = None

    $ Distribution() # распределяем персонажей по комнатам и устанавливаем фоны для текущей локации

    # отключение возможности помыть посуду, если ее вымыли Лиза или Алиса
    if not dishes_washed:
        if tm > "20:00":
            $ dishes_washed = True
        elif (day+2) % 7 != 6:
            $ __name_label = ""
            if (day+2) % 7 == 0:
                $ __CurShedRec = GetPlan(plan_alice, day, "10:00")
                if __CurShedRec is not None:
                    $ __name_label = __CurShedRec.label
            else:
                $ __CurShedRec = GetPlan(plan_alice, day, "11:00")
                if __CurShedRec is not None:
                    $ __name_label = __CurShedRec.label

            if __name_label == "alice_dishes":
                if ((day+2) % 7 == 0 and tm >= "11:00") or tm >= "12:00":
                    $ dishes_washed = True

    # обновим extra-info для сохранений
    $ NewSaveName()

    # поиск управляющего блока для персонажа, находящегося в текущей комнате
    $ __name_label = ""
    if len(current_room.cur_char) > 0:
        $ __CurShedRec = GetPlan(eval("plan_"+current_room.cur_char[0]), day, tm)
        if __CurShedRec is not None:
            $ __name_label = __CurShedRec.label

    $ SetAvailableActions()

    if __name_label != "" and renpy.has_label(__name_label):
        # управляющий блок найден и существует
        call expression __name_label from _call_expression_2
    else:
        # устанавливаем фон комнаты без персонажей
        if current_room.cur_bg.find("_") >= 0:
            scene image(current_room.cur_bg.replace("_", ""))
        else:
            scene image(current_room.cur_bg)

    if mgg.energy < 10 and not flags["little_energy"]:
        Max_00 "Я слишком устал. Надо бы вздремнуть..."
        $ flags["little_energy"] = True

    if mgg.energy < 5:
        jump LittleEnergy
    call screen room_navigation


label after_load:
    # срабатывает каждый раз при загрузке сохранения или начале новой игры
    # проверяем на версию сохранения, при необходимости дописываем/исправляем переменные

    if current_ver == "v0.01.TechDemo":
        scene BG villa-door
        "Сохранения версии техно-демо не поддерживаются. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    elif current_ver[:5] == "v0.02":
        scene BG villa-door
        "К сожалению сохранения этой версии не поддерживаются из-за большого количества внутренних изменений. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    else:
        if current_ver < "0.03.0.006":
            $ current_ver = "0.03.0.006"
            $ items['hide_cam'].price = 790
        if current_ver < "0.03.0.007":
            $ current_ver = "0.03.0.007"
            $ dcv['lisa.ad'] = Daily(done=True, enabled=True)
        # if current_ver < "0.03.1.000":
        #     $ current_ver = "0.03.1.000"
        #     $ possibility["sg"].stages.extend([
        #         PossStage("interface poss lessons ep01", _("Какое-то время я помогал Лизе с уроками, причем безвозмездно, а потом как-то меньше стал уделать ей внимание. И вот, после очередной двойки она обратилась ко мне за помощью. Я согласился, но с условием, что она будет спать только в футболке и трусах. И думаю, что мне удастся её ещё на что-нибудь раскрутить..."), _("Правда она немного на меня обиднелась, но это я переживу... Подарю ей что-нибудь и она оттает...")),
        #         PossStage("interface poss lessons ep01", _("Пообещав Лизе помогать ей с уроками по принципы \"ты мне - я тебе\", я через некоторое время совсем про нее забыл. И вот, после очередной двойки Лиза мне напомнила о моём обещании. Нужно постараться уделять ей внимание хотя бы раз в неделю...")),
        #         PossStage("interface poss lessons ep01", _("Под видом помощи я делал так, что Лизе ставили двойку... И теперь она меня на этом спалила... Сильно обиделась, но от моей помощи не отказалась..."), _("Правда теперь она доверяет мне меньше и подставить ее уже не получится...")),
        #         ])
        if current_ver < "0.03.1.001":
            $ current_ver = "0.03.1.001"
            $ del possibility["sg"].stages[4:]
            $ possibility["sg"].stages.extend([
                PossStage("interface poss lessons ep01", _("Хоть я и пообещал помогать Лизе с уроками, но делать этого я не стал. И без того было много дел. После очередной двойки и наказания от мамы, она подошла ко мне и упрашивала о помощи. Я согласился, но с условием, что она будет спать только в футболке и трусиках. И думаю, что мне удастся её ещё на что-нибудь раскрутить..."), _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает...")),
                PossStage("interface poss lessons ep01", _("Я помогал Лизе с уроками какое-то время, причём безвозмездно, но это стало довольно скучным делом и я перестал уделять ей внимание с этим. И вот, после очередной двойки и наказания от мамы, она обратилась ко мне за помощью. Я согласился, но с условием, что она будет спать только в футболке и трусиках. И думаю, что мне удастся её ещё на что-нибудь раскрутить..."), _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает...")),
                PossStage("interface poss lessons ep01", _("Пообещав помогать Лизе с уроками по принципу \"ты мне - я тебе\", я через некоторое время совсем про неё забыл. И вот, после очередной двойки и наказания от мамы, Лиза напомнила о том, что я ей обещал. Пожалуй, мне стоит уделять её урокам больше внимания...")),
                PossStage("interface poss lessons ep01", _("Под видом помощи с уроками Лизы, я намеренно делал ошибки так, чтобы ей ставили двойки и наказывали... В чём теперь она меня и подозревает. Не удивительно, что Лиза сильно обиделась на меня, но вместе с тем, от моей помощи не отказалась..."), _("Сомневаюсь, что теперь получится её подставить, уж слишком большое недоверие она ко мне испытывает.")),
                ])
        if current_ver < "0.03.1.002":
            $ current_ver = "0.03.1.002"
            $ items.update({
                "pajamas"   : Item(_("ЛЁГКАЯ ПИЖАМА"), _("Удобнейшие маечка и шортики. В них не жарко душными летними ночами, и так же уютно в течение всего года."), "pajamas", 0, 100, cells=2),
                "nightie"   : Item(_("НОЧНУШКА"), _("Полупрозрачные сорочка и трусики. Облегающий фасон подчёркивает все достоинства и изгибы фигуры, а лёгкое кружево придаст ещё больше сексуальности."), "nightie", 0, 100, cells=2),
                })
        if current_ver < "0.03.1.003":
            $ current_ver = "0.03.1.003"
            python:
                for char in chars:
                    chars[char].attention = day
            $ items['bathrobe'].InShop = False
            if 'bathrobe' in chars['lisa'].gifts:
                $ chars['lisa'].gifts.remove('bathrobe')
                $ chars['lisa'].relmax -= 100
                $ money += 100
                $ cloth_type["lisa"]["casual"] = 'a'
                if GetRelMax('lisa')[0] > 2 and GetMood('lisa')[0] > 2:
                    $ cloth_type["lisa"]["learn"]  = 'c'
                else:
                    $ cloth_type["lisa"]["learn"]  = 'a'
                $ plan = GetPlan(plan_lisa, day, tm)
                $ ClothingNps("lisa", plan.name)
                if 'lisa' in current_room.cur_char and not renpy.get_screen("say"):
                    if plan.label != '' and renpy.has_label(plan.label):
                        call expression plan.label
            elif items['bathrobe'].have:
                $ items['bathrobe'].have = False
                $ money += 100

        if current_ver < '0.03.1.005':
            $ current_ver = '0.03.1.005'
            $ talk_var.update({
                "ae.ladd"  : 0,
                "dinner"   : 0,
                "breakfast" : 0,
                })
            $ flags['cam2bath'] = False
            $ items['nightie'].cells = 2
            $ items['pajamas'].cells=2

        if current_ver < '0.03.1.006':
            $ current_ver = '0.03.1.006'
            $ items.update({
                "cosmatic1" : Item(_("Набор косметики"), _("Небольшой набор косметики для повседневного использования. Для женщин - только лучшее..."), "cosmatics1", 5, 100),
                "cosmatic2" : Item(_("Набор косметики"), _("Небольшой набор косметики для повседневного использования. Для женщин - только лучшее..."), "cosmatics2", 5, 100),
                "cosmatic3" : Item(_("Набор косметики"), _("Небольшой набор косметики для повседневного использования. Для женщин - только лучшее..."), "cosmatics3", 5, 100),
                "ritter-m": Item(_("Шоколад \"Ritter Sport\" mini (9 штук)"), _("Шоколадное наслаждение для каждого случая... Множество лакомых сортов с лучшими ингредиентами со всего мира."), "ritter-1", 2, 25),
                "ritter-b": Item(_("Шоколад \"Ritter Sport\" (4 штуки)"), _("Шоколадное наслаждение для каждого случая... Множество лакомых сортов с лучшими ингредиентами со всего мира."), "ritter-2", 2, 50),
                "raffaello-m": Item(_("Конфеты \"Raffaello\" (16 штук)"), _("Хрустящие кокосовые конфеты с цельным миндальным орехом. Вместо тысячи слов..."), "raffaello-1", 2, 30),
                "raffaello-b": Item(_("Конфеты \"Raffaello\" (24 штуки)"), _("Хрустящие кокосовые конфеты с цельным миндальным орехом. Вместо тысячи слов..."), "raffaello-2", 2, 45),
                "ferrero-m"  : Item(_("Конфеты \"Ferrero Rocher\" (16 штук)"), _("Сочетание цельного фундука и восхитительного сливочно-орехового крема в хрустящей вафельной оболочке подарит вам неповторимые вкусовые ощущения."), "ferrero-1", 2, 40),
                "ferrero-b"  : Item(_("Конфеты \"Ferrero Rocher\" (24 штуки)"), _("Сочетание цельного фундука и восхитительного сливочно-орехового крема в хрустящей вафельной оболочке подарит вам неповторимые вкусовые ощущения."), "ferrero-2", 2, 60),
                })
            $ flags['promise_kiss'] = False
        if current_ver < '0.03.1.007':
            $ current_ver = '0.03.1.007'
            $ flags['tv_peep'] = 0

        if current_ver < '0.03.1.009':
            $ current_ver = '0.03.1.009'
            $ talk_var['ann_movie'] = 0

        if current_ver < '0.03.1.010':
            $ current_ver = '0.03.1.010'
            $ talk_var.update({
                "alice_sun": 0,
                'sun_oiled': 0,
                })
            $ items.update({
                "solar"      : Item(_("КРЕМ ДЛЯ ЗАГАРА"), _("Легкий, хорошо впитывающийся препарат для ускорения загара обладает увлажняющими и защитными свойствами. Рекомендуется для применения на пляже и в солярии."), "solar", 5, 50),
                "max-a"      : Item(_("МУЖСКИЕ МАЙКА И ШОРТЫ"), _("Свободный и лёгкий летний комплект одежды на каждый день."), "max-a", 0, 100, cells=2),
                })
            $ kol_cream = 0

        if current_ver < '0.03.1.011':
            $ current_ver = '0.03.1.011'
            $ sorry_gifts = {
                'lisa'  : SorryGift(),
                'alice' : SorryGift(),
                }

        if current_ver < '0.03.1.012':
            $ current_ver = '0.03.1.012'
            $ items['ferrero-m'].name = _("Конфеты \"Ferrero Rocher\" (16 штук)")
            $ items['ferrero-b'].name = _("Конфеты \"Ferrero Rocher\" (24 штуки)")
            $ items['bathrobe'].price = 200
            $ items['pajamas'].price = 200
            $ items['nightie'].price = 200
            $ items['max-a'].price = 150
            $ flags['lisa_superhug'] = 0


        if current_ver < config.version:
            $ current_ver = config.version
