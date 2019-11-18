

label Waiting(delta, ratio=1, sleep=False, alarm=""):
    # обработчик ожидания, запускает события по времени
    $ renpy.block_rollback()

    $ __prevday = day
    $ __prevtime = tm

    if alarm != "":
        $ d2 = TimeDifference(__prevtime, alarm)
        if delta == 0 or d2 < delta:
            $ delta = d2

    $ Wait(delta)

    $ __name_label = ""

    # здесь располагаем ссылку на функцию поиска стартующих по времени событий
    $ cut_id = GetCutEvents(__prevtime, tm, sleep)
    if cut_id == "" and not "00:00" <= __prevtime <= "06:00":
        $ cut_id = GetCutEvents(__prevtime, tm, False) # попробуем найти событие для неспящего

    if sleep and tm < "08:00" and cut_id == "":
        # проверим, нет ли событий стартующих во время ночного сна, но чуть позднее
        $ cut_id = GetCutEvents(__prevtime, "08:00", True)

    # и устанавливаем время на начало кат-события, если оно есть
    if cut_id != "":
        $ __name_label = EventsByTime[cut_id].label
        if __prevtime > tm:
            if __prevtime <= EventsByTime[cut_id].tm < "23:59":
                $ day = __prevday
        $ tm = EventsByTime[cut_id].tm

    if day != __prevday:

        # здесь будет блок обработки ежедневно обнуляемых значений
        $ talk_var["ask_money"] = 0
        $ lisa_dress["naked"] = "04a"
        $ lisa_dress["dressed"] = "00b"

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

        python:
            # уменьшение счетчика событий, зависимых от прошедших дней
            for i in dcv:  #
                if dcv[i].enabled:
                    dcv[i].lost -= 1
                    if dcv[i].lost == 0:
                        dcv[i].done = True
                        dcv[i].enabled = False
            # сбросим подглядывания
            for key in peeping:
                peeping[key] = 0
    if __prevtime < "12:00" and tm >= "12:00":
        # вернем на значения по-умолчанию после утренних подглядываний
        $ lisa_dress["naked"] = "04a"
        $ lisa_dress["dressed"] = "00b"

    $ delt = TimeDifference(__prevtime, tm) # вычислим действительно прошедшее время

    if sleep:
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
        $ max_profile.energy -= delt * 5 * ratio / 60.0
        if max_profile.energy < 5:
            jump Wearied

    if __name_label != "" and renpy.has_label(__name_label):
        # если есть кат-событие - запускаем его
        call expression __name_label from _call_expression
        # иначе запускаем блок "после ожидания"

    jump AfterWaiting


label AfterWaiting:

    $ Distribution() # распределяем персонажей по комнатам и устанавливаем фоны для текущей локации

    # отключение возможности помыть посуду, если ее вымыли Лиза или Алиса
    if not dishes_washed:
        if tm > "20:00":
            $ dishes_washed = True
        elif (day+2) % 7 != 6:
            if (day+2) % 7 == 0:
                 $ __name_label = GetScheduleRecord(schedule_alice, day, "10:00")[0].label
            else:
                 $ __name_label = GetScheduleRecord(schedule_alice, day, "11:00")[0].label

            if __name_label == "alice_dishes":
                if ((day+2) % 7 == 0 and tm >= "11:00") or tm >= "12:00":
                    $ dishes_washed = True

    # поиск управляющего блока для персонажа, находящегося в текущей комнате
    $ __name_label = ""
    if len(current_room.cur_char) > 0:
        $ __name_label = GetScheduleRecord(eval("schedule_"+current_room.cur_char[0]), day, tm)[0].label
        $ AvailableActions["talk"].enabled = (len(GetTalksTheme()) > 0)

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
        if GetScheduleRecord(schedule_lisa, day, tm)[0].dress != "dressed":
            $ AvailableActions["unbox"].active = True

        if "00:00" <= tm <= "04:00":
            $ AvailableActions["alarm"].active = True
            $ AvailableActions["sleep"].active = True
        if "11:00" <= tm <= "17:00":
            $ AvailableActions["nap"].active = True

        if max_profile.energy > 10:
            if GetScheduleRecord(schedule_lisa, day, tm)[0].dress != "dressed":
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
        if "06:00" <= tm <= "18:00":
            $ AvailableActions["shower"].active = True
        if "20:00" <= tm <= "23:59" or "00:00" <= tm <= "04:00":
            $ AvailableActions["bath"].active = True
        if "08:00" <= tm <= "09:00" and day < 19:
            $ AvailableActions["throwspider3"].active = True

    if current_room == house[4]:  # гостиная
        if items["ann_movie"].have and GetScheduleRecord(schedule_ann, day, tm)[0].label == "ann_tv":
            $ AvailableActions["momovie"].active = True
        if not dishes_washed and len(current_room.cur_char) == 0:
            $ AvailableActions["dishes"].active = True

    if len(current_room.cur_char) > 0:  # в текущей локации кто-то есть, включаем диалог
        $ AvailableActions["talk"].active = True


label after_load:
    # срабатывает каждый раз при загрузке сохранения или начале новой игры
    # проверяем на версию сохранения, при необходимости дописываем/исправляем переменные

    if current_ver < "0.01.0.020":
        $ current_ver = "0.01.0.020" # ставим номер версии
        # и выполняем необходимые действия с переменными или фиксы
        pass
