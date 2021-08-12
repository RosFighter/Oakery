
label set_alice_schedule:
    # полностью очистим расписание
    $ alice.plan = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]

    # добавим базовое расписание
    $ alice.add_schedule(
        Schedule((1, 2, 3, 4, 5, 6, 0), '0:0', '0:59', 'bath', "принимает ванну", 'house', 3, 'alice_bath', enabletalk=False, glow=120),
        Schedule((1, 2, 3, 4, 5, 6, 0), '1:0', '5:59', 'sleep', "спит (ночь)", 'house', 1, 'alice_sleep_night', enabletalk=False, glow=105),
        Schedule((2, 3, 5, 6, 0), '6:0', '7:59', 'sleep', "спит (утро)", 'house', 1, 'alice_sleep_morning', enabletalk=False, glow=110),
        Schedule((1, 4), '6:0', '6:59', 'sleep', "спит (утро)", 'house', 1, 'alice_sleep_morning', variable="not 'kira' in chars", enabletalk=False, glow=110),
        Schedule((1, 4), '6:0', '6:59', 'sleep', _("спит (утро)"), 'house', 1, 'alice_sleep_morning', variable="'kira' in chars", enabletalk=False, glow=110),
        Schedule((1, 4), '7:0', '7:59', 'sleep', "спит (утро)", 'house', 1, 'alice_sleep_morning', variable="not 'kira' in chars", enabletalk=False, glow=110),
        Schedule((1, 4), '7:0', '7:59', 'shower', 'в душе с Лизой', 'house', 3, 'alice_lisa_shower', variable="'kira' in chars", enabletalk=False, glow=135),
        Schedule((1, 4), '8:0', '8:59', 'shower', "принимает душ", 'house', 3, 'alice_shower', variable="not 'kira' in chars", enabletalk=False, glow=120),
        Schedule((1, 4), '8:0', '8:59', 'resting', _("в своей комнате"), 'house', 1, 'alice_rest_morning', variable="'kira' in chars", talklabel='alice_morning_closer', glow=110),
        # одна в душе
        Schedule((2, 5), '8:0', '8:59', 'shower', "принимает душ", 'house', 3, 'alice_shower', enabletalk=False, glow=120),
        Schedule((3, 6, 0), '8:0', '8:59', 'shower', "принимает душ", 'house', 3, 'alice_shower', variable="not 'kira' in chars", enabletalk=False, glow=120),
        Schedule((3, 6, 0), '8:0', '8:59', 'shower', 'в душе с Кирой', 'house', 3, 'kira_alice_shower', variable="'kira' in chars", enabletalk=False, glow=140),
        Schedule((0, 1, 2, 3, 4, 5, 6), '9:0', '9:59', 'breakfast', "семейный завтрак", 'house', 5, 'breakfast', enabletalk=False, glow=105),
        Schedule((1, 2, 3, 4, 5), '10:0', '10:59', 'resting', "в своей комнате", 'house', 1, 'alice_rest_morning', talklabel='alice_morning_closer', glow=110),
        Schedule((6,), '10:0', '10:59', 'dressed', "одевается в магазин", 'house', 1, 'alice_dressed_shop', enabletalk=False, glow=110),
        Schedule((0,), '10:0', '10:59', 'dishes', "моет посуду", 'house', 4, 'alice_dishes', variable='not dishes_washed', talklabel='alice_dishes_closer'),
        Schedule((0,), '10:0', '10:59', 'read', "читает на веранде", 'house', 5, 'alice_read', talklabel='alice_read_closer', variable='dishes_washed', glow=110),
        Schedule((1, 2, 3, 4, 5), '11:0', '11:59', 'dishes', "моет посуду", 'house', 4, 'alice_dishes', variable='not dishes_washed', talklabel='alice_dishes_closer'),
        Schedule((1, 2, 3, 4, 5), '11:0', '11:59', 'read', "читает на веранде", 'house', 5, 'alice_read', talklabel='alice_read_closer', variable='dishes_washed', glow=110),
        Schedule((0,), '11:0', '11:59', 'dressed', "одевается к подруге", 'house', 1, 'alice_dressed_friend', enabletalk=False, glow=110),
        Schedule((1, 2, 3, 4, 5), '12:0', '12:59', 'sun', "загорает", 'house', 6, 'alice_sun', variable="not 'kira' in chars", glow=110),
        Schedule((1, 2, 3, 4, 5), '12:0', '12:59', 'read', _("читает на веранде"), 'house', 5, 'alice_read', variable="'kira' in chars", talklabel='alice_read_closer', glow=110),
        Schedule((1, 2, 3, 4, 5), "13:0", "13:29", "smoke", _("курит"), "house", 6, "alice_smoke", glow=105, variable="day>1 and alice.dcv.special.done"),
        Schedule((1, 2, 3, 4, 5), "13:0", "13:29", "swim", _("в бассейне"), "house", 6, "alice_swim", glow=105, variable="not (day>1 and alice.dcv.special.done)"),
        Schedule((1, 2, 3, 4, 5), '13:30', '14:59', 'swim', "в бассейне", 'house', 6, 'alice_swim', glow=105),
        Schedule((6,), '11:0', '13:59', 'in_shop', "в магазине"),
        Schedule((6,), '14:0', '14:59', 'dressed', "одевается к подруге", 'house', 1, 'alice_dressed_friend', enabletalk=False, glow=110),
        Schedule((1, 2, 3, 4, 5), '15:0', '15:59', 'sun', "загорает", 'house', 6, 'alice_sun', glow=110),
        Schedule((1, 2, 3, 4, 5), '16:0', '17:59', 'read', "читает на веранде", 'house', 5, 'alice_read', talklabel='alice_read_closer', glow=110),
        Schedule((6,), '15:0', '16:59', 'at_friends'),
        Schedule((0,), '12:0', '16:59', 'at_friends'),
        Schedule((6,), '17:0', '17:59', 'sun', "загорает с Анной", 'house', 6, 'ann_alice_sun', glow=115),
        Schedule((0,), '17:0', '17:59', 'swim', "в бассейне с Анной", 'house', 6, 'ann_alice_swim', glow=110),
        Schedule((1, 2, 3, 4, 5), '18:0', '18:59', 'cooking', "готовит ужин", 'house', 4, 'alice_cooking_dinner', talklabel='alice_cooking_closer'),
        Schedule((0, 6), '18:0', '18:59', 'read', "читает на веранде", 'house', 5, 'alice_read', talklabel='alice_read_closer', glow=110),
        Schedule((0, 1, 2, 3, 4, 5, 6), '19:0', '19:59', 'dinner', "семейный ужин", 'house', 5, 'dinner', enabletalk=False, glow=105),
        Schedule((1, 2, 3, 4, 5, 6, 0), '20:0', '21:59', 'blog', "в своей комнате", 'house', 1, 'alice_rest_evening', talklabel='alice_evening_closer', glow=110),
        Schedule((1, 2, 3, 4, 5, 6, 0), '22:0', '23:59', 'tv', "смотрит ТВ", 'house', 4, 'alice_tv', talklabel='alice_tv_closer'),
        )

    if flags.dinner >= 11:
        # после второй субботы Алиса может посещать ночной клуб
        call alice_init_nightclub from _call_alice_init_nightclub_2

    # if 'kira' in chars:
    #     # Приехала Кира
    #     call alice_after_arrival_kira from _call_alice_after_arrival_kira

    if 'black_linderie' in alice.gifts:
        # Макс подарил Алисе черное нижнее бельё
        call alice_can_blog_in_underwear from _call_alice_can_blog_in_underwear

    return

