init 9999 python:
    renpy.config.rollback_enabled = True
    renpy.config.hard_rollback_limit = 50
    renpy.config.rollback_length = 50

init python:
    config.statement_callbacks.remove(_window_auto_callback)
    renpy.game.preferences.show_empty_window = False

define lime   = "#00FF00"
define red    = "#FF0000"
define orange = "#FFBE00"
define gray   = "#808080"

# define config.gl2 = True
define dop = namedtuple('dop', 'day tm ctm ll ul ddop')

default succes          = _("{color=#00FF00}{i}Убеждение удалось!{/i}{/color}\n")
default undetect        = _("{color=#00FF00}{i}Вы остались незамеченным!{/i}{/color}\n")
default succes_hide     = _("{color=#00FF00}{i}Получилось!{/i}{/color}\n")
default restrain        = _("{color=#00FF00}{i}Удалось сдержаться{/i}{/color}\n")
default like            = _("{color=#00FF00}{i}Ей нравится!{/i}{/color}\n")
default lucky           = _("{color=#00FF00}{i}Повезло!{/i}{/color}\n")
default alice_good_mass = _("{color=#00FF00}{i}Алисе понравился массаж!{/i}{/color}\n")
default lisa_good_mass  = _("{color=#00FF00}{i}Лизе понравился массаж!{/i}{/color}\n")
default lisa_good_kiss  = _("{color=#00FF00}{i}Лизе понравился поцелуй!{/i}{/color}\n")
default ann_good_mass   = renpy.config.say_menu_text_filter(renpy.translate_string(_("{color=#00FF00}{i}Маме понравился массаж!{/i}{/color}\n")))

init 110:
    $ failed           = _("{color=#E59400}{i}Убеждение не удалось!{/i}{/color}\n")
    $ spotted          = _("{color=#E59400}{i}Вас заметили!{/i}{/color}\n")
    $ risky            = _("{color=#E59400}{i}Слишком рискованно!{/i}{/color}\n")
    $ failed_hide      = _("{color=#E59400}{i}Не получилось!{/i}{/color}\n")
    $ norestrain       = _("{color=#E59400}{i}Сдержаться не удалось{/i}{/color}\n")
    $ dont_like        = _("{color=#E59400}{i}Ей не нравится!{/i}{/color}\n")
    $ unlucky          = _("{color=#E59400}{i}Не повезло!{/i}{/color}\n")
    $ alice_bad_mass   = _("{color=#E59400}{i}Алисе не понравился массаж!{/i}{/color}\n")
    $ lisa_bad_mass    = _("{color=#E59400}{i}Лизе не понравился массаж!{/i}{/color}\n")
    $ lisa_bad_kiss    = _("{color=#E59400}{i}Лизе не понравился поцелуй!{/i}{/color}\n")
    $ impact_reduced   = _("{color=#FFBE00}{b}Внимание:{/b} Ваше влияние на присутствующих понизилось!{/color}\n")
    $ ann_bad_mass     = renpy.config.say_menu_text_filter(renpy.translate_string(_("{color=#E59400}{i}Маме не понравился массаж!{/i}{/color}\n")))

    $ renpy.music.register_channel('fg_music', mixer='music', loop=True)

define good_mission     = _("{color=#00FF00}{i}Успех!{/i}{/color}\n")
define bad_mission      = _("{color=#E59400}{i}Провал!{/i}{/color}\n")

define config.has_autosave = False
define config.has_quicksave = False

define config.autosave_slots = 30
define config.quicksave_slots = 30
define config.autosave_on_quit = False
default persistent.grid_vbox = 'grid'
default persistent.request_savename = True
default persistent.transparent_textbox = False
default persistent.all_opportunities = False
default persistent.skip_lisa_dressed = False
default persistent.use_cheats = False
default cheats_warning = False
default number_autosave = 0
default number_quicksave = 0
default number_save = 0
default last_save_name = "(None)"

define rl = create_random_list()
default rand_result = 0

# (для экрана сохранений андроид)
default day = 1
default tm  = '08:50'
default save_name = ''
default weekday = GetWeekday(day)

default morningwood_var = [1, 2, 3]

default persistent.memories = {}
default persistent.mems_var = []

default persistent.photos = {}
default expected_photo = []

default purchased_items = []
default var_pose = '02'
default var_pose2 = '01'
default var_stage = '01'
default var_cum = ''
default var_dress = ''
default var_dress2 = ''
default var_film = ''

define cam_flag = []
define cam_list = []
define cheat_skip = False
define skip_error = False
default skiped = []

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

define cloth = None

define events_by_tm = Events_by_time()

default cam_poses = {}
default cam_pose_blog = []
default cur_ch = 'max'
default current_language_list = []
default stockings = False
default menu_starting = False
default kt6_first = False

