
define clothes_dict = {
    'alice' : {
        'casual'    : [('a', '01a', 'Обычная одежда'), ('b', '01c', 'Пижама'), ('d', '01e', 'Открытая футболка и микро-шорты')],
        'sleep'     : [('a', '02', 'Белое бельё'), ('b', '02ia', 'Тёмное бельё')],
        'lingerie'  : [('a', '02', 'Белое бельё'), ('b', '02ia', 'Тёмное бельё'), ('c', '02ka', 'Чёрное боди'), ('d', '02la', 'Кружевное боди')],
        },
    'ann'   : {
        'casual'    : [('a', '01a', 'Обычная одежда'), ('b', '01b', 'Футболка'), ('d', '01e', 'Топ и шорты')],
        'sports'    : [('a', '05a', 'Спортивная форма'), ('c', '05c', 'Спортивные лиф и мини-шорты')],
        'cook_morn' : [('a', '05b', 'Спортивная форма + фартук'), ('b', '01c', 'Футболка + фартук'), ('c', '05d', 'Спортивные лиф и мини-шорты + фартук'), ('d', '01f', 'Топ и шорты + фартук')],
        'cook_eve'  : [('b', '01c', 'Футболка + фартук'), ('d', '01f', 'Топ и шорты + фартук')],
        'rest_morn' : [('a', '01b', 'Футболка'), ('d', '01e', 'Топ и шорты')],
        'rest_eve'  : [('a', '01b', 'Футболка'), ('b', '04b', 'Полотенце'), ('d', '01e', 'Топ и шорты')],
        'sleep'     : [('a', '02', 'Чёрное бельё'), ('b', '02f', 'Ночнушка')],
        },
    'eric'  : {
        'casual'    : [('a', '01a', 'Майка и джинсы'), ('b', '01b', 'Рубашка и шорты')],
        },
    'lisa'  : {
        'casual'    : [('a', '01a', 'Обычная одежда'), ('b', '04', 'Халатик'), ('d', '01c', 'Розовые топик и юбочка')],
        'sleep'     : [('a', '02', 'Маечка и штаны'), ('b', '02a', 'Маечка и трусики'), ('c', '02c', 'Трусики')],
        'swimsuit'  : [('a', '03', 'Закрытый купальник'), ('b', '03b', 'Красное бикини')],
        'learn'     : [('a', '01a', 'Обычная одежда'), ('b', '04', 'Халатик'), ('c', '04b', 'Полотенце'), ('d', '01c', 'Розовые топик и юбочка'), ('h', '01ba', 'Школьная форма')],
        'weekend'   : [('w', '01e', 'Платье с пиджаком'), ('w1', '01ea', 'Платье')],
        },
    'mgg'   : {
        'casual'    : [('a', '01a', 'Обычная одежда'), ('b', '01b', 'Майка и шорты'), ('c', '01c', 'Шорты')],
        },
    }

