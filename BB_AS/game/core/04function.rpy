init python:
    config.layers.insert(1, 'wm')

    def GetWeekday(day):  # возвращает номер дня недели
        return (day+2) % 7


    # Увеличивает время, заданное в формате 'hh:mm' на delta минут
    def add_time(ts, delta=1):
        h, m = ts.split(':')
        ti = int(h)*60 + int(m) + delta ## переведем время в минуты и прибавим дельту
        if ti > 0:
            h = ti // 60
            m = ti % 60
        else:
            ti = -1 * ti
            h = (1440 - (ti % 1140)) // 60
            m = (1440 - (ti % 1140)) % 60

        return ('0'+str(h))[-2:]+':'+('0'+str(m))[-2:]


    def Wait(delta): # функция реализует ожидание в минутах
        global day, tm
        h, m = tm.split(':')
        ti = int(h)*60 + int(m) + int(delta)
        h = ti // 60
        m = ti % 60

        if h > 23:
            day += h // 24
            h = h % 24

        tm = ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:]


    # функция вычисляет разницу в минутах между time2 и time1
    # если time1 больше, считается, что оно принадлежит предыдущему дню """
    def TimeDifference(time1, time2):
        h1, m1 = time1.split(':')
        h2, m2 = time2.split(':')
        t1 = int(h1)*60+int(m1)
        t2 = int(h2)*60+int(m2)

        if t1 > t2:
            return 24*60-t1 + t2

        return t2 - t1


    def CooldownTime(time2): # возвращает время, когда откатится кулдаун в формате "день час:мин"
        h1, m1 = tm.split(':')
        h2, m2 = time2.split(':')
        ti = int(h1)*60+int(m1) + int(h2)*60+int(m2)
        h = (ti % 1440) // 60
        m = ti % 60
        d = day + ti // 1440

        return str(d)+' ' + ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:]


    def ItsTime(tm_kd): # проверяет, прошел ли кулдаун """
        d1, hm = tm_kd.split(' ')
        h1, m1 = hm.split(':')
        h2, m2 = tm.split(':')

        return (day*24 + int(h2))*60 + int(m2) >= (int(d1)*24 + int(h1))*60 + int(m1)


    # функция назначает фон локациям согласно текущего времени
    # и распределяет персонажей по локациям согласно расписанию """
    def Distribution():
        h, m = tm.split(':')

        for loc in locations:
            for room in locations[loc]:
                room.cur_char = []
                if '06:00' <= tm < '11:00':
                    room.cur_bg = 'location '+str(loc)+' '+room.id+' morning-'+random_loc_ab
                elif '11:00' <= tm < '18:00':
                    room.cur_bg = 'location '+str(loc)+' '+room.id+' day-'+random_loc_ab
                elif '18:00' <= tm < '21:00':
                    room.cur_bg = 'location '+str(loc)+' '+room.id+' evening-'+random_loc_ab
                else:
                    room.cur_bg = 'location '+str(loc)+' '+room.id+' night-'+random_loc_ab

        for char in chars:

            # plan_char = GetPlan(eval('plan_'+char), day, tm)
            plan_char = chars[char].get_plan()
            if plan_char is not None:
                if plan_char.loc != '' and not plan_char.loc is None:
                    eval(plan_char.loc+"["+str(plan_char.room)+"].cur_char.append('"+char+"')")


    # устанавливает активность кнопки чтения, если есть недочитанные книги
    def ReadBookCheck():
        for key in items:
            if items[key].need_read > items[key].read and ItsTime(cooldown['learn']):
                AvailableActions['readbook'].active = True


    # находит самое раннее всплывающее событие в указанный промежуток времени и возвращает его ключ
    def GetCutEvents(tm1, tm2, sleep):

        # получим список событий, "всплывающих" в указанный период
        eventslist = []
        timelist = []
        for cut in EventsByTime:
            if (EventsByTime[cut].enabled and
                ((tm1 < tm2 and tm1 < EventsByTime[cut].tm <= tm2) or
                 ((tm1 < tm2 and tm1 < EventsByTime[cut].tm <= '08:00') and EventsByTime[cut].extend and EventsByTime[cut].sleep) or
                 (tm1 > tm2 and (tm1 < EventsByTime[cut].tm <= '23:59' or '00:00' <= EventsByTime[cut].tm <= tm2)))
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
            return ''


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

        if len(current_room.cur_char) == 1 and current_room.cur_char[0] in gifts:
            for gift in gifts[current_room.cur_char[0]]:
                if items[gift.item].have and eval(gift.req):
                    menu_items.append((gift.select, gift))

        return menu_items


    def GetChance(Skil, multiplier=1, limit=1000): # Вычисляет и возвращает шанс успешного применения навыка
        ch = clip(int(Skil * 10 * multiplier), 0, limit)
        return Chance(ch)


    def RandomChance(chance): # прошло или нет применение навыка с указанным шансом
        return renpy.random.randint(0, 1000) < chance


    def NewSaveName(): # дополнение имени сохранения
        global save_name
        save_name = ('' + '$@' + str(weekdays[GetWeekday(day)][0]) +
                    '$@' + str(tm) + '$@' + str(day) +
                    '$@' + str(number_quicksave) +
                    '$@' + str(number_autosave))


    def NewNumberAutosave(): # новый номер автосохранения
        global number_autosave
        number_autosave += 1

        NewSaveName()


    def ChangeRel(rel): # возвращает текстовое описание изменения отношений
        return {
                  rel <= -50 : __("{color=[red]}значительно ухудшилось{/color}"),
            -50 < rel <= -10 : __("{color=[red]}ухудшилось{/color}"),
            -10 < rel <= 0   : __("{color=[red]}немного ухудшилось{/color}"),
            0   < rel <= 10  : __("{color=[lime]}немного улучшилось{/color}"),
            10  < rel <= 50  : __("{color=[lime]}улучшилось{/color}"),
            50  < rel        : __("{color=[lime]}значительно улучшилось{/color}")
            }[True]


    def ChangeMood(mood): # возвращает текстовое описание изменения отношений
        return{
            mood <  0 : __("{color=[red]}снизилось{/color}"),
            mood >= 0 : __("{color=[lime]}повысилось{/color}")
            }[True]


    def AddRelMood(char, rel, mood): # добавить изменение настроения и отношений и показать подсказку
        rel_suf = ChangeRel(rel)
        mood_suf = ChangeMood(mood)

        if _preferences.language is None:
            char_name = chars[char].name_1
        else:
            char_name = char.capitalize()

        chars[char].relmax = clip(chars[char].relmax + rel, -450, 2000)
        chars[char].mood   = clip(chars[char].mood + mood,  -435, 435)
        if rel != 0 and mood != 0:
            notify_list.append(__("Настроение %s %s \nЕё отношение к Максу %s") % (char_name, mood_suf, rel_suf))
        elif rel != 0:
            notify_list.append(__("Отношение %s к Максу %s") % (char_name, rel_suf))
        elif mood != 0:
            notify_list.append(__("Настроение %s %s") % (char_name, mood_suf))


    def GetDeliveryList(): # формирует список доставляемых товаров
        global delivery_list, items
        for i in items:
            if items[i].bought and items[i].delivery > 0:
                items[i].delivery -= 1
                if items[i].delivery == 0:
                    if items[i].category in [0, 4, 5, 6]:
                        delivery_list[1].append(i)
                    else:
                        delivery_list[0].append(i)


    def GetDeliveryString(courier): # формирует строку cо списком доставленных товаров
        if _preferences.language is None:
            StrDev = "Так... В накладной написано следующее:"
        elif _preferences.language == "english":
            StrDev = "So... In the consignment note says the following:"

        n = 0
        for i in delivery_list[courier]:
            items[i].bought = False
            items[i].have = True
            n += 1
            globals()['TmpName'+str(n)] = items[i].name
            StrDev += "\n \"[TmpName" + str(n) +"!t]\""
        return StrDev


    def DeletingDeliveryTempVar(courier): # удаляет временные переменные строки списа доставленных товаров
        n = 1
        for i in delivery_list[courier]:
            del globals()['TmpName'+str(n)]
            n += 1
        delivery_list[courier].clear()


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
            watchers = mgg.invited * renpy.random.randint(170, 250) / 60000.0 # количество привлеченных рекламмой зрителей
            watchers = round(watchers, 2)

            cam2.clear()
            # рассчитаем время события
            h, m = prevtime.split(':')
            ti = int(h)*60 + int(m) + 10*i
            h = (ti % 1440) // 60
            m = ti % 60
            cur_day = prevday + ti // 1440
            cur_tm = ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:]

            for loc in locations:
                num_room = 0
                for room in locations[loc]:
                    r1 = renpy.random.randint(0, 1)
                    r2 = renpy.random.randint(600, 900)
                    for cam in room.cams:
                        # определим наличее персонажей в комнате
                        grow_list.clear()
                        for char in chars:
                            ## получим расписание персонажа на этот момент
                            # cur_shed = GetPlan(eval('plan_'+char), cur_day, cur_tm)
                            cur_shed = chars[char].get_plan(cur_day, cur_tm)
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
                        if len(room.cams) > 1 and room.cams.index(cam) == r1:
                            k_glow = k_glow * r2 / 1000. # если в локации две камеры, то для одной из них коэфициент прироста зрителей будет меньше

                        pub = cam.public * k_glow # прирост/отток публики
                        cam.public += round(pub / 6.0, 2) # прирост зрителей от интереса событий
                        earn = (cam.public * k_grow) /45000.0 # расчет прибыли. Чем зрителям интересней, тем больше они донатят
                        earn = round(earn, 2)
                        cam.total += earn
                        if cur_tm == '04:00':
                            cam.today += earn
                            if mgg.credit.fines and mgg.credit.debt > 0:  # если есть непогашенный кредит со штрафом
                                mgg.credit.part(min(int(cam.today/2), mgg.credit.debt))  # половина ежедневного дохода идет в счет погашения долга
                            cam.today = 0
                        else:
                            cam.today += earn
                        mgg.income(earn)
                        # print('время:{tm}, ads:{site.invited}(watchers:{watc}), k.cam:{cam.grow}, k.ev:{grow}, pub:{cam.public}({pub})(({glow})), earn:{earn}, total:{cam.total}'.format(site=site, cam=cam, tm=cur_tm, grow=k_grow, watc=watchers, earn=earn, pub=pub, glow=k_glow))
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

            mgg.invited -= watchers
        # в конце расчета округлим полученные значения
        for loc in locations:
            for room in locations[loc]:
                for cam in room.cams:
                    cam.public = int(cam.public)


    def SetAvailableActions(): # включает кнопки действий

        # Обнулим кнопки
        for key in AvailableActions:
            AvailableActions[key].active = False

        # активируем поиск камеры, если в комнате никого и комната не проверена
        if current_room not in InspectedRooms and len(current_room.cur_char) == 0:
            AvailableActions['searchcam'].active = True

        # актувируем установку камеры, если она есть в сумке, в локации никого и есть место для установки
        if (len(current_room.cams) < current_room.max_cam and items['hide_cam'].have
                                                          and len(current_room.cur_char) == 0):
            AvailableActions['install'].active = True
            AvailableActions['install'].enabled = True

        # в текущей локации кто-то есть, активируем диалог
        if len(current_room.cur_char) > 0:
            AvailableActions['talk'].active = True

        # установка разрешения диалога
        if len(current_room.cur_char) == 1:
            # cur_plan = GetPlan(eval('plan_'+current_room.cur_char[0]), day, tm)
            cur_plan = chars[current_room.cur_char[0]].get_plan()
            # если при данном занятии разрешен диалог и есть тема для разговора
            AvailableActions['talk'].enabled = (cur_plan.enabletalk and len(TalkMenuItems()) > 0)
        else:
            AvailableActions['talk'].enabled = False

        # комната Макса и Лизы
        if current_room == house[0]:
            # cur_plan = GetPlan(plan_lisa, day, tm)
            cur_plan = lisa.get_plan()

            if (cur_plan is not None and cur_plan.name != 'dressed' and '08:00' <= tm < '21:30'):
                AvailableActions['unbox'].active = True

            if '00:00' <= tm <= '04:00':
                AvailableActions['alarm'].active = True
                AvailableActions['sleep'].active = True
            if '11:00' <= tm <= '17:00':
                AvailableActions['nap'].active = True

            if mgg.energy > 5:
                if cur_plan is not None and cur_plan.name != 'dressed':
                    AvailableActions['notebook'].active = True

            if ('06:00' <= tm <= '21:30' and cur_plan is not None
                                         and cur_plan.name != 'dressed'):
                for key in items:
                    if items[key].have and items[key].need_read > items[key].read and ItsTime(cooldown['learn']):
                        AvailableActions['readbook'].active = True

        # комната Алисы
        if current_room == house[1] and len(current_room.cur_char) == 0:
            # cur_plan = GetPlan(plan_alice, day, tm)
            cur_plan = alice.get_plan()
            AvailableActions['usb'].active = True
            AvailableActions['searchbook'].active = (cur_plan.name != 'read' and '08:00' <= tm < '22:00')
            if items['spider'].have:
                AvailableActions['hidespider'].active = True
            AvailableActions['searchciga'].active = (cur_plan.name != 'smoke' and 'betray_smoke' in dcv and dcv['betray_smoke'].done and '08:00' <= tm < '19:00')

        # ванная комната
        if current_room == house[3]:
            # cur_plan = GetPlan(plan_alice, day, tm)
            cur_plan = alice.get_plan()
            if cur_plan.label == 'alice_shower' and len(current_room.cur_char) == 1: # Алиса принимает душ одна
                AvailableActions['throwspider3'].active = True

            if '06:00' <= tm <= '18:00' and mgg.cleanness < 80:
                AvailableActions['shower'].active = True
            if ('20:00' <= tm <= '23:59' or '00:00' <= tm <= '04:00') and mgg.cleanness < 80:
                AvailableActions['bath'].active = True #True - временно
            AvailableActions['shower'].enabled = len(current_room.cur_char) == 0
            AvailableActions['bath'].enabled = len(current_room.cur_char) == 0

        # гостиная
        if current_room == house[4]:
            # cur_plan = GetPlan(plan_ann, day, tm)
            cur_plan = alice.get_plan()
            if items['ann_movie'].have and cur_plan is not None and cur_plan.label == 'ann_tv':
                AvailableActions['momovie'].active = True
            if not dishes_washed and len(current_room.cur_char) == 0:
                AvailableActions['dishes'].active = True

        # двор
        if current_room == house[6]:
            AvailableActions['clearpool'].enabled = ('10:00' <= tm <= '16:00') and (len(current_room.cur_char) == 0)
            AvailableActions['clearpool'].active = (dcv['clearpool'].stage == 1)
            AvailableActions['catchspider'].active = ('10:00' <= tm < '12:00') and not items['spider'].have


    def ChoiceClothes(): # Проверяет необходимоть смены текущей одежды
        mgg.dress = clothes[mgg].casual.GetCur().suf

        if all([day>=11, GetWeekday(day)==6, talk_var['dinner']==6]):
            clothes[ann].casual.GetCur().suf = 'a'

        for char in chars:
            prev_shed = chars[char].get_plan(prevday, prevtime)
            cur_shed  = chars[char].get_plan()
            if prev_shed.name != cur_shed.name: # начато новое действие, значит меняем одежду

                if char == 'alice' and talk_var['sun_oiled']:  # Если Алису уже намазали кремом, повторное намазываение невозможно
                    talk_var['sun_oiled'] = 3
                ClothingNps(char, cur_shed.name)


    def ClothingNps(char, name): # устанавливает текущую одежду согласно расписанию (в том числе для инфо)
        if name == 'dressed':
            chars[char].dress_inf = '00b'
        elif char == 'lisa':
            if name == 'sleep':
                lisa.dress = clothes[lisa].sleep.GetCur().suf  #'b' if poss['sg'].stn > 2 else 'a'
                lisa.dress_inf = clothes[lisa].sleep.GetCur().info  #'02a' if poss['sg'].stn > 2 else '02'

            elif name in ['shower', 'bath']:
                lisa.dress_inf = '04a'

            elif name in ['breakfast', 'dishes', 'read', 'phone', 'dinner']:
                lisa.dress = clothes[lisa].casual.GetCur().suf  #'b' if 'bathrobe' in lisa.gifts and lisa.GetMood()[0] > 1 else 'a'
                lisa.dress_inf = clothes[lisa].casual.GetCur().info  #'04' if 'bathrobe' in lisa.gifts and lisa.GetMood()[0] > 1 else '01a'

            elif name == 'in_shcool':
                lisa.dress_inf = '01b'

            elif name == 'sun':
                lisa.dress = clothes[lisa].swimsuit.GetCur().suf  #'b' if 'bikini' in lisa.gifts else 'a'
                lisa.dress_inf = clothes[lisa].swimsuit.GetCur().info  #'03b' if 'bikini' in lisa.gifts else '03'

            elif name == 'swim':
                lisa.dress = clothes[lisa].swimsuit.GetCur().suf  #'b' if 'bikini' in lisa.gifts else 'a'
                lisa.dress_inf = clothes[lisa].swimsuit.GetCur().info
                if pose3_1 == '03':
                    lisa.dress_inf += 'w'

            elif name == 'homework':
                if all([clothes[lisa].learn.cur > 0, GetRelMax('lisa')[0] > 2, lisa.GetMood()[0] > 2, 'bathrobe' in lisa.gifts]):
                    lisa.dress = clothes[lisa].learn.GetCur().suf
                    lisa.dress_inf = clothes[lisa].learn.GetCur().info
                elif GetRelMax('lisa')[0] > 2 and lisa.GetMood()[0] > 2:
                    lisa.dress  = 'c'
                    lisa.dress_inf = '04b'
                elif 'bathrobe' in lisa.gifts:
                    lisa.dress  = 'b'
                    lisa.dress_inf = '04'
                else:
                    lisa.dress  = 'a'
                    lisa.dress_inf = '01a'

            elif name in ['in_shop', 'at_tutor']:
                lisa.dress_inf = '01'

            else:
                lisa.dress = 'a'
                lisa.dress_inf = '01a'

        elif char == 'alice':
            if name == 'sleep':
                alice.dress_inf = '02'
            elif name in ['shower', 'bath']:
                alice.dress_inf = '04aa'
            elif name in ['breakfast', 'read', 'dinner']:
                alice.dress = clothes[alice].casual.GetCur().suf  #cloth_type['alice']['casual']
                alice.dress_inf = clothes[alice].casual.GetCur().info  #'01c' if cloth_type['alice']['casual'] == 'b' else '01a'
            elif name in ['resting', 'blog', 'tv']:
                alice.dress = clothes[alice].casual.GetCur().suf  #cloth_type['alice']['casual']
                alice.dress_inf = clothes[alice].casual.GetCur().info
                if not ('09:00' <= tm < '20:00'):
                    alice.dress_inf += 'a'
                # if cloth_type['alice']['casual'] == 'b':
                #     alice.dress_inf = '01c' if '09:00' <= tm < '20:00' else '01ca'
                # else:
                #     alice.dress_inf = '01a' if '09:00' <= tm < '20:00' else '01aa'
            elif name == 'sun':
                alice.dress = 'a'
                alice.dress_inf = '03'
            elif name == 'swim':
                alice.dress = 'a'
                alice.dress_inf = '03a' if pose3_2 == '03' else '03'
            elif name in ['in_shop', 'at_friends']:
                alice.dress_inf = '01'
            elif name == 'cooking':
                alice.dress = clothes[alice].casual.GetCur().suf  #cloth_type['alice']['casual']
                alice.dress_inf = '01d' if alice.dress == 'b' else '01b'
            elif name == 'smoke':
                alice.dress = 'b' if flags['smoke'] == 'toples' else 'a'
                alice.dress_inf = '03b' if flags['smoke'] == 'toples' else '03'
            else:
                alice.dress = 'a'
                alice.dress_inf = '01a'

        elif char == 'ann':
            if name == 'sleep':
                ann.dress = clothes[ann].sleep.GetCur().suf  #cloth_type['ann']['sleep']
                ann.dress_inf = clothes[ann].sleep.GetCur().info  #'02' if cloth_type['ann']['sleep'] == 'a' else '02f'
            elif name in ['shower', 'bath', 'shower2']:
                ann.dress_inf = '04a'
            elif name == 'yoga':
                ann.dress_inf = '05'
            elif name == 'cooking':
                ann.dress = clothes[ann].cook_morn.GetCur().suf if tm < '12:00' else clothes[ann].cook_eve.GetCur().suf  #cloth_type['ann']['cooking']
                ann.dress_inf = clothes[ann].cook_morn.GetCur().info if tm < '12:00' else clothes[ann].cook_eve.GetCur().info  #'05b' if cloth_type['ann']['cooking'] == 'a' else '01c'
            elif name == 'breakfast':
                ann.dress = clothes[ann].cook_morn.GetCur().suf
                ann.dress_inf = '05a' if ann.dress == 'a' else '01b'
            elif name == 'resting':
                if tm <= '12:00':
                    ann.dress = 'a'
                    ann.dress_inf = '01b'
                elif tm <= '19:00':
                    ann.dress = 'b'
                    ann.dress_inf = '03'
                else:
                    ann.dress = clothes[ann].rest_eve.GetCur().suf  #cloth_type['ann']['rest']
                    ann.dress_inf = clothes[ann].rest_eve.GetCur().info  #'01b' if cloth_type['ann']['rest'] == 'a' else '04b'
            elif name == 'at_work':
                ann.dress_inf = '01a'
            elif name == 'in_shop':
                ann.dress_inf = '01'
            elif name == 'read':
                ann.dress = 'a' if tm < '14:00' else 'b'
                ann.dress_inf = '01b' if tm < '14:00' else '03'
            elif name == 'sun':
                ann.dress_inf = '03'
            elif name == 'swim':
                ann.dress_inf = '03a'
            elif name == 'dinner':
                ann.dress = clothes[ann].casual.GetCur().suf  #cloth_type['ann']['casual']
                ann.dress_inf = clothes[ann].casual.GetCur().info  #'01d' if cloth_type['ann']['casual'] == 'a' else '01b'
            elif name == 'tv':
                ann.dress_inf = '04b'
            elif name == 'tv2':
                ann.dress_inf = '04b'
            elif name == 'fuck':
                ann.dress_inf = '00b'
            else:
                ann.dress = 'a'
                ann.dress_inf = '01a'

        elif char == 'eric':
            if name in ['dinner', 'rest', 'tv2']:
                eric.dress = clothes[ann].casual.GetCur().suf  #cloth_type['ann']['casual']
                eric.dress_inf = '01a' if eric.dress == 'a' else '01b'
            elif name in ['fuck', 'sleep']:
                eric.dress_inf = '00a'
            elif name == 'shower2':
                eric.dress_inf = '00b'
            else:
                eric.dress_inf = '01'
        return


    def GetKolCams(location): # возвращает количество камер в локации
        kolcam = 0
        for room in location:
            for cam in room.cams:
                kolcam += 1
        return kolcam


    def SetCamsGrow(room, grow): # устанавливает коэффициент интереса к событию для камер в комнате
        for cam in room.cams:
            cam.grow = max(cam.grow, grow)
            # grow = int(grow * 0.8) # для каждой последующей камеры интерес снижается на 20%


    def clip(x, a, b): # вписывает число x в диапазон между a и b
        return a if x < a else(b if x > b else x)


    def clip_time(x, a='06:00', b='08:00'):
        ti = int(tm[:2])*60 + int(tm[-2:])
        h1, m1 = a.split(':')
        t_a = int(h1)*60 + int(m1) - ti
        h2, m2 = b.split(':')
        t_b = int(h2)*60 + int(m2) - ti
        return t_a if x < t_a else (t_b if x > t_b else x)


    def GetRelMax(char): # возвращает кортеж с номером и описанием диапазона отношений персонажа с Максом
        rel = chars[char].relmax
        return {
                   rel <= -300 : (-3, _("Война")),
            -300 < rel <= -100 : (-2, _("Враждебные")),
            -100 < rel <   0   : (-1, _("Плохие")),
            0    <= rel < 100  : ( 0, _("Прохладные")),
            100  <= rel < 300  : ( 1, _("Неплохие")),
            300  <= rel < 600  : ( 2, _("Хорошие")),
            600  <= rel < 1000 : ( 3, _("Тёплые")),
            1000 <= rel < 1500 : ( 4, _("Дружеские")),
            1500 <= rel        : ( 5, _("Близкие"))
            }[True]


    def AttitudeChange(char, level):  # изменение отношения персонажа в уровнях
        lvl = abs(level)
        mn = 1 if level > 0 else -1
        while lvl > 1:
            rel = {
                -3 : 300*mn,
                -2 : 200*mn,
                -1 : 100*mn,
                 0 : 100*mn,
                 1 : 200*mn,
                 2 : 300*mn,
                 3 : 400*mn,
                 4 : 500*mn,
                 5 : 600*mn}[GetRelMax(char)[0]]
            chars[char].relmax = clip(chars[char].relmax + rel , -450, 2000)
            lvl -= 1
        if lvl > 0:
            rel = {
                -3 : 300*mn*lvl,
                -2 : 200*mn*lvl,
                -1 : 100*mn*lvl,
                 0 : 100*mn*lvl,
                 1 : 200*mn*lvl,
                 2 : 300*mn*lvl,
                 3 : 400*mn*lvl,
                 4 : 500*mn*lvl,
                 5 : 600*mn*lvl}[GetRelMax(char)[0]]
            chars[char].relmax = clip(chars[char].relmax + rel, -450, 2000)


    def GetRelEric(char): # возвращает кортеж с номером и описанием диапазона отношений персонажа с Эриком
        return {
            -3 : _("Война"),
            -2 : _("Враждебные"),
            -1 : _("Плохие"),
            0  : _("Прохладные"),
            1  : _("Неплохие"),
            2  : _("Хорошие"),
            3  : _("Тёплые"),
            4  : _("Дружеские"),
            5  : _("Близкие")
            }.get(chars[char].releric, None)


    def MoodNeutralize(): # с течением времени настроение стрепится к нейтральному
        cycles = spent_time / 10 # расчет выполняется каждые 10 минут
        for char in chars:
            for i in range(cycles):
                if chars[char].mood > 0:
                    chars[char].mood -= 1
                elif chars[char].mood < 0:
                    chars[char].mood += 3 # возвращается в норму настроение быстрее, чем падает


    def seat_Breakfast(): # рассаживает семью за завтраком
        renpy.scene()
        renpy.show('BG breakfast 00') # общий фон
        renpy.show('Ann breakfast 0'+renpy.random.choice(['1', '2', '3'])+ann.dress)
        renpy.show('Alice breakfast 0'+renpy.random.choice(['1', '2', '3'])+alice.dress)
        renpy.show('Lisa breakfast 0'+renpy.random.choice(['1', '2', '3'])+lisa.dress)
        renpy.show('FG breakfast 0'+renpy.random.choice(['1', '2', '3'])) # стол
        renpy.show('Max breakfast 0'+renpy.random.choice(['1', '2', '3'])+mgg.dress)


    def seat_Dinner(): # рассаживает семью за ужином
        renpy.scene()
        renpy.show('BG dinner 00') # общий фон
        if day == 4 or day == 11 or ('eric' in chars and eric.plan_name == 'dinner'):
            renpy.show('Ann dinner eric-0'+renpy.random.choice(['1', '2', '3'])+ann.dress)
        else:
            renpy.show('Ann dinner 0'+renpy.random.choice(['1', '2', '3'])+ann.dress)
        renpy.show('Alice dinner 0'+renpy.random.choice(['1', '2', '3'])+alice.dress)
        renpy.show('Lisa dinner 0'+renpy.random.choice(['1', '2', '3'])+lisa.dress)
        if day == 4 or day == 11 or ('eric' in chars and eric.plan_name == 'dinner'):
            renpy.show('FG dinner 0'+renpy.random.choice(['1', '2', '3'])+'a') # стол
        else:
            renpy.show('FG dinner 0'+renpy.random.choice(['1', '2', '3'])) # стол
        renpy.show('Max dinner 0'+renpy.random.choice(['1', '2', '3'])+mgg.dress)


    def GetLisaPunChance():  # вероятность наказания Лизы
        if len(punlisa) == 0 or punlisa[0][0] > 2:
            pun_chance = 0  # Макс помогал правильно
        elif punlisa[0][0] == 1:
            pun_chance = 1000  # Макс сделал ошибку
        elif poss['sg'].stn == 2 and talk_var['truehelp']>=6:  # Макс на "хорошей" ветке и помог 6 и более раз
            grow = 100
            mind = 250
            if punlisa[0][0] == 2:  # если Макс просил об услуге неудачно, базовый шанс двойки 30% (сердитая Лиза менее внимательна, чем обычно)
                pun_chance = 300.0
            else:
                pun_chance = 100.0
            for d in range(1, len(punlisa)):
                if punlisa[d][3]:
                    pun_chance -= mind
                    mind = 250 # сбрасываем здравомыслие на исходную
                if punlisa[d][0] > 2:
                    pun_chance -= 300  # Макс помог Лизе, шанс наказания уменьшается на 15%
                    grow = 100
                    if d < 7:
                        break
                elif not punlisa[d][0]:
                    pun_chance += grow
                grow = grow * 1.15  # чем больше дней прошло со дня помощи Макса, тем выше шанс наказания
                mind = mind * 0.85  # чем больше дней прошло с момента последнего наказания, тем меньше усердие Лизы
        else:  # Макс не помогал с домашкой накануне
            help_count = 0
            grow = 50
            mind = 250
            if punlisa[0][0] == 2:  # если Макс просил об услуге неудачно, базовый шанс двойки 30% (сердитая Лиза менее внимательна, чем обычно)
                pun_chance = 300.0
            else:
                pun_chance = 50.0

            for d in range(1, len(punlisa)):
                if punlisa[d][3]:
                    pun_chance -= mind
                    mind = 250 # сбрасываем здравомыслие на исходную
                if punlisa[d][0] > 2:
                    pun_chance -= 150  # Макс помог Лизе, шанс наказания уменьшается на 15%
                    grow = 50
                    if d < 7:
                        help_count += 1
                        if help_count > 1:  # если за неделю Макс помог дважды, шанс наказания мизерный
                            break           # прерываем цикл расчета
                elif not punlisa[d][0]:
                    pun_chance += grow
                grow = grow * 1.15  # чем больше дней прошло со дня помощи Макса, тем выше шанс наказания
                mind = mind * 0.85  # чем больше дней прошло с момента последнего наказания, тем меньше усердие Лизы
        return clip(pun_chance, 0, 900)


    def GetAlicePunChance():  # вероятность наказания Алисы
        if len(punalice) == 0 or not dcv['smoke'].done:  # Алиса не курила
            pun_chance = 0
        elif punalice[0][1]:   # Макс подставил Алису
            pun_chance = 1000
        else:
            finded = 0
            help_count = 0
            grow = 50
            mind = 250
            if punalice[0][0] == 2:  # если Макс просил об услуге неудачно, базовый шанс плохо спрятать сигареты 30% (сердитая Алиса менее внимательна, чем обычно)
                pun_chance = 300.0
            else:
                pun_chance = 50.0

            for d in range(1, len(punalice)):
                if punalice[d][3]:   # Ализа понесла наказание
                    finded += 1
                    pun_chance -= mind  # шанс наказания снижается на уровень здравомыслия
                    mind = 250          # сбрасываем здравомыслие на исходную
                elif punalice[d][2]:  # Макс пытался заступиться за Алису перед наказанием
                    finded += 1
                    pun_chance += grow // 3       # шанс невнимательности меньше
                    mind = clip(mind+100, 0, 250) # плюс прирост здравомыслия
                if punalice[d][0] > 2: # Алиса выполнила требование Макса, шанс наказания уменьшается на 15%
                    pun_chance -= 150
                    grow = 50
                    if d < 7:
                        help_count += 1
                        if help_count > 1:  # если за неделю Макс дважды успешно шантажировал, шанс наказания мизерный
                            break           # прерываем цикл расчета
                else:   # Макс не шантажировал Алису или шантажировал неудачно
                    pun_chance += grow

                if d < 7 and finded > 1:  # если за последнюю неделю сигареты были найдены уже дважды
                    pun_chance -= 250
                    break
                grow = grow * 1.1   # чем больше дней прошло со дня, когда Макс чего-то требовал, тем выше шанс наказания
                mind = mind * 0.85  # чем больше дней прошло с момента последнего наказания, тем меньше внимательна Алиса
        return clip(pun_chance, 0, 900)


    def GetDisobedience():  # вероятность ослушания Алисы
        chance = 90
        rise = 90
        for d in range(0, len(punalice)-1):
            if punalice[d][0] in [4,5,6]:
                break # посчет идет только до ближайшего требования Макса
            else:
                chance += rise
                rise *= 1.1
        return clip(chance, 0, 1000)


    def ColumnSum(punchar, i, limit=50):  # сумму i-тых элементов списка списков
        sm = 0
        for d in range(len(punchar)):
            if d < limit:
                sm += punchar[d][i]
        return sm


    def GetChanceConvince(punchar, multiplier = 1):  # возвращает шанс убедить персонажа после наказаний
        ch = mgg.social * 10 * multiplier
        mind = 200
        for d in punchar:
            if d[3]:  # если сестра была наказана, убедить ее проще
                ch += mind
            mind = mind * 0.70 # чем больше дней прошло с момента последнего наказания, тем меньше прибавка
        return Chance(clip(int(ch), 0, 900))


    def notify_queue():  # функция показа всплывающего сообщения из очереди
        global notify_list
        if all((not renpy.get_screen('notify'), notify_list)):
            renpy.notify(notify_list.pop(0));

    # функция для смены курсора
    # курсоры должны лежать в папке images/interface/cursors
    # формат имен фалов для курсоров:
    # 'images/interface/cursors/ИмяКурсора.png'
    def cursor(name = None):
        config.mouse = None
        if renpy.game.preferences.physical_size[1] < 900:
            if name == 'find':
                config.mouse = {'default' : [('images/interface/cursors/find-64.webp', 27, 27)]}
            elif name == 'talk':
                config.mouse = {'default' : [('images/interface/cursors/talk-64.webp', 11, 50)]}
            elif name == 'palms':
                config.mouse = {'default' : [('images/interface/cursors/palms-64.webp', 37, 32)]}
            elif name:
                config.mouse = {'default' : [('images/interface/cursors/' + name + '-64.webp', 0, 0)]}
        else:
            if name == 'find':
                config.mouse = {'default' : [('images/interface/cursors/find-80.webp', 33, 33)]}
            elif name == 'talk':
                config.mouse = {'default' : [('images/interface/cursors/talk-80.webp', 14, 61)]}
            elif name == 'palms':
                config.mouse = {'default' : [('images/interface/cursors/palms-80.webp', 46, 40)]}
            elif name:
                config.mouse = {'default' : [('images/interface/cursors/' + name + '-80.webp', 0, 0)]}
    # превращаем функцию в action,
    # чтобы можно было привязать, например, к нажатию кнопок:
    # action Cursor('talk')
    Cursor = renpy.curry(cursor)

    def have_dialog():  # возвращает признак наличия диалога для первого персонажа в комнате
        # cur_plan = GetPlan(eval('plan_'+current_room.cur_char[0]), day, tm)
        if current_room.cur_char:
            cur_plan = chars[current_room.cur_char[0]].get_plan()
            return cur_plan.enabletalk and len(TalkMenuItems()) > 0
        else:
            return False


    def there_in_stock(char):  # проверяет, есть ли у Макса подарок персонажу в качестве извинения
        for id in sorry_gifts[char].valid:
            if items[id].have:
                return True
        return False


    def check_is_home(char, loc='house'):  # определяет (по расписанию) находится ли персонаж дома в данный момент
        return chars[char].get_plan().loc == loc


    def check_only_home(char, loc='house'):  # проверяет, что кроме этого персонажа и Макса дома больше никого нет
        rez = True
        for ch in chars:
            char_loc = chars[char].get_plan().loc
            if ch != char and loc == char_loc:
                rez = False
                break
        return rez


    def add_lim(var, a, limit):
        if var.find('.')>0:
            v1, arg = var.split('.')
            if eval(var) < limit:
                setattr(eval(v1), arg, a)
                if eval(var) > limit:
                    setattr(eval(v1), arg, limit)
        else:
            if eval(var) < limit:
                globals()[var] += a
                if eval(var) > limit:
                    globals()[var] = limit
