

#######################################################################################################################
## Локации

default house = [
    Room("my_room", _("МОЯ\nКОМНАТА"), "location house myroom icon", 1), #0
    Room("alice_room", _("КОМНАТА\nАЛИСЫ"), "location house aliceroom icon", 1), #1
    Room("ann_room", _("КОМНАТА\nАННЫ"), "location house annroom icon", 1), #2
    Room("bathroom", _("ВАННАЯ\nКОМНАТА"), "location house bathroom icon", 2), #3
    Room("lounge", _("ГОСТИНАЯ"), "location house lounge icon", 3), #4
    Room("terrace", _("ВЕРАНДА"), "location house terrace icon", 1), #5
    Room("courtyard", _("ДВОР"), "location house courtyard icon", 2), #6
]

default locations = {"house": house}


#######################################################################################################################
## Персонажи

default characters = {
     "lisa": Profile(_("Лиза"), _("Лизы"), _("Лизе"), _("Лизу"), _("Лизой"), _("Лизе"),
        _("Лиза, младшая сестрёнка. Милая и весёлая. Она ещё учится в школе. С Лизой мы общаемся на одной волне, хотя изредка ссоримся. Но если что-то случается, защиты ищет именно у меня."),
        "Lisa", relmax=150),
     "alice": Profile(_("Алиса"), _("Алисы"), _("Алисе"), _("Алису"), _("Алисой"), _("Алисе"),
        _("Алиса, моя старшая сестра.  В любой непонятной ситуации бьёт по лицу (в лучшем случае). Недавно закончила школу и, так же, как и я, ищет свой путь. Целыми днями сидит в ноутбуке и занимается каким-то своим блогом. Как это часто бывает с братьями и старшими сёстрами, мы не очень ладим..."),
         "Alice"),
     "ann": Profile(_("Анна"), _("Анны"), _("Анне"), _("Анну"), _("Анной"), _("Анне"), _("Анна, моя мама. Сама воспитывает нас с двумя сёстрами уже несколько лет. Работает в офисе какой-то компании. Хотя, зарплата у неё вполне приличная, но почти всё уходит на оплату жилья, еду и одежду."),
        "Ann", 0, 0, 2),
    }

default max_profile = MaxProfile(_("Макс"),  _("Макса"), _("Максу"), _("Макса"), _("Максом"), _("Максе"),
                        _("Всегда в поисках приключений на свою пятую точку"), "Max info-00")

default sex_stat = {
    "lisa" : SexStat(),
    "alice": SexStat(),
    "ann"  : SexStat(),
    }


#######################################################################################################################
## Расписание персонажей

default schedule_lisa = [
    Schedule((0, 1, 2, 3, 4, 5, 6), "0:0", "6:59", _("спит в нашей комнате (ночь)"), "house", 0, "lisa_sleep", dress="sleepwear", enabletalk=False),
    Schedule((0, 1, 2, 3, 4, 5, 6), "7:0", "7:59", _("принимает душ"), "house", 3, "lisa_shower", dress="naked", enabletalk=False),
    Schedule((0, 1, 2, 3, 4, 5, 6), "8:0", "8:59", _("читает в нашей комнате"), "house", 0, "lisa_read", dress="casual2"),
    Schedule((1, 2, 3, 4, 5), "10:0", "10:59", _("одевается в школу"), "house", 0, "lisa_dressed_school", dress="dressed", enabletalk=False),
    Schedule((6, ), "10:0", "10:59", _("одевается в магазин"), "house", 0, "lisa_dressed_shop", dress="dressed", enabletalk=False),
    Schedule((0, ), "10:0", "10:59", _("одевается за закрытыми дверями"), "house", 0, "lisa_dressed_somewhere", dress="dressed", enabletalk=False),
    Schedule((1, 2, 3, 4, 5), "11:0", "15:59", _("в школе"), dress="shcool"),
    Schedule((6, ), "11:0", "13:59", _("в магазине"), dress="out"),
    Schedule((0, ), "11:0", "14:59", dress="out"),
    Schedule((6, ), "14:0", "14:59", _("читает в нашей комнате"), "house", 0, "lisa_read", dress="casual"),
    Schedule((0, 6), "15:0", "15:59", _("в бассейне"), "house", 6, "lisa_swim", dress="swim"),
    Schedule((1, 2, 3, 4, 5), "16:0", "16:59", _("в бассейне"), "house", 6, "lisa_swim", dress="swim"),
    Schedule((6, ), "16:0", "16:59", _("загорает"), "house", 6, "lisa_sun", dress="swim"),
    Schedule((0, ), "16:0", "16:59", _("читает в нашей комнате"), "house", 0, "lisa_read", dress="casual2"),
    Schedule((1, 2, 3, 4, 5), "17:0", "18:59", _("загорает"), "house", 6, "lisa_sun", dress="swim"),
    Schedule((0, 6), "17:0", "18:59", _("читает в нашей комнате"), "house", 0, "lisa_read", dress="casual2"),
    Schedule((0, 1, 2, 3, 4, 5, 6), "20:0", "20:59", _("моет посуду"), "house", 4, "lisa_dishes", dress="casual", talklabel="lisa_dishes_closer"),
    Schedule((0, 1, 2, 3, 4, 5, 6), "21:0", "21:59", _("лежит с телефоном в нашей комнате"), "house", 0, "lisa_phone", dress="casual"),
    Schedule((0, 1, 2, 3, 4, 5, 6), "22:0", "22:59", _("принимает ванну"), "house", 3, "lisa_bath", dress="naked", enabletalk=False),
    Schedule((1, 2, 3, 4, 5), "23:0", "23:59", _("учит уроки"), "house", 0, "lisa_homework", dress="learn"),
    Schedule((0, 6), "23:0", "23:59", _("лежит с телефоном в нашей комнате"), "house", 0, "lisa_phone", dress="casual2"),
    ]