init python:

    # Проверяет необходимоть смены текущей одежды
    def ChoiceClothes():
        global cur_shed
        mgg.dress = mgg.clothes.casual.GetCur().suf

        if all([GetWeekday(day)==6, day>=11, flags.dinner==6]):
            ann.clothes.casual.GetCur().suf = 'a'

        for char in chars:

            prev_shed = chars[char].get_plan(prevday, prevtime)
            # print 'ChoiceClothes', char, prev_shed.name, chars[char].plan_name, tm, prevtime
            if (prev_shed is None and chars[char].plan_name) or (chars[char].plan_name is not None and prev_shed.name!=chars[char].plan_name): # начато новое действие, значит меняем одежду

                # удалим флаг подсматривания за персонажем через камеры при смене текущего действия
                for cur_act in cam_flag:
                    if cur_act.split('_')[0] == char:
                        cam_flag.remove(cur_act)

                # удалим признак просмотра неактивной камеры
                if chars[char].loc:
                    i = 0
                    for cam in chars[char].loc.cams:
                        if chars[char].loc.id+'-'+str(i) in cam_flag:
                            cam_flag.remove(chars[char].loc.id+'-'+str(i))
                        i += 1

                if char == 'alice' and alice.daily.oiled in [1, 2]:  # Если Алису уже намазали кремом, повторное намазываение невозможно
                    alice.daily.oiled = 3

                if char in ['ann', 'eric'] and 'ann_eric_scene' in globals():
                    ann_eric_scene = '' # обнулим сцену для камер, если она есть

                dress, inf, clot = GetDressNps(char, chars[char].plan_name)
                if dress != '':
                    chars[char].dress = dress
                if inf != '':
                    chars[char].dress_inf = inf


    # устанавливает текущую одежду согласно расписанию (в том числе для инфо)
    def ClothingNps(char, name):
        dress, inf, clot = GetDressNps(char, name)
        if dress != '':
            chars[char].dress = dress
            # print('%s - %s : %s'%(char, clot, dress))
        if inf != '':
            chars[char].dress_inf = inf
        return


    # возвращает одежду персонажа char для действия name
    def GetDressNps(char, name):
        dress, inf, clot = '', '', ''
        if name=='dressed':
            inf = '00b'

        elif char=='lisa':
            if name in ['sleep', 'sleep2']:
                clot  = 'sleep'
                dress = lisa.clothes.sleep.GetCur().suf
                inf   = lisa.clothes.sleep.GetCur().info
                if all([olivia_night_visits, lisa.flags.kiss_breast, lisa.sleeptoples]):
                    dress = 'c'
                    inf   = '02c'
            elif name == 'tv2':
                dress = 'c' if lisa_will_be_topless() > 0 else 'b'
                inf = '02c' if lisa_will_be_topless() > 0 else '02a'
            elif name in ['breakfast', 'dinner', 'dishes', 'practice']:
                dress = lisa.clothes.casual.GetCur().suf
                inf   = lisa.clothes.casual.GetCur().info
                clot  = 'casual'
            elif name == 'phone':
                if '11:00' > tm > '10:00':
                    dress = 'o'
                    inf = '01aa'
                else:
                    dress = lisa.clothes.casual.GetCur().suf
                    inf   = lisa.clothes.casual.GetCur().info
                    clot  = 'casual'
            elif name == 'read':
                if tm < '08:00':
                    dress   = {'a':'p', 'b':'p1', 'c':'p2'}[lisa.clothes.sleep.GetCur().suf]
                    inf     = lisa.clothes.sleep.GetCur().info
                    clot    = 'sleep'
                elif 'bikini' in lisa.gifts and '19:00' > tm >= '13:00':
                    dress   = 's'
                    inf     = lisa.clothes.swimsuit.GetCur().info
                    clot    = 'swimsuit'
                else:
                    dress = lisa.clothes.casual.GetCur().suf
                    inf   = lisa.clothes.casual.GetCur().info
                    clot  = 'casual'
            elif name in ['shower', 'bath']:
                inf = '04a'
            elif name == 'repeats':
                dress = 'h' #lisa.clothes.learn[4].suf
                inf = '01ba' #lisa.clothes.learn[4].info
            elif name == 'at_tutor':
                dress = lisa.clothes.weekend.GetCur().suf
                inf   = lisa.clothes.weekend.GetCur().info
            elif name == 'in_shcool':
                inf = '01b'
            elif name in ['sun', 'swim']:
                dress = lisa.clothes.swimsuit.GetCur().suf
                inf   = lisa.clothes.swimsuit.GetCur().info
                clot  = 'swimsuit'
                if name == 'swim' and pose3_1 == '03':
                    inf += 'w'
            elif name in ['in_shop', 'at_tutor']:
                inf = '01'
            elif name == 'homework':
                # ставим текщущую одежды соотвестсвенно гардеробу
                if not lisa.clothes.learn.cur and lisa.GetMood()[0]>2:
                    dress = lisa.clothes.learn.sel[2].suf
                    inf   = lisa.clothes.learn.sel[2].info
                else:
                    dress = lisa.clothes.learn.GetCur().suf
                    inf   = lisa.clothes.learn.GetCur().info
                clot  = 'learn'

        elif char=='alice':
            dress = alice.clothes.casual.GetCur().suf
            inf   = alice.clothes.casual.GetCur().info
            if alice.req.result=='nojeans' and dress!='a':
                # если есть требование не носить джинсы, но установлена другая одежда - отменяем требование
                alice.req.reset()
            elif alice.req.result=='nopants' and dress!='a':
                # если есть требование не носить трусы под джинсами, но установлена другая одежда - также отменяем требование
                alice.req.reset()
            elif all([dress=='a', alice.req.result=='nojeans', not check_is_home('ann')]):
                dress = 'c'
                inf   = '02e'

            if name == 'sleep':
                dress = alice.clothes.sleep.GetCur().suf
                inf   = alice.clothes.sleep.GetCur().info
                if alice.req.result == 'sleep':
                    alice.sleeptoples = True
                    dress += 'a'
                    inf = {'a':'02ga', 'b':'02ja'}[alice.clothes.sleep.GetCur().suf]
                elif alice.req.result == 'naked':
                    alice.sleepnaked = True
                    dress = ''
                    inf = '00a'
            elif name in ['shower', 'bath']:
                inf = '04aa'
            elif name in ['read', 'breakfast', 'dinner', 'dishes']:
                clot = 'casual'
            elif name in ['resting', 'tv']:
                clot = 'casual'
                if not ('09:00' <= tm < '20:00'):
                    inf += 'a'
            elif name == 'blog':
                if (GetWeekday(day) in [1, 4, 5] and all(['black_linderie' in alice.gifts, poss['blog'].st()>4, alice.dcv.feature.done])
                    or (GetWeekday(day)==3 and alice.dcv.intrusion.enabled)):
                    # блог в нижнем белье
                    clot = 'lingerie'
                    dress = alice.clothes.lingerie.GetCur().suf
                    inf   = alice.clothes.lingerie.GetCur().info
                else:
                    # блог в обычной одежде
                    clot = 'casual'
                    if not ('09:00' <= tm < '20:00'):
                        inf += 'a'
            elif name == 'sun':
                dress = 'a'
                inf   = '03'
            elif name == 'swim':
                dress = 'a'
                inf = '03a' if pose3_2 == '03' else '03'
            elif name in ['in_shop', 'at_friends']:
                inf = '01'
            elif name == 'cooking':
                inf  = {'a' : '01b', 'b' : '01d', 'c' : '01g', 'd' : '01f'}[dress]
                clot = 'casual'
            elif name == 'smoke':
                dress = 'b' if alice.req.result == 'toples' else 'a'
                inf   = '03b' if alice.req.result == 'toples' else '03'
            elif name == 'club':
                dress = 'a'
                inf   = '06'

        elif char=='ann':
            if name == 'sleep':
                dress = ann.clothes.sleep.GetCur().suf
                inf   = ann.clothes.sleep.GetCur().info
                clot  = 'sleep'
            elif name == 'sleep2':
                dress = 'n'
                inf = '00'
            elif name in ['shower', 'bath', 'shower2']:
                inf = '04a'
            elif name == 'yoga':
                dress = ann.clothes.sports.GetCur().suf
                inf   = ann.clothes.sports.GetCur().info
            elif name == 'cooking':
                if tm < '12:00':
                    if ann.clothes.cook_morn.cur in [0, 2]:
                        ann.clothes.cook_morn.cur = 2 if ann.clothes.sports.cur > 0 else 0
                    dress = ann.clothes.cook_morn.GetCur().suf
                    inf   = ann.clothes.cook_morn.GetCur().info
                    clot  = 'cook_morn'
                else:
                    dress = ann.clothes.cook_eve.GetCur().suf
                    inf   = ann.clothes.cook_eve.GetCur().info
                    clot  = 'cook_eve'
            elif name == 'breakfast':
                dress = ann.clothes.cook_morn.GetCur().suf
                inf   = {'a':'05a', 'b':'01b', 'd':'01e', 'c':'05с'}[ann.clothes.cook_morn.GetCur().suf]
                clot  = 'cook_morn'
            elif name == 'resting':
                if tm <= '12:00':
                    dress = ann.clothes.rest_morn.GetCur().suf
                    inf   = ann.clothes.rest_morn.GetCur().info
                    clot  = 'rest_morn'
                elif tm <= '19:00':
                    dress = 'b' # купальник
                    inf   = '03'
                    clot  = 'купальник'
                else: # футболка или полотенце
                    dress = ann.clothes.rest_eve.GetCur().suf
                    inf   = ann.clothes.rest_eve.GetCur().info
                    clot  = 'rest_eve'
            elif name == 'at_work':
                inf = '01a'
            elif name == 'in_shop':
                inf = '01'
            elif name == 'read':
                dress = ann.clothes.rest_morn.GetCur().suf if tm < '14:00' else 'b'
                inf   = ann.clothes.rest_morn.GetCur().info if tm < '14:00' else '03'
                clot  = 'rest_morn' if tm < '14:00' else 'купальник'
            elif name == 'sun':
                inf = '03'
            elif name == 'swim':
                inf = '03a'
            elif name == 'dinner':
                dress = ann.clothes.casual.GetCur().suf
                inf   = ann.clothes.casual.GetCur().info
                clot  = 'casual'
            elif name in ['tv','tv2']:
                inf = '04b'
            elif name == 'fuck':
                inf = '00b'
            else:
                dress = 'a'
                inf   = '01a'
                clot  = 'else'

        elif char=='eric':
            if name in ['dinner', 'rest', 'tv2', 'shat', 'sleep', 'practice', 'sexed_lisa']:
                dress = 'b' if day % 2 else 'a'
                inf = '01a' if dress == 'a' else '01b'
                clot = 'повседневка'
            elif name in ['fuck', 'sleep2']:
                inf = '00a'
            elif name == 'shower2':
                inf = '00b'
            else:
                inf  = '01'
                clot = 'else'

        elif char=='kira':
            dress = 'a'
            if name in ['swim', 'sun']:
                inf = '03w' if pose3_4 == '03' and name == 'swim' else '03'
            elif name == 'sleep':
                if kira.sleepnaked and GetWeekday(day)==6:
                    dress = 'b'
                inf = '00' if kira.sleepnaked and GetWeekday(day)==6 else '02'
            elif name == 'night_tv':
                inf = '02'
            elif name == 'studio':
                inf = '01b'
            elif name in ['bath', 'shower']:
                inf = '04a'
            elif name == 'night_swim':
                inf = '00a'
            elif name == 'club':
                dress = 'a'
                inf   = '06'

        elif char=='olivia':
            dress = random_loc_ab

            if name in ['sleep2', 'sleep', 'at_home']:
                inf = '00'
            elif name == 'in_shcool':
                inf = '01'
            elif name == 'sun':
                inf = '00' if olivia.dcv.other.stage else '03'
                dress = 'b' if olivia.dcv.other.stage else 'a'
            elif name == 'swim':
                if pose3_3=='01':
                    inf = '00' if olivia.dcv.other.stage else '03'
                else:
                    inf = '00a' if olivia.dcv.other.stage else '03a'

        # print("%s %s clot - %s, dress - %s ( %s )"%(char, name, clot, dress, inf))
        return dress, inf, clot


    # проверка одежды персонажей на соответствие словарю
    def checking_clothes():
        for char_id in clothes_dict:
            if char_id == 'mgg':
                char = mgg
            elif char_id in chars:
                char = chars[char_id]
            else:
                continue

            for clot_type in clothes_dict[char_id]:
                clots = getattr(char.clothes, clot_type)
                # print clots
                if clots is None:
                    add_new_clot_type(clots, clot_type, char_id)
                else:
                    check_extend_clot_type(clots, clot_type, char_id)

        setting_clothes_by_conditions()

        for char_id in clothes_dict:
            if char_id == 'mgg':
                char = mgg
            elif char_id in chars:
                char = chars[char_id]
            else:
                continue
            for clot_type in clothes_dict[char_id]:
                clots = getattr(char.clothes, clot_type)
                if not (clots.sel[clots.cur].rand or clots.sel[clots.cur].change):
                    # установленная одежда недопустима
                    clots.SetRand(True)     # принудительная установка допустимой случайной одежды
                    plan = chars[char_id].get_plan()
                    ClothingNps(char_id, plan.name) # установка текущей одежды


    # проверяет и при необходимости переименовывает одежду перосонажа
    def renamed_clothes():
        for char_id in clothes_dict:
            if char_id == 'mgg':
                char = mgg
            elif char_id in chars:
                char = chars[char_id]
            else:
                continue

            for clot_type in clothes_dict[char_id]:
                clots = getattr(char.clothes, clot_type)
                for k in range(len(clothes_dict[char_id][clot_type])):
                    clot = clothes_dict[char_id][clot_type][k]
                    if clots.sel[k].name != clot[2]:
                        clots.sel[k].name = clot[2]


    # добавляет новую одежду для персонажа
    def add_new_clot_type(clots, clot_type, char_id):
        clot_name = {
                'casual'    : _("Повседневная"),
                'sleep'     : _("Для сна"),
                'sports'    : _("Для йоги"),
                'lingerie'  : _("Блог в нижнем белье"),
                'cook_morn' : _("Готовит завтрак"),
                'cook_eve'  : _("Готовит ужин"),
                'rest_morn' : _("Утренний отдых"),
                'rest_eve'  : _("Вечерний отдых"),
                'swimsuit'  : _("Купальник"),
                'learn'     : _("За уроками"),
                'weekend'   : _("Для прогулок"),
            }[clot_type]

        clot_list = []
        for clot in clothes_dict[char_id][clot_type]:
            clot_list.append(Garb(clot[0], clot[1], clot[2]))

        if char_id != 'mgg':
            setattr(chars[char_id].clothes, clot_type, Clothes(clot_name, clot_list))
            clots = getattr(chars[char_id].clothes, clot_type)
        else:
            setattr(mgg.clothes, clot_type, Clothes(clot_name, clot_list))
            clots = getattr(mgg.clothes, clot_type)

        # теперь нужно активировать одежду "по умолчанию"
        # 'тип_одежды' : (доступна вручную, номер либо список/кортеж номеров одежды)
        def_list = {
                'casual'    : (False, (0, 1) if char_id in ['ann', 'eric'] else 0),
                'sleep'     : (True,  0),
                'sports'    : (True, 0),
                'lingerie'  : (True,  0),
                'cook_morn' : (False, (0, 1)),
                'cook_eve'  : (False, (0, 1)),
                'rest_morn' : (False, 0),
                'rest_eve'  : (False, (0, 1)),
                'swimsuit'  : (False, 0),
                'learn'     : (False, (0, 2)),
                'weekend'   : (False, (0, 1))
            }[clot_type]

        if def_list[0]:
            clots.enable(def_list[1], 0)
        else:
            clots.rand_enable(def_list[1])


    # проверяет список одежды персонажа
    def check_extend_clot_type(clots, clot_type, char_id):
        for k in range(len(clothes_dict[char_id][clot_type])):
            clot = clothes_dict[char_id][clot_type][k]

            if k < len(clots.sel):
                # пропущенное вставляем
                if clot[0] < clots.sel[k].suf:
                    clots.sel.insert(k, Garb(clot[0], clot[1], clot[2]))
            else:
                # добавляем новые
                clots.sel.append(Garb(clot[0], clot[1], clot[2]))


    # устанавливает допустимую/открытую одежду всем персонажам согласно условиям
    def setting_clothes_by_conditions():
        # Алиса
        alice.clothes.sleep.enable(0)       # обычное бельё для сна доступно всегда
        alice.clothes.casual.enable(0)      # джинсы доступны всегда
        if 'pajamas' in alice.gifts:        # подарена пижамка
            alice.clothes.casual.enable(1)
        if 'kira' in chars:                 # приехала Кира
            alice.clothes.casual.enable(2)
        if 'black_linderie' in alice.gifts: # подарено тёмное бельё для блога
            alice.clothes.sleep.enable(1)
            alice.clothes.lingerie.rand_enable((0, 1))
        if 'sexbody1' in alice.gifts:       # подарено боди
            alice.clothes.lingerie.rand_enable(2)
        if 'sexbody2' in alice.gifts:       # подарено кружевное боди
            # открываем доступ к смене одежды
            alice.clothes.lingerie.enable((0, 1, 2, 3))
            # но при этом ставим условие
            alice.clothes.lingerie.set_condition("infl[alice].balance[2]=='m' and infl[alice].m[1]>=35", _("Влияние Макса недостаточно"))

        # Анна
        ann.clothes.sleep.enable(0)         # обычное бельё для сна доступно всегда
        ann.clothes.casual.rand_enable((0, 1))
        ann.clothes.cook_morn.rand_enable((0, 1))
        ann.clothes.cook_eve.rand_enable(0)
        ann.clothes.rest_morn.rand_enable(0)
        ann.clothes.rest_eve.rand_enable((0, 1))
        ann.clothes.sports.enable(0)
        if 'kira' in chars:
            ann.clothes.casual.rand_enable(2)
            ann.clothes.cook_morn.rand_enable(3)
            ann.clothes.cook_eve.rand_enable(1)
            ann.clothes.rest_morn.rand_enable(1)
            ann.clothes.rest_eve.rand_enable(2)
        if 'nightie' in ann.gifts:          # подарена ночнушка
            ann.clothes.sleep.enable(1)
        if 'fit1' in ann.gifts:             # подарены Спортивные лиф и мини-шорты
            ann.clothes.sports.enable(1)

        # Лиза
        lisa.clothes.learn.enable(2)        # полотенце доступно всегда
        lisa.clothes.learn.disable(4)       # школьная форма никогда недоступна (только событием)
        lisa.clothes.weekend.rand_enable((0, 1))

        if 'bikini' in lisa.gifts:          # подарен купальник
            lisa.clothes.swimsuit.enable(1)
            lisa.clothes.swimsuit.disable(0)
        else:
            lisa.clothes.swimsuit.enable(0)
            lisa.clothes.swimsuit.disable(1)
        if 'bathrobe' in lisa.gifts:        # подарен халатик
            lisa.clothes.casual.enable(1)
            lisa.clothes.learn.enable(1)
        else:
            lisa.clothes.casual.disable(1)
            lisa.clothes.learn.disable(1)
        if 'kira' in chars:                 # приехала Кира
            lisa.clothes.casual.enable(2)
            lisa.clothes.casual.disable(0)
            lisa.clothes.learn.enable(3)
            lisa.clothes.learn.disable(0)
        else:
            lisa.clothes.casual.rand_enable(0)
            lisa.clothes.casual.disable(2)
            lisa.clothes.learn.rand_enable(0)
            lisa.clothes.learn.disable(3)
        if 'poss' in globals() and poss['sg'].st() not in [-1, 0, 1, 2, 4]:
            lisa.clothes.sleep.enable(1)
            lisa.clothes.sleep.disable(0)
        else:
            lisa.clothes.sleep.enable(0)
            lisa.clothes.sleep.disable(1)

        # Макс
        if items['max-a'].have:             # куплены шорты с майкой
            mgg.clothes.casual.enable(1)
        if 'kira' in chars:                 # приехала Кира
            mgg.clothes.casual.enable(2)
            mgg.clothes.casual.disable(0)
        else:
            mgg.clothes.casual.enable(0)
            mgg.clothes.casual.disable(2)


    # возвращает вариант одежды Лизы для переодеваний
    def get_lisa_dress_pose(vr, pose=''):
        var = {'boobs': False, 'ass':False, 'np':False, 'fin':False}
        lvl = get_lisa_emancipation()
        if vr == 0:
            # нулевой момент
            if lisa.prev_plan in ['shower', 'bath']:                # после душа/ванной
                pose = '00g'                                    # полотенце
                lisa.dress_inf = '04b'
            elif lisa.prev_plan == 'in_shop':                       # после шопинга
                pose = '00o'                                    # для шопинга
                lisa.dress_inf = '01aa'
            elif lisa.prev_plan == 'at_tutor':                      # после прогулки/репетитора
                pose = '00' +lisa.clothes.weekend.GetCur().suf  # платье
                lisa.dress_inf = lisa.clothes.weekend.GetCur().info
            elif lisa.prev_plan in ['in_shcool', 'on_courses']:     # после школы
                pose = '00h'                                    # школьная форма
                lisa.dress_inf = '01ba'
            elif lisa.prev_plan in ['sun', 'swim']:                 # после отдыха во дворе, если нет бикини
                pose = '00s0' if lisa.clothes.swimsuit.GetCur().suf == 'a' else '00s1'
                lisa.dress_inf = lisa.clothes.swimsuit.GetCur().info
            elif lisa.plan_name in ['dressed', 'read', 'dishes']:   # после чтения, мытья посуды или одевается "на выход" (в школу, магазин или к репетитору)
                if lvl > 1 and '11:00' > tm > '10:00':
                    pose = '07f1' if weekday == 6 else '07e3'
                    lisa.dress_inf = '02i' if weekday == 6 else '02h'
                    var['fin'] = True
                else:
                    pose = '00'+lisa.clothes.casual.GetCur().suf    # повседневка
                    lisa.dress_inf = lisa.clothes.casual.GetCur().info
            elif lisa.prev_plan == 'homework':                      # перед сном
                pose = '00'+('g' if lisa.prev_dress == 'c' else lisa.prev_dress)
            elif lisa.prev_plan == 'phone':
                pose = '00' + lisa.prev_dress
            return pose, var

        if not pose:
            # сгенерируем позу для "повезло"
            lst = []
            if lvl > 2:                                 # голая
                lst.extend(['01', '04'])

            if lisa.plan_name in ['sun', 'swim'] and 'bikini' in lisa.gifts:       # бикини
                lst.extend(['01c1', '04c1'])
                if lvl > 1:
                    lst.extend(['01c', '04c'])
            elif lisa.prev_plan in ['shower', 'bath']:  # полотенце
                lst.extend(['01g1', '04g1'])
                if lvl > 2:
                    lst.extend(['01g', '04g'])
            else:                                       # нижнее бельё
                lst.extend(['01h', '04h'])              # трусики
                # if lvl < 2:
                #     lst.extend(['01h2', '04h2'])        # маечка с трусиками
                # elif lvl > 2:
                #     lst.extend(['01h1', '04h1'])        # маечка без трусиков


            if lisa.plan_name == 'dressed':
                if not GetWeekday(day):
                    # воскресенье, прогулка/репетитор
                    lst.extend(['01w', '04w'])
                elif GetWeekday(day) == 6:
                    # суббота, шопинг
                    lst.extend(['01a', '01f1', '04a', '04f1'])
                    if lvl > 2:
                        lst.extend(['01f', '04f'])
                else:
                    # будни, в школу
                    lst.extend(['01e1', '01e3', '04e1', '04e3'])
                    if lvl > 2:
                        lst.extend(['01e', '01e2', '04e', '04e2'])
            elif lisa.plan_name in ['read', 'phone', 'homework']:
                if lisa.clothes.casual.GetCur().suf == 'a':
                    lst.extend(['01a', '04a'])
                elif lisa.clothes.casual.GetCur().suf == 'b':
                    lst.append('01b1')
                    if lvl > 2:
                        lst.append('01b')
                else:   # lisa.clothes.casual.GetCur().suf == 'd'
                    lst.extend(['01d1', '01d2', '04d1', '04d2'])
                    if lvl > 2:
                        lst.extend(['01d', '04d'])

            pose = renpy.random.choice(lst)

        if vr < 2:
            if lvl == 1 and pose in ['01b1', '01d1', '01h', '01g1',
                        '04d1', '04h', '04g1', '01e1', '01e3',
                        '04e1', '04e3', '01f1']:
                pose = {
                    '01h':'03h', '04h':'06h',       # трусики
                    '01g1':'03g1', '04g1':'06g1',   # трусики с полотенцем
                    '01b1':'03b1',                  # халат
                    '01d1':'03d', '04d1':'06d',     # розовый
                    '01e1':'03e', '01e3':'08e3',    # школьная лицом
                    '04e1':'06e', '04e3':'08e3',    # школьная спиной
                    '01f1':'08f1', '04f1':'08f1'    # для шопинга
                    }[pose]
            else:
                pose = {
                    '01':'03', '04':'06',           # голая
                    '01c1':'02c1', '04c1':'05c1', '01c':'03c', '04c':'06c',     # бикини
                    '01w':'02w', '04w':'06w',       # платье
                    '01h':'02h', '04h':'05h',       # трусики
                    '01h1':'08h1', '04h1':'08h1',   # маечка
                    '01h2':'08h2', '04h2':'08h2',   # маечка и трусики
                    '01f':'08f', '01f1':'07f1',  '04f':'08f', '04f1':'08f1',    # для шопинга
                    '01a':'02a', '04a':'05a',       # базовая повседневка
                    '01e':'03e', '01e1':'02e1', '01e2':'08e2', '01e3':'07e3',   # школьная лицом
                    '04e':'06e', '04e1':'05e1', '04e2':'08e2', '04e3':'07e3',   # школьная спиной
                    '01b':'03b', '01b1':'02b1',     # халат
                    '01d':'03d', '01d1':'02d1', '01d2':'02d2',                  # розовый лицом
                    '04d':'06d', '04d1':'05d1', '04d2':'05d2',                  # розовый спиной
                    '01g':'03g', '01g1':'02g1', '04g':'06g', '04g1':'05g1',     # с полотенцем
                    }[pose]

        var['np']       = pose in ['01', '01b', '01d', '01e', '01e2', '01f',
                                   '01g', '01h1', '03', '03b', '03g', '04',
                                   '04d', '04e', '04e2', '04f', '04g', '04h1',
                                   '04w', '06', '06g', '08e2', '08f', '08h1']

        var['ass']      = pose in ['06h', '06g1', '06c', '06', '05h', '05g1',
                                   '04w', '04h', '04g1', '04g', '04f1', '04f',
                                   '04e3', '04e2', '04e1', '04e', '04d1', '04d',
                                   '04c1', '04c', '04', '04h1', '04h2']

        var['boobs']    = pose in ['06w', '06h', '06g1', '06e', '06d', '06c',
                                   '06', '05h', '05g1', '05e1', '05d2', '05d1',
                                   '05c1', '05a', '04w', '04h', '04g1', '04g',
                                   '04e1', '04e', '04d2', '04d1', '04d', '04c1',
                                   '04c', '04a', '04', '03h', '03g1', '03g',
                                   '03e', '03d', '03c', '03b1', '03b', '03',
                                   '02w', '02h', '02g1', '02e1', '02d2', '02d1',
                                   '02c1', '02b1', '02a', '01w', '01h', '01g1',
                                   '01g', '01e1', '01e', '01d2', '01d1', '01d',
                                   '01c1', '01c', '01b1', '01a', '01']

        var['fin']      = pose in ['07e3', '07f1', '08e3', '08f1', '01f1', '01e3']

        if pose in ['01', '03', '04', '06']:
            lisa.dress_inf = '00'   # голая
        elif pose in ['01h', '02h', '03h', '04h', '05h', '06h']:
            lisa.dress_inf = '02c'  # трусики
        elif pose in ['01h1', '04h1', '08h1']:
            lisa.dress_inf = '02b'  # маечка
        elif pose in ['01h2', '04h2', '08h2']:
            lisa.dress_inf = '02a'  # маечка и трусики
        elif pose in ['01a', '02a', '04a', '05a']:
            lisa.dress_inf = '02g'  # штаны
        elif pose in ['01e', '01e1', '02e1', '03e', '04e', '04e1', '05e1', '06e']:
            lisa.dress_inf = '02e'  # школьная юбка
        elif pose in ['01e2', '04e2', '08e2']:
            lisa.dress_inf = '02d'  # школьная рубашка
        elif pose in ['01e3', '04e3', '07e3', '08e3']:
            lisa.dress_inf = '02h'  # школьная рубашка и трусики
        elif pose in ['01f', '04f', '08f']:
            lisa.dress_inf = '02f'  # выходной верх
        elif pose in ['01f1', '04f1', '07f1', '08f1']:
            lisa.dress_inf = '02i'  # выходной верх + трусики
        elif pose in ['01w', '02w', '04w', '06w']:
            lisa.dress_inf = '01ea' # платье

        if pose:
            # print vr, lvl, lisa.prev_dress, lisa.plan_name, pose
            return pose, var
        else:
            # print 'bag:', pose, lst, lvl, tm, weekday, lisa.prev_plan, lisa.plan_name
            return '02h', var

    # возвращает вариант одежды Лизы для переодеваний при Максе
    def get_lisa_dress_inroom(vr, no_naked=0):
        lvl = get_lisa_emancipation()

        lst = []
        lst.append('01h')       # трусики для всех вариантов действий
        if lvl == 1 and lisa.plan_name == 'sleep':
            lst.append('01h3')  # пижама для первого уровня

        if lisa.prev_plan == 'in_shcool':
            lst.append('01e')   # школьная юбка после школы

        if lisa.plan_name in ['swim', 'sun'] or lisa.prev_plan in ['swim', 'sun']:
            lst.append('01c')   # трусики от бикини перед или после отдыха во дворе

        if lisa.prev_plan not in ['in_shcool', 'in_shop', 'at_tutor', 'homework', 'on_courses']:
            lst.append({'a':'01a', 'b':'01b1', 'd':'01d'}[lisa.clothes.casual.GetCur().suf])
            if lisa.clothes.casual.GetCur().suf == 'b' and lvl > 2:
                lst.append('01b')
        elif all([lisa.prev_plan == 'homework', lisa.clothes.learn.GetCur().suf != 'c']):
            lst.append({'a':'01a', 'b':'01b1', 'd':'01d'}[lisa.clothes.learn.GetCur().suf])
            if lisa.clothes.learn.GetCur().suf == 'b' and lvl > 2:
                lst.append('01b')

        elif lisa.prev_plan == 'in_shop':
            lst.append('01a')

        if all([lvl > 2, lisa.plan_name != 'sleep', lisa.prev_plan != 'dishes', not no_naked]):
            lst.append('01')

        pose = renpy.random.choice(lst)
        # print pose, lst

        if not vr:  # подсмотреть не удалось
            if lvl == 1:
                pose = {
                    '01a':'05a',
                    '01b1':'03b1',
                    '01c':'06c',
                    '01d':'05d1',
                    '01e':'05e1',
                    '01h':'06h',
                    '01h3':renpy.random.choice(['02h3', '05h3']),
                    }[pose]
            elif lvl == 2:
                pose = {
                    '01a':renpy.random.choice(['02a', '05a']),
                    '01b1':'02b1',
                    '01c':'03c',
                    '01d':'02d1',
                    '01e':'02e1',
                    '01h':'02h',
                    }[pose]
            else:   #lvl == 3
                pose = {
                    '01':renpy.random.choice(['03', '06']),
                    '01a':renpy.random.choice(['02a', '05a']),
                    '01b':'03b',
                    '01b1':'02b1',
                    '01c':renpy.random.choice(['03c', '06c']),
                    '01d':renpy.random.choice(['02d1', '05d1']),
                    '01e':renpy.random.choice(['02e1', '05e1']),
                    '01h':renpy.random.choice(['02h', '05h']),
                    }[pose]
        # print pose
        return pose


    # возвращает вариант одежды Оливии для переодеваний
    def get_olivia_dress_pose(vr, pose=''):
        if vr == 0:
            if 6 > weekday > 0:
                return '00h'                                # школьная форма
            else:
                return 'a' if random_loc_ab == 'a' else '00b' # выходная одёжка

        if not pose:
            # сгенерируем позу для "повезло"
            lst = []
            if 6 > weekday > 0:
                lst.extend(['01e', '04e'])      # школьная форма (юбка)
                lst.extend(['01e2', '04e2'])    # школьная форма (верх)
            elif random_loc_ab == 'a':
                lst.extend(['01a', '04a'])
                lst.extend(['01a2', '04a2'])
            else:
                lst.extend(['01b', '04b'])
                lst.extend(['01b2', '04b2'])

            if olivia.dcv.other.stage:
                # Оливия загорает голой
                lst.extend(['01', '04'])
            else:
                # Оливия загорает в купальнике
                lst.extend(['01c', '04c'])

            pose = renpy.random.choice(lst)

        if vr < 2:
            pose = {'01e':'07e', '04e':'07e', '01e2':'07e2', '04e2':'07e2',
            '01':'07', '04':'07', '01c':'07c', '04c':'07c',
            '01a':'07a', '04a':'07a', '01a2':'07a2', '04a2':'07a2',
            '01b':'07b', '04b':'07b', '01b2':'07b2', '04b2':'07b2',}[pose]

        return pose

    # возвращает вариант одежды Оливии для переодеваний при Максе
    def get_olivia_dress_inroom(vr):
        if 6 > weekday > 0:
            lst = ['01e', '01e2']
        else:
            lst = ['01a', '01a2'] if random_loc_ab == 'a' else ['01b', '01b2']

        if olivia.dcv.other.stage:
            lst.append('01')
        else:
            lst.append('01c')

        pose = renpy.random.choice(lst)
        if not vr:  # подсмотреть не удалось
            pose = {
                '01e':'02e', '01e2':'02e2', '01':'02', '01c':'02c',
                '01a':'02a', '01a2':'02a2','01b':'02b', '01b2':'02b2',
                }[pose]

        return pose


    # возвращает вариант одежды Анны для переодеваний
    def get_ann_dress_pose(vr, pose='', balcony=False):
        lvl = get_ann_emancipation()

        if vr == 0:
            # нулевой момент
            if ann.prev_plan in ['shower', 'shower2']:      # после душа
                pose = renpy.random.choice(['07b2', '07b']) if lvl > 1 else '07b'
                ann.dress_inf = '04'                        # халат / чуть распахнутый халат
            elif ann.prev_plan == 'yoga':                   # после йоги
                pose = '07h' if ann.clothes.sports.GetCur().suf == 'a' else '07i'       # спортивка
                ann.dress_inf = ann.clothes.sports.GetCur().info
            elif ann.prev_plan == 'breakfast':
                pose = '07'+{'a':'h', 'b':'f', 'c':'i', 'd':'e'}[ann.clothes.cook_morn.GetCur().suf]
                ann.dress_inf = {'a':'05a', 'b':'01b', 'd':'01e', 'c':'05с'}[ann.clothes.cook_morn.GetCur().suf]
            elif ann.prev_plan == 'in_shop':
                pose = '07j'
                ann.dress_inf = '01'
            elif ann.prev_plan in ['resting', 'read'] and tm[:2] == '14':
                pose = '07f' if ann.clothes.rest_morn.GetCur().suf == 'a' else '07e'
                ann.dress_inf = ann.clothes.rest_morn.GetCur().info
            elif ann.prev_plan in ['sun', 'swim']:
                pose = '07d'
                ann.dress_inf = '03'
            elif ann.prev_plan == 'tv':
                pose = '07g'
                ann.dress_inf = '04b'
            return pose

        if not pose:
            # сгенерируем позу для "повезло"
            lst = []
            # предыдущая одежда
            if balcony:
                lst.extend(['01c2', '04c2'])
                if lvl > 1:
                    lst.extend(['01', '04'])
            elif ann.prev_plan in ['shower', 'shower2']:      # после душа
                lst.append('01b1')                      # халат + трусики
                if lvl > 1:
                    lst.append('01b')                   # халат без трусиков
            elif ann.prev_plan == 'yoga':                   # после йоги
                if ann.clothes.sports.cur:
                    lst.extend(['01i1', '04i1'])        # низ новой спортики
                else:
                    lst.extend(['01h1', '04h1'])        # низ спортики
            elif ann.prev_plan in ['sun', 'swim']:          # после бассейна
                lst.extend(['01d2', '04d2'])            # низ купальника
            elif ann.prev_plan == 'breakfast':              # после завтрака
                lst.extend({
                    'a': ['01h1', '04h1'],              # низ спортики
                    'b': ['01f', '04f'],                # шорты b
                    'c': ['01i1', '04i1'],              # низ новой спортики
                    'd': ['01e', '04e'],                # шорты d
                    }[ann.clothes.cook_morn.GetCur().suf])
            elif ann.prev_plan == 'in_shop':                # после шопинга
                lst.extend(['01c2', '04c2'])            # трусики
            elif ann.prev_plan == 'read':                   # после чтения
                if ann.clothes.rest_morn.GetCur().suf == 'a':
                    lst.extend(['01f', '04f'])                              # шорты b
                elif ann.clothes.rest_morn.GetCur().suf == 'd':
                    lst.extend(['01e', '04e'])                              # шорты d

            # одеваемая одежда
            if balcony:
                pass
            elif ann.plan_name == 'yoga':                         # йога
                if lvl == 1:
                    lst.extend(['01h', '04h'])                              # полная спортивка
                else:
                    if ann.clothes.sports.cur:
                        lst.extend(['01i1', '01i2', '04i1', '04i2'])        # низ и верх новой спортики
                    else:
                        lst.extend(['01h1', '01h2', '04h1', '04h2'])        # низ и верх спортики
            elif ann.plan_name == 'cooking' and tm < '12:00':   # готовка утром
                if ann.clothes.cook_morn.GetCur().suf == 'b':
                    lst.extend(['01f', '04f'])                              # шорты b
                elif ann.clothes.cook_morn.GetCur().suf == 'd':
                    lst.extend(['01e', '04e'])                              # шорты d
                    lst.extend(['01e3', '04e3'])                            # верх d + трусики
                    if lvl > 1:
                        lst.extend(['01e2', '04e2'])                        # верх d
            elif ann.plan_name == 'dressed':                    # одевается на работу/шопинг
                lst.extend(['01c2', '04c2'])                                # трусики
                if GetWeekday(day) != 6:
                    # будни
                    lst.extend(['01a3', '04a3'])                            # рабочий топ + трусики
                    if lvl > 1:
                        lst.extend(['01a', '01a2', '04a', '04a2'])          # рабочая юбка, рабочий топ
            elif ann.plan_name in ['sun', 'swim']:              # купальник
                lst.extend(['01d2', '04d2'])                                # низ купальника
                if lvl > 1:
                    lst.extend(['01d1', '04d1'])                            # верх купальника
            elif ann.plan_name == 'cooking' and tm > '12:00':   # готовка вечером
                if ann.clothes.cook_eve.GetCur().suf == 'b':
                    lst.extend(['01f', '04f'])                              # шорты b
                elif ann.clothes.cook_eve.GetCur().suf == 'd':
                    lst.extend(['01e', '04e'])                              # шорты d
                    lst.extend(['01e3', '04e3'])                            # верх d + трусики
                    if lvl > 1:
                        lst.extend(['01e2', '04e2'])                        # верх d
            elif ann.plan_name == 'resting' and tm < '12:00':   # отдых утром после завтрака
                if ann.clothes.rest_morn.GetCur().suf == 'a':
                    lst.extend(['01f', '04f'])                              # шорты b
                elif ann.clothes.rest_morn.GetCur().suf == 'd':
                    lst.extend(['01e', '04e'])                              # шорты d
                    lst.extend(['01e3', '04e3'])                            # верх d + трусики
                    if lvl > 1:
                        lst.extend(['01e2', '04e2'])                        # верх d
            elif ann.plan_name == 'resting' and tm > '20:00':   # отдых вечером
                if ann.clothes.rest_eve.GetCur().suf == 'a':
                    lst.extend(['01f', '04f'])                              # шорты b
                elif ann.clothes.rest_eve.GetCur().suf == 'd':
                    lst.extend(['01e', '04e'])                              # шорты d
                    lst.extend(['01e3', '04e3'])                            # верх d + трусики
                    if lvl > 1:
                        lst.extend(['01e2', '04e2'])                        # верх d

            pose = renpy.random.choice(lst)

        if vr < 2:
            if lvl == 1 and pose in ['01b1', '01h3', '04h3', '01e3', '04e3',
                                    '01a3', '04a3', '01c2', '04c2']:
                pose = {
                    '01b1':'03b1',                  # халат
                    '01h3':'03h3', '04h3':'06h3',    # верх спортивки + трусики
                    '01e3':'03e3', '04e3':'06e3',   # верх d + трусики
                    '01a3':'03a3', '04a3':'06a3',   # рабочий топ + трусики
                    '01c2':'03c2', '04c2':'06c2',   # трусики
                    }[pose]
            else:
                pose = {
                    '01b':'03b', '01b1':'02b1',                                 # халат
                    '01h':'02h', '04h':'05h',                                   # полная спортивка
                    '01h1':'02h1', '04h1':'05h1', '01h2':'03h2', '04h2':'06h2', # низ / верх спортивки
                    '01i1':'02i1', '04i1':'05i1', '01i2':'03i2', '04i2':'06i2', # низ / верх новой спортивки
                    '01f':'02f', '04f':'05f', '01e':'02e', '04e':'05e',         # шорты b / d
                    '01e2':'03e2', '04e2':'06e2', '01e3':'02e3', '04e3':'05e3', # верх d / + трусики
                    '01a':'02a', '04a':'05a',                                   # рабочая юбка
                    '01a2':'03a2', '04a2':'06a2', '01a3':'02a3', '04a3':'05a3', # рабочий топ / + трусики
                    '01c2':'02c2', '04c2':'05c2',                               # трусики
                    '01d1':'08d1', '04d1':'08d1', '01d2':'02d2', '04d2':'05d2', # верх / низ бикини
                    '01':'02', '04': '06',          # голая
                    }[pose]

        if pose:
            return pose
        else:
            return '02c2'


    def get_ann_dress(vr, pose=''):
        global var_pose, var_dress

        lvl = get_ann_emancipation()

        # определим доступные варианты одежды
        lst = []
        if vr == 'b':    # на балконе, неодета
            lst.append('c2')      # трусики
            if lvl > 1:
                lst.append('')    # голая
        elif vr == 'b0':    # на балконе одетая
            lst.extend(['a'] if 6 > weekday > 0 else ['e', 'f'])
        elif vr == 'g':
            lst.append('j' if weekday == 6 else 'a')
        elif vr == 0:
            # нулевой момент
            if ann.prev_plan in ['shower', 'shower2']:      # после душа
                lst.append('b')       # халат
                if lvl > 1:
                    lst.append('b2')  # чуть распахнутый халат
            elif ann.prev_plan == 'yoga':                   # после йоги
                lst.append('h' if ann.clothes.sports.GetCur().suf == 'a' else 'i')       # спортивка
            elif ann.prev_plan == 'breakfast':
                lst.append({'a':'h', 'b':'f', 'c':'i', 'd':'e'}[ann.clothes.cook_morn.GetCur().suf])
            elif ann.prev_plan == 'in_shop':
                lst.append('j')
            elif ann.prev_plan in ['resting', 'read'] and tm[:2] == '14':
                lst.append('f' if ann.clothes.rest_morn.GetCur().suf == 'a' else 'e')
            elif ann.prev_plan in ['sun', 'swim']:
                lst.append('d')
            elif ann.prev_plan == 'tv':
                lst.append('g')
        else:
            if ann.prev_plan in ['shower', 'shower2']:      # после душа
                lst.append('b1')                                            # халат + трусики
                if lvl > 1:
                    lst.append('b')                                         # халат без трусиков
            elif ann.prev_plan == 'yoga':                   # после йоги
                lst.append('i1' if ann.clothes.sports.cur else 'h1')        # низ спортики
            elif ann.prev_plan in ['sun', 'swim']:          # после бассейна
                lst.append('d2')                                            # низ купальника
            elif ann.prev_plan == 'breakfast':              # после завтрака
                lst.append({'a': 'h1', 'b': 'f', 'c': 'i1', 'd': 'e'}[ann.clothes.cook_morn.GetCur().suf])
            elif ann.prev_plan == 'in_shop':                # после шопинга
                lst.append('c2')                                            # трусики
            elif ann.prev_plan == 'read':                   # после чтения
                if ann.clothes.rest_morn.GetCur().suf == 'a':
                    lst.append('f')                                         # шорты b
                elif ann.clothes.rest_morn.GetCur().suf == 'd':
                    lst.append('e')                                         # шорты d

            if ann.plan_name == 'yoga':                         # йога
                if lvl == 1:
                    lst.append('h')                              # полная спортивка
                else:
                    if ann.clothes.sports.cur:
                        lst.extend(['i1', 'i2'])        # низ и верх новой спортики
                    else:
                        lst.extend(['h1', 'h2'])        # низ и верх спортики
            elif ann.plan_name == 'cooking' and tm < '12:00':   # готовка утром
                if ann.clothes.cook_morn.GetCur().suf == 'b':
                    lst.append('f')                              # шорты b
                elif ann.clothes.cook_morn.GetCur().suf == 'd':
                    lst.extend(['e', 'e3'])                      # шорты d, верх d + трусики
                    if lvl > 1:
                        lst.append('e2')                        # верх d
            elif ann.plan_name == 'dressed':                    # одевается на работу/шопинг
                lst.append('c2')                                # трусики
                if GetWeekday(day) != 6:
                    # будни
                    lst.append('a3')                            # рабочий топ + трусики
                    if lvl > 1:
                        lst.extend(['a', 'a2'])          # рабочая юбка, рабочий топ
            elif ann.plan_name in ['sun', 'swim']:              # купальник
                lst.append('d2')                                # низ купальника
                if lvl > 1:
                    lst.append('d1')                            # верх купальника
            elif ann.plan_name == 'cooking' and tm > '12:00':   # готовка вечером
                if ann.clothes.cook_eve.GetCur().suf == 'b':
                    lst.append('f')                              # шорты b
                elif ann.clothes.cook_eve.GetCur().suf == 'd':
                    lst.extend(['e', 'e3'])                     # шорты d, верх d + трусики
                    if lvl > 1:
                        lst.append('e2')                        # верх d
            elif ann.plan_name == 'resting' and tm < '12:00':   # отдых утром после завтрака
                if ann.clothes.rest_morn.GetCur().suf == 'a':
                    lst.append('f')                              # шорты b
                elif ann.clothes.rest_morn.GetCur().suf == 'd':
                    lst.extend(['e', 'e3'])                     # шорты d, верх d + трусики
                    if lvl > 1:
                        lst.append('e2')                        # верх d
            elif ann.plan_name == 'resting' and tm > '20:00':   # отдых вечером
                if ann.clothes.rest_eve.GetCur().suf == 'a':
                    lst.append('f')                              # шорты b
                elif ann.clothes.rest_eve.GetCur().suf == 'd':
                    lst.extend(['e', 'e3'])                     # шорты d, верх d + трусики
                    if lvl > 1:
                        lst.append('e2')                        # верх d

        if not pose:
            # установим одежду и выберем позу для момента "повезло"
            var_dress = renpy.random.choice(lst)
            if vr in [0, 'g', 'b0']:
                pose = '07'
            elif var_dress in ['b', 'b1']:
                pose = '01'
            else:
                pose = renpy.random.choice(['01', '04'])

        if vr == 1:
            # не повезло, смотрим, в какую позу встанет Анна
            if lvl == 1 and var_dress in ['a3', 'b1', 'c2', 'e3', 'h3']:
                pose = {'01':'03', '04':'06'}[pose]
            elif var_dress in ['a', 'a3', 'b1', 'c2', 'd2', 'e', 'e3', 'f', 'h', 'h1', 'i1']:
                pose = {'01':'02', '04':'05'}[pose]
            elif var_dress == 'd1':
                pose = '08'
            else:
                pose = {'01':'03', '04':'06'}[pose]

        var_pose = pose