init:
    $ config.keymap['hide_windows'].append('`')
    if renpy.variant("touch") or renpy.variant("small"):
        $ config.mouse = None
    elif (renpy.game.preferences.physical_size is not None
            and renpy.game.preferences.physical_size[1] < 900):
        $ config.mouse = {
            'default': [('images/interface/cursors/arrow-64.png', 0, 0)],
            'find' : [('images/interface/cursors/find-64.webp', 27, 27)],
            'talk' : [('images/interface/cursors/talk-64.webp', 11, 50)],
            'palms': [('images/interface/cursors/palms-64.webp', 37, 32)],
            }
    else:
        $ config.mouse = {
            'default': [('images/interface/cursors/arrow-80.png', 0, 0)],
            'find' : [('images/interface/cursors/find-80.webp', 33, 33)],
            'talk' : [('images/interface/cursors/talk-80.webp', 14, 61)],
            'palms': [('images/interface/cursors/palms-80.webp', 46, 40)],
            }

define random_choice = renpy.random.choice
define random_randint = renpy.random.randint

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
    'blog1'         : TalkTheme('alice', _("Значит, у тебя есть блог?"), 'talkblog1', "alice.flags.crush==1", -1),
    'blog2'         : TalkTheme('alice', _("Слушай, насчёт блога..."), 'talkblog2', "poss['blog'].st()==1", 1),
    'blog3'         : TalkTheme('alice', _("Насчёт твоего блога... А если не особо раздеваться?"), 'talkblog3', "all([alice.dcv.feature.done, alice.stat.mast, poss['blog'].st() in [2,3]])", 1),
    'alice_dw'      : TalkTheme('alice', _("Насчёт посуды..."), 'wash_dishes_alice', "not alice.daily.dishes and alice.plan_name == 'dishes'", -2),
    'alice_tv'      : TalkTheme('alice', _("Не возражаешь против компании?"), 'alice_talk_tv', "all([not alice.daily.tvwatch, alice.plan_name == 'tv', alice.dcv.mistress.done or not alice.dcv.mistress.stage, alice.daily.mistress < 2])"),
    'aboutbooks'    : TalkTheme('alice', _("Что читаешь?"), 'alice_aboutbooks', "alice.plan_name == 'read' and not poss['secretbook'].used(0)"),
    # 'alice_peep'    : TalkTheme('alice', _("Хотел извиниться за утренний инцидент..."), 'Alice_sorry', "all([alice.daily.shower==3, alice.dcv.shower.done, not (alice.flags.touched and len(alice.sorry.give)>3)])"),
    'alice_peep'    : TalkTheme('alice', _("Хотел извиниться за утренний инцидент..."), 'Alice_sorry', "all([alice.daily.shower==3, alice.dcv.shower.done, poss['risk'].st()<11])"),
    'alice_peep1'   : TalkTheme('alice', _("Извини, но я случайно увидел, как ты принимаешь душ..."), 'Alice_sorry', "all([alice.daily.shower==3, alice.dcv.shower.done, poss['risk'].st()==12])"),
    'alice_peep2'   : TalkTheme('alice', _("Хочу извиниться. Я бессовестно подглядывал за тобой утром..."), 'Alice_sorry', "all([alice.daily.shower==3, alice.dcv.shower.done, poss['risk'].st()==14])"),
    'alice_sol'     : TalkTheme('alice', _("Загораешь?"), 'Alice_solar', "all([not alice.hourly.sun_cream, any([not alice.daily.oiled, alice.daily.oiled==3]), alice.plan_name == 'sun'])"),
    'alice_gift'    : TalkTheme('alice', _("У меня для тебя обещанная вкусняшка!"), 'alice_sorry_gifts', "all([len(alice.sorry.give)<3, alice.sorry.owe, alice.sorry.there_in_stock(), alice.plan_name in ['sun', 'read', 'resting', 'blog'], alice.daily.oiled != 2])"),
    'alice_gift2'   : TalkTheme('alice', _("У меня для тебя обещанная вкусняшка!"), 'alice_gift_sweets', "all([len(alice.sorry.give)>2, alice.sorry.owe, alice.sorry.there_in_stock(), alice.plan_name in ['sun', 'read', 'resting', 'blog'], (alice.daily.oiled!=2 or alice.flags.touched)])"),
    'aboutbath'     : TalkTheme('alice', _("Насчёт ванны ночью..."), 'alice_about_bath', "alice.flags.incident in [1, 3]"),
    'alice.kiss'    : TalkTheme('alice', _("А ты умеешь целоваться?"), 'alice_about_kiss', "all([lisa.dcv.seduce.stage==1, 'alice' not in flags.how_to_kiss])"),
    'eric.ling0'    : TalkTheme('alice', _("Я слышал, Эрик тебе новое бельё собирается купить?"), 'alice_about_lingerie0', "get_stage_sexbody2()==3"),
    'eric.ling1'    : TalkTheme('alice', _("Покажешь боди, которое тебе Эрик купит?"), 'alice_showing_lingerie1', "all([get_stage_sexbody2()==4, current_room==house[1]])"),
    'a.privpun0'    : TalkTheme('alice', _("Хотел узнать, хорошо ли тебе сидится?"), 'alice_about_defend_punish0', "all([alice.dcv.private.enabled, alice.dcv.private.stage==0, alice.dcv.private.lost>1])"),
    'a.privpun1'    : TalkTheme('alice', _("Не слабо тебя отшлёпали!"), 'alice_about_defend_punish1', "all([alice.dcv.private.stage==2, alice.dcv.private.lost>1])"),
    'a.privpun2'    : TalkTheme('alice', _("Ты не передумала о наказаниях?"), 'alice_about_defend_punish1.cont', "all([alice.dcv.private.stage==3, alice.dcv.private.lost>1])"),
    'a.privpunt'    : TalkTheme('alice', _("Отшлёпать тебя сейчас или..."), 'alice_about_private_punish', "all([not alice.flags.private, alice.dcv.private.stage==4, alice.dcv.private.lost>1])"),
    'a.privpun'     : TalkTheme('alice', _("Пора отшлёпать одну милую попку!"), 'alice_private_punish_0', "all([alice.plan_name in ['sun', 'smoke'], alice.flags.private, alice.dcv.private.stage==4, not alice.dcv.private.done, not alice.spanked])"),
    'a.privpunr'    : TalkTheme('alice', _("Пора отшлёпать одну милую попку!"), 'alice_private_punish_r', "all([alice.plan_name == 'sun', alice.dcv.private.stage==5, not alice.dcv.private.done, not alice.spanked])"),
    'a.carry'       : TalkTheme('alice', _("Тебе помочь накрыть на стол?"), 'alice_help_carry_plates', "all([alice.plan_name == 'cooking', alice.dcv.battle.stage])"),
    'a.wallet'      : TalkTheme('alice', "Э-э-э... Что не интересно?", 'alice_about_wallet', "all([flags.eric_wallet == 2, not alice.flags.talkblock])"),
    'a.showdown'    : TalkTheme('alice', _("Как ты после случившегося?"), 'alice_about_showdown', "all([flags.eric_wallet==4, not alice.flags.showdown_e])"),

    'a.domine0'     : TalkTheme('alice', _("Я пришёл извиниться за то, что было утром. Я больше не буду."), 'alice_mistress_0', "all([not alice.dcv.mistress.stage, alice.plan_name == 'tv', not alice.dcv.mistress.done, not alice.daily.mistress])"),
    'a.domine1'     : TalkTheme('alice', _("Я снова подглядывал. Извини."), 'alice_mistress_1', "all([alice.dcv.mistress.stage == 1, alice.plan_name == 'tv', not alice.dcv.mistress.done, not alice.daily.mistress])"),
    'a.domine2'     : TalkTheme('alice', _("Ну давай, можешь меня наказывать..."), 'alice_mistress_2', "all([alice.dcv.mistress.stage == 2, alice.plan_name == 'tv', not alice.dcv.mistress.done, not alice.daily.mistress])"),
    'a.domine3'     : TalkTheme('alice', _("Я выбираю наказание от тебя..."), 'alice_mistress_3', "all([alice.dcv.mistress.stage > 2, alice.plan_name == 'tv', not alice.dcv.mistress.done, not alice.daily.mistress])"),

    'ask_money'     : TalkTheme('ann', _("Мам, дай денег, пожалуйста..."), 'ann_ask_money', "all([ann.daily.ask_money==0, not flags.about_earn])"),
    'aboutfood'     : TalkTheme('ann', _("Я продукты заказал!"), 'ann_aboutfood', "dcv.buyfood.stage==2 and not dcv.buyfood.done"),
    'aboutpool'     : TalkTheme('ann', _("Мам, бассейн чист!"), 'ann_aboutpool', "dcv.clearpool.stage==2 and dcv.clearpool.lost>3"),
    'ann_tv'        : TalkTheme('ann', _("Что смотришь?"), 'ann_talk_tv', "not ann.daily.tvwatch and ann.plan_name == 'tv'"),
    'ann_mw'        : TalkTheme('ann', _("Насчёт случая с Лизой..."), 'Ann_MorningWood', "dcv.mw.stage == 1"),
    'ann.kiss'      : TalkTheme('ann', _("Мам, а как учатся целоваться?"), 'ann_about_kiss', "all([lisa.dcv.seduce.stage==1, 'ann' not in flags.how_to_kiss])"),
    'ann.secr1'     : TalkTheme('ann', _("Мам, Кира отправила меня к тебе..."), 'ann_about_ann_secret1', "ann.dcv.feature.stage==1"),
    'ann.yoga0'     : TalkTheme('ann', _("С тобой можно?"), 'ann_yoga_with_max0', "all([ann.plan_name=='yoga', ann.dcv.feature.stage==4, ann.dcv.feature.done])"),
    'ann.yoga1'     : TalkTheme('ann', _("Я присоединюсь?"), 'ann_yoga_with_maxr', "all([ann.plan_name=='yoga', ann.dcv.feature.stage>4, ann.dcv.feature.done, ann.dcv.seduce.done])"),
    'm.wallet'      : TalkTheme('ann', "Да не крал я у него ничего! Он всех обманывает!", 'ann_about_wallet', "all([flags.eric_wallet == 2, not ann.flags.talkblock])"),
    'm.olivia.0'    : TalkTheme('ann', _("Мам, нужно поговорить об Оливии."), 'ann_about_olivia0', "all([olivia.flags.incident > 1, lisa.flags.showdown_e == 3, ann.plan_name != 'yoga'])"),     # девчонки хотя бы раз намазывались кремом
    'm.olivia.1'    : TalkTheme('ann', _("Мам, ты подумала об Оливии?"), 'ann_about_olivia1', "all([lisa.flags.showdown_e == 4, ann.dcv.special.done, ann.plan_name != 'yoga'])"),     # первая попытка убедить Анну провалилась

    'eric.money'    : TalkTheme('eric', _("Мне нужны деньги..."), 'eric_needmoney', "all([not eric.daily.ask_money, get_rel_eric()[0] > 0, 'money' in flags.bonus_from_eric])"),
    'eric.wtf'      : TalkTheme('eric', _("Эрик, мы же договорились!"), 'eric_voy_wtf', "all([flags.voy_stage == 1, get_rel_eric()[0] > 0])"),
    # 'eric.kira0'    : TalkTheme('eric', _("Хочу рассказать тебе кое-что о Кире..."), 'Eric_talk_about_Kira_0', "all([wcv.catch_Kira.enabled, not wcv.catch_Kira.done, wcv.catch_Kira.stage < 1, ger_rel_eric()[0] == 3])"),
    'eric.kira1'    : TalkTheme('eric', _("Я хотел поговорить о Кире..."), 'Eric_talk_about_Kira_1', "all([wcv.catch_Kira.stage==1, kira.dcv.battle.stage>0])"),