default schedule_ann  = [
    Schedule((0, 1, 2, 3, 4, 5, 6), "0:0", "5:59", _("спит"), "house", 2, "ann_sleep", dress="sleepwear", enabletalk=False),
    Schedule((0, 1, 2, 3, 4, 5, 6), "6:0", "6:59", _("принимает душ"), "house", 3, "ann_shower", dress="naked", enabletalk=False),
    Schedule((0, 1, 2, 3, 4, 5, 6), "7:0", "7:59", _("занимается йогой"), "house", 6, "ann_yoga", dress="yoga"),
    Schedule((0, 1, 2, 3, 4, 5, 6), "8:0", "8:59", _("готовит завтрак"), "house", 4, "ann_cooking", dress="cooking", talklabel="ann_cooking_closer"),
    Schedule((1, 2, 3, 4, 5), "10:0", "10:59", _("одевается на работу"), "house", 2, "ann_dressed_work", dress="dressed", enabletalk=False),
    Schedule((6, ), "10:0", "10:59", _("одевается в магазин"), "house", 2, "ann_dressed_shop", dress="dressed", enabletalk=False),
    Schedule((0, ), "10:0", "11:59", _("в своей комнате"), "house", 2, "ann_resting", dress="casual"),
    Schedule((1, 2, 3, 4, 5), "11:0", "18:59", _("на работе"), dress="work"),
    Schedule((6, ), "11:0", "13:59", _("в магазине"), dress="out"),
    Schedule((0, ), "12:0", "13:59", _("читает на веранде"), "house", 5, "ann_read", dress="work"),
    Schedule((0, 6), "14:0", "14:59", _("в бассейне"), "house", 6, "ann_swim", dress="swim"),
    Schedule((0, 6), "15:0", "15:59", _("в своей комнате"), "house", 2, "ann_resting", dress="casual"),
    Schedule((0,), "16:0", "16:59", _("в бассейне"), "house", 6, "ann_swim", dress="swim"),
    Schedule((6,), "16:0", "16:59", _("читает на веранде"), "house", 5, "ann_read", dress="casual"),
    Schedule((6, ), "17:0", "17:59", _("загорает"), "house", 6, "ann_sun", dress="swim"),
    Schedule((0, ), "17:0", "17:59",_("читает на веранде"), "house", 5, "ann_read", dress="casual"),
    Schedule((0, 6), "18:0", "18:59", _("готовит ужин"), "house", 4, "ann_cooking", dress="cooking", talklabel="ann_cooking_closer"),
    Schedule((0, 1, 2, 3, 4, 5, 6), "20:0", "20:59", _("принимает ванну"), "house", 3, "ann_bath", dress="naked", enabletalk=False),
    Schedule((0, 1, 2, 3, 4, 5, 6), "21:0", "21:59", _("смотрит ТВ"), "house", 4, "ann_tv", dress="casual3", talklabel="ann_tv_closer"),
    Schedule((0, 1, 2, 3, 4, 5, 6), "22:0", "23:59", _("в своей комнате"), "house", 2, "ann_resting", dress="casual2"),
    ]

