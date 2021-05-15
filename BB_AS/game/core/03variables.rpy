
##  Ежедневно обновляемые переменные
default pose2_1 = renpy.random.choice(['01', '02'])
default pose3_1 = renpy.random.choice(['01', '02', '03'])
default pose2_2 = renpy.random.choice(['01', '02'])
default pose3_2 = renpy.random.choice(['01', '02', '03'])
default pose2_3 = renpy.random.choice(['01', '02'])
default pose2_4 = renpy.random.choice(['02', '03'])
default pose3_3 = renpy.random.choice(['01', '02', '03'])
default pose3_4 = renpy.random.choice(['01', '02', '03'])
default random_loc_ab = renpy.random.choice(['a', 'b'])
default tv_scene = renpy.random.choice(['', 'bj', 'hj'])
default random_sigloc = renpy.random.choice(['n', 't'])
default persone_button1 = None
default persone_button2 = None
default persone_button3 = None

default ctd = Countdown(5, '')  #{'time_left':4.9, 'timer_range':4.9, 'timer_jump':''}

################################################################################

##  блоки установки начальных значений переменных
label InitHouse: # стартовая инициация виллы
    python:
        house = [
            Room('my_room', _("МОЯ\nКОМНАТА"), _("МОЯ КОМНАТА"), 'location house myroom icon', 1), #0
            Room('alice_room', _("КОМНАТА\nАЛИСЫ"), _("КОМНАТА АЛИСЫ"), 'location house aliceroom icon', 1), #1
            Room('ann_room', _("КОМНАТА\nАННЫ"), _("КОМНАТА АННЫ"), 'location house annroom icon', 1), #2
            Room('bathroom', _("ВАННАЯ\nКОМНАТА"), _("ВАННАЯ КОМНАТА"), 'location house bathroom icon', 1), #3
            Room('lounge', _("ГОСТИНАЯ"), _("ГОСТИНАЯ"), 'location house lounge icon', 1), #4
            Room('terrace', _("ВЕРАНДА"), _("ВЕРАНДА"), 'location house terrace icon', 1), #5
            Room('courtyard', _("ДВОР"), _("ДВОР"), 'location house courtyard icon', 2), #6
            ]

        locations = {'house': house}

        current_location = house
        current_room = house[5]
        prev_room = house[6]
    return


label InitVariable: # стартовая инициация переменных
    python:
        # current_ver = config.version
        day = 1
        tm = '08:50'
        prevday = 1
        prevtime = '08:50'

        flags = Other_Flags_and_counters()

        spent_time = 0
        cur_ratio = 1
        status_sleep = False
        alarm_time = ''

        InspectedRooms = []
        dishes_washed = False

        CurChar = 'max'
        CurPoss = ""
        search_theme = []

        SpiderKill = 0  # вариант избавления от паука: выкинуть 0, использовать в душе 1, убить 2
        SpiderResp = 0  # дней до гарантированного респа паука: 1 - выкинули с балкона, 2 - запустили в душ, 3 - убили
        NightOfFun = [] # список "ночных забав". Рандомно срабатывает одна из списка

        kol_cream = 0
        kol_choco = 0
        at_comp = False
        view_cam = Null

        prenoted = 0     # замечено отсутствие Эрика в комнате Ани

        ae_tv_order = ['0'+str(i) for i in range(1, 8)]     # последовательность фильмов, просматриваемых Анной и Эриком
        ol_tv_order = ['0'+str(i) for i in range(1, 8)]     # последовательнгость сериалов для Лизы и Оливии
        cam_poses = {}

    return


