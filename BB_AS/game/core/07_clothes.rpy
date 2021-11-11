
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

    def ChoiceClothes(): # Проверяет необходимоть смены текущей одежды
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


    def GetDressNps(char, name):
        dress, inf, clot = '', '', ''
        if name=='dressed':
            inf = '00b'

        elif char=='lisa':
            if name in ['sleep', 'sleep2']:
                dress = lisa.clothes.sleep.GetCur().suf
                inf   = lisa.clothes.sleep.GetCur().info
                clot  = 'sleep'
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
                dress = ann.clothes.casual.GetCur().suf if tm < '14:00' else 'b'
                inf   = ann.clothes.casual.GetCur().info if tm < '14:00' else '03'
                clot  = 'casual' if tm < '14:00' else 'купальник'
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
            if olivia.dcv.other.stage:
                dress = 'b'
            else:
                dress = 'a'

            if name in ['sleep2', 'sleep', 'at_home']:
                inf = '00'
            elif name == 'in_shcool':
                inf = '01'
            elif name == 'sun':
                inf = '00' if olivia.dcv.other.stage else '03'
            elif name == 'swim':
                if pose3_3=='01':
                    inf = '00' if olivia.dcv.other.stage else '03'
                else:
                    inf = '00a' if olivia.dcv.other.stage else '03a'

        # print("%s %s clot - %s, dress - %s ( %s )"%(char, name, clot, dress, inf))
        return dress, inf, clot


    def ClothingNps(char, name): # устанавливает текущую одежду согласно расписанию (в том числе для инфо)
        dress, inf, clot = GetDressNps(char, name)
        if dress != '':
            chars[char].dress = dress
            # print('%s - %s : %s'%(char, clot, dress))
        if inf != '':
            chars[char].dress_inf = inf
        return


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
                        # print 'меняем имя одежды', '('+char_id+'-'+clot_type+')', clots.sel[k].name,'|', clot[2]
                        clots.sel[k].name = clot[2]


    def add_new_clot_type(clots, clot_type, char_id):
        # такой одежды у персонажа ещё не было, нужно добавить
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


    def check_extend_clot_type(clots, clot_type, char_id):
        # проверяем список одежды
        for k in range(len(clothes_dict[char_id][clot_type])):
            clot = clothes_dict[char_id][clot_type][k]

            if k < len(clots.sel):
                # пропущенное вставляем
                if clot[0] < clots.sel[k].suf:
                    clots.sel.insert(k, Garb(clot[0], clot[1], clot[2]))
            else:
                # добавляем новые
                clots.sel.append(Garb(clot[0], clot[1], clot[2]))


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


    class MenuClothes():
        id_char = ''
        name    = ''

        def __init__(self, id_char, name):
            self.id_char    = id_char
            self.name       = name

        def open(self, id_clot, var):
            # открывает вариант типа одежды персонажа для главного меню
            if self.id_char not in menu_clothes_dict:
                print ('Персонаж', self.name, 'отсутствует в списке одежды для меню')
                return False

            if id_clot not in menu_clothes_dict[self.id_char]:
                print ('тип одежды', id_clot, 'для персонажа', self.name, 'отсутствует в списке одежды для меню')
                return False

            if menu_clothes_dict[self.id_char][id_clot][var] is None:
                print ('Вариант', var, 'недоступен для одежды', id_clot, 'персонажа', self.name)
                return False

            if self.id_char not in persistent.mm_chars:
                # добавим персонажа, создав пустой список доступной одежды
                persistent.mm_chars[self.id_char] = []

            if not persistent.mm_chars[self.id_char]:
                # если список одежды персонажа пуст,
                # в качестве текущей одежды ставим полный вариант добавляемой
                persistent.mm_chars[self.id_char].append((id_clot, 0))

                # !!! в пустой список полный комплект добавляем дважды !!!
                persistent.mm_chars[self.id_char].append((id_clot, 0))

            else:
                if var != 0 :
                    # если добавляется не полный комплект, полный открываем автоматически
                    if not persistent.mm_chars[self.id_char].count((id_clot, 0)):
                        persistent.mm_chars[self.id_char].append((id_clot, 0))

            if (id_clot, var) not in persistent.mm_chars[self.id_char]:
                # вариант одежды для персонажа в списке отсутствует
                persistent.mm_chars[self.id_char].append((id_clot, var))

            return True

        def get_current(self):
            # возвращает текущий вариант одежды персонажа для главного меню
            if self.id_char not in persistent.mm_chars:
                return None, None
            return persistent.mm_chars[self.id_char][0]

        def get_open_clot(self):
            # возвращает список открытых вариантов одежды для персонажа
            lst0 = []
            lst1 = []
            for i in range(1, len(persistent.mm_chars[self.id_char])):
                lst0.append(persistent.mm_chars[self.id_char][i][0])

            for k in menu_clothes_dict[self.id_char]:
                if k in lst0:
                    lst1.append(k)

            return lst1

        def get_all_open(self):
            lst = []
            for i in range(1, len(persistent.mm_chars[self.id_char])):
                lst.append(persistent.mm_chars[self.id_char][i][0])
            return lst

        def get_open_var(self, clot):
            lst = []

            if clot == 'naked':
                return []

            for i in range(5):
                if (clot, i) in persistent.mm_chars[self.id_char]:
                    lst.append(i)

            return lst

        def render0(self, clot):
            lst = []
            if menu_clothes_dict[self.id_char][clot][0][0]:
                # для полного варианта есть рендер
                lst.append(menu_clothes_dict[self.id_char][clot][0][0])
            else:
                # рендер составной

                if 3 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][3] is not None:
                    # низ
                    lst.append(menu_clothes_dict[self.id_char][clot][3][0])
                elif 4 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][4] is not None:
                    # или трусики
                    lst.append(menu_clothes_dict[self.id_char][clot][4][0])

                if 2 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][2] is not None:
                    # верх
                    lst.append(menu_clothes_dict[self.id_char][clot][2][0])
            return lst

        def get_render_list(self):
            clot, cur = self.get_current()
            if clot is None:
                # print ('0 - нет персонажа')
                return []
            lst = []
            if clot == 'naked' or clot not in menu_clothes_dict[self.id_char]:
                # print ('1 - нет типа одежды или установлена обнажёнка')
                return []

            if cur == 0:
                # полный вариант
                lst = self.render0(clot)

            elif cur == 1:
                # верх + трусики
                if 1 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][1]:
                    # вариант существует
                    if menu_clothes_dict[self.id_char][clot][1][0]:
                        # задан отдельный рендер
                        lst.append(menu_clothes_dict[self.id_char][clot][1][0])
                    else:
                        # рендер составной
                        if 4 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][4] is not None:
                            # трусики заданы
                            lst.append(menu_clothes_dict[self.id_char][clot][4][0])
                        else:
                            # произошла ошибка и трусики не заданы, отображаем низ
                            if 3 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][3] is not None:
                                lst.append(menu_clothes_dict[self.id_char][clot][3][0])
                        if 2 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][2] is not None:
                            # отображаем верх
                            lst.append(menu_clothes_dict[self.id_char][clot][2][0])
                else:
                    # где-то произошла ошибка и варианта (верх + трусики) несуществует
                    # отображаем полный
                    lst = render0(self, clot)

            elif cur == 2:
                # только верх
                if 2 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][2]:
                    # вариант существует
                    # отображаем верх
                    lst.append(menu_clothes_dict[self.id_char][clot][2][0])
                else:
                    # где-то произошла ошибка и варианта (только верх) несуществует
                    # отображаем полный
                    lst = render0(self, clot)
            elif cur == 3:
                # только низ
                if 3 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][3]:
                    # вариант существует
                    # отображаем низ
                    lst.append(menu_clothes_dict[self.id_char][clot][3][0])
                else:
                    # где-то произошла ошибка и варианта (только низ) несуществует
                    # отображаем полный
                    lst = render0(self, clot)
            elif cur == 4:
                # только трусики
                if 4 in menu_clothes_dict[self.id_char][clot] and menu_clothes_dict[self.id_char][clot][4]:
                    # вариант существует
                    # отображаем низ
                    lst.append(menu_clothes_dict[self.id_char][clot][4][0])
                else:
                    # где-то произошла ошибка и варианта (только низ) несуществует
                    # отображаем полный
                    lst = render0(self, clot)

            return lst

        def get_info(self, id_clot, var):
            if self.id_char not in menu_clothes_dict:
                # print ('Персонаж', self.name, 'отсутствует в списке одежды для меню')
                return None

            if id_clot not in menu_clothes_dict[self.id_char]:
                # print ('тип одежды', id_clot, 'для персонажа', self.name, 'отсутствует в списке одежды для меню')
                return None

            if var not in menu_clothes_dict[self.id_char][id_clot] or menu_clothes_dict[self.id_char][id_clot][var] is None:
                # print ('Вариант', var, 'недоступен для одежды', id_clot, 'персонажа', self.name)
                return None

            return menu_clothes_dict[self.id_char][id_clot][var][1]

        def set_current(self, id_clot, var):
            persistent.mm_chars[self.id_char][0] = (id_clot, var)

    def set_mm_clot(char, clot, var):
        menu_chars[char].set_current(clot, var)

    Set_mm_clot = renpy.curry(set_mm_clot)

