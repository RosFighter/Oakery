init python:

    # Увеличивает время, заданное в формате 'hh:mm' на delta минут
    def AddTime(ts, delta=1):
        h, m = ts.split(":")
        ti = int(h)*60 + int(m) + delta ## переведем время в минуты и прибавим дельту
        if ti > 0:
            h = ti // 60
            m = ti % 60
        else:
            ti = -1 * ti
            h = (1440 - (ti % 1140)) // 60
            m = (1440 - (ti % 1140)) % 60

        return ("0"+str(h))[-2:]+":"+("0"+str(m))[-2:]


    # ключ для сортировки списка с расписанием - время начала действия
    def SortByTime(inputStr):
        return inputStr.ts


    # ключ для сортировки списка с расписанием - дата и время начала действия
    def SortByDayTime(inputStr):
        return str(inputStr[0]) + "_" + inputStr[1]


    # добавляет в список с расписанием персонажа новые действия
    # блоки на один и тот же период с разным сдвигом в одном периоде или
    # на разные значения в вычисляемом variable ВСЕГДА дожны добавляться одним блоком
    def AddSchedule(schedule, *added_sheds):
        edited = []
        # составим список расписаний, затронутых изменениями (в последствии будут удалены)
        for nsh in added_sheds:
            for osh in schedule:
                if (osh.ts <= nsh.ts < osh.te) or (nsh.ts <= osh.ts < nsh.te):
                    for day in nsh.lod:
                        if day in osh.lod:
                            edited.append(osh)
                            break
        edited = set(edited)
        # теперь из этого списка отберем части, незатронутые изменениями
        # и внесем их в список для добавления.
        # сначала отберем дни, незатронутые изменениями
        new_schedule = []
        for ed in edited:
            list_of_day = list(ed.lod)  # берем все дни
            for nsh in added_sheds:
                if (ed.ts <= nsh.ts < ed.te) or (nsh.ts <= ed.ts < nsh.te):
                    for day in nsh.lod:
                        if day in list_of_day:  # если день задействован хоть в одной новой записи - удаляем его
                            list_of_day.remove(day)

            # добавим в новый список добавляемых расписаний дни без изменений, если список дней не пустой
            if len(list_of_day):
                new_schedule.append(
                    Schedule(list_of_day, ed.ts, ed.te, ed.name, ed.desc, ed.loc, ed.room, ed.label, ed.krat, ed.shift, ed.weekstart,
                             ed.variable, ed.enabletalk, ed.talklabel, ed.glow))

        new_schedule = set(new_schedule)

        # теперь определим границы времени днях, затронутых изменениями
        # и если остается время частично незатронутое изменениями,
        # то его тоже добавляем в список...
        for ed in edited:
            for nsh in added_sheds:
                list_of_day = tuple(day for day in ed.lod if day in nsh.lod)
                if ed.ts < nsh.ts < ed.te and len(list_of_day):
                    new_schedule.append(
                        Schedule(list_of_day, ed.ts, AddTime(nsh.ts, -1), ed.name, ed.desc, ed.loc, ed.room, ed.label, ed.krat,
                                 ed.shift, ed.weekstart, ed.variable, ed.enabletalk, ed.talklabel, ed.glow))
                if ed.ts < nsh.te < ed.te and len(list_of_day):
                    new_schedule.append(
                        Schedule(list_of_day, AddTime(nsh.te), ed.te, ed.name, ed.desc, ed.loc, ed.room, ed.label, ed.krat, ed.shift,
                                 ed.weekstart, ed.variable, ed.enabletalk, ed.talklabel, ed.glow))

            # удалим старые строки из начального списка
            schedule.remove(ed)

        # добавим в список расписания список действий незатронутых изменениями
        schedule.extend(new_schedule)
        # добавим в список новые действия
        for nsh in added_sheds:
            schedule.append(nsh)

        schedule.sort(key=SortByTime)


    # Возвращает список записей с текущим действием персонажа
    # Аргументы:
    # schedule - список записей с расписанием,
    # day      - день (целое),
    # tm     - время в формате 'hh:mm',
    # week     - номер недели (целое)
    def GetScheduleRecordList(schedule, day, tm): # только для тестирования расписания
        h, m = tm.split(":")  # нормализуем время на всякий случай
        tm = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:]
        day += 2  # в игре отсчет начинается со среды и дня под номером 1
        rez = []
        for sh in schedule:
            if ((sh.ts <= tm <= sh.te) and (day % 7 in sh.lod) and (day / 7 >= sh.weekstart) and
                (((day // 7) - sh.weekstart) % sh.krat == sh.shift) and (eval(sh.variable))):
                    rez.append(sh)

        return rez


    # Возвращает запись с текущим действием персонажа
    #     Аргументы:
    #     schedule - список записей с расписанием,
    #     day      - день (целое),
    #     tm     - время в формате 'hh:mm',
    #     week     - номер недели (целое)
    def GetScheduleRecord(schedule, day, tm):
        h, m = tm.split(":")  # нормализуем время на всякий случай
        tm = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:]
        day += 2  # в игре отсчет начинается со среды и дня под номером 1
        rez = []
        for sh in schedule:
            if ((sh.ts <= tm <= sh.te) and (day % 7 in sh.lod) and (day / 7 >= sh.weekstart) and
                (((day // 7) - sh.weekstart) % sh.krat == sh.shift) and (eval(sh.variable))):
                    rez.append(sh)

        if len(rez) > 1:
            print("ошибочка-с...", rez)
        elif len(rez) == 0:
            return None
        else:
            return rez[0]


    # функция для разработчика, проверяет расписание на перехлесты
    def VerifySchedule(schedule):
        max_krat = 1
        max_week = 0
        for sh in schedule:  # определяем неделю старта теста и максимальную длительность в неделях (кратность)
            max_krat = max(max_krat, sh.krat)
            max_week = max(max_week, sh.weekstart)

        errors = set()
        skipped = set()

        for day in range(max_week*7, (max_week + max_krat) * 7 * 2):  # удваиваем диаппазон на всякий случай
            start_skip = end_skip = ""
            for hour in range(24):
                for minute in range(60):
                    tm = "{0}:{1}".format(("0" + str(hour))[-2:], ("0" + str(minute))[-2:])
                    temp_list = GetScheduleRecordList(schedule, day, tm)

                    if len(temp_list) > 1:
                        for tl in temp_list:
                            errors.add(tl)
                    elif len(temp_list) == 0:
                        if start_skip == "":
                            start_skip = tm
                        elif end_skip == "" or AddTime(end_skip) == tm:
                            end_skip = tm
                    elif end_skip != "":
                        skipped.add(((day % 7,), start_skip, end_skip))
                        start_skip = end_skip = ""

        skip_list = []
        skipped = list(skipped)
        while len(skipped):
            start_skip = end_skip = ""
            lod = []
            for skip in skipped:
                if not start_skip:
                    start_skip = skip[1]
                    end_skip = skip[2]
                    lod.extend(skip[0])
                elif start_skip == skip[1] and end_skip == skip[2]:
                    lod.extend(skip[0])

            lod.sort()
            skip_list.append((lod[:], start_skip, end_skip))
            i = 0
            while i < len(skipped):
                if start_skip == skipped[i][1] and end_skip == skipped[i][2]:
                    skipped.pop(i)
                else:
                    i += 1

        if len(skip_list):
            print("Пропущено в расписании", skip_list)
        else:
            print("Пропусков не обнаружено")
        if len(errors):
            print(errors)
        else:
            print("Ошибок не обнаружено")


    # функция назначает фон локациям согласно текущего времени
    # и распределяет персонажей по локациям согласно расписанию """
    def Distribution():
        h, m = tm.split(":")

        for loc in locations:
            for room in locations[loc]:
                room.cur_char = []
                if "06:00" <= tm < "11:00":
                    room.cur_bg = "location "+str(loc)+" "+room.id+" morning-"+random_loc_ab
                elif "11:00" <= tm < "18:00":
                    room.cur_bg = "location "+str(loc)+" "+room.id+" day-"+random_loc_ab
                elif "18:00" <= tm < "21:00":
                    room.cur_bg = "location "+str(loc)+" "+room.id+" evening-"+random_loc_ab
                else:
                    room.cur_bg = "location "+str(loc)+" "+room.id+" night-"+random_loc_ab

        for char in characters:

            schedule_char = GetScheduleRecord(eval("schedule_"+char), day, tm)
            if schedule_char is not None:
                if schedule_char.loc != "" and not schedule_char.loc is None:
                    eval(schedule_char.loc+"["+str(schedule_char.room)+"].cur_char.append(\""+char+"\")")


    def Wait(delta): # функция реализует ожидание в минутах
        global day, tm
        h, m = tm.split(":")
        ti = int(h)*60 + int(m) + delta
        h = ti // 60
        m = ti % 60

        if h > 23:
            day += h // 24
            h = h % 24

        tm = ("0"+str(h))[-2:] + ":" + ("0"+str(m))[-2:]


    # функция вычисляет разницу в минутах между time2 и time1
    # если time1 больше, считается, что оно принадлежит предыдущему дню """
    def TimeDifference(time1, time2):
        h1, m1 = time1.split(":")
        h2, m2 = time2.split(":")
        t1 = int(h1)*60+int(m1)
        t2 = int(h2)*60+int(m2)

        if t1 > t2:
            return 24*60-t1 + t2

        return t2 - t1


    def CooldownTime(time2): # возвращает время, когда откатится кулдаун в формате "день час:мин"
        h1, m1 = tm.split(":")
        h2, m2 = time2.split(":")
        ti = int(h1)*60+int(m1) + int(h2)*60+int(m2)
        h = (ti % 1440) // 60
        m = ti % 60
        d = day + ti // 1440

        return str(d)+" " + ("0"+str(h))[-2:] + ":" + ("0"+str(m))[-2:]


    def ItsTime(tm_kd): # проверяет, прошел ли кулдаун """
        d1, hm = tm_kd.split(" ")
        h1, m1 = hm.split(":")
        h2, m2 = tm.split(":")

        return (day*24 + int(h2))*60 + int(m2) >= (int(d1)*24 + int(h1))*60 + int(m1)


    # устанавливает активность кнопки чтения, если есть недочитанные книги
    def ReadBookCheck():
        for key in items:
            if items[key].need_read > items[key].read and ItsTime(cooldown["learn"]):
                AvailableActions["readbook"].active = True


    # находит самое раннее всплывающее событие в указанный промежуток времени и возвращает его ключ
    def GetCutEvents(tm1, tm2, sleep):

        # получим список событий, "всплывающих" в указанный период
        eventslist = []
        timelist = []
        for cut in EventsByTime:
            if (EventsByTime[cut].enabled and
                ((tm1 < tm2 and tm1 < EventsByTime[cut].tm <= tm2) or
                 ((tm1 < tm2 and tm1 < EventsByTime[cut].tm <= "08:00") and EventsByTime[cut].extend and EventsByTime[cut].sleep) or
                 (tm1 > tm2 and (tm1 < EventsByTime[cut].tm <= "23:59" or "00:00" <= EventsByTime[cut].tm <= tm2)))
                and (((day+2) % 7) in EventsByTime[cut].lod) and eval(EventsByTime[cut].variable) and
                (sleep == EventsByTime[cut].sleep or (sleep and EventsByTime[cut].cut and not EventsByTime[cut].sleep))):
                    eventslist.append(cut)
                    timelist.append(EventsByTime[cut].tm)

        # получаем самое раннее время на случай если кат-событий несколько
        if len(eventslist) > 0:
            mintime = min(timelist)

        # удалим из списка ключи с другим временем
        i = 0
        while i <= len(eventslist)-1:
            if EventsByTime[eventslist[i]].tm == mintime:
                i += 1
            else:
                eventslist.pop(i)

        # если в это время стартует несколько событий - выбираем одно рандомно
        if len(eventslist) > 1:
            return eventslist[renpy.random.randint(0, len(eventslist)-1)]
        elif len(eventslist) == 1:
            return eventslist[0]
        else:
            return ""


    # ищет все доступные темы для разговора с персонажем в текущей комнате
    # если персонажей несколько, то диалог должен быть для всех
    # возвращает ключи словаря с вариантами фраз
    def GetTalksTheme():
        talkslist = []

        for i in talks:
            if len(current_room.cur_char) == 1:
                # один персонаж
                if talks[i].char == current_room.cur_char[0] and eval(talks[i].req):
                    talkslist.append(i)
            else:
                # несколько персонажей
                if sorted(current_room.cur_char) == sorted(talks[i].char) and eval(talks[i].req):
                    talkslist.append(i)

        return talkslist


    def TalkMenuItems(): # возвращает список кортежей для создания меню

        menu_items = []
        talklist = GetTalksTheme()

        for i in talklist:
            menu_items.append((talks[i].select, i))

        return menu_items


    def GetChance(Skil, multiplier=1, limit=1000): # Вычисляет и возвращает шанс успешного применения навыка
        return clip(Skil * 10 * multiplier, 0, limit)


    def RandomChance(chance): # прошло или нет применение навыка с указанным шансом
        return renpy.random.randint(0, 1000) < chance


    def NewSaveName(): # дополнение имени сохранения
        global save_name
        save_name = ("" + "$@" + str(weekdays[(day+2) % 7][0]) +
                    "$@" + str(tm) + "$@" + str(day) +
                    "$@" + str(number_quicksave) +
                    "$@" + str(number_autosave))


    def NewNumberAutosave(): # новый номер автосохранения
        global number_autosave
        number_autosave += 1

        NewSaveName()


    def ChangeRel(rel): # возвращает текстовое описание изменения отношений
        return {
                  rel <= -50 : __("значительно ухудшилось"),
            -50 < rel <= -10 : __("ухудшилось"),
            -10 < rel <= 0   : __("немного ухудшилось"),
            0   < rel <= 10  : __("немного улучшилось"),
            10  < rel <= 50  : __("улучшилось"),
            50  < rel        : __("значительно улучшилось")
            }[True]


    def ChangeMood(mood): # возвращает текстовое описание изменения отношений
        return{
            mood <  0 : __("снизилось"),
            mood >= 0 : __("повысилось")
            }[True]


    def AddRelMood(char, rel, mood): # добавить изменение настроения и отношений и показать подсказку
        rel_suf = ChangeRel(rel)
        mood_suf = ChangeMood(mood)

        if _preferences.language is None:
            char_name = characters[char].name_1
        else:
            char_name = char.capitalize()

        characters[char].relmax = clip(characters[char].relmax + rel, -450, 1400)
        characters[char].mood   = clip(characters[char].mood + mood,  -435, 435)
        if rel != 0 and mood != 0:
            renpy.notify(__("Настроение %s %s \nЕе отношение к Максу %s") % (char_name, mood_suf, rel_suf))
        elif rel != 0:
            renpy.notify(__("Отношение %s к Максу %s") % (char_name, rel_suf))
        elif mood != 0:
            renpy.notify(__("Настроение %s %s") % (char_name, mood_suf))


    def BuyItem(id): # выполняет покупку предмета из интернет-магазина
        global money, items
        money -= items[id].price
        items[id].buy = True
        if (day+2) % 7 != 6:
            items[id].delivery = 1
        else:
            items[id].delivery = 2


    def GetDeliveryList(): # формирует список доставляемых товаров
        global delivery_list, items
        for i in items:
            if items[i].buy and items[i].delivery > 0:
                items[i].delivery -= 1
                if items[i].delivery == 0:
                    delivery_list.append(i)


    def GetDeliveryString(): # формирует строку cо списком доставленных товаров
        StrDev = "Так... В накладной написано следующее:"
        n = 0
        for i in delivery_list:
            items[i].buy = False
            items[i].have = True
            n += 1
            globals()["TmpName"+str(n)] = items[i].name
            StrDev += "\n \"[TmpName" + str(n) +"!t]\""
        return StrDev


    def DeletingDeliveryTempVar(): # удаляет временные переменные строки списа доставленных товаров
        n = 1
        for i in delivery_list:
            del globals()["TmpName"+str(n)]
            n += 1
        delivery_list.clear()


    def BuyPromotion(): #Покупка пакета рекламы
        global money
        money -= 50

        ef = 10 + renpy.random.randint(-100, 100)/100.0 # процент эффективности рекламы
        k = 0
        for loc in locations:
            for room in locations[loc]:
                for cam in room.cams:
                    if cam.grow < 100:
                        cam.grow = 100
                    if cam.HD:
                        ef += 10.0 / (1 + k) # каждая HD-камера немного повышает эффективность рекламы

        site.invited += int(round(10000 * ef / 100.0, 0))
        renpy.notify(_("Приобретен пакет рекламы"))


    def CamShow(): # расчет притока/оттока зрителей для каждой камеры и соответствующего начисления
        grow_list = []

        cameras = [] # список установленных камер
        earned = 0 # вся полученная с камер прибыль
        for loc in locations:
            for room in locations[loc]:
                for cam in room.cams:
                    cameras.append(cam)
                    earned += cam.total

        if len(cameras) == 0:
            return

        # коэффициент заработанного на сайте
        if earned > 10000:
            k_earn = 400
        elif earned > 5000:
            k_earn = 450
        elif earned > 1000:
            k_earn = 500
        else:
            k_earn = 600
        # рандомизация коэффициента
        k_earn += renpy.random.randint(-25, 51)

        # коэффициент количества камер
        if len(cameras) > 5:
            k_cams = 16.0
        elif len(cameras) > 4:
            k_cams = 15.0
        elif len(cameras) > 2:
            k_cams = 14.0
        elif len(cameras) > 1:
            k_cams = 12.0
        else:
            k_cams = 10.0

        cam2 = [] # список камер с повышенным зрительским интересом

        cycles = spent_time / 10 # расчет выполняется каждые 10 минут

        for i in range(cycles):
            watchers = site.invited * renpy.random.randint(170, 250) / 60000.0 # количество привлеченных рекламмой зрителей
            watchers = round(watchers, 2)

            cam2.clear()
            # рассчитаем время события
            h, m = prevtime.split(":")
            ti = int(h)*60 + int(m) + 10*i
            h = (ti % 1440) // 60
            m = ti % 60
            cur_day = prevday + ti // 1440
            cur_tm = ("0"+str(h))[-2:] + ":" + ("0"+str(m))[-2:]

            for loc in locations:
                num_room = 0
                for room in locations[loc]:
                    for cam in room.cams:
                        # определим наличее персонажей в комнате
                        grow_list.clear()
                        for char in characters:
                            ## получим расписание персонажа на этот момент
                            cur_shed = GetScheduleRecord(eval("schedule_"+char), cur_day, cur_tm)
                            if cur_shed is not None and cur_shed.loc == loc and cur_shed.room == num_room:
                                # есть персонаж в комнате
                                grow_list.append(cur_shed.glow) # значит добавим в список коэф. зрительского интереса к фоновому событию

                        if len(grow_list) == 0:
                            if room == current_room:
                                k_grow = max(cam.grow, 95)
                            else:
                                if cam.grow - 0.9 < 10:
                                    k_grow = 10
                                elif cam.grow - 0.9 > 200:
                                    k_grow = 200
                                elif cam.grow > 100:
                                    k_grow = 100
                                else:
                                    k_grow = cam.grow - 0.9 # отток зрителей 0.9%
                        elif len(grow_list) == 1:
                            k_grow = max(cam.grow, 105, grow_list[0])
                        elif max(grow_list) > 0:
                            k_grow = max(cam.grow, max(grow_list))
                        else: # персонажей больше одного
                            k_grow = max(cam.grow, 115)

                        if k_grow > 115:
                            cam2.append(cam)

                        if cam.public > k_earn + 200:
                            k_grow = min(k_grow, 98.333)
                        elif cam.public > k_earn + 150:
                            k_grow = min(k_grow, 99.16)
                        elif cam.public > k_earn + 100:
                            k_grow = min(k_grow, 99.66)
                        elif cam.public > k_earn:
                            k_grow = min(k_grow, 106)
                        elif cam.public > k_earn - 100:
                            k_grow = min(k_grow, 112)
                        elif cam.public > k_earn - 200:
                            k_grow = min(k_grow, 124)

                        k_glow = (k_grow-100) / 100. # коэффициент прироста зрителей
                        pub = cam.public * k_glow # прирост/отток публики
                        cam.public += round(pub / 6.0, 2) # прирост зрителей от интереса событий
                        earn = (cam.public * k_grow) /45000.0 # расчет прибыли. Чем зрителям интересней, тем больше они донатят
                        earn = round(earn, 2)
                        cam.total += earn
                        if cur_tm == "04:00":
                            cam.today = 0
                        else:
                            cam.today += earn
                        site.account += earn
                        # print("время:{tm}, ads:{site.invited}(watchers:{watc}), k.cam:{cam.grow}, k.ev:{grow}, pub:{cam.public}({pub})(({glow})), earn:{earn}, total:{cam.total}".format(site=site, cam=cam, tm=cur_tm, grow=k_grow, watc=watchers, earn=earn, pub=pub, glow=k_glow))
                        cam.grow = k_grow
                    num_room += 1

            if len(cam2) > 0:
                pub = watchers / len(cam2)
                for cam in cam2:
                    cam.public += pub
            else:
                pub = watchers / len(cameras)
                for cam in cameras:
                    cam.public += pub

            site.invited -= watchers
        # в конце расчета округлим полученные значения
        for loc in locations:
            for room in locations[loc]:
                for cam in room.cams:
                    cam.public = int(cam.public)


    def Withdraw(): # выплата с сайта
        global money
        money += int(site.account)
        site.account -= int(site.account)


    def SetAvailableActions(): # включает кнопки действий

        # Обнулим кнопки
        for key in AvailableActions:
            AvailableActions[key].active = False

        # активируем поиск камеры, если в комнате никого и комната не проверена
        if current_room not in InspectedRooms and len(current_room.cur_char) == 0:
            AvailableActions["searchcam"].active = True

        # актувируем установку камеры, если она есть в сумке, в локации никого и есть место для установки
        if (len(current_room.cams) < current_room.max_cam and items["hide_cam"].have
                                                          and len(current_room.cur_char) == 0):
            AvailableActions["install"].active = True

        # в текущей локации кто-то есть, активируем диалог
        if len(current_room.cur_char) > 0:
            AvailableActions["talk"].active = True

        # установка разрешения диалога
        if len(current_room.cur_char) == 1:
            CurShedRec = GetScheduleRecord(eval("schedule_"+current_room.cur_char[0]), day, tm)
            # если при данном занятии разрешен диалог и
            #   есть тема для разговора или приближение
            AvailableActions["talk"].enabled = (CurShedRec.enabletalk and
                                                  (len(GetTalksTheme()) > 0 or
                                                   CurShedRec.talklabel is not None)
                                                )

        # комната Макса и Лизы
        if current_room == house[0]:
            CurShedRec = GetScheduleRecord(schedule_lisa, day, tm)

            if (CurShedRec is not None and CurShedRec.name != "dressed" and "08:00" <= tm < "21:30"):
                AvailableActions["unbox"].active = True

            if "00:00" <= tm <= "04:00":
                AvailableActions["alarm"].active = True
                AvailableActions["sleep"].active = True
            if "11:00" <= tm <= "17:00":
                AvailableActions["nap"].active = True

            if max_profile.energy > 5:
                if CurShedRec is not None and CurShedRec.name != "dressed":
                    AvailableActions["notebook"].active = True

            if ("06:00" <= tm <= "21:30" and CurShedRec is not None
                                         and CurShedRec.name != "dressed"):
                for key in items:
                    if items[key].have and items[key].need_read > items[key].read and ItsTime(cooldown["learn"]):
                        AvailableActions["readbook"].active = True

        # комната Алисы
        if current_room == house[1] and len(current_room.cur_char) == 0:
            AvailableActions["usb"].active = True
            AvailableActions["searchbook"].active = True
            AvailableActions["searchciga"].active = True
            if items["spider"].have:
                AvailableActions["hidespider"].active = True

        # ванная комната
        if current_room == house[3]:
            CurShedRec = GetScheduleRecord(schedule_alice, day, tm)
            if CurShedRec.label == "alice_shower" and len(current_room.cur_char) == 1: # Алиса принимает душ одна
                AvailableActions["throwspider3"].active = True
            if "06:00" <= tm <= "18:00" and max_profile.cleanness < 80:
                AvailableActions["shower"].active = True
            if ("20:00" <= tm <= "23:59" or "00:00" <= tm <= "04:00") and max_profile.cleanness < 80:
                AvailableActions["bath"].active = False #True - временно

        # гостиная
        if current_room == house[4]:
            CurShedRec = GetScheduleRecord(schedule_ann, day, tm)
            if items["ann_movie"].have and CurShedRec is not None and CurShedRec.label == "ann_tv":
                AvailableActions["momovie"].active = True
            if not dishes_washed and len(current_room.cur_char) == 0:
                AvailableActions["dishes"].active = True

        # двор
        if current_room == house[6]:
            AvailableActions["clearpool"].enabled = ("08:00" <= tm <= "16:00") and (len(current_room.cur_char) == 0)
            AvailableActions["clearpool"].active = (dcv["clearpool"].stage == 1)


    def ChoiceClothes(): # Проверяет необходимоть смены текущей одежды
        for char in characters:
            prev_shed = GetScheduleRecord(eval("schedule_"+char), prevday, prevtime)
            cur_shed  = GetScheduleRecord(eval("schedule_"+char), day, tm)
            if prev_shed.name != cur_shed.name: # начато новое действие, значит меняем одежду
                # ПРОВЕРИМ НЕОБХОДИМОСТЬ ОбНОВЛЕНИЯ РАНДОМНОЙ ОДЕЖДЫ (временный блок)
                if prevtime < "04:00" <= tm:
                    cloth_type["ann"]["cooking"]  = renpy.random.choice(["a", "b"])
                    cloth_type["alice"]["casual"] = renpy.random.choice(["a", "b"])
                    cloth_type["lisa"]["swim"]    = renpy.random.choice(["a", "b"])
                    cloth_type["lisa"]["casual"]  = renpy.random.choice(["a", "b"])
                    cloth_type["lisa"]["learn"]   = renpy.random.choice(["a", "b", "c"])
                    max_profile.dress = renpy.random.choice(["a", "b"])

                elif prevtime < "16:00" <= tm and day > 1:
                    cloth_type["ann"]["cooking"] = "b"
                    cloth_type["lisa"]["casual"] = renpy.random.choice(["a", "b"])

                elif prevtime < "22:00" <= tm and day > 1:
                    cloth_type["ann"]["rest"]   = renpy.random.choice(["a", "b"])
                    cloth_type["lisa"]["sleep"] = renpy.random.choice(["a", "b"])
                # после "смены одежды" прописываем одежды по расписанию
                ClothingNps(char, cur_shed.name)


    def ClothingNps(char, name): # устанавливает текущую одежду согласно расписанию (в том числе для инфо)
        if name == "dressed":
            characters[char].dress_inf = "00b"
        elif char == "lisa":
            if name == "sleep":
                characters["lisa"].dress = cloth_type["lisa"]["sleep"]
                if cloth_type["lisa"]["sleep"] == "a":
                    characters["lisa"].dress_inf = "02"
                else:
                    characters["lisa"].dress_inf = "02a"

            elif name == "shower" or name == "bath":
                characters["lisa"].dress_inf = "04a"

            elif (name == "breakfast" or name == "dishes" or name == "read"
                                      or name == "phone"  or name == "dinner" ):
                characters["lisa"].dress = cloth_type["lisa"]["casual"]
                if cloth_type["lisa"]["casual"] == "a":
                    characters["lisa"].dress_inf = "01a"
                else:
                    characters["lisa"].dress_inf = "04"

            elif name == "in_shcool":
                characters["lisa"].dress_inf = "01b"

            elif name == "sun":
                characters["lisa"].dress = cloth_type["lisa"]["swim"]
                if cloth_type["lisa"]["swim"] == "a":
                    characters["lisa"].dress_inf = "03"
                else:
                    characters["lisa"].dress_inf = "03b"

            elif name == "swim":
                characters["lisa"].dress = cloth_type["lisa"]["swim"]
                if pose3_1 == "03":
                    if cloth_type["lisa"]["swim"] == "a":
                        characters["lisa"].dress_inf = "03a"
                    else:
                        characters["lisa"].dress_inf = "03c"
                else:
                    if cloth_type["lisa"]["swim"] == "a":
                        characters["lisa"].dress_inf = "03"
                    else:
                        characters["lisa"].dress_inf = "03b"

            elif name == "homework":
                characters["lisa"].dress = cloth_type["lisa"]["learn"]
                if cloth_type["lisa"]["learn"] == "a":
                    characters["lisa"].dress_inf = "01a"
                elif cloth_type["lisa"]["learn"] == "b":
                    characters["lisa"].dress_inf = "04"
                else:
                    characters["lisa"].dress_inf = "04b"

            elif name == "in_shop" or name == "at_tutor":
                characters["lisa"].dress_inf = "01"

            else:
                characters["lisa"].dress = "a"
                characters["lisa"].dress_inf = "01a"

        elif char == "alice":
            if name == "sleep":
                characters["alice"].dress_inf = "02"
            elif name == "shower" or name == "bath":
                characters["alice"].dress_inf = "04aa"
            elif name == "breakfast" or name == "read" or name == "dinner":
                characters["alice"].dress = cloth_type["alice"]["casual"]
                if cloth_type["alice"]["casual"] == "a":
                    characters["alice"].dress_inf = "01a"
                else:
                    characters["alice"].dress_inf = "01c"
            elif name == "resting" or name == "blog" or name == "tv":
                characters["alice"].dress = cloth_type["alice"]["casual"]
                if cloth_type["alice"]["casual"] == "a":
                    if "09:00" <= tm < "20:00":
                        characters["alice"].dress_inf = "01a"
                    else:
                        characters["alice"].dress_inf = "01aa"
                else:
                    if "09:00" <= tm < "20:00":
                        characters["alice"].dress_inf = "01c"
                    else:
                        characters["alice"].dress_inf = "01ca"
            elif name == "sun":
                characters["alice"].dress = "a"
                characters["alice"].dress_inf = "03"
            elif name == "swim":
                characters["alice"].dress = "a"
                if pose3_2 == "03":
                    characters["alice"].dress_inf = "03a"
                else:
                    characters["alice"].dress_inf = "03"
            elif name == "in_shop" or name == "at_friends":
                characters["alice"].dress_inf = "01"
            elif name == "cooking":
                characters["alice"].dress = cloth_type["alice"]["casual"]
                if cloth_type["alice"]["casual"] == "a":
                    characters["alice"].dress_inf = "01b"
                else:
                    characters["alice"].dress_inf = "01d"
            else:
                characters["alice"].dress = "a"
                characters["alice"].dress_inf = "01a"

        elif char == "ann":
            if name == "sleep":
                characters["ann"].dress_inf = "02"
            elif name == "shower" or name == "bath":
                characters["ann"].dress_inf = "04a"
            elif name == "yoga":
                characters["ann"].dress_inf = "05"
            elif name == "cooking":
                characters["ann"].dress = cloth_type["ann"]["cooking"]
                if cloth_type["ann"]["cooking"] == "a":
                    characters["ann"].dress_inf = "05b"
                else:
                    characters["ann"].dress_inf = "01c"
            elif name == "breakfast":
                characters["ann"].dress = cloth_type["ann"]["cooking"]
                if cloth_type["ann"]["cooking"] == "a":
                    characters["ann"].dress_inf = "05a"
                else:
                    characters["ann"].dress_inf = "01b"
            elif name == "resting":
                if tm <= "12:00":
                    characters["ann"].dress = "a"
                    characters["ann"].dress_inf = "01b"
                elif tm <= "19:00":
                    characters["ann"].dress = "b"
                    characters["ann"].dress_inf = "03"
                else:
                    characters["ann"].dress = cloth_type["ann"]["rest"]
                    if cloth_type["ann"]["rest"] == "a":
                        characters["ann"].dress_inf = "01b"
                    else:
                        characters["ann"].dress_inf = "04b"
            elif name == "at_work":
                characters["ann"].dress_inf = "01a"
            elif name == "in_shop":
                characters["ann"].dress_inf = "01"
            elif name == "read":
                if tm < "14:00":
                    characters["ann"].dress = "a"
                    characters["ann"].dress_inf = "01b"
                else:
                    characters["ann"].dress = "b"
                    characters["ann"].dress_inf = "03"
            elif name == "sun":
                characters["ann"].dress_inf = "03"
            elif name == "swim":
                characters["ann"].dress_inf = "03a"
            elif name == "dinner":
                characters["ann"].dress = cloth_type["ann"]["casual"]
                if cloth_type["ann"]["casual"] == "a":
                    characters["ann"].dress_inf = "01d"
                else:
                    characters["ann"].dress_inf = "01b"
            elif name == "tv":
                characters["ann"].dress_inf = "04b"
            else:
                characters["ann"].dress = "a"
                characters["ann"].dress_inf = "01a"

        elif char == "eric":
            pass


    def SetCamsGrow(room, grow): # устанавливает коэффициент интереса к событию для камер в комнате
        for cam in room.cams:
            cam.grow = grow
            grow = int(grow * 0.9) # для каждой последующей камеры интерес снижается на 10%


    def clip(x, a, b): # вписывает число x в диапазон между a и b
        return a if x < a else(b if x > b else x)


    def GetMood(char): # возвращает кортеж с номером и описанием диапазона настроения персонажа
        mood = characters[char].mood
        return {
                   mood <= -285 : (-4, _("Ужасное")),
            -285 < mood <= -165 : (-3, _("Очень плохое")),
            -165 < mood <= -75  : (-2, _("Плохое")),
            -75  < mood <= -15  : (-1, _("Не очень")),
            -15  < mood <=  15  : (0, _("Нейтральное")),
             15  < mood <=  75  : (1, _("Неплохое")),
             75  < mood <=  165 : (2, _("Хорошее")),
            165  < mood <=  285 : (3, _("Очень хорошее")),
            285  < mood         : (4, _("Прекрасное")),
            }[True]


    def GetRelMax(char): # возвращает кортеж с номером и описанием диапазона отношений персонажа с Максом
        rel = characters[char].relmax
        return {
                   rel <= -250 : (-3, _("Война")),
            -250 < rel <= -100 : (-2, _("Враждебные")),
            -100 < rel <   0   : (-1, _("Плохие")),
            0    <= rel < 100  : ( 0, _("Прохладные")),
            100  <= rel < 250  : ( 1, _("Неплохие")),
            250  <= rel < 450  : ( 2, _("Хорошие")),
            450  <= rel < 700  : ( 3, _("Тёплые")),
            700  <= rel < 1000 : ( 4, _("Дружеские")),
            1000 <= rel        : ( 5, _("Близкие"))
            }[True]


    def GetRelEric(char): # возвращает кортеж с номером и описанием диапазона отношений персонажа с Эриком
        rel = characters[char].releric
        return {
            #        rel <= -250 : (-3, _("Война")),
            # -250 < rel <= -100 : (-2, _("Враждебные")),
            # -100 < rel <   0   : (-1, _("Плохие")),
            # 0    <= rel < 100  : ( 0, _("Прохладные")),
            # 100  <= rel < 250  : ( 1, _("Неплохие")),
            # 250  <= rel < 450  : ( 2, _("Хорошие")),
            # 450  <= rel < 700  : ( 3, _("Тёплые")),
            # 700  <= rel < 1000 : ( 4, _("Дружеские")),
            # 1000 <= rel        : ( 5, _("Близкие"))
            -3 : _("Война"),
            -2 : _("Враждебные"),
            -1 : _("Плохие"),
            0  : _("Прохладные"),
            1  : _("Неплохие"),
            2  : _("Хорошие"),
            3  : _("Тёплые"),
            4  : _("Дружеские"),
            5  : _("Близкие")
            }[True]


    def MoodNeutralize(): # с течением времени настроение стрепится к нейтральному
        cycles = spent_time / 10 # расчет выполняется каждые 10 минут
        for char in characters:
            for i in range(cycles):
                if characters[char].mood > 0:
                    characters[char].mood -= 1
                elif characters[char].mood < 0:
                    characters[char].mood += 3 # возвращается в норму настроение быстрее, чем падает


    def seat_Breakfast(): # рассаживает семью за завтраком
        renpy.scene()
        renpy.show("BG breakfast 00") # общий фон
        renpy.show("Ann breakfast 0"+renpy.random.choice(["1", "2", "3"])+characters["ann"].dress)
        renpy.show("Alice breakfast 0"+renpy.random.choice(["1", "2", "3"])+characters["alice"].dress)
        renpy.show("Lisa breakfast 0"+renpy.random.choice(["1", "2", "3"])+characters["lisa"].dress)
        renpy.show("FG breakfast 0"+renpy.random.choice(["1", "2", "3"])) # стол
        renpy.show("Max breakfast 0"+renpy.random.choice(["1", "2", "3"])+max_profile.dress)


    def seat_Dinner(): # рассаживает семью за ужином
        renpy.scene()
        renpy.show("BG dinner 00") # общий фон
        renpy.show("Ann dinner 0"+renpy.random.choice(["1", "2", "3"])+characters["ann"].dress)
        renpy.show("Alice dinner 0"+renpy.random.choice(["1", "2", "3"])+characters["alice"].dress)
        renpy.show("Lisa dinner 0"+renpy.random.choice(["1", "2", "3"])+characters["lisa"].dress)
        renpy.show("FG dinner 0"+renpy.random.choice(["1", "2", "3"])) # стол
        renpy.show("Max dinner 0"+renpy.random.choice(["1", "2", "3"])+max_profile.dress)