# Алиса может посещать ночной клуб
label alice_init_nightclub:
    $ alice.add_schedule(
        Schedule((5,), '20:0', '20:59', 'dressed', 'одевается в ночной клуб', 'house', 1, 'alice_dressed_club', variable="not flags.noclub", enabletalk=False, glow=110),
        Schedule((5,), '20:0', '20:59', 'blog', "блог в нижнем белье", 'house', 1, 'alice_blog_lingerie', variable="flags.noclub", enabletalk=False, glow=150),
        Schedule((5,), '21:0', '21:59', 'blog', "блог в нижнем белье", 'house', 1, 'alice_blog_lingerie', variable="flags.noclub", enabletalk=False, glow=150),
        Schedule((5,), '21:0', '21:59', 'club', 'в ночном клубе', variable="not flags.noclub"),
        Schedule((5,), '22:0', '23:59', 'tv', "смотрит ТВ", 'house', 4, 'alice_tv', variable="flags.noclub", talklabel='alice_tv_closer'),
        Schedule((5,), '22:0', '23:59', 'club', 'в ночном клубе', variable="not flags.noclub"),
        Schedule((6,), '0:0', '0:59', 'bath', "принимает ванну", 'house', 3, 'alice_bath', variable="flags.noclub", enabletalk=False, glow=120),
        Schedule((6,), '0:0', '0:59', 'club', 'в ночном клубе', variable="not flags.noclub"),
        Schedule((6,), '1:0', '2:59', 'sleep', "спит (ночь)", 'house', 1, 'alice_sleep_night', variable="flags.noclub", enabletalk=False, glow=105),
        Schedule((6,), '1:0', '2:59', 'club', 'в ночном клубе', variable="not flags.noclub"),
        Schedule((6,), '3:0', '3:59', 'sleep', "спит (ночь)", 'house', 1, 'alice_sleep_night', variable="flags.noclub", enabletalk=False, glow=105),
        Schedule((6,), '3:0', '3:59', 'bath', 'в ванной после ночного клуба (Кира ещё не приехала)', 'house', 3, 'alice_after_club', variable="not flags.noclub and 'kira' not in chars", enabletalk=False, glow=120),
        Schedule((6,), '3:0', '3:59', 'return', 'возвращение из ночного клуба (с Кирой)', 'house', 6, 'return_from_club', variable="not flags.noclub and 'kira' in chars", enabletalk=False, glow=130),
        )
    return