define menu_clothes_dict = {
    # 'персонаж' : [('id одежды' , {0 : (рендер одежды, рендер в инфо), - полный
    #                               1 : (), - топ + трусики
    #                               2 : (), - только топ
    #                               3 : (), - только низ
    #                               4 : ()  - только трусики
    #                               }),
    #                               ...]
    #
    # заготовка: ('', {0: ('', ''), 1: ('', ''), 2: ('', ''), 3: ('', ''), 4: ('', '')}),
    'max'   : OrderedDict([
        ('naked',    {0: (None, '00')}),
        ('casual_c', {0: ('01c', '01c'), 1: None, 2: None, 3: None, 4: None}),
        ]),
    'alice' : OrderedDict([
        ('naked',    {0: (None, '00')}),
        ('casual_d', {0: ('01a', '01e'), 1: None, 2: ('01a1', '01e1'),
                      3: ('01a2', '02h'), 4 : None
                      }),
        ('swim',     {0: (None, '03'), 1:None, 2:('01b1', '03b1'),
                      3:('01b2', '03b'), 4:None
                      }),
        ('sleep0',   {0: (None, '02i1'), 1:None, 2:('01c1', '02i2'),
                      3:None, 4:('01c2', '02i3')
                      }),
        ('sleep1',   {0: (None, '02j1'), 1:None, 2:('01d1', '02j2'),
                      3:None, 4:('01d2', '02j3')
                      }),
        ]),
    'ann'   : OrderedDict([
        ('naked',    {0: (None, '00')}),
        ('casual_d', {0: (None, '01e'), 1: (None, '02i'), 2: ('01a1', '02h'),
                      3: ('01a2', '02g'), 4: ('01c2', '02b')}),
        ('swim',     {0: (None, '03'), 1: None, 2: ('01b1', '03a1'),
                      3: ('01b2', '03a2'), 4: None}),
        ('sleep0',   {0: (None, '02'), 1: None, 2: ('01c1', '02a'),
                      3: None, 4: ('01c2', '02b')}),
        ]),
    'kira'  : OrderedDict([
        ('naked',    {0: (None, '00')}),
        ('casual_d', {0: (None, '01a'), 1: None, 2: ('01a1', '01a1'),
                      3: ('01a2', '01a2'), 4: None}),
        ('swim',     {0: (None, '03'), 1: None, 2: ('01b1', '03b'),
                      3: ('01b2', '03c'), 4: None}),
        ('sleep0',   {0: ('01c', '02'), 1: None, 2: ('01c1', '02b'),
                      3: None, 4: ('01c2', '02a')}),
        ]),
    'lisa'  : OrderedDict([
        ('naked',    {0: (None, '00')}),
        ('casual_d', {0: (None, '01c'), 1: (None, '01c2'), 2: ('01a1', '01c3'),
                      3: ('01a2', '01c1'), 4: ('01c3', '02c')}),
        ('swim',     {0: (None, '03b'), 1: None, 2: ('01b1', '03d1'),
                      3: ('01b2', '03d'), 4: None}),
        ('sleep0',   {0: (None, '02'), 1: None, 2: ('01c1', '02b'),
                      3: ('01c2', '02c1'), 4: None}),
        ('sleep1',   {0: (None, '02a'), 1: None, 2: ('01c1', '02b'),
                      3: None, 4: ('01c3', '02c')}),
        ]),
    }

