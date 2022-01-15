# f - полный комплект одежды
# t - топ (блузка, футболка и т.п.)
# b - низ (юбка, джинсы, шорты и т.п)
# lt - верх нижнего белья/купальника
# lb - низ белья/купальника или нижнее бельё, если оно цельное
# h - головной убор
# st - чулки/колготки
# sh - обувь
# a1 - аксессуар 1
# a2 - аксессуар 2

# tb - топ + низ в случае их перекрытия
# tlb - топ + трусики

init python:

    # класс описания "печенек"
    class MM_Cookies():

        def __init__(self, char, clot, room, lod, tm1, tm2, xy, sc=1.0, al=1.0, num=1, req='True'):
            self.char   = char
            self.clot   = clot
            self.room   = room
            self.xy     = xy
            self.sc     = sc
            self.al     = al
            self.num    = num
            self.req    = req

            if isinstance(lod, (str, basestring)):
                self.lod = tuple([int(x) for x in lod.replace(', ', ',').split(',')])
            elif isinstance(lod, int):
                self.lod = (lod, )
            else:
                self.lod = lod
            h, m = tm1.split(':') if str(tm1).find(':') > 0 else str(float(tm1)).replace('.', ':').split(':')
            self.tm1 = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]

            h, m = tm2.split(':') if str(tm2).find(':') > 0 else str(float(tm2)).replace('.', ':').split(':')
            self.tm2 = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]


        def mark_found(self):
            if self.num == 1:
                if self.char not in persistent.mm_cookies:
                    persistent.mm_cookies[self.char] = {}
                persistent.mm_cookies[self.char][self.clot] = set()
            persistent.mm_cookies[self.char][self.clot].add('cookie_'+str(self.num))

            if self.char in chars:
                notify_list.append(__("{color=[lime]}Открыта детальная настройка для одного из костюмов %s в главном меню{/color}") % renpy.translate_string(chars[self.char].name_1))


    # класс описания элементов одежды главного меню
    class MMIoC():
        # main menu item of clothing
        def __init__(self, i, p, r=None, n='', f=0, ex=0, nc=1, over=None, eq=None, idlst=None):
            self.ind    = i     # индекс элемента одежды
            self.p      = p     # рендер настроек
            self.r      = r     # рендер главного меню
            self.name   = n     # наименование элемента одежды для кнопки настроек
            self.ex     = ex    # снимать можно только для экстра
            self.nc     = nc    # требуется "печенек" для снятия
            self.full   = f     # рендер настроек полный (включая тело)
            if isinstance(over, (str, basestring)):
                self.over = over.replace(', ', ',').split(',')
            else:
                # if over:
                #     print n, over, type(over), isinstance(over, (str, basestring))
                self.over = over # список игнорируемых идентификаторов (при надетых шортах кнопка трусиков неактивна)
            self.eq     = eq    # id одежды-эквивалента (при активации эквивалент деактивируется)
            self.id_lst = idlst # список ключей заменяемых элементов одежды (для составных)

        def __repr__(self):
            return '{self.ind}, p:{self.p}, r:{self.r}, name:{self.name}, f:{self.full}, over:{self.over}, eq:{self.eq}, ex:{self.ex}, nc:{self.nc}'.format(self=self)


    # класс справочника одежды персонажей главного меню
    class MMClot():
        # clothes - упорядоченный словарь элементов одежды
        # sc - scale (масштаб) костюма в настройках

        def __init__(self, clot, sc=1.0):
            self.scale = sc
            self.clothes = OrderedDict()
            for id, item in clot:
                added = item
                if '+' in id:
                    idlst = id.split('+')
                    if not added.r:
                        # составной рендер
                        cl_o = []
                        cl_r = []
                        for id_item in idlst:
                            cl_r.append((self.clothes[id_item].ind, self.clothes[id_item].r))
                            if self.clothes[id_item].over:
                                cl_o.extend(self.clothes[id_item].over)
                        cl_r.sort()
                        added.r = [i[1] for i in cl_r]
                        added.over = cl_o if cl_o else None
                    added.id_lst = idlst

                self.clothes[id] = added

        # возвращает словарь отдельных элементов одежды (активированных)
        # и список кортежей кнопок (наименование, id в словаре, доступность)
        def get_btn_list(self, char_id, clot_id):
            dict_item = {}
            btn = []
            equv = []
            find_cookies = 0
            if char_id in persistent.mm_cookies:
                if clot_id in persistent.mm_cookies[char_id]:
                    find_cookies = len(persistent.mm_cookies[char_id][clot_id])

            for item in self.clothes:
                if '+' not in item:
                    # это отдельный элемент
                    dict_item[item] = 1 if item not in equv else 0

                    cookies = self.clothes[item].nc <= find_cookies

                    # кнопка доступна, если есть экстра, одежда без ограничений
                    # выполнено требование по печенькам или у одежды есть эквивалент (тогда они переключаются)
                    access = cookies and any([extra_content, not self.clothes[item].ex, self.clothes[item].eq])

                    # один из эквивалентов обязательно должен быть активирован
                    required = self.clothes[item].ex and not extra_content

                    btn.append((self.clothes[item].name, item, access, self.clothes[item].eq, required))
                    if self.clothes[item].eq:
                        equv.append(self.clothes[item].eq)
                        # print 'equv:', equv
            return dict_item, btn

        # возвращает список спрайтов одежды для главного меню в порядке наложения
        def get_menu_rdr(self, dict_item, iter=1):

            if not extra_content:
                # активируем "неснимаемые" одёжки для не-экстра
                for k in dict_item:
                    if not dict_item[k] and self.clothes[k].ex:
                        # элемент одежды не активирован, но обязателен в не-экстра
                        if not self.clothes[k].eq:
                            # нет эквивалента
                            dict_item[k] = 1
                        elif not dict_item[self.clothes[k].eq]:
                            # есть эквивалент и он не активен
                            dict_item[k] = 1

            # сформируем список одетых элементов
            itm = [k for k in dict_item if dict_item[k]]

            rdr_lst = []    # список кортежей рендеров (индекс, рендер)

            # исключить из списка игнорируемые элементы
            for i in itm:
                if self.clothes[i].over is None:
                    continue
                for k in self.clothes[i].over:
                    if k in itm:
                        itm.remove(k)

            # выбрать используемые составные рендеры
            for k in self.clothes:
                if '+' not in k:
                    # пропустим одиночные элементы
                    continue

                if list_in_list(self.clothes[k].id_lst, itm):
                    # все элементы составного рендера содержаться в списке используемых

                    # пополним список рендеров
                    if isinstance(self.clothes[k].r, (str, basestring)):
                        rdr_lst.append((self.clothes[k].ind, self.clothes[k].r))
                    else:
                        for i in self.clothes[k].id_lst:
                            rdr_lst.append((self.clothes[i].ind, self.clothes[i].r))

                    # удалим задействованные элементы из списка одетых
                    for i in self.clothes[k].id_lst:
                        itm.remove(i)

            # дополним одиночными элементами
            for k in itm:
                rdr_lst.append((self.clothes[k].ind, self.clothes[k].r))

            # упорядочим по индексу
            rdr_lst.sort()

            # возвращаем список рендеров
            if iter < 2:
                return [k[1] for k in rdr_lst if k[0] < 11]
            else:
                return [k[1] for k in rdr_lst if k[0] > 10]

        # возвращает список спрайтов одежды для окна выбора в порядке наложения
        def get_pref_rdr(self, dict_item):

            if not extra_content:
                # активируем "неснимаемые" одёжки для не-экстра
                for k in dict_item:
                    if not dict_item[k] and self.clothes[k].ex:
                        # элемент одежды не активирован, но обязателен в не-экстра
                        if not self.clothes[k].eq:
                            # нет эквивалента
                            dict_item[k] = 1
                        elif not dict_item[self.clothes[k].eq]:
                            # есть эквивалент и он не активен
                            dict_item[k] = 1

            # сформируем список одетых элементов
            itm = [k for k in dict_item if dict_item[k]]

            rdr_lst = []    # список кортежей рендеров (индекс, рендер)
            full = False

            # исключить из списка игнорируемые элементы
            for i in itm:
                if self.clothes[i].over is None:
                    continue
                for k in self.clothes[i].over:
                    if k in itm:
                        itm.remove(k)

            if len(itm) == 1:
                full = self.clothes[itm[0]].full

            # выбрать используемые составные рендеры
            for k in self.clothes:
                if '+' not in k:
                    # пропустим одиночные элементы
                    continue

                if list_in_list(self.clothes[k].id_lst, itm):
                    # все элементы составного рендера содержаться в списке используемых

                    rdr_lst.append((self.clothes[k].ind, self.clothes[k].p))
                    if self.clothes[k].full:
                        full = True

                    # удалим задействованные элементы из списка одетых
                    for i in self.clothes[k].id_lst:
                        itm.remove(i)

            # дополним одиночными элементами
            for k in itm:
                rdr_lst.append((self.clothes[k].ind, self.clothes[k].p))

            # упорядочим по индексу
            rdr_lst.sort()

            # возвращаем список рендеров
            return full, [k[1] for k in rdr_lst], self.scale


    # класс одежды персонажей главного меню
    class MenuClothes():
        id_char = ''
        name    = ''

        def __init__(self, id_char, name):
            self.id_char    = id_char
            self.name       = name

        # открывает тип одежды персонажа для главного меню
        def open(self, id_clot):
            if self.id_char not in mm_clot_dict:
                print ('Персонаж', self.name, 'отсутствует в списке одежды для меню')
                return False

            if id_clot not in mm_clot_dict[self.id_char]:
                print ('тип одежды', id_clot, 'для персонажа', self.name, 'отсутствует в списке одежды для меню')
                return False

            if self.id_char not in persistent.mm_chars:
                # добавим персонажа, создав пустой список доступной одежды
                persistent.mm_chars[self.id_char] = []

            if not persistent.mm_chars[self.id_char]:
                # если список одежды персонажа пуст, добавляемый вариант
                # устанавливаем в качестве текущего
                persistent.mm_chars[self.id_char].append((id_clot, mm_clot_dict[self.id_char][id_clot].get_btn_list(self.id_char, id_clot)[0]))

            if id_clot not in persistent.mm_chars[self.id_char]:
                persistent.mm_chars[self.id_char].append(id_clot)
                if 'chars' in globals():
                    if self.id_char != 'max':
                        notify_list.append(__("{color=#00FF00}Открыт новый костюм %s для главного меню{/color}") % renpy.translate_string(chars[self.id_char].name_1))
                    else:
                        notify_list.append(__("{color=#00FF00}Открыт новый костюм %s для главного меню{/color}") % renpy.translate_string(mgg.name_1))

            return True

        # закрывает тип одежды персонажа для главного меню
        def close(self, id_clot):
            if self.id_char not in mm_clot_dict:
                print ('Персонаж', self.name, 'отсутствует в списке одежды для меню')
                return False

            if id_clot not in mm_clot_dict[self.id_char]:
                print ('тип одежды', id_clot, 'для персонажа', self.name, 'отсутствует в списке одежды для меню')
                return False

            if self.id_char not in persistent.mm_chars:
                # добавим персонажа, создав пустой список доступной одежды
                persistent.mm_chars[self.id_char] = []
                return False

            if id_clot in persistent.mm_chars[self.id_char]:
                if len(persistent.mm_chars[self.id_char]) == 2:
                    # открыт только удаляемый костюм
                    # очищаем список и выходим
                    persistent.mm_chars[self.id_char].clear()
                    return True
                else:
                    persistent.mm_chars[self.id_char].remove(id_clot)

            if persistent.mm_chars[self.id_char][0][0] == id_clot:
                # в качестве текущей одежды установлена удаляемая
                persistent.mm_chars[self.id_char][0] = tuple([
                    persistent.mm_chars[self.id_char][1],
                    mm_clot_dict[self.id_char][persistent.mm_chars[self.id_char][1]].get_btn_list(self.id_char, persistent.mm_chars[self.id_char][1])[0]
                    ])
                return True

        def get_current(self):
            # возвращает текущий вариант одежды персонажа для главного меню
            if self.id_char not in persistent.mm_chars:
                return None, None
            clot, var = persistent.mm_chars[self.id_char][0]

            if not extra_content:
                # активируем "неснимаемые" одёжки для не-экстра
                for k in var:
                    if k not in mm_clot_dict[self.id_char][clot].clothes:
                        print 'bag clothes mm', self.id_char, clot, k
                        continue
                    if not var[k] and mm_clot_dict[self.id_char][clot].clothes[k].ex:
                        # элемент одежды не активирован, но обязателен в не-экстра
                        if not mm_clot_dict[self.id_char][clot].clothes[k].eq:
                            # нет эквивалента
                            var[k] = 1
                        elif not var[mm_clot_dict[self.id_char][clot].clothes[k].eq]:
                            # есть эквивалент и он не активен
                            var[k] = 1

            return clot, var

        def get_open_clot(self):
            # возвращает список открытых вариантов одежды для персонажа
            lst0 = []
            lst1 = []
            if self.id_char not in persistent.mm_chars:
                return []
            for i in range(1, len(persistent.mm_chars[self.id_char])):
                lst0.append(persistent.mm_chars[self.id_char][i])

            for k in mm_clot_dict[self.id_char]:
                if k in lst0:
                    lst1.append(k)

            return lst1

        def get_render_list(self, iter=1):
            # выводит список слоёв одежды в порядке наложения
            clot, cur = self.get_current()
            if clot is None:
                # print ('0 - нет персонажа')
                return []

            full = mm_clot_dict[self.id_char][clot].get_btn_list(self.id_char, clot)[0]

            # print set(full.keys()) - set(cur.keys()), set(cur.keys()) - set(full.keys())

            if any([set(full.keys()) - set(cur.keys()), set(cur.keys()) - set(full.keys())]):
                return mm_clot_dict[self.id_char][clot].get_menu_rdr(full, iter)
            else:
                return mm_clot_dict[self.id_char][clot].get_menu_rdr(cur, iter)

        def get_info(self, clot, var):
            if self.id_char not in mm_clot_dict:
                # print ('Персонаж', self.name, 'отсутствует в списке одежды для меню')
                return None

            if clot not in mm_clot_dict[self.id_char]:
                # print ('тип одежды', id_clot, 'для персонажа', self.name, 'отсутствует в списке одежды для меню')
                return None

            full = mm_clot_dict[self.id_char][clot].get_btn_list(self.id_char, clot)[0]

            # print set(full.keys()) - set(cur.keys()), set(cur.keys()) - set(full.keys())

            if any([set(full.keys()) - set(var.keys()), set(var.keys()) - set(full.keys())]):
                return mm_clot_dict[self.id_char][clot].get_pref_rdr(full)
            else:
                return mm_clot_dict[self.id_char][clot].get_pref_rdr(var)

        def set_current(self, clot, var):
            persistent.mm_chars[self.id_char][0] = (clot, var)

        def get_btn_list(self, clot):
            if self.id_char not in mm_clot_dict:
                # print ('Персонаж', self.name, 'отсутствует в списке одежды для меню')
                return []

            if clot not in mm_clot_dict[self.id_char]:
                # print ('тип одежды', id_clot, 'для персонажа', self.name, 'отсутствует в списке одежды для меню')
                return []

            return mm_clot_dict[self.id_char][clot].get_btn_list(self.id_char, clot)[1]

        def get_full(self, clot):
            return mm_clot_dict[self.id_char][clot].get_btn_list(self.id_char, clot)[0]

    def set_mm_clot(char, clot, var):
        menu_chars[char].set_current(clot, var)

    Set_mm_clot = renpy.curry(set_mm_clot)

    mm_clot_dict = {
        'max'   : OrderedDict([
            ('casual_c', MMClot([('b', MMIoC(1, '01c', '01c', _("Шорты"), 1, over='lb', nc=0)),
                                 ('lb', MMIoC(1, '02', '01d', _("Трусы"), 1, 1, nc=0))])),
            ('new_year', MMClot([('h', MMIoC(2, '05a', '01x1', _("Шапка"), nc=0)),
                                 ('a1', MMIoC(12, '05b', '01x2', _("Борода"), nc=0)),
                                 ('b1', MMIoC(1, '05c', '01x3', _("Трусы #1"), ex=1, eq='b2', nc=0)),
                                 ('b2', MMIoC(1, '05d', '01x4', _("Трусы #2"), ex=1, eq='b1', nc=0))])),
            ]),
        'alice' : OrderedDict([
            ('casual_d', MMClot([('t', MMIoC(2, '01e1', '01a1', _("Маечка"), 1)),
                                 ('b', MMIoC(1, '02h', '01a2', _("Минишортики"), 1, 1)),
                                 ('t+b', MMIoC(0, '01e', '01a', f=1))])),
            ('swim',     MMClot([('lt', MMIoC(2, '03b1', '01b1', _("Лиф"), 1)),
                                 ('lb', MMIoC(1, '03b', '01b2', _("Плавки"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '03', f=1))])),
            ('sleep0',   MMClot([('lt', MMIoC(2, '02i2', '01c1', _("Лифчик"), 1)),
                                 ('lb', MMIoC(1, '02i3', '01c2', _("Трусики"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '02i1', f=1))])),
            ('sleep1',   MMClot([('lt', MMIoC(2, '02j2', '01d1', _("Лифчик"), 1)),
                                 ('lb', MMIoC(1, '02j3', '01d2', _("Трусики"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '02j1', f=1))])),
            ('new_year', MMClot([('h', MMIoC(1, '05a', '01x1', _("Шапочка"), nc=0)),
                                 ('a1', MMIoC(2, '05b', '01x2', _("Бант на шею"), nc=0)),
                                 ('dr', MMIoC(4, '05d', '01x4', _("Кружевное платье"))),
                                 ('lb', MMIoC(3, '05e', '01x5', _("Трусики"), ex=1)),
                                 ('st', MMIoC(5, '05f', '01x6', _("Чулочки"))),
                                 ('dr+lb', MMIoC(4, '05c', '01x3'))])),
            ]),
        'ann'   : OrderedDict([
            ('casual_d', MMClot([('t', MMIoC(3, '02h', '01a1', _("Топик"), 1)),
                                 ('b', MMIoC(2, '02g', '01a2', _("Шортики"), 1, over='lb')),
                                 ('lb', MMIoC(1, '02b', '01c2', _("Трусики"), 1, 1)),
                                 ('t+b', MMIoC(0, '01e', f=1)),
                                 ('t+lb', MMIoC(0, '02i', f=1))])),
            ('swim',     MMClot([('lt', MMIoC(1, '03a1', '01b1', _("Лиф"), 1)),
                                 ('lb', MMIoC(2, '03a2', '01b2', _("Плавки"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '03', f=1))])),
            ('sleep0',   MMClot([('lt', MMIoC(1, '02a', '01c1', _("Лифчик"), 1)),
                                 ('lb', MMIoC(2, '02b', '01c2', _("Трусики"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '02', f=1))])),
            ('new_year', MMClot([('h', MMIoC(1, '00x1', '01x1', _("Шляпка"), nc=0)),
                                 ('a1', MMIoC(6, '00x2', '01x2', _("Бабочка на шею"), nc=0)),
                                 ('dr', MMIoC(5, '00x3', '01x3', _("Кружевное платье"), over='b, a2')),
                                 ('a2', MMIoC(4, '00x4', '01x4', _("Мишура на груди"))),
                                 ('b', MMIoC(3, '00x5', '01x5', _("Шортики"), ex=1))])),
            ]),
        'kira'  : OrderedDict([
            ('casual_d', MMClot([('t', MMIoC(1, '01a1', '01a1', _("Лиф"), 1)),
                                 ('b', MMIoC(2, '01a2', '01a2', _("Минишортики"), 1, 1)),
                                 ('t+b', MMIoC(0, '01a', f=1))])),
            ('swim',     MMClot([('lt', MMIoC(1, '03b', '01b1', _("Минилиф"), 1)),
                                 ('lb', MMIoC(2, '03c', '01b2', _("Миниплавки"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '03', f=1))])),
            ('sleep0',   MMClot([('lt', MMIoC(2, '02b', '01c1', _("Сорочка"), 1)),
                                 ('lb', MMIoC(1, '02a', '01c2', _("Трусики"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '02', '01c', f=1))])),
            ('new_year', MMClot([('h', MMIoC(1, '05a', '01x1', _("Шапочка"), nc=0)),
                                 ('dr', MMIoC(2, '05b', '01x2', _("Свитер без рукавов"), eq='br', over='lb')),
                                 ('br', MMIoC(2, '05c', '01x3', _("Откровенный корсет"), eq='dr')),
                                 ('lb', MMIoC(3, '05d', '01x4', _("Трусики"), ex=1)),
                                 ('a1', MMIoC(4, '05e', '01x5', _("Браслетики на запястья"), nc=0))])),
            ]),
        'lisa'  : OrderedDict([
            ('casual_d', MMClot([('t', MMIoC(3, '01c3', '01a1', _("Топик"), 1)),
                                 ('b', MMIoC(2, '01c1', '01a2', _("Юбочка"), 1, over='lb')),
                                 ('lb', MMIoC(1, '02c', '01c3', _("Трусики"), 1, 1)),
                                 ('t+b', MMIoC(0, '01c', f=1)),
                                 ('t+lb', MMIoC(0, '01c2', f=1))])),
            ('swim',     MMClot([('lt', MMIoC(1, '03d1', '01b1', _("Лиф"), 1)),
                                 ('lb', MMIoC(2, '03d', '01b2', _("Плавки"), 1, 1)),
                                 ('lt+lb', MMIoC(0, '03b', f=1))])),
            ('sleep0',   MMClot([('t', MMIoC(2, '02b', '01c1', _("Маечка"), 1)),
                                 ('b', MMIoC(1, '02c1', '01c2', _("Штанишки"), 1, 1, eq='lb')),
                                 ('lb', MMIoC(1, '02c', '01c3', _("Трусики"), 1, 1, eq='b')),
                                 ('t+b', MMIoC(0, '02', f=1)),
                                 ('t+lb', MMIoC(0, '02a', f=1))])),
            ('new_year', MMClot([('h', MMIoC(5, '05a', '01x1', _("Шапочка"), nc=0)),
                                 ('a1', MMIoC(4, '05b', '01x5', _("Леденец на шею"), nc=0)),
                                 ('t', MMIoC(1, '05c', '01x2', _("Свитер с рукавами"))),
                                 ('b', MMIoC(3, '05d', '01x4', _("Колготки"), over='lb')),
                                 ('lb', MMIoC(2, '05e', '01x3', _("Трусики"), ex=1))])),
            ]),
        }

    mm_cookies = [
        # персонаж, одежда, комната, дни недели, время от и до, координаты печеньки, масштаб печеньки, прозрачность печеньки, номер печеньки костюма, доп.условие
        MM_Cookies('ann', 'swim', 'house[6]', '0', '14:00', '14:59', (1150, 40), 0.75, 0.6),
        MM_Cookies('kira', 'swim', 'house[6]', '5', '11:00', '12:59', (1753, 723), 0.75, 0.6),
        ]

    mm_cookies_events = [
        # персонаж, одежда, комната, дни недели, время от и до, координаты печеньки, масштаб печеньки, прозрачность печеньки, номер печеньки костюма, доп.условие
        MM_Cookies('lisa', 'casual_d', 'house[0]', '4', '23:00', '23:59', (310, 0), 0.8, req="lisa.dress=='d'"),
        MM_Cookies('lisa', 'swim', 'house[0]', '0,1,2,3,4,5,6', '15:00', '17:30', (1820, 470), 0.8, 0.8, req="'c' in pose"),
        MM_Cookies('lisa', 'sleep0', 'house[0]', '0,1,2,3,4,5,6', '00:00', '01:00', (518, 7), 0.6, 0.8, req="renpy.showing('BG char Lisa horror-myroom 01a')"),
        MM_Cookies('lisa', 'new_year', 'house[0]', '2,5', '20:30', '21:59', (60, 13), 0.75, 0.5),

        MM_Cookies('alice', 'casual_d', 'house[4]', '3', '22:00', '23:59', (457, 206), 0.5, 0.8, req="alice.dress=='d'"),
        MM_Cookies('alice', 'swim', 'house[6]', '4', '15:00', '15:59', (165, 614), 0.75, 0.8, req="renpy.showing('BG char Alice sun-alone 05')"),
        MM_Cookies('alice', 'sleep0', 'house[0]', '0,1,2,3,4,6', '02:00', '04:00', (1793, 501), 0.5, 0.35, req="alice.dress=='a'"),
        MM_Cookies('alice', 'sleep1', 'house[0]', '0,1,2,3,4,6', '02:00', '04:00', (1820, 30), 0.5, 0.35, req="alice.dress=='b'"),
        MM_Cookies('alice', 'new_year', 'house[6]', '1,2,3,4,5', '13:00', '15:59', (1827, 367), 0.75, 0.5, req="renpy.showing('BG punish-sun 03')"),

        MM_Cookies('ann', 'casual_d', 'house[5]', '0,1,2,3,4,5,6', '19:00', '19:59', (754, 596), 0.75, req="ann.dress=='d' and not check_is_home('eric')"),
        MM_Cookies('ann', 'sleep0', 'house[6]', '1,3', '7:0', '7:59', (5, 730), 0.6, 0.4, req="renpy.showing('BG char Ann yoga 02')"),
        MM_Cookies('ann', 'new_year', 'house[4]', '0', '21:00', '21:59', (25, 207), 0.75, 0.3, req="renpy.showing('BG tv-mass-03')"),

        MM_Cookies('kira', 'casual_d', 'house[5]', '6', '09:00', '09:59', (960, 587), 0.75),
        MM_Cookies('kira', 'sleep0', 'house[4]', '0,3', '03:00', '03:59', (119, 423), 0.75, 0.3, req="renpy.showing('BG tv-kiss-03')"),
        MM_Cookies('kira', 'new_year', 'house[6]', '6', '03:00', '03:59', (95, 390), 0.75, 0.7, req="renpy.showing('BG char Kira after-club-s02-f')"), #(126, 561)
        ]

    def open_cookies():

        if datetime.today().month in [1, 2, 12]:
            # open New_Year
            menu_chars['Max'].open('new_year')
            menu_chars['Alice'].open('new_year')
            menu_chars['Ann'].open('new_year')
            menu_chars['Kira'].open('new_year')
            menu_chars['Lisa'].open('new_year')
        else:
            menu_chars['Max'].close('new_year')
            menu_chars['Alice'].close('new_year')
            menu_chars['Ann'].close('new_year')
            menu_chars['Kira'].close('new_year')
            menu_chars['Lisa'].close('new_year')

        # open casual
        menu_chars['Max'].open('casual_c')
        menu_chars['Alice'].open('casual_d')
        menu_chars['Ann'].open('casual_d')
        menu_chars['Kira'].open('casual_d')
        menu_chars['Lisa'].open('casual_d')

        if len(persistent.mm_cookies) < 4:
            return

        if 'kira' in persistent.mems_var and 'swim' not in menu_chars['Kira'].get_open_clot():
            # купальники
            if all(['casual_d' in persistent.mm_cookies['lisa'],
                    'casual_d' in persistent.mm_cookies['alice'],
                    'casual_d' in persistent.mm_cookies['ann'],
                    'casual_d' in persistent.mm_cookies['kira']]):
                menu_chars['Lisa'].open('swim')
                menu_chars['Alice'].open('swim')
                menu_chars['Ann'].open('swim')
                menu_chars['Kira'].open('swim')

        if 'kira' in persistent.mems_var and 'sleep0' not in menu_chars['Kira'].get_open_clot():
            # нижнее бельё
            if all(['swim' in persistent.mm_cookies['lisa'],
                    'swim' in persistent.mm_cookies['alice'],
                    'swim' in persistent.mm_cookies['ann'],
                    'swim' in persistent.mm_cookies['kira']]):
                menu_chars['Lisa'].open('sleep0')
                menu_chars['Alice'].open('sleep0')
                menu_chars['Alice'].open('sleep1')
                menu_chars['Ann'].open('sleep0')
                menu_chars['Kira'].open('sleep0')

default persistent.mm_chars = {}
default persistent.mm_cookies = {}

define menu_chars = OrderedDict([
    ('Max'  , MenuClothes('max', _("Макс"))),
    ('Ann'  , MenuClothes('ann', _("Анна"))),
    ('Lisa' , MenuClothes('lisa', _("Лиза"))),
    ('Kira' , MenuClothes('kira', _("Кира"))),
    ('Alice', MenuClothes('alice', _("Алиса"))),
    ])

default mm_char = sorted(menu_chars)[0]

# установка "открытия" одежды главного меню
init 100 python:
    if 'kira' in persistent.mems_var:
        if not persistent.menu_var:
            persistent.menu_var = '01'
            persistent.mm_chars.clear()

        if datetime.today().month in [1, 2, 12]:
            # open New_Year
            menu_chars['Max'].open('new_year')
            menu_chars['Alice'].open('new_year')
            menu_chars['Ann'].open('new_year')
            menu_chars['Kira'].open('new_year')
            menu_chars['Lisa'].open('new_year')
        else:
            menu_chars['Max'].close('new_year')
            menu_chars['Alice'].close('new_year')
            menu_chars['Ann'].close('new_year')
            menu_chars['Kira'].close('new_year')
            menu_chars['Lisa'].close('new_year')

        # open casual
        menu_chars['Max'].open('casual_c')
        menu_chars['Alice'].open('casual_d')
        menu_chars['Ann'].open('casual_d')
        menu_chars['Kira'].open('casual_d')
        menu_chars['Lisa'].open('casual_d')
