

label Waiting: ##(delta, ratio=1, sleep=False, alarm=""):
    # обработчик ожидания, запускает события по времени
    $ renpy.block_rollback()

    $ __prevday = day
    $ __prevtime = tm

    if alarm_time != "":
        $ d2 = TimeDifference(__prevtime, alarm_time)
        if spent_time == 0 or d2 < spent_time:
            $ spent_time = d2

    $ Wait(spent_time)

    $ __name_label = ""

    # здесь располагаем ссылку на функцию поиска стартующих по времени событий
    $ cut_id = GetCutEvents(__prevtime, tm, status_sleep)
    # if cut_id == "" and not "00:00" <= __prevtime <= "06:00":
    #     $ cut_id = GetCutEvents(__prevtime, tm, False) # попробуем найти событие для неспящего
    #
    # if sleep and tm < "08:00" and cut_id == "":
    #     # проверим, нет ли событий стартующих во время ночного сна, но чуть позднее
    #     $ cut_id = GetCutEvents(__prevtime, "08:00", True)

    # и устанавливаем время на начало кат-события, если оно есть
    if cut_id != "":
        $ __name_label = EventsByTime[cut_id].label
        if __prevtime > tm:
            if __prevtime <= EventsByTime[cut_id].tm < "23:59":
                $ day = __prevday
        $ tm = EventsByTime[cut_id].tm

    if day != __prevday:
        # временный блок случайного назначения одежды
        $ dress_suf["alice"] = renpy.random.choice(["a", "b"])
        $ dress_suf["lisa"] = renpy.random.choice(["a", "b"])
        $ dress_suf["max"] = renpy.random.choice(["a", "b"])
        $ dress_suf["ann"] = renpy.random.choice(["a", "b"])
        $ dress_suf["lisa-learn"] = renpy.random.choice(["a", "b", "c"])
        if possibility["Swimsuit"].stage_number >= 0 :
            $ swim_suf["lisa"] = renpy.random.choice(["a", "b"])
        if day > 2:
            $ dress_suf["lisa-sleepwear"] = renpy.random.choice(["a", "b"])

        if dress_suf["lisa"] == "a":
            $ lisa_dress["casual"]  = "01a"
            $ lisa_dress["casual2"] = "01a"
        else:
            $ lisa_dress["casual"]  = "04"
            $ lisa_dress["casual2"] = "04"

        if dress_suf["lisa-sleepwear"] == "a":
            $ lisa_dress["sleepwear"] = "02"
        else:
            $ lisa_dress["sleepwear"] = "02a"

        if dress_suf["lisa-learn"] == "a":
            $ lisa_dress["learn"] = "01a"
        elif dress_suf["lisa-learn"] == "b":
            $ lisa_dress["learn"] = "04"
        else:
            $ lisa_dress["learn"] = "04b"

        if swim_suf["lisa"] == "a":
            $ lisa_dress["swim"] = "03"
        else:
            $ lisa_dress["swim"] = "03b"

        if dress_suf["alice"] == "a":
            $ alice_dress["casual"] = "01a"
            $ alice_dress["casual2"] = "01aa"
        else:
            $ alice_dress["casual"] = "01c"
            $ alice_dress["casual2"] = "01ca"

        # здесь будет блок обработки ежедневно обнуляемых значений
        $ talk_var["ask_money"] = 0
        $ talk_var["lisa_dw"] = 0 # разговор о помывке посуды
        $ talk_var["alice_dw"] = 0

        $ random2   = renpy.random.choice(["01", "02"])
        $ random3_1 = renpy.random.choice(["01", "02", "03"])
        $ random4_1 = renpy.random.choice(["01", "02", "03", "04"])
        $ random3_2 = renpy.random.choice(["01", "02", "03"])
        $ random4_2 = renpy.random.choice(["01", "02", "03", "04"])
        $ random3_3 = renpy.random.choice(["01", "02", "03"])
        $ random4_3 = renpy.random.choice(["01", "02", "03", "04"])
        $ random5   = renpy.random.choice(["01", "02", "03", "04", "05"])
        $ random6   = renpy.random.choice(["01", "02", "03", "04", "05", "06"])
        $ random_ab = renpy.random.choice(["a", "b"])
        $ random_suf = renpy.random.choice(["a", "b"])

        python:
            # уменьшение счетчика событий, зависимых от прошедших дней
            for i in dcv:  #
                if dcv[i].enabled:
                    dcv[i].lost -= 1
                    if dcv[i].lost == 0:
                        dcv[i].done = True
                        dcv[i].enabled = False
    if __prevtime[:2] != tm[:2]:
        # вернем на значения по-умолчанию после подглядываний
        $ lisa_dress["naked"] = "04a"
        $ lisa_dress["dressed"] = "00b"
        $ ann_dress["naked"] = "04b"
        $ ann_dress["dressed"] = "00b"
        $ alice_dress["naked"] = "04aa"
        $ alice_dress["dressed"] = "00b"
        if swim_suf["alice"] == "a":
            $ alice_dress["swim"] = "03"
        if swim_suf["ann"] == "a":
            $ ann_dress["swim"] = "03"
        if swim_suf["lisa"] == "a":
            $ lisa_dress["swim"] = "03"
        else:
            $ lisa_dress["swim"] = "03b"


        if tm < "10:00":
            if random_suf == "a":
                $ ann_dress["cooking"] = "05b"
            else:
                $ ann_dress["cooking"] = "01c"
        elif tm > "17:00":
            $ ann_dress["cooking"] = "01b"
            if dress_suf["alice"] == "a":
                $ alice_dress["cooking"] = "01b"
            else:
                $ alice_dress["cooking"] = "01d"

        if tm < "14:00":
            $ ann_dress["casual"] = "01b"
        else:
            $ ann_dress["casual"] = "03"

        if tm > "19:00":
            if random_ab == "a":
                $ ann_dress["casual2"] = "01b"
            else:
                $ ann_dress["casual2"] = "04b"


        python:
            # сбросим подглядывания
            for key in peeping:
                peeping[key] = 0

    $ delt = TimeDifference(__prevtime, tm) # вычислим действительно прошедшее время

    if status_sleep:
        # если это сон, тогда энергия восстанавливается

        if delt >= 360:
            $ max_profile.energy = 100 # за 6 часов сна Макс полностью восстанавливает свои силы
        elif delt >= 300:
            $ max_profile.energy += delt * 0.25 # (15% в час)
        elif delt >= 240:
            $ max_profile.energy += delt * 0.2 # (12% в час)
        else:
            $ max_profile.energy += delt * 1 / 6 # (10% в час)
        if max_profile.energy > 100:
            $ max_profile.energy = 100
    else: # в противном случае - расходуется
        $ max_profile.energy -= delt * 5 * cur_ratio / 60.0
        # if max_profile.energy < 5:
        #     jump Wearied

    # обновим extra-info для сохранений
    $ NewSaveName()

    if __name_label != "" and renpy.has_label(__name_label):
        # если есть кат-событие - запускаем его
        jump expression __name_label

    # иначе запускаем блок "после ожидания"
    jump AfterWaiting


