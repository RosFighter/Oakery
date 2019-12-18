init python:
    def AddTime(ts, delta=1):
        """Увеличивает время, заданное в формате 'hh:mm' на delta минут"""
        h, m = ts.split(":")
        ti = int(h)*60 + int(m) + delta ## переведем время в минуты и прибавим дельту
        h = ti // 60
        m = ti % 60
        return ("0"+str(h))[-2:]+":"+("0"+str(m))[-2:]


    def SortByTime(inputStr):
        """ключ для сортировки списка с расписанием - сремя начала действия"""
        return inputStr.ts


    def SortByDayTime(inputStr):
        return str(inputStr[0]) + "_" + inputStr[1]


    def AddSchedule(schedule, *added_sheds):
        """добавляет в список с расписанием персонажа новые действия
        блоки на один и тот же период с разным сдвигом в одном периоде или
        на разные значения в вычисляемом variable ВСЕГДА дожны добавляться одним болоком"""
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
                    Schedule(list_of_day, ed.ts, ed.te, ed.desc, ed.loc, ed.room, ed.label, ed.krat, ed.shift, ed.weekstart,
                             ed.variable, ed.dress))

        new_schedule = set(new_schedule)

        # теперь определим границы времени днях, затронутых изменениями
        # и если остается время частично незатронутое изменениями,
        # то его тоже добавляем в список...
        for ed in edited:
            for nsh in added_sheds:
                list_of_day = tuple(day for day in ed.lod if day in nsh.lod)
                if ed.ts < nsh.ts < ed.te and len(list_of_day):
                    new_schedule.append(
                        Schedule(list_of_day, ed.ts, AddTime(nsh.ts, -1), ed.desc, ed.loc, ed.room, ed.label, ed.krat,
                                 ed.shift, ed.weekstart, ed.variable, ed.dress))
                if ed.ts < nsh.te < ed.te and len(list_of_day):
                    new_schedule.append(
                        Schedule(list_of_day, AddTime(nsh.te), ed.te, ed.desc, ed.loc, ed.room, ed.label, ed.krat, ed.shift,
                                 ed.weekstart, ed.variable, ed.dress))

            # удалим старые строки из начального списка
            schedule.remove(ed)

        # добавим в список расписания список действий незатронутых изменениями
        schedule.extend(new_schedule)
        # добавим в список новые действия
        for nsh in added_sheds:
            schedule.append(nsh)

        schedule.sort(key=SortByTime)


    def GetScheduleRecordList(schedule, day, tm):
        """ Возвращает запись, с текущим действием персонажа
            Аргументы:
            schedule - список записей с расписанием,
            day      - день (целое),
            tm     - время в формате 'hh:mm',
            week     - номер недели (целое) """
        h, m = tm.split(":")  # нормализуем время на всякий случай
        tm = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:]
        day += 2  # в игре отсчет начинается со среды и дня под номером 1
        rez = []
        for sh in schedule:
            if ((sh.ts <= tm <= sh.te) and (day % 7 in sh.lod) and (day / 7 >= sh.weekstart) and
                (((day // 7) - sh.weekstart) % sh.krat == sh.shift) and (eval(sh.variable))):
                    rez.append(sh)

        return rez


    def GetScheduleRecord(schedule, day, tm):
        """ Возвращает запись, с текущим действием персонажа
            Аргументы:
            schedule - список записей с расписанием,
            day      - день (целое),
            tm     - время в формате 'hh:mm',
            week     - номер недели (целое) """
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


    def VerifySchedule(schedule):
        """ функция для разработчика, проверяет расписание на перехлесты"""
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


    def Distribution():
        """ функция назначает фон локациям согласно текущего времени
            и распределяет персонажей по локациям согласно расписанию """
        h, m = tm.split(":")

        for loc in locations:
            for room in locations[loc]:
                room.cur_char = []
                if "06:00" <= tm < "11:00":
                    room.cur_bg = "location "+str(loc)+" "+room.id+" morning-"+random_ab
                elif "11:00" <= tm < "18:00":
                    room.cur_bg = "location "+str(loc)+" "+room.id+" day-"+random_ab
                elif "18:00" <= tm < "21:00":
                    room.cur_bg = "location "+str(loc)+" "+room.id+" evening-"+random_ab
                else:
                    room.cur_bg = "location "+str(loc)+" "+room.id+" night-"+random_ab

        for char in characters:

            schedule_char = GetScheduleRecord(eval("schedule_"+char), day, tm)
            if schedule_char is not None:
                if schedule_char.loc != "" and not schedule_char.loc is None:
                    eval(schedule_char.loc+"["+str(schedule_char.room)+"].cur_char.append(\""+char+"\")")

                characters[char].sufix = schedule_char.dress


    def Wait(delta):
        """ функция реализует ожидание в минутах """
        global day, tm
        h, m = tm.split(":")
        ti = int(h)*60 + int(m) + delta
        h = ti // 60
        m = ti % 60

        if h > 23:
            day += h // 24
            h = h % 24

        tm = ("0"+str(h))[-2:] + ":" + ("0"+str(m))[-2:]


    def TimeDifference(time1, time2):
        """ функция вычисляет разницу в минутах между time2 и time1
            если time1 больше, считается, что оно принадлежит предыдущему дню """
        h1, m1 = time1.split(":")
        h2, m2 = time2.split(":")
        t1 = int(h1)*60+int(m1)
        t2 = int(h2)*60+int(m2)

        if t1 > t2:
            return 24*60-t1 + t2

        return t2 - t1


    def CooldownTime(time2):
        """ возвращает время, когда откатится кулдаун в формате "день час:мин" """
        h1, m1 = tm.split(":")
        h2, m2 = time2.split(":")
        ti = int(h1)*60+int(m1) + int(h2)*60+int(m2)
        h = ti // 60
        m = ti % 60
        d = day + h // 24

        return str(d)+" " + ("0"+str(h))[-2:] + ":" + ("0"+str(m))[-2:]


    def ItsTime(next_learn):
        """ проверяет, прошел ли кулдаун """
        d1, hm = next_learn.split(" ")
        h1, m1 = hm.split(":")
        h2, m2 = tm.split(":")

        return (day*24 + int(h2))*60 + int(m2) >= (int(d1)*24 + int(h1))*60 + int(m1)


    def ReadBookCheck():
        """ устанавливает активность кнопки чтения, если есть недочитанные книги"""
        for key in items:
            if items[key].need_read > items[key].read and ItsTime(cooldown["learn"]):
                AvailableActions["readbook"].active = True


    def GetCutEvents(tm1, tm2, sleep):
        """ находит самое раннее всплывающее событие в указанный промежуток времени и возвращает его ключ"""

        # получим список событий, "всплывающих" в указанный период
        eventslist = []
        timelist = []
        for cut in EventsByTime:
            if (EventsByTime[cut].enabled and
                ((tm1 < tm2 and tm1 < EventsByTime[cut].tm <= tm2) or
                 ((tm1 < tm2 and tm1 < EventsByTime[cut].tm <= "08:00") and EventsByTime[cut].extend and EventsByTime[cut].sleep) or
                 (tm1 > tm2 and (tm1 < EventsByTime[cut].tm <= "23:59" or "00:00" <= EventsByTime[cut].tm <= tm2)))
                and (day in EventsByTime[cut].lod) and eval(EventsByTime[cut].variable) and
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


    def GetTalksTheme():
        """ ищет все доступные темы для разговора с персонажем в текущей комнате
            если персонажей несколько, то диалог должен быть для всех
            возвращает ключи словаря с вариантами фраз"""
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


    def TalkMenuItems():
        """ возвращает список кортежей для создания меню """

        menu_items = []
        talklist = GetTalksTheme()

        for i in talklist:
            menu_items.append((talks[i].select, talks[i].label))

        return menu_items

    def GetChance(Skil, Divisor=1):
        """ Вычисляет и возвращает шанс успешного применения навыка """
        cap = 100.0 / Divisor

        return min(90.0, 100.0 * (Skil / cap))

    def RandomChance(chance):
        """ прошло илинет применение навыка с указанным шансом """
        return renpy.random.random() < chance / 100.0

    def NewSaveName():
        global save_name
        save_name = ("" + "$@" + str(weekdays[(day+2) % 7][0]) +
                    "$@" + str(tm) + "$@" + str(day) +
                    "$@" + str(number_quicksave) +
                    "$@" + str(number_autosave))

    def NewNumberAutosave():
        global number_autosave
        number_autosave += 1

        NewSaveName()

    def HintRelMood(char, rel, mood):
        if rel >= 50:
            rel_suf = __("значительно улучшилось")
        elif rel >= 10:
            rel_suf = __("улучшилось")
        elif rel > 0:
            rel_suf = __("немного улучшилось")
        elif rel <= -50:
            rel_suf = __("значительно ухудшилось")
        elif rel <= -10:
            rel_suf = __("ухудшилось")
        elif rel < 0:
            rel_suf = __("немного ухудшилось")

        if mood > 0:
            mood_suf = __("повысилось")
        elif mood < 0:
            mood_suf = __("снизилось")

        if _preferences.language is None:
            char_name = characters[char].name_1
        else:
            char_name = char.capitalize()

        if rel != 0 and mood != 0:
            renpy.notify(__("Настроение %s %s \nЕе отношение к Максу %s") % (char_name, mood_suf, rel_suf))
        elif rel != 0:
            renpy.notify(__("Отношение %s к Максу %s") % (char_name, rel_suf))
        elif mood != 0:
            renpy.notify(__("Настроение %s %s") % (char_name, mood_suf))
