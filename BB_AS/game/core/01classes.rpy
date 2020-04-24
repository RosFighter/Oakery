init python:

    # ключ для сортировки списка с расписанием - время начала действия
    def SortByTime(inputStr):
        return inputStr.ts


    # ключ для сортировки списка с расписанием - дата и время начала действия
    def SortByDayTime(inputStr):
        return str(inputStr[0]) + '_' + inputStr[1]


    ############################################################################
    class Schedule:  # действие в расписании персонажа
        """ действие расписания персонажа для укладки в список
            блоки на один и тот же период с разным сдвигом в одном периоде или
            на разные значения в вычисляемом variable ВСЕГДА дожны добавляться одним блоком """

        def __init__(self, lod, ts, te, name, desc="", loc="", room="", label="", krat=1, shift=0, weekstart=0, variable="True", enabletalk=True, talklabel=None, glow=0):
            self.lod        = lod # lod - кортеж дней недели для действия
            # ts – время начала действия
            h, m = ts.split(':') if str(ts).find(':') > 0 else str(float(ts)).replace('.', ':').split(':')
            self.ts         = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]

            h, m = te.split(':') if str(te).find(':') > 0 else str(float(te)).replace('.', ':').split(':')
            self.te         = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]
            # te – время окончания действия
            self.name       = name       # наименование действия
            self.desc       = desc       # описание действия
            self.loc        = loc        # локация
            self.room       = room       # комната в локации
            self.label      = label      # имя блока обработки события (формирует сцену или запускает действие)
            self.krat       = krat       # периодичность в неделях
            self.shift      = shift      # для недель, имеющих периодичность; сдвиг относительно стартовой недели (начинается с 0)
            self.weekstart  = weekstart  # номер стартовой недели
            self.variable   = variable   # строка с логическим выражением, вычисляется при получиении текущего мемстоположения персонажа
            self.enabletalk = enabletalk # возможность разговора
            self.talklabel  = talklabel  # блок обработки начала диалога (формирует сцену старта диалога)
            self.glow       = glow       # коэффициент эмоционального накала (интерес зрителей)

        def __repr__(self):
            return "{self.name}, по дням: {self.lod}, с {self.ts}, до {self.te}, \"{self.desc}\", в {self.loc}[{self.room}], каждые {self.krat} "\
                    "нед., со сдвигом {self.shift}, начиная с {self.weekstart} недели".format(self=self)


    class SexStat:  # статистика сексуальных отношений
        def __init__(self, hand=0, foot=0, blow=0, boob=0, vm=0, mast=0, anal=0, vaginal=0, exhibit=0, lesbian=0, trio=0, orgy=0, sm=0, dm=0):
            self.hand    = hand      # hand_job "ручная работа"
            self.foot    = foot      # foot_job "работа" ножками
            self.blow    = blow      # blow_job минет
            self.boob    = boob      # boob_job дрочка грудью
            self.vm      = vm        # вуайеризм
            self.mast    = mast      # мастурбация
            self.anal    = anal      # анал
            self.vaginal = vaginal   # традиционный секс
            self.exhibit = exhibit   # эксгибиционизм
            self.lesbian = lesbian   # лесбийские игры
            self.trio    = trio      # секс втроём
            self.orgy    = orgy      # больше 3-х участников
            self.sm      = sm        # подчинение
            self.dm      = dm        # доминирование

        def __repr__(self):
            return "ручками: {self.hand}, ножками: {self.foot}, минет: {self.blow}, грудью: {self.boob}, "\
                    "вуайеризм: {self.vm}, мастурбация: {self.mast}, анал: {self.anal}, секс: {self.vaginal}, "\
                    "эксгибиционизм: {self.exhibit}, втроём: {self.trio}, оргия: {self.orgy}, подчинение: {self.sm}, "\
                    "доминирование: {self.dm}".format(self=self)


    class Profile():  # Описание и характеристики персонажа (не ГГ)
        def __init__(self, name, name_1, name_2, name_3, name_4, name_5, desc='', pref='', mood=0, relmax=0):
            self.name      = name      # имя
            self.name_1    = name_1    # имя в родительном падеже (от кого?)
            self.name_2    = name_2    # имя в дательном падеже (кому?)
            self.name_3    = name_3    # имя в винительном падеже (про кого?)
            self.name_4    = name_4    # имя в творительном падеже (с кем?)
            self.name_5    = name_5    # имя в предложном падеже (о ком?)
            self.desc      = desc      # описание
            self.pref      = pref      # префикс (папка) изображений

            self.sleeptoples = False
            self.sleepnaked  = False

            self.nopants   = False
            self.naked     = False

            self.dress     = 'a'
            self.dress_inf = '01a'     # суфикс изображения в окно описания

            self.mood      = mood      # текущее настроение
            self.relmax    = relmax    # уровень отношений с ГГ
            self.ri        = 0         # (romantic interest) заинтересованность
            self.free      = 0         # текущая раскрепощенность (для Эрика – None)
            self.releric   = None      # уровень отношений с Эриком (для Эрика – None)
            self.infmax    = None      # влияние Макса (для Эрика – None)
            self.inferic   = None      # влияние Эрика (для Эрика – None)
            self.gifts     = []        # полученные подарки
            self.attention = 0         # день, когда последний раз было уделено внимание персонажу

            self.plan      = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]  # расписание персонажа
            self.sex_stat  = SexStat()  # статистика сексульных отношений

            self.plan_name = 'None'  # наименование текущего действия для ускорения сранений. Обновляется при каждом запросе расписания с текущей датой/временем

        def GetMood(self): # возвращает кортеж с номером и описанием диапазона настроения персонажа
            mood = self.mood
            return {
                       mood <= -285 : (-4, _("Ужасное")),
                -285 < mood <= -165 : (-3, _("Очень плохое")),
                -165 < mood <= -75  : (-2, _("Плохое")),
                -75  < mood <= -15  : (-1, _("Не очень")),
                -15  < mood <=  15  : (0, _("Нейтральное")),
                 15  < mood <=  75  : (1, _("Неплохое")),
                 75  < mood <=  165 : (2, _("Хорошее")),
                165  < mood <=  285 : (3, _("Очень хорошее")),
                285  < mood         : (4, _("Прекрасное")),
                }[True]

        def __repr__(self):
            return "имя: {self.name}, \nописание: {self.desc},\n папка изображений=\"{self.pref}\", тек.изобр.=\"{self.dress_inf}\","\
                    " настроение: {self.mood}, раскрепощенность: {self.free}, отношения с Максом: {self.relmax}, "\
                    "отношения с Эриком: {self.releric}, влияние Эрика: {self.inferic}".format(self=self)

        # добавляет в расписание запись или блок связанных записей
        def add_sched_rec(self, *add_rec):
            new_plan = []
            if type(add_rec[0]) == list:
                zap = add_rec[0][0]
            else:
                zap = add_rec[0]
            for rec in self.plan:
                edited = False
                if (rec.ts <= zap.ts < rec.te) or (zap.ts <= rec.ts < zap.te): # время записей пересекается
                    for d in zap.lod:  # перебираем кортеж дней
                        if d in rec.lod:      # если день входит в кортеж записей, запись нужно изменять
                            edited = True
                            break
                if edited:  # в новый план запись вставляется в измененном виде
                    # сначала отберем дни, незатронутые изменениями
                    list_of_day = tuple(d for d in rec.lod if d not in zap.lod)
                    if len(list_of_day):  # есть дни, не затронутые изменениями
                        new_plan.append(Schedule(list_of_day, rec.ts, rec.te, rec.name, rec.desc, rec.loc, rec.room, rec.label,
                                                 rec.krat, rec.shift, rec.weekstart, rec.variable, rec.enabletalk, rec.talklabel,
                                                 rec.glow))
                    list_of_day = tuple(d for d in rec.lod if d in zap.lod)
                    if rec.ts < zap.ts < rec.te and len(list_of_day):  # часть перед новой записью
                        new_plan.append(Schedule(list_of_day, rec.ts, add_time(zap.ts, -1), rec.name, rec.desc, rec.loc,
                                                 rec.room, rec.label, rec.krat, rec.shift, rec.weekstart, rec.variable,
                                                 rec.enabletalk, rec.talklabel, rec.glow))
                    if rec.ts < zap.te < rec.te and len(list_of_day):  # часть после новой записи
                        new_plan.append(Schedule(list_of_day, add_time(zap.te), rec.te, rec.name, rec.desc, rec.loc,
                                                 rec.room, rec.label, rec.krat, rec.shift, rec.weekstart, rec.variable,
                                                 rec.enabletalk, rec.talklabel, rec.glow))
                else:  # копируем запись в новый план как есть
                    new_plan.append(rec)

            for rec in add_rec:
                if type(rec) == list:
                    new_plan.extend(rec)
                else:
                    new_plan.append(rec)
            new_plan.sort(key=SortByTime)
            self.plan.clear()
            self.plan.extend(new_plan)

        # добавляет в расписание список записей
        def add_schedule(self, *added_plan):
            #переберем новый список в поиске записей совпадающих по дням недели и времени, но различающихся условием или сдвигом недели
            new_list = []
            block = []
            for pl in added_plan:
                nayden = False
                for nl in new_list:
                    if pl.lod == nl.lod and pl.ts == nl.ts and pl.te == nl.te:
                        nayden = True
                        block.append([nl, pl])
                        new_list.remove(nl)
                if not nayden:
                    for bl in block:
                        if bl[0].lod == pl.lod and bl[0].ts == pl.ts and bl[0].te == pl.te:
                            nayden = True
                            bl.append(pl)
                if not nayden:
                    new_list.append(pl)

            # добавим отдельные записи
            for nl in new_list:
                self.add_sched_rec(nl)

            # добавим блок связанных записей
            for bl in block:
                self.add_sched_rec(bl)

        # Возвращает запись с текущим действием персонажа
        #     Аргументы:
        #     day      - день (целое),
        #     tm     - время в формате 'hh:mm',
        #     week     - номер недели (целое)
        def get_plan(self, d='', t=''):
            global day, tm
            d1 = d if d!='' else day
            tm1 = t if t!='' else tm
            h, m = tm1.split(':')  # нормализуем время на всякий случай
            tm1 = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]
            d1 += 2  # в игре отсчет начинается со среды и дня под номером 1
            rez = []
            for sh in self.plan:
                if ((sh.ts <= tm1 <= sh.te) and (d1 % 7 in sh.lod) and (d1 / 7 >= sh.weekstart) and
                    (((d1 // 7) - sh.weekstart) % sh.krat == sh.shift) and (eval(sh.variable))):
                        rez.append(sh)

            if len(rez) > 1:
                print("ошибочка-с...", rez)
            elif len(rez) == 0:
                return None
            else:
                if d=='' and t=='':
                    self.plan_name = rez[0].name
                return rez[0]

        # Возвращает список записей с текущим действием персонажа
        # Аргументы:
        # schedule - список записей с расписанием,
        # d1      - день (целое),
        # tm1     - время в формате 'hh:mm',
        # week     - номер недели (целое)
        def get_plan_list(self, d1, tm1): # только для тестирования расписания
            h, m = tm1.split(':')  # нормализуем время на всякий случай
            tm1 = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]
            d1 += 2  # в игре отсчет начинается со среды и дня под номером 1
            rez = []
            for sh in self.plan:
                if ((sh.ts <= tm1 <= sh.te) and (d1 % 7 in sh.lod) and (d1 / 7 >= sh.weekstart) and
                    (((d1 // 7) - sh.weekstart) % sh.krat == sh.shift) and (eval(sh.variable))):
                        rez.append(sh)

            return rez

        # функция для разработчика, проверяет расписание на перехлесты
        def verify_schedule(self):
            max_krat = 1
            max_week = 0
            for sh in schedule:  # определяем неделю старта теста и максимальную длительность в неделях (кратность)
                max_krat = max(max_krat, sh.krat)
                max_week = max(max_week, sh.weekstart)

            errors = set()
            skipped = set()

            kolve = (max_week + max_krat) * 7 * 2

            for d1 in range(max_week*7, kolve):  # удваиваем диаппазон на всякий случай
                start_skip = end_skip = ''
                for hour in range(24):
                    for minute in range(60):
                        tm1 = '{0}:{1}'.format(('0' + str(hour))[-2:], ('0' + str(minute))[-2:])
                        temp_list = self.get_plan_list(d1, tm1)

                        if len(temp_list) > 1:
                            for tl in temp_list:
                                errors.add(tl)
                        elif len(temp_list) == 0:
                            if start_skip == '':
                                start_skip = tm1
                            elif end_skip == '' or add_time(end_skip) == tm1:
                                end_skip = tm1
                        elif end_skip != '':
                            skipped.add(((d1 % 7,), start_skip, end_skip))
                            start_skip = end_skip = ''

            skip_list = []
            skipped = list(skipped)
            while len(skipped):
                start_skip = end_skip = ''
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


    ############################################################################
    class Loan:
        def __init__(self):
            self.level    = 0      # уровень доступного кредита
            self.amount   = 0      # выдан займ на сумму
            self.debt     = 0      # непогашенный остаток
            self.fines    = False  # начислен штраф
            self.left     = 0      # дней до начисления штрафа

        def issue(self, sum):  # выдать займ на сумму
            self.amount = sum
            self.debt   = int(sum * 1.1)
            self.left   = 30

        def repay(self):  # полностью погасить займ
            if self.fines:
                self.level = 0
            elif self.amount == 500 and self.level == 1:
                self.level = 2
            elif self.amount == 1000 and self.level == 2:
                self.level = 3
            elif self.amount == 2000 and self.level == 3:
                self.level = 4
            self.amount = 0
            self.debt = 0
            self.left = 0

        def part(self, sum):  # погасить часть займа на сумму
            if sum < self.debt:
                self.debt -= sum
            else:
                self.repay()

        def charge(self):   # начислим штраф в размере тройной суммы оставшегося долга
            self.debt = self.debt * 3
            self.fines = True
            self.left = 30


    class MaxProfile:
        """ Здесь будут описание и характеристики Макса"""

        def __init__(self, name, name_1, name_2, name_3, name_4, name_5, desc='', img=''):
            self.name        = name        # имя
            self.name_1      = name_1      # имя в родительном падеже (от кого?)
            self.name_2      = name_2      # имя в дательном падеже (кому?)
            self.name_3      = name_3      # имя в винительном падеже (про кого?)
            self.name_4      = name_4      # имя в творительном падеже (с кем?)
            self.name_5      = name_5      # имя в предложном падеже (о ком?)
            self.desc        = desc        # описание
            self.img         = img         # изображение в окно описания
            self.energy      = 100.0       # запас сил, энергия
            self.training    = 20.0        # тренированность
            self.cleanness   = 70.0        # чистота
            self.social      = 8.0         # навыки убеждения
            self.massage     = 0.0         # навыки массажа
            self.ero_massage = 0.0         # навыки эро.массажа
            self.stealth     = 9.0         # навык скрытности
            self.kissing     = 0.0         # навык поцелуев
            self.cuni        = 0.0         # опыт куни
            self.sex         = 0.0         # сексуальный опыт
            self.anal        = 0.0         # опыт анального секса
            self.dress       = "a"         # суфикс файлов одежды ("a", "b", "c"...)

            self.__tange   = 150

            self.__account = 0 # состояние счета на сайте
            self.invited = 0 # привлечено зрителей за счет рекламы

            self.credit    = Loan()

        @property
        def money(self):
            return self.__tange

        @property
        def account(self):
            return self.__account

        def ask(self, lvl):   # просим денег
            self.__tange += {
                0: 10,
                1: 20,
                2: 40,
                3: 60,
                4: 115,
                5: 50,
                6: 100,
                7: 150,
                8: 200,
                9: 500,
                }[lvl]

        def pay(self, sum):   # оплачиваем услуги
            if abs(sum) <= self.__tange:
                self.__tange -= int(abs(sum))

        def buy_promoution(self): # Покупка пакета рекламы
            if self.__tange >= 50:
                self.__tange -= 50
                ef = 10 + renpy.random.randint(-100, 100)/100.0 # процент эффективности рекламы
                k = 0
                for loc in locations:
                    for room in locations[loc]:
                        for cam in room.cams:
                            if cam.grow < 100:
                                cam.grow = 100
                            if cam.HD:
                                ef += 10.0 / (1 + k) # каждая HD-камера немного повышает эффективность рекламы
                self.invited += int(round(10000 * ef / 100.0, 0))
                notify_list.append(_("Приобретен пакет рекламы"))

        def income(self, earn):
            self.__account += earn  # прибыль с сайта

        def withdraw(self): # выплата с сайта
            self.__tange += int(self.__account)
            self.__account -= int(self.__account)

        def credit_repay(self):
            if self.__tange >= self.credit.debt:
                self.__tange -= self.credit.debt
                self.credit.repay()

        def credit_getting(self, sum):
            self.credit.issue(abs(sum))
            self.__tange += abs(sum)

        def credit_part(self, sum):
            if self.__tange >= sum:
                self.__tange -= sum
                self.credit.part(sum)

        def __repr__(self):
            return "имя: {self.name}, описание: {self.desc}, изображение=\"{self.img}\", "\
            "\nзапас сил: {self.energy}, тренированность: {self.training}, чистота: {self.cleanness}, "\
            "\nубежд: {self.social}, массаж: {self.massage}, эро.массаж: {self.ero_massage}"\
            "\nскрыт: {self.stealth}, опыт поцелуев: {self.kissing}, куни: {self.cuni}"\
            "секс: {self.sex}, анал: {self.anal}".format(self=self)


    ############################################################################
    ############################################################################
    class Room:  # описание комнат в каждой локации (дом, школа, кафе и т.п.)
        def __init__(self, id, name, cam_name, icon="", max_cam=1, cur_bg="", cur_char=[]):
            self.id            = id        # идентификатор (идентификатор конкретной комнаты в локации {my_room, alice_room...})
            self.name          = name      # Наименование для окна навигации
            self.cam_name      = cam_name  # Наименование для камер
            self.icon          = icon      # миниатюра для окна навигации
            self.max_cam       = max_cam   # максимально возможное количество установленных камер для данной комнаты
            self.cams          = []        # список камер, установленных в комнате
            self.cur_bg        = cur_bg    # текущий фон для комнаты
            self.cur_char      = cur_char  # список персонажей, находящихся в комнате в данный момент

        def __repr__(self):
            return "id: {self.id}, наименование: {self.name}, миниатюра=\"{self.icon}\", фон: {self.cur_bg}, "\
            "персонажи в комнате: {self.cur_char}".format(self=self)


    ############################################################################
    class ActionsButton:
        """ класс-формат для объявления списка доступных действий """

        def __init__(self, sing="", icon="", label="", enabled=False):
            self.sing    = sing    # подпись кнопки
            self.icon    = icon    # иконка кнопки
            self.label   = label   # имя блока обработки события
            self.enabled = enabled # доступна ли кнопка в целом (задается событиями)
            self.active  = False   # доступна ли кнопка в данной локации или с данным персонажем
                                   # для отображения кнопки должны быть истинны оба условия

        def __repr__(self):
            return "Кнопка: {self.sing} с иконкой \"{self.icon}\" запускает метку {self.label}. {self.enabled}".format(self=self)


    ############################################################################
    class Item:
        """ класс-формат описания предметов как в инвентаре, так и доступных для заказа в ИМ """

        def __init__(self, name, desc="", img="", category="", price=0, InShop=False, have=False, bought=False, delivery=0, need_read=0, cells=1):
            self.name      = name      # наименование (в магазине и в сумке)
            self.desc      = desc      # описание
            self.img       = img       # изображение
            self.category  = category  # номер категории магазина
            self.price     = price     # цена в магазине
            self.InShop    = InShop    # доступно к приобретению
            self.have      = have      # есть в сумке
            self.bought    = bought    # куплено, но еще не доставлено
            self.delivery  = delivery  # доставка через .. дней
            self.need_read = need_read # если больше нуля - признак книги. Сколько циклов чтения нужно
            self.read      = 0         # сколько раз уже прочитано
            self.cells     = cells     # занимаемые по вертикали ячейки (1 или 2)

        def buy(self): # выполняет покупку предмета из интернет-магазина
            mgg.pay(self.price)
            self.bought = True
            self.delivery = 1 if GetWeekday(day) != 6 else 2


        def __repr__(self):
            return "наименование=\"{self.name}\", описание: {self.desc}, изображение: {self.img}"\
            "цена: {self.price}, в магазине {self.InShop}, имеется {self.have}, куплено {self.bought}"\
            "доставка через {self.delivery}, прочитано {self.read}/{self.need_read}".format(self=self)


    ############################################################################
    class PossStage:  # Описание этапа возможности
        def __init__(self, image="", desc="", ps=""):
            self.image  = image # изображение в экран описания возможностей
            self.desc   = desc  # описание этапа возможности (в окно возможэностей)
            self.ps     = ps    # послесловие (мысли ГГ по поводу развития или сообщение о временном или постоянном окончании возможности)
            self.used   = False
        def __repr__(self):
            return "изображение=\"{self.image}\", описание: {self.desc}, послесловие: {self.ps}\n".format(self=self)


    ############################################################################
    class Poss:  # описание возможности
        def __init__(self, name, stages=[], stn=-1):
            self.name   = name    # Наименование (в экран описания возможностей)
            self.stages = stages  # список этапов возможности
            self.stn    = stn     # текущий этап
        def __repr__(self):
            return "Наименование=\"{self.name}\", текущий этап: {self.stn}, список этапов:\n {self.stages}".format(self=self)

        def SetStage(self, stage): # устанавливает этап "возможности"
            a = [1 for st in self.stages if st.used]

            self.stn = stage
            self.stages[stage].used = True

            if sum(a) == 0:
                notify_list.append(_("{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"))

        def OpenStage(self, stage): # открывает этап "возможности", если номер этапа больше текущего, устанавливает текущим новый этап
            a = [1 for st in self.stages if st.used]
            self.stages[stage].used = True
            if self.stn < stage:
                self.stn = stage
            if sum(a) == 0:
                notify_list.append(_("{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"))

    ############################################################################
    class TalkTheme:  # описание темы для разговора
        def __init__(self, char, select, label, req="False", mood=0, kd_id=""):
            self.char   = char    # персонаж, (или список персонажей) с которым должен вестись диалог
            self.select = select  # Фраза, которая будет отображаться в меню выбора диалога с персонажем
            self.label  = label   # Метка перехода при выборе пункта меню
            self.req    = req     # Условие, выполнение которого делает фразу доступной для отображения
            self.mood   = mood    # минимальное настроение для запуска разговора на эту тему
            self.kd_id  = kd_id   # идентификатор кулдауна
        def __repr__(self):
            return "стартовая фраза=\"{self.select}\", метка: {self.label}, условие: {self.req}".format(self=self)


    ############################################################################
    class Daily:
        def __init__(self, lost=0, done=False, enabled=False):
            self.lost    = lost     # осталось дней до срабатываения события
            self.enabled = enabled  # дейлик активен, нужно ежедневно убавлять счетчик до 0
            self.done    = done     # счетчик достиг 0, для проверки доступности диалога
            self.stage   = 0

        def set_lost(self, lost):
            self.lost = lost
            self.done = lost == 0

        def __repr__(self):
            return "Этап: {self.stage}, осталось дней: {self.lost}, выполнено: {self.done}, активно: {self.enabled}".format(self=self)


    ############################################################################
    class CutEvent:
        """ События, запускаемые в конкретное время"""
        def __init__(self, tm="", lod=(0, 1, 2, 3, 4, 5, 6), label="", desc="", variable="True", enabled=True, stage=0, sleep=False, extend=False, cut=False):
            h, m = tm.split(":") if str(tm).find(":") > 0 else str(float(tm)).replace(".", ":").split(":")
            self.tm        = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:] # время начала события

            self.lod      = lod      # кортеж дней недели для события
            self.label    = label    # имя блока обработки события
            self.desc     = desc     # описание события
            self.variable = variable # строка с логическим выражением, вычисляется при получиении события
            self.enabled  = enabled
            self.stage    = stage    # этап события. Если None - повторяемое
            self.sleep    = sleep    # для запуска нужно, чтобы Макс спал
            self.extend   = extend   # при выполнении условия, если Макс встает раньше наступления события, то продлевать сон
            self.cut      = cut      # прерывать сон при наступлении события

        def __repr__(self):
            return "\"{self.desc}\" стартует в {self.tm} по дням: {self.lod}, только если Макс спит {self.sleep}".format(self=self)


    ############################################################################
    class Helper:
        """ """
        def __init__(self, id, name, desc):
            self.id   = id
            self.name = name
            self.desc = desc

        def __repr__(self):
            return "\"{self.name}\" ({self.id}): {self.desc}".format(self=self)


    ############################################################################
    class HideCam:
        def __init__(self, HD = False):
            self.today    = 0      # прибыль за текущий день
            self.total    = 0      # полная прибыль, полученная с камеры
            self.public   = 0      # текущее количество зрителей
            self.grow     = 0      # прирост
            self.HD       = HD

        def __repr__(self):
            return "Прибыль: {self.total}({self.today}), зрителей: {self.public}, прирост: {self.grow}".format(self=self)


    ############################################################################


    ############################################################################
    class OnLineCource:
        def __init__(self, header, desc, total, price, grow):
            self.header = header  # Заголовок курса
            self.desc   = desc    # описание курса
            self.less   = 0       # пройдено лекций
            self.total  = total   # всего лекций
            self.price  = price   # цена
            self.grow   = grow    # максимальная эффективность занятия
            self.bought = False   # курс приобретен

        def buy(self):  # покупка онлайн-курса
            mgg.pay(self.price)
            self.bought = True


    class OnLineCources:
        def __init__(self, name, skill, img, cources):
            self.name    = name     # Наименование курса (общение, массаж)
            self.skill   = skill    # повышаемый параметр
            self.img     = img      # префикс изображений ("soc"+"-"+индекс курса+"-"+индекс части: soc-0-0, soc-0-1...)
            self.cources = cources  # список частей курса
            self.current = 0        # текущая часть курса

    ############################################################################


    class Gift:  # предметы-подарки
        def __init__(self, item, select, label, mood = -1, req='True'):
            self.item   = item    # id предмета-подарка
            self.select = select  # фраза в окне диалогов
            self.label  = label   # метка запуска диалога дарения
            self.req    = req
            self.mood   = mood


    class SorryGift:  # извинительные подарки
        def __init__(self):
            self.owe   = False  # Макс должен подарить извинительный подарок
            self.left  = 0      # осталось дней до наказания, если не вручит подарок
            self.give  = []     # ранее врученные извинительные подарки
            self.valid = set()  # множество ID товаров, допустимых в качестве извинений
            self.days  = []     # список дней, когда Макс оправдывался после подглядывания

        def start(self, d=1):
            self.owe = True
            self.left = d+1 if (day+d+2) % 7 == 0 else d
            self.days.insert(0, day)


    class Chance:
        def __init__(self, ch):
            self.ch  = {ch < 0 : 0, ch > 1000 : 1000, 0 <= ch <= 1000: ch}[True]
            self.col = {ch < 333 : red, ch > 666 : lime, 333 <= ch <= 666 : orange}[True]
            self.vis = str(int(ch/10)) + "%"