# после приезда Киры у Алисы меняется расписание душа и чтения
# label alice_after_arrival_kira:
#     $ alice.add_schedule(
#         Schedule((1, 4), '6:0', '6:59', 'sleep', _("спит (утро)"), 'house', 1, 'alice_sleep_morning', enabletalk=False, glow=110),
#         Schedule((1, 4), '7:00', '7:59', 'shower', 'в душе с Лизой', 'house', 3, 'alice_lisa_shower', enabletalk=False, glow=135),
#         Schedule((1, 4), '8:0', '8:59', 'resting', _("в своей комнате"), 'house', 1, 'alice_rest_morning', talklabel='alice_morning_closer', glow=110),
#         Schedule((3, 6, 0), '8:00', '8:59', 'shower', 'в душе с Кирой', 'house', 3, 'kira_alice_shower', enabletalk=False, glow=140),
#         Schedule((1, 2, 3, 4, 5), '12:0', '12:59', 'read', _("читает на веранде"), 'house', 5, 'alice_read', talklabel='alice_read_closer', glow=110),
#         )
#     return

# теперь Алиса начинает вести блог в нижнем белье
label alice_can_blog_in_underwear:
    $ alice.add_schedule(
        Schedule((1, 4), '20:0', '21:59', 'blog', "блог в нижнем белье", 'house', 1, 'alice_blog_lingerie', variable="poss['blog'].st()>4 and alice.dcv.feature.done", enabletalk=False, glow=150),
        Schedule((1, 4), '20:0', '21:59', 'blog', "в своей комнате", 'house', 1, 'alice_rest_evening', variable="not(poss['blog'].st()>4 and alice.dcv.feature.done)", talklabel='alice_evening_closer', glow=110),
        Schedule((3,), '20:0', '20:59', 'blog', "в своей комнате", 'house', 1, 'alice_rest_evening', variable="not alice.dcv.intrusion.enabled", enabletalk=False, glow=150),
        Schedule((3,), '20:0', '20:59', 'blog', "блог с Эриком", 'house', 1, 'blog_with_Eric', variable="alice.dcv.intrusion.enabled", enabletalk=False, glow=150),
        Schedule((3,), '21:0', '21:59', 'blog', "в своей комнате", 'house', 1, 'alice_rest_evening', variable="not alice.dcv.intrusion.enabled", enabletalk=False, glow=150),
        Schedule((3,), '21:0', '21:59', 'blog', "блог в нижнем белье", 'house', 1, 'alice_blog_lingerie', variable="alice.dcv.intrusion.enabled", enabletalk=False, glow=150),
        Schedule((6,), '20:0', '21:59', 'blog', "блог в нижнем белье", 'house', 1, 'alice_blog_lingerie', variable="alice.dcv.intrusion.enabled", enabletalk=False, glow=150),
        Schedule((6,), '20:0', '21:59', 'blog', "в своей комнате", 'house', 1, 'alice_rest_evening', variable="not alice.dcv.intrusion.enabled", talklabel='alice_evening_closer', glow=110),
        )
    return


################################################################################