default persistent.mm_chars = {}

define menu_chars = OrderedDict([
    ('Max'  , MenuClothes('max', _("Макс"))),
    ('Ann'  , MenuClothes('ann', _("Анна"))),
    ('Lisa' , MenuClothes('lisa', _("Лиза"))),
    ('Kira' , MenuClothes('kira', _("Кира"))),
    ('Alice', MenuClothes('alice', _("Алиса"))),
    ])

default mm_char = sorted(menu_chars)[0]
# default clot = menu_chars[mm_char].get_current()[0]
# default var = menu_chars[mm_char].get_current()[1]

init 100 python:
    if 'kira' in persistent.mems_var:
        # if not 'menu_var' in persistent:
        #     $ persistent.menu_var = '01'
        # persistent.mm_chars.clear()

        menu_chars['Max'].open('casual_c', 0)
        menu_chars['Alice'].open('casual_d', 0)
        menu_chars['Ann'].open('casual_d', 0)
        menu_chars['Lisa'].open('casual_d', 0)
        menu_chars['Kira'].open('casual_d', 0)

        # open all
        menu_chars['Alice'].open('naked', 0)
        menu_chars['Alice'].open('casual_d', 2)
        menu_chars['Alice'].open('casual_d', 3)
        menu_chars['Alice'].open('swim', 2)
        menu_chars['Alice'].open('swim', 3)
        menu_chars['Alice'].open('sleep0', 2)
        menu_chars['Alice'].open('sleep0', 4)
        menu_chars['Alice'].open('sleep1', 2)
        menu_chars['Alice'].open('sleep1', 4)

        menu_chars['Ann'].open('naked', 0)
        menu_chars['Ann'].open('casual_d', 1)
        menu_chars['Ann'].open('casual_d', 2)
        menu_chars['Ann'].open('casual_d', 3)
        menu_chars['Ann'].open('casual_d', 4)
        menu_chars['Ann'].open('swim', 2)
        menu_chars['Ann'].open('swim', 3)
        menu_chars['Ann'].open('sleep0', 2)
        menu_chars['Ann'].open('sleep0', 4)

        menu_chars['Kira'].open('naked', 0)
        menu_chars['Kira'].open('casual_d', 2)
        menu_chars['Kira'].open('casual_d', 3)
        menu_chars['Kira'].open('swim', 2)
        menu_chars['Kira'].open('swim', 3)
        menu_chars['Kira'].open('sleep0', 2)
        menu_chars['Kira'].open('sleep0', 4)

        menu_chars['Lisa'].open('naked', 0)
        menu_chars['Lisa'].open('casual_d', 1)
        menu_chars['Lisa'].open('casual_d', 2)
        menu_chars['Lisa'].open('casual_d', 3)
        menu_chars['Lisa'].open('casual_d', 4)
        menu_chars['Lisa'].open('swim', 2)
        menu_chars['Lisa'].open('swim', 3)
        menu_chars['Lisa'].open('sleep0', 2)
        menu_chars['Lisa'].open('sleep0', 3)
        menu_chars['Lisa'].open('sleep1', 2)
        menu_chars['Lisa'].open('sleep1', 4)
