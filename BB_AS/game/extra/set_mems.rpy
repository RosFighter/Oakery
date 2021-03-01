init python:
    import copy

    def get_lisa_dress(st='', tp='casual'):
        if tp == 'learn':
            dr_l = ['c', 'd'] if 'kira' in persistent.mems_var else ['c']
        elif tp == 'sleep':
            dr_l = ['b']
        else:
            dr_l = ['d'] if 'kira' in persistent.mems_var else ['a']

        if 'bathrobe' in persistent.mems_var:
            dr_l.append('b')

        if st!='':
            if type(st)==list:
                dr_l.extend(st)
            else:
                dr_l.append(st)

        # if tp != '':
        #     print(dr_l)
        return renpy.random.choice(dr_l)


    def get_max_dress(st='', ex=''):
        dr_m = ['c'] if 'kira' in persistent.mems_var else ['a']
        if 'max-a' in persistent.mems_var:
            dr_m.append('b')
        if st!='':
            if type(st)==list:
                dr_m.extend(st)
            else:
                dr_m.append(st)
        # print dr_m
        dr_m = list(set(dr_m))
        if ex!='':
            if type(ex)==list:
                for j in ex:
                    if j in dr_m:
                        dr_m.remove(j)
            else:
                if ex in dr_m:
                    dr_m.remove(ex)

        # print dr_m
        return renpy.random.choice(dr_m)

    ############################################################################

    # Новый купальник Лизы
    def set_gift_swimsuit():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.plan_name = renpy.random.choice(['sun', 'read'])
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = renpy.random.choice(['a', 'b']) if 'max-a' in persistent.mems_var else 'a'
        my_scope = {
                'lisa' : tl,
                'flags': {'promise_kiss':True},
                'mgg'         : mg,
            }
        return my_scope

    # Извинительная пижамка для Алисы
    def set_gift_pajamas():
        sg = {'alice': SorryGift()}
        sg['alice'].give = sorry_gifts['alice'].give.copy()
        sg['alice'].owe = True
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.plan_name = renpy.random.choice(['sun', 'resting'])
        if al.plan_name != 'sun':
            al.dress = renpy.random.choice(['a', 'd']) if 'kira' in persistent.mems_var else 'a'
            _tm = renpy.random.choice(['10:20', '21:00'])
        else:
            al.dress = 'a'
            _tm = '15:30'

        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.append('nopants')
        if 'alice_not_nopants' in persistent.mems_var:
            sm.append('not_nopants')
        smoke = renpy.random.choice(sm)
        fl = {
                'alice_hugs': 4,
                'smoke': smoke if al.dress=='a' else ''
            }

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()

        my_scope = {
                'sorry_gifts' : sg,
                'alice'       : al,
                'flags'       : fl,
                'tm'          : _tm,
                'talk_var'    : {'sun_oiled': 0},
                'mgg'         : mg,
                'pose2_2'     : renpy.random.choice(['01', '02']),
                'pose3_2'     : renpy.random.choice(['01', '02', '03']),
            }
        return my_scope

    # Тёмное кружево
    def set_gift_black_lingerie():
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.plan_name = renpy.random.choice(['sun', 'resting'])
        if al.plan_name != 'sun':
            dress = ['a', 'd'] if 'kira' in persistent.mems_var else ['a']
            _tm = renpy.random.choice(['10:20', '21:00'])
            if 'pajamas' in alice.gifts:
                dress.append('b')
            al.dress = renpy.random.choice(dress)
        else:
            al.dress = 'a'
            _tm = '15:30'

        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.append('nopants')
        if 'alice_not_nopants' in persistent.mems_var:
            sm.append('not_nopants')
        smoke = renpy.random.choice(sm)
        fl = {
                'smoke': smoke if al.dress=='a' else ''
            }

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 45.0

        my_scope = {
                'alice'       : al,
                'flags'       : fl,
                'tm'          : _tm,
                'talk_var'    : {'sun_oiled': 0},
                'mgg'         : mg,
            }
        return my_scope

    ############################################################################

    # Давай я нанесу крем
    def set_sunscreen():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c' if 'kira' in persistent.mems_var else 'b'
        mg.social = 100
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        tdcv = {'eric.lingerie':Daily()}
        if renpy.seen_label('massage_sunscreen.hips'):
            tdcv['eric.lingerie'].stage = 7

        my_scope = {
            'alice'          : al,
            'talk_var'       : {'sun_oiled':1},
            'dcv'            : tdcv,
            'online_cources' : copy.deepcopy(online_cources),
            'mgg'            : mg,
            '_massaged'      : [],
            '_talk_top'      : False,
            'tm'             : '15:00',
            'house'          : copy.deepcopy(house),
            'items'          : {"spider" : Item("", "", "spider", None)},
            'infl'           : {al:Influence()}
            }
        return my_scope

    # Ножкам приятно
    def set_talk_tv():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 100
        mg.massage = 100

        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        dr_var = [0,]
        if 'alice_nopants' in persistent.mems_var:
            dr_var.append(1)
        if 'alice_not_nopants' in persistent.mems_var:
            dr_var.append(2)
        if 'pajamas' in alice.gifts:
            dr_var.append(3)
        if 'smoke_nojeans' in persistent.mems_var and renpy.random.choice([False, True]):
            dr_var.append(4)
        if 'kira' in persistent.mems_var:
            dr_var.append(5)
        # print(dr_var)
        # renpy.random.shuffle(dr_var)
        var = renpy.random.choice(dr_var)
        # print(var)
        al.dress, smoke = {
                0 : ('a', ''),
                1 : ('a', 'nopants'),
                2 : ('a', 'not_nopants'),
                3 : ('b', ''),
                4 : ('c', 'nojeans'),
                5 : ('d', ''),
            }[var]
        # print(dr_var, var, al.dress, smoke)

        my_scope = {
                'tm'        : '22:00',
                'mgg'       : mg,
                'talk_var'  : {'al.tv.mas' : 0, 'al.tvgood':3},
                'flags'     : {'alice.tv.mass':7, 'smoke':smoke, 'double_mass_alice':0},
                'dcv'       : {'tvchoco' : Daily(done=renpy.random.choice([False, True]), enabled=True)},
                'kol_choco' : 5,
                'pose3_2'   : renpy.random.choice(['01', '02', '03']),
                'alice'     : al,
                'house'     : copy.deepcopy(house),
            }
        return my_scope

    # Помассирую не только ножки
    def set_advanced_massage1():

        my_scope = {
                'tm'        : '22:00',
                'flags'     : {'double_mass_alice':renpy.random.randint(1, 2)},
                '_drink'    : 2,
                '_ch20'     : Chance(700),
                '_ch25'     : Chance(875),
                '_pose'     : renpy.random.choice(['03', '04']),
                '_dress'    : (renpy.random.choice(['b','c']) if 'max-a' in persistent.mems_var else 'c') + renpy.random.choice((['b', 'c', 'd'] if 'pajamas' in alice.gifts else ['c', 'd']))
            }
        return my_scope

    # Первый массаж ног
    def set_foot_mass():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress('a')

        my_scope = {
                'pose3_1' : renpy.random.choice(['01', '02', '03']),
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope

    # Внимание к пальчикам
    def set_hand_mass():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        my_scope = {
                'talk_var' : {'kissingmassage':False},
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope

    # Разомнём и плечики
    def set_shoulders_mass():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        my_scope = {
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope

    # Массаж для любимой тёти
    def set_kira_bathmass():

        my_scope = {
            'talk_var' : {'kira.porn': 1, 'lisa.footmass': 1, 'kira.bath.mass':0},
            }
        return my_scope

    # Совсем другой массаж
    def set_kira_bathfj():
        mg        = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        mg.sex    = 7

        my_scope = {
            'talk_var' : {'kira.tv.touch': 1, 'teachkiss':2},
            'flags'    : {'kira.tv.bj': False, 'promise.cuni.kira':renpy.random.choice([True, False]), 'hj_in_pool':renpy.random.choice([1, 2])},
            'memes'    : 1,
            'mgg'      : mg,
            }
        return my_scope

    ############################################################################

    # Ночные страхи
    def set_spider_in_bed():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.mood = 250
        # вписать бельё
        al.dress = renpy.random.choice(['a', 'b']) if 'black_linderie' in persistent.mems_var else 'a'

        sm = [None, None]
        if 'alice_sleeptoples' in persistent.mems_var:
            sm.extend(['sleep', 'not_sleep'])
        if 'alice_sleepnaked' in persistent.mems_var:
            sm.extend(['naked', 'not_naked'])
        sm = renpy.random.choice(sm)
        smr = None if sm is None else {'sleep':'sleep', 'not_sleep':'sleep', 'naked':'naked', 'not_naked':'naked'}[sm]
        my_scope = {
            'talk_var' : {'smoke': ''},
            'flags'    : {'smoke': sm, 'smoke.request':smr ,'noted': False},
            'mgg'      : mg,
            'tm'       : '02:30',
            'alice'    : al,
            }
        return my_scope

    # Кто это там ползёт
    def set_spider_massage():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c'

        my_scope = {
            'talk_var' : {'sun_oiled': renpy.random.choice([1, 2])},
            'mgg'      : mg,
            'tm'       : '15:00'
            }
        return my_scope

    # Монстр в ванной комнате
    def set_spider_shower():
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.mood = 250
        al.relmax = 500

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 100

        my_scope = {
            'tm'       : '15:00',
            'alice'    : al,
            'mgg'      : mg,
            'chars'    : {'alice': al}
            }
        return my_scope

    # После клуба
    def set_after_club():
        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.extend(['nopants', 'not_nopants'])
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")

        my_scope = {
            'talk_var' : {'smoke': ''},
            'flags'    : {'smoke': renpy.random.choice(sm), 'noted': False},
            'tm'       : '03:00',
            'alice'    : al,
            }
        return my_scope

    # Я была плохой девочкой
    def set_after_club_next1():
        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.extend(['nopants', 'not_nopants'])
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")

        my_scope = {
            'talk_var'  : {'smoke': '', 'teachkiss':(4 if 'kira_tv_bj' in persistent.memories and persistent.memories['kira_tv_bj']>0 else 3)},
            'flags'     : {'smoke': renpy.random.choice(sm), 'noted': False, 'double_mass_alice':(2 if 'double_mass_alice' in persistent.mems_var else 0)},
            'tm'        : '03:00',
            'alice'     : al,
            'spent_time': 0,
            }
        return my_scope

    ############################################################################

    # Смотрим порно вместе с тётей
    def set_porn_tv():
        tk = Profile("Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'
        my_scope = {
            'talk_var' : {'kira.porn' : 2, 'kira.bath.mass':True},
            'flags'    : {'kira.tv.bj' : False, 'promise.cuni.kira':renpy.random.choice([True, False])},
            'kira'     : tk,
            }
        return my_scope

    # Первый урок поцелуев
    def set_kira_kiss_01():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.kissing = 0

        my_scope = {
            'mgg'      : mg,
            }
        return my_scope

    # А это уже совсем не массаж!
    def set_kira_bathbj():
        mg        = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        mg.sex    = 7

        my_scope = {
            'talk_var' : {'kira.tv.touch': 2, 'teachkiss':2},
            'flags'    : {'kira.tv.bj': True, 'promise.cuni.kira':renpy.random.choice([True, False]), 'hj_in_pool':renpy.random.choice([1, 2])},
            'memes'    : 2,
            'mgg'      : mg,
            }
        return my_scope

    # Второй урок поцелуев
    def set_kira_kiss_02():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.kissing = 1.1
        mg.social = 100

        my_scope = {
            'talk_var': {'teachkiss': 2, 'kira.bath.mass': 1 if 'kira.bath.mass' in persistent.mems_var else 0},
            'mgg'      : mg,
            }
        return my_scope

    # Третий урок поцелуев
    def set_kira_kiss_03():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = 7

        my_scope = {
            'flags'    : {'kira.bath.fj': True, 'kira.tv.bj': renpy.random.choice([True, False]), 'hj_in_pool':renpy.random.randint(0, 2)},
            'mgg'      : mg,
            }
        return my_scope

    # Горячее, чем порно
    def set_porn_tv2():
        tk = Profile("Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = 7
        my_scope = {
            'talk_var' : {'kira.porn' : 2, 'kira.bath.mass':True},
            'flags'    : {'kira.tv.bj' : True, 'hj_in_pool':2},
            'kira'     : tk,
            'mgg'      : mg,
            }
        return my_scope

    # Небольшое приключение перед сном
    def set_night_swim():

        my_scope = {
                'flags' : {'hj_in_pool':renpy.random.randint(1, 2), 'promise.cuni.kira':False, 'kira.tv.bj':True},
        }
        return my_scope

    # Не зря купил сорочку

    # С меня приятный должок

    ############################################################################

    # Вкусные уроки с сестрёнкой
    def set_lisa_advanced_kiss_lesson():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.kissing = 6.0

        my_scope = {
                'lisa'      : tl,
                'mgg'       : mg,
                'spent_time': 0,
            }
        return my_scope

    # Кажется, мы что-то забыли
    def set_kiss_massage1():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.kissing = 6.0

        my_scope = {
                'talk_var' : {'kissingmassage':True},
                'lisa'     : tl,
                'mgg'      : mg,
            }
        return my_scope

    ############################################################################

    # Больше, чем помощь с домашним заданием
    def set_homework_mass_01():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 45.0
        mg.massage = 19.1

        my_scope = {
                'pose3_1' : renpy.random.choice(['01', '02', '03']),
                'lisa'    : tl,
                'mgg'     : mg,
            }
        return my_scope

    # Ужастики в обнимку с Лизой
    def set_horor_01():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress  = 'b' # get_lisa_dress(tp='sleep')
        mg        = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex    = 9

        my_scope = {
            'lisa'     : tl,
            'mgg'      : mg,
            'flags'    : {
                        'cur_series' : renpy.random.randint(1, 2),
                        'cur_movies' : [
                                        renpy.random.choice(['hes', 'f13']),
                                        renpy.random.randint(0, 4),
                                        renpy.random.randint(0, 4),
                                        ],
                        },
            'talk_var' : {'kiss_lessons': (12 if 'horror_kiss' in persistent.mems_var else 6)},
            }
        return my_scope

    # Порно-портфолио для Киры
    def set_kira_photoset_01():
        # [items['photocamera'].have, items['nightie2'].have, GetWeekday(day)==6]
        itm = {
            "photocamera": Item(_("ФОТОАППАРАТ"), have=True),
            "nightie2"   : Item(_("КОРОТКАЯ ПИКАНТНАЯ СОРОЧКА"), have=True),
            }
        my_scope = {
                'items' : itm,
                'day'   : 32,
            }
        return my_scope

    # Немного БДСМ от Киры

    # Первые снимки для блога Алисы
    def set_alice_body_photoset1():
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b'])

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')

        my_scope = {
                'dcv'           : {
                                    'alice.secret' : Daily(done=True),
                                    'gift.lingerie': Daily(),
                                },
                'cam_pose_blog' : '',
                'tm'            : '20:30',
                'spent_time'    : 0,
                'peeping'       : {'alice_blog':0},
                'alice'         : al,
                'mgg'           : mg,
                'items'         : {'sexbody1':Item("ЧЁРНОЕ СЕКСУАЛЬНОЕ БОДИ", have=True)},
                'expected_photo': [],
            }

        if 'alice_photoset1' in persistent.mems_var:
            my_scope['flags'] = {'alice.drink': True}
        else:
            my_scope['flags'] = {'alice.drink': False}

        return my_scope

    # Я обошёл Эрика с подарком для Алисы
    def set_gift_lace_lingerie():
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b'])

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.stealth = 28.7

        tdcv = {
                'alice.secret' : Daily(done=True),
                'gift.lingerie': Daily(),
                'eric.lingerie': Daily(3, enabled=True),
            }
        tdcv['eric.lingerie'].stage = 3
        tdcv['gift.lingerie'].stage = 2
        # all([not dcv['eric.lingerie'].done, dcv['eric.lingerie'].lost<5, items['sexbody2'].have])
        my_scope = {
                'dcv'           : tdcv,
                'cam_pose_blog' : '',
                'tm'            : '20:30',
                'peeping'       : {'alice_blog':0},
                'spent_time'    : 0,
                'alice'         : al,
                'items'         : {
                                    'sexbody1':Item("ЧЁРНОЕ СЕКСУАЛЬНОЕ БОДИ"),
                                    'sexbody2':Item("ЧЁРНОЕ КРУЖЕВНОЕ БОДИ", have=True)
                                },
                'mgg'           : mg,
            }

        if 'alice_photoset1' in persistent.mems_var:
            my_scope['flags'] = {'alice.drink': True}
        else:
            my_scope['flags'] = {'alice.drink': False}
        return my_scope

    # Я принес тебе полотенце!
    def set_alice_towel_after_club():
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.gifts.append('sexbody1')
        # all(['sexbody1' in alice.gifts, flags['alice.nakedpunish']])
        # 'bath_tongue' - dcv['eric.lingerie'].stage in [5, 7]
        tdcv = {
                'eric.lingerie': Daily(),
            }
        tdcv['eric.lingerie'].stage = 7 if 'bath_tongue' in persistent.mems_var else 0
        my_scope = {
                'flags' : {'alice.drink' : 2, 'alice.nakedpunish':True},
                'tm'    : '03:15',
                'alice' : al,
                'dcv'   : tdcv,
            }
        return my_scope

    # Стриптиз после клуба
    def set_kira_strip_01():

        tdcv = {'kiratalk':Daily()}
        tdcv['kiratalk'].stage = 6 if 'strip.show' in persistent.mems_var else 5
        my_scope = {
                'dcv'   : tdcv,
                'tm'    : '03:10',
                'flags' : {
                            'alice.drink' : renpy.random.choice([0, 1]),
                            'kira.tv.bj'  : True,
                            'strip.show'  : False,
                        },
                'kira'  : Profile("Кира", "Киры", "Кире", "Киру", "Кирой", "Кире"),
            }
        return my_scope

    ############################################################################

    # Урок по минету от мамы и Эрика
    # Так близко к маминой попке
    # Глубокий минет в мамином исполнении
    def set_lessons_Eric_01():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()

        my_scope = {
                'mgg'       : mg,
                '_stockings' : RandomChance(500),
            }
        return my_scope

    ############################################################################

    # Её первые познания...
    # Как возбудить ещё больше?
    # Нежно и аккуратно!
    # Как долго это нужно делать?
    def set_sexed_01():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        te = Profile("Эрик", "Эрика", "Эрику", "Эрика", "Эриком", "Эрике")
        te.dress = renpy.random.choice(['a', 'b'])

        my_scope = {
            'eric' : te,
            'lisa' : tl,
            }
        return my_scope

    # Кружевное боди для Алисы от Эрика
    def set_blog_with_Eric_01():

        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b', 'c'])

        te = Profile("Эрик", "Эрика", "Эрику", "Эрика", "Эриком", "Эрике")
        te.dress = renpy.random.choice(['a', 'b'])

        my_scope = {
                'peeping'    : {
                                'alice_blog'     : 0,
                                'blog_with_eric' : 0,
                                },
                'spent_time' : 0,
                'tm'         : '20:20',
                'alice'      : al,
                'eric'       : te,
            }
        return my_scope