default schedule_alice = [
    Schedule((1, 2, 3, 4, 5, 6, 0), "0:0", "0:59", _("принимает ванну"), "house", 3, "alice_bath", dress="naked", enabletalk=False),
    Schedule((1, 2, 3, 4, 5, 6, 0), "1:0", "7:59", _("спит"), "house", 1, "alice_sleep", dress="sleepwear", enabletalk=False),
    Schedule((1, 2, 3, 4, 5, 6, 0), "8:0", "8:59", _("принимает душ"), "house", 3, "alice_shower", dress="naked", enabletalk=False),
    Schedule((1, 2, 3, 4, 5), "10:0", "10:59", _("в своей комнате"), "house", 1, "alice_rest_morning", dress="casual", talklabel="alice_morning_closer"),
    Schedule((6,), "10:0", "10:59", _("одевается в магазин"), "house", 1, "alice_dressed_shop", dress="dressed", enabletalk=False),
    Schedule((0,), "10:0", "10:59", _("моет посуду"), "house", 4, "alice_dishes", 1, 0, 0, "not dishes_washed", dress="casual", talklabel="alice_dishes_closer"),
    Schedule((0,), "10:0", "10:59", _("читает на веранде"), "house", 5, "alice_read", 1, 0, 0, "dishes_washed", dress="casual"),
    Schedule((1, 2, 3, 4, 5), "11:0", "11:59", _("моет посуду"), "house", 4, "alice_dishes", 1, 0, 0, "not dishes_washed", dress="casual", talklabel="alice_dishes_closer"),
    Schedule((1, 2, 3, 4, 5), "11:0", "11:59", _("читает на веранде"), "house", 5, "alice_read", 1, 0, 0, "dishes_washed", dress="casual"),
    Schedule((0,), "11:0", "11:59", _("куда-то одевается"), "house", 1, "alice_dressed_somewhere", dress="dressed", enabletalk=False),
    Schedule((1, 2, 3, 4, 5), "12:0", "12:59", _("загорает"), "house", 6, "alice_sun", dress="swim"),
    Schedule((1, 2, 3, 4, 5), "13:0", "13:59", _("в бассейне"), "house", 6, "alice_swim", dress="swim"),  # потом заменится на вариативное курит/плавает
    Schedule((6,), "11:0", "13:59", _("в магазине"), dress="out"),
    Schedule((1, 2, 3, 4, 5), "14:0", "14:59", _("в бассейне"), "house", 6, "alice_swim", dress="swim"),
    Schedule((6,), "14:0", "14:59", _("куда-то одевается"), "house", 1, "alice_dressed_somewhere", dress="dressed", enabletalk=False),
    Schedule((1, 2, 3, 4, 5), "15:0", "15:59", _("загорает"), "house", 6, "alice_sun", dress="swim"),
    Schedule((1, 2, 3, 4, 5), "16:0", "17:59", _("читает на веранде"), "house", 5, "alice_read", dress="casual"),
    Schedule((6,), "15:0", "16:59", dress="out"),
    Schedule((0,), "12:0", "16:59", dress="out"),
    Schedule((6,), "17:0", "17:59", _("читает на веранде"), "house", 5, "alice_read", dress="casual"),
    Schedule((0,), "17:0", "17:59", _("в бассейне"), "house", 6, "alice_swim", dress="swim"),
    Schedule((1, 2, 3, 4, 5), "18:0", "18:59", _("готовит ужин"), "house", 4, "alice_cooking_dinner", dress="cooking", talklabel="alice_cooking_closer"),
    Schedule((0,), "18:0", "18:59", _("читает на веранде"), "house", 5, "alice_read", dress="casual"),
    Schedule((6,), "18:0", "18:59", _("загорает"), "house", 6, "alice_sun", dress="swim"),
    Schedule((1, 2, 3, 4, 5, 6, 0), "20:0", "21:59", _("в своей комнате"), "house", 1, "alice_rest_evening", dress="casual2", talklabel="alice_evening_closer"),
    Schedule((1, 2, 3, 4, 5, 6, 0), "22:0", "23:59", _("смотрит ТВ"), "house", 4, "alice_tv", dress="casual2", talklabel="alice_tv_closer"),
    ]

#######################################################################################################################
## Кнопки действий