#====================
    'eric.lisa.b_0' : TalkTheme('eric', _("Мою премию за помощь с Лизой!"), 'Eric_bonus_for_Lisa', "all([flags.voy_stage == 8, get_rel_eric()[0] == 3, not kira.dcv.battle.stage, all([lisa.dcv.battle.stage, alice.dcv.battle.stage])])"),
    'eric.stocking' : TalkTheme('eric', _("Чтобы на маме были не только очки для сна, но и чулки!"), 'Eric_ask_stockings', "all([flags.can_ask in [1, 2], not eric.daily.blog_we, get_rel_eric()[0] == 3, alice.dcv.intrusion.stage > 6])"),
    'eric.no_stock' : TalkTheme('eric', _("Чтобы на маме были только очки для сна!"), 'Eric_ask_no_stockings', "all([flags.can_ask == 3, not eric.daily.blog_we, get_rel_eric()[0] == 3, alice.dcv.intrusion.stage > 6])"),
#====================

    'eric.tribute'  : TalkTheme('eric', _("Вот деньги, чтобы ты не лез к Лизе..."), 'Eric_tribute', "all([eric_obligation.volume, not eric_obligation.paid, mgg.money >= eric_obligation.get_debt(), not flags.eric_wallet])"),
    'eric.nomoney'  : TalkTheme('eric', _("У меня нет денег, чтобы ты не лез к Лизе."), 'Eric_tribute_no_money', "all([eric_obligation.volume, not eric_obligation.paid, mgg.money < eric_obligation.get_debt(), not flags.eric_wallet])"),

    'kt1'           : TalkTheme('kira', _("Да тут всегда хорошая погода..."), 'kira_firsttalk', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==0])"),
    'kt2'           : TalkTheme('kira', _("Ага, как всегда..."), 'kira_talk2', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==1])"),
    'kt3'           : TalkTheme('kira', _("Да, шикарная!"), 'kira_talk3', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==2])"),
    'kira.kiss'     : TalkTheme('kira', _("Кира, мне нужно научиться целоваться..."), 'kira_about_kiss', "all([kira.dcv.feature.stage>2, lisa.dcv.seduce.stage==1, list_in_list(['ann', 'alice'], flags.how_to_kiss), 'kira' not in flags.how_to_kiss])"),
    'kt4'           : TalkTheme('kira', _("Ну как, ты с мамой-то поговорила?"), 'kira_talk4', "all([kira.stat.blowjob, kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==3])"),
    'kt5'           : TalkTheme('kira', _("Как отдыхается, тётя Кира?"), 'kira_talk5', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==4])"),

    'kt6'           : TalkTheme('kira', _("Насчёт фотосессии..."), 'kira_talk6', "all([not kt6_first, kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==5, (not items['photocamera'].have and not items['nightie2'].have) or (items['photocamera'].have and items['nightie2'].have)])"),
    'kt6_2'         : TalkTheme('kira', _("Насчёт фотосессии..."), 'kira_talk6', "all([kt6_first==1, kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==5, items['photocamera'].have, items['nightie2'].have])"),
    'kt6_3'         : TalkTheme('kira', _("Насчёт фотосессии..."), 'kira_talk6', "all([kt6_first==2, weekday==6, kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==5, items['photocamera'].have, items['nightie2'].have])"),

    'kt_ft1'        : TalkTheme('kira', _("Понравились фотографии?"), 'kira_about_photo1', "all([kira.dcv.feature.done, kira.dcv.feature.stage==6, kira.plan_name=='sun'])"),
    'kt_cuni'       : TalkTheme('kira', _("Не злишься на меня, тётя Кира?"), 'kira_about_cuni', "all([kira.dcv.sweets.done, kira.flags.promise, kira.plan_name=='sun'])"),
    'kt.ft2'        : TalkTheme('kira', _("Так когда будем снова фотографироваться, тётя Кира?"), 'kira_about_photo2', "all([kira.dcv.feature.stage==7, kira.plan_name=='sun', not expected_photo, kira.dcv.photo.stage==1, kira.dcv.photo.done, kira.dcv.feature.done])"),
    'ann.secr0'     : TalkTheme('kira', _("Тётя Кира, когда ты уже с мамой поговоришь?!"), 'kira_about_ann_secret0', "all([kira.plan_name=='sun', not ann.dcv.feature.stage, flags.lisa_sexed>=1, alice.dcv.intrusion.enabled, alice.dcv.intrusion.lost<3, kira.dcv.photo.stage>1])"),
    'ann.secr2'     : TalkTheme('kira', _("Я хотел спросить про тот случай из детства мамы..."), 'kira_about_ann_secret2', "all([kira.plan_name=='sun', ann.dcv.feature.stage==2, ann.dcv.feature.done])"),
    'ann.secr_r'    : TalkTheme('kira', _("Расскажи уже про тот случай из детства мамы..."), 'kira_about_ann_secret_r', "all([kira.plan_name=='sun', ann.dcv.feature.stage==3, ann.dcv.feature.done])"),
    'kt_ft3_0'      : TalkTheme('kira', _("Когда будет новая фотосессия, тётя Кира?"), 'kira_about_photo3_0', "all([kira.dcv.feature.stage==8, ann.dcv.feature.stage>3, kira.dcv.feature.done])"),
    'k.wallet'      : TalkTheme('kira', "Ты уже в курсе, что Эрик заявил?", 'kira_about_wallet', "all([flags.eric_wallet == 2, not kira.flags.talkblock])"),
    'k.showdown'    : TalkTheme('kira', _("Уже слышала новость, тётя Кира?"), 'kira_about_showdown', "all([flags.eric_wallet==4, not kira.flags.showdown_e])"),

    'lisa_fd'       : TalkTheme('lisa', _("О школе..."), 'about_school', "day==1 and tm>='16:00' and flags.lisa_fd==0 and lisa.flags.crush==0"),
    'lisa_swim'     : TalkTheme('lisa', _("А ты чего так загораешь?"), 'talk_swim', "poss['Swimsuit'].st()<0 and lisa.plan_name == 'sun'"),
    'lisas_boy'     : TalkTheme('lisa', _("Насчёт твоего парня..."), 'about_boy', "lisa.flags.crush==1", 0, "lisa_boy"),
    'lisas_boy2'    : TalkTheme('lisa', _("Насчёт твоего парня..."), 'about_boy2', "2 < lisa.flags.crush < 6", 1),
    'lisa_dw'       : TalkTheme('lisa', _("Насчёт посуды..."), 'wash_dishes_lisa', "not lisa.daily.dishes and lisa.plan_name == 'dishes'", -2),
    'lisa_mw'       : TalkTheme('lisa', _("Насчёт этого случая утром..."), 'Lisa_MorningWood', "poss['seduction'].st() == 0 and current_room==house[0]", 0, "talkcooldown"),
    'lisa_mw2'      : TalkTheme('lisa', _("Хотел поговорить о Большом Максе..."), 'Lisa_MorningWoodCont', "dcv.mw.stage==3 and current_room==house[0]"),
    'lisa_mw3'      : TalkTheme('lisa', _("А ты у нас шалунья, оказывается..."), 'Lisa_MorningWoodCont', "dcv.mw.stage==5 and current_room==house[0]"),
    'lisa_sg1'      : TalkTheme('lisa', _("Насчёт успеваемости..."), 'Lisa_sg1', "poss['sg'].st() == 0"),
    'lisa_hw'       : TalkTheme('lisa', _("Помочь с уроками?"), 'Lisa_HomeWork', "poss['sg'].st() > 1 and not lisa.daily.homework and lisa.plan_name == 'homework'"),
    'lisa_peep'     : TalkTheme('lisa', _("Хотел извиниться за утренний инцидент..."), 'Lisa_sorry', "lisa.daily.shower==3 and lisa.dcv.shower.done"),
    'lisa_gift'     : TalkTheme('lisa', _("У меня для тебя обещанная вкусняшка!"), 'lisa_sorry_gifts', "all([lisa.sorry.owe, lisa.sorry.there_in_stock(), lisa.plan_name in ['sun', 'read', 'phone']])"),
    'l.ab.sec1'     : TalkTheme('lisa', _("У тебя странный вид..."), 'liza_secret_alisa', "all([poss['nightclub'].st() < 5, 'dress' in alice.gifts, GetRelMax('lisa')[0]>2, lisa.GetMood()[0]>1, alice.dcv.feature.stage<1, alice.dcv.feature.done])"),
    'l.ab.sec2'     : TalkTheme('lisa', _("Может всё-таки поделишься своими переживаниями по поводу Алисы?"), 'liza_secret_alisa', "all([poss['nightclub'].st() < 5, 'dress' in alice.gifts, GetRelMax('lisa')[0]>2, lisa.GetMood()[0]>1, alice.dcv.feature.stage>0, alice.dcv.feature.done])"),
    'lisa.hand'     : TalkTheme('lisa', _("Массаж рук заказывала?"), 'liza_hand_mass', "weekday in [2, 5] and all([learned_hand_massage(), lisa.flags.handmass, not lisa.daily.massage, lisa.plan_name == 'phone'])"),
    'l.firstkiss'   : TalkTheme('lisa', _("Ну что, Лиза, готова?"), 'lisa_ment_kiss1', "all([GetRelMax('lisa')[0]>1, lisa.plan_name=='read', lisa.dcv.seduce.stage>3, 'lisa' not in flags.how_to_kiss])"),
    'l.nextkiss'    : TalkTheme('lisa', _("Ну что, готова?"), 'lisa_ment_kiss', "all([lisa.plan_name=='read', lisa.dcv.seduce.done, poss['seduction'].st()>8, flags.stopkiss<1, lisa.dcv.seduce.stage < 5])"),
    'l.sex-ed1'     : TalkTheme('lisa', _("Лиза, ты же любишь читать?"), 'lisa_sexbook1', "all([lisa.plan_name in ['sun', 'read', 'phone'], items['sex.ed'].have, poss['seduction'].st()<13])"),
    'l.sex-ed2'     : TalkTheme('lisa', _("Лиза, у меня для тебя особая книжка..."), 'lisa_sexbook2', "all([lisa.plan_name in ['sun', 'read', 'phone'], items['sex.ed'].have, poss['seduction'].st()>13])"),
    'l.ab_aeed0'    : TalkTheme('lisa', _("Рассказывай, что делали?"), 'lisa_about_ae_sexed0', "not flags.l_ab_sexed and flags.lisa_sexed==0"),
    'l.ab_aeed1'    : TalkTheme('lisa', _("Ну так и чему же тебя учили?"), 'lisa_about_ae_sexed1', "not flags.l_ab_sexed and flags.lisa_sexed==1"),
    'l.ab_aeed2'    : TalkTheme('lisa', _("Что новенького было на уроке?"), 'lisa_about_ae_sexed2', "not flags.l_ab_sexed and flags.lisa_sexed==2"),
    'l.ab_aeed3'    : TalkTheme('lisa', _("Что нового мама с Эриком тебе рассказали?"), 'lisa_about_ae_sexed3', "not flags.l_ab_sexed and flags.lisa_sexed==3"),
    'l.ab_aeed4'    : TalkTheme('lisa', _("Что нового узнала на уроке у мамы и Эрика?"), 'lisa_about_ae_sexed4', "not flags.l_ab_sexed and flags.lisa_sexed==4"),
    'l.stopkiss'    : TalkTheme('lisa', _("{i}урок поцелуев{/i}"), 'lisa_stop_kiss', "all([lisa.plan_name=='read', lisa.dcv.seduce.done, poss['seduction'].st()>7, flags.stopkiss==1])"),
    'lisas_boy3'    : TalkTheme('lisa', _("Насчёт Алекса..."), 'about_boy3', "all([GetRelMax('lisa')[0]>1, lisa.flags.crush==6, day>=10, lisa.dcv.feature.done])", 1),
    'l.olivia_1'    : TalkTheme('lisa', _("Есть успехи с Оливией?"), 'about_olivia_1', "all([lisa.flags.crush==7, lisa.dcv.feature.done, weekday!=0])", 1),
    'l.olivia_2'    : TalkTheme('lisa', _("Что-нибудь узнала про Оливию?"), 'about_olivia_2', "all([lisa.flags.crush==8, lisa.dcv.feature.done, weekday!=0])", 1),
    'l.olivia_3'    : TalkTheme('lisa', _("Ну так, что там с трусиками Оливии?"), 'about_olivia_3', "all([lisa.flags.crush==9, lisa.dcv.feature.done, weekday!=0])", 1),
    'l.olivia_4'    : TalkTheme('lisa', _("Ты позвала Оливию к нам?"), 'about_olivia_4', "all([lisa.flags.kiss_lesson, lisa.flags.crush==10, lisa.dcv.feature.done, weekday!=3])", 1),
    'l_ab_alex4'    : TalkTheme('lisa', _("Ну как, получилось рассказать всё Оливии?"), 'about_alex4', "all([lisa.flags.crush==15, weekday in [3, 4] or (weekday==2 and tm>'19:00')])"),
    'l.toples_0'    : TalkTheme('lisa', _("Нравится, что я спасаю твою попку от наказания?"), 'about_horror_toples', "all([tm<'23:00', lisa.flags.topless, lisa.flags.defend>4, not lisa.dcv.other.stage, lisa.dcv.other.lost])"),
    'ol.l.t1'       : TalkTheme(['lisa', 'olivia'], _("Учтите, я испытываю... некоторый подъём!"), 'olivia_talk1', "all([olivia.plan_name=='sun', not olivia.dcv.feature.stage, olivia.dcv.feature.done])"),
    'ol.l.t2'       : TalkTheme(['lisa', 'olivia'], _("Пошепчемся немного о моей сестрёнке?"), 'olivia_talk2', "all([olivia.plan_name=='sun', olivia.dcv.feature.stage==1, olivia.dcv.feature.done])"),
    'ol.l.t3'       : TalkTheme(['lisa', 'olivia'], _("Что новенького, Оливия?"), 'olivia_talk3', "all([olivia.plan_name=='sun', weekday==2, olivia.dcv.feature.stage==3, olivia.dcv.feature.done])"),
    'ol.l.t4'       : TalkTheme(['lisa', 'olivia'], _("Рад тебя видеть, Оливия!"), 'olivia_talk4', "all([olivia.plan_name=='sun', weekday in[2, 5], olivia.dcv.feature.stage==4, olivia.dcv.feature.done, olivia.dcv.special.stage])"),
    'l.take_school' : TalkTheme('lisa', _("Ну как, всё повторила? \n{i}(проводить Лизу в школу){/i}"), 'take_to_school', "all([lisa.flags.help, lisa.plan_name == 'repeats'])", 1),
    'l.wallet'      : TalkTheme('lisa', "Надеюсь, ты не поверила Эрику?", 'lisa_about_wallet', "all([flags.eric_wallet == 2, not lisa.flags.talkblock])"),
    'l.need_phone'  : TalkTheme('lisa', "Мне нужна твоя помощь!", 'lisa_asked_phone', "all([flags.eric_wallet == 2, lisa.flags.talkblock, not any([flags.asked_phone, flags.eric_photo2, lisa.hourly.talkblock, weekday in [4, 5]])])"),
    'l.showdown'    : TalkTheme('lisa', _("Лиза, ты чего нос повесила?"), 'lisa_about_showdown', "all([flags.eric_wallet==4, not lisa.flags.showdown_e])"),
    'l.olivia_6'    : TalkTheme('lisa', _("Мама разрешила!"), 'lisa_about_olivia_6', "lisa.flags.showdown_e == 5"),

    'l.cont_kiss0'  : TalkTheme('lisa', _("Кстати, а как тебе та книжка, которую я дарил?"), 'lisa_about_sex_book0', "all([lisa.plan_name == 'read', lisa.dcv.seduce.stage == 5, lisa.dcv.seduce.done])"),

    'l.read.w.mc'   : TalkTheme('lisa', _("Можно вместе с тобой книжку почитать?"), 'lisa_read_with_Max0', "all([lisa.plan_name == 'read', lisa.dcv.seduce.stage == 6, lisa.dcv.seduce.done, lisa.dcv.special.stage==7])"),
    'l.read.w.mc.r' : TalkTheme('lisa', _("Можно к тебе присоединиться?"), 'lisa_read_with_Max_r', "all([lisa.plan_name == 'read', lisa.dcv.seduce.stage > 7, lisa.dcv.seduce.done])"),

    'ol.l.sun_cr0'  : TalkTheme(['lisa', 'olivia'], _("А у меня есть крем для загара. Хотите?"), 'about_first_sunscreen', "all([olivia.plan_name=='sun', olivia.flags.incident==1])"),
    'ol.l.sun_cr1'  : TalkTheme(['lisa', 'olivia'], _("Давайте, я намажу вас кремом для загара?"), 'olivia_second_sunscreen', "all([olivia.plan_name=='sun', not olivia.daily.oiled, olivia.flags.incident==2])"),
    'ol.l.sun_cr2'  : TalkTheme(['lisa', 'olivia'], _("Давайте, я намажу вас кремом для загара?"), 'olivia_third_sunscreen',  "all([olivia.plan_name=='sun', not olivia.daily.oiled, olivia.flags.incident==3])"),
    'ol.l.sun_crR'  : TalkTheme(['lisa', 'olivia'], _("Давайте, я намажу вас кремом для загара?"), 'olivia_repeat_sunscreen',  "all([olivia.plan_name=='sun', not olivia.daily.oiled, olivia.flags.incident>3])"),
    'ol.l.sun_crG'  : TalkTheme(['lisa', 'olivia'], _("Вам дать крем для загара?"), 'olivia_give_sunscreen',  "all([olivia.plan_name=='sun', not olivia.daily.oiled, olivia.flags.incident>3, olivia.flags.handmass])"),

    # ====== 0.09.1 ===================
    'ann.drink1'    : TalkTheme('ann', _("Мам, поговорим?"), 's1_ann_talk_about_night', "ann.dcv.drink.stage==1"),
    'ann.drink2'    : TalkTheme('kira', _("Хотел поговорить о маме..."), 's1_kira_talk_about_ann_drink', "all([kira.plan_name=='sun', ann.dcv.drink.stage==2])"),
    'ann.intime0'   : TalkTheme('ann', _("Мам, ты подумала?"), 's1_about_intimate_lessons', "all([ann.dcv.private.stage == 1, ann.dcv.private.done])"),

    # ====== 0.09.2 ===================
    'a.havemoney'   : TalkTheme('alice', _("Я разжился деньгами! Идём за костюмом?"), 'ev_v92_002', "all([alice.flags.showdown_e == 2, flags.eric_wallet > 4])"),

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
    'lisa'  : [
        Gift('bikini', _("А у меня есть то, о чём ты мечтала..."), 'gift_swimsuit'),
        Gift('bathrobe', _("У меня для тебя подарок {i}(Халат){/i}"), 'gift_bathrobe', -1, "lisa.plan_name in ['sun', 'read', 'phone']"),
        Gift(['ritter-m', 'ritter-b'], _("У меня для тебя вкусняшка!"), 'lisa_gift_sweets', -1, "all(['bathrobe' in lisa.gifts, lisa.plan_name in ['sun', 'read', 'phone', 'repeats'], not lisa.daily.sweets])"),
        ],
    'alice' : [
        Gift('cigarettes', _("У меня есть кое-что запрещённое..."), 'gift_cigarettes', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('dress', _("Угадай: маленькое, чёрненькое..."), 'gift_dress', -2, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('erobook_1', _("У меня для тебя одна книжка..."), 'gift_book', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('erobook_2', _("У меня снова для тебя книжка..."), 'gift_book', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('erobook_3', _("И снова у меня для тебя книжка..."), 'gift_book', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('erobook_4', _("И снова у меня для тебя книжка..."), 'gift_book', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('erobook_5', _("У меня снова для тебя книжка..."), 'gift_book', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('pajamas', _("У меня для тебя подарок {i}(Пижама){/i}"), 'gift_pajamas', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift('b.lingerie', _("У меня есть кое-что, о чём мы беседовали..."), "gift_black_lingerie", -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        Gift(['ferrero-m', 'ferrero-b'], _("Прикупил для тебя немного сладенького!"), 'alice_gift_sweets', -1, "all(['pajamas' in alice.gifts, alice.plan_name in ['sun', 'read', 'resting', 'blog'], not alice.daily.sweets, (alice.daily.oiled!=2 or alice.flags.touched), not alice.sorry.owe])"),
        Gift('mistress1', _("У меня для тебя подарок {i}(Кожаный костюм){/i}"), 'alice_gift_mistress1', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog', 'tv']"),
        Gift('whip', _("У меня для тебя подарок {i}(Плётка){/i}"), 'alice_gift_whip', -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog', 'tv']"),
        ],
    'ann'   : [
        # Gift(['cosmatic1', 'cosmatic2', 'cosmatic3'], _("У меня для тебя подарок {i}(Косметика){/i}"), 'gift_cosmatics'),
        Gift('fit1', _("Мам, я купил тебе одежду полегче!"), 'ann_gift_fit1', 0, "ann.plan_name in ['read', 'resting', 'sun']"),
        ],
    }
