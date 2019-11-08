init python:

    class Profile:  # Описание и характеристики персонажа (не ГГ)
        def __init__(self, name, name_1, name_2, name_3, name_4, name_5, desc="", icon="", img="", mood=0, ri=0, ri_text="", mindedness=None, relmax=0, releric=None, influence=None):
            self.name      = name      # имя
            self.name_1    = name_1    # имя в родительном падеже (от кого?)
            self.name_2    = name_2    # имя в дательном падеже (кому?)
            self.name_3    = name_3    # имя в винительном падеже (про кого?)
            self.name_4    = name_4    # имя в творительном падеже (с кем?)
            self.name_5    = name_5    # имя в предложном падеже (о ком?)
            self.desc      = desc      # описание
            self.icon      = icon      # миниатюра для окна навигации
            self.img       = img       # изображение в окно описания

            self.mood      = mood      # текущее настроение
            self.ri        = ri        # (romantic interest) заинтересованность
            self.ri_text   = ri_text   # текстовое описание текущего уровня заинтересованности
            self.mindedness= mindedness# текущая раскрепощенность (для Эрика – None)
            self.relmax    = relmax    # уровень отношений в ГГ
            self.releric   = releric   # уровень отношений с Эриком (для Эрика – None)
            self.influence = influence # влияние Эрика (для Эрика – None)
            self.talks     = []

        def __repr__(self):
            return "имя: {self.name}, \nописание: {self.desc},\n миниатюра=\"{self.icon}\", изображение=\"{self.img}\","\
                    " настроение: {self.mood}, раскрепощенность: {self.mindedness}, отношения с Максом: {self.relmax}, "\
                    "отношения с Эриком: {self.releric}, влияние Эрика: {self.influence}".format(self=self)


################################################################################
    class MaxProfile:
        """ Здесь будут описание и характеристики Макса"""

        def __init__(self, name, name_1, name_2, name_3, name_4, name_5, desc="", img=""):
            self.name        = name        # имя
            self.name_1      = name_1      # имя в родительном падеже (от кого?)
            self.name_2      = name_2      # имя в дательном падеже (кому?)
            self.name_3      = name_3      # имя в винительном падеже (про кого?)
            self.name_4      = name_4      # имя в творительном падеже (с кем?)
            self.name_5      = name_5      # имя в предложном падеже (о ком?)
            self.desc        = desc        # описание
            self.img         = img         # изображение в окно описания
            self.energy      = 100         # запас сил, энергия
            self.training    = 20          # тренированность
            self.cleanness   = 70          # чистота
            self.persuade    = 20          # навыки убеждения
            self.massage     = 0           # навыки массажа
            self.ero_massage = 0           # навыки эро.массажа
            self.stealth     = 20          # навык скрытности
            self.kissing     = 0           # навык поцелуев
            self.cunnilingus = 0           # опыт куни
            self.sex         = 0           # сексуальный опыт
            self.anal        = 0           # опыт анального секса

        def __repr__(self):
            return "имя: {self.name}, описание: {self.desc}, изображение=\"{self.img}\", "\
            "\nзапас сил: {self.energy}, тренированность: {self.training}, чистота: {self.cleanness}, "\
            "\nубежд: {self.persuade}, массаж: {self.massage}, эро.массаж: {self.ero_massage}"\
            "\nскрыт: {self.stealth}, опыт поцелуев: {self.kissing}, куни: {self.cunnilingus}"\
            "секс: {self.sex}, анал: {self.anal}".format(self=self)


################################################################################
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


################################################################################
    class Room:  # описание комнат в каждой локации (дом, школа, кафе и т.п.)
        def __init__(self, id, name, icon="", max_cam=1, cam_installed=0, cur_bg="", cur_char=[]):
            self.id            = id        # идентификатор (идентификатор конкретной комнаты в локации {my_room, alice_room...})
            self.name          = name      # Наименование для окна навигации
            self.icon          = icon      # миниатюра для окна навигации
            self.max_cam       = max_cam   # максимально возможное количество установленных камер для данной комнаты
            self.cam_installed = cam_installed  # установленно камер в комнате
            self.cur_bg        = cur_bg    # текущий фон для комнаты
            self.cur_char      = cur_char  # список персонажей, находящихся в комнате в данный момент

        def __repr__(self):
            return "id: {self.id}, наименование: {self.name}, миниатюра=\"{self.icon}\", фон: {self.cur_bg}, "\
            "персонажи в комнате: {self.cur_char}".format(self=self)