default AvailableActions = {
    "momovie"     : ActionsButton(_("ПОСМОТРЕТЬ\nФИЛЬМ"), "interface disc", "WatchMovie"),
    "city"        : ActionsButton(_("ВЫЙТИ\nИЗ ДОМА"), "interface city", "GoCity"),
    "touch"       : ActionsButton(_("ПОИГРАТЬ\nС ЛИЗОЙ"), "interface touch", "TouchLisa"),
    "usb"         : ActionsButton(_("УСТАНОВИТЬ\nКЕЙЛОГГЕР"), "interface usb", "InstallKeylogger"),
    "install"     : ActionsButton(_("УСТАНОВИТЬ\nКАМЕРУ"), "interface install", "InstallCam"),
    "hidespider"  : ActionsButton(_("СПРЯТАТЬ\nПАУКА"), "interface spider", "HideSpider"),
    "throwspider3": ActionsButton(_("БРОСИТЬ\nПАУКА>"), "interface spider", "BathroomSpider"),
    "throwspider6": ActionsButton(_("БРОСИТЬ\nПАУКА>"), "interface spider", "CourtyardSpider"),
    "catchspider" : ActionsButton(_("ИСКАТЬ\nПАУКОВ>"), "interface spider", "SearchSpider"),
    "searchciga"  : ActionsButton(_("ИСКАТЬ\nСИГАРЕТЫ"), "interface search", "SearchCigarettes"),
    "searchbook"  : ActionsButton(_("ИСКАТЬ\nКНИГУ"), "interface search", "SearchSecretBook"),
    "clearpool"   : ActionsButton(_("ЧИСТИТЬ\nБАССЕЙН"), "interface clearpool", "ClearPool"),
    "readbook"    : ActionsButton(_("ЧИТАТЬ"), "interface book", "BookRead"),
    "searchcam"   : ActionsButton(_("ИСКАТЬ\nКАМЕРУ"), "interface search", "SearchCam"),
    "unbox"       : ActionsButton(_("РАЗОБРАТЬ\nКОРОБКИ"), "interface box", "Box"),
    "notebook"    : ActionsButton(_("ВКЛЮЧИТЬ\nНОУТБУК"), "interface notebook", "Notebook", True),
    "sleep"       : ActionsButton(_("СПАТЬ"), "interface sleep", "Sleep", True),
    "alarm"       : ActionsButton(_("УСТАНОВИТЬ\nБУДИЛЬНИК"), "interface alarm", "Alarm", True),
    "nap"         : ActionsButton(_("ВЗДРЕМНУТЬ"), "interface alarm", "Nap", True),
    "shower"      : ActionsButton(_("ПРИНЯТЬ\nДУШ"), "interface shower", "Shower", True),
    "bath"        : ActionsButton(_("ПРИНЯТЬ\nВАННУ"), "interface bath", "Bath", True),
    "talk"        : ActionsButton(_("ПОГОВОРИТЬ"), "interface talk", "StartDialog"),
    "dishes"      : ActionsButton(_("МЫТЬ\nПОСУДУ"), "interface dishes", "DishesWashed"),
    }

# список ключей словаря кнопок. создан заранее для сохраниения нужного порядка
default ListButton = [
    "momovie",
    "city",
    "touch",
    "usb",
    "install",
    "hidespider",
    "throwspider3",
    "throwspider6",
    "catchspider",
    "searchciga",
    "searchbook",
    "clearpool",
    "readbook",
    "searchcam",
    "unbox",
    "nap",
    "alarm",
    "sleep",
    "shower",
    "notebook",
    "bath",
    "talk",
    "dishes",
    ]

#######################################################################################################################
## Предметы

default ShopCat = {
    0 : _("Одежда"),
    1 : _("Книги"),
    2 : _("Продукты"),
    3 : _("Электроника"),
    4 : _("Товары 18+"),
    5 : _("Косметика"),
    6 : _("Украшения"),
    7 : _("Другое"),
    }

