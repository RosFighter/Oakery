init python:
    import copy

    def get_lisa_dress(st='', tp='casual'):
        if tp == 'learn':
            dr_l = ['c', 'd'] if 'kira' in persistent.mems_var else ['c']
        else:
            dr_l = ['d'] if 'kira' in persistent.mems_var else ['a']

        if 'bathrobe' in persistent.mems_var:
            dr_l.append('b')
        if st!='':
            if type(st)==list:
                dr_l.extend(st)
            else:
                dr_l.append(st)
        return renpy.random.choice(dr_l)


    def get_max_dress(st=''):
        dr_m = ['c'] if 'kira' in persistent.mems_var else ['a']
        if 'max-a' in persistent.mems_var:
            dr_m.append('b')
        if st!='':
            if type(st)==list:
                dr_m.extend(st)
            else:
                dr_m.append(st)
        return renpy.random.choice(dr_m)


    def set_gift_swimsuit():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.plan_name = renpy.random.choice(['sun', 'read'])
        my_scope = {
                'lisa' : tl,
                'flags': {'promise_kiss':True},
            }
        return my_scope


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


    def set_foot_mass():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress(tp='learn')

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()

        my_scope = {
                'pose3_1' : renpy.random.choice(['01', '02', '03']),
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope


    def set_hand_mass():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress()
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        my_scope = {
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope


    def set_shoulders_mass():
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = get_lisa_dress('learn')
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = get_max_dress()
        my_scope = {
                'lisa' : tl,
                'mgg'  : mg,
            }
        return my_scope


    def set_sunscreen():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c' if 'kira' in persistent.mems_var else 'b'
        mg.social = 100

        my_scope = {
            'talk_var'       : {'sun_oiled':1},
            'online_cources' : copy.deepcopy(online_cources),
            'mgg'            : mg,
            '_massaged'      : [],
            '_talk_top'      : False,
            'tm'             : '15:00',
            'house'          : copy.deepcopy(house),
            'items'          : {"spider" : Item("", "", "spider", None),}
            }
        return my_scope


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
        print(dr_var)
        var = renpy.random.choice(dr_var)
        print(var)
        al.dress, smoke = {
                0 : ('a', ''),
                1 : ('a', 'nopants'),
                2 : ('a', 'not_nopants'),
                3 : ('b', ''),
                4 : ('c', 'nojeans'),
                5 : ('d', ''),
            }[var]

        my_scope = {
                'tm'        : '22:00',
                'mgg'       : mg,
                'talk_var'  : {'al.tv.mas' : 0, 'al.tvgood':3},
                'flags'     : {'alice.tv.mass' : 7, 'smoke':smoke},
                'dcv'       : {'tvchoco' : Daily(done=renpy.random.choice([False, True]), enabled=True)},
                'kol_choco' : 5,
                'pose3_2'   : renpy.random.choice(['01', '02', '03']),
                'alice'     : al,
                'house'     : copy.deepcopy(house),
            }
        return my_scope


    def set_spider_in_bed():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.mood = 250

        sm = ['']
        if 'alice_sleeptoples' in persistent.mems_var:
            sm.extend(['sleep', 'not_sleep'])
        my_scope = {
            'talk_var' : {'smoke': ''},
            'flags'    : {'smoke': renpy.random.choice(sm), 'noted': False},
            'mgg'      : mg,
            'tm'       : '02:30',
            'alice'    : al,
            }
        return my_scope


    def set_spider_massage():
        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = 'c'

        my_scope = {
            'talk_var' : {'sun_oiled': renpy.random.choice([1, 2])},
            'mgg'      : mg,
            'tm'       : '15:00'
            }
        return my_scope


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


    def set_porn_tv():
        tk = Profile("Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'
        my_scope = {
            'talk_var' : {'kira.porn' : 2, 'kira.bath.mass':True},
            'flags'    : {'kira.tv.bj' : False},
            'kira'     : tk,
            }
        return my_scope


    def set_porn_tv2():
        tk = Profile("Кира", "Киры", "Кире", "Киру", "Кирой", "Кире")
        tk.dress = 'a'

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = 7
        my_scope = {
            'talk_var' : {'kira.porn' : 2, 'kira.bath.mass':True},
            'flags'    : {'kira.tv.bj' : True},
            'kira'     : tk,
            'mgg'      : mg,
            }
        return my_scope


    def set_kira_kiss_01():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.kissing = 0

        my_scope = {
            'mgg'      : mg,
            }
        return my_scope


    def set_kira_kiss_02():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.kissing = 1.1
        mg.social = 100

        my_scope = {
            'talk_var': {'teachkiss': 2, 'kira.bath.mass': 1 if 'kira.bath.mass' in persistent.mems_var else 0},
            'mgg'      : mg,
            }
        return my_scope


    def set_kira_kiss_03():

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.sex = 7

        my_scope = {
            'flags'    : {'kira.bath.fj': True, 'kira.tv.bj': renpy.random.choice([True, False])},
            'mgg'      : mg,
            }
        return my_scope


    def set_kira_bathmass():

        my_scope = {
            'talk_var' : {'kira.porn': 1, 'lisa.footmass': 1, 'kira.bath.mass':0},
            }
        return my_scope


    def set_kira_bathfj():
        mg        = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        mg.sex    = 7

        my_scope = {
            'talk_var' : {'kira.tv.touch': 1, 'teachkiss':2},
            'flags'    : {'kira.tv.bj': False},
            'memes'    : 1,
            'mgg'      : mg,
            }
        return my_scope


    def set_kira_bathbj():
        mg        = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.social = 100
        mg.sex    = 7

        my_scope = {
            'talk_var' : {'kira.tv.touch': 2, 'teachkiss':2},
            'flags'    : {'kira.tv.bj': True},
            'memes'    : 2,
            'mgg'      : mg,
            }
        return my_scope
