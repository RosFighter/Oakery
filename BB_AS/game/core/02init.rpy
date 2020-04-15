init 9999 python:
    renpy.config.rollback_enabled = True
    renpy.config.hard_rollback_limit = 64
    renpy.config.rollback_length = 64

define lime   = "#00FF00"
define red    = "#FF0000"
define orange = "#E59400"
define gray   = "#808080"

default failed = _("{color=#E59400}{i}Убеждение не удалось!{/i}{/color}\n")
default succes = _("{color=#00FF00}{i}Убеждение удалось!{/i}{/color}\n")

default undetect = _("{color=#00FF00}{i}Вы остались незамеченным!{/i}{/color}\n")
default spotted  = _("{color=#E59400}{i}Вас заметили!{/i}{/color}\n")

default alice_good_mass = _("{color=[lime]}{i}Алисе понравился массаж!{/i}{/color}\n")
default alice_bad_mass = _("{color=[orange]}{i}Алисе не понравился массаж!{/i}{/color}\n")

define config.has_autosave = False
define config.has_quicksave = False

define config.autosave_slots = 30
define config.quicksave_slots = 30
define config.autosave_on_quit = False
default persistent.grid_vbox = "grid"
default persistent.orint = False
default number_autosave = 0
default number_quicksave = 0

define weekdays = (
                  (_("ВС"), _("ВОСКРЕСЕНЬЕ")),
                  (_("ПН"), _("ПОНЕДЕЛЬНИК")),
                  (_("ВТ"), _("ВТОРНИК")),
                  (_("СР"), _("СРЕДА")),
                  (_("ЧТ"), _("ЧЕТВЕРГ")),
                  (_("ПТ"), _("ПЯТНИЦА")),
                  (_("СБ"), _("СУББОТА"))
                  )
define notify_list = []

init:
    $ config.keymap['hide_windows'].append('`')
################################################################################

## Меню помощи
define helps = [
    Helper(_("Управление"), _("Управление"), _("В данной игре предусмотрено управление с помощью клавиатуры. Вы можете сохраняться в любой момент. Быстрые клавиши по-умолчанию:\nF5 - сохранить, F8 - загрузить.\n\n\nКроме того, во время диалогов работают клавиши 1... 9 для различных вариантов ответов. Если вариант всего один, можно нажимать клавишу [[Space].\n\n\nДля переключения между комнатами можно воспользоваться клавишами 1... 7.\n\n\nОтключить интерфейс можно клавишами [[ ` ], [[ h ] или нажав среднюю клавишу мыши.\nЭто очень удобно, если область диалогов скрывает интересную часть изображения...")),
    Helper(_("Возможности"), _("Возможности"), _("В процессе игры, во время диалогов и других действий, вы можете открыть для себя новые \"возможности\". Их механика немного похожа на \"задания\" или \"квесты\" из других игр, но есть некоторые отличия.\n\n\n\"Возможности\" могут открывать доступ к скрытым событиям или покупкам в интернет-магазине, к новым опциям в ноутбуке или действиям в некоторых комнатах. Читайте внимательно описание каждой \"возможности\" и вы ничего не упустите!")),
    Helper(_("Настроение"), _("Настроение"), _("Различные действия или фразы, сказанные Максом, могут вызывать соответствующую реакцию в виде смены настроения персонажа.\n\n\nЕсли у персонажа плохое настроение, он может отказаться с вами обсуждать некоторые темы.\n\n\nПостепенно, каждый час, настроение плавно стремится к нейтральному состоянию. Однако, если настроение очень плохое, оно будет долго восстанавливаться.\n\n\nЧтобы поднять настроение, можно подарить то, что нужно именно этому персонажу или же просто извиниться. А иногда и правильное слово во время разговора может значительно улучшить настроение.")),
    Helper(_("Шоу"), _("Шоу"), _("Скрытые камеры могут быть основным источником дохода. Чем больше аудитория, тем больше людей, готовых платить за просмотр.\n\n\nУвеличить аудиторию можно с помощью рекламы. Если на камерах не происходит ничего интересного - аудитория падает. Если в кадр попадают пикантные моменты, аудитория растёт.\n\n\nЕсли у вас есть сайт, вы можете зарабатывать на рекламных баннерах. Поэтому, чем больше аудитория, тем больше у вас денег.\n\n\n{i}{b}Внимание:{/b} В следующих версиях игры появятся VIP-пользователи с особыми просьбами. Если вы будете их выполнять, получите солидную прибавку к доходу.{/i}")),
]