label InitCharacters: # стартовая инициация персонажей
    python:
        chars = {
            'alice': Profile('alice', _("Алиса"), _("Алисы"), _("Алисе"), _("Алису"), _("Алисой"), _("Алисе"),
                    _("Алиса, моя старшая сестра.  В любой непонятной ситуации бьёт по лицу (в лучшем случае). Недавно закончила школу и, так же, как и я, ищет свой путь. Целыми днями сидит в ноутбуке и занимается каким-то своим блогом. Как это часто бывает с братьями и старшими сёстрами, мы не очень ладим..."),
                    'Alice'),
            'lisa': Profile('lisa', _("Лиза"), _("Лизы"), _("Лизе"), _("Лизу"), _("Лизой"), _("Лизе"),
                    _("Лиза, младшая сестрёнка. Милая и весёлая. Она ещё учится в школе. С Лизой мы общаемся на одной волне, хотя изредка ссоримся. Но если что-то случается, защиты ищет именно у меня."),
                    'Lisa', relmax=150),
            'ann': Profile('ann', _("Анна"), _("Анны"), _("Анне"), _("Анну"), _("Анной"), _("Анне"), _("Анна, моя мама. Сама воспитывает нас с двумя сёстрами уже несколько лет. Работает в офисе какой-то компании. Хотя, зарплата у неё вполне приличная, но почти всё уходит на оплату жилья, еду и одежду."),
                    'Ann', relmax=250),
            }

        mgg = MaxProfile('mgg', _("Макс"),  _("Макса"), _("Максу"), _("Макса"), _("Максом"), _("Максе"),
                                _("Всегда в поисках приключений на свою пятую точку."), 'Max info-00')

        alice = chars['alice']
        ann   = chars['ann']
        lisa  = chars['lisa']

    # расписание
    call set_alice_schedule from _call_set_alice_schedule_1

    call set_ann_schedule from _call_set_ann_schedule_1

    call set_lisa_schedule from _call_set_lisa_schedule_1

    python:
        # предметы
        items = {}
        checking_items()

        # список товаров для доставки
        delivery_list = [[], []]

        # одежда
        checking_clothes()

        infl = {
            lisa : Influence(),
            ann : Influence(),
            alice : Influence(),
            }
        #     lisa.clothes.casual     = Clothes(_("Повседневная"), [Garb('a', '01a', 'Обычная одежда')])
        #     lisa.clothes.sleep      = Clothes(_("Для сна"),
        #                     [Garb('a', '02', 'Обычная одежда'), Garb('b', '02a', 'Маечка и трусики')])
        #     lisa.clothes.swimsuit   = Clothes(_("КУПАЛЬНИК"), [Garb('a', '03', 'Закрытый купальник')])
        #     lisa.clothes.learn      = Clothes(_("За уроками"),
        #                     [Garb('a', '01a', 'Обычная одежда'), Garb('c', '04b', 'Полотенце', True)])
        #
        #     alice.clothes.casual = Clothes(_("Повседневная"), [Garb('a', '01a', 'Обычная одежда', True)])
        #     alice.clothes.sleep = Clothes(_("Для сна"), [Garb('a', '02', 'Белое кружевное бельё', True)])
        #
        #     ann.clothes.casual = Clothes(_("Повседневная"),
        #                     [Garb('a', '01a', 'Обычная одежда', False, True), Garb('b', '01b', 'Футболка', False, True)])
        #     ann.clothes.cook_morn = Clothes(_("Для приготовления завтрака"),
        #                     [Garb('a', '05b', 'Спортивная форма + фартук', False, True), Garb('b', '01c', 'Футболка + фартук', False, True)])
        #     ann.clothes.cook_eve = Clothes(_("Для приготовления ужина"), [Garb('b', '01c', 'Футболка + фартук', False, True)])
        #     ann.clothes.rest_morn = Clothes(_("Для утреннего отдыха"), [Garb('a', '01b', 'Футболка', False, True)])
        #
        #     ann.clothes.rest_eve = Clothes(_("Для вечернего отдыха"),
        #                     [Garb('a', '01b', 'Футболка', False, True), Garb('b', '04b', 'Полотенце', False, True)])
        #     ann.clothes.sleep = Clothes(_("Для сна"), [Garb('a', '02', 'Обычная одежда для сна')])
        #
        #     ann.clothes.rest_eve.rand = True
        #     ann.clothes.casual.rand = True
        #     ann.clothes.cook_morn.rand = True
        #
        #     mgg.clothes.casual = Clothes(_("Повседневная"), [Garb('a', '01a', 'Обычная одежда', True)])

    return