label set_ann_schedule:
    # полностью очистим расписание
    $ ann.plan = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]

    # добавим базовое расписание
    $ ann.add_schedule(
        Schedule((0, 1, 2, 3, 4, 5, 6), '0:0', '5:59', 'sleep', "спит", 'house', 2, 'ann_sleep', enabletalk=False, glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '6:0', '6:59', 'shower', "принимает душ", 'house', 3, 'ann_shower', enabletalk=False, glow=120),
        Schedule((0, 1, 2, 3, 4, 5, 6), '7:0', '7:59', 'yoga', "занимается йогой", 'house', 6, 'ann_yoga', glow=115),
        Schedule((0, 1, 2, 3, 4, 5, 6), '8:0', '8:59', 'cooking', "готовит завтрак", 'house', 4, 'ann_cooking', talklabel='ann_cooking_closer'),
        Schedule((0, 1, 2, 3, 4, 5, 6), '9:0', '9:59', 'breakfast', "семейный завтрак", 'house', 5, 'breakfast', enabletalk=False, glow=105),
        Schedule((1, 2, 3, 4, 5), '10:0', '10:59', 'dressed', "одевается на работу", 'house', 2, 'ann_dressed_work', enabletalk=False, glow=115),
        Schedule((6, ), '10:0', '10:59', 'dressed', "одевается в магазин", 'house', 2, 'ann_dressed_shop', enabletalk=False, glow=115),
        Schedule((0, ), '10:0', '11:59', 'resting', "в своей комнате", 'house', 2, 'ann_resting'),
        Schedule((1, 2, 3, 4, 5), '11:0', '18:59', 'at_work', "на работе"),
        Schedule((6, ), '11:0', '13:59', 'in_shop', "в магазине"),
        Schedule((0, ), '12:0', '13:59', 'read', "читает на веранде", 'house', 5, 'ann_read', talklabel='ann_read_closer', glow=110),
        Schedule((0, 6), '14:0', '14:59', 'swim', "в бассейне", 'house', 6, 'ann_swim', glow=105),
        Schedule((0, 6), '15:0', '15:59', 'resting', "в своей комнате", 'house', 2, 'ann_resting', glow=110),
        Schedule((0, 6), '16:0', '16:59', 'read', "читает на веранде", 'house', 5, 'ann_read', talklabel='ann_read_closer', glow=110),
        Schedule((6, ), '17:0', '17:59', 'sun', "загорает с Алисой", 'house', 6, 'ann_alice_sun', glow=115),
        Schedule((0, ), '17:0', '17:59', 'swim', "в бассейне с Алисой", 'house', 6, 'ann_alice_swim', glow=110),
        Schedule((0, 6), '18:0', '18:59', 'cooking', "готовит ужин", 'house', 4, 'ann_cooking', talklabel='ann_cooking_closer'),
        Schedule((0, 1, 2, 3, 4, 5, 6), '19:0', '19:59', 'dinner', "семейный ужин", 'house', 5, 'dinner', enabletalk=False, glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '20:0', '20:59', 'bath', "принимает ванну", 'house', 3, 'ann_bath', enabletalk=False, glow=120),
        Schedule((0, 1, 2, 3, 4, 5, 6), '21:0', '21:59', 'tv', "смотрит ТВ", 'house', 4, 'ann_tv', talklabel='ann_tv_closer'),
        Schedule((0, 1, 2, 3, 4, 5, 6), '22:0', '23:59', 'resting', "в своей комнате", 'house', 2, 'ann_resting', glow=110),
        )

    if 'eric' in chars:
        call ann_after_appearance_eric from _call_ann_after_appearance_eric

    return

label ann_after_appearance_eric:
    $ ann.add_schedule(
        Schedule((2, 4, 5), '0:0', '5:59', 'sleep2', 'спит с Эриком', 'house', 2, 'eric_ann_sleep', enabletalk=False, glow=110),
        Schedule((2, 4, 5), '6:0', '6:59', 'shower2', 'в душе с Эриком', 'house', 3, 'eric_ann_shower', enabletalk=False, glow=130),
        Schedule((1, 3, 4), '21:0', '21:59', 'tv2', 'смотрит ТВ с Эриком', 'house', 4, 'eric_ann_tv', enabletalk=False, glow=150),
        # блок секс.обучения Лизы
        Schedule((1,), '22:00', '22:29', 'fuck', 'трахается с Эриком', 'house', '2', 'eric_ann_fucking', variable="not lisa.dcv.intrusion.stage", enabletalk=False, glow=150),
        Schedule((1,), '22:00', '22:29', 'sexed_lisa', 'АиЭ учат Лизу. Вводный урок', 'house', 2, 'sexed_lisa', variable="lisa.dcv.intrusion.stage and flags.lisa_sexed<0", enabletalk=False, glow=120),
        Schedule((1,), '22:00', '22:29', 'sexed_lisa', 'АиЭ учат Лизу', 'house', 2, 'sexed_lisa', variable="0<=flags.lisa_sexed<4", enabletalk=False, glow=180),
        Schedule((1,), '22:00', '22:29', 'fuck', 'трахается с Эриком', 'house', '2', 'eric_ann_fucking', variable="flags.lisa_sexed>=4", enabletalk=False, glow=150),
        # конец блока
        Schedule((1,), '22:30', '23:59', 'fuck', 'трахается с Эриком', 'house', '2', 'eric_ann_fucking', enabletalk=False, glow=150),
        Schedule((3, 4), '22:0', '23:59', 'fuck', 'трахается с Эриком', 'house', '2', 'eric_ann_fucking', enabletalk=False, glow=150),
        Schedule((2, 5, 6), '20:0', '23:59', 'None', 'у Эрика дома'),
        Schedule((3, 6, 0), '0:0', '5:59', 'None', 'у Эрика дома'),
        )
    return


################################################################################