default items = {
    "spider": Item(_("ПАУК"), _("Самое страшное существо на свете. С точки зрения Алисы, конечно. Нужно этим воспользоваться в подходящий момент!"), "spider", None),
    "hide_cam": Item(_("СКРЫТАЯ КАМЕРА"), _("Высокотехнологичная микро-камера, предназначенная для скрытного наблюдения. Имеет радиомодуль для беспроводной передачи зашифрованного цифрового видеосигнала."), "cam", 3, 990),
    "ann_movie": Item(_("ФИЛЬМ \"ШКОЛЬНИЦЫ\""), _("Строгая учительница пытается наказать непослушных школьниц..."), "", None),
    "bathrobe": Item(_("ШЕЛКОВЫЙ ХАЛАТ"), _("Короткий, лёгкий, почти шёлковый халат высшего качества. Made in China."), "bathrobe", 0, 100, True, cells=2),
    "bikini": Item(_("КУПАЛЬНИК КРАСНЫЙ"), _("Купальник для тех, кто не стесняется своего тела. Скрывает только самые интимные участки. Всё остальное открыто для солнца и глаз окружающих."), "bikini", 0, 200, True, cells=2),
    "cigarettes": Item(_("СИГАРЕТЫ"), _("Пачка сигарет Lucky Strike. Для настоящих мужчин!"), "cigarettes", 7, 10),
    "dress": Item(_("МАЛЕНЬКОЕ ЧЕРНОЕ ПЛАТЬЕ"), _("Отличный подарок для девушки, желающей произвести фурор на вечеринке или дискотеке."), "dress-1", 0, 200, cells=2),
    "erobook_1": Item(_("ЛЮБЯЩАЯ РУБИ"), _("Роман о запретной любви между секретаршей и её начальником, полный любви, страсти, эмоций и... мистики."), "erobook-1", 1, 20, True),
    "erobook_2": Item(_("ПРЕМЬЕР-МИНИСТР"), _("Новый эротический роман, входящий в Топ-10 лучших романов и новелл США!"), "erobook-2", 1, 30, True),
    "erobook_3": Item(_("БЫТЬ КУКЛОЙ"), _("В поместье Картера красивые девушки обучаются, чтобы стать идеальными жёнами для самых влиятельных людей этого мира."), "erobook-3", 1, 50, True),
    "erobook_4": Item(_("КНИГА ОРГАЗМОВ"), _("Что получится, если собрать самые горячие истории об оргазмах от 69 различных авторов?"), "erobook-4", 1, 75, True),
    "erobook_5": Item(_("ИСТОРИЯ О"), _("Это история о доминировании и подчинении. История об одной прекрасной девушке по имени О."), "erobook-5", 1, 100, True),
    "ladder": Item(_("Стремянка"), _("Небольшая стремянка, позволяющая достать то, для чего не хватает роста"), "ladder", 7, cells=2),
    "manual": Item(_("WEB STANDARDS"), _("Книга рассказывает о способах создавать свои сайты, работающие на любых устройствах."), "manual-1", 1, 100, True),
    #"": Item(_(""), _(""), "", , ),
    }

#######################################################################################################################
## Установка начальных значений переменных

default current_ver = config.version  # устанавливаем
default day = 1
default tm = "09:00"

default spent_time = 0
default cur_ratio = 1
default status_sleep = False
default alarm_time = ""


default next_learn = "0 00:00"

default money = 150
default current_location = house
default current_room = house[5]
default prev_room = house[6]
default InspectedRooms = []

default number_autosave = 0
default number_quicksave = 0

default flags = {
    "Lisa_bathrobe" : False,
    "morning_erect" : 0,
    "about_poss"    : True,
    "little_energy" : False,
}

default dress_suf = {
    "ann"  :"a",
    "alice":"a",
    "lisa" :"a",
    "max"  :"a",
    "ann-sleepwear"  :"a",
    "alice-sleepwear":"a",
    "lisa-sleepwear" :"a",
    "max-sleepwear"  :"a",
    "lisa-learn"     :"a",
}

default swim_suf = {
    "ann":"a",
    "alice":"a",
    "lisa":"a",
}
#######################################################################################################################
## переменные для экранов

default CurChar = "max"
default CurPoss = ""
default search_theme = []

#######################################################################################################################
##  Ежедневно обновляемые переменные

default random2_1 = renpy.random.choice(["01", "02"])
default random3_1 = renpy.random.choice(["01", "02", "03"])
default random4_1 = renpy.random.choice(["01", "02", "03", "04"])
default random2_2 = renpy.random.choice(["01", "02"])
default random3_2 = renpy.random.choice(["01", "02", "03"])
default random4_2 = renpy.random.choice(["01", "02", "03", "04"])
default random2_3 = renpy.random.choice(["01", "02"])
default random3_3 = renpy.random.choice(["01", "02", "03"])
default random4_3 = renpy.random.choice(["01", "02", "03", "04"])
default random5   = renpy.random.choice(["01", "02", "03", "04", "05"])
default random6   = renpy.random.choice(["01", "02", "03", "04", "05", "06"])
default random_ab = renpy.random.choice(["a", "b"])
default random_suf = renpy.random.choice(["a", "b"])

