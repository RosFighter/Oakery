
label old_fix:
    # "ver [current_ver], _ver [_version]"
    if current_ver == 'v0.01.TechDemo':
        scene BG villa-door
        "Сохранения версии техно-демо не поддерживаются. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    elif current_ver[:5] == 'v0.02':
        scene BG villa-door
        "К сожалению сохранения этой версии не поддерживаются из-за большого количества внутренних изменений. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    elif current_ver < '0.03.5.000':
        scene BG villa-door
        "К сожалению сохранения этой версии не поддерживаются из-за большого количества внутренних изменений. Начните новую игру или выберите другое сохранение."
        $ renpy.full_restart()
    else:
        if current_ver == "0.06.6.00":
            $ current_ver = "0.06.0.00"

        if current_ver < "0.03.5.999":
            call after_load_03_5 from _call_after_load_03_5

        if current_ver < "0.03.9.999":
            call after_load_03_9 from _call_after_load_03_9

        if current_ver < "0.04.0.999":
            call after_load_04_0 from _call_after_load_04_0

        if current_ver < "0.04.1.999":
            call after_load_04_1 from _call_after_load_04_1

        if current_ver < "0.04.5.999":
            call after_load_04_5 from _call_after_load_04_5

        if current_ver < "0.05.0.999":
            call after_load_05_0 from _call_after_load_05_0

        if current_ver < "0.06.0.999":
            call after_load_06_0 from _call_after_load_06_0

    return