label set_eric_schedule:
    if 'eric' not in chars:
        return
    # полностью очистим расписание
    $ eric.plan = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]

    # добавим базовое расписание
    $ eric.add_schedule(
        Schedule((4,), '0:00', '5:59', 'sleep2', 'спит с Анной', 'house', 2, 'eric_ann_sleep', enabletalk=False, glow=110),
        Schedule((2, 5), '0:00', '1:59', 'sleep2', 'спит с Анной', 'house', 2, 'eric_ann_sleep', enabletalk=False, glow=110),
        # Эрик пользует Киру
        Schedule((2, 5), '2:00', '2:29', 'sleep2', 'спит с Анной', 'house', 2, 'eric_ann_sleep', variable="not wcv.catch_Kira.stage", enabletalk=False, glow=110),
        Schedule((2, 5), '2:00', '2:29', 'fuck',  'Кира делает Эрику минет', 'house', 3, 'kira_bath_with_eric', variable="wcv.catch_Kira.stage and not flags.eric_jerk", enabletalk=False, glow=140),
        Schedule((2, 5), '2:00', '2:29', 'sleep2', 'спит с Анной', 'house', 2, 'eric_ann_sleep', variable="wcv.catch_Kira.stage and flags.eric_jerk", enabletalk=False, glow=110),
        # конец блока
        Schedule((2, 5), '2:30', '5:59', 'sleep2', 'спит с Анной', 'house', 2, 'eric_ann_sleep', enabletalk=False, glow=110),
        Schedule((2, 4, 5), '6:00', '6:59', 'shower2', 'в душе с Анной', 'house', 3, 'eric_ann_shower', enabletalk=False, glow=130),
        Schedule((1, 3, 4), '19:00', '19:59', 'dinner', 'семейный ужин', 'house', 5, 'dinner', enabletalk=False, glow=105),
        Schedule((6,), '19:00', '19:59', 'dinner', _('семейный ужин'), 'house', 5, 'dinner', enabletalk=False, glow=105, variable="Eric_at_dinner()"),
        Schedule((6,), '19:00', '19:59', 'None', variable="not Eric_at_dinner()"),
        # Эрик ведёт блог с Алисой
        Schedule((3,), '20:00', '20:59', 'rest', 'в Аниной комнате', 'house', 2, 'eric_resting', variable="not alice.dcv.intrusion.enabled"),
        Schedule((3,), '20:00', '20:59', 'blog', "блог с Эриком", 'house', 1, 'blog_with_Eric', variable="alice.dcv.intrusion.enabled", enabletalk=False, glow=150),
        # конец блока
        Schedule((1, 4), '20:00', '20:59', 'rest', 'в Аниной комнате', 'house', 2, 'eric_resting'),
        Schedule((1, 3, 4), '21:00', '21:59', 'tv2', 'смотрит ТВ с Анной', 'house', 4, 'eric_ann_tv', enabletalk=False, glow=150),
        # блок секс.обучения Лизы
        Schedule((1,), '22:00', '22:29', 'fuck', 'трахает Анну в её комнате', 'house', '2', 'eric_ann_fucking', variable="not lisa.dcv.intrusion.stage", enabletalk=False, glow=150),
        Schedule((1,), '22:00', '22:29', 'sexed_lisa', 'АиЭ учат Лизу. Вводный урок', 'house', 2, 'sexed_lisa', variable="lisa.dcv.intrusion.stage and flags.lisa_sexed<0", enabletalk=False, glow=120),
        Schedule((1,), '22:00', '22:29', 'sexed_lisa', 'АиЭ учат Лизу', 'house', 2, 'sexed_lisa', variable="0<=flags.lisa_sexed<4", enabletalk=False, glow=180),
        Schedule((1,), '22:00', '22:29', 'fuck', 'трахает Анну в её комнате', 'house', '2', 'eric_ann_fucking', variable="flags.lisa_sexed>=4", enabletalk=False, glow=150),
        # конец блока
        Schedule((1,), '22:30', '23:59', 'fuck', 'трахает Анну в её комнате', 'house', '2', 'eric_ann_fucking', enabletalk=False, glow=150),
        Schedule((3, 4), '22:00', '23:59', 'fuck', 'трахает Анну в её комнате', 'house', '2', 'eric_ann_fucking', enabletalk=False, glow=150),
        )

    return


################################################################################