# переменные со счетчиком дней
default dcv = {
    "pool_cleaned"    : Dayly(enabled=True),
    "order_cosmetics" : Dayly(enabled=True),
    "order_product"   : Dayly(enabled=True),
    "delivery"        : Dayly(),
}

# события, запускаемые в конкретное время
default EventsByTime = {
    "breakfast"        : CutEvent("09:00", label="breakfast", desc="завтрак", cut=True),
    "dinner"           : CutEvent("19:00", label="dinner", desc="ужин", cut=True),
    "shoping"          : CutEvent("11:00", (6, ), False, "shoping", "семейный шопинг"),
    "MorningWood"      : CutEvent("06:30", label="MorningWood", variable="day == 2", sleep=True, desc="утренний стояк", extend=True),
    "AfterSchoolFD"    : CutEvent("16:00", label="AfterSchoolFD", variable="day == 1", desc="Лиза первый раз приходит из школы", cut=True),
    "Wearied"          : CutEvent("03:30", label="Wearied", sleep=False, desc="поспать бы надо"),
}

# ежедневное подсматривание
default peeping = {
    "ann_shower"   : 0,
    "lisa_shower"  : 0,
    "alice_shower" : 0,
    "ann_dressed"  : 0,
    "lisa_dressed" : 0,
    "alice_dressed": 0,
    "ann_eric_tv"  : 0,
    "ann_eric_sex1": 0,
    "ann_eric_sex2": 0,
    "ann_bath"     : 0,
    "lisa_bath"    : 0,
    "alice_bath"   : 0,
    "alice_sleep"  : 0,
    "ann_sleep"    : 0,
}

# Переменные отвечающие за изображение в экране информации
default lisa_dress = {
    "casual"    : "01a",
    "casual2"   : "01a",
    "sleepwear" : "02",
    "shcool"    : "01b",
    "learn"     : "01a",
    "out"       : "01",
    "swim"      : "03",
    "naked"     : "04a",
    "dressed"   : "00b",
}

default ann_dress = {
    "casual"    : "01b",
    "yoga"      : "05",
    "casual2"   : "04b",
    "casual3"   : "04b",
    "sleepwear" : "02",
    "work"      : "01a",
    "out"       : "01",
    "swim"      : "03",
    "naked"     : "00b",
    "dressed"   : "00b",
    "cooking"   : "01c",
}

default alice_dress = {
    "casual"    : "01a",
    "casual2"   : "01aa",
    "sleepwear" : "02",
    "out"       : "01",
    "swim"      : "03",
    "naked"     : "04aa",
    "dressed"   : "00b",
    "cooking"   : "01b",
}

