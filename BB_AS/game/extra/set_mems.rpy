init python:

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
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.plan_name = renpy.random.choice(['sun', 'read'])
        tl.flags.promise = True
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = renpy.random.choice(['a', 'b']) if 'max-a' in persistent.mems_var else 'a'
        my_scope = {
                'lisa' : tl,
                'mgg'         : mg,
            }
        return my_scope

    # Извинительная пижамка для Алисы
    def set_gift_pajamas():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.plan_name = renpy.random.choice(['sun', 'resting'])
        if al.plan_name != 'sun':
            al.dress = renpy.random.choice(['a', 'd']) if 'kira' in persistent.mems_var else 'a'
            _tm = renpy.random.choice(['10:20', '21:00'])
        else:
            al.dress = 'a'
            _tm = '15:30'
        al.sorry.owe = True
        al.flags.hugs_type = 4
        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.append('nopants')
        if 'alice_not_nopants' in persistent.mems_var:
            sm.append('not_nopants')
        smoke = renpy.random.choice(sm)
        al.req.result = smoke if al.dress=='a' else ''

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()

        my_scope = {
                'tm'          : _tm,
                'mgg'         : mg,
                'alice'       : al,
                'pose2_2'     : renpy.random.choice(['01', '02']),
                'pose3_2'     : renpy.random.choice(['01', '02', '03']),
            }
        return my_scope

    # Тёмное кружево
    def set_gift_black_lingerie():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.plan_name = renpy.random.choice(['sun', 'resting'])
        if al.plan_name != 'sun':
            dress = ['a', 'd'] if 'kira' in persistent.mems_var else ['a']
            _tm = renpy.random.choice(['10:20', '21:00'])
            if 'pajamas' in persistent.mems_var:
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
        al.req.result = smoke if al.dress=='a' else ''

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 45.0

        my_scope = {
                'tm'          : _tm,
                'alice'       : al,
                'mgg'         : mg,
            }
        return my_scope

    ############################################################################

    # Давай я нанесу крем
    def set_sunscreen():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c' if 'kira' in persistent.mems_var else 'b'
        mg.social = 100
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        if renpy.seen_label('massage_sunscreen.hips'):
            al.dcv.intrusion.stage = 7

        my_scope = {
            'alice'          : al,
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

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 100
        mg.massage = 100

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        dr_var = [0,]
        if 'alice_nopants' in persistent.mems_var:
            dr_var.append(1)
        if 'alice_not_nopants' in persistent.mems_var:
            dr_var.append(2)
        if 'pajamas' in persistent.mems_var:
            dr_var.append(3)
        if 'smoke_nojeans' in persistent.mems_var:  # and renpy.random.choice([False, True]):
            dr_var.append(4)
        if 'kira' in persistent.mems_var:
            dr_var.append(5)
        var = renpy.random.choice(dr_var)
        # print dr_var, var
        al.dress, al.req.result = {
                0 : ('a', ''),
                1 : ('a', 'nopants'),
                2 : ('a', 'not_nopants'),
                3 : ('b', ''),
                4 : ('c', 'nojeans'),
                5 : ('d', ''),
            }[var]
        al.stat.footjob = 3
        al.flags.m_foot = 7
        al.dcv.seduce.done = renpy.random.choice([False, True])

        my_scope = {
                'house'     : copy.deepcopy(house),
                'tm'        : '22:00',
                'mgg'       : mg,
                'alice'     : al,
                'kol_choco' : 5,
                'pose3_2'   : renpy.random.choice(['01', '02', '03']),
            }
        return my_scope

    # Помассирую не только ножки
    def set_advanced_massage1():

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.flags.hip_mass = renpy.random.randint(1, 2)
        dr_var = ['b', 'c'] if 'pajamas' in persistent.mems_var else ['c']
        if 'kira' in persistent.mems_var:
            dr_var.append('d')
        my_scope = {
                'tm'        : '22:00',
                'alice'     : al,
                '_drink'    : 2,
                '_ch20'     : Chance(700),
                '_ch25'     : Chance(875),
                '_pose'     : renpy.random.choice(['03', '04']),
                '_dress'    : (renpy.random.choice(['b','c']) if 'max-a' in persistent.mems_var else 'c') + renpy.random.choice(dr_var)
            }
        return my_scope

    # Первый массаж ног
    def set_foot_mass():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress('a')

        my_scope = {
                'pose3_1' : renpy.random.choice(['01', '02', '03']),
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope

    # Внимание к пальчикам
    def set_hand_mass():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        my_scope = {
                'kissmas'   : False,
                'lisa'      : tl,
                'mgg'       : mg,
            }
        return my_scope

    # Разомнём и плечики
    def set_shoulders_mass():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        my_scope = {
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope

    # Массаж для любимой тёти
    def set_kira_bathmass():

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")

        my_scope = {
            'kira'  : tk,
            }
        return my_scope

    # Совсем другой массаж
    def set_kira_bathfj():
        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        mg.sex    = 7

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.flags.m_breast = 1
        tk.flags.promise = renpy.random.choice([True, False])
        tk.stat.handjob = renpy.random.choice([1, 2])

        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dcv.seduce.stage = 2

        my_scope = {
            'mgg'   : mg,
            'kira'  : tk,
            'lisa'  : tl,
            'memes' : 1,
            }
        return my_scope

    ############################################################################

    # Ночные страхи
    def set_spider_in_bed():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = renpy.random.randint(221, 379) / 10.0
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.mood = 250
        # вписать бельё
        al.dress = renpy.random.choice(['a', 'b']) if 'black_linderie' in persistent.mems_var else 'a'

        sm = [None, None]
        if 'alice_sleeptoples' in persistent.mems_var:
            sm.extend(['sleep', 'not_sleep'])
        if 'alice_sleepnaked' in persistent.mems_var:
            sm.extend(['naked', 'not_naked'])
        al.req.result = renpy.random.choice(sm)
        print sm
        al.req.req = {None: None, 'sleep':'sleep', 'not_sleep':'sleep', 'naked':'naked', 'not_naked':'naked'}[al.req.result]
        my_scope = {
            'tm'       : '02:30',
            'mgg'      : mg,
            'alice'    : al,
            }
        return my_scope

    # Кто это там ползёт
    def set_spider_massage():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c'

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.daily.oiled = renpy.random.choice([1, 2])

        if 'squeeze_chest' in persistent.mems_var:
            # тискал Алису за грудь
            al.dcv.intrusion.stage = 7

        my_scope = {
            'tm'    : '15:00',
            'alice' : al,
            'mgg'   : mg,
            }
        return my_scope

    # Монстр в ванной комнате
    def set_spider_shower():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.mood = 250
        al.relmax = 500

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.social = 100

        # были обнимашки во время ивента
        al.gifts.append('sexbody1')
        al.flags.hugs = 5

        # были рискованные обнимашки
        al.flags.privpunish += 1

        my_scope = {
            'tm'       : '08:00',
            'alice'    : al,
            'mgg'      : mg,
            'chars'    : {'alice': al},
            }
        return my_scope

    # Торчащая мощь
    def set_spider_massage2():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c'

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.daily.oiled = 2

        # Алиса может спрятаться за Максом
        al.dcv.intrusion.stage = 7
        al.flags.privpunish = 1
        # Алиса уже пряталась за Максом
        al.flags.touched = True

        my_scope = {
            'tm'    : '15:00',
            'alice' : al,
            'mgg'   : mg,
            }
        return my_scope

    # После клуба
    def set_after_club():
        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.extend(['nopants', 'not_nopants'])
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.req.result = renpy.random.choice(sm)

        my_scope = {
            'tm'       : '03:00',
            'alice'    : al,
            }
        return my_scope

    # Я была плохой девочкой
    def set_after_club_next1():
        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.extend(['nopants', 'not_nopants'])
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.req.result       = renpy.random.choice(sm)
        # Макс ласкал киску Алисы перед ТВ
        al.flags.hip_mass   = 2 if 'double_mass_alice' in persistent.mems_var else 0
        al.dcv.intrusion.stage = 7

        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        # полностью пройден второй урок поцелуев у Киры
        tl.dcv.seduce.stage = 4 if 'kira_night_tv.second_lesson' in persistent.memories and persistent.memories['kira_night_tv.second_lesson'] else 3

        my_scope = {
            'tm'        : '03:00',
            'alice'     : al,
            'lisa'      : tl,
            'mgg'       : mgg,
            'spent_time': 0,
            }
        return my_scope

    # Я принес тебе полотенце!
    def set_alice_towel_after_club():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.gifts.append('sexbody1')
        al.dcv.intrusion.stage = 7 if 'bath_tongue' in persistent.mems_var else 0
        al.flags.nakedpunish = True
        al.daily.drink = 2

        my_scope = {
                'tm'    : '03:15',
                'alice' : al,
            }
        return my_scope

    # Первые снимки для блога Алисы
    def set_alice_body_photoset1():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b'])

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')

        if 'alice_photoset1' in persistent.mems_var:
            al.daily.drink = 1

        my_scope = {
                'cam_pose_blog' : '',
                'tm'            : '20:30',
                'spent_time'    : 0,
                'alice'         : al,
                'mgg'           : mg,
                'items'         : {'sexbody1':Item("ЧЁРНОЕ СЕКСУАЛЬНОЕ БОДИ", have=True)},
                'expected_photo': [],
            }

        return my_scope

    # Я обошёл Эрика с подарком для Алисы
    def set_gift_lace_lingerie():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b'])

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.stealth = 28.7

        al.dcv.intrusion.stage = 3
        al.dcv.intrusion.set_lost(3)
        al.dcv.photo.stage = 2
        if 'alice_photoset1' in persistent.mems_var:
            al.daily.drink = 1
        my_scope = {
            'cam_pose_blog' : '',
            'tm'            : '20:30',
            'spent_time'    : 0,
            'alice'         : al,
            'mgg'           : mg,
            'items'         : {
                                'sexbody1':Item("ЧЁРНОЕ СЕКСУАЛЬНОЕ БОДИ"),
                                'sexbody2':Item("ЧЁРНОЕ КРУЖЕВНОЕ БОДИ", have=True)
                            },
            }

        return my_scope

    ############################################################################

    # Смотрим порно вместе с тётей
    def set_porn_tv():
        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'
        tk.flags.porno = 2
        tk.flags.m_foot = 1
        tk.flags.promise = renpy.random.choice([True, False])
        my_scope = {
            'kira'     : tk,
            }
        return my_scope

    # Первый урок поцелуев
    def set_kira_kiss_01():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.kissing = 0

        my_scope = {
            'mgg'      : mg,
            }
        return my_scope

    # А это уже совсем не массаж!
    def set_kira_bathbj():
        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        mg.sex    = 7

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.flags.promise = renpy.random.choice([True, False])
        tk.stat.blowjob = 1
        tk.stat.handjob = renpy.random.choice([1, 2])
        tk.flags.m_breast = 2

        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dcv.seduce.stage = 2

        my_scope = {
            'memes' : 2,
            'mgg'   : mg,
            'kira'  : tk,
            'lisa'  : tl,
            }
        return my_scope

    # Второй урок поцелуев
    def set_kira_kiss_02():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.kissing = 1.1
        mg.social = 100

        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dcv.seduce.stage = 2

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.flags.m_foot = 1 if 'kira.bath.mass' in persistent.mems_var else 0

        my_scope = {
            'kira'  : tk,
            'lisa'  : tl,
            'mgg'   : mg,
            }
        return my_scope

    # Третий урок поцелуев
    def set_kira_kiss_03():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = 7

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.stat.blowjob = renpy.random.choice([True, False])
        tk.stat.handjob = renpy.random.randint(0, 2)
        tk.stat.footjob = 1
        my_scope = {
            'kira'  : tk,
            'mgg'      : mg,
            }
        return my_scope

    # Горячее, чем порно
    def set_porn_tv2():
        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'
        tk.flags.porno  = 2
        tk.flags.m_foot = 1
        tk.stat.blowjob = 1
        tk.stat.handjob = 2

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = 7
        my_scope = {
            'kira'     : tk,
            'mgg'      : mg,
            }
        return my_scope

    # Небольшое приключение перед сном
    def set_night_swim():

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.stat.handjob   = renpy.random.randint(1, 2)
        tk.flags.promise  = False
        tk.stat.blowjob   = 1
        my_scope = {
            'kira'     : tk,
            }
        return my_scope

    # Не зря купил сорочку

    # С меня приятный должок

    # Стриптиз после клуба
    def set_kira_strip_01():

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dcv.feature.stage = 6 if 'strip.show' in persistent.mems_var else 5
        tk.stat.blowjob = 1

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.daily.drink = renpy.random.choice([0, 1])

        my_scope = {
                'tm'    : '03:10',
                'kira'  : tk,
                'alice' : al,
            }
        return my_scope

    # Порно-портфолио для Киры
    def set_kira_photoset_01():
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

    ############################################################################

    # Вкусные уроки с сестрёнкой
    def set_lisa_advanced_kiss_lesson():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
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
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        mg.kissing = 6.0

        my_scope = {
                'kissmas'   : True,
                'lisa'     : tl,
                'mgg'      : mg,
            }
        return my_scope

    # Больше, чем помощь с домашним заданием
    def set_homework_mass_01():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
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
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress  = 'b'
        tl.flags.kiss_lesson = 12 if 'horror_kiss' in persistent.mems_var else 6

        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex    = 9

        tf = Other_Flags_and_counters()
        tf.cur_series = renpy.random.randint(1, 2)
        tf.cur_movies = [renpy.random.choice(['hes', 'f13']), renpy.random.randint(0, 4), renpy.random.randint(0, 4)]

        my_scope = {
            'lisa'  : tl,
            'mgg'   : mg,
            'flags' : tf,
            }
        return my_scope

    ############################################################################

    # Урок по минету от мамы и Эрика
    # Так близко к маминой попке
    # Глубокий минет в мамином исполнении
    def set_lessons_Eric_01():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
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
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        te = Profile('eric', "Эрик", "Эрика", "Эрику", "Эрика", "Эриком", "Эрике")
        te.dress = renpy.random.choice(['a', 'b'])

        my_scope = {
            'eric' : te,
            'lisa' : tl,
            }
        return my_scope

    # Кружевное боди для Алисы от Эрика
    def set_blog_with_Eric_01():

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b', 'c'])

        te = Profile('eric', "Эрик", "Эрика", "Эрику", "Эрика", "Эриком", "Эрике")
        te.dress = renpy.random.choice(['a', 'b'])

        my_scope = {
                'spent_time' : 0,
                'tm'         : '20:20',
                'alice'      : al,
                'eric'       : te,
            }
        return my_scope