################################################################################
    class Schedule:  # действие в расписании персонажа
        """ действие расписания персонажа для укладки в список
            блоки на один и тот же период с разным сдвигом в одном периоде или
            на разные значения в вычисляемом variable ВСЕГДА дожны добавляться одним болоком
            Описание полей:
            lod       – кортеж дней недели для действия
            ts        – время начала действия
            te        – время окончания действия
            desc      – описание действия
            loc       – локация
            room      – комната в локации
            label     – имя блока обработки события
            krat      – периодичность в неделях
            shift     – для недель, имеющих периодичность - сдвиг относительно стартовой недели (начинается с 0)
            weekstart – номер стартовой недели
            variable  – строка с логическим выражением, вычисляется при получиении текущего мемстоположения персонажа """

        def __init__(self, lod, ts, te, desc="", loc="", room="", label="", krat=1, shift=0, weekstart=0, variable="True"):
            self.lod       = lod

            h, m = ts.split(":") if str(ts).find(":") > 0 else str(float(ts)).replace(".", ":").split(":")
            self.ts        = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:]

            h, m = te.split(":") if str(te).find(":") > 0 else str(float(te)).replace(".", ":").split(":")
            self.te        = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:]

            self.desc      = desc
            self.loc       = loc
            self.room      = room
            self.label     = label
            self.krat      = krat
            self.shift     = shift
            self.weekstart = weekstart
            self.variable  = variable

        def __repr__(self):
            return "дни: {self.lod}, с {self.ts}, до {self.te}, \"{self.desc}\", в {self.loc}[{self.room}], каждые {self.krat} "\
                    "нед., со сдвигом {self.shift}, начиная с {self.weekstart} недели".format(self=self)


################################################################################
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


################################################################################
    class Item:
        """ класс-формат описания предметов как в инвентаре, так и доступных для заказа в ИМ """

        def __init__(self, name, desc="", img="", category="", price=0, InShop=False, have=False, buy=False, delivery=0, need_read=0):
            self.name      = name      # наименование (в магазине и в сумке)
            self.desc      = desc      # описание
            self.img       = img       # изображение
            self.price     = price     # цена в магазине
            self.InShop    = InShop    # доступно к приобретению
            self.have      = have      # есть в сумке
            self.buy       = buy       # куплено, но еще не доставлено
            self.delivery  = delivery  # доставка через .. дней
            self.need_read = need_read # если больше нуля - признак книги. Сколько циклов чтения нужно
            self.read      = 0         # сколько раз уже прочитано
        def __repr__(self):
            return "наименование=\"{self.name}\", описание: {self.desc}, изображение: {self.img}"\
            "цена: {self.price}, в магазине {self.InShop}, имеется {self.have}, куплено {self.buy}"\
            "доставка через {self.delivery}, прочитано {self.read}/{self.need_read}".format(self=self)


################################################################################
    class PossStage:  # Описание этапа возможности
        def __init__(self, image="", desc="", ps=""):
            self.image  = image # изображение в экран описания возможностей
            self.desc   = desc  # описание этапа возможности (в окно возможэностей)
            self.ps     = ps    # послесловие (мысли ГГ по поводу развития или сообщение о временном или постоянном окончании возможности)
        def __repr__(self):
            return "изображение=\"{self.image}\", описание: {self.desc}, послесловие: {self.ps}\n".format(self=self)


################################################################################
    class Poss:  # описание возможности
        def __init__(self, name, stages=[], stage_number=-1):
            self.name         = name          # Наименование (в экран описания возможностей)
            self.stages       = stages        # список этапов возможности
            self.stage_number = stage_number  # текущий этап
        def __repr__(self):
            return "Наименование=\"{self.name}\", текущий этап: {self.stage_number}, список этапов:\n {self.stages}".format(self=self)


################################################################################
    class TalkTheme:  # описание темы для разговора
        def __init__(self, char, select, label, req="False"):
            self.char   = char    # персонаж, (или список персонажей) с которым должен вестись диалог
            self.select = select  # Фраза, которая будет отображаться в меню выбора диалога с персонажем
            self.label  = label   # Метка перехода при выборе пункта меню
            self.req    = req     # Условие, выполнение которого делает фразу доступной для отображения
        def __repr__(self):
            return "стартовая фраза=\"{self.select}\", метка: {self.label}, условие: {self.req}".format(self=self)


################################################################################
    class Dayly:
        def __init__(self, lost=0, done=False, enabled=False, stage=0):
            self.lost    = lost     # осталось дней до срабатываения события
            self.enabled = enabled  # дейлик активен, нужно ежедневно убавлять счетчик до 0
            self.done    = done     # счетчик достиг 0, для проверки доступности диалога
        def __repr__(self):
            return "Этап: {self.stage}, осталось дней: {self.lost}, выполнено: {self.done}, активно: {self.enabled}".format(self=self)


################################################################################
    class CutEvent:
        """ События, запускаемые в конкретное время
            Описание полей:
            tm        – время начала события
            lod       – кортеж дней недели для события
            label     – имя блока обработки события
            desc      – описание события
            variable  – строка с логическим выражением, вычисляется при получиении события
            stage     - этап события. Если None - повторяемое
            sleep     - для запуска нужно, чтобы Макс спал"""
        def __init__(self, tm="", lod=(0, 1, 2, 3, 4, 5, 6), enabled=True, label="", desc="", variable="True", stage=0, sleep=False):
            h, m = tm.split(":") if str(tm).find(":") > 0 else str(float(tm)).replace(".", ":").split(":")
            self.tm        = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:]

            self.lod      = lod
            self.enabled  = enabled
            self.label    = label
            self.desc     = desc
            self.variable = variable
            self.stage    = stage
            self.sleep    = sleep

        def __repr__(self):
            return "\"{self.desc}\" стартует в {self.tm} по дням: {self.lod}, только если Макс спит {self.sleep}".format(self=self)