label set_kira_schedule:
    if 'kira' not in chars:
        return
    # полностью очистим расписание
    $ kira.plan = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]

    # добавим базовое расписание
    $ kira.add_schedule(
        Schedule((0, 1, 3, 4), '0:00', '2:59', 'studio', 'в студии'),
        Schedule((2, 5), '0:00', '1:59', 'studio', 'в студии'),
        # Эрик пользует Киру
        Schedule((2, 5), '2:00', '2:29', 'bath',  'принимает ванну', 'house', 3, 'kira_bath', variable="not wcv.catch_Kira.stage", enabletalk=False, glow=125),
        Schedule((2, 5), '2:00', '2:29', 'bath',  'Кира делает Эрику минет', 'house', 3, 'kira_bath_with_eric', variable="wcv.catch_Kira.stage and not flags.eric_jerk", enabletalk=False, glow=140),
        Schedule((2, 5), '2:00', '2:29', 'bath',  'принимает ванну', 'house', 3, 'kira_bath', variable="wcv.catch_Kira.stage and flags.eric_jerk", enabletalk=False, glow=125),
        # конец блока
        Schedule((2, 5), '2:30', '2:59', 'bath',  'принимает ванну', 'house', 3, 'kira_bath', enabletalk=False, glow=125),
        Schedule((1, 4), '3:00', '3:59', 'night_swim', 'ночное купание', 'house', 6, 'kira_night_swim', enabletalk=False, glow=125),
        Schedule((2, 5), '3:00', '5:59', 'sleep', 'спит в гостиной (ночь)', 'house', 4, 'kira_sleep_night', enabletalk=False, glow=110),
        Schedule((2, 5), '6:00', '6:59', 'sleep', 'спит в гостиной (утро)', 'house', 4, 'kira_sleep_morning', enabletalk=False, glow=115),
        Schedule((6,), '0:00', '2:59', 'None', variable="flags.noclub"),
        Schedule((6,), '0:00', '2:59', 'nightclub', 'в ночном клубе с Алисой', variable="not flags.noclub"),
        Schedule((6,), '3:00', '3:59', 'None', variable="flags.noclub"),
        Schedule((6,), '3:00', '3:59', 'return', 'возвращение из ночного клуба', 'house', 6, 'return_from_club', variable="not flags.noclub", enabletalk=False, glow=130),
        Schedule((0, 3), '3:00', '3:59', 'night_tv', 'ночной просмотр порно', 'house', 4, 'kira_night_tv', enabletalk=False, glow=110),
        Schedule((0, 1, 3, 4, 6), '4:00', '5:59', 'sleep', 'спит в гостиной (ночь)', 'house', 4, 'kira_sleep_night', enabletalk=False, glow=110),
        Schedule((0, 1, 3, 4, 6), '6:00', '7:59', 'sleep', 'спит в гостиной (утро)', 'house', 4, 'kira_sleep_morning', enabletalk=False, glow=115),
        Schedule((1, 4), '8:00', '8:59', 'shower', 'одна в душе', 'house', 3, 'kira_shower', enabletalk=False, glow=120),
        Schedule((2, 5), '7:00', '7:59', 'shower', 'в душе с Лизой', 'house', 3, 'kira_lisa_shower', enabletalk=False, glow=135),
        Schedule((2, 5), '8:00', '8:59', 'swim', 'в бассейне', 'house', 6, 'kira_swim', enabletalk=False, glow=105),
        Schedule((0, 3, 6), '8:00', '8:59', 'shower', 'в душе с Алисой', 'house', 3, 'kira_alice_shower', enabletalk=False, glow=140),
        Schedule((0, 1, 2, 3, 4, 5, 6), '9:00', '9:59', 'breakfast', 'семейный завтрак', 'house', 5, 'breakfast', enabletalk=False, glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '10:00', '10:59', 'swim', 'в бассейне', 'house', 6, 'kira_swim', glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '11:00', '12:59', 'sun', 'загорает', 'house', 6, 'kira_sun', glow=120),
        Schedule((0, 1, 2, 3, 4, 5, 6), '13:00', '23:59', 'studio', 'в студии'),
        )

    return


################################################################################