# Возможности
default possibility = {
    "cams" : Poss(_("Скрытые камеры"), [
            PossStage("interface poss cams 00", _("Я нашёл пустую коробку из под скрытой камеры. Видимо, она установлена где-то в доме. Нужно поискать как следует - вдруг, кто-то за нами наблюдал всё это время?")),
            PossStage("interface poss cams 01", _("Итак, я нашёл скрытую камеру в гостиной. Она вмонтирована в стену, видимо, во время ремонта. Поэтому, её нельзя вытащить, не повредив. Кроме того, оказалось, что камера сейчас ни к чему не подключена. Может быть, стоит целенаправленно изучить способы подключения камер, чтобы извлечь из неё какую-то пользу...")),
            PossStage("interface poss cams 01", _("Ко мне пришла отличная идея - заработать на трансляции с веб-камеры в интернет, но я об этом знаю очень мало... Может быть, поможет какая-то литература?")),
            PossStage("interface poss cams 01", _("так, я внимательно прочитал книгу Web Standards и разобрался как сделать свой сайт. Пожалуй, стоит начать именно с этого. Мне потребуются деньги на домен, хостинг и оплату готового шаблона с дизайном. Всего нужно порядка $100.")),
            PossStage("interface poss cams 01", _("Наконец-то, у меня есть свой собственный сайт, где транслируется изображение с камеры из гостиной! Теперь нужно увеличить аудиторию, ведь чем больше людей, тем больше доход от рекламных баннеров. Сделать это можно с помощью вложений в рекламу своего сайта. Кроме того, если в кадре происходит что-то интересное, аудитория также растёт."),
                      _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной «возможности» в текущей версии игры.{/i}")),
    ]),
    "seduction" : Poss(_("Наставник"), [
            PossStage("", _("Кажется, Лиза совсем ничего не знает о мальчиках. Возможно, она даже порно ни разу не видела, раз так удивилась обычному утреннему стояку. Может быть, стоит заняться просветительской деятельностью среди своей младшей сестрёнки? Но с чего начать? Поговорить?")),
            PossStage("", _("Я поговорил с Лизой и стало ясно, что для того, чтобы чему-то учить, нужно сначала завоевать авторитет."),),
            #PossStage("", _(""), _("")),
            #PossStage("", _(""), _("")),
    ]),
    "secretbook" : Poss(_("Особые книги"), [
            PossStage("", _("Алиса читает какие-то книги, но не хочет говорить о них. На порно журналы не похоже... Что же ещё там может быть? Нужно попытаться выяснить это как можно скорее... Любопытно же!")),
            PossStage("", _("Я нашёл какую-то книгу, но из названия ничего не понятно, а читать саму книгу ни времени, ни желания нет. Может быть, поискать о ней информацию в интернете?")),
            PossStage("", _("Вот это да! Я был не так далёк от истины. Конечно, это не порно, но уж точно эротика, да ещё какая! Видимо, Алисе нравятся любовные романы с эротическими оттенками, так сказать. Может быть, стоит ей подарить подобную книгу и посмотреть на её реакцию?")),
            PossStage("", _("Судя по реакции Алисы, подарок ей понравился. Видимо, стоит периодически заходить в книжный интернет-магазин и смотреть новинки. Возможно, таким образом удастся чуть-чуть улучшить отношения с Алисой."),
                      _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной «возможности» в текущей версии игры.{/i}")),
    ]),
    "Schoolmate" : Poss(_("Одноклассник"), [
            PossStage("", _("Очевидно, Лиза по уши влюблена в какого-то своего одноклассника по имени Алекс. Как она рассказала, у него есть подруга Оливия, самая красивая девочка в школе. Лиза ждёт от меня помощи в виде совета - как ей быть дальше.\n\nВ голову приходит сразу три варианта: предложить ей забыть об этом парне, предложить ей сражаться с Оливией за Алекса до конца или же помочь переключить внимание Оливии на кого-то другого..."),
                      _("Да, и похоже о своём мальчике Лиза разговаривает только, когда у неё хорошее настроение...")),
            PossStage("", _("Я предложил Лизе забыть о её парне и, похоже, она прислушалась к моему совету. Конечно, она расстроилась, но может быть это и к лучшему? Возможно, она сосредоточит своё внимание на ком-то, кто всегда рядом?")),
            PossStage("", _("Я убедил Лизу, что нужно бороться за своё счастье. Осталось только разработать план и достичь поставленной цели!")),
            PossStage("", _("Я разработал хитрый план, который сделает всех счастливыми: Лиза должна подужиться с Оливией, стать её лучшей подругой, познакомить её со мной, а я её соблазню... Ну, попытаюсь. Но если получится, то у меня будет девушка, а у Лизы её Алекс. Отличный план! Вот только как соблазняют самых красивых девочек школы?")),
    ]),
    "Blog" : Poss(_("Блог"), [
            PossStage("", _("Алиса рассказала о своём блоге и о своей проблеме, связанной с потерей вещей во время переезда. Теперь ей нечего показывать, не в чем вести блог и, вообще, она в печали. Кажется, она согласна на любую помощь и идеи, даже от меня! Может быть, посидеть в интернете, поискать какое-то решение?")),
            PossStage("", _("В результате поисков информации в интернете о том, чем могла бы заняться Алиса, удалось кое-что выяснить. Самыми популярными оказались блоги, где где ведущие - девушки. Причём, чем более откровенные наряды и чем больше грудь, тем более популярны шоу. С грудью, конечно, ничего не поделать, а вот наряды... Может быть, поговорить с ней об этом?")),
            PossStage("", _("Я пообщался с Алисой насчёт своих выводов о популярности блога и намекнул, что можно рекламировать не только крема и лаки, но и нижнее бельё, например. Удивительно, но Алиса согласилась. Правда, теперь мне нужно найти нижнее бельё для того, чтобы она заинтересовала свою аудиторию и привлекла внимание рекламодателей...")),
            PossStage("", _("Я подарил Алисе симпатичный комплект нижнего белья. Ей очень понравилось. Она даже при мне его примерила! Правда, я почти ничего не увидел, но было волнующе... Что самое любопытное, она намекнула, что можно поискать и что-то более... сексуальное!")),
            PossStage("", _("Мой очередной подарок Алисе произвёл эффект, но не совсем тот, на который я расчитывал. Чёрное маленькое боди без верха не подойдёт для её блога... Однако, подойдёт для кого-то, но для кого она не сказала... Столько секретов..."),
                      _("Ах да! Алиса сообщила, что с нею связался какой-то рекламодатель, который будет высылать ей нижнее бельё и потом платить за это! Теперь я ей больше не нужен...")),
    ]),
    "Swimsuit" : Poss(_("Купальник"), [
            PossStage("interface poss swimsuit ep01", _("Я заметил, что Лиза всё время в одном и том же закрытом купальнике. Так же невозможно толком загореть? Она тоже так считает, но другого нет. Остальные пропали с другими вещами во время переезда. Может быть, удастся как-то ей помочь?")),
            PossStage("interface poss swimsuit ep01", _("Во время завтрака Лиза намекнула маме, что нужно бы купить во время шоппинга купальник, который не скрывает половину тела и в котором можно загорать...")),
            PossStage("interface poss swimsuit ep01", _("Выяснилось, что во время последнего шоппинга забыли купить Лизе купальник, о котором она просила. Теперь придётся ждать до следующих выходных, когда Эрик снова повезёт всех за покупками. Но в этот раз сам Эрик пообещал ей подарить этот купальник. Может быть, его опередить?")),
            PossStage("interface poss swimsuit ep01", _("Мне удалось накопить немного денег и купить тот самый купальник, который так хотела Лиза. Кажется, она меня любит! А Эрик теперь обломается со своими подарками, ведь я уже подарил то, что так хочет младшая сестрёнка!"), _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной «возможности» в текущей версии игры. Продолжение следует...{/i}")),
            PossStage("interface poss swimsuit ep01", _("Мне не удалось купить и подарить Лизе купальник до того, как это сделал для неё Эрик. Кажется, их отношения улучшились. Вот если бы я подарил тот чёртов купальник, то Лиза была бы мне очень благодарна, а не ему..."), _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной «возможности» в текущей версии игры. Продолжение следует...{/i}")),
    ]),
}

# Диалоги
default talks = {
    "blog1"     : TalkTheme("alice", _("Значит, у тебя есть блог?"), "talkblog1", "talk_var[\"blog\"]==1"),
    "blog2"     : TalkTheme("alice", _("Насчёт блога..."), "talkblog2", "talk_var[\"blog\"]==3"),
    "lisa_fd"   : TalkTheme("lisa", _("О школе..."), "about_school", "day==1 and tm>=\"16:00\" and talk_var[\"lisa_fd\"]==0 and talk_var[\"boy\"]==0"),
    "lisa_swim" : TalkTheme("lisa", _("А ты чего так загораешь?"), "talk_swim",
                    "possibility[\"Swimsuit\"].stage_number < 0 and GetScheduleRecord(schedule_lisa, day, tm).label == \"lisa_sun\""),
    "lisas_boy" : TalkTheme("lisa", _("Насчёт твоего парня..."), "about_boy", "talk_var[\"boy\"]==1"),
    "lisa_dw" : TalkTheme("lisa", _("Насчёт посуды..."), "wash_dishes_lisa", "talk_var[\"lisa_dw\"]==0 and GetScheduleRecord(schedule_lisa, day, tm).label == \"lisa_dishes\""),
    "alice_dw" : TalkTheme("alice", _("Насчёт посуды..."), "wash_dishes_alice", "talk_var[\"alice_dw\"]==0 and GetScheduleRecord(schedule_alice, day, tm).label == \"alice_dishes\""),
    #"" : TalkTheme("", _(""), "", ""),
}

# Переменные влияющие на запуск диалогов
default talk_var = {
    "blog" : 0,
    "boy" : 0,
    "lisa_fd": 0,
    "ask_money": 0,
    "lisa_dw": 0,
    "alice_dw": 0,
}


default cooldown = {
    "learn" : "0 00:00",
}