label InitActions: # кнопки действий
    python:
        AvailableActions = OrderedDict([
            ('momovie'     , ActionsButton(_("ПОСМОТРЕТЬ\nФИЛЬМ"), 'interface disc', 'WatchMovie')),
            ('city'        , ActionsButton(_("ВЫЙТИ\nИЗ ДОМА"), 'interface city', 'GoCity')),
            ('touch'       , ActionsButton(_("ПОИГРАТЬ\nС ЛИЗОЙ"), 'interface touch', 'TouchLisa')),
            ('usb'         , ActionsButton(_("УСТАНОВИТЬ\nКЕЙЛОГГЕР"), 'interface usb', 'InstallKeylogger')),
            ('install'     , ActionsButton(_("УСТАНОВИТЬ\nКАМЕРУ"), 'interface install', 'InstallCam')),
            ('hidespider'  , ActionsButton(_("СПРЯТАТЬ\nПАУКА"), 'interface spider', 'HideSpider')),
            ('throwspider3', ActionsButton(_("БРОСИТЬ\nПАУКА"), 'interface spider', 'BathroomSpider')),
            ('throwspider6', ActionsButton(_("БРОСИТЬ\nПАУКА"), 'interface spider', 'CourtyardSpider')),
            ('catchspider' , ActionsButton(_("ИСКАТЬ\nПАУКОВ"), 'interface spider', 'SearchSpider')),
            ('searchciga'  , ActionsButton(_("ИСКАТЬ\nСИГАРЕТЫ"), 'interface search', 'SearchCigarettes')),
            ('searchbook'  , ActionsButton(_("ИСКАТЬ\nКНИГУ"), 'interface search', 'SearchSecretBook')),
            ('clearpool'   , ActionsButton(_("ЧИСТИТЬ\nБАССЕЙН"), 'interface clearpool', 'ClearPool')),
            ('readbook'    , ActionsButton(_("ЧИТАТЬ"), 'interface book', 'BookRead', True)),
            ('searchcam'   , ActionsButton(_("ИСКАТЬ\nКАМЕРУ"), 'interface search', 'SearchCam')),
            ('unbox'       , ActionsButton(_("РАЗОБРАТЬ\nКОРОБКИ"), 'interface box', 'Box')),
            ('notebook'    , ActionsButton(_("ВКЛЮЧИТЬ\nНОУТБУК"), 'interface notebook', 'Notebook', True)),
            ('sleep'       , ActionsButton(_("СПАТЬ"), 'interface sleep', 'Sleep', True)),
            ('alarm'       , ActionsButton(_("УСТАНОВИТЬ\nБУДИЛЬНИК"), 'interface alarm', 'Alarm', True)),
            ('nap'         , ActionsButton(_("ВЗДРЕМНУТЬ"), 'interface alarm', 'Nap', True)),
            ('shower'      , ActionsButton(_("ПРИНЯТЬ\nДУШ"), 'interface shower', 'Shower', True)),
            ('bath'        , ActionsButton(_("ПРИНЯТЬ\nВАННУ"), 'interface bath', 'Bath', True)),
            ('talk'        , ActionsButton(_("ПОГОВОРИТЬ"), 'interface talk', 'StartDialog')),
            ('dishes'      , ActionsButton(_("МЫТЬ\nПОСУДУ"), 'interface dishes', 'DishesWashed')),
            ])
    return


label InitPoss: # Возможности
    $ poss = {}
    $ poss_update()
    return


label InitTalksEvents: # стартовая инициация диалогов и событий

    # Переменные влияющие на запуск диалогов

    $ cooldown = {
        'learn'         : '0 00:00',
        'blog'          : '0 00:00',
        'lisa_boy'      : '0 00:00',
        'talkcooldown'  : '0 00:00',
        }

    # переменные со счетчиком дней

    $ dcv = Daily_list()

    $ wcv = Weekly_list()

    return