label set_lisa_schedule:
    # полностью очистим расписание
    $ lisa.plan = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]

    $ lisa.add_schedule(
        # если пришла Оливия, смотрим ТВ
        Schedule((6,), '0:00', '1:59', 'tv2', "смотрит ТВ с Оливией", 'house', 4, 'olivia_lisa_tv',  variable="olivia_night_visits", enabletalk=False, glow=140),
        Schedule((6,), '2:00', '5:59', 'sleep2', "спит с Оливией", 'house', 0, 'olivia_lisa_sleep',  variable="olivia_night_visits", enabletalk=False, glow=130),

        Schedule((6,), '0:00', '1:59', 'sleep', "спит (ночь)", 'house', 0, 'lisa_sleep_night',  variable="not olivia_night_visits", enabletalk=False, glow=102),
        Schedule((6,), '2:00', '5:59', 'sleep', "спит (ночь)", 'house', 0, 'lisa_sleep_night',  variable="not olivia_night_visits", enabletalk=False, glow=102),
        Schedule((0, 1, 2, 3, 4, 5), '0:0', '5:59', 'sleep', "спит (ночь)", 'house', 0, 'lisa_sleep_night', enabletalk=False, glow=102),
        # конец блока
        Schedule((0, 1, 2, 3, 4, 5, 6), '6:0', '6:59', 'sleep', "спит (утро)", 'house', 0, 'lisa_sleep_morning', enabletalk=False, glow=102),
        # одна в душе
        Schedule((0, 3, 6), '7:00', '7:59', 'shower', "принимает душ", 'house', 3, 'lisa_shower', enabletalk=False, glow=120),
        # если приехала Кира, в душе не одна
        Schedule((1, 4), '7:00', '7:59', 'shower', "принимает душ", 'house', 3, 'lisa_shower', variable="'kira' not in chars", enabletalk=False, glow=120),
        Schedule((1, 4), '7:00', '7:59', 'shower', 'в душе с Алисой', 'house', 3, 'alice_lisa_shower', variable="'kira' in chars", enabletalk=False, glow=135),
        Schedule((2, 5), '7:00', '7:59', 'shower', "принимает душ", 'house', 3, 'lisa_shower', variable="'kira' not in chars", enabletalk=False, glow=120),
        Schedule((2, 5), '7:00', '7:59', 'shower', 'в душе с Кирой', 'house', 3, 'kira_lisa_shower', variable="'kira' in chars", enabletalk=False, glow=135),
        # конец блока
        Schedule((0, 1, 2, 3, 4, 5, 6), '8:0', '8:59', 'read', "читает", 'house', 0, 'lisa_read', talklabel='lisa_read_closer', glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '9:0', '9:59', 'breakfast', "семейный завтрак", 'house', 5, 'breakfast', enabletalk=False, glow=105),
        Schedule((1, 2, 3, 4, 5), '10:0', '10:59', 'dressed', "одевается в школу", 'house', 0, 'lisa_dressed_school', enabletalk=False, glow=110),
        Schedule((6, ), '10:0', '10:59', 'dressed', "одевается в магазин", 'house', 0, 'lisa_dressed_shop', enabletalk=False, glow=110),
        # в случае репетитора (мягкие меры Эрика) расписание Лизы не меняется)
        Schedule((0, ), '10:0', '10:59', 'dressed', "одевается к репетитору", 'house', 0, 'lisa_dressed_repetitor', enabletalk=False, glow=110),
        Schedule((0, ), '11:0', '14:59', 'at_tutor', "у репетитора"),
        # конец блока
        Schedule((1, 2, 3, 4, 5), '11:0', '15:59', 'in_shcool', "в школе"),
        Schedule((6, ), '11:0', '13:59', 'in_shop', "в магазине"),
        Schedule((6, ), '14:0', '14:59', 'read', "читает", 'house', 0, 'lisa_read', glow=105),
        Schedule((0, 6), '15:0', '15:59', 'swim', "в бассейне", 'house', 6, 'lisa_swim', glow=105),
        # доп.курсы Лизы по будния (жёсткие меры Эрика)
        Schedule((1, 2, 3, 4, 5), '16:0', '16:59', 'swim', "в бассейне", 'house', 6, 'lisa_swim', variable="lisa.dcv.battle.stage not in [3, 6] and not olivia_visits()", glow=105),
        Schedule((1, 2, 3, 4, 5), '16:0', '16:59', 'sun', "загорает с Оливией", 'house', 6, 'olivia_lisa_sun', variable="lisa.dcv.battle.stage not in [3, 6] and olivia_visits()", glow=130),
        Schedule((1, 2, 3, 4, 5), '16:0', '16:59', 'on_courses', "на курсах", variable="lisa.dcv.battle.stage in [3, 6]"),

        Schedule((1, 2, 3, 4, 5), '17:0', '17:59', 'sun', "загорает", 'house', 6, 'lisa_sun', variable="lisa.dcv.battle.stage not in [3, 6] and not olivia_visits()", glow=110),
        Schedule((1, 2, 3, 4, 5), '17:0', '17:59', 'sun', "загорает с Оливией", 'house', 6, 'olivia_lisa_sun', variable="olivia_visits()", glow=130),
        Schedule((1, 2, 3, 4, 5), '17:0', '17:59', 'swim', "в бассейне", 'house', 6, 'lisa_swim', variable="lisa.dcv.battle.stage in [3, 6] and not olivia_visits()", glow=105),

        Schedule((1, 2, 3, 4, 5), '18:0', '18:59', 'swim', "в бассейне с Оливией", 'house', 6, 'olivia_lisa_swim', variable="olivia_visits()", glow=130),
        Schedule((1, 2, 3, 4, 5), '18:0', '18:59', 'sun', "загорает", 'house', 6, 'lisa_sun', variable="lisa.dcv.battle.stage not in [3, 6] and not olivia_visits()", glow=110),
        Schedule((1, 2, 3, 4, 5), '18:0', '18:59', 'sun', "загорает", 'house', 6, 'lisa_sun', variable="lisa.dcv.battle.stage in [3, 6] and not olivia_visits()", glow=110),
        # конец блока
        Schedule((6, 0), '16:0', '16:59', 'sun', "загорает", 'house', 6, 'lisa_sun', glow=110),
        Schedule((0, 6), '17:0', '18:59', 'read', "читает", 'house', 0, 'lisa_read', glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '19:0', '19:59', 'dinner', "семейный ужин", 'house', 5, 'dinner', enabletalk=False, glow=105),
        Schedule((0, 1, 2, 3, 4, 5, 6), '20:0', '20:59', 'dishes', "моет посуду", 'house', 4, 'lisa_dishes', talklabel='lisa_dishes_closer'),
        Schedule((0, 1, 2, 3, 4, 5, 6), '21:0', '21:59', 'phone', "лежит с телефоном", 'house', 0, 'lisa_phone', glow=105),
        # блок секс.обучения Лизы
        Schedule((1, ), '22:0', '22:29', 'bath', "принимает ванну", 'house', 3, 'lisa_bath', variable="not lisa.dcv.intrusion.stage", enabletalk=False, glow=120),
        Schedule((1, ), '22:00', '22:29', 'sexed_lisa', 'АиЭ учат Лизу. Вводный урок', 'house', 2, 'sexed_lisa', variable="lisa.dcv.intrusion.stage and flags.lisa_sexed<0", enabletalk=False, glow=120),
        Schedule((1, ), '22:00', '22:29', 'sexed_lisa', 'АиЭ учат Лизу', 'house', 2, 'sexed_lisa', variable="0<=flags.lisa_sexed<4", enabletalk=False, glow=180),
        Schedule((1, ), '22:0', '22:29', 'bath', "принимает ванну", 'house', 3, 'lisa_bath', variable="flags.lisa_sexed>=4", enabletalk=False, glow=120),
        # конец блока
        Schedule((1, ), '22:30', '22:59', 'bath', "принимает ванну", 'house', 3, 'lisa_bath', enabletalk=False, glow=120),
        Schedule((0, 2, 3, 4, 5, 6), '22:0', '22:59', 'bath', "принимает ванну", 'house', 3, 'lisa_bath', enabletalk=False, glow=120),
        Schedule((1, 2, 3, 4, 5), '23:0', '23:59', 'homework', "учит уроки", 'house', 0, 'lisa_homework', glow=105),
        Schedule((0, 6), '23:0', '23:59', 'phone', "лежит с телефоном", 'house', 0, 'lisa_phone', glow=105),
        )

    return


