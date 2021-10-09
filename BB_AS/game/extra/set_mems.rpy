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
        if not dr_m:
            return 'c'
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
        mg.social = renpy.random.randint(143, 197) / 10
        mg.massage = renpy.random.randint(134, 174) / 10
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
        mg.social = renpy.random.randint(258, 197) / 10 #27
        mg.massage = renpy.random.randint(58, 78) / 10 #6.8

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
                'chars'     : ['alice'],
            }
        return my_scope

    # Помассирую не только ножки
    def set_advanced_massage1():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.flags.hip_mass = renpy.random.randint(1, 2)
        dr_var = ['b', 'c'] if 'pajamas' in persistent.mems_var else ['c']
        if 'kira' in persistent.mems_var:
            dr_var.append('d')
        al.dress = renpy.random.choice(dr_var)
        al.daily.drink = 2

        my_scope = {
                'tm'            : '22:00',
                'alice'         : al,
                'mgg'           : mg,
                '_pose'         : renpy.random.choice(['03', '04']),
                'chars'         : ['kira'],
                'rand_result'   : True,
            }
        return my_scope

    # Могу не только руками
    def set_advanced_massage2():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.sex = renpy.random.randint(123, 167) / 10 #14.2
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.flags.hip_mass = renpy.random.randint(1, 2)
        al.dcv.intrusion.stage = 7
        dr_var = ['b', 'c'] if 'pajamas' in persistent.mems_var else ['c']
        if 'kira' in persistent.mems_var:
            dr_var.append('d')
        al.dress = renpy.random.choice(dr_var)
        my_scope = {
                'alice'     : al,
                'mgg'       : mg,
                '_drink'    : 1,
                '_pose'     : renpy.random.choice(['05', '06']),
                '_dress'    : mg.dress + al.dress,
            }
        return my_scope

    # Ответная благодарность
    def set_advanced_massage3():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.sex = renpy.random.randint(168, 197) / 10 #18
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.flags.hip_mass = renpy.random.randint(1, 2)
        dr_var = ['b', 'c'] if 'pajamas' in persistent.mems_var else ['c']
        if 'kira' in persistent.mems_var:
            dr_var.append('d')
        al.dress = renpy.random.choice(dr_var)
        my_scope = {
                'alice'     : al,
                'mgg'       : mg,
            }
        return my_scope

    # Первый массаж ног
    def set_foot_mass():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress() if tl.dress == 'd' else get_max_dress('a')
        mg.massage = renpy.random.randint(70, 90) / 10#8.7

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
        mg.massage = renpy.random.randint(65, 80) / 10#7.6
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
        mg.massage = renpy.random.randint(67, 92) / 10#8.1
        my_scope = {
                'lisa' : tl,
                'mgg'  : mg,
                'rand_result' : True,
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
        mg.social = renpy.random.randint(720, 870) / 10
        mg.sex    = renpy.random.randint(60, 80) / 10

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
        mg.social = renpy.random.randint(181, 219) / 10.0
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.mood = 250
        al.dress = renpy.random.choice(['a', 'b']) if 'black_linderie' in persistent.mems_var else 'a'

        sm = [None, None]
        if 'alice_sleeptoples' in persistent.mems_var:
            sm.extend(['sleep', 'not_sleep'])
        if 'alice_sleepnaked' in persistent.mems_var:
            sm.extend(['naked', 'not_naked'])
        al.req.result = renpy.random.choice(sm)
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
        mg.social = renpy.random.randint(350, 450) / 10

        if renpy.seen_label('alice_shower.hug'):
            # были обнимашки во время ивента
            al.gifts.append('sexbody1')
            al.flags.hugs = 5

        if renpy.seen_label('alice_shower.dangerous_hugs'):
            # были рискованные обнимашки
            al.flags.privpunish += 1

        my_scope = {
            'tm'       : '08:00',
            'alice'    : al,
            'mgg'      : mg,
            'chars'    : {'alice': al},
            }
        return my_scope

    # Держи и не отпускай
    def set_spider_massage2():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c'

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.daily.oiled = 2

        if 'hide_behind' in persistent.mems_var:
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
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
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
            'tm'            : '03:00',
            'alice'         : al,
            'lisa'          : tl,
            'mgg'           : mg,
            'spent_time'    : 0,
            }
        return my_scope

    # Как тебе такое?
    def set_after_club_next2():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = renpy.random.randint(110, 130) / 10
        sm = ['']
        if 'alice_nopants' in persistent.mems_var:
            sm.extend(['nopants', 'not_nopants'])
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.req.result       = renpy.random.choice(sm)
        # Макс ласкал киску Алисы перед ТВ
        al.flags.hip_mass   = 5
        al.dcv.intrusion.stage = 7
        al.daily.drink = 2

        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        # полностью пройден второй урок поцелуев у Киры
        tl.dcv.seduce.stage = 4
        if renpy.seen_label('alice_after_club.need_hurry'):
            al.flags.touched = True

        my_scope = {
            'tm'            : '03:00',
            'alice'         : al,
            'lisa'          : tl,
            'mgg'           : mg,
            'spent_time'    : 0,
            }
        return my_scope

    # Я принес тебе полотенце!
    def set_alice_towel_after_club():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        # mg.sex = renpy.random.randint(110, 130) / 10
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.gifts.append('sexbody1')
        al.dcv.intrusion.stage = 7 if 'bath_tongue' in persistent.mems_var else 0
        al.flags.nakedpunish = True
        al.daily.drink = 2
        if renpy.seen_label('alice_towel_after_club.not_even_close'):
            al.flags.hip_mass = 5

        my_scope = {
                'tm'    : '03:15',
                'alice' : al,
                'mgg'   : mg,
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
                'items'         : {'sexbody1':Item("ЧЁРНОЕ СЕКСУАЛЬНОЕ БОДИ", have=True), 'photocamera':Item("ФОТОАППАРАТ", have=True)},
                'expected_photo': [],
            }

        return my_scope

    # Я обошёл Эрика с подарком для Алисы
    def set_gift_lace_lingerie():
        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b'])

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.stealth = renpy.random.randint(270, 290) / 10

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

    # Попка, которую я теперь могу отшлёпать
    def set_private_punish1():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        my_scope = {
            'mgg'           : mg,
            }

        return my_scope

    # Меня нужно наказать именно так!
    def set_alice_domine_drink():

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.social = renpy.random.randint(650, 850) / 10
        mg.sex = renpy.random.randint(170, 270) / 10
        mg.kissing = renpy.random.randint(110, 165) / 10

        al = Profile('alice', "Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.dress = renpy.random.choice(['a', 'b', 'c', 'd'])
        al.flags.hip_mass = 5

        my_scope = {
            'tm'        : '22:00',
            'pose3_2'   : renpy.random.choice(['01', '02', '03']),
            'mgg'       : mg,
            'alice'     : al,
            'kol_choco' : 5,

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
        mg.sex    = renpy.random.randint(60, 80) / 10

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
        mg.kissing = renpy.random.randint(90, 130) / 10
        mg.social = renpy.random.randint(300, 400) / 10

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
        mg.sex = renpy.random.randint(60, 80) / 10

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.stat.blowjob = renpy.random.choice([True, False])
        tk.stat.handjob = renpy.random.randint(0, 2)
        tk.stat.footjob = 1
        my_scope = {
            'kira'  : tk,
            'mgg'   : mg,
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
        mg.sex = renpy.random.randint(60, 80) / 10
        my_scope = {
            'kira'     : tk,
            'mgg'      : mg,
            }
        return my_scope

    # Небольшое приключение перед сном
    def set_night_swim():

        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = renpy.random.randint(700, 930) / 10
        mg.sex    = renpy.random.randint(60, 80) / 10

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.stat.handjob   = renpy.random.randint(1, 2)
        tk.flags.promise  = False
        tk.stat.blowjob   = 1
        if 'bj_in_pool' in persistent.mems_var:
            tk.stat.sex = 5
        my_scope = {
            'mgg'      : mg,
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
                'items'     : itm,
                'weekday'   : 6,
                # 'day'   : 32,
            }
        return my_scope

    # Немного БДСМ от Киры

    # Хватит мять сиськи
    def set_porn_tv3():
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.stat.handjob = 2
        if renpy.seen_label('kira_photoset3'):
            mg.sex = renpy.random.randint(110, 130) / 10
            tk.dcv.photo.stage = 3
        else:
            mg.sex = renpy.random.randint(130, 160) / 10
            tk.dcv.photo.stage = 2
        my_scope = {
            'kira'  : tk,
            'mgg'   : mg,
            'naked' : False,
            }
        return my_scope

    # И помылись, и порезвились
    def set_kira_batxsex1():
        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex    = renpy.random.randint(110, 140) / 10
        mg.dress = get_max_dress(ex='a')

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dcv.photo.stage = 2

        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dcv.seduce.stage = 2

        my_scope = {
            'mgg'   : mg,
            'kira'  : tk,
            'lisa'  : tl,
            }
        return my_scope

    # Кто нас фотографирует?
    def set_kira_photoset3():

        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex    = renpy.random.randint(350, 790) / 10

        tk = Profile('kira', "Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'
        my_scope = {
            'pose3_4'   : renpy.random.choice(['01', '02', '03']),
            'kira'      : tk,
            'mgg'       : mg,
        }

        return my_scope

    ############################################################################

    # Вкусные уроки с сестрёнкой
    def set_lisa_advanced_kiss_lesson():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()

        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.kissing = renpy.random.randint(50, 80) / 10

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
        mg.dress = get_max_dress(ex='a')
        mg.kissing = renpy.random.randint(42, 57) / 10
        mg.massage = renpy.random.randint(65, 85) / 10

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
        mg.dress = get_max_dress(ex='a')
        mg.social = renpy.random.randint(200, 297) / 10
        mg.massage = renpy.random.randint(170, 210) / 10

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
        mg.sex    = renpy.random.randint(80, 100) / 10

        tf = Other_Flags_and_counters()
        tf.cur_series = renpy.random.randint(1, 2)
        tf.cur_movies = [renpy.random.choice(['hes', 'f13', 'scr']), renpy.random.randint(1, 5), renpy.random.randint(1, 5), renpy.random.randint(1, 4)]

        my_scope = {
            'lisa'  : tl,
            'mgg'   : mg,
            'flags' : tf,
            }
        return my_scope

    # Без майки куда интереснее
    def set_horor_02():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress  = 'b'
        tl.flags.kiss_lesson = 12
        tl.dcv.other.stage = 1

        mg        = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex    = renpy.random.randint(120, 160) / 10

        tf = Other_Flags_and_counters()
        tf.cur_series = renpy.random.randint(1, 2)
        tf.cur_movies = [renpy.random.choice(['hes', 'f13', 'scr']), renpy.random.randint(1, 5), renpy.random.randint(1, 5), renpy.random.randint(1, 4)]

        my_scope = {
            'lisa'  : tl,
            'mgg'   : mg,
            'flags' : tf,
            }
        return my_scope

    # Долой смущение
    def set_olivia_second_night_visit():
        tl = Profile('lisa', "Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dcv.special.stage=4

        to = Profile('olivia', "Оливия", "Оливии", "Оливии", "Оливию", "Оливией", "Оливии")
        to.dcv.other.stage = 1

        tf = Other_Flags_and_counters()
        tf.film_punish = False

        t_tv_order = ['0'+str(i) for i in range(1, 8)]
        renpy.random.shuffle(t_tv_order)

        my_scope = {
            'lisa'          : tl,
            'olivia'        : to,
            'flags'         : tf,
            'film'          : None,
            'ol_tv_order'   : t_tv_order,
            }
        return my_scope

    ############################################################################

    # Я уже взрослый!
    def set_ann_ero1():
        ta = Profile('ann', "Анна", "Анны", "Анне", "Анну", "Анной", "Анне")
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        my_scope = {
            'ann' : ta,
            'mgg' : mg,
            }
        return my_scope

    # Это точно триллер-детектив?  и  Полотенце снова сползает...
    def set_ann_ero2():
        ta = Profile('ann', "Анна", "Анны", "Анне", "Анну", "Анной", "Анне")
        ta.flags.handmass = True
        mg = MaxProfile('mgg', "Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress(ex='a')
        mg.massage = renpy.random.randint(600, 800) / 10
        my_scope = {
            'ann'       : ta,
            'mgg'       : mg,
            'pose3_1'   : renpy.random.choice(['01', '02', '03']),
            'pose3_3'   : renpy.random.choice(['01', '02', '03']),
            'flags'     : Other_Flags_and_counters(),
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
                '_stockings' : random_outcome(50),
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
