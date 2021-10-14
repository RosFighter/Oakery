
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
