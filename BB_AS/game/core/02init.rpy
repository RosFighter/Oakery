init 9999 python:
    renpy.config.rollback_enabled = True
    renpy.config.hard_rollback_limit = 16
    renpy.config.rollback_length = 16

init python:
    config.statement_callbacks.remove(_window_auto_callback)
    renpy.game.preferences.show_empty_window = False

define lime   = "#00FF00"
define red    = "#FF0000"
define orange = "#FFBE00"
define gray   = "#808080"

# define config.gl2 = True
define dop = namedtuple('dop', 'day tm ctm ll ul ddop')

define failed = _("{color=#E59400}{i}Убеждение не удалось!{/i}{/color}\n")
define succes = _("{color=#00FF00}{i}Убеждение удалось!{/i}{/color}\n")

define undetect = _("{color=#00FF00}{i}Вы остались незамеченным!{/i}{/color}\n")
define spotted  = _("{color=#E59400}{i}Вас заметили!{/i}{/color}\n")
define risky    = _("{color=#E59400}{i}Слишком рискованно!{/i}{/color}\n")

define alice_good_mass = _("{color=#00FF00}{i}Алисе понравился массаж!{/i}{/color}\n")
define alice_bad_mass  = _("{color=#E59400}{i}Алисе не понравился массаж!{/i}{/color}\n")

define lisa_good_mass = _("{color=#00FF00}{i}Лизе понравился массаж!{/i}{/color}\n")
define lisa_bad_mass  = _("{color=#E59400}{i}Лизе не понравился массаж!{/i}{/color}\n")

define ann_good_mass = _("{color=#00FF00}{i}Маме понравился массаж!{/i}{/color}\n")
define ann_bad_mass  = _("{color=#E59400}{i}Маме не понравился массаж!{/i}{/color}\n")
define succes_hide = _("{color=#00FF00}{i}Получилось!{/i}{/color}\n")
define failed_hide  = _("{color=#E59400}{i}Не получилось!{/i}{/color}\n")

define restrain = _("{color=#00FF00}{i}Удалось сдержаться{/i}{/color}\n")
define norestrain = _("{color=#E59400}{i}Сдержаться не удалось{/i}{/color}\n")

define lisa_good_kiss = _("{color=#00FF00}{i}Лизе понравился поцелуй!{/i}{/color}\n")
define lisa_bad_kiss  = _("{color=#E59400}{i}Лизе не понравился поцелуй!{/i}{/color}\n")

define like = _("{color=#00FF00}{i}Ей нравится!{/i}{/color}\n")
define dont_like = _("{color=#E59400}{i}Ей не нравится!{/i}{/color}\n")

define lucky = _("{color=#00FF00}{i}Повезло!{/i}{/color}\n")
define unlucky = _("{color=#E59400}{i}Не повезло!{/i}{/color}\n")

define config.has_autosave = False
define config.has_quicksave = False

define config.autosave_slots = 30
define config.quicksave_slots = 30
define config.autosave_on_quit = False
default persistent.grid_vbox = 'grid'
default persistent.orint = False
default persistent.request_savename = True
default persistent.transparent_textbox = False
default persistent.all_opportunities = False
default number_autosave = 0
default number_quicksave = 0
default number_save = 0
default last_save_name = "(None)"

# (для экрана сохранений андроид)
default day = 1
default tm  = '08:50'
default save_name = ''

default morningwood_var = [1, 2, 3]

default persistent.memories = {}
default persistent.mems_var = []

default persistent.photos = {}
default expected_photo = []

default purchased_items = []

