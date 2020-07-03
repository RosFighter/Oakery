init python:
    def set_gift_swimsuit():
        global my_scope
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.plan_name = renpy.random.choice(['sun', 'read'])
        my_scope = {
                'lisa' : tl,
                'flags': {'promise_kiss':True},
            }


    def set_gift_pajamas():
        global my_scope
        sg = {'alice': SorryGift()}
        sg['alice'].give = sorry_gifts['alice'].give.copy()
        sg['alice'].owe = True
        al = Profile("Алиса", "Алисы", "Алисе", "Алису", "Алисой", "Алисе")
        al.plan_name = 'resting'
        # al.plan_name = renpy.random.choice(['sun', 'resting'])
        if al.plan_name != 'sun':
            al.dress = renpy.random.choice(['a', 'd']) if 'kira' in chars else 'a'
            _tm = renpy.random.choice(['10:20', '21:00'])
        else:
            al.dress = 'a'
            _tm = '15:30'

        fl = {
                'alice_hugs': 4,
                'smoke': renpy.random.choice(['', 'nopants', 'not_nopants']) if al.dress=='a' else ''
            }

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = renpy.random.choice(['a', 'b', 'c']) if 'kira' in chars else renpy.random.choice(['a', 'b'])

        my_scope = {
                'sorry_gifts' : sg,
                'alice'       : al,
                'flags'       : fl,
                'tm'          : _tm,
                'talk_var'    : {'sun_oiled': renpy.random.choice([0, 2])},
                'mgg'         : mg,
                'pose2_2'     : renpy.random.choice(['01', '02']),
                'pose3_2'     : renpy.random.choice(['01', '02', '03']),
            }


    def set_foot_mass():
        global my_scope
        tl = Profile("Лиза", "Лизы", "Лизе", "Лизу", "Лизой", "Лизе")
        tl.dress = renpy.random.choice(['b', 'c', 'd']) if 'kira' in chars else renpy.random.choice(['b', 'c'])

        mg = MaxProfile("Макс", "Макса", "Максу", "Макса", "Максом", "Максе")
        mg.dress = renpy.random.choice(['a', 'b', 'c']) if 'kira' in chars else renpy.random.choice(['a', 'b'])

        my_scope = {
                'pose3_1' : renpy.random.choice(['01', '02', '03']),
                'lisa' : tl,
                'mgg'  : mg,
            }


    def set_hand_mass():
        global my_scope



    def set_shoulders_mass():
        global my_scope