label after_load_03_5:
    # "03.5"
    if current_ver < "0.03.5.002":
        $ current_ver = "0.03.5.002"

        $ poss['seduction'].stages[1].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['Schoolmate'].stages[0].ps = _("Да, и похоже о своём мальчике Лиза разговаривает только, когда у неё хорошее настроение... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['blog'].stages[0].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['Swimsuit'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['Swimsuit'].stages[4].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['nightclub'].stages[2].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['nightclub'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['nightclub'].stages[4].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['smoke'].stages[1].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['smoke'].stages[2].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['sg'].stages[4].ps = _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['sg'].stages[5].ps = _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['sg'].stages[6].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['sg'].stages[6].ps = _("Сомневаюсь, что теперь получится её подставить, уж слишком большое недоверие она ко мне испытывает. \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['spider'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['alpha'].stages[0].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['SoC'].stages[8].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        $ poss['risk'].stages[8].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

    if current_ver < "0.03.5.003":
        $ current_ver = "0.03.5.003"

        $ poss['sg'].stages.append(PossStage("interface poss lessons ep01", _("Я помогал Лизе с уроками какое-то время, причём безвозмездно, но это стало довольно скучным делом и я намеренно стал делать ошибки так, чтобы ей ставили двойки и наказывали... И вот, после очередной двойки и наказания от мамы, она обратилась ко мне за помощью. Я согласился, но с условием, что она будет спать только в футболке и трусиках. И думаю, что мне удастся её ещё на что-нибудь раскрутить..."),
                    _("Правда, Лиза слегка на меня обиделась, но это я переживу. Подарю ей что-нибудь вкусненькое и она оттает... \n\n{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")))

    return


label after_load_03_9:
    # "03.9"
    if current_ver < "0.03.9.001":
        $ current_ver = "0.03.9.001"

        $ poss['seduction'].stages[1].ps = ""
        $ poss['seduction'].stages.extend([
            PossStage("interface poss mentor ep02", _("Лиза снова увидела мой утренний стояк. На этот раз маму она не позвала, что уже хорошо. Хотя, смотрела она на мой член не только с подозрением, но ещё и с интересом. По крайней мере, мне так показалось. Думаю, нужно с ней об этом поговорить...")),
            PossStage("interface poss mentor ep03", _("Это, конечно, не точно, но Лиза хотела потрогать мой член, думая, что я спал. И судя по её реакции на то, что я это увидел, даже она сама с себя удивилась. Посмотрим, что она потом об этом скажет..."),
                    _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),
            ])

        # $ EventsByTime['MorningWoodCont'] = CutEvent('06:30', label='MorningWoodCont', desc='утренний стояк продолжение', variable="all([day>=7, dcv['mw'].done, flags['morning_erect']%2==0, poss['seduction'].stn > 0])", sleep=True, cut=True)
        # $ dcv['mw'] = Daily(done=True, enabled=True)

    if current_ver < "0.03.9.002":
        $ current_ver = "0.03.9.002"

        # $ flags['alice.tv.mass'] = 0
        # $ talk_var['al.tv.mas'] = 0
        $ poss['seduction'].stages[3].ps = ""
        $ poss['seduction'].stages.append(PossStage("interface poss mentor ep04", _("Похоже, интерес Лизы к противоположному полу и всему, что связано со взрослой жизнью, растёт не по дням, а по часам. Не знаю уж, мой стоящий по утрам член так её раззадорил или ещё что-то, но она согласилась меня слушаться по вопросам о мальчиках и всем этим взрослым штучкам... Вот только прежде, чем учить, может быть стоит самому чему-то научиться? А самое главное - при этом ничего не испортить, а то она снова откажется..."), _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")))

        $ kol_choco = 0
        # $ items['choco'] = Item(_("КОНФЕТЫ С ЛИКЁРОМ"), _("Шоколадные конфеты с ликёром. Уникальные ароматизаторы скрывают вкус алкоголя. Отлично поднимают настроение. Очень крепкие."), "choco", 2, 20)
        # $ dcv['tvchoco'] = Daily(done=True, enabled=True)

    if current_ver < "0.03.9.003":
        $ current_ver = "0.03.9.003"

        # $ alice_good_mass = _("{color=#E59400}{i}Алисе понравился массаж!{/i}{/color}\n")
        # $ alice_bad_mass  = _("{color=#E59400}{i}Алисе не понравился массаж!{/i}{/color}\n")
        $ poss['nightclub'].stages[2].ps = ""
        $ poss['nightclub'].stages[3].ps = ""
        $ poss['nightclub'].stages[4].ps = ""
        $ poss['nightclub'].stages[6].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        # $ dcv['alice.secret'] = Daily(done=True, enabled=True)

    if current_ver < "0.03.9.004":
        $ current_ver = "0.03.9.004"

        # python:
            # clothes = {
            #     lisa  : Clothing(),
            #     alice : Clothing(),
            #     ann   : Clothing(),
            #     mgg   : Clothing(),
            #     }
            #
            # clothes[lisa].casual = Clothes(_("Повседневная"), [
            #         Garb('a', '01a', 'Обычная одежда'),
            #     ])
            # clothes[lisa].learn = Clothes(_("За уроками"), [
            #         Garb('a', '01a', 'Обычная одежда'),
            #         Garb('c', '04b', 'Полотенце', True),
            #     ])
            # if 'bathrobe' in lisa.gifts:
            #     clothes[lisa].casual.sel.insert(1, Garb('b', '04', _("ШЕЛКОВЫЙ ХАЛАТ"), True))
            #     clothes[lisa].learn.sel.insert(1, Garb('b', '04', 'Халатик', True))
            #
            # clothes[lisa].swimsuit = Clothes(_("КУПАЛЬНИК"), [
            #         Garb('a', '03', 'Закрытый купальник'),
            #     ])
            # if 'bikini' in lisa.gifts:
            #     clothes[lisa].swimsuit.sel.insert(1, Garb('b', '03b', 'КУПАЛЬНИК КРАСНЫЙ', True))
            #     clothes[lisa].swimsuit.cur = 1
            #
            # clothes[lisa].sleep = Clothes(_("Для сна"), [
            #         Garb('a', '02', 'Обычная одежда'),
            #         Garb('b', '02a', 'Маечка и трусики'),
            #     ])
            # if poss['sg'].stn > 2:
            #     clothes[lisa].sleep.cur = 1
            #
            # clothes[alice].casual = Clothes(_("Повседневная"), [
            #         Garb('a', '01a', 'Обычная одежда', True),
            #     ])
            # if 'pajamas' in alice.gifts:
            #     clothes[alice].casual.sel.insert(1, Garb('b', '01c', 'Пижама', True))
            #
            # clothes[ann].casual = Clothes(_("Повседневная"), [
            #         Garb('a', '01a', 'Обычная одежда', False, True),
            #         Garb('b', '01b', 'Футболка', False, True),
            #     ])
            # clothes[ann].casual.rand = True
            # clothes[ann].cook_morn = Clothes(_("Для приготовления завтрака"), [
            #         Garb('a', '05b', 'Спортивная форма + фартук', False, True),
            #         Garb('b', '01c', 'Футболка + фартук', False, True),
            #     ])
            # clothes[ann].cook_morn.rand = True
            # clothes[ann].cook_eve = Clothes(_("Для приготовления ужина"), [
            #         Garb('b', '01c', 'Футболка + фартук', False, True),
            #     ])
            # clothes[ann].rest_eve = Clothes(_("Для вечернего отдыха"), [
            #         Garb('a', '01b', 'Футболка', False, True),
            #         Garb('b', '04b', 'Полотенце', False, True),
            #     ])
            # clothes[ann].rest_eve.rand = True
            # clothes[ann].sleep = Clothes(_("Для сна"), [
            #         Garb('a', '02', 'Обычная одежда для сна', True),
            #     ])
            # if 'nightie' in ann.gifts:
            #     clothes[ann].sleep.sel.append(Garb('b', '02f', 'НОЧНУШКА', True))
            #     clothes[ann].sleep.rand = True
            #
            # clothes[mgg].casual = Clothes(_("Повседневная"), [
            #         Garb('a', '01a', 'Обычная одежда', True),
            #     ])
            # if items['max-a'].have:
            #     clothes[mgg].casual.sel.append(Garb('b', '01b', 'МУЖСКИЕ МАЙКА И ШОРТЫ', True))
            #     clothes[mgg].casual.cur = 1
            #
            # del globals()['cloth_type']

    if current_ver < "0.03.9.005":
        $ current_ver = "0.03.9.005"

        # $ clothes[lisa].learn.name = _("За уроками")
        # $ clothes[ann].casual.sel[0].change = False
        # $ clothes[ann].casual.sel[1].change = False
        # $ clothes[ann].cook_morn.sel[0].change = False
        # $ clothes[ann].cook_morn.sel[1].change = False
        # $ clothes[ann].cook_eve.sel[0].change = False
        # $ clothes[ann].rest_eve.sel[0].change = False
        # $ clothes[ann].rest_eve.sel[1].change = False
        # if 'bikini' in lisa.gifts:
        #     $ clothes[lisa].swimsuit.cur = 1

    if current_ver < "0.03.9.007":
        $ current_ver = "0.03.9.007"

        # if 'nightie' in ann.gifts:
        #     $ clothes[ann].sleep.sel[1] = Garb('b', '02f', 'НОЧНУШКА', True)

    if current_ver < "0.03.9.008":
        $ current_ver = "0.03.9.008"

        # $ talk_var['al.tvgood'] = 0

        $ poss['alpha'].stages[0].ps = ""
        $ poss['alpha'].stages[2].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")
        $ poss['alpha'].stages[3].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        # $ flags['alice.drink'] = 0
        # $ talk_var['lisa.sh_br'] = 0
        # $ talk_var['lisa.footmass'] = -1
        # $ talk_var['lisa.handmass'] = -1

        $ poss['nightclub'].stages[6].ps = ""
        $ poss['nightclub'].stages[7].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

        # $ flags['talkaboutbath'] = 0

    if current_ver < "0.03.9.009":
        $ current_ver = "0.03.9.009"

        # $ EventsByTime['Kira arrival'] = CutEvent('08:40', label='Kira_arrival', desc='приезд Киры', variable="all([day>=18, GetWeekday(day)==6, talk_var['breakfast']==12, talk_var['dinner']==17])", cut=True)

    if current_ver < "0.03.9.010":
        $ current_ver = "0.03.9.010"
        # $ dcv['new_pun'] = Daily(done=True, enabled=True)
        # if 'bathrobe' in lisa.gifts and len(clothes[lisa].casual.sel)<2:
        #     $ clothes[lisa].casual.sel.insert(1, Garb('b', '04', _("ШЕЛКОВЫЙ ХАЛАТ"), True))

    if current_ver < "0.03.9.011":
        $ current_ver = "0.03.9.011"
        # $ clothes[ann].rest_morn = Clothes(_("Для утреннего отдыха"), [
        #         Garb('a', '01b', 'Футболка', False, True),
        #     ])

    if current_ver < "0.03.9.012":
        $ current_ver = "0.03.9.012"
        # $ talk_var['teachkiss'] = 0
        # $ talk_var['ask.teachkiss'] = []
        # $ dcv['lizamentor'] = Daily(done=True, enabled=True) # обучение Лизы
        $ poss['seduction'].stages[4].ps = ""
        $ poss['seduction'].stages.extend([
            PossStage("interface poss mentor ep05", _("Итак, Лиза поинтересовалась, чему же я собираюсь её учить. И сразу же поставила меня в глупую ситуацию. Я вроде бы должен её учить, но сам не умею даже целоваться! Нужно срочно найти кого-то, кто бы мне помог в этом... Да, легко сказать...")),
            PossStage("interface poss mentor ep06", _("Кажется, я нашёл ту, которая научит меня целоваться. И это... моя тётя! Это так странно... Ну она точно в этом вопросе понимает достаточно. Да я был бы рад любому учителю, но такой - идеален! Да, тётя Кира сказала, что лучше об этом поговорить в более интимной обстановке. Например, когда она ночью смотрит телек.")),
            PossStage("interface poss mentor ep06", _("Тётя Кира превосходный учитель поцелуев! Она согласилась меня иногда учить. Кто знает, может быть она научит и чему-то ещё?\n\nНу всё. Теперь нужно практиковаться в поцелуях с тётей Кирой и передавать полученные знания Лизе... Только вот её ещё нужно убедить..."),
                    _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}"))])
        # if 'kira' in chars:
        #     $ talk_var['kira.porn'] = 0
        #     $ talk_var['kira.bath.mass'] = 0

    if current_ver < "0.03.9.014":
        $ current_ver = "0.03.9.014"
        if 'bikini' in lisa.gifts:
            if not 'gift_swimsuit.swimsuit_show' in persistent.memories:
                $ persistent.memories['gift_swimsuit.swimsuit_show'] = renpy.seen_label('gift_swimsuit.swimsuit_show')

        if renpy.seen_label('gift_pajamas'):
            if not 'gift_pajamas' in persistent.memories:
                $ persistent.memories['gift_pajamas'] = flags['alice_hugs'] > 3

        if renpy.seen_label('Lisa_HomeWork.first_foot_mass'):
            if not 'Lisa_HomeWork.first_foot_mass' in persistent.memories:
                $ persistent.memories['Lisa_HomeWork.first_foot_mass'] = True

    if current_ver < "0.03.9.015":
        $ current_ver = "0.03.9.015"

        # $ talk_var['kira.tv.touch'] = 0

    if current_ver < "0.03.9.016":
        $ current_ver = "0.03.9.016"

        # $ flags['kira.bath.fj'] = False
        # $ flags['kira.tv.bj'] = False

    if current_ver < "0.03.9.017":
        $ current_ver = "0.03.9.017"

        # $ kira.daily.shower = 0

    return


label after_load_04_0:
    # "04.0"
    if current_ver < "0.04.0.02":
        $ current_ver = "0.04.0.02"

        if GetRelMax('eric')[0] < -1:
            $ poss['alpha'].stages[2].used = False
            $ poss['alpha'].OpenStage(3)

    if current_ver < "0.04.0.03":
        $ current_ver = "0.04.0.03"

        # $ EventsByTime['night_of_fun'].tm = '02:30'

    if current_ver < "0.04.0.04":
        $ current_ver = "0.04.0.04"

        if items['max-a'].have:
            $ items['max-a'].block()
        if poss['nightclub'].stn >= 5 and kol_choco == 0:
            $ items['choco'].unblock()
        # if 'kira' in chars:
            # $ flags['hint.cources'] = False

        if talk_var['dinner'] > talk_var['breakfast']+4:
            $ talk_var['breakfast'] = 4
            $ talk_var['dinner'] = 4

    if current_ver < "0.04.0.05":
        $ current_ver = "0.04.0.05"
        # if 'talkaboutbath' not in flags:
        #     $ flags['talkaboutbath'] = 0

        if flags['talkaboutbath'] > 0 and not poss['nightclub'].used(5):
            $ flags['talkaboutbath'] = 0
            $ poss['nightclub'].stages[7].used = False
            if poss['nightclub'].used(4):
                $ poss['nightclub'].stn = 4
            elif poss['nightclub'].used(3):
                $ poss['nightclub'].stn = 3
            else:
                $ poss['nightclub'].stn = 2

        if all([kol_choco == 0, items['choco'].have]):
            $ items['choco'].have = False

    if current_ver < "0.04.0.06":
        $ current_ver = "0.04.0.06"

        if all([kol_choco == 0, items['choco'].have]):
            $ items['choco'].have = False

        python:
            for mem in persistent.memories:
                if persistent.memories[mem] == True:
                    persistent.memories[mem] = 1
                elif persistent.memories[mem] == False:
                    persistent.memories[mem] = -1

        if 'kira' in chars:
            $ added_mem_var('kira')
        if items['max-a'].have:
            $ added_mem_var('max-a')
        if 'pajamas' in alice.gifts:
            $ added_mem_var('pajamas')
        if 'bathrobe' in lisa.gifts:
            $ added_mem_var('bathrobe')

        if renpy.seen_label('kira_bath.kira_mass_bath_first'):
            $ added_mem_var('kira_mass_bath_first')

        if flags['kira.tv.bj']:
            $ added_mem_var('kira.tv.bj')

        if talk_var['al.tvgood'] > 0 and 'alice_talk_tv' not in persistent.memories:
            $ persistent.memories['alice_talk_tv'] = 1
        elif renpy.seen_label('alice_talk_tv.choco') and 'alice_talk_tv' not in persistent.memories:
            $ persistent.memories['alice_talk_tv'] = 0

        if renpy.seen_label('kira_night_tv.second_lesson') and 'kira_night_tv.first_lesson' not in persistent.memories:
            $ persistent.memories['kira_night_tv.first_lesson'] = 1
        if renpy.seen_label('kira_night_tv.repeat_lesson') and 'kira_night_tv.second_lesson' not in persistent.memories:
            $ persistent.memories['kira_night_tv.first_lesson'] = 1
            $ persistent.memories['kira_night_tv.second_lesson'] = 1

        if 'massage_sunscreen.spider' not in persistent.memories:
            $ persistent.memories['massage_sunscreen.spider'] = 0

    return


label after_load_04_1:
    # "04.1"
    if current_ver < "0.04.1.00":
        $ current_ver = "0.04.1.00"

        $ at_comp = False
        $ view_cam = Null

    if current_ver < "0.04.1.03":
        $ current_ver = "0.04.1.03"

        # $ dcv.update({
        #         'lisa_sweets' : Daily(done=True, enabled=True), # дарение сладости Лизе
        #         'alice_sweets': Daily(done=True, enabled=True), # дарение сладости Алисе
        #         'ann_sweets'  : Daily(done=True, enabled=True), # дарение сладости Анне
        #     })

        if 4 in sorry_gifts['alice'].give and sorry_gifts['alice'].owe:
            $ sorry_gifts['alice'].owe = False
            $ sorry_gifts['alice'].valid = {'ferrero-b', 'ferrero-m'}

    if current_ver < "0.04.1.04":
        $ current_ver = "0.04.1.04"

        # if 'warning' not in flags:
        #     $ flags['warning'] = False

    if current_ver < "0.04.1.05":
        $ current_ver = "0.04.1.05"

        # if 'cam_fun_alice' not in flags:
        #     $ flags['cam_fun_alice'] = False
        if not flags['cam2bath']:
            $ house[3].max_cam = 2
            if len(house[3].cams) > 1:
                $ house[3].cams.pop(1)

    if current_ver < "0.04.1.06":
        $ current_ver = "0.04.1.06"

        $ cam_poses = {}

    return


label after_load_04_5:
    # "04.5"
    if current_ver < "0.04.5.02":
        $ current_ver = "0.04.5.02"

        # if len(clothes[lisa].learn.sel)>2 and not clothes[lisa].learn.sel[2].change:
        #     $ clothes[lisa].learn.sel[2].change = True
        #     $ clothes[lisa].learn.sel[2].rand = True

        if kol_choco == 0 and items['choco'].have:
            $ items['choco'].have = False
        if poss['nightclub'].stn >= 5 and kol_choco == 0:
            $ items['choco'].unblock()

    if current_ver < "0.04.5.05":
        $ current_ver = "0.04.5.05"

        # $ dcv['lisa_mentor'] = Daily(done=True, enabled=True) # попытка обучения Лизы
        $ talk_var['kiss_lessons'] = 0 # количество успешно проведённых уроков поцелуев с Лизой
        $ poss['seduction'].stages[7].ps = ''
        $ poss['seduction'].stages.extend([
                PossStage("interface poss mentor ep08", _("Я поговорил с Лизой насчёт её обучения. Она выдвинула ряд условий, среди которых запрет мне к ней прикасаться, если она против. Ну уже что-то."), _("Похоже обучаться Лиза согласна только если у неё хорошее настроение...")), #8
                PossStage("interface poss mentor ep09", _("Мне удалось впечатлить Лизу своим искусством целоваться! Хотя, пока на искусство это не тянет, но ей понравилось! Всё-таки, тётя Кира отличный учитель. Но нужно продолжать практиковаться.")), #9
                PossStage("interface poss mentor ep10", _("Лиза намекнула, что не против двигаться дальше и я решил увлечь её поцелуями настолько, чтобы ей нравились при этом и мои прикосновения. А для этого нужно больше целоваться с тётей Кирой по ночам...")), #10
                PossStage("interface poss mentor ep10", _("Лизе очень нравится как я целуюсь. Она даже намекнула, что пора бы научить её ещё чему-то полезному. На этот раз, как мне кажется, стоит подтянуть теорию. Может быть, купить ей какую-то книжку по анатомии, чтобы она разобралась в физиологии и поняла, какие естественные процессы могут происходить между мужчинами и женщинами?")), #11
                PossStage("interface poss mentor ep12", _("Я решил, что и мне самому будет полезно прочитать купленную для Лизы книгу. Вдруг, тем самым, я что-то для себя интересное открою...")), #12
                PossStage("interface poss mentor ep12", _("Книга прочитана! Не то, чтобы много всего нового я для себя открыл, но есть то, что может помочь нам с Лизой ещё больше сблизиться. А пока можно ей книжку подарить...")), #13
                PossStage("interface poss mentor ep12", _("Я подарил Лизе книжку, которая содержит много ответов на её вопросы. Нужно будет поинтересоваться через какое-то время, что она об этой книге думает..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")), #14
                PossStage("interface poss mentor ep12", _("Я подарил Лизе книжку, которая содержит много ответов на её вопросы. Да мне и самому было бы полезно её почитать, но лень.\n\n\nНужно будет поинтересоваться через какое-то время, что она об этой книге думает..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")) #15
            ])

    if current_ver < "0.04.5.06":
        $ current_ver = "0.04.5.06"

        # $ talk_var['kiss_massage'] = 0 # количество поцелуев во время массажа рук
        if GetKolCams(house)==9:
            $ items['hide_cam'].give()

    if current_ver < "0.04.5.07":
        $ current_ver = "0.04.5.07"

        $ clothes[alice].sleep = Clothes(_("Для сна"), [
                Garb('a', '02', 'Белое кружевное бельё', True),
            ])

    if current_ver < "0.04.5.08":
        $ current_ver = "0.04.5.08"

        $ poss['blog'].stages = poss['blog'].stages[:1]
        $ poss['blog'].stages.extend([
                    PossStage("interface poss blog ep02", _("В результате поисков информации в интернете о том, чем могла бы заняться Алиса, удалось кое-что выяснить. Самыми популярными оказались блоги, где ведущие - девушки. Причём, чем более откровенные наряды и чем больше грудь, тем более популярны шоу. С грудью, конечно, ничего не поделать, а вот наряды... Может быть, поговорить с ней об этом?")),  #1
                    PossStage("interface poss blog ep03", _("Я пообщался с Алисой насчёт своих выводов о популярности блога и намекнул, что можно рекламировать не только крема и лаки, но и нижнее бельё, например. Но крутить своей попкой перед камерой она не собирается, так что покрутит сама того не зная, когда я поставлю скрытую камеру в её комнату. Как знать, сколько всего интересного можно будет увидеть...")),  #2 камера не установлена
                    PossStage("interface poss blog ep03", _("Я пообщался с Алисой насчёт своих выводов о популярности блога и намекнул, что можно рекламировать не только крема и лаки, но и нижнее бельё, например. Но крутить своей попкой перед камерой она не собирается... А зря, ведь она и так уже это делает на скрытую камеру, которую я поставил в её комнате. Как знать, может мне удастся увидеть что-то, чего ещё не было...")),  #3 камера уже установлена
                    PossStage("interface poss blog ep03", _("Я решил снова предложить Алисе идею по развитию её блога - рекламировать нижнее бельё. Удивительно, но она согласилась! Правда, теперь мне нужно найти нижнее бельё для того, чтобы она заинтересовала свою аудиторию и привлекла внимание рекламодателей...")),  #4
                    PossStage("interface poss blog ep04", _("Я подарил Алисе симпатичный комплект нижнего белья. Ей очень понравилось. Она даже при мне его примерила! Правда, я почти ничего не увидел, но было волнующе... Что самое любопытное, она намекнула, что можно поискать и что-то более... сексуальное!")),
                    # PossStage("interface poss blog ep05", _("Мой очередной подарок Алисе произвёл эффект, но не совсем тот, на который я расcчитывал. Чёрное маленькое боди без верха не подойдёт для её блога... Однако, подойдёт для кого-то, но для кого она не сказала... Столько секретов..."),
                    #           _("Ах да! Алиса сообщила, что с нею связался какой-то рекламодатель, который будет высылать ей нижнее бельё и потом платить за это! Теперь я ей больше не нужен...")),
                ])
        if day > 2 and not poss['blog'].used(0):
            $ poss['blog'].OpenStage(0)
        if poss['blog'].stn==1:
            $ poss['blog'].OpenStageStage(1)
        # $ flags['cam_fun_alice'] = False

    if current_ver < "0.04.5.09":
        $ current_ver = "0.04.5.09"

        # $ items['b.lingerie'] = Item(_("КОМПЛЕКТ ТЁМНОГО НИЖНЕГО БЕЛЬЯ"), _("Отличное нижнее бельё тёмного цвета. Отличный подарок для любимой девушки."), 'lingerie', 0, 350, cells=2)

    if current_ver < "0.04.5.10":
        $ current_ver = "0.04.5.10"

        # $ items['sex.ed'] = Item(_("СЕКС-ОБРАЗОВАНИЕ"), _("Книга обо всём, связанным с сексом. Отлично подходит для обучения подрастающего поколения."), 'sex-ed', 1, 150, need_read=4)
        if talk_var['kiss_lessons'] >= 9:
            $ poss['seduction'].OpenStage(11)
            $ items['sex.ed'].unblock()
        $ poss['seduction'].stages[14].ps = _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")

    if current_ver < "0.04.5.11":
        $ current_ver = "0.04.5.11"

        $ poss['blog'].stages = poss['blog'].stages[:5]
        $ poss['blog'].stages.extend([
                PossStage("interface poss blog ep04", _("Я подарил Алисе симпатичный комплект нижнего белья. Ей очень понравилось. Правда, увидеть мне ничего не удалось, только Алису уже в этом самом белье, но даже это было волнующе... Что самое любопытное, она намекнула, что можно поискать и что-то более... сексуальное!")),  # 5
                PossStage("interface poss blog ep04", _("Я подарил Алисе симпатичный комплект нижнего белья. Ей очень понравилось. Она даже при мне его примерила! Увидел я не так чтобы много всего, но было волнующе... Что самое любопытное, она намекнула, что можно поискать и что-то более... сексуальное!")),  # 6
            ])

        # $ peeping['alice_blog'] = 0
        # $ EventsByTime['Wearied'].tm = '03:50'

    if current_ver < "0.04.5.12":
        $ current_ver = "0.04.5.12"

        # $ flags['double_mass_alice'] = 0

    if current_ver < "0.04.5.13":
        $ current_ver = "0.04.5.13"

        $ items['photocamera'] = Item(_("ФОТОАППАРАТ"), _("Профессиональный фотоаппарат с объективом. Не новый, но в отличном состоянии. Подойдёт как для новичков, так и для профессионалов."), 'photocamera', 3, 500)
        # $ items['nightie2']    = Item(_("КОРОТКАЯ ПИКАНТНАЯ СОРОЧКА"), _("Соблазнительная чёрная сорочка выполнена из эластичного тюля. В комплект так же входят трусики-стринги."), 'nightie2', 0, 200, cells=2)

    if current_ver < "0.04.5.14":
        $ current_ver = "0.04.5.14"

        $ poss['aunt'] = Poss([
                PossStage("interface poss aunt ep01", _("Итак, к нам приехала тётя Кира, мамина младшая сестра. Конечно, и раньше не были замечены у неё какие-либо комплексы, но сейчас она стала такой... такой... А ещё она увидела мой член, в первый же день! Так неловко. Но и себя тётя Кира показала во всей красе, в таком купальнике, если его можно назвать купальником... Да ещё такие намёки на моего папу. Неужели, они были настолько... знакомы? Нужно выпытать у неё всё, что только возможно.")), #0
                PossStage("interface poss aunt ep02", _("Я рассказал тёте Кире всё про Эрика, вот как есть, так и сказал. Кажется, она сомневается в моих словах, но пообещала аккуратно всё выяснить и разузнать. Может быть, даже с самим Эриком пообщается...")), #1
                PossStage("interface poss aunt ep03", _("Вот это да! Моя тётя снимается в порно! Неужели, я живу рядом с порнозвездой? Теперь понятно, почему меня к ней так и тянет. Её просто окружает аура секса! Может быть, ещё больше сблизиться с ней будет не так сложно, как я думал...")), #2
                PossStage("interface poss aunt ep03", _("Кира предложила мне немного заработать. Нужно лишь её пофотографировать. Вот только для этих целей нужен фотоаппарат. Конечно, вряд-ли она заплатит мне столько, сколько стоит фотоаппарат, зато есть шанс, что мне что-нибудь обломится другое за эту фотосессию...")), #3
                PossStage("interface poss aunt ep05", _("Фотосессия вышла классная, хоть ничего нового я для себя и не открыл. Ну почти, были интересные моменты, а это намного лучше, чем вообще ничего! Теперь нужно немного подождать, чтобы стало понятно, насколько удачными получились снимки. Может я даже что-то и получу за эту фотосессию...")), #4
                PossStage("interface poss aunt ep05", _("Итак, снимки вышли удачными и мы с Кирой договорились на новую фотосессию, пока никого не будет дома. Но ещё не ясно, когда мы её проведём... Интересно, что такое Кира хочет достать для съёмок!? Остаётся только ждать..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")), #5
            ])
        if 'kiratalk' in dcv:
            if dcv['kiratalk'].stage>=1:
                $ poss['aunt'].OpenStage(0)
            if dcv['kiratalk'].stage>=3:
                $ poss['aunt'].OpenStage(1)
            if dcv['kiratalk'].stage>=4:
                $ poss['aunt'].OpenStage(2)
            if dcv['kiratalk'].stage>=5:
                $ poss['aunt'].OpenStage(3)
                $ poss['aunt'].stages[3].ps = _("А ещё, будет не лишним, купить для этой фотосессии сексуальную сорочку для моей любимой тёти!")

    if current_ver < "0.04.5.15":
        $ current_ver = "0.04.5.15"

        if talk_var['dinner'] >= 11:
            call alice_init_nightclub from _call_alice_init_nightclub_1

        # $ EventsByTime['MorningWoodCont'].variable="all([day>=7, dcv['mw'].done, flags['morning_erect']%2==0, 0<poss['seduction'].stn<5])"
        # $ EventsByTime['MorningWoodCont2'] = CutEvent('06:30', label='MorningWoodCont2', desc='периодический утренний стояк', variable="all([poss['seduction'].stn>10, dcv['mw'].done, lisa.GetMood()[0]>2])", sleep=True, cut=True)

    if current_ver < "0.04.5.16":
        $ current_ver = "0.04.5.16"

        # $ flags['promise.cuni.kira'] = False  # Макс получил дрочку в бассене и пообещал куни
        $ flags['hj_in_pool'] = 0  # не было дрочек в бассейне
        # $ dcv['kiratalkcuni'] = Daily(done=True, enabled=True)

    if current_ver < "0.04.5.17":
        $ current_ver = "0.04.5.17"

        $ poss['Christine'] = Poss([
                    PossStage("interface poss chris ep01", _("Моими подозрительными заказами всякой женской одежды заинтересовалась девчонка из доставки. Как выяснилось, её зовут Кристина. \nЯ не решился подкатить к ней... Она бы меня наверняка отшила. Хотя, попробовать всё равно можно было..."),  #0
                                _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),
                    PossStage("interface poss chris ep01", _("Моими подозрительными заказами всякой женской одежды заинтересовалась девчонка из доставки. Как выяснилось, её зовут Кристина. \nНе самым умным решением было к ней сразу же подкатывать, но что сделано, то сделано. Понятно, что она бы в любом случае меня отшила, но попробовать стоило..."), #1
                                _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),
            ])

    if current_ver < "0.04.5.18":
        $ current_ver = "0.04.5.18"

        # $ talk_var['eric.fee'] = 0
        # $ talk_var['eric.voy.stage'] = 0 if GetRelMax('eric')[0]>3 else -1
        # $ dcv['eric.money'] = Daily(done=True, enabled=True)

    if current_ver < "0.04.5.19":
        $ current_ver = "0.04.5.19"

        $ poss['control'] = Poss([
                    PossStage("interface poss control ep01", _("Что это было? Мама поймала меня на подглядывании за ними, пока они трахались, собиралась наказать, но Эрик сказал нет и мама согласилась?! Моя мама, которая запрещала мне смотреть даже эротику, согласилась, чтобы я присутствовал при таком? Это невероятно. Либо Эрик какой-то колдун, либо дело в другом и нужно в этом разобраться, как следует."),  #0
                                _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),
            ])

    return


label after_load_05_0:
    # "05.0"
    if current_ver < "0.05.0.01":
        $ current_ver = "0.05.0.01"

        # if clothes[alice].sleep is None:
        #     $ clothes[alice].sleep = Clothes(_("Для сна"), [
        #             Garb('a', '02', 'Белое кружевное бельё', True),
        #         ])

    if current_ver < "0.05.0.02":
        $ current_ver = "0.05.0.02"

        if items['photocamera'].InShop and (items['photocamera'].have or items['photocamera'].bought) and not items['nightie2'].InShop:
            $ purchased_items.append(items['photocamera'])

    if current_ver < "0.05.0.06":
        $ current_ver = "0.05.0.06"

        if flags['hj_in_pool']:
            $ added_mem_var('hj_in_pool')

        if renpy.seen_label('advanced_massage1'):
            $ added_mem_var('advanced_massage1')

    # if current_ver < "0.05.0.07":
    #     $ current_ver = "0.05.0.07"

        # $ clothes[alice].casual.name = _("Повседневная")

        # if len(clothes[alice].sleep.sel) < 2 and 'black_linderie' in alice.gifts:
        #     $ clothes[alice].sleep.sel.append(Garb('b', '02ia', "Тёмое кружевное бельё", True))
        #     $ clothes[alice].sleep.cur = 1
        #     $ clothes[alice].sleep.rand = True

    return


label after_load_06_0:
    # "06.0"
    if current_ver < "0.06.0.00":
        $ current_ver = "0.06.0.00"

        if 'aunt' in poss and poss['aunt'].stn == 5:
            $ append_photo('01-Kira', 12)

        if poss['sg'].stn == 2 and talk_var['truehelp'] > 5:
            $ poss['sg'].stages[2].ps = _("А что если я не буду помогать Лизе какое-то время? Или несколько раз сделаю ошибку в её работе?")

        $ poss['seduction'].stages[12].desc = _("Я решил, что и мне самому будет полезно прочитать купленную для Лизы книгу. Вдруг, тем самым, я что-то для себя интересное открою...")

        $ poss['seduction'].stages[14].ps = ''
        $ poss['seduction'].stages[15].ps = ''

        $ poss['seduction'].stages.extend([
                PossStage("interface poss alpha ep02", _("Только я подарил Лизе книгу по сексуальному образованию, как тут же нарисовался Эрик. Он, видите ли, вместе с моей мамой, собирается взяться за её сексуальное воспитание! \n\nВ обмен на возможность подглядывать за этим процессом и кое-каким бонусом, с которым мне нужно будет определиться со временем, я согласился его поддержать. Мы же с ним как-никак \"друзья\".")), #16
                PossStage("interface poss alpha ep02", _("Только я подарил Лизе книгу по сексуальному образованию, как тут же нарисовался Эрик. Он, видите ли, вместе с моей мамой, собирается взяться за её сексуальное воспитание! \n\nВ обмен на возможность подглядывать за этим процессом, я согласился его поддержать. Незачем мне враждовать с Эриком.")), #17
                PossStage("interface poss alpha ep02", _("Только я подарил Лизе книгу по сексуальному образованию, как тут же нарисовался Эрик. Он, видите ли, вместе с моей мамой, собирается взяться за её сексуальное воспитание! \n\nНе смотря на то, что мы с ним \"дружим\", я постарался убедить его, что Лизе ещё рановато это познавать... Это не особо помогло, но Эрик дал мне пару недель на \"чтение книг по теме сексуального образования\" с Лизой. По крайней мере, я выиграл немного времени, которое стоит использовать с умом...")), #18
                PossStage("interface poss alpha ep02", _("Только я подарил Лизе книгу по сексуальному образованию, как тут же нарисовался Эрик. Он, видите ли, вместе с моей мамой, собирается взяться за её сексуальное воспитание! \n\nЯ, естественно, отказался ему в этом содействовать. Враждовать, так враждовать! Вряд ли теперь у меня есть много времени, чтобы избавиться от него, так что нужно скорее искать такой способ...")), #19
                PossStage("interface poss mentor ep20", _("Как выяснилось, Эрик проплатил репетитора для Лизы по воскресеньям, чтобы улучшить её оценки, а в действительности, чтобы втереться к ней в доверие. Теперь он и моя мама будут по понедельникам проводить для Лизы уроки сексуального воспитания..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")), #20
                PossStage("interface poss mentor ep21", _("Как выяснилось, Эрик проплатил дополнительные курсы для Лизы в школе, чтобы улучшить её оценки, а в действительности, чтобы втереться к ней в доверие. А заодно и от меня отстранить, ведь теперь моя помощь с уроками ей особо и не нужна. И ещё он и моя мама будут по понедельникам проводить для Лизы уроки сексуального воспитания..."),
                        _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")), #21

            ])

        $ poss['blog'].stages.extend([
                PossStage("interface poss blog ep06", _("Я подобрал кое-что более сексуальное для Алисы, а именно - полупрозрачное боди. В меру откровенное, потому что иначе я рискую не увидеть его на ней. А при дарении, пока она была под впечатлением, я ещё и умудрился уговорить её попозировать мне... нужны же ей качественные фотоснимки для развития блога! \n\nМного я не наснимал, всё-таки мы с Алисой ещё не настолько близки, но уже лучше находим общий язык. Посмотрим, что будет дальше...")), #7
                PossStage("interface poss blog ep06", _("Я подобрал кое-что более сексуальное для Алисы, а именно - полупрозрачное боди. В меру откровенное, потому что иначе я рискую не увидеть его на ней. А при дарении, пока она была под впечатлением, я ещё и умудрился уговорить её попозировать мне... нужны же ей качественные фотоснимки для развития блога! \n\nФотосессия вышла очень интересной, спасибо за это конфетам с алкоголем. Мне удалось сделать несколько весьма горячих снимков с Алисой и они прекрасно подойдут для моей коллекции... Хоть мы с Алисой всё ещё не очень близки, но уже лучше находим общий язык. Посмотрим, что будет дальше...")),  #8
                PossStage("interface poss alpha ep02", _("Только мои отношения с Алисой начали понемногу налаживаться, как ко мне подвалил Эрик с расспросами о том, чем там моя старшая сестрёнка занимается за компьютером... \n\nЯ рассказал ему всё, что знал о её блоге. Ну а как иначе, мы же друзья. Теперь он собирается помочь ей с развитием блога и мне лучше этому не мешать... а ещё лучше - помогать ему с этим.")),  #9
                PossStage("interface poss alpha ep02", _("Только мои отношения с Алисой начали понемногу налаживаться, как ко мне подвалил Эрик с расспросами о том, чем там моя старшая сестрёнка занимается за компьютером... \n\nЯ решил не облегчать ему жизнь и сказал, что мало об этом знаю. Эрик же, чтобы не тратить своё время, попросил меня за несколько недель узнать как можно больше о занятиях Алисы...")),  #10
                PossStage("interface poss alpha ep02", _("Только мои отношения с Алисой начали понемногу налаживаться, как ко мне подвалил Эрик с расспросами о том, чем там моя старшая сестрёнка занимается за компьютером... \n\nЯ решил прекратить вражду с Эриком и рассказал ему всё, что знал о её блоге. Теперь он собирается помочь ей с развитием блога и мне лучше этому не мешать... а ещё лучше - помогать ему с этим.")),  #11
                PossStage("interface poss alpha ep02", _("Только мои отношения с Алисой начали понемногу налаживаться, как ко мне подвалил Эрик с расспросами о том, чем там моя старшая сестрёнка занимается за компьютером... \n\nУ меня совершенно нет желания помогать ему подкатывать к моей сестрёнке, что ему и сказал. У нас ведь вражда! Главное, чтобы мне это боком не вышло...")),  #12
                PossStage("interface poss blog ep08", _("Теперь, каждую среду, пока мама принимает ванну, Эрик тусуется у Алисы в комнате, якобы помогая ей с блогом. Понятно, что на самом деле он хочет поглазеть на Алису в нижнем белье... а в будущем и в трусики к ней залезть.")),  #13
                PossStage("interface poss blog ep08", _("Теперь, каждую среду, пока мама принимает ванну, Эрик тусуется у Алисы в комнате, якобы помогая ей с блогом. Понятно, что на самом деле он хочет поглазеть на Алису в нижнем белье... а в будущем и в трусики к ней залезть.\n\nА ещё мне повезло узнать, что Эрик собирается купить ей новое кружевное боди! Обидно, конечно, что она попросила об этом не меня. Интересно, как Эрик отреагирует, если я его опережу с покупкой...")),  #14
                PossStage("interface poss blog ep09a", _("Эрик подарил Алисе кружевное боди, которое она просила. Похоже, это их сблизило, чего он и добивался. И будет добиваться дальше..."),
                          _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),  #15
                PossStage("interface poss blog ep09b", _("Эрик подарил Алисе кружевное боди, которое она просила. Похоже, это их сблизило, чего он и добивался, а вот я не успел его обойти. Нужно скорее избавляться от Эрика, иначе он заберёт у меня всё..."),
                          _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),  #16
                PossStage("interface poss blog ep09c", _("Мне удалось опередить Эрика с покупкой кружевного боди и подарить его Алисе первым! Она даже переоделась при мне и не слишком при этом прикрывалась. Правда в конце у неё ногу свело, но это значит, что у меня теперь есть весомый повод забраться в массаже её прелестных ножек несколько дальше, чем раньше... И мне стоит попробовать это сделать!")),  #17
                PossStage("interface poss alpha ep02", _("Эрик оказался, мягко говоря, не в восторге от того, что я опередил его с дарением кружевного боди для Алисы.\n\nОн предупредил, что если я ещё раз испорчу его планы, друзьями нам дальше не быть... А в качестве наказания, лишил меня всех возможных \"премиальных\", что мне теперь нужно как-то исправить..."),
                          _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),  #18
                PossStage("interface poss alpha ep02", _("Эрик оказался, мягко говоря, не в восторге от того, что я опередил его с дарением кружевного боди для Алисы.\n\nОн пригрозил, что у меня теперь будут большие проблемы! Как будто меня этим можно испугать..."),
                          _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),  #19
            ])

        $ poss['discrediting'] = Poss([
                PossStage("interface poss discrediting ep01", _("Мне случайно удалось заметить, как Эрик посреди ночи стоит около окна в комнату Алисы и дрочит на неё! Не ожидал я такое увидеть... Мне казалось, что Эрик из тех, кто скорее проститутку снимет, чем будет просто дрочить, но как оказалось... я ошибался.\n\nНаверняка он делает это уже не первый раз! Надо понаблюдать за ним по ночам, чтобы заполучить снимок с его грязными делишками... Лучше иметь против него козырь, на случай чего...")),  #0
                PossStage("interface poss discrediting ep01", _("Получилось! Я сфотографировал, как Эрик дрочит на Алису! Конечно, на самом деле на снимке не понятно, на кого или на что он дрочит, так что не слишком-то эта фотография мне поможет в случае какой-нибудь заварушки с Эриком.\n\nБыло бы хорошо, если бы Эрик обнаглел настолько, что стал дрочить на Алису прямо посреди её комнаты... Вот это уже бы тянуло на компромат! В кадр правда попадёт Алиса, но основное внимание на такой фотографии будет приковано к Эрику. Дело за малым - придумать, как заманить его в комнату Алисы...")),  #1
                PossStage("interface poss discrediting ep03", _("Я так и знал, что Эрик не устоит перед голой и спящей Алисой! Правда, можно ли его за это винить? Я бы на его месте тоже не устоял... Теперь, остаётся лишь успеть сделать снимок, пока он в её комнате...")),  #2
                PossStage("interface poss discrediting ep03", _("Вот всё и получилось! У меня есть два снимка, на которых Эрик, как грязный извращенец, дрочит пока все спокойно спят... А на одном из снимков даже видно на кого он дрочит...\n\nМне стоит быть осторожнее с этими снимками, Эрик столько всего делает для моих сестёр, что они запросто могут рассказать о том, что у меня есть. А так же хорошенько подумать над тем, как я буду использовать эти снимки.\n\nЯ могу придержать этот компромат, пойти с ним к Эрику в ближайшее время или же вовсе как-то подставить его..."),
                          _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")),  #3
            ])

        $ talk_var.update({
                'fight_for_Lisa'  : 0,  # битва за Лизу, стадии
                'fight_for_Alice' : 0,  # битва за Алису
                'ae_lisa_number'  : -1, # "урок", проведённый Эриком (и Аней) с Лизой
                'fight_for_Kira'  : 0,  # битва за Киру
                'bonus_from_eric' : ['money',],
            })

        # $ EventsByTime.update({
        #         'Eric_talkLisa0'  : CutEvent('20:00', (6, ), 'Eric_talk_about_Lisa_0', "разговор с Эриком о Лизе", "all([GetWeekday(day)==6, poss['seduction'].stn in [14, 15], talk_var['fight_for_Lisa']==0, dcv['lizamentor'].lost<7, ('sexbody1' not in alice.gifts or talk_var['fight_for_Alice']>3)])", cut=True),
        #         'Eric_talkLisa1'  : CutEvent('20:00', (6, ), 'Eric_talk_about_Lisa_1', "разговор с Эриком о Лизе в случае 'отсрочки'", "all([GetWeekday(day)==6, talk_var['fight_for_Lisa']==2, dcv['ae_ed_lisa'].enabled, dcv['ae_ed_lisa'].done])", cut=True),
        #         'Eric_talkAlice0' : CutEvent('20:00', (6, ), 'Eric_talk_about_Alice_0', "разговор с Эриком о Алисе", "all([GetWeekday(day)==6, talk_var['fight_for_Alice']==0, 'sexbody1' in alice.gifts, (talk_var['fight_for_Lisa']==0 or talk_var['fight_for_Lisa']>3)])", cut=True),
        #         'Eric_talkAlice1' : CutEvent('20:00', (6, ), 'Eric_talk_about_Alice_1', "разговор с Эриком о Алисе в случае 'отсрочки'", "all([GetWeekday(day)==6, talk_var['fight_for_Alice']==2, dcv['eric_alice'].enabled, dcv['eric_alice'].done])", cut=True),
        #         'Eric_ab_laceling': CutEvent('20:00', (6, ), 'Eric_talk_about_lace_lingerie', "разговор с Эриком, если Макс подарил бельё Алисе", "all([GetWeekday(day)==6, 'sexbody2' in alice.gifts, 4<dcv['eric.lingerie'].stage<7])", cut=True),
        #     })

        # $ peeping['ael_sexed'] = 0  # подсматривание за сек.уроками Лизы

        $ dcv.update({
                'ae_ed_lisa'     : Daily(done=True),  # до следующего урока Лизы у АиЭ
                'film_punish'    : Daily(done=True),  # пока счетчик не прошёл, Макс должен посмотреть с Лизой фильм
                'kira.nextphoto' : Daily(done=True),  # отсрочка до следующей фотосессии с Кирой
                'eric_alice'     : Daily(done=True),  # отсрочка у Эрика по Алисые
                'gift.lingerie'  : Daily(done=True),  # фотосессии Алисы в нижнем белье
                'about_blog'     : Daily(done=True, enabled=True),  # интересуемся у Алисы, как дела с блогом (в нижнем белье)
                'eric.lingerie'  : Daily(done=True),  # по истечении Эрик подарит бельё Алисе (борьба на опережение)
                'lisa.punpause'  : Daily(done=True),  # во время паузы невозможны наказания без подставы
                'alice.punpause' : Daily(done=True),
                'alice.prudence' : Daily(done=True),  # дни благоразумия (Алиса не нарушает условий Макса)
            })

        $ wcv = {
                'catch.Kira' : Weekly(4),  # счетчик недель до гарантированного спаливания Киры Эриком (после активации)
            }

        $ flags.update({
                'l.ab_aeed'         : False,  # состоялся разговор с Лизой о последнем уроке АиЭ (доступен один раз в течении текущей недели)
                'dinner_ab_lisa'    : False,  # разговор за ужином о доп.обучении Лизы
                'dinner_ab_earn'    : False,  # разговор за ужином о доходах Макса и старт секс.обучения Лизы в случае отсрочки
                'film_punish'       : False,  # после подглядывания за Лизой Макс должен посмотреть с ней фильм
                'dinner_ab_earn'    : False,  # разговор за ужином о доходах Макса и старт секс.обучения Лизы в случае отсрочки
                'film_punish'       : False,  # после подглядывания за Лизой Макс должен посмотреть с ней фильм
                'lisa.stopkiss'     : 0,      # нужно прекратить поцелуи с Лизой
                'strip.show'        : False,  # Кира спит голой после стриптиза
                'eric.jerk'         : False,  # Эрик дрочит на Алису
                'eric.noticed'      : False,  # в этот день Эрик замечен за дрочкой
                'eric.firstjerk'    : False,  # первый раз заметили Эрика
                'eric.photo1'       : 0,
                'eric.photo2'       : 0,
            })

        # вещи
        $ items.update({
                "sexbody1" : Item(_("ЧЁРНОЕ СЕКСУАЛЬНОЕ БОДИ"), _("Прозрачное сетчатое боди с открытой спиной чёрного цвета."), 'sexbody1', 0, 500, False, cells=2),
                "sexbody2" : Item(_("ЧЁРНОЕ КРУЖЕВНОЕ БОДИ"), _("Женское сексуальное нижнее бельё с кружевным узором по краям."), 'sexbody2', 0, 450, False, cells=2),
            })

        # влияние
        $ infl = {
            lisa : Influence(),
            ann : Influence(),
            alice : Influence(),
            }

        if 'kira' in chars:
            $ infl[kira] = Influence()

        if poss['Swimsuit'].used(3):
            $ infl[lisa].add_m(30, True)
        else:
            $ infl[lisa].add_e(30, True)

        if poss['nightclub'].stages[4]:
            $ infl[alice].add_m(30, True)
        else:
            $ infl[alice].add_e(30, True)

        if 'bathrobe' in lisa.gifts:
            $ infl[lisa].add_m(30, True)

        if 'pajamas' in alice.gifts:
            $ infl[alice].add_m(30, True)

        if 'black_linderie' in alice.gifts:
            $ infl[alice].add_m(30, True)

        $ infl[ann].add_e(150, True)
        if 'nightie' in ann.gifts:
            $ infl[ann].add_m(30, True)

        $ prenoted = 0  # замечено отсутствие Эрика в комнате Ани

        # $ peeping['blog_with_eric'] = 0

        if 'kira' in chars:
            $ poss['aunt'].stages.append(PossStage("interface poss aunt ep07", _("Вот и состоялась вторая фотосессия! И она была отпадной! Не только потому что Кира решила пофотографироваться на тему БДСМ, но и потому что у нас был секс... Мой первый, настоящий секс... Теперь я официально больше не девственник! Вернее, неофициально... я ведь трахался с тётей. Надеюсь, не в последний раз! Хотя, с этим Эриком, который во всё лезет, лучше быть очень осторожным..."),
                    _("{i}{b}Внимание:{/b} Пока это всё, что можно сделать для данной \"возможности\" в текущей версии игры.{/i}")))

        # $ flags['noclub'] = False

    if current_ver < "0.06.0.01":
        $ current_ver = "0.06.0.01"

        while alice.gifts.count('sexbody2') > 1:
            $ alice.gifts.remove('sexbody2')

        $ poss['blog'].stages[15].image = 'interface poss blog ep09a'
        $ poss['blog'].stages[16].image = 'interface poss blog ep09b'
        $ poss['blog'].stages[17].image = 'interface poss blog ep09c'

    if current_ver < "0.06.0.02":
        $ current_ver = "0.06.0.02"

        if 'sexbody2' in alice.gifts:
            $ items['sexbody2'].have = False

    if current_ver < "0.06.0.04":
        $ current_ver = "0.06.0.04"

        if poss['blog'].stn in [15, 16] and dcv['eric.lingerie'].stage < 8:
            $ dcv['eric.lingerie'].stage = 8

    if current_ver < "0.06.0.05":
        $ current_ver = "0.06.0.05"

        # if 'black_linderie' in alice.gifts and 'cam_pose_blog' not in globals():
        #     $ cur_blog_lingerie = ''
        #     $ cam_pose_blog = []

        $ poss['blog'].stages[14].ps = _("Если я хочу это сделать, то нужно торопиться, чтобы успеть подарить ей боди до субботы... И дарить надо, когда Алиса занимается блогом, тогда она может быть переоденется при мне!")

        $ __poss20 = __poss18 = False
        if poss['blog'].used(19):
            $ poss['blog'].stages[19].used = False
            $ __poss20 = True
        if poss['blog'].used(18):
            $ poss['blog'].stages[18].used = False
            $ poss['blog'].stages[19].used = True
        if poss['blog'].used(17):
            $ poss['blog'].stages[17].used = False
            $ poss['blog'].stages[18].used = True
        if poss['blog'].used(16):
            $ poss['blog'].stages[16].used = False
            $ poss['blog'].stages[17].used = True
        if poss['blog'].used(15):
            $ poss['blog'].stages[15].used = False
            if dcv['eric.lingerie'].stage in [5, 7]:
                $ __poss18 = True
            else:
                $ poss['blog'].stages[16].used = True

        $ poss['blog'].stages.insert(15, PossStage("interface poss blog ep08", _("Теперь, каждую среду, пока мама принимает ванну, Эрик тусуется у Алисы в комнате, якобы помогая ей с блогом. Понятно, что на самом деле он хочет поглазеть на Алису в нижнем белье... а в будущем и в трусики к ней залезть.\n\nА ещё мне повезло узнать, что Эрик собирается купить ей новое кружевное боди! Обидно, конечно, что она попросила об этом не меня. Интересно, как Эрик отреагирует, если я его опережу с покупкой..."), _("Что бы я там не хотел, теперь уже поздно! Мне остаётся только наблюдать...")))  #15!

        $ poss['blog'].stages[16].desc = _("Эрик подарил Алисе кружевное боди, которое она просила. Похоже, это их сблизило, чего он и добивался, а вот я не успел его обойти. Нужно скорее избавляться от Эрика, иначе он заберёт у меня всё...")
        $ poss['blog'].stages[17].desc = _("Эрик подарил Алисе кружевное боди, которое она просила. Похоже, это их сблизило, чего он и добивался. И будет добиваться дальше...")

        if dcv['eric.lingerie'].stage == 8:
            $ poss['blog'].OpenStage(15)
        if dcv['eric.lingerie'].stage == 9:
            $ poss['blog'].OpenStage(17 if GetRelMax('eric')[0]>0 else 16)

        if __poss20:
            $ poss['blog'].OpenStage(20)

        python:
            for i in xrange(20, 15, -1):
                if poss['blog'].used(i) and poss['blog'].stn < i:
                    poss['blog'].stn = i
                    "break [i]"
                    break

    if current_ver < "0.06.0.06":
        $ current_ver = "0.06.0.06"

        if talk_var['fight_for_Lisa'] in [4, 5]:
            $ poss['seduction'].OpenStage(20)
        elif talk_var['fight_for_Lisa'] == 6:
            $ poss['seduction'].OpenStage(21)

    if current_ver < "0.06.0.07":
        $ current_ver = "0.06.0.07"

        # $ EventsByTime['night_of_fun'].tm = '02:50'

        # if len(clothes[lisa].learn.sel)>2:
        #     $ clothes[lisa].learn.sel[2].change = True
        #     $ clothes[lisa].learn.sel[2].rand = True
        # elif len(clothes[lisa].learn.sel)==2:
        #     $ clothes[lisa].learn.sel[1].change = True
        #     $ clothes[lisa].learn.sel[1].rand = True

        #### для воспоминаний ##################################################

        # первая фотосессия Киры
        if renpy.seen_label('first_photoset') and 'kira_photoset1' not in persistent.mems_var:
            $ added_mem_var('kira_photoset1')

        # Алиса. Примерка боди с фотосессией
        if renpy.seen_label('alice_body_photoset1') and 'alice_photoset1' not in persistent.mems_var:
            $ added_mem_var('alice_photoset1')

        # Алиса. Макс опередил Эрика
        if renpy.seen_label('gift_lace_lingerie') and 'lace_ling_max1' not in persistent.mems_var:
            $ added_mem_var('lace_ling_max1')

        # Алиса. Эрик опередил Макса
        if all([renpy.seen_label('gift_lace_lingerie'),
                dcv['eric.lingerie'].stage==9,
                'lace_ling_eric1' not in persistent.mems_var]):
            $ added_mem_var('lace_ling_eric1')

        if (renpy.seen_label('alice_body_photoset1') and
                '01-Alice' in persistent.photos and
                '05' in persistent.photos['01-Alice']):
            $ added_mem_var('alice_photoset1')

    return