# Диалоги
define talks = {
    "blog1"      : TalkTheme("alice", _("Значит, у тебя есть блог?"), "talkblog1", "talk_var['blog']==1", -1),
    "blog2"      : TalkTheme("alice", _("Насчёт блога..."), "talkblog2", "talk_var['blog']==3", 1),
    "lisa_fd"    : TalkTheme("lisa", _("О школе..."), "about_school", "day==1 and tm>=\"16:00\" and talk_var[\"lisa_fd\"]==0 and talk_var['boy']==0"),
    "lisa_swim"  : TalkTheme("lisa", _("А ты чего так загораешь?"), "talk_swim", "poss['Swimsuit'].stn < 0 and GetPlan(plan_lisa, day, tm).name == 'sun'"),
    "lisas_boy"  : TalkTheme("lisa", _("Насчёт твоего парня..."), "about_boy", "talk_var['boy']==1", 0, "lisa_boy"),
    "lisas_boy2" : TalkTheme("lisa", _("Насчёт твоего парня..."), "about_boy2", "2 < talk_var['boy'] < 6", 1),
    "lisa_dw"    : TalkTheme("lisa", _("Насчёт посуды..."), "wash_dishes_lisa", "talk_var['lisa_dw']==0 and GetPlan(plan_lisa, day, tm).name == 'dishes'", -1),
    "alice_dw"   : TalkTheme("alice", _("Насчёт посуды..."), "wash_dishes_alice", "talk_var['alice_dw']==0 and GetPlan(plan_alice, day, tm).name == 'dishes'", -1),
    "ask_money"  : TalkTheme("ann", _("Мам, дай денег, пожалуйста..."), "ann_ask_money", "talk_var['ask_money']==0"),
    "aboutfood"  : TalkTheme("ann", _("Я продукты заказал!"), "ann_aboutfood", "dcv['buyfood'].stage==2 and dcv['buyfood'].lost==2"),
    "aboutpool"  : TalkTheme("ann", _("Мам, бассейн чист!"), "ann_aboutpool", "dcv['clearpool'].stage==2 and not dcv['clearpool'].done"),
    "ann_tv"     : TalkTheme("ann", _("Что смотришь?"), "ann_talk_tv", "talk_var['ann_tv']==0 and GetPlan(plan_ann, day, tm).name == 'tv'"),
    "alice_tv"   : TalkTheme("alice", _("Не возражаешь против компании?"), "alice_talk_tv", "talk_var['alice_tv']==0 and GetPlan(plan_alice, day, tm).name == 'tv'"),
    "aboutbooks" : TalkTheme("alice", _("Что читаешь?"), "alice_aboutbooks", "GetPlan(plan_alice, day, tm).name == \"read\" and poss['secretbook'].stn < 0"),
    "ann_mw"     : TalkTheme("ann", _("Насчёт случая с Лизой..."), "Ann_MorningWood", "flags['morning_erect'] == 1"),
    "lisa_mw"    : TalkTheme("lisa", _("Насчёт этого случая утром..."), "Lisa_MorningWood", "poss['seduction'].stn == 0", 0, "talkcooldown"),
    "lisa_sg1"   : TalkTheme("lisa", _("Насчёт успеваемости..."), "Lisa_sg1", "poss['sg'].stn == 0"),
    "lisa_sg2"   : TalkTheme("lisa", _("Ну как, ты подумала о моих условиях?"), "Lisa_sg2", "poss['sg'].stn == 1 and talk_var['lisa.pun'] > 0"),
    "lisa_hw"    : TalkTheme("lisa", _("Помочь с уроками?"), "Lisa_HomeWork", "poss['sg'].stn > 1 and not flags['lisa_hw'] and GetPlan(plan_lisa, day, tm).name == 'homework'"),
    "lisa_peep"  : TalkTheme("lisa", _("Хотел извиниться за утренний инцидент..."), "Lisa_sorry", "peeping['lisa_shower']==3"),
    "alice_peep" : TalkTheme("alice", _("Хотел извиниться за утренний инцидент..."), "Alice_sorry", "peeping['alice_shower']==3"),
    "alice_sol"  : TalkTheme("alice", _("Загораешь?"), "Alice_solar", "talk_var['alice_sun']==0 and (talk_var['sun_oiled']==0 or talk_var['sun_oiled']==3)and GetPlan(plan_alice, day, tm).name == 'sun'"),
    "lisa_gift"  : TalkTheme("lisa", _("У меня для тебя обещанная вкусняшка!"), "lisa_sorry_gifts", "sorry_gifts['lisa'].owe and there_in_stock('lisa') and GetPlan(plan_lisa, day, tm).name in ['sun', 'read', 'phone']"),
    "alice_gift" : TalkTheme("alice", _("У меня для тебя обещанная вкусняшка!"), "alice_sorry_gifts", "sorry_gifts['alice'].owe and there_in_stock('alice') and GetPlan(plan_alice, day, tm).name in ['sun', 'read', 'resting', 'blog']"),
    }