label InitCources:  # онлайн курсы
    $ online_cources = [
        OnLineCources(_("Общение"), 'social', 'com', [
            OnLineCource(_("Навыки общения: Чувства человека"), _("Это базовый курс обучения навыкам общения и содержит в себе основную информацию об органах чувств, о реакции человека на ваши слова, а также основы языка тела."), 3, 200, 2),
            OnLineCource(_("Навыки общения: Основы коммуникации"), _("Это второй курс обучения навыкам общения. Из него вы узнаете как повлиять на решение человека без слов, как подобрать правильный слова в нужной ситуации для достижения своей цели."), 3, 400, 2),
            OnLineCource(_("Навыки общения: Без границ"), _("Это продвинутый длительный курс, предназначенный для тех, кто хочет постоянно обучаться и совершенствоваться. На данный момент это последний доступный курс."), 3, 800, 2),
            ]),
        ]
    $ CurCource = online_cources[0]
    return


label InitPunish:  # стартовая инициация наказаний
    $ warning = 0
    $ punreason = [
        0,  # подглядывал за Лизой и она рассказала об этом Анне
        0,  # подглядывал за Алисой и она рассказала об этом Анне
        0,  # подглядывал за Анной
        0,  # подглядывал за Анной с Эриком  в спальне
        0,  # грубо говорил об Эрике в разговоре с Анной
        0,  # подкинул паука Алисе в душ
        0,  # подглядывал за Анной с Эриком  в душе
        0,  # подглядывал за Лизой и засекла Анна
        ]
    $ punlisa = []
    $ punalice = []
    $ newpunishment = 0
    $ pun_list = []
    return


label AddEric:
    $ chars['eric'] = Profile('eric', _("Эрик"), _("Эрика"), _("Эрику"), _("Эрика"), _("Эриком"), _("Эрике"), _("Ещё до того, как мама познакомила меня со своим внезапным ухажёром Эриком, я начал чувствовать, что ничего хорошего он в мою жизнь не принесёт. Слишком уж он подозрительный..."), "Eric")
    $ eric = chars['eric']

    call set_eric_schedule from _call_set_eric_schedule_1
    call ann_after_appearance_eric from _call_ann_after_appearance_eric_1
    $ infl[ann].freeze = False
    return


label AddKira:
    # добавляем Киру и её расписание
    $ chars['kira'] = Profile('kira', _("Кира"), _("Киры"), _("Кире"), _("Киру"), _("Кирой"), _("Кире"), _("Тётя Кира, мамина младшая сестра. Конечно, у неё и раньше не были замечены какие-либо комплексы, но сейчас она стала такой... такой..."), "Kira")
    $ kira = chars['kira']
    call set_kira_schedule from _call_set_kira_schedule_1

    # обновляем расписание Лизы и Алисы
    call alice_after_arrival_kira from _call_alice_after_arrival_kira_1

    # добавляем новую одежду Максу и девчонкам
    $ setting_clothes_by_conditions()

    $ ChoiceClothes()

    $ added_mem_var('kira')

    $ infl[kira] = Influence()

    return


label alice_add_black_linderie:
    $ added_mem_var('black_linderie')
    $ items['b.lingerie'].give()
    $ alice.gifts.append('black_linderie')
    $ setting_clothes_by_conditions()

    if alice.plan_name=='blog':
        $ alice.dcv.feature.set_lost(1) # включаем суточный откат, чтобы Алиса не начала блог в белье в этот же день, если блог уже начат

    # прописываем расписание:
    call alice_can_blog_in_underwear from _call_alice_can_blog_in_underwear_1

    # $ blog_lingerie = ['a', 'a', 'a', 'b', 'b', 'b']
    # $ renpy.random.shuffle(blog_lingerie)
    # $ cur_blog_lingerie = 'b'

    return


label AddOlivia:
    # добавляем Оливию и её расписание
    $ chars['olivia'] = Profile('olivia', _("Оливия"), _("Оливии"), _("Оливии"), _("Оливию"), _("Оливией"), _("Оливии"), _("Оливия, одноклассница моей младшей сестрёнки Лизы. Довольно милая девчонка. А главное с изюминкой... Ходит по школе без трусиков, а у себя по дому вообще голая, как и её родители, они ведь натуристы. Это классно, что у Лизы появилась такая интересная подружка!"), "Olivia")
    $ olivia = chars['olivia']
    call set_olivia_shedule from _call_set_olivia_shedule

    $ added_mem_var('olivia')

    return
