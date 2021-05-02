
init python:

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
        if any([day==4, day==11]):
            # первая и вторая субботы
            rez = True
        elif all([GetWeekday(day)==6, day>=11, flags.dinner==6]):
            # вторая суббота с Эриком (фикс пропущенных)
            rez = True
        elif all([GetWeekday(day)==6, poss['seduction'].stn in [14, 15], not lisa.dcv.battle.stage, lisa.dcv.battle.lost<7, ('sexbody1' not in alice.gifts or alice.dcv.battle.stage>3)]):
            # начинается битва за Лизу, битва за Алису еще не началась или уже результат определился
            rez = True
        elif all([GetWeekday(day)==6, lisa.dcv.battle.stage==2, lisa.dcv.intrusion.done]):
            # продолжение разговора о Лизе в случае отсрочки
            rez = True
        elif all([GetWeekday(day)==6, not alice.dcv.battle.stage, 'sexbody1' in alice.gifts, (not lisa.dcv.battle.stage or lisa.dcv.battle.stage>3)]):
            # начинается битва за Алису, битва за Лизу еще не началась или уже результат определился
            rez = True
        elif all([GetWeekday(day)==6, alice.dcv.battle.stage==2, alice.dcv.battle.enabled, alice.dcv.battle.done]):
            # продолжение разговора об Алисе в случае отсрочки
            rez = True
        elif all([GetWeekday(day)==6, 'sexbody2' in alice.gifts, 4<alice.dcv.intrusion.stage<7]):
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
            return False

        rez = False

        if all([GetWeekday(day)==3, olivia.dcv.feature.stage < 3]):
            # среда, первые две беседы с Оливией
            rez = True
        elif all([lisa.flags.crush>11, GetWeekday(day)==2, olivia.dcv.feature.stage>2]):
            # каждый вторник, больше двух бесед с Оливией
            rez = True
        elif  all([GetWeekday(day)==5, olivia.dcv.feature.stage<4]):
            # пятница, беседа о ночных посиделках ещё не состоялась
            rez = True
        elif  all([GetWeekday(day)==5, olivia.dcv.feature.stage>3, not olivia.dcv.special.done]):
            # пятница, состоялась беседа о ночных посиделках, не прошел откат ночных посиделок
            rez = True

        return rez


    # Оливия приходит на ночные посиделки
    def olivia_nightvisits():
        if 'olivia' not in chars:
            return False

        rez = False

        if  all([GetWeekday(day)==6, olivia.dcv.feature.stage>3, olivia.dcv.special.done]):
            # ночь с пятницы на субботу, состоялась беседа о ночных посиделках, прошел откат ночных посиделок
            rez = True

        return rez


    # список sub_lst входит в список lst
    def list_in_list(sub_lst, lst):
        return all(x in lst for x in sub_lst)