define cam_flag = []
define cam_list = []

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
    'blog1'      : TalkTheme('alice', _("Значит, у тебя есть блог?"), 'talkblog1', "alice.flags.crush==1", -1),
    'blog2'      : TalkTheme('alice', _("Слушай, насчёт блога..."), 'talkblog2', "poss['blog'].st()==1", 1),
    'blog3'      : TalkTheme('alice', _("Насчёт твоего блога... А если не особо раздеваться?"), 'talkblog3', "all([alice.dcv.feature.done, alice.stat.mast, poss['blog'].st() in [2,3]])", 1),
    'alice_dw'   : TalkTheme('alice', _("Насчёт посуды..."), 'wash_dishes_alice', "not alice.daily.dishes and alice.plan_name == 'dishes'", -2),
    'alice_tv'   : TalkTheme('alice', _("Не возражаешь против компании?"), 'alice_talk_tv', "not alice.daily.tvwatch and alice.plan_name == 'tv'"),
    'aboutbooks' : TalkTheme('alice', _("Что читаешь?"), 'alice_aboutbooks', "alice.plan_name == 'read' and not poss['secretbook'].used(0)"),
    'alice_peep' : TalkTheme('alice', _("Хотел извиниться за утренний инцидент..."), 'Alice_sorry', "all([alice.daily.shower==3, alice.dcv.shower.done, not (alice.flags.touched and len(alice.sorry.give)>3)])"),
    'alice_sol'  : TalkTheme('alice', _("Загораешь?"), 'Alice_solar', "all([not alice.hourly.sun_cream, any([not alice.daily.oiled, alice.daily.oiled==3]), alice.plan_name == 'sun'])"),
    'alice_gift' : TalkTheme('alice', _("У меня для тебя обещанная вкусняшка!"), 'alice_sorry_gifts', "all([len(alice.sorry.give)<3, alice.sorry.owe, alice.sorry.there_in_stock(), alice.plan_name in ['sun', 'read', 'resting', 'blog'], alice.daily.oiled != 2])"),
    'alice_gift2': TalkTheme('alice', _("У меня для тебя обещанная вкусняшка!"), 'alice_gift_sweets', "all([len(alice.sorry.give)>2, alice.sorry.owe, alice.sorry.there_in_stock(), alice.plan_name in ['sun', 'read', 'resting', 'blog'], (alice.daily.oiled!=2 or alice.flags.touched)])"),
    'aboutbath'  : TalkTheme('alice', _("Насчёт ванны ночью..."), 'alice_about_bath', "alice.flags.incident in [1, 3]"),
    'alice.kiss' : TalkTheme('alice', _("А ты умеешь целоваться?"), 'alice_about_kiss', "all([lisa.dcv.seduce.stage==1, 'alice' not in flags.how_to_kiss])"),
    'eric.ling0' : TalkTheme('alice', _("Я слышал, Эрик тебе новое бельё собирается купить?"), 'alice_about_lingerie0', "alice.dcv.intrusion.stage==1"),
    'eric.ling1' : TalkTheme('alice', _("Покажешь боди, которое тебе Эрик купит?"), 'alice_showing_lingerie1', "all([alice.dcv.intrusion.stage==2, current_room==house[1]])"),
    'a.privpun0' : TalkTheme('alice', _("Хотел узнать, хорошо ли тебе сидится?"), 'alice_about_defend_punish0', "all([alice.dcv.private.enabled, alice.dcv.private.stage==0, alice.dcv.private.lost>1])"),
    'a.privpun1' : TalkTheme('alice', _("Не слабо тебя отшлёпали!"), 'alice_about_defend_punish1', "all([alice.dcv.private.stage==2, alice.dcv.private.lost>1])"),
    'a.privpun2' : TalkTheme('alice', _("Ты не передумала о наказаниях?"), 'alice_about_defend_punish1.cont', "all([alice.dcv.private.stage==3, alice.dcv.private.lost>1])"),
    'a.privpunt' : TalkTheme('alice', _("Отшлёпать тебя сейчас или..."), 'alice_about_private_punish', "all([not alice.flags.private, alice.dcv.private.stage==4, alice.dcv.private.lost>1])"),
    'a.privpun'  : TalkTheme('alice', _("Пора отшлёпать одну милую попку!"), 'alice_private_punish_0', "all([alice.plan_name in ['sun', 'smoke'], alice.flags.private, alice.dcv.private.stage==4, not alice.dcv.private.done, not alice.spanked])"),
    'a.privpunr' : TalkTheme('alice', _("Пора отшлёпать одну милую попку!"), 'alice_private_punish_r', "all([alice.plan_name == 'sun', alice.dcv.private.stage==5, not alice.dcv.private.done, not alice.spanked])"),

    'ask_money'  : TalkTheme('ann', _("Мам, дай денег, пожалуйста..."), 'ann_ask_money', "all([ann.daily.ask_money==0, not flags.about_earn])"),
    'aboutfood'  : TalkTheme('ann', _("Я продукты заказал!"), 'ann_aboutfood', "dcv.buyfood.stage==2 and not dcv.buyfood.done"), # dcv.buyfood.lost==2"),
    'aboutpool'  : TalkTheme('ann', _("Мам, бассейн чист!"), 'ann_aboutpool', "dcv.clearpool.stage==2 and dcv.clearpool.lost>3"),
    'ann_tv'     : TalkTheme('ann', _("Что смотришь?"), 'ann_talk_tv', "not ann.daily.tvwatch and ann.plan_name == 'tv'"),
    'ann_mw'     : TalkTheme('ann', _("Насчёт случая с Лизой..."), 'Ann_MorningWood', "dcv.mw.stage == 1"),
    'ann.kiss'   : TalkTheme('ann', _("Мам, а как учатся целоваться?"), 'ann_about_kiss', "all([lisa.dcv.seduce.stage==1, 'ann' not in flags.how_to_kiss])"),
    'ann.secr1'  : TalkTheme('ann', _("Мам, Кира отправила меня к тебе..."), 'ann_about_ann_secret1', "ann.dcv.feature.stage==1"),
    'ann.yoga0'  : TalkTheme('ann', _("С тобой можно?"), 'ann_yoga_with_max0', "all([ann.plan_name=='yoga', ann.dcv.feature.stage==4, ann.dcv.feature.done])"),
    'ann.yoga1'  : TalkTheme('ann', _("Я присоединюсь?"), 'ann_yoga_with_maxr', "all([ann.plan_name=='yoga', ann.dcv.feature.stage>4, ann.dcv.feature.done])"),

    'eric.money' : TalkTheme('eric', _("Мне нужны деньги..."), 'eric_needmoney', "all([not eric.daily.ask_money, GetRelMax('eric')[0]>3, 'money' in flags.bonus_from_eric])"),
    'eric.wtf'   : TalkTheme('eric', _("Эрик, мы же договорились!"), 'eric_voy_wtf', "all([flags.voy_stage==1, GetRelMax('eric')[0]>0])"),
    'eric.kira0' : TalkTheme('eric', _("Хочу рассказать тебе кое-что о Кире..."), 'Eric_talk_about_Kira_0', "all([wcv.catch_Kira.enabled, not wcv.catch_Kira.done, wcv.catch_Kira.stage<1, GetRelMax('eric')[0]>0])"),
    'eric.kira1' : TalkTheme('eric', _("Я хотел поговорить о Кире..."), 'Eric_talk_about_Kira_1', "all([wcv.catch_Kira.stage==1, kira.dcv.battle.stage>0])"),

    'kt1'        : TalkTheme('kira', _("Да тут всегда хорошая погода..."), 'kira_firsttalk', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==0])"),
    'kt2'        : TalkTheme('kira', _("Ага, как всегда..."), 'kira_talk2', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==1])"),
    'kt3'        : TalkTheme('kira', _("Да, шикарная!"), 'kira_talk3', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==2])"),
    'kira.kiss'  : TalkTheme('kira', _("Кира, мне нужно научиться целоваться..."), 'kira_about_kiss', "all([kira.dcv.feature.stage>2, lisa.dcv.seduce.stage==1, list_in_list(['ann', 'alice'], flags.how_to_kiss), 'kira' not in flags.how_to_kiss])"),
    'kt4'        : TalkTheme('kira', _("Ну как, ты с мамой-то поговорила?"), 'kira_talk4', "all([kira.stat.blowjob, kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==3])"),
    'kt5'        : TalkTheme('kira', _("Как отдыхается, тётя Кира?"), 'kira_talk5', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==4])"),
    'kt6'        : TalkTheme('kira', _("Насчёт фотосессии..."), 'kira_talk6', "all([kira.dcv.feature.done, kira.plan_name=='sun', kira.dcv.feature.stage==5, (not items['photocamera'].have and not items['nightie2'].have) or (items['photocamera'].have and items['nightie2'].have)])"),
    'kt_ft1'     : TalkTheme('kira', _("Понравились фотографии?"), 'kira_about_photo1', "all([kira.dcv.feature.done, kira.dcv.feature.stage==6, kira.plan_name=='sun'])"),
    'kt_cuni'    : TalkTheme('kira', _("Не злишься на меня, тётя Кира?"), 'kira_about_cuni', "all([kira.dcv.sweets.done, kira.flags.promise, kira.plan_name=='sun'])"),
    'kt.ft2'     : TalkTheme('kira', _("Так когда будем снова фотографироваться, тётя Кира?"), 'kira_about_photo2', "all([kira.dcv.feature.stage==7, kira.plan_name=='sun', not expected_photo, kira.dcv.photo.stage==1, kira.dcv.photo.done, kira.dcv.feature.done])"),
    # 'ann.secr0'  : TalkTheme('kira', _("Тётя Кира, когда ты уже с мамой поговоришь?!"), 'kira_about_ann_secret0', "all([kira.plan_name=='sun', not ann.dcv.feature.stage, flags.lisa_sexed>=2])"),
    'ann.secr0'  : TalkTheme('kira', _("Тётя Кира, когда ты уже с мамой поговоришь?!"), 'kira_about_ann_secret0', "all([kira.plan_name=='sun', not ann.dcv.feature.stage, flags.lisa_sexed>=1, alice.dcv.intrusion.enabled, alice.dcv.intrusion.lost<3, kira.dcv.photo.stage>1])"),
    'ann.secr2'  : TalkTheme('kira', _("Я хотел спросить про тот случай из детства мамы..."), 'kira_about_ann_secret2', "all([kira.plan_name=='sun', ann.dcv.feature.stage==2, ann.dcv.feature.done])"),
    'ann.secr_r' : TalkTheme('kira', _("Расскажи уже про тот случай из детства мамы..."), 'kira_about_ann_secret_r', "all([kira.plan_name=='sun', ann.dcv.feature.stage==3, ann.dcv.feature.done])"),

    'lisa_fd'    : TalkTheme('lisa', _("О школе..."), 'about_school', "day==1 and tm>='16:00' and flags.lisa_fd==0 and lisa.flags.crush==0"),
    'lisa_swim'  : TalkTheme('lisa', _("А ты чего так загораешь?"), 'talk_swim', "poss['Swimsuit'].st()<0 and lisa.plan_name == 'sun'"),
    'lisas_boy'  : TalkTheme('lisa', _("Насчёт твоего парня..."), 'about_boy', "lisa.flags.crush==1", 0, "lisa_boy"),
    'lisas_boy2' : TalkTheme('lisa', _("Насчёт твоего парня..."), 'about_boy2', "2 < lisa.flags.crush < 6", 1),
    'lisa_dw'    : TalkTheme('lisa', _("Насчёт посуды..."), 'wash_dishes_lisa', "not lisa.daily.dishes and lisa.plan_name == 'dishes'", -2),
    'lisa_mw'    : TalkTheme('lisa', _("Насчёт этого случая утром..."), 'Lisa_MorningWood', "poss['seduction'].st() == 0 and current_room==house[0]", 0, "talkcooldown"),
    'lisa_mw2'   : TalkTheme('lisa', _("Хотел поговорить о Большом Максе..."), 'Lisa_MorningWoodCont', "dcv.mw.stage==3 and current_room==house[0]"),
    'lisa_mw3'   : TalkTheme('lisa', _("А ты у нас шалунья, оказывается..."), 'Lisa_MorningWoodCont', "dcv.mw.stage==5 and current_room==house[0]"),
    'lisa_sg1'   : TalkTheme('lisa', _("Насчёт успеваемости..."), 'Lisa_sg1', "poss['sg'].st() == 0"),
    # 'lisa_sg2'   : TalkTheme('lisa', _("Ну как, ты подумала о моих условиях?"), 'Lisa_sg2', "poss['sg'].st() == 1 and lisa.flags.pun > 0"),
    'lisa_hw'    : TalkTheme('lisa', _("Помочь с уроками?"), 'Lisa_HomeWork', "poss['sg'].st() > 1 and not lisa.daily.homework and lisa.plan_name == 'homework'"),
    'lisa_peep'  : TalkTheme('lisa', _("Хотел извиниться за утренний инцидент..."), 'Lisa_sorry', "lisa.daily.shower==3 and lisa.dcv.shower.done"),
    'lisa_gift'  : TalkTheme('lisa', _("У меня для тебя обещанная вкусняшка!"), 'lisa_sorry_gifts', "all([lisa.sorry.owe, lisa.sorry.there_in_stock(), lisa.plan_name in ['sun', 'read', 'phone']])"),
    'l.ab.sec1'  : TalkTheme('lisa', _("У тебя странный вид..."), 'liza_secret_alisa', "all([poss['nightclub'].st() < 5, 'dress' in alice.gifts, GetRelMax('lisa')[0]>2, lisa.GetMood()[0]>1, alice.dcv.feature.stage<1, alice.dcv.feature.done])"),
    'l.ab.sec2'  : TalkTheme('lisa', _("Может всё-таки поделишься своими переживаниями по поводу Алисы?"), 'liza_secret_alisa', "all([poss['nightclub'].st() < 5, 'dress' in alice.gifts, GetRelMax('lisa')[0]>2, lisa.GetMood()[0]>1, alice.dcv.feature.stage>0, alice.dcv.feature.done])"),
    'lisa.hand'  : TalkTheme('lisa', _("Массаж рук заказывала?"), 'liza_hand_mass', "GetWeekday(day) in [2, 5] and all([learned_hand_massage(), lisa.flags.handmass, not lisa.daily.massage, lisa.plan_name == 'phone'])"),
    'l.firstkiss': TalkTheme('lisa', _("Ну что, Лиза, готова?"), 'lisa_ment_kiss1', "all([GetRelMax('lisa')[0]>1, lisa.plan_name=='read', lisa.dcv.seduce.stage>3, 'lisa' not in flags.how_to_kiss])"),
    'l.nextkiss' : TalkTheme('lisa', _("Ну что, готова?"), 'lisa_ment_kiss', "all([lisa.plan_name=='read', lisa.dcv.seduce.done, poss['seduction'].st()>8, flags.stopkiss<1])"),
    'l.sex-ed1'  : TalkTheme('lisa', _("Лиза, ты же любишь читать?"), 'lisa_sexbook1', "all([lisa.plan_name in ['sun', 'read', 'phone'], items['sex.ed'].have, poss['seduction'].st()<13])"),
    'l.sex-ed2'  : TalkTheme('lisa', _("Лиза, у меня для тебя особая книжка..."), 'lisa_sexbook2', "all([lisa.plan_name in ['sun', 'read', 'phone'], items['sex.ed'].have, poss['seduction'].st()>13])"),
    'l.ab_aeed0' : TalkTheme('lisa', _("Рассказывай, что делали?"), 'lisa_about_ae_sexed0', "not flags.l_ab_sexed and flags.lisa_sexed==0"),
    'l.ab_aeed1' : TalkTheme('lisa', _("Ну так и чему же тебя учили?"), 'lisa_about_ae_sexed1', "not flags.l_ab_sexed and flags.lisa_sexed==1"),
    'l.ab_aeed2' : TalkTheme('lisa', _("Что новенького было на уроке?"), 'lisa_about_ae_sexed2', "not flags.l_ab_sexed and flags.lisa_sexed==2"),
    'l.ab_aeed3' : TalkTheme('lisa', _("Что нового мама с Эриком тебе рассказали?"), 'lisa_about_ae_sexed3', "not flags.l_ab_sexed and flags.lisa_sexed==3"),
    'l.ab_aeed4' : TalkTheme('lisa', _("Что нового узнала на уроке у мамы и Эрика?"), 'lisa_about_ae_sexed4', "not flags.l_ab_sexed and flags.lisa_sexed==4"),
    'l.stopkiss' : TalkTheme('lisa', _("{i}урок поцелуев{/i}"), 'lisa_stop_kiss', "all([lisa.plan_name=='read', lisa.dcv.seduce.done, poss['seduction'].st()>7, flags.stopkiss==1])"),
    'lisas_boy3' : TalkTheme('lisa', _("Насчёт Алекса..."), 'about_boy3', "all([GetRelMax('lisa')[0]>1, lisa.flags.crush==6, day>=10, lisa.dcv.feature.done])", 1),
    'l.olivia_1' : TalkTheme('lisa', _("Есть успехи с Оливией?"), 'about_olivia_1', "all([lisa.flags.crush==7, lisa.dcv.feature.done, GetWeekday(day)!=0])", 1),
    'l.olivia_2' : TalkTheme('lisa', _("Что-нибудь узнала про Оливию?"), 'about_olivia_2', "all([lisa.flags.crush==8, lisa.dcv.feature.done, GetWeekday(day)!=0])", 1),
    'l.olivia_3' : TalkTheme('lisa', _("Ну так, что там с трусиками Оливии?"), 'about_olivia_3', "all([lisa.flags.crush==9, lisa.dcv.feature.done, GetWeekday(day)!=0])", 1),
    'l.olivia_4' : TalkTheme('lisa', _("Ты позвала Оливию к нам?"), 'about_olivia_4', "all([lisa.flags.kiss_lesson, lisa.flags.crush==10, lisa.dcv.feature.done, GetWeekday(day)!=3])", 1),
    'l_ab_alex4' : TalkTheme('lisa', _("Ну как, получилось рассказать всё Оливии?"), 'about_alex4', "all([lisa.flags.crush==15, GetWeekday(day) in [3, 4] or (GetWeekday(day)=2 and tm>'19:00')])"),
    'l.toples_0' : TalkTheme('lisa', _("Нравится, что я спасаю твою попку от наказания?"), 'about_horror_toples', "all([tm<'23:00', lisa.flags.topless, lisa.flags.defend>4, not lisa.dcv.other.stage, lisa.dcv.other.lost])"),
    'ol.l.t1'    : TalkTheme(['lisa', 'olivia'], _("Учтите, я испытываю... некоторый подъём!"), 'olivia_talk1', "all([olivia.plan_name=='sun', not olivia.dcv.feature.stage, olivia.dcv.feature.done])"),
    'ol.l.t2'    : TalkTheme(['lisa', 'olivia'], _("Пошепчемся немного о моей сестрёнке?"), 'olivia_talk2', "all([olivia.plan_name=='sun', olivia.dcv.feature.stage==1, olivia.dcv.feature.done])"),
    'ol.l.t3'    : TalkTheme(['lisa', 'olivia'], _("Что новенького, Оливия?"), 'olivia_talk3', "all([olivia.plan_name=='sun', GetWeekday(day)==2, olivia.dcv.feature.stage==3, olivia.dcv.feature.done])"),
    'ol.l.t4'    : TalkTheme(['lisa', 'olivia'], _("Рад тебя видеть, Оливия!"), 'olivia_talk4', "all([olivia.plan_name=='sun', GetWeekday(day)in[2, 5], olivia.dcv.feature.stage==4, olivia.dcv.feature.done, olivia.dcv.special.stage])"),
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
        # Gift(['ritter-m', 'ritter-b'], _("{color=#808080}У меня для тебя вкусняшка! \n (нужно выждать несколько дней){/color}"), '', -1, "all(['bathrobe' in lisa.gifts, lisa.plan_name in ['sun', 'read', 'phone'], not lisa.dcv.sweets.done])"),
        Gift(['ritter-m', 'ritter-b'], _("У меня для тебя вкусняшка!"), 'lisa_gift_sweets', -1, "all(['bathrobe' in lisa.gifts, lisa.plan_name in ['sun', 'read', 'phone'], not lisa.daily.sweets])"),
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
        Gift("b.lingerie", _("У меня есть кое-что, о чём мы беседовали..."), "gift_black_lingerie", -1, "alice.plan_name in ['sun', 'read', 'resting', 'blog']"),
        # Gift(['ferrero-m', 'ferrero-b'], _("{color=#808080}Прикупил для тебя немного сладенького! \n (нужно выждать несколько дней){/color}"), '', -1, "all(['pajamas' in alice.gifts, alice.plan_name in ['sun', 'read', 'resting', 'blog'], not alice.dcv.sweets.done, not alice.sorry.owe])"),
        Gift(['ferrero-m', 'ferrero-b'], _("Прикупил для тебя немного сладенького!"), 'alice_gift_sweets', -1, "all(['pajamas' in alice.gifts, alice.plan_name in ['sun', 'read', 'resting', 'blog'], not alice.daily.sweets, (alice.daily.oiled!=2 or alice.flags.touched), not alice.sorry.owe])"),
        ],
    'ann'   : [
        # Gift(['cosmatic1', 'cosmatic2', 'cosmatic3'], _("У меня для тебя подарок {i}(Косметика){/i}"), 'gift_cosmatics'),
        Gift('fit1', _("Мам, я купил тебе одежду полегче!"), 'ann_gift_fit1', 0, "ann.plan_name in ['read', 'resting', 'sun']"),
        ],
    }
