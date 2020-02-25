

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
        call NewDay

    # если прошло какое-то время, проверим необходимость смены одежды
    $ ChoiceClothes()

    if prevtime[:2] != tm[:2]:
        # почасовой сброс
        $ flags["little_energy"] = False
        $ peeping["alice_sleep"] = False
        $ peeping["ann_sleep"] = False
        # позы обновляются каждый час
        $ pose3_1 = renpy.random.choice(["01", "02", "03"])
        $ pose3_2 = renpy.random.choice(["01", "02", "03"])
        $ pose3_3 = renpy.random.choice(["01", "02", "03"])
        $ pose2_1 = renpy.random.choice(["01", "02"])
        $ pose2_2 = renpy.random.choice(["01", "02"])
        $ pose2_3 = renpy.random.choice(["01", "02"])
        $ tv_scene = renpy.random.choice(["", "bj", "hj"])

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

    $ random_loc_ab = renpy.random.choice(["a", "b"])

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

    $ GetDeliveryList()

    if 0 < GetWeekday(prevday) < 6:
        if possibility['sg'].stn > 0 and not flags["lisa_hw"]:  # был разговор с Лизой по поводу наказаний и не помогали
            $ punlisa.insert(0, [  # вставляем в начало
                0,  # помощь Макса с д/з (0, 1, 2, 3, 4) (не помогал / допустил ошибку / неудачно попросил услугу / помог безвозмездно / помог за услугу)
                0,  # получена двойка в школе (0, 1)
                0,  # Макс заступился за Лизу перед наказанием (0, 1, 2)
                0,  # Лиза понесла наказание (0, 1)
                0,  # подозрительность
                ])
            $ del punlisa[10:]
        if possibility['smoke'].stn > 0:  # Макс видел курящую Алису
            $ punalice.insert(0, [  # вставляем в начало
                0,  # Макс шантажировал Алису
                0,  # Макс подставлял Алису
                0,  # Макс заступился за Алису перед наказанием
                0,  # Ализа понесла наказание
                0,  # подозрительность
                ])
            $ del punalice[10:]
    $ flags["lisa_hw"] = False
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
    elif current_ver < "v0.03.0.000":
        $ current_ver = "v0.02.0.000" # ставим номер версии
        # и выполняем необходимые действия с переменными или фиксы
        pass

    if 'online_cources' not in globals():
        call InitCources
