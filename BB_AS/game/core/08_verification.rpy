
init python:

    # список sub_lst входит в список lst
    def list_in_list(sub_lst, lst):
        return all(x in lst for x in sub_lst)


    # определяет (по расписанию) находится ли персонаж дома в данный момент
    def check_is_home(char, loc='house'):
        if char not in chars:
            return False

        return chars[char].get_plan().loc == loc


    # проверяет, что кроме этого персонажа и Макса дома больше никого нет
    def check_only_home(char, loc='house'):
        rez = True
        for ch in chars:
            if ch == char:
                continue
            char_loc = chars[ch].get_plan().loc
            if loc == char_loc:
                rez = False
                break
        return rez


    # проверяет по расписанию, находится ли персонаж в текущей комнате
    def check_is_room(char, room=None):
        if _in_replay:
            return True
        if char not in chars:
            return False
        plan_char = chars[char].get_plan()
        if room is None:
            return eval(plan_char.loc+'['+str(plan_char.room)+']')==current_room
        else:
            return eval(plan_char.loc+'['+str(plan_char.room)+']')==room


    # присутствует ли Эрик за ужином
    def Eric_at_dinner():
        rez = False
        if flags.eric_banished:
            return rez

        if any([day==4, day==11]):
            # первая и вторая субботы
            rez = True
        elif all([weekday==6, day>=11, flags.dinner==6]):
            # вторая суббота с Эриком (фикс пропущенных)
            rez = True
        elif all([weekday==6, poss['seduction'].st() in [14, 15], not lisa.dcv.battle.stage, lisa.dcv.battle.lost<7, ('sexbody1' not in alice.gifts or alice.dcv.battle.stage>3)]):
            # начинается битва за Лизу, битва за Алису еще не началась или уже результат определился
            rez = True
        elif all([weekday==6, lisa.dcv.battle.stage==2, lisa.dcv.intrusion.done]):
            # продолжение разговора о Лизе в случае отсрочки
            rez = True
        elif all([weekday==6, not alice.dcv.battle.stage, 'sexbody1' in alice.gifts, (not lisa.dcv.battle.stage or lisa.dcv.battle.stage>3)]):
            # начинается битва за Алису, битва за Лизу еще не началась или уже результат определился
            rez = True
        elif all([weekday==6, alice.dcv.battle.stage==2, alice.dcv.battle.enabled, alice.dcv.battle.done]):
            # продолжение разговора об Алисе в случае отсрочки
            rez = True
        elif all([weekday==6, 'sexbody2' in alice.gifts, 4<alice.dcv.intrusion.stage<7]):
            # Макс опередил Эрика с кружевным бельём Алисы
            rez = True

        return rez


    # пройден первый урок массажа ног
    def learned_foot_massage():
        return _in_replay or (len(online_cources)>1 and online_cources[1].cources[0].less)


    # пройден первый урок массажа рук
    def learned_hand_massage():
        return _in_replay or (len(online_cources)>1 and online_cources[1].cources[1].less)


    # Оличия приходит в гости днём
    def olivia_visits():
        if 'olivia' not in chars:
            return 0

        rez = 0

        if all([weekday==3, olivia.dcv.feature.stage < 2]):
            # среда, первые две беседы с Оливией
            rez = 1
        elif all([lisa.flags.crush>11, weekday==2, olivia.dcv.feature.stage>1]):
            # каждый вторник, больше двух бесед с Оливией
            rez = 2
        elif  all([weekday==5, 1<olivia.dcv.feature.stage<4]):
            # пятница, беседа о ночных посиделках ещё не состоялась
            rez = 3
        elif  all([weekday==5, olivia.dcv.feature.stage>3, not olivia.dcv.special.done]):
            # пятница, состоялась беседа о ночных посиделках, не прошел откат ночных посиделок
            rez = 4
        elif all([weekday==5, olivia.dcv.special.stage==1, olivia.dcv.feature.stage<5]):
            # пятница, после первых ночных посиделок, разговора с Оливией после ночного визита ещё не было
            rez = 5
        elif all([weekday==5, olivia.dcv.feature.stage>4, olivia.dcv.special.done, flags.eric_banished, lisa.flags.showdown_e<2]):
            # пятница, после изгнания Эрика Оливия приходит днём, ещё не было
            # разговора с Лизой о ночных визитах Оливии
            rez = 6
        elif all([weekday in [0, 6], 6 > lisa.flags.showdown_e > 1]):
            # состоялся разговор с Лизой о ночных визитах Оливии,
            # Оливия ещё не может приходить при Анне ночью
            rez = 7
        elif all([weekday == 0, lisa.flags.showdown_e > 5]):
            # Оливия может приходить ночью, поэтому днём приходит во вторник и воскресенье
            rez = 8
        return rez


    # Оливия приходит на ночные посиделки
    def olivia_nightvisits():
        if 'olivia' not in chars:
            return 0

        rez = 0

        if  all([GetWeekday(day)==6, olivia.dcv.feature.stage>3, olivia.dcv.special.done, not olivia.dcv.special.stage]):
            # ночь с пятницы на субботу, состоялась беседа о ночных посиделках, ночных посиделок ещё не было
            rez = 1
        elif all([GetWeekday(day)==6, olivia.dcv.feature.stage>4, olivia.dcv.special.done, not flags.eric_banished]):
            # ночь с пятницы на субботу, состоялась беседа после первых ночных посиделках, прошел откат ночных посиделок
            # Эрик ещё не изгнан
            rez = 2
        elif all([GetWeekday(day)==6, olivia.dcv.feature.stage>4, olivia.dcv.special.done, lisa.flags.showdown_e > 5]):
            # ночь с пятницы на субботу, состоялась беседа после первых ночных посиделках, прошел откат ночных посиделок
            # Анна дала разрешение на ночные визиты Оливии
            rez = 3

        return rez


    # Лиза уже снимала майку при просмотре ТВ с Оливией
    def lisa_was_topless():
        return 'olivia' in chars and olivia.dcv.special.stage>1


    # Лиза снимет майку для события
    def lisa_will_be_topless():
        ###условия для того, чтобы Лиза сняла майку##
        if not lisa_was_topless():
            return 0    # не было просмотра ТВ с Оливией топлесс

        if lisa.plan_name == 'tv2':
            # 1 с пн-пт Лизу наказывали и была 1 успешная защита от наказания, то: 1 помощь с уроками + 1 массаж рук + 1 мытьё посуды
            # 2 с пн-пт Лизу не наказывали, то: 2 помощи с уроками + 1 массаж рук + 2 мытья посуды
            # 3 с пн-пт Лизу наказывали и не было защиты или не поучилось защитить, то: 3 помощи с уроками + 2 массажа рук + 3 мытья посуды
            # 4 уговор с Лизой на ужастики-топлесс, но Макс больше 2х раз за неделю влез в душ, идёт 2хнедельный откат

            lw = lisa.weekly
            if not lisa.dcv.shower.done:
                # Макс попался на третьем подглядывании за неделю (соглашение об ужастиках топлесс)
                return -4
            if lw.punished:
                # Лизу наказывали
                if lw.protected:
                    # была успешная защита от наказания
                    return 1 if all([lw.help, lw.mass1, lw.dishes]) else -1
                else:
                    # не защитил (или не смог)
                    return 3 if all([lw.help>2, lw.mass1>1, lw.dishes>2]) else -3
            else:
                # не было наказаний
                    return 2 if all([lw.help>1, lw.mass1, lw.dishes>1]) else -2
        # else:
        #     if not lisa.dcv.other.done:
        #         # Лизу наказали, значит ужастики в майке
        #         return -4


    # соблюдены условия для открытия второй камеры ванной
    def looked_ladder():
        if all([flags.ladder>2, house[3].cams, house[3].max_cam<2]):
            # стремянка установлена, есть камера в ванной, вторая камера не активирована
            rez = all([alice.flags.ladder, ann.flags.ladder, lisa.flags.ladder])
            if 'kira' in chars:
                rez = all([rez, kira.flags.ladder])
            rez = any([rez, eric.flags.ladder > 1])
            return rez
        else:
            return False


    # возвращает стадии подглядывания в душе за Алисой
    def get_alice_shower_peeping_stage():

        if 0 < len(alice.sorry.give) < 4 or (not poss['risk'].used(0) and mgg.stealth > 20):
            return 0

        if len(alice.sorry.give) == 4 and 'sexbody2' not in alice.gifts:
            return 1

        if 'sexbody2' in alice.gifts:
            return 2

        return -1


    # можно ли подмешивать слабительное Эрику
    def can_use_laxative():

        if 'eric' not in chars:
            return False

        return all([
            flags.lisa_sexed in [7, 10],
            lisa.dcv.intrusion.stage > 2,
            eric.get_plan(day, '19:00').name == 'dinner',
            items['laxative'].have,
            not flags.trick,
            ])


    # можно ли подмешивать Эрику антистояк
    def can_use_sedative():
        if 'eric' not in chars:
            return False

        return all([
            flags.lisa_sexed in [7, 10],
            lisa.dcv.intrusion.stage > 2,
            eric.get_plan(day, '19:00').name == 'dinner',
            items['sedative'].have,
            not flags.trick,
            ])


    # возвращает уровень раскрепощения Лизы
    def get_lisa_emancipation():
        # 01. Совсем стеснительная. Стесняется показываться перед Максом с обнажённой грудью и в трусиках. Переход: убеждение спать без штанов.
        # 02. Стеснительная. Стесняется показываться перед Максом с обнажённой грудью и без трусиков. Переход: снятие майки при просмотре ТВ с Оливией.
        # 03. Любопытная. Стесняется показываться перед Максом без трусиков. Переход:???
        if lisa_was_topless():
            # Лиза снимала майку при Оливии
            return 3    # Любопытная
        elif poss['sg'].st() not in [0, 1, 2, 4]:
            # Макс убедил Лизу спать без штанов
            return 2    # Стеснительная
        else:
            return 1    # Совсем стеснительная


    # возвращает уровень раскрепощения Анны
    def get_ann_emancipation():
        # 01. Я же мать! Стесняется показываться перед Максом в нижнем белье. Переход: 1-ая попытка сделать массаж у ТВ.
        # 02. Не для детских глаз. Стесняется показываться перед Максом с обнажённой грудью и без трусиков. Переход: ???.
        if _in_replay or poss['mom-tv'].st() > 7:
            # состоялся первый массаж у ТВ
            return 2
        else:
            return 1


    # проверяет выполнение условий для отображения печеньки
    def cookie_verification(cookie):
        # количество найденых печенек на одну меньше текущего номера
        # определим количество уже найденных печенек данной одежды персонажа
        # и прибавим единичку

        if _in_replay:
            return False

        try:
            fc = len(persistent.mm_cookies[cookie.char][cookie.clot]) + 1
        except:
            fc = 1

        try:
            rez = eval(cookie.req)
        except:
            rez = True  # если условие ошибочно прописано, считаем, что оно выполняется

        if 'kira' not in chars:
            return False

        if all([
                #  открыт тип одежду у персонажа
                cookie.clot in menu_chars[cookie.char.title()].get_open_clot(),
                cookie.num == fc,                   # правильное количество уже найденных
                current_room == eval(cookie.room),  # нужная комната
                weekday in cookie.lod,              # нужный день недели
                cookie.tm1 <= tm < cookie.tm2,      # нужное время
                rez,                                # выполняется дополнительное условие
            ]):
            return True
        else:
            return False


    # можно ли заняться сексом с Кирой в душе
    def can_kira_sex_shower():

        return all([
            wcv.catch_Kira.stage not in [1, 2], # Эрик не палил Макса с Кирой в ванной, или уже изгнан
            kira.dcv.photo.stage > 2,           # состоялась третья фотосессия
            kira.stat.handjob > 1,              # получена периодическая дрочка в бассейне
            not kira.flags.promise,             # за Максом нет долга по куни
            ])


    # Алиса загорает топлес после нанесения крема
    def alice_sun_topless():
        return alice.plan_name == 'sun' and alice.daily.oiled in [2, 4]


    # возвращает стадию событий по вручению кружевного белья Алисе
    def get_stage_sexbody2():
        if not alice.dcv.intrusion.enabled:
            # Эрик ещё не вмешивался в блог Алисы
            return 0
        elif flags.eric_banished:
            #  Эрик изгнан
            return 1
        elif all([alice.dcv.intrusion.enabled, 4 > alice.dcv.intrusion.lost > 1, alice.dcv.intrusion.stage < 1]):
            # Эрик прорвёл первый совместный блог с Алисой, Макс ещё не знает о покупке Эриком белья
            return 2
        elif all([alice.dcv.intrusion.enabled, 4 > alice.dcv.intrusion.lost > 1, alice.dcv.intrusion.stage == 1]):
            # Макс знает о покупке Эриком белья, но ещё не говорил об этом с Алисой
            return 3
        elif all([alice.dcv.intrusion.enabled, 4 > alice.dcv.intrusion.lost > 1, alice.dcv.intrusion.stage == 2]):
            # Макс знает о покупке Эриком белья, но подошёл к Алисе не вовремя
            return 4
        elif all([alice.dcv.intrusion.enabled, 4 > alice.dcv.intrusion.lost > 1, alice.dcv.intrusion.stage == 3]):
            # Макс знает о покупке Эриком белья и знает, какое именно нужно, т.е. может купить
            return 5
        elif all([alice.dcv.intrusion.enabled, alice.dcv.intrusion.stage == 5]):
            # Макс подарил Алисе кружевное боди, но ещё не разговаривал после этого с Эриком
            return 6
        elif all([alice.dcv.intrusion.enabled, alice.dcv.intrusion.stage == 7]):
            # Макс подарил Алисе кружевное боди, и поговорил после этого с Эриком
            return 7
        elif all([alice.dcv.intrusion.enabled, alice.dcv.intrusion.done, alice.dcv.intrusion.stage < 5]):
            # срок вышел и теперь боди Алисе купит Эрик
            return 8
        elif all([alice.dcv.intrusion.enabled, alice.dcv.intrusion.done, alice.dcv.intrusion.stage == 8]):
            # срок вышел и Эрик купил боди Алисе (но она его ещё не примеряла при нём)
            return 9
        elif all([alice.dcv.intrusion.enabled, alice.dcv.intrusion.done, alice.dcv.intrusion.stage == 9]):
            # Эрик купил боди Алисе и она примеряла боди при нём
            return 10

        return 'bag'


    # Макс может подарить Алисе кружевное боди
    def can_give_sexbody2():
        return all([
            not alice.dcv.intrusion.done,       # срок, когда Эрик купит боди, ещё не пришёл
            alice.dcv.intrusion.stage > 2,      # Макс знает, какое именно боди нужно Алисе
            weekday in [4, 5],                  # боди можно подарить в четверг или пятницу
            alice.dcv.intrusion.lost in [1, 2], # когда откату осталось 1-2 дня
            items['sexbody2'].have,             # у Макса есть кружевное боди
            ])

    # отношения Макса с Эриком
    def get_rel_eric():
        if _in_replay:
            return rel_eric

        if 'eric' not in chars:
            return False
        if eric.relmax == 0:
            return (0, _("Не определены"))
        elif eric.relmax < 0:
            return (-1, _("Откровенная вражда"))

        # для определения дружбы / хитрой дружбы нужно разобрать выбор Макса в вопросах по девушкам
        # варианты:
        #   дружба              - до определения отношений хотя бы с одной девушкой
        #   Настоящая дружба    - выбран вариант отдать девушку Эрику (обеих девушек после определения отношений по обеим)
        #   Фальшивая дружба    - хотя бы по одной девушке начал юлить

        if not any([lisa.dcv.battle.stage, alice.dcv.battle.stage]):
            # ещё ни по одной девушке отношения не определены
            return (1, _("Дружба"))

        elif any([
                all([lisa.dcv.battle.stage in [1, 4], alice.dcv.battle.stage in [1, 4, 7]]),    # выбор сделан по обеим девушкам
                all([not lisa.dcv.battle.stage, alice.dcv.battle.stage in [1, 4, 7]]),          # по Лизе путь не выбран, по Алисе выбрана настоящая дружба
                all([lisa.dcv.battle.stage in [1, 4], not alice.dcv.battle.stage]),             # по Алисе путь не выбран, по Лизе выбрана настоящая дружба
                ]):
            # настоящая дружба
            return (3, _("Настоящая дружба"))

        elif any([
                all([lisa.dcv.battle.stage in [3, 6], alice.dcv.battle.stage in [3, 6, 9]]),    # выбор сделан по обеим девушкам
                all([not lisa.dcv.battle.stage, alice.dcv.battle.stage in [3, 6, 9]]),          # по Лизе путь не выбран, по Алисе откровенная вражда
                all([lisa.dcv.battle.stage in [3, 6], not alice.dcv.battle.stage]),             # по Алисе путь не выбран, по Лизе откровенная вражда
                ]):
            # откровенная вражда
            pass
        else:
            # хотя бы по одной девушке Макс попытался схитрить
            return (2, _("Фальшивая дружба"))