# Категории магазина
define ShopCat = {
    0 : _("Одежда"),
    1 : _("Книги"),
    2 : _("Продукты"),
    3 : _("Электроника"),
    4 : _("Товары 18+"),
    5 : _("Косметика"),
    6 : _("Украшения"),
    7 : _("Другое"),
    }

define gifts = {
    "lisa"  : [
        Gift("bikini", _("А у меня есть то, о чём ты мечтала..."), "gift_swimsuit"),
        Gift("bathrobe", _("У меня для тебя подарок {i}(Халат){/i}"), "gift_bathrobe", -1, "GetPlan(plan_lisa, day, tm).name in ['sun', 'read', 'phone']"),
        ],
    "alice" : [
        Gift("cigarettes", _("У меня есть кое-что запрещённое..."), "gift_cigarettes", -1),
        Gift("dress", _("Угадай: маленькое, чёрненькое..."), "gift_dress", -2),
        Gift("erobook_1", _("У меня для тебя одна книжка..."), "gift_book", -1),
        Gift("erobook_2", _("У меня снова для тебя книжка..."), "gift_book", -1),
        Gift("erobook_3", _("И снова у меня для тебя книжка..."), "gift_book", -1),
        Gift("erobook_4", _("И снова у меня для тебя книжка..."), "gift_book", -1),
        Gift("erobook_5", _("У меня снова для тебя книжка..."), "gift_book", -1),
        Gift("pajamas", _("У меня для тебя подарок {i}(Пижама){/i}"), "gift_pajamas", -1, "GetPlan(plan_alice, day, tm).name in ['sun', 'read', 'resting', 'blog']"),
        # Gift("", _(""), ""),
        ],
    "ann"   : [
        # Gift("cosmatic1", _("У меня для тебя подарок {i}(Косметика){/i}"), "gift_cosmatics"),
        # Gift("cosmatic2", _("У меня для тебя подарок {i}(Косметика){/i}"), "gift_cosmatics"),
        # Gift("cosmatic3", _("У меня для тебя подарок {i}(Косметика){/i}"), "gift_cosmatics"),
        # Gift("nightie", _("У меня для тебя подарок {i}(Ночнушка){/i}"), "gift_nightie"),
        ],
    }