################################################################################

label set_olivia_shedule:
    if 'olivia' not in chars:
        return

    $ olivia.plan = [Schedule((0, 1, 2, 3, 4, 5, 6), '0:00', '23:59', 'None')]

    $ olivia.add_schedule(
        Schedule((6,), '0:00', '1:59', 'tv2', "смотрит ТВ с Оливией", 'house', 4, 'olivia_lisa_tv',  variable="olivia_night_visits", enabletalk=False, glow=140),
        Schedule((6,), '2:00', '5:59', 'sleep2', "спит с Оливией", 'house', 0, 'olivia_lisa_sleep',  variable="olivia_night_visits", enabletalk=False, glow=130),
        Schedule((6,), '0:00', '1:59', 'sleep', "спит y себя дома",  variable="not olivia_night_visits"),
        Schedule((6,), '2:00', '5:59', 'sleep', "спит y себя дома",  variable="not olivia_night_visits"),

        Schedule((1, 2, 3, 4, 5), '11:0', '15:59', 'in_shcool', "в школе"),

        Schedule((1, 2, 3, 4, 5), '16:0', '16:59', 'sun', "загорает с Лизой", 'house', 6, 'olivia_lisa_sun', variable="lisa.dcv.battle.stage not in [3, 6] and olivia_visits()", glow=130),
        Schedule((1, 2, 3, 4, 5), '16:0', '16:59', 'at_home', "у себя дома", variable="lisa.dcv.battle.stage in [3, 6] or not olivia_visits()"),
        Schedule((1, 2, 3, 4, 5), '17:0', '17:59', 'sun', "загорает с Лизой", 'house', 6, 'olivia_lisa_sun', variable="olivia_visits()", glow=130),
        Schedule((1, 2, 3, 4, 5), '17:0', '17:59', 'at_home', "у себя дома", variable="not olivia_visits()"),
        Schedule((1, 2, 3, 4, 5), '18:0', '18:59', 'swim', "в бассейне с Оливией", 'house', 6, 'olivia_lisa_swim', variable="olivia_visits()", glow=130),
        Schedule((1, 2, 3, 4, 5), '18:0', '18:59', 'at_home', "у себя дома", variable="not olivia_visits()"),
        )

    return