label AfterWaiting:

    $ spent_time = 0
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
                $ __CurShedRec = GetScheduleRecord(schedule_alice, day, "10:00")
                if __CurShedRec is not None:
                    $ __name_label = __CurShedRec.label
            else:
                $ __CurShedRec = GetScheduleRecord(schedule_alice, day, "11:00")
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
        $ __CurShedRec = GetScheduleRecord(eval("schedule_"+current_room.cur_char[0]), day, tm)
        if __CurShedRec is not None:
            $ __name_label = __CurShedRec.label

    call SetAvailableActions from _call_SetAvailableActions

    if __name_label != "" and renpy.has_label(__name_label):
        # управляющий блок найден и существует
        call expression __name_label from _call_expression_1
    else:
        # устанавливаем фон комнаты без персонажей
        if current_room.cur_bg.find("_") >= 0:
            scene image(current_room.cur_bg.replace("_", ""))
        else:
            scene image(current_room.cur_bg)

    call screen room_navigation


label SetAvailableActions: # включает кнопки действий

    python:
        # Обнулим кнопки
        for key in AvailableActions:
            AvailableActions[key].active = False

    if current_room == house[0]:  # комната Макса и Лизы
        $ __CurShedRec = GetScheduleRecord(schedule_lisa, day, tm)

        if (__CurShedRec is not None and __CurShedRec.dress != "dressed"
            and "08:00" <= tm < "21:30"):
            $ AvailableActions["unbox"].active = True

        if "00:00" <= tm <= "04:00":
            $ AvailableActions["alarm"].active = True
            $ AvailableActions["sleep"].active = True
        if "11:00" <= tm <= "17:00":
            $ AvailableActions["nap"].active = True

        if max_profile.energy > 10:
            if __CurShedRec is not None and __CurShedRec.dress != "dressed":
                $ AvailableActions["notebook"].active = True

    if current_room == house[0] or (current_room == house[5] and len(current_room.cur_char) == 0):
        python:
            for key in items:
                if items[key].need_read > items[key].read and ItsTime():
                    AvailableActions["readbook"].active = True

    if (current_room.cam_installed < current_room.max_cam
        and items["hide_cam"].have
        and len(current_room.cur_char) == 0):
        $ AvailableActions["install"].active = True

    if current_room not in InspectedRooms and len(current_room.cur_char) == 0:
        $ AvailableActions["searchcam"].active = True

    if current_room == house[1] and len(current_room.cur_char) == 0:  # комната Алисы
        $ AvailableActions["usb"].active = True
        if items["spider"].have:
            $ AvailableActions["hidespider"].active = True

        $ AvailableActions["searchbook"].active = True
        $ AvailableActions["searchciga"].active = True

    if current_room == house[3]:  # ванная комната
        if "06:00" <= tm <= "18:00" and max_profile.cleanness < 80:
            $ AvailableActions["shower"].active = True
        if ("20:00" <= tm <= "23:59" or "00:00" <= tm <= "04:00") and max_profile.cleanness < 80:
            $ AvailableActions["bath"].active = False #True - временно
        if "08:00" <= tm <= "09:00" and day < 19:
            $ AvailableActions["throwspider3"].active = True

    if current_room == house[4]:  # гостиная
        $ __CurShedRec = GetScheduleRecord(schedule_ann, day, tm)
        if items["ann_movie"].have and __CurShedRec is not None and __CurShedRec.label == "ann_tv":
            $ AvailableActions["momovie"].active = True
        if not dishes_washed and len(current_room.cur_char) == 0:
            $ AvailableActions["dishes"].active = True

    if len(current_room.cur_char) > 0:  # в текущей локации кто-то есть, включаем диалог
        $ AvailableActions["talk"].active = True

    if len(current_room.cur_char) == 1:
        $ __CurShedRec = GetScheduleRecord(eval("schedule_"+current_room.cur_char[0]), day, tm)
        $ AvailableActions["talk"].enabled = (__CurShedRec.enabletalk and
                                              (len(GetTalksTheme()) > 0 or
                                               __CurShedRec.talklabel is not None)
                                             )


label after_load:
    # срабатывает каждый раз при загрузке сохранения или начале новой игры
    # проверяем на версию сохранения, при необходимости дописываем/исправляем переменные

    if current_ver == "v0.01.TechDemo":
        scene BG villa-door
        "Сохранения версии техно-демо не поддерживаются. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    elif current_ver != "v0.02.0.001":
        $ current_ver = "v0.02.0.001" # ставим номер версии
        # и выполняем необходимые действия с переменными или фиксы
        pass
