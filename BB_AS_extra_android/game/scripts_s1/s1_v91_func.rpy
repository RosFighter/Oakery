
init python:

    # чит на денежку
    def get_cheats_money():
        mgg.ask(9)
        dcv.ch_money.set_lost(1)

    # чит настроения
    def set_mood_lvl(char, lvl):
        if char not in chars:
            return
        if lvl < -4:
            lvl = -4
        elif lvl > 4:
            lvl = 4

        if lvl == chars[char].GetMood()[0]:
            return

        chars[char].mood = {
            -4  : -300,
            -3  : -190,
            -2  : -90,
            -1  : -25,
            0   : 0,
            1   : 25,
            2   : 90,
            3   : 190,
            4   : 300
            }[lvl]

    # чит отношений с Максом
    def set_relation_lvl(char, lvl):
        if char not in chars:
            return
        if lvl < -3:
            lvl = -3
        elif lvl > 5:
            lvl = 5

        if lvl == GetRelMax(char)[0]:
            return

        chars[char].relmax = {
            -3  : -310,
            -2  : -110,
            -1  : -10,
            0   : 10,
            1   : 110,
            2   : 330,
            3   : 660,
            4   : 1100,
            5   : 1650
            }[lvl]

    # чит влияния
    def set_influence(char, asp):
        if asp == 'm+':
            infl[chars[char]].add_m(20, True)
        elif asp == 'm-':
            infl[chars[char]].sub_m(20, True)
        elif asp == 'e+':
            infl[chars[char]].add_e(20, True)
        elif asp == 'e-':
            infl[chars[char]].sub_e(20, True)

    # возвращает имя метки завтрака
    def get_breakfast():
        if day == 1:
            return 'first'
        elif day == 2:
            return '2'
        elif day == 3:
            return '3'
        elif day == 4:
            # первый шопинг
            return '4'
        elif all([day>=5, weekday==0, flags.breakfast==4]):
            # после ночёвки у Эрика
            return '5'
        elif all([day>=7, weekday==2, flags.breakfast==5, flags.dinner==6]):
            # вторник после ночевки Эрика
            return '7'
        elif all([day>=12, weekday==0, flags.breakfast==7, flags.dinner==11]):
            # Аня рассказывает о вероятной свадьбе
            return '12'
        elif all([day>=18, weekday==6, flags.breakfast==12, flags.dinner==17]):
            # первый завтрак с Кирой
            return '18'
        elif 'kira' in chars and all([weekday==2, kira.dcv.feature.stage in [6, 7],
                                            flags.breakfast==18, flags.dinner==17]):
                # первое упоминание Александры (через несколько дней после первой
                # фотосессии с Кирой)
            return '35'
        elif 'kira' in chars and all([
                kira.flags.showdown_e,      # поговорили об Эрике со всеми кроме
                lisa.flags.showdown_e,      # Анны
                alice.flags.showdown_e,
                # прошло не менее 3-х рабочих дней с момента изгнания Эрика
                eric.dcv.battle.lost<56 or (eric.dcv.battle.lost<58 and weekday>4),
                flags.eric_wallet == 4,     # этап "кошелька"
                ]):
            # завтрак через несколько дней после изгнания Эрика
            return 'after_showdown_with_eric'
        else:
            return False

    # возвращает имя метки ужина
    def get_dinner():
        if day == 1:
            return 'first'
        elif day == 2:
            return '2'
        elif day == 3:
            return '3'
        elif day == 4: # первый ужин с Эриком
            return '4'
        elif all([day>=5, weekday==0, flags.dinner==4]):
            return '5'
        elif all([day>=6, weekday==1, flags.breakfast==5, flags.dinner==5]):
            return '6'
        elif all([day>=11, weekday==6, flags.breakfast==7, flags.dinner==6]):
            return '11'
        elif all([day>=12, weekday==0, flags.dinner==11, flags.breakfast==12]):
            return '12'
        elif all([day>=17, weekday==5, flags.breakfast==12, flags.dinner==12]):
            return '17'
        elif all([weekday==1, lisa.dcv.battle.stage in [1, 2, 3], not flags.add_training]):
            return 'ab_lisa_ed'
        elif all([weekday==0, lisa.dcv.intrusion.done, not flags.about_earn,
                (lisa.dcv.battle.stage in [4, 6] and lisa.dcv.intrusion.stage==1 and flags.lisa_sexed==1)
                    or (lisa.dcv.battle.stage==2 and not lisa.dcv.intrusion.stage)]):
            return 'ab_earn'
        elif all([weekday==5, items['sexbody2'].have, alice.dcv.intrusion.stage<5, alice.dcv.intrusion.enabled]):
            return 'lace_lingerie'
        else:
            return False

    ############################################################################

    # полночь
    def start_midnight(cheat = False):
        global random_loc_ab, random_sigloc
        global prenoted, film, SpiderResp, olivia_night_visits

        random_loc_ab = random_choice(['a', 'b'])
        random_sigloc = random_choice(['n', 't'])

        alice_disodedience()    # нарушение или соблюдение требований Алисой

        GetDeliveryList()       # список доставок

        changing_movie()        # меняем фильм, который смотрят АиЭ

        ###     сброс флагов    ####
        olivia_night_visits = olivia_nightvisits()
        lisa.sleeptoples = False

        flags.eric_noticed = False
        prenoted = 0
        film = ''
        if SpiderResp > 0:      # откат респа паука
            SpiderResp -= 1

        # уменьшение счётчиков дней
        dcv.countdown()

        for ch in chars:
            char = chars[ch]
            if char.id == 'lisa':
                # фильм-наказание сбрасывается позже, при наступлении нового игрового дня
                char.dcv.countdown(['special'])
            else:
                char.dcv.countdown()

            if char.dcv.shower.done and char.dcv.shower.stage:
                # откат по подглядыванию в душе кончился, обнуляем этап
                char.dcv.shower.stage = 0

        ###     корректоры      ####
        if flags.about_earn:
            # был разговор о заработках за ужином
            if dcv.clearpool.done and dcv.clearpool.stage < 3:  # прошёл откат чистки бассейна
                dcv.clearpool.stage = 3     # теперь Макс работает без оплаты
            if dcv.buyfood.done and dcv.buyfood.stage < 3:      # прошёл откат заказа продуктов
                dcv.buyfood.stage = 3       # теперь Макс работает без оплаты
        if poss['nightclub'].st() >= 5 and kol_choco == 0:
            items['choco'].unblock()

    # новая неделя
    def start_newweek(cheat = False):
        global shower_schedule

        if 'kira' in chars:
            kira.sleepnaked = False # сбрасываем флаг стриптиза Киры

        if 'kira' in chars and not shower_schedule:
            shower_schedule = 1         # активируем новое расписаниеa
        elif all([shower_schedule == 1, alice.flags.together_sleep > 0]):
            shower_schedule = 2         # в среду и воскресенье Лизу с Кирой отправляем в душ раньше Алисы

        if all(['sexbody2' in alice.gifts, flags.lisa_sexed>0, get_rel_eric()[0] < 0]):
            # отношения с Эриком по сёстрам определены, вражда
            # активируем еженедельный счетчик на спаливание Киры и Макса Эриком
            wcv.catch_Kira.enabled = True  # теперь Эрик может спалить Макса и Киру

        if 'olivia' in chars:
            if olivia.dcv.feature.stage==2:
                # состоялись первые два разговора по средам, теперь Оливия будет приходить во вторник и пятницу
                olivia.dcv.feature.stage = 3

        flags.noclub = False
        flags.trick = False

        # назначаем день бонусных потрахушек (за Лизу) на новую неделю
        if flags.voy_stage in [9, 10, 12, 13, 14]:
            flags.ae_bonus_day = random_choice([1, 3, 4])

        # уменьшение счетчика событий, зависимых от прошедших дней
        wcv.countdown()

        for char in chars:
            chars[char].weekly.reset()

        # еженедельное снижения влияния
        if not cheat:
            if 'eric' in chars and all([eric_obligation.get_debt(), flags.eric_wallet == 0, get_rel_eric()[0] < 0]):
                # Макс не заплатил Эрику дань, запускается кошелёк
                eric_obligation.volume = 0
                eric_obligation.debt = 0
                flags.eric_wallet = 1
            for char in infl:
                infl[char].sub_m(30)
                infl[char].sub_e(30)

        if 'eric' in chars:
            eric_obligation.reset()

    # новый игровой день
    def start_newday(cheat = False):
        global random_tab, ann_eric_scene, stockings

        random_tab = [[random_randint(0, 99) for i in range(10)] for j in range(10)]

        if 'spider' in NightOfFun:
            NightOfFun.remove('spider') # если ночная забава не состоялась, паука из списка забав удаляем - он сбежал

        pun_list_update()   # наполнение списков наказания сестёр
        cam_poses.clear()   # очистка списка использованных поз для камер
        cam_flag.clear()    # очистка подсматриваний через камеры
        ann_eric_scene = ''

        if flags.voy_stage in [9, 10, 12, 13, 14] and weekday == flags.ae_bonus_day:
            # наличие чулков определяется договорённстью
            stockings = flags.can_ask == 3
        else:
            # просто рандом
            stockings = random_outcome(50) # шанс, что Аня будет в чулках, 50%

        # сброс фильма-наказания
        lisa.dcv.countdown(only=['special'])

        for ch in chars:
            char = chars[ch]
            # сбросим подглядывания, диалоги и состояния
            char.daily.reset()
            char.spanked = False

            # срок извинительных подарков
            if char.sorry.owe and char.sorry.left > 0:
                char.sorry.left -= 1

            # для каждого типа одежды каждого персонажа запустим рандомную смену
            char.clothes.SetDailyRand()

        if olivia_nightvisits():
            # установим откат для ночных визитов Оливии.
            if not olivia.dcv.special.stage:
                # первого ночного визита Оливии ещё не было
                olivia.dcv.special.set_lost(5)

            elif lisa.flags.showdown_e > 1:
                # после изгнания Эрика откат 1 неделя
                olivia.dcv.special.set_lost(5)

            else:
                # если Эрик вмешался до прихода Оливии, откат неделя, иначе две недели
                olivia.dcv.special.set_lost(5 * olivia.dcv.battle.stage)

        # назначаем день бонусных потрахушек (за Лизу) первый раз
        if flags.voy_stage in [9, 10, 12, 13, 14] and not flags.ae_bonus_day:
            flags.ae_bonus_day = random_choice([1, 3, 4])

        if mgg.credit.debt > 0:        # если кредит не погашен
            mgg.credit.left -= 1       # уменьшим счетчик дней
            if mgg.credit.left == 0:   # если счетчик дней кончился
                mgg.credit.charge()    # начислим штраф

        if alice.flags.promise == 'bath':
            alice.flags.promise = False     # если Макс пропустил развлечение в ванной, Алиса ему ничего не должна

    ############################################################################

    # нарушение или соблюдение требований Алисой
    def alice_disodedience():
        if alice.dcv.special.enabled and alice.dcv.set_up.enabled:
            alice.daily.smoke = 0
            alice.nopants     = False
            alice.sleeptoples = False
            alice.sleepnaked  = False
        if alice.req.req == 'money':
            alice.req.reset()
        elif alice.req.result=='nojeans': # если требование не носить джинсы, оно не может быть нарушено
            pass
        elif alice.req.req and (not alice.req.result or alice.req.result[:3] != 'not'):
            # Если требование Макса было и это не деньги
            if alice.req.req in ['sleep', 'naked', 'bikini'] and alice.flags.together_sleep:  # 09.2
                # Макс уже ночевал с Алисой, требование спать топлес или голой больше не нарушается
                # после 3-го совместного душа требование загорать топлес так же не нарушается
                alice.req.result = alice.req.req
                if alice.req.req == 'sleep':
                    alice.sleeptoples = True
                elif alice.req.req == 'naked':
                    alice.sleepnaked = True
            elif random_outcome(GetDisobedience()):
                # шанс, что Алиса не будет соблюдать договоренность
                alice.req.result = 'not_' + alice.req.req
                alice.req.noted = False  # нарушение ещё не замечено Максом
            else:
                alice.req.result = alice.req.req
                if alice.req.req == 'nopants':
                    alice.nopants = True
                elif alice.req.req == 'sleep':
                    alice.sleeptoples = True
                elif alice.req.req == 'naked':
                    alice.sleepnaked = True

    # замена фильма, который смотрят АиЭ
    def changing_movie():
        global ae_tv_order
        if 'eric' in chars and all([eric.daily.tv_sex, eric.stat.handjob > 0]):
            # если подсматривали за АиЭ у ТВ, меняем фильм
            ae_tv_order.pop(0)
            if not ae_tv_order:
                ae_tv_order = ['0'+str(i) for i in range(1, 8)]
                renpy.random.shuffle(ae_tv_order)  # перемешаем список случайным образом

    # ежедневное наполнение списков расчета наказаний сестёр
    def pun_list_update():
        if 0 < GetWeekday(prevday) < 6:
            if poss['sg'].st() > 0 and not lisa.daily.homework:  # был разговор с Лизой по поводу наказаний и не помогал
                punlisa.insert(0, [  # вставляем в начало
                    0,  # помощь Макса с д/з (0, 1, 2, 3, 4) (не помогал / допустил ошибку / неудачно попросил услугу / помог безвозмездно / помог за услугу)
                    0,  # получена двойка в школе (0, 1)
                    0,  # Макс заступился за Лизу перед наказанием (0, 1, 2)
                    0,  # Лиза понесла наказание (0, 1)
                    0,  # подозрительность
                    ])
                del punlisa[10:]

        if poss['smoke'].st() > 2:  # Макс видел курящую Алису
            punalice.insert(0, [  # вставляем в начало
                0,  # Макс шантажировал Алису (1-передумал, 2-неудачно, 3-деньги, 4-перекур топлес, 5-лифчик, 6-трусики, 7-джинсы, 8-голая)
                0,  # Макс подставлял Алису
                0,  # Макс заступился за Алису перед наказанием
                0,  # Ализа понесла наказание
                0,  # подозрительность
                ])
            del punalice[14:]

    # уменьшает букву одежды для многослойных изображений
    def sub_dress_ind(k):
        return {'a':'', 'b':'a', 'c':'b', 'd':'c'}[k]
