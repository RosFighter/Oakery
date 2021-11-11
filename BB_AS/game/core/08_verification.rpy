
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

        return rez


    # Оливия приходит на ночные посиделки
    def olivia_nightvisits():
        if 'olivia' not in chars:
            return 0

        rez = 0

        if  all([GetWeekday(day)==6, olivia.dcv.feature.stage>3, olivia.dcv.special.done, not olivia.dcv.special.stage]):
            # ночь с пятницы на субботу, состоялась беседа о ночных посиделках, ночных посиделок ещё не было
            rez = 1
        elif all([GetWeekday(day)==6, olivia.dcv.feature.stage>4, olivia.dcv.special.done]):
            # ночь с пятницы на субботу, состоялась беседа после первых ночных посиделках, прошел откат ночных посиделок
            rez = 2

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

            if flags.eric_wallet == 2:
                # 5 Эрик запустил кошелёк, девчонки смотрят кино без Макса
                return 5

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
            flags.lisa_sexed > 6,
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
            flags.lisa_sexed > 6,
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
