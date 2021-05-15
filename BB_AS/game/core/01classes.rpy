init python:
    from itertools import izip, cycle
    from collections import namedtuple, OrderedDict
    import hashlib, base64, copy

    # ключ для сортировки списка с расписанием - время начала действия
    def SortByTime(inputStr):
        return inputStr.ts

    # ключ для сортировки списка с расписанием - дата и время начала действия
    def SortByDayTime(inputStr):
        return str(inputStr[0]) + '_' + inputStr[1]


    ############################################################################

    class Garb():
        def __init__(self, suf, info, name="", change=False, rand=False):
            self.suf    = suf    # суфикс для выбора спрайта
            self.info   = info   # имя изображения для инфо-окна
            self.name   = name   # наименование для окна выбора варианта одежды
            self.change = change # доступен выбор этого варианта для ручной установки
            if change:
                self.rand = True  # если вариант доступен для выбора, то и для случайного выбора он тоже доступен
            else:
                self.rand = rand  # этот вариант доступен для случайного выбора

        def enable(self):
            self.change = True
            self.rand   = True

        def rand_enable(self):
            self.rand   = True

        def disable(self):
            self.change = False
            self.rand   = False

        def __repr__(self):
            r1 = 'доступно' if self.change else 'только случайно' if self.rand else 'заблокировано'
            return "{self.name} ({self.suf}/{self.info}), {r1}".format(self=self, r1=r1)

    class Clothes():
        name    = ''        # Наименование типа одежды для окна выбора
        sel     = None      # список доступных вариантов выбора (тип Garb)
        cur     = 0         # номер выбранного варианта из списка
        rand    = False     # выбирать случайно из доступных вариантов раз в days дней
        left    = 0         # осталось дней до случайного выбора
        days    = 1         # количество дней по умолчанию до смены одежды
        req     = 'True'    # условие доступности ручного выбора одежды
        hints   = ''        # подсказка, показываемая при невозможности выбора

        def __init__(self, name="", sel=[], req='True', hints=""):
            self.name   = name
            self.sel    = sel
            self.req    = req
            self.hints  = hints

        # достаточно ли вариантов для ручной установки
        def Opens(self):
            l = [i for i in range(len(self.sel)) if self.sel[i].change]
            return True if len(l)>1 else False

        # достаточно ли активно вариантов случайного выбора
        def RandOpens(self):
            l = [i for i in range(len(self.sel)) if self.sel[i].rand]
            return True if len(l)>1 else False

        # устанавливает случайную одежду, отличную от текущей
        def SetRand(self, forced=False):
            if self.left > 0 and not forced:
                self.left -= 1
            else:
                lr = [i for i in range(len(self.sel)) if self.sel[i].rand and i!=self.cur for j in range(5)]
                if len(lr):
                    renpy.random.shuffle(lr)
                    self.cur = renpy.random.choice(lr)
                    if self.cur > len(self.sel)-1:
                        # print("баг, однако  "+self.name+' - ['+str(lr)+']')
                        self.cur = len(self.sel)-1
                    self.left = self.days

        # возвращает список открытых для ручного выбора
        def GetOpen(self):
            return [i for i in range(len(self.sel)) if self.sel[i].change]

        # вызвращает текущий вариант одежды
        def GetCur(self):
            if self.cur > len(self.sel)-1:
                # print("баг, однако  "+self.name+' - '+str(self.cur))
                self.cur = len(self.sel)-1
            return self.sel[self.cur]

        # проверяет, является ли вариант одежды заблокированным для изменения вручную
        @property
        def blocked(self):
            rez = False
            try:
                rez = eval(self.req)
            except:
                return True

            return not rez

        # проверяет, открыт ли доступ к конкретному варианту
        @property
        def enabled(self, num):
            return self.sel[num].rand   # если доступен вручную, случайный тоже доступен

        # активирует одежду для смены вручную (конкретную или список)
        def enable(self, nums, cur=None):
            added = False
            if type(nums) == int:
                if not self.sel[nums].rand:
                    added = True
                self.sel[nums].enable()
            elif type(nums) in [tuple, list]:
                for k in nums:
                    if not self.sel[k].rand:
                        added = True
                    self.sel[k].enable()
            if cur is not None:
                self.cur = cur
            elif added:
                self.rand = True
                self.left = self.days
                if type(nums) == int:
                    self.cur = nums
                elif type(nums) in [tuple, list]:
                    self.cur = max(nums)
                    self.rand   = True

        # активирует одежду для рандомной смены (конкретную или список)
        def rand_enable(self, nums=[]):
            added = False
            if type(nums) == int:
                if not self.sel[nums].rand:
                    self.sel[nums].rand_enable()
                    added = True
            elif type(nums) in [tuple, list]:
                for k in nums:
                    if not self.sel[k].rand:
                        self.sel[k].rand_enable()
                        added = True

            if added:
                self.rand = True
                self.left = self.days
                if type(nums) == int:
                    self.cur = nums
                elif type(nums) in [tuple, list]:
                    self.cur    = max(nums)

        # закрывает доступ
        def disable(self, nums):
            if type(nums) == int:
                self.sel[nums].disable()
                if self.cur == nums:
                    self.SetRand()
            elif type(nums) in [tuple, list]:
                for k in nums:
                    self.sel[k].disable()
                if self.cur in nums:
                    self.SetRand()

        # устанавливает условие доступности (и подсказку) для типа одежды
        def set_condition(self, req, hints):
            self.req    = req
            self.hints  = hints

        def __repr__(self):
            return self.name+':    '+str({attr : getattr(self, attr) for attr in self.__dict__ if attr not in ['id', 'name']})[1:-1]

    class Clothing():

        casual      = None  # повседневная одежда
        sleep       = None  # одежда для сна
        swimsuit    = None  # купальник
        sports      = None  # спортивная форма
        work        = None  # школьная форма или рабочая одежда
        club        = None  # одежда для клуба
        out         = None  # одежда для прогулок
        cook_morn   = None  # для утренней готовки
        cook_eve    = None  # для вечерней готовки
        rest_morn   = None  # для утреннего отдыха
        rest_day    = None  # для отдыха днем
        rest_eve    = None  # для вечернего отдыха
        learn       = None  # для выполнения домашних заданий
        lingerie    = None  # бельё для проведения блога

        def __init__(self):
            self.casual     = None  # повседневная одежда
            self.sleep      = None  # одежда для сна
            self.swimsuit   = None  # купальник
            self.sports     = None  # спортивная форма
            self.work       = None  # школьная форма или рабочая одежда
            self.club       = None  # одежда для клуба
            self.out        = None  # одежда для прогулок
            self.cook_morn  = None  # для утренней готовки
            self.cook_eve   = None  # для вечерней готовки
            self.rest_morn  = None  # для утреннего отдыха
            self.rest_day   = None  # для отдыха днем
            self.rest_eve   = None  # для вечернего отдыха
            self.learn      = None  # для выполнения домашних заданий
            self.lingerie   = None  # бельё для проведения блога

        def GetList(self):
            l = []
            for attr in self.__dict__:
                if getattr(self, attr) is not None:
                    l.append(attr)
            return l

        def Opens(self):
            l = []
            for attr in self.__dict__:
                val_attr = getattr(self, attr)
                if val_attr is not None and val_attr.Opens():
                    l.append(attr)
            return True if len(l) else False

        def __repr__(self):
            return '\n'.join([attr for attr in self.__dict__ if getattr(self, attr) is not None])

    ############################################################################

    class Chrs():
        id          = ''
        dress       = "a"         # суфикс файлов одежды ("a", "b", "c"...)
        def __init__(self, id, name, name_1, name_2, name_3, name_4, name_5, desc=''):
            self.id         = id        # идентификатор
            self.name       = name      # имя
            self.name_1     = name_1    # имя в родительном падеже (от кого?)
            self.name_2     = name_2    # имя в дательном падеже (кому?)
            self.name_3     = name_3    # имя в винительном падеже (про кого?)
            self.name_4     = name_4    # имя в творительном падеже (с кем?)
            self.name_5     = name_5    # имя в предложном падеже (о ком?)
            self.desc       = desc      # описание

    class Schedule():           # действие в расписании персонажа
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
            rez = "{self.name}, по дн:{self.lod}, с {self.ts}, до {self.te}, \"{self.desc}\", в {self.loc}[{self.room}], каждые {self.krat} "\
                    "нед., со сдв.{self.shift}, нач. с {self.weekstart} нед.".format(self=self)
            if self.variable != "True":
                rez += "\n    условие: {self.variable}".format(self=self)
            return rez

    class SexStat():            # статистика сексуальных отношений
        id          = ''    # идентификатор принадлежности
        # демонстрации
        sh_breast   = 0     # показы груди
        sh_ass      = 0     # показы попки
        sh_pussy    = 0     # показы киски

        kiss        = 0     # поцелуи

        handjob     = 0     # hand_job "ручная работа"
        footjob     = 0     # foot_job "работа" ножками
        blowjob     = 0     # blow_job минет
        boobjob     = 0     # boob_job дрочка грудью
        assjob      = 0     # дрочка попкой
        mast        = 0     # мастурбация

        sex         = 0     # традиционный секс

        def __init__(self, id):
            self.id         = id
            self.sh_breast  = 0
            self.sh_ass     = 0
            self.sh_pussy   = 0

            self.kiss       = 0

            self.handjob    = 0
            self.footjob    = 0
            self.blowjob    = 0
            self.boobjob    = 0
            self.assjob     = 0
            self.mast       = 0

            self.sex        = 0

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__ if attr!='id'})[1:-1]

    class Request():            # требование к девушке
        req     = None      # текущее требование
        result  = None      # результат
        noted   = False     # нарушение требования замечено Максом

        def reset(self):
            self.req    = None
            self.result = None
            self.noted  = False

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    class Weekly_resets():      # сбрасываемые раз в неделю
        mass1       = 0
        dishes      = 0
        help        = 0
        punished    = 0
        protected   = 0

        def __init__(self):
            self.mass1      = 0
            self.dishes     = 0
            self.help       = 0
            self.punished   = 0
            self.protected  = 0

        def reset(self):
            for attr in self.__dict__:
                setattr(self, attr, 0)

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    class Daily_resettable():   # сбрасываемые при наступлении нового дня
        # подсматривания
        shower  = 0     # душ
        bath    = 0     # ванная
        sex     = 0     # секс в комнате
        tv_sex  = 0     # секс перед тв
        sex_ed  = 0     # урок секс.образования
        blog    = 0     # блог
        blog_we = 0     # блог с Эриком

        # диалоги
        dishes      = 0     # диалог о помывке посуды
        tvwatch     = 0     # диалог о совместном просмотре ТВ
        massage     = 0     # диалог о массаже
        homework    = 0     # диалог о помощи с домашкой
        smoke       = 0     # диалог во время курения
        ask_money   = 0     # просил денег

        # состояния
        oiled    = 0    # намазана солнцезащитным кремом
        drink    = 0    # пьяна

        def __init__(self):
            self.shower     = 0
            self.bath       = 0
            self.sex        = 0
            self.tv_sex     = 0
            self.sex_ed     = 0
            self.blog       = 0
            self.blog_we    = 0

            self.dishes     = 0
            self.tvwatch    = 0
            self.massage    = 0
            self.homework   = 0
            self.smoke      = 0
            self.ask_money  = 0

            self.oiled      = 0
            self.drink      = 0

        def reset(self):
            for attr in self.__dict__:
                setattr(self, attr, 0)

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    class Hourly_resets():      # сбрасываемые ежечасно
        # подсматривания
        sleep   = 0
        dressed = 0
        # диалоги
        sun_cream = 0

        def __init__(self):
            self.sleep   = 0
            self.dressed = 0
            self.sun_cream = 0

        def reset(self):
            for attr in self.__dict__:
                setattr(self, attr, 0)

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    class Flags_Counter():      # флаги и счетчики персонажей
        id          = ''        # идентификатор принадлежности
        # флаги
        nakedpunish = False     # были "голые" наказания
        handmass    = False     # доступен массаж рук
        touched     = False     # прикасалась к члену Макса
        promise     = False     # обещание девушки Максу (или наоборот)
        hip_mass    = 0         # доступ к массажу бёдер
        hugs_type   = 0         # тип обнимашек за третье дарение "извинительных" сладостей
        private     = False     # доступно приватное наказание (оговорили дни и условия)
        crush       = 0         # стадии разговора об увлечении (для Эрика - стадии начального отношения)
        incident    = 0         # стадии разговора об инцеденте

        # счетчики
        defend      = 0         # счетчик спасений от наказания голышом
        privpunish  = 0         # счетчик успешных приватных наказаний
        hugs        = 0         # счетчик обнимашек(поцелуев) за периодические сладости
        pun         = 0         # всего наказаний
        m_foot      = 0         # счетчик массажей ног
        m_shoulder  = 0         # счетчик массажей плеч
        m_breast    = 0         # счетчик массажей груди
        m_back      = 0         # счетчик массажей спины
        m_pussy     = 0         # счетчик масажей киски
        kiss_lesson = 0         # счетчик уроков поцелуев
        porno       = 0         # счетчик совместно просмотренных порнофильмов
        erofilms    = 0         # счетчик совместно просмотренных эротических фильмов
        help        = 0         # счетчик помощи девушке (с домашкой, йогой или чем-то подобным)
        truehelp    = 0         # помощь Макса с полной самоотдачей
        ladder      = 0         # счетчик подсматриваний со стремянки
        topless     = 0         # снимала верх при Максе

        def __init__(self, id):
            self.id         = id
            # флаги
            self.nakedpunish    = False
            self.handmass       = False
            self.promise        = False
            self.hip_mass       = 0
            self.hugs_type      = 0
            self.private        = False

            #счетчики
            self.defend         = 0
            self.privpunish     = 0
            self.hugs           = 0
            self.pun            = 0
            self.m_foot         = 0
            self.m_shoulder     = 0
            self.m_breast       = 0
            self.m_back         = 0
            self.m_pussy        = 0
            self.kiss_lesson    = 0
            self.porno          = 0
            self.erofilms       = 0
            self.help           = 0
            self.truehelp       = 0

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__ if attr!='id'})[1:-1]

    class Dcv_list():           # дейлики персонажей
        punpause    = None      # во время паузы невозможны наказания без подставы
        prudence    = None      # дни благоразумия (не нарушает условий Макса)
        sweets      = None      # дарение сладости (или обещание "сладости")
        battle      = None      # битва за девушку (откаты и стадии)
        intrusion   = None      # вмешательство (махинации) Эрика
        photo       = None      # фотосессии
        set_up      = None      # можем подставить
        feature     = None      # секреты, особенности, стадии бесед
        special     = None      # курение Алисы, фильм-наказание с Лизой, ночные посещения с Оливией
        seduce      = None      # соблазнение
        other       = None      # прочее, просмотры ТВ с Оливией
        gifts       = None      # особые подарки
        private     = None      # доступно приватное наказание

        def __init__(self):
            self.punpause   = Daily()
            self.prudence   = Daily()
            self.sweets     = Daily()
            self.battle     = Daily()
            self.intrusion  = Daily()
            self.photo      = Daily()
            self.set_up     = Daily()
            self.feature    = Daily()
            self.special    = Daily()
            self.seduce     = Daily()
            self.other      = Daily()
            self.gifts      = Daily()
            self.private    = Daily()

        def countdown(self, exceptions=[], only=[]):
            for attr in self.__dict__:
                if attr in exceptions:
                    continue

                if only and attr not in only:
                    continue

                dcv = getattr(self, attr)
                if type(dcv) != Daily:
                    continue

                if dcv.enabled and dcv.lost>0:
                    dcv.set_lost(dcv.lost - 1)

        def reinit(self):
            for attr in self.__dict__:
                if getattr(self, attr) is None:
                    setattr(self, attr, Daily())

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    ############################################################################

    class Profile(Chrs):        # Описание и характеристики персонажа (не ГГ)

        # сбрасываем при наступлении нового дня
        spanked     = False     # отшлёпана сегодня

        # обычные параметры
        sleeptoples = False     # спит топлес
        sleepnaked  = False     # спит голой

        nopants     = False     # не носит трусики

        dress_inf   = '01a'     # суфикс изображения в окно описания

        ri          = 0         # (romantic interest) заинтересованность
        free        = 0         # текущая раскрепощенность (для Эрика – None)
        releric     = None      # уровень отношений с Эриком (для Эрика – None)
        infmax      = None      # влияние Макса (для Эрика – None)
        inferic     = None      # влияние Эрика (для Эрика – None)
        attention   = 0         # день, когда последний раз было уделено внимание персонажу

        plan_name   = None      # наименование текущего действия для ускорения сранений. Обновляется при каждом запросе расписания с текущей датой/временем

        gifts       = None      # полученные подарки
        sorry       = None      # "извинительные" подарки
        flags       = None      # общие флаги и счетчики
        req         = None      # требование
        stat        = None      # статистика сексульных отношений
        clothes     = None      # сменяемая одежда

        # сбрасываемые
        weekly  = None          # раз в неделю
        daily   = None          # при наступлении нового дня
        hourly  = None          # ежечасно
        dcv     = None          # дейлики

        def __init__(self, id, name, name_1, name_2, name_3, name_4, name_5, desc='', pref='', mood=0, relmax=0):
            super(Profile, self).__init__(id, name, name_1, name_2, name_3, name_4, name_5, desc)
            self.pref       = pref              # префикс (папка) изображений

            self.mood       = mood              # текущее настроение
            self.relmax     = relmax            # уровень отношений с ГГ
            self.plan       = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]    # расписание персонажа

            self.gifts      = []                # полученные подарки
            self.sorry      = SorryGift()       # "извинительные" подарки
            self.flags      = Flags_Counter(id) # флаги и счетчики
            self.stat       = SexStat(id)       # статистика сексульных отношений
            self.req        = Request()         # требование к девушке

            self.clothes    = Clothing()        # сменяемая одежда

            # сбрасываемые
            self.weekly = Weekly_resets()
            self.daily  = Daily_resettable()
            self.hourly = Hourly_resets()
            self.dcv    = Dcv_list()

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

        # функция для разработчика, возвращает список расписаний на день и час со всеми вариантами условий
        def get_all_plans_list(self, d1, tm1):
            h, m = tm1.split(':')  # нормализуем время на всякий случай
            tm1 = ('0' + str(int(h)))[-2:] + ':' + ('0' + str(int((m + '0')[:2])))[-2:]
            wd  = GetWeekday(d1)    # день недели
            wn  = (d1+2) // 7       # номер недели
            rez = []
            for sh in self.plan:
                if all([sh.ts <= tm1 <= sh.te, wd in sh.lod,    # нужное время и день недели
                    (wn >= sh.weekstart), (wn - sh.weekstart) % sh.krat == sh.shift]):   # нужная неделя
                    # варианты условий игнорируем для этой фукнции
                        rez.append(sh)
            return rez

        # функция для разработчика, проверяет расписание на перехлесты
        def verify_schedule(self):
            max_krat = 1
            max_week = 0
            for sh in self.plan:  # определяем неделю старта теста и максимальную длительность в неделях (кратность)
                max_krat = max(max_krat, sh.krat)
                max_week = max(max_week, sh.weekstart)

            errors = set()
            skipped = set()

            kolve = (max_week + max_krat) * 7 * 2

            for d1 in range(max_week*7, kolve):  # удваиваем диаппазон на всякий случай
                start_skip = end_skip = ''
                for hour in range(24):
                    for minute in range(0, 60, 10):
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
                print("Skiped:\n", skip_list)
            else:
                print("Skiped not detected")
            if len(errors):
                print("Error:\n",errors)
            else:
                print("Errors not detected")

        # Вспомогательная. При загрузке записи производит необходимую
        # корректировку агрументов экземпляра класса
        def reinit(self):
            # для 0.06.5
            if hasattr(self, 'naked'):
                delattr(self, 'naked')
            if hasattr(self, 'sex_stat'):
                delattr(self, 'sex_stat')

            if self.stat is None:
                self.stat       = SexStat(self.id)     # статистика отношений с ГГ

            if self.gifts is None:
                self.gifts      = []                # полученные подарки

            if self.req is None:
                self.req      = Request()

            if self.daily is None:
                self.daily      = Daily_resettable()
            if self.hourly is None:
                self.hourly     = Hourly_resets()

            if self.clothes is None:
                self.clothes    = Clothing()        # сменяемая одежда

            if self.sorry is None:
                self.sorry      = SorryGift()       # "извинительные" подарки

            if self.flags is None:
                self.flags      = Flags_Counter(self.id)   # флаги и счетчики

            if self.dcv is None:
                self.dcv        = Dcv_list()

            if self.weekly is None:
                self.weekly = Weekly_resets()

    ############################################################################

    class Loan():
        level    = 0      # уровень доступного кредита
        amount   = 0      # выдан займ на сумму
        debt     = 0      # непогашенный остаток
        fines    = False  # начислен штраф
        left     = 0      # дней до начисления штрафа

        def __init__(self):
            pass

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

    class MaxFlags():        # флаги и счетчики мгг
        # сбрасываемые ежечасно
        tired       = False     # мало энергии (устал)

        # флаги
        nakedpunish = False     # были "голые" наказания

        # счетчики
        pun         = 0         # счетчик наказаний Макса

        def __init__(self):
            self.tired          = False
            self.nakedpunish    = False
            self.pun            = 0

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

        def hourly_reset(self):
            self.tired  = False

    class MaxProfile(Chrs):

        energy      = 100.0         # запас сил, энергия
        training    = 20.0          # тренированность
        cleanness   = 70.0          # чистота
        social      = 8.0           # навыки убеждения
        massage     = 0.0           # навыки массажа
        ero_massage = 0.0           # навыки эро.массажа
        stealth     = 9.0           # навык скрытности
        kissing     = 0.0           # навык поцелуев
        sex         = 0.0           # сексуальный опыт

        cuni        = 0.0           # опыт куни
        anal        = 0.0           # опыт анального секса

        __tange     = 150

        __account   = 0             # состояние счета на сайте
        invited     = 0             # привлечено зрителей за счет рекламы

        clothes     = None    # сменяемая одежда
        flags       = None    # флаги и счетчики мгг
        credit      = None

        def __init__(self, id, name, name_1, name_2, name_3, name_4, name_5, desc='', img=''):

            super(MaxProfile, self).__init__(id, name, name_1, name_2, name_3, name_4, name_5, desc)
            self.img        = img           # изображение в окно описания
            self.clothes    = Clothing()    # сменяемая одежда
            self.flags      = MaxFlags()    # флаги и счетчики мгг
            self.credit     = Loan()

        @property
        def money(self):
            return self.__tange

        # @money.setter
        # def money(self, val):
        #     self.__tange = val

        @property
        def account(self):
            return self.__account

        def ask(self, lvl, fee=0):   # просим денег
            self.__tange += fee+{
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

        def reinit(self):
            if self.clothes is None:
                self.clothes    = Clothing()    # сменяемая одежда
            if self.flags is None:
                self.flags      = MaxFlags()    # флаги и счетчики мгг
            if self.credit is None:
                self.credit     = Loan()

        def __repr__(self):
            return "имя: {self.name}, описание: {self.desc}, изображение=\"{self.img}\", "\
            "\nзапас сил: {self.energy}, тренированность: {self.training}, чистота: {self.cleanness}, "\
            "\nубежд: {self.social}, массаж: {self.massage}, эро.массаж: {self.ero_massage}"\
            "\nскрыт: {self.stealth}, опыт поцелуев: {self.kissing}, куни: {self.cuni}"\
            "секс: {self.sex}, анал: {self.anal}".format(self=self)

    ############################################################################

    class Other_Flags_and_counters():

        # флаги
        eric_jerk       = False     # Эрик сегодня дрочит на Алису
        eric_noticed    = False     # Эрик сегодня замечен за дрочкой
        eric_photo1     = 0         # получено фото Эрика на балконе
        eric_photo2     = 0         # получено фото Эрика в комнате Алисы
        eric_fee        = 0         # прибавка или штраф к карманным деньгам от Эрика
        voy_stage       = 0         # стадии подглядывания за АиЭ

        ladder          = 0         # стадии получения/установки стремянки
        credit          = 0         # стадии доступа к кредиту  (доработать на опережение Эрика с бельём)
        bonus_from_eric = []        # бонусы за дружбу с Эриком
        lisa_fd         = 0         # разговор с Лизой после школы в первый день
        how_to_kiss     = []        # список опрошенных об уроках поцелуев
        lisa_sexed      = -1        # номер урока секс.образования от Эрика
        l_ab_sexed      = False     # доступен разговор с Лизой об очередном уроке Эрика
        warning         = False     # сообщение об опасности просмотра камер в присутствии Лизы

        back_shop       = 0         # счетчик сюжетных возвращений с шопинга

        stopkiss        = 0         # стадии прекращения обучения Лизы поцелуям
        add_training    = False     # состоялся разговор за ужином о дополнительных занятиях Лизы
        about_earn      = False     # состоялся разговор за ужином о заработках
        hint_cources    = False     # была подсказка, что для убеждения Киры нужны курсы
        film_punish     = False     # в качестве наказания за подглядывание теперь смотрим с Лизой фильм
        noclub          = False     # в эту пятницу Алиса не идёт в клуб (ведёт блог в нижнем белье)
        cur_series      = 0         # 1/2 часть фильма, просматриваемого с Лизой
        cur_movies      = []        # список (выбранный фильм, фильм Кошмаров, фильм Пятницы)

        # счетчики
        breakfast       = 0         # завтраков
        dinner          = 0         # ужинов
        courier1        = 0         # доставок Сэма
        courier2        = 0         # доставок Кристины

        def __init__(self):
            self.eric_jerk          = False
            self.eric_noticed       = False
            self.eric_photo1        = 0
            self.eric_photo2        = 0
            self.bonus_from_eric    = []
            self.how_to_kiss        = []
            self.lisa_sexed         = -1
            self.l_ab_sexed         = False
            self.ladder             = 0
            self.credit             = 0
            self.warning            = False

            self.breakfast          = 0
            self.dinner             = 0
            self.courier1           = 0
            self.courier2           = 0

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    ############################################################################
    ############################################################################

    class Room():  # описание комнат в каждой локации (дом, школа, кафе и т.п.)
        def __init__(self, id, name, cam_name, icon="", max_cam=1, cur_bg="", cur_char=[]):
            self.id            = id        # идентификатор (идентификатор конкретной комнаты в локации {my_room, alice_room...})
            self.name          = name      # Наименование для окна навигации
            self.cam_name      = cam_name  # Наименование для камер
            self.icon          = icon      # миниатюра для окна навигации
            self.max_cam       = max_cam   # максимально возможное количество установленных камер для данной комнаты
            self.cur_bg        = cur_bg    # текущий фон для комнаты
            self.cur_char      = cur_char  # список персонажей, находящихся в комнате в данный момент

            self.cams          = []        # список камер, установленных в комнате

        def __repr__(self):
            return "id: {self.id}, наименование: {self.name}, миниатюра=\"{self.icon}\", фон: {self.cur_bg}, "\
            "персонажи в комнате: {self.cur_char}".format(self=self)

    ############################################################################

    class ActionsButton():
        """ класс-формат для объявления списка доступных действий """
        active  = False   # доступна ли кнопка в данной локации или с данным персонажем

        def __init__(self, sing="", icon="", label="", enabled=False):
            self.sing    = sing    # подпись кнопки
            self.icon    = icon    # иконка кнопки
            self.label   = label   # имя блока обработки события
            self.enabled = enabled # доступна ли кнопка в целом (задается событиями)
                                   # для отображения кнопки должны быть истинны оба условия

        def __repr__(self):
            return "Кнопка: {self.sing} с иконкой \"{self.icon}\" запускает метку {self.label}. {self.enabled}".format(self=self)

    ############################################################################

    class Item():
        """ класс-формат описания предметов как в инвентаре, так и доступных для заказа в ИМ """
        have      = False   # есть в сумке
        bought    = False   # куплено, но ещё не доставлено
        delivery  = 0       # доставка через .. дней
        read      = 0       # сколько раз уже прочитано

        def __init__(self, name, desc="", img="", category="", price=0, InShop=False, need_read=0, cells=1, have=False):
            self.name       = name      # наименование (в магазине и в сумке)
            self.desc       = desc      # описание
            self.img        = img       # изображение
            self.category   = category  # номер категории магазина
            self.price      = price     # цена в магазине
            self.InShop     = InShop    # доступно к приобретению
            self.need_read  = need_read # если больше нуля - признак книги. Сколько циклов чтения нужно
            self.cells      = cells     # занимаемые по вертикали ячейки (1 или 2)
            self.have       = have      # есть в сумке

        def buy(self):          # выполняет покупку предмета из интернет-магазина
            mgg.pay(self.price)
            self.bought     = True
            self.delivery   = 1 if GetWeekday(day) != 6 else 2
            purchased_items.append(self)

        def block(self):        # блокирует доступ к приобретению
            self.InShop = False

        def unblock(self):      # открывает доступ к приобретению предмета
            self.InShop = True

        def give(self):         # вручение предмета
            self.have   = False
            self.InShop = False

        def use(self):          # использование (или вручение), можно купить повторно
            self.have   = False

        def __repr__(self):
            return "наименование=\"{self.name}\", описание: {self.desc}, изображение: {self.img}"\
            "цена: {self.price}, в магазине {self.InShop}, имеется {self.have}, куплено {self.bought}"\
            "доставка через {self.delivery}, прочитано {self.read}/{self.need_read}".format(self=self)

    ############################################################################

    class PossHint():   # подсказки к этапу возможности
        def __init__(self, hint, req=True):
            self.hint   = hint      # подсказака
            self.req    = req       # условие отображения подсказки

        def met(self):
            rez = False
            try:
                rez = eval(self.req)
            except KeyError:
                pass
            except Exception:
                pass
            return rez

    class PossStage():  # Описание этапа возможности
        used    = False
        hints   = None
        def __init__(self, img="", desc="", ps="", hints=[]):
            self.img    = img   # изображение в экран описания возможностей
            self.desc   = desc  # описание этапа возможности (в окно возможэностей)
            self.ps     = ps    # послесловие (мысли ГГ по поводу развития)
            self.used   = False # этап был пройден
            self.hints  = hints # список подсказок к этапу возможности

        def __repr__(self):
            return "изображение=\"{self.img}\", описание: {self.desc}, послесловие: {self.ps}\n".format(self=self)

    class Poss():  # описание возможности
        stn     = -1
        def __init__(self, stages=[]):
            # self.stn    = -1        # текущий этап
            self.stages = stages    # список НОМЕРОВ этапов возможности

        def __repr__(self):
            return "{cur} ({self.stages})".format(self=self, cur = max([i if st else -1 for i, st in enumerate(self.stages)]))

        def OpenStage(self, stage): # для корректировки старых сохранений
            a = [1 for st in self.stages if st.used]
            self.stages[stage].used = True
            if self.stn < stage:
                self.stn = stage
            if sum(a) == 0:
                notify_list.append(_("{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"))

        def open(self, stage): # открывает этап "возможности", если номер этапа больше текущего, устанавливает текущим новый этап
            if sum(self.stages) < 1:
                notify_list.append(_("{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"))
            self.stages[stage] = 1

        def used(self, stage):      # проверяет, задействован ли этап возможности
            return self.stages[stage]   #.used

        def st(self):   # возвращает номер текущего этапа (максимальный открытый)
            stn = [i for i, st in enumerate(self.stages) if st]
            return max(stn) if stn else -1


    ############################################################################

    class TalkTheme():  # описание темы для разговора
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

    class Daily():
        stage = 0   # стадия событтия

        def __init__(self, lost=0, done=False, enabled=False):
            self.lost       = lost                         # осталось дней до срабатываения события
            self.enabled    = enabled                      # активен, нужно ежедневно убавлять счетчик до 0
            self.done       = True if lost==0 else done    # счетчик достиг 0, для проверки доступности диалога

        def set_lost(self, lost):
            if lost > 0:
                self.enabled = True
            self.lost = lost
            self.done = lost == 0

        def disable(self):
            self.enabled    = False
            self.lost       = 0
            self.done       = True

        def __repr__(self):
            return "Этап: {self.stage}, осталось дней: {self.lost}, выполнено: {self.done}, активно: {self.enabled}".format(self=self)

    class Daily_list():
        clearpool   = Daily(enabled=True)   # очистка бассейна
        ordercosm   = Daily(enabled=True)   # заказ косметики
        buyfood     = Daily(enabled=True)   # заказ продуктов
        mw          = Daily(enabled=True)   # утренний стояк
        new_pun     = Daily()               # следующий тип наказания

        def __init__(self):
            self.clearpool  = Daily(enabled=True)   # очистка бассейна
            self.ordercosm  = Daily(enabled=True)   # заказ косметики
            self.buyfood    = Daily(enabled=True)   # заказ продуктов
            self.mw         = Daily(enabled=True)   # утренний стояк
            self.new_pun    = Daily()               # следующий тип наказания

        def countdown(self, exceptions=[], only=[]):
            for attr in self.__dict__:
                if attr in exceptions:
                    continue

                if only and attr not in only:
                    continue

                dcv = getattr(self, attr)
                if type(dcv) != Daily:
                    continue

                if dcv.enabled and dcv.lost>0:
                    dcv.set_lost(dcv.lost - 1)

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    class Weekly():
        stage = 0  # стадия события

        def __init__(self, lost=0, done=False, enabled=False):
            self.lost       = lost                         # осталось недель до срабатываения события
            self.enabled    = enabled                      # активен, нужно еженедельно убавлять счетчик до 0
            self.done       = True if lost==0 else done    # счетчик достиг 0, для проверки доступности диалога

        def set_lost(self, lost):
            if lost > 0:
                self.enabled = True
            self.lost = lost
            self.done = lost == 0

        def disable(self):
            self.enabled    = False
            self.lost       = 0
            self.done       = True

        def __repr__(self):
            return "Этап: {self.stage}, осталось недель: {self.lost}, выполнено: {self.done}, активно: {self.enabled}".format(self=self)

    class Weekly_list():

        catch_Kira = Weekly(4)

        def __init__(self):
            self.catch_Kira = Weekly(4)

        def countdown(self, exceptions=[], only=[]):
            for attr in self.__dict__:
                if attr in exceptions:
                    continue

                if only and attr not in only:
                    continue

                dcv = getattr(self, attr)
                if type(dcv) != Weekly:
                    continue

                if dcv.enabled and dcv.lost>0:
                    dcv.set_lost(dcv.lost - 1)

        def __repr__(self):
            return str({attr : getattr(self, attr) for attr in self.__dict__})[1:-1]

    ############################################################################

    class CutEvent():
        """ События, запускаемые в конкретное время"""
        def __init__(self, tm="", lod=(0, 1, 2, 3, 4, 5, 6), label="", desc="", variable="True", enabled=True, stage=0, sleep=None, extend=False, cut=False):
            h, m = tm.split(":") if str(tm).find(":") > 0 else str(float(tm)).replace(".", ":").split(":")
            self.tm        = ("0" + str(int(h)))[-2:] + ":" + ("0" + str(int((m + "0")[:2])))[-2:] # время начала события

            self.lod      = lod      # кортеж дней недели для события
            self.label    = label    # имя блока обработки события
            self.desc     = desc     # описание события
            self.variable = variable # строка с логическим выражением, вычисляется при получиении события
            # self.enabled  = enabled
            # self.stage    = stage    # этап события. Если None - повторяемое
            self.sleep    = sleep    # для запуска нужно, чтобы Макс спал
            self.extend   = extend   # при выполнении условия, если Макс встает раньше наступления события, то продлевать сон
            self.cut      = cut      # прерывать сон при наступлении события

        def __repr__(self):
            return "\"{self.desc}\" стартует в {self.tm} по дням: {self.lod}, только если Макс спит {self.sleep}".format(self=self)

    class Events_by_time():

        breakfast       = CutEvent('09:00', label='breakfast', desc='завтрак', cut=True)
        dinner          = CutEvent('19:00', label='dinner', desc='ужин', cut=True)
        shoping         = CutEvent('11:00', (6, ), 'shoping', 'семейный шопинг', cut=True)
        back_shoping    = CutEvent('14:00', (6, ), 'back_shoping', 'возвращение с семейного шопинга', "flags.back_shop < 2", cut=True)
        delivery1       = CutEvent('13:30', (1, 2, 3, 4, 5, 6), 'delivery1', 'доставка товаров Сэмом', 'len(delivery_list[0])>0', cut=True)
        delivery2       = CutEvent('15:30', (1, 2, 3, 4, 5, 6), 'delivery2', 'доставка товаров Кристиной', 'len(delivery_list[1])>0', cut=True)
        night_of_fun    = CutEvent('02:50', label='night_of_fun', sleep=True, variable='len(NightOfFun)>0', desc='ночные забавы')
        Wearied         = CutEvent('03:50', label='Wearied', sleep=False, desc='поспать бы надо')

        AfterSchool     = CutEvent('16:00', label='AfterSchoolFD', variable='day == 1', desc='Лиза первый раз приходит из школы', cut=True)
        need_money      = CutEvent('12:00', label='need_money', desc='срочно нужны деньги', variable='day==9', cut=True)
        Kira_arrival    = CutEvent('08:40', label='Kira_arrival', desc='приезд Киры', variable="all([GetWeekday(day)==6, day>=18, flags.breakfast==12, flags.dinner==17])", cut=True)

        MorningWood     = CutEvent('06:30', label='MorningWood', variable='day == 2', sleep=True, desc='утренний стояк', extend=True)
        MorningWood1    = CutEvent('06:30', label='MorningWoodCont', desc='утренний стояк продолжение', variable="all([day>=7, dcv.mw.done, dcv.mw.stage%2==0, 0<poss['seduction'].st()<4])", sleep=True, cut=True)
        MorningWood2    = CutEvent('06:30', label='MorningWoodCont2', desc='периодический утренний стояк', variable="all([poss['seduction'].st()>10, dcv.mw.done, lisa.GetMood()[0]>2])", sleep=True, cut=True)

        MeetingEric     = CutEvent('18:50', (6, ), 'MeetingEric', 'знакомство с Эриком', 'day == 4', cut=True)
        Eric_af_dinner  = CutEvent('20:00', (6, ), 'Eric_talk_afterdinner', 'разговор с Эриком после субботнего ужина', 'day<12 or flags.dinner==11')
        Eric_Lisa0      = CutEvent('20:00', (6, ), 'Eric_talk_about_Lisa_0', "разговор с Эриком о Лизе", "all([GetWeekday(day)==6, poss['seduction'].st() in [14, 15], not lisa.dcv.battle.stage, lisa.dcv.battle.lost<7, ('sexbody1' not in alice.gifts or alice.dcv.battle.stage>3)])")
        Eric_Lisa1      = CutEvent('20:00', (6, ), 'Eric_talk_about_Lisa_1', "разговор с Эриком о Лизе в случае 'отсрочки'", "all([GetWeekday(day)==6, lisa.dcv.battle.stage==2, lisa.dcv.intrusion.done])")
        Eric_Alice0     = CutEvent('20:00', (6, ), 'Eric_talk_about_Alice_0', "разговор с Эриком о Алисе", "all([GetWeekday(day)==6, not alice.dcv.battle.stage, 'sexbody1' in alice.gifts, (not lisa.dcv.battle.stage or lisa.dcv.battle.stage>3)])")
        Eric_Alice1     = CutEvent('20:00', (6, ), 'Eric_talk_about_Alice_1', "разговор с Эриком о Алисе в случае 'отсрочки'", "all([GetWeekday(day)==6, alice.dcv.battle.stage==2, alice.dcv.battle.enabled, alice.dcv.battle.done])")
        Eric_laceling   = CutEvent('20:00', (6, ), 'Eric_talk_about_lace_lingerie', "разговор с Эриком, если Макс подарил бельё Алисе", "all([GetWeekday(day)==6, 'sexbody2' in alice.gifts, 4<alice.dcv.intrusion.stage<7])")

        MeetingOlivia   = CutEvent('16:00', (3, ), 'olivia_first_meeting', "Оливия приходит на виллу в первый раз", "all([GetWeekday(day)==3, lisa.flags.crush==11, lisa.dcv.feature.done])", cut=True)
        Night_Olivia    = CutEvent('00:00', (6, ), 'olivia_night_visit', "Оливия приходит на ночные посиделки", "all([GetWeekday(day)==6, olivia_nightvisits()])", cut=True)

        Lisa_ab_Alex1   = CutEvent('20:00', (3, ), 'about_alex1', "1-й разговор с Лизой о подкате Алекса", "all([olivia.dcv.feature.stage==5, lisa.flags.crush==12])")
        Lisa_ab_Alex2   = CutEvent('20:00', (5, ), 'about_alex2', "2-й разговор с Лизой о подкате Алекса", "all([lisa.flags.crush==13, lisa.dcv.feature.done])")
        Lisa_ab_Alex3   = CutEvent('20:00', (1, ), 'about_alex3', "3-й разговор с Лизой о подкате Алекса", "all([lisa.flags.crush==14, lisa.dcv.feature.done])")

        Lisa_ab_horror  = CutEvent('20:00', label='Lisa_wear_Tshirt', desc="Лизу наказали и она носит майку", variable="all([lisa.dcv.other.stage, punlisa[0][3]])")

        def get_list_events(self, tm1, tm2, ev_day):
            # составим список всех событий, вписывающихся во временные рамки
            lst = []
            for attr in Events_by_time.__dict__:
                cut = getattr(Events_by_time, attr)
                if type(cut) != CutEvent:
                    continue

                resp = False

                if GetWeekday(ev_day) in cut.lod or cut.lod is None:
                    # день недели входит в диаппазон
                    if tm1 < cut.tm <= tm2 or all([cut.tm==tm2, tm2=='00:00']):
                        # время события входит в диаппазон
                        # print attr, tm1, cut.tm, tm2
                        if cut.sleep is None:
                            resp = True
                        elif (status_sleep == cut.sleep):
                            resp = True
                        elif all([status_sleep, cut.cut, not cut.sleep]):
                            resp = True
                        # print attr, resp, (status_sleep, cut.sleep), (status_sleep, cut.cut, cut.sleep)

                    elif all([tm2 < cut.tm < '08:00', status_sleep, cut.sleep, cut.extend]):
                        # время события позже диаппазона, но МГГ спит и стоит статус продлевать сон
                        resp = True

                if not resp:
                    continue

                # проверим  условия и удалим лишние
                try:
                    resp = eval(cut.variable)
                except KeyError:
                    continue
                except Exception:
                    continue

                if resp:
                    lst.append(cut)

            return lst

        def upcoming(self):
            if tm < prevtime and day>prevday:
                lst = self.get_list_events(prevtime, '23:59', prevday)
                if not lst:
                    lst.extend(self.get_list_events('00:00', tm, day))
            else:
                lst = self.get_list_events(prevtime, tm, day)

            if not lst:
                return None
            elif len(lst) > 1:
                tm_l = []   # список времени событий
                for cut in lst:
                    tm_l.append(cut.tm)
                min_tm = min(tm_l)  # время наиболее раннего
                i = 0
                while i <= len(lst)-1:
                    if lst[i].tm != min_tm:
                        # удалим все события, с другим временем
                        lst.pop(i)
                    else:
                        i += 1
                if len(lst) > 1:
                    return lst[renpy.random.randint(0, len(eventslist)-1)]
                else:
                    return lst[0]
            else:
                return lst[0]


    ############################################################################

    class Helper():
        """ """
        def __init__(self, id, name, desc):
            self.id   = id
            self.name = name
            self.desc = desc

        def __repr__(self):
            return "\"{self.name}\" ({self.id}): {self.desc}".format(self=self)

    ############################################################################

    class HideCam():
        today  = 0      # прибыль за текущий день
        total  = 0      # полная прибыль, полученная с камеры
        public = 0      # текущее количество зрителей
        grow   = 0      # прирост

        def __init__(self, HD = False):
            self.HD       = HD

        def __repr__(self):
            return "Прибыль: {self.total}({self.today}), зрителей: {self.public}, прирост: {self.grow}".format(self=self)

    ############################################################################

    class OnLineCource():
        less   = 0       # пройдено лекций
        bought = False   # курс приобретен

        def __init__(self, header, desc, total, price, grow):
            self.header = header  # Заголовок курса
            self.desc   = desc    # описание курса
            self.total  = total   # всего лекций
            self.price  = price   # цена
            self.grow   = grow    # максимальная эффективность занятия

        def buy(self):  # покупка онлайн-курса
            mgg.pay(self.price)
            self.bought = True

    class OnLineCources():
        current = 0 # текущая часть курса
        def __init__(self, name, skill, img, cources):
            self.name    = name     # Наименование курса (общение, массаж)
            self.skill   = skill    # повышаемый параметр
            self.img     = img      # префикс изображений ("soc"+"-"+индекс курса+"-"+индекс части: soc-0-0, soc-0-1...)
            self.cources = cources  # список частей курса

    ############################################################################

    class Gift():  # предметы-подарки
        def __init__(self, item, select, label, mood = -1, req='True'):
            self.item   = item      # id предмета-подарка
            self.select = select    # фраза в окне диалогов
            self.label  = label     # метка запуска диалога дарения
            self.mood   = mood      # необходимо настроение
            self.req    = req       # условие доступности дарения

    class SorryGift():  # извинительные подарки
        owe     = False     # Макс должен подарить извинительный подарок
        left    = 0         # осталось дней до наказания, если не вручит подарок
        give    = None      # ранее врученные извинительные подарки
        valid   = None      # множество ID товаров, допустимых в качестве извинений
        days    = None      # список дней, когда Макс оправдывался после подглядывания

        def __init__(self):
            self.give   = []    # ранее врученные извинительные подарки
            self.valid  = set() # множество ID товаров, допустимых в качестве извинений
            self.days   = []    # список дней, когда Макс оправдывался после подглядывания

        def start(self, d=1):
            self.owe    = True
            self.left   = d+1 if (day+d+2) % 7 == 0 else d
            self.days.insert(0, day)

        def there_in_stock(self):   # проверяет, есть ли у Макса подарок персонажу в качестве извинения
            for ID in self.valid:
                if items[ID].have:
                    return True
            return False

    class Chance():
        def __init__(self, ch):
            self.ch  = {ch < 0 : 0, ch > 1000 : 1000, 0 <= ch <= 1000: ch}[True]
            self.col = {ch < 333 : red, ch > 666 : lime, 333 <= ch <= 666 : orange}[True]
            self.vis = str(int(ch//10)) + "%"

    class Influence():
        LIM = 200
        freeze = True
        lim_m = LIM
        lim_e = LIM
        def __init__(self, m = None, e = None):
            self.__m = m
            self.__e = e

        @property
        def m(self):
            # возвращает влияние Макса
            return [self.__m, (self.__m * 100) // Influence.LIM if self.__m is not None else 0]

        @property
        def e(self):
            # возвращает влияние Эрика
            return [self.__e, (self.__e * 100) // Influence.LIM if self.__e is not None else 0]

        @property
        def balance(self):
            # возвращает список из трех пунктов:
            # % влияния Макса (от максимума)
            # % влияния Эрика (от Максимума)
            # 'n', 'm' или 'e' в зависимости от того, у кого влияние выше (n - нейтрально, разница в пределах 5%)
            p1 = (self.__m * 100) // Influence.LIM if self.__m is not None else 0
            p2 = (self.__e * 100) // Influence.LIM if self.__e is not None else 0
            if p2-5 < p1 < p2+5 or p1-1 < p2 < p1+5:
                p3 = 'n'
            elif p1 >= p2+5:
                p3 = 'm'
            else:
                p3 = 'e'

            return [p1, p2, p3]

        def add_m(self, d, b = False):
            if self.__m is not None:
                d = d if self.__m + d < self.lim_m else self.lim_m - self.__m
            if d == 0:
                return

            if b or not self.freeze:
                if self.__m is not None:
                    self.__m += d
                else:
                    self.__m = d
                if self.__e is not None:
                    self.__e -= d // 2
                    if self.__e < 0:
                        self.__e = 0

        def add_e(self, d, b = False):
            if self.__e is not None:
                d = d if self.__e + d < self.lim_e else self.lim_e - self.__e
            if d == 0:
                return

            if b or not self.freeze:
                if self.__e is not None:
                    self.__e += d
                else:
                    self.__e = d
                if self.__m is not None:
                    self.__m -= d // 2
                    if self.__m < 0:
                        self.__m = 0

        def sub_m(self, d, b = False):
            if b or not self.freeze:
                if self.__m is not None:
                    self.__m -= d
                    if self.__m < 0:
                        self.__m = 0

        def sub_e(self, d, b = False):
            if b or not self.freeze:
                if self.__m is not None:
                    self.__m -= d
                    if self.__m < 0:
                        self.__m = 0

    class Countdown():

        def __init__(self, timer_range, timer_jump):
            self.time_left   = timer_range - .1
            self.timer_range = timer_range - .1
            self.timer_jump  = timer_jump

    class Chip():
        def __init__(self, nm, pr, cv, lv, dv, mv, dd=None):
            self.nm = nm    # наименование показателя
            self.pr = pr    # строка-кортеж, содержащая day, tm(игровое время), ctm (время назначения проверки), ll, ul, ddop
            self.cv = cv    # текущее значение
            self.lv = lv    # последнее значение
            self.dv = dv    # значение на начало дня
            self.mv = mv    # максимальное значение
            self.dd = dd    # значение дополнительного параметра

    class Cipher():

        # класс для хранения и шифровки числовых параметров
        LETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
            'abcdefghijklmnopqrstuvwxyz' + \
            '0123456789' + \
            ':.;,?!@#$%&()+=-*/_<>[]{}`~^"\'\\' + \
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ' + \
            'абвгдеёжзийклмнопрстуфхйчшщьыъэюя'

        NS = '0123456789abcdefghijklmnopqrstuvwxyz'

        hran  = {}  # словарь-хранилище зашифрованных параметров
        kdir  = {}  # словарь ключей для шифровки параметров (обновляются при верификации)
        cur   = {}  # номера ключей и слова для шифровки текущих значений (меняются при верификации)

        name = ''

        def __init__(self, name, val=None, ll=None, ul=None, ddop=None):
            # генерируем ключи для подстановочного шифра
            if not Cipher.hran:
                # словаря ключей обновляются при инициации только при пустом хранилище
                self.__key_gen__()
                self.__cur_gen__()
                # так же один раз задается порядок символов для задания
                # произвольной шифрованой системы счисления
                l0 = list('123456789abcdefghijklmnopqrstuvwxyz')
                renpy.random.shuffle(l0)
                Cipher.NS = '0'+''.join(l0)

            # шифруем name и используем его md5 в качестве ключа словаря hran
            self.name = self.alg3_0(name)
            digest = hashlib.md5(self.alg2(name).encode("utf-8")).hexdigest()

            if val is None:
                val = 0     # шифруем как 0

            # затем шифруем значение и размещаем его в нужных частях значения словаря
            if not digest[:12] in Cipher.hran:
                Cipher.hran[digest[:12]] = Chip(
                        self.alg0(self.alg2(self.name, 0, Cipher.cur[2]), 0, Cipher.cur[3]),            # nm, наименование параметра
                        self.alg3_0(str((day, tm, tm, ll, ul, ddop))),                                  # pr, кортеж дополнительных параметров, нужные для проверки
                        self.alg0(self.alg4(self.to_str(val))+';'+tm, 0, digest),                       # cv, текущее значение
                        self.alg1(self.alg2(self.to_str(val), 0, Cipher.cur[2])+';'+tm+';'+str(day)),   # lv, последнее значение
                        self.alg4(self.alg0(self.to_str(val)), Cipher.cur[1]),                          # dv, значение на начало дня
                        self.alg4(self.alg0(self.to_str(val), 0, Cipher.cur[3]), Cipher.cur[0]),        # mv, максимальное значение
                        None if ddop is None else self.alg0(self.to_str(eval(ddop))),                   # dd, значение дополнительного параметра
                    )
            else:
                print "Показатель уже есть в хранилище"

        def get(self):
            digest = hashlib.md5(self.alg2(self.alg3_1(self.name)).encode("utf-8")).hexdigest()
            return self.from_str(self.alg4(self.alg0(Cipher.hran[digest[:12]].cv, 1, digest)[:-6], '10'))

        def add(self, pr):
            # добавляет pr к текущему значению
            digest  = hashlib.md5(self.alg2(self.alg3_1(self.name)).encode("utf-8")).hexdigest()
            val     = self.from_str(self.alg4(self.alg0(Cipher.hran[digest[:12]].cv, 1, digest)[:-6], '10'))+pr
            pr      = self.razdop(self.alg3_1(Cipher.hran[digest[:12]].pr))
            if pr.ll and val < pr.ll:
                var = pr.ll
            if pr.ul and val > pr.ul:
                var = pr.ul
            Cipher.hran[digest[:12]].cv = self.alg0(self.alg4(self.to_str(val))+';'+tm, 0, digest)

        def update(self, newval):
            # задаём новое текущее значение
            digest = hashlib.md5(self.alg2(self.alg3_1(self.name)).encode("utf-8")).hexdigest()
            pr      = self.razdop(self.alg3_1(Cipher.hran[digest[:12]].pr))
            if pr.ll and val < pr.ll:
                var = pr.ll
            if pr.ul and val > pr.ul:
                var = pr.ul
            Cipher.hran[digest[:12]].cv = self.alg0(self.alg4(self.to_str(newval))+';'+tm, 0, digest)

        def add_limits(self, ll, ul=None):
            # устанавливает лимиты значения, если не были заданы при создании
            digest  = hashlib.md5(self.alg2(self.alg3_1(self.name)).encode("utf-8")).hexdigest()
            pr      = self.razdop(self.alg3_1(Cipher.hran[digest[:12]].pr))
            edited = False
            val     = self.from_str(self.alg4(self.alg0(Cipher.hran[digest[:12]].cv, 1, digest)[:-6], '10'))
            if ll and val < ll:
                edited = True
                var = ll
            if ul and val > ul:
                edited = True
                var = ul
            if edited:
                Cipher.hran[digest[:12]].cv = self.alg0(self.alg4(self.to_str(newval))+';'+tm, 0, digest)
            Cipher.hran[digest[:12]].pr = self.alg3_0(str((day, tm, pr.ctm, ll, ul, pr.ddop)))

        def add_ddop(self, ddop):
            # устанавливает (или заменяет) дополнительный параметр, если не был задан при создании
            digest = hashlib.md5(self.alg2(self.alg3_1(self.name)).encode("utf-8")).hexdigest()
            pr = self.razdop(self.alg3_1(Cipher.hran[digest[:12]].pr))
            Cipher.hran[digest[:12]].pr = self.alg3_0(str((day, tm, pr.ctm, pr.ll, pr.ul, pr.ddop)))
            Cipher.hran[digest[:12]].dd = None if ddop is None else self.alg0(self.to_str(eval(ddop)))

        def proverka(self, ctm=None, tp=0):
            if ctm is None:
                ctm = tm
            # tp: 0 - раз в 6 часов, 1 - новый игровой день
            td = {}
            # расшифруем все значения во временный словарь
            for dict_key in Cipher.hran:
                nm      = self.alg3_1(self.alg2(self.alg0(Cipher.hran[dict_key].nm, 1, Cipher.cur[3]), 1, Cipher.cur[2]))
                pr      = self.razdop(self.alg3_1(Cipher.hran[dict_key].pr))
                digest  = hashlib.md5(self.alg2(nm).encode("utf-8")).hexdigest()
                cv      = self.from_str(self.alg4(self.alg0(Cipher.hran[dict_key].cv, 1, digest)[:-6], '10'))
                tv      = self.alg1(Cipher.hran[dict_key].lv, 1)
                lv      = self.from_str(self.alg2(tv[:tv[:tv.rfind(';')].rfind(';')], 1, Cipher.cur[2]))
                dv      = self.from_str(self.alg0(self.alg4(Cipher.hran[dict_key].dv, Cipher.cur[1][::-1]), 1))
                mv      = self.from_str(self.alg0(self.alg4(Cipher.hran[dict_key].mv, Cipher.cur[0][::-1]), 1, Cipher.cur[3]))
                dd      = None if Cipher.hran[dict_key].dd is None else self.from_str(self.alg0(Cipher.hran[dict_key].dd, 1))

                td[nm]  = [cv, lv, dv, mv, dd, pr, digest]

            if tp==1:
                # если проверка "новый день", сменим ключи
                self.__key_gen__()
                self.__cur_gen__()

            # проверим и обновим значения
            for nm in td:
                cv      = td[nm][0]
                lv      = td[nm][1]
                dv      = td[nm][2]
                mv      = td[nm][3]
                dd      = td[nm][4]
                pr      = td[nm][5]
                digest  = td[nm][6]

                if not self.acceptable(nm, td, tp):
                    # изменения за пределами разрешённых
                    cv = lv / 2 if cv > mv else lv

                if tp<1:
                    # обновим последнее значение
                    lv  = cv
                else:
                    # обновим последнее и суточное значения
                    dv = lv = cv

                # при необходимости обновим максимальное значение
                if cv > mv:
                    mv  = cv

                # обновим значение дополнительного реквизита
                ll      = pr.ll
                ul      = pr.ul
                ddop    = pr.ddop

                if ddop is not None:
                    dd  = eval(ddop)

                # запишем значения в словрь
                # записываем сразу все параметры, чтобы не проверять на изменения при проверке в течении дня
                # а при ежедневной проверке у нас меняются ключи
                Cipher.hran[digest[:12]] = Chip(
                        self.alg0(self.alg2(self.alg3_0(nm), 0, Cipher.cur[2]), 0, Cipher.cur[3]),      # nm, наименование параметра
                        self.alg3_0(str((day, tm, ctm, ll, ul, ddop))),                                 # pr, кортеж дополнительных параметров, нужные для проверки
                        self.alg0(self.alg4(self.to_str(cv))+';'+tm, 0, digest),                        # cv, текущее значение
                        self.alg1(self.alg2(self.to_str(lv), 0, Cipher.cur[2])+';'+tm+';'+str(day)),    # lv, последнее значение
                        self.alg4(self.alg0(self.to_str(dv)), Cipher.cur[1]),                           # dv, значение на начало дня
                        self.alg4(self.alg0(self.to_str(mv), 0, Cipher.cur[3]), Cipher.cur[0]),         # mv, максимальное значение
                        None if ddop is None else self.alg0(self.to_str(eval(ddop))),                   # dd, значение дополнительного параметра
                    )

        def acceptable(self, nm, td, tp=0):
            if td[nm][0] < td[nm][1]:
                # текущее значение меньше последнего
                return True
            else:
                t_delta = td[nm][0] - td[nm][1]
                d_delta = td[nm][0] - td[nm][2]
            rez = True

            # if self.alg3_1(eval(nm).name) != nm:
            #     # строка имени параметра должна выдавать именно это значение, а не какое-то другое
            #     return False

            if nm=='mgg.money':
                pass
            elif nm=='mgg.account':
                pass

            return rez

        def __key_gen__(self):
            # исходный список символов для формирования ключей подстановочного шифра
            l0 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
                'abcdefghijklmnopqrstuvwxyz' + \
                '0123456789' + ':.;,!@#$()+=-*_<>~^')
            for i in range(10):
                renpy.random.shuffle(l0)
                Cipher.kdir[i] = ''.join(l0)

        def __cur_gen__(self):
            k0 = renpy.random.randint(0, 9)
            k1 = renpy.random.randint(0, 9)
            while k0 == k1:
                k1 = renpy.random.randint(0, 9)
            k2 = renpy.random.randint(0, 9)
            k3 = renpy.random.randint(0, 9)
            while k2 == k3:
                k3 = renpy.random.randint(0, 9)
            lets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            w1 = w2 = ''
            for i in range(renpy.random.randint(6, 15)):
                w1 += lets[renpy.random.randint(0, 51)]
            for i in range(renpy.random.randint(6, 15)):
                w2 += lets[renpy.random.randint(0, 51)]
            Cipher.cur[0] = str(k0)+str(k1)
            Cipher.cur[1] = str(k2)+str(k3)
            Cipher.cur[2] = w1
            Cipher.cur[3] = w2

        def razdop(self, pr):
            ts = pr[1:-1].split(', ')
            try:
                tday = int(ts[0])
            except:
                print "Не удалось преобразовать день к числу ({t1})".format(t1=ts[0])
                tday = day

            ttm  = ts[1][2:-1]
            ctm = ts[2][2:-1]
            if ts[3] == "None":
                ll = None
            elif ts[3].find('.'):
                ll = float(ts[3])
            else:
                ll = int(ts[3])
            if ts[4] == "None":
                ul = None
            elif ts[3].find('.'):
                ul = float(ts[4])
            else:
                ul = int(ts[4])
            ddop = None if ts[5] == "None" else ts[5][2:-1]

            return dop(tday, ttm, ctm, ll, ul, ddop)

        def to_str(self, val):
            if type(val)==float:
                return self.alg3_0('f_'+str(val))
            elif type(val)==int:
                return self.alg3_0('i_'+str(val))
            else:
                # в остальных случаях на выходе дешифровки будет строка
                return self.alg3_0(str(val))

        def from_str(self, string):
            t = self.alg3_1(string)
            try:
                if t[:2]=='f_':
                    return float(t[2:])
                elif t[:2]=='i_':
                    return int(t[2:])
                else:
                    return t
            except ValueError:
                print "Ошибка преобразования строки в число {t} ({str})".format(t=t, str=string)
                return 0

        def alg0(self, string, mode=0, kw=None):
            # метод Виженера
            tr = []
            keyIndex = 0
            if kw is None:
                kw = Cipher.cur[2]

            for sym in string:
                num = self.LETS.find(sym)
                if num != -1:
                    if mode == 0:
                        num += self.LETS.find(kw[keyIndex])
                    elif mode == 1:
                        num -= self.LETS.find(kw[keyIndex])
                    num %= len(self.LETS)

                    tr.append(self.LETS[num])
                    keyIndex += 1

                    if keyIndex == len(kw):
                        keyIndex = 0
                else:
                    tr.append(sym)
            return ''.join(tr)

        def alg1(self, string, mode=0):
            # Афинный шифр
            if mode > 0:
                return ''.join(map(lambda ch:chr(55*(ord(ch)-3)%128), string)).decode('utf-8')
            else:
                return ''.join(map(lambda ch:chr((7*ord(ch)+3)%128), string.encode('utf-8')))

        def alg2(self, string, mode=0, sk='SagitTariUs'):
            # метод XOR
            if mode==1:
                string = base64.b64decode(string)
            rez = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(string, cycle(sk)))
            if mode==0:
                return base64.b64encode(rez).strip()
            return rez

        def alg3_0(self, string, numb_sys=None, rev=None):
            # мой алгоритм. шифровка в произвольную систему счисления на базе рандомизированной строки
            if numb_sys is None:
                numb_sys = renpy.random.randint(4, 36)  # выбираем систему счисления
            nums = []
            max_len = 1
            if rev is None:
                rev = renpy.random.randint(1, 3)        # каждая rev запись будет в развёрнутом виде
            for ch in string:
                s = ''
                d = ord(ch)  # получаем десятичный код символа
                if d == 0:
                    s = Cipher.NS[0]
                while d > 0:
                    # переводим в выбранную систему счисления, регистр случаен
                    s = (Cipher.NS[d % numb_sys] if renpy.random.randint(0, 1)>0 else Cipher.NS[d % numb_sys].upper())+ s
                    d = d // numb_sys
                max_len = max(max_len, len(s))
                nums.append(s)

            # первые 2 символа - система счисления
            # 3-й символ номер разворачиваемых
            # 4й и 5й - максимальная длина записи символа в развёрнутом виде
            rez = ('0'+str(numb_sys))[-2:]+str(rev)+(('0'+str(max_len))[-2:])[::-1]
            s0 = ''.join('0' for ch in range(max_len))
            x = 0
            for d in nums:
                rez += ((s0 + d)[-max_len:][::-1] if x % rev == 0 else (s0 + d)[-max_len:])
                x += 1

            return rez

        def alg3_1(self, string):
            # мой алгоритм. дешифровка
            try:
                numb_sys = int(string[:2])
                rev      = int(string[2])
                max_len  = int(string[4:2:-1])
            except ValueError:
                print "Ошибка преобразования в число {t1}, {t2}, {t3})".format(t1=string[:2], t2=string[2], t3=string[4:2:-1])
                return ''

            string = string[5:]
            nums = [(string[x:x+max_len][::-1] if (x // max_len) % rev == 0 else string[x:x+max_len]) for x in range(0, len(string), max_len)]
            result = ''
            for st in nums:
                result += chr(int(sum([Cipher.NS.find(st[x].lower())*numb_sys**(len(st)-x-1) for x in range(len(st))])))
            return result

        def alg4(self, crtext, sk='01'):
            # подстановочный шифр
            key1 = self.kdir[int(sk[0])]    # определяем позицию символа в первом ключе
            key2 = self.kdir[int(sk[1])]    # и заменяем символом с такой же позицией из второго ключа
            return ''.join([((key2[key1.find(symbol)] if key1.find(symbol)!=-1 else symbol)) for symbol in crtext])
