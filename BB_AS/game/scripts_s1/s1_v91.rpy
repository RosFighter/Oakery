
label s1_cheat_screen:
    if not cheats_warning:
        if dcv.ch_money is None:
            $ dcv.ch_money = Daily(enabled=True)
        call screen s1_cheat_warning()

    call screen s1_cheat_screen()


label s1_cheat_skip(skip_days=0):

    # $ print('skip '+str(skip_days)+' days')
    # $ print(cheat_skip)

    if cheat_skip:
        $ skiped = []
        $ renpy.retain_after_load()

        # создаём авто-сохранение
        $ renpy.loadsave.force_autosave(True, True)

    if cheat_skip:
        # переводим Макса в его комнату
        $ current_room = house[0]
        $ mgg.energy = 100.0
        $ mgg.cleanness = 80.0
        python:
            while skip_days > 0:
                skiped.append(weekday)
                skip_days -= 1

                if tm >= '06:00':
                    # проверяем наличие событий до полуночи
                    event_list = events_by_tm.get_list_events(tm, '23:59', day)
                    if events_by_tm.breakfast in event_list:            # завтрак
                        if not get_breakfast():
                            event_list.remove(events_by_tm.breakfast)
                    if events_by_tm.dinner in event_list:               # ужин
                        if not get_dinner():
                            event_list.remove(events_by_tm.dinner)
                    if events_by_tm.MorningWood2 in event_list:         # периодический утренний стояк
                        event_list.remove(events_by_tm.MorningWood2)

                    if len(event_list):
                        # если остались неудалённые события, прерываем пропуск
                        # print event_list
                        skip_error = True
                        break

                    # если событий нет, начинаем новые сутки и проверяем наличие событий до утра
                    day += 1
                    tm = '00:00'
                    weekday = GetWeekday(day)
                    start_midnight()
                    if weekday == 0:
                        start_newweek()

                event_list = events_by_tm.get_list_events(tm, '05:59', day)

                if events_by_tm.Night_Olivia in event_list:         # ночной визит Оливии
                    if any([poss['Schoolmate'].used(20), poss['Schoolmate'].used(13)]):
                        # периодические просмотры пройдены
                        event_list.remove(events_by_tm.Night_Olivia)
                if events_by_tm.Wearied in event_list:              # необходимость сна Макса
                    event_list.remove(events_by_tm.Wearied)

                # если событий нет, начинаем новый игровой день
                start_newday()

                tm = '06:00'

                if len(event_list):
                    # если остались неудалённые события, прерываем пропуск
                    # print event_list
                    skip_error = True
                    break
            # else:
            #     skip_error = True

        if skip_error:
            # если встечено событие, загружаем сохранение, созданное перед пропуском дней
            $ renpy.loadsave.load("auto-1")
        else:
            # $ print skiped
            if len(skiped) > 2 and lisa_was_topless():
                $ lisa.weekly.dishes = 2 if skiped > 3 else 1
            if 6 in skiped:
                $ skiped.remove(6)
            if 0 in skiped:
                $ skiped.remove(0)
            if len(skiped) > 2 and lisa.stat.sh_breast > 0:
                $ lisa.weekly.help = 2 if skiped > 3 else 1
                if 2 in skiped:
                    $ lisa.weekly.mass1 = 1

            $ tm = '06:00'
    else:
        "Есть важные события. Пропуск завершить не удалось."

    jump AfterWaiting


label s1_sleeping_with_anna:
    $ current_room = house[2]
    $ SetCamsGrow(house[2], 350)
    $ prevtime = '02:00'
    $ spent_time = 240
    $ CamShow()
    $ status_sleep = True

    # call NewDay from _call_NewDay_1
    $ start_newday()

    $ changes_main(240)

    $ spent_time = 0
    $ prevtime = '05:50'
    $ tm = '05:50'
    scene black with dis8

    return


label s1_ann_drink_cam:
    # по камере гостиной
    # cam-lounge-04a-night-829p + cam-lounge-ann-drunk-01a-829p
    show Ann_drink_cam at laptop_screen
    show FG cam-shum-act at laptop_screen
    $ ann.daily.drink = 1
    if not ann.dcv.drink.stage:
        # 1-ый раз
        Max_09 "{m}Что это мама делает в такой поздний час в гостиной? Может, что-то случилось...{/m}" nointeract
        menu:
            "{i}идти в гостиную{/i}":
                jump s1_ann_first_drink
    else:
        Max_07 "{m}Похоже, мама снова выпивает в гордом одиночестве!{/m}"

    return


label s1_ann_first_drink:
    # Анна выпивает (с субботы на воскресенье, 01:00)
    # после изгнания Эрика и разговора за завтраком (flags.eric_wallet == 5),
    # состоялся второй разговор на балконе (ann.flags.showdown_e > 1)
    # и 5 расширенных йог (ann.flags.truehelp > 4)

    # lounge-night-01-ann-01-drunk + lounge-night-01-ann-01a-drunk
    scene Ann_drink
    if ann.daily.drink > 0:
        # Макс видел Анну в гостиной через камеру
        Max_07 "{m}Ох, ничего себе! Мама сидит здесь совсем одна и выпивает... Почему? Лучше мне не оставлять её одну в таком состоянии...{/m}"
        $ ann.daily.drink = 1
    else:
        Max_09 "{m}Что это мама делает в такой поздний час в гостиной? Кажется, ничего хорошего...{/m}"

    $ ann.dcv.drink.stage = 1

    Max_00 "Эй, мам, что ты здесь делаешь?"
    Ann_14 "А? Это ты Макс... Я... Просто решила немножко расслабиться..."

    # lounge-night-02 + lounge-night-02-ann&max-01-drunk + lounge-night-02-ann-01a-drunk + lounge-night-02-max-(01b/01c)-drunk
    show Ann_drink closer
    Max_08 "Обычно ты не так расслабляешься... Так что давай рассказывай, что не так?"
    Ann_12 "Всё хорошо. Я просто устала..."
    Max_09 "От чего?"
    Ann_17 "Да от Эрика и его злорадной рожи... И от чувства собственной ничтожности..."
    Max_07 "Эй, не говори так! Ты самая замечательная женщина на свете!"
    Ann_18 "А кто этого поганого извращенца, привёл в наш дом? Ведь я! Я виновата..."
    Max_09 "Ты же не знала, что он такой! Всё хорошо, сейчас эта проблема уже решена. Так что прекращай себя винить и пить в одиночестве. Ты не одна, мам! Я всегда рядом!"
    Ann_02 "Ох, это так мило, сынок... Ты... Ты самый лучший. Сразу видно настоящего мужчину."
    Max_15 "Вот. И мужчина тебе говорит, что с алкоголем на сегодня всё. Пора идти спать."
    Ann_14 "Хорошо, мой милый... Только... Ты проводишь меня до комнаты? Кажется, меня развезло уже с одного бокала вина."
    Max_07 "Ну, конечно! Пойдём..."
    Ann_04 "Спасибо, сынок... Ты... Ты такой заботливый." nointeract

    menu:
        "{i}помочь маме добраться до кровати{/i}":
            scene black with dis5

    # annroom-night-door-01 + annroom-night-door-01-ann&max-01 + annroom-night-door-01-ann-01a + annroom-night-door-01-max-(01b/01c)
    $ var_stage = '01'
    scene Ann_sleep_drink door with diss5
    Ann_07 "Хи-хи... Комната так смешно качается... Правда?"
    Max_10 "А тебя и правда развезло, мам! Осталось идти совсем немного..."
    Ann_06 "Спа... Спасибо, что довёл меня, милый... Если бы не ты, я бы точно выселила Киру с дивана в гостиной."
    Max_01 "У нас вообще-то два дивана в гостиной, помнишь?"
    Ann_05 "О, точно! Я вспомнила... Хи-хи... Вот и моя кроватка!"
    Max_04 "Ага, добрались."

    # annroom-bedann-night-02 + annroom-bedann-night-02-ann&max-01 + annroom-bedann-night-02-ann-01a + annroom-bedann-night-02-max-(01b/01c)
    $ var_stage, var_pose = '02', '01'
    scene Ann_sleep_drink
    Ann_03 "Ох, как же хорошо оказаться в мягкой постели... Всё, я спать..."
    Max_09 "Эй, мам, подожди! А ты переодеться не хочешь? В халате будет жарко спать."
    Ann_14 "Да, ты прав, будет жарко. Но я сейчас не в том состоянии, чтобы переодеваться..."
    Max_07 "Не переживай, я всё сделаю. Тебе нужно только приподняться."

    # annroom-bedann-night-03 + annroom-bedann-night-03-ann&max-01 + annroom-bedann-night-03-max-01(b/c)02(b/c) + annroom-bedann-night-03-ann-01a
    $ var_stage = '03'
    Ann_13 "Ох, только я без лифчика, сынок. Давай, я попробую сама переодеться..."
    Max_01 "Не волнуйся, здесь довольно темно, так что при всём желании я всё равно ничего не увижу."
    Ann_12 "Да? Эээ... И ты даже не хочешь увидеть?"
    Max_07 "Ну, как мужчина, конечно хочу! И не только увидеть... Но сейчас я всего лишь пытаюсь тебе помочь..."

    # annroom-bedann-night-03 + annroom-bedann-night-03-ann&max-02 + annroom-bedann-night-03-max-01(b/c)02(b/c) + annroom-bedann-night-03-ann-02b
    $ var_pose = '02'
    Ann_14 "Спасибо, мой хороший. Мне как-то даже не удобно перед тобой... Что тебе приходится делать такое для меня..."
    Max_04 "Всё нормально, мам. Поддержка любимой мамы - дело святое... Вот и всё! Твой лифчик там, где ему и положено быть."
    Ann_03 "Ох, даже не знаю, чтобы я без тебя делала... А сейчас прости, я просто умираю, так хочу спать..."
    Max_07 "Конечно, мам, ложись. Но я, на всякий случай, останусь здесь. Вдруг, тебе станет плохо и нужна будет помощь."
    Ann_17 "Ты останешься спать со мной? Рядом? Сынок, ты уже слишком большой, чтобы спать с мамой..."
    Max_09 "И тем не менее, я останусь, мне так будет спокойнее за тебя. Кровать большая."

    # annroom-bedann-night-04 + annroom-bedann-night-04-ann&max-01 + annroom-bedann-night-04-ann-01b + annroom-bedann-night-04-max-01c
    $ var_stage, var_pose = '04', '01'
    scene Ann_sleep_drink
    Ann_02 "Я... Спасибо, мой милый, ты такой заботливый... Ты у меня самый лучший!"
    Max_01 "Поцелую перед сном, чтобы ты ни о чём не переживала и отдыхала..."
    Ann_08 "Ох... Это так мило и нежно, сынок... Спокойной ночи."
    Max_04 "Спи, мам... Сладких снов."

    # annroom-bedann-n-01 + annroom-bedann-n-01-ann&max-sleep-01 + annroom-bedann-n-01-ann&max-sleep-01b + annroom-bedann-n-01-max-sleep-01c
    scene Ann_Max_sleep
    Max_02 "{m}Наконец-то я лежу с мамой в одной постели! И не смотря на то, что сейчас она просто спит, это огромное достижение, поскольку она не выгнала меня, а позволила остаться. И я безумно рад засыпать рядом с такой шикарной женщиной...{/m}" nointeract
    menu:
        "{i}спать до утра{/i}":
            scene black with dis5
            call screen after_a_while   # !!!ЧЕРЕЗ НЕКОТОРОЕ ВРЕМЯ...!!! #на тёмном экране
            scene black with dis5

    # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-01 + annroom-bedann-night-05-ann-01b + annroom-bedann-night-05-max-01c
    $ var_stage = '05'
    scene Ann_sleep_drink
    Max_19 "{m}Что это?! Оу! Похоже, маме не хватает близости и она во сне потянулась обниматься... Это так сильно возбуждает, чувствовать её нежное и горячее тело, которое так крепко прижимается ко мне...{/m}"
    Ann_03 "Ммм... Неужели это не сон и ты действительно здесь... рядом со мной?"
    Max_01 "Да, я здесь. Всё хорошо..."

    # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-02 + annroom-bedann-night-05-ann-02b + annroom-bedann-night-05-max-02c
    $ var_pose = '02'
    Ann_03 "Ох... Похоже, что ты соскучился по мне так же сильно, как и я по тебе... Мне так не хватало твоего большого и горячего мальчика... Я очень хочу его..."
    Max_07 "Эээ... Мам?"

    # annroom-bedann-night-06 + annroom-bedann-night-06-ann&max-00 + annroom-bedann-night-06-max-00c + annroom-bedann-night-06-ann-00b
    $ var_stage, var_pose = '06', '00'
    Ann_15 "Ой!!! Макс! Я совсем не думала, что это ты, сынок... Какой стыд!"
    Max_09 "Да? И кто, ты думала, рядом с тобой лежит? Неужели, Эрик?"
    Ann_19 "Конечно, нет! С этим подонком я бы уж точно не потянулась обниматься!"
    Max_07 "А кто тогда?"
    Ann_17 "Неважно! Зря я так напилась. Иди к себе, Макс. Нам не стоит спать вместе, от греха подальше." nointeract
    menu:
        "{i}уйти{/i}":
            pass

    $ renpy.end_replay()
    $ poss['boss'].open(4)
    $ spent_time += 90
    $ current_room = house[0]
    $ mgg.energy = 40
    jump Sleep


label s1_ann_talk_about_night:
    # Разговор с Анной после 1-ой выпивки
    # доступен сразу с утра
    # "Мам, поговорим?"
    Ann_12 "Если ты про то, что случилось ночью, то можешь даже не утруждаться. Я не хочу это обсуждать. Давай просто забудем."
    Max_07 "Ну, знаешь... После того, как ты запустила свою руку мне в шорты, у меня много вопросов!"
    Ann_14 "Ох, ну зачем напоминать о таком? Мне ужасно стыдно! Выводы для себя я уже сделала, что алкоголь для меня - зло. Тема закрыта, Макс."
    Max_10 "Ладно, как скажешь."
    $ ann.dcv.drink.stage = 2
    $ spent_time += 10
    return


label s1_kira_talk_about_ann_drink:
    # Разговор с Кирой об Анне
    # после разговора по выпивке
    # "Хотел поговорить о маме..."
    scene BG sun-talk-01
    show Kira sun-talk 01
    show Max sun-talk 01
    Kira_01 "Не переживай за неё, Макс. Она женщина взрослая и переживёт это расставание с Эриком. Но моральная поддержка будет очень кстати."
    Max_09 "Это всё понятно. Я про другое хотел спросить. Похоже, мама начала искать утешение в алкоголе."
    Kira_03 "Ну... Это не так и страшно, если в меру. Она же не каждый день это делает, иначе по ней было бы видно."
    Max_07 "Да, пока я только раз застал её за этим делом. Она себя вообще нормально ведёт, когда выпьет?"
    Kira_08 "Боишься, что она начнёт всех по заднице лупить направо и налево?"
    Max_10 "Нет. Просто хочу знать, чего от неё стоит ожидать в таком состоянии."
    Kira_14 "На самом деле Аню пьяной я видела не так уж много раз. По молодости было дело, уже после того нашего с ней детского... происшествия..."
    Max_09 "И ничего странного за ней ты тогда не наблюдала?"
    Kira_05 "Расскажу маленькую тайну... Мой первый, сам знаешь какой опыт, с девушками был как раз с твоей мамой."
    Max_08 "Ого! Вот с этого момента поподробнее..."
    Kira_07 "Помню, мы с ней урвали бутылочку вина... Ну и пустились во все тяжкие. Как я поняла, когда её развезёт, то она впадает в какое-то состояние... типа фантазии. Она понимает, что происходит и всё помнит, но не считает, что это было правдой."
    Max_02 "Во как! Ну и... понравилось тебе \"развлекаться\" с моей мамой?"
    Kira_06 "А то! Мы были молодые и любопытные... Я и сейчас, собственно, осталась такой же... По большей части."
    Max_03 "И мне это нравится, тётя Кира!"
    Kira_04 "Мне тоже, Макс. Ты уж там присматривай за своей мамой, чтобы она много не пила."
    Max_04 "Обязательно!"
    $ ann.dcv.drink.stage = 3
    $ spent_time += 10
    return


label s1_ann_drink:
    # Анна выпивает (с субботы на воскресенье, 01:00)
    # Макс набрал 5 успешных расширенных йог

    # lounge-night-01-ann-01-drunk + lounge-night-01-ann-01a-drunk
    $ var_pose = '01'
    scene Ann_drink
    if ann.daily.drink > 0:
        # Макс видел Анну в гостиной через камеру
        Max_07 "{m}Лучше мне не оставлять её одну в таком состоянии...{/m}"
    else:
        # Макс не смотрел камеру гостиной
        Max_09 "{m}Ага, мама снова выпивает, пока все спят! Ну, кроме меня, конечно...{/m}"

    $ ann.dcv.drink.set_lost(1)

    Max_09 "Снова расслабляешься, пока никто не видит?"
    Ann_12 "Да, сынок. Раз в недельку, да немножко, почему бы и нет. Ты почему не спишь?"

    # lounge-night-02 + lounge-night-02-ann&max-01-drunk + lounge-night-02-ann-01a-drunk + lounge-night-02-max-(01b/01c)-drunk
    $ var_pose = '02'
    Max_00 "Кто-то же должен за тобой присматривать. Много ты уже выпила?"
    Ann_13 "Нет, всего лишь бокальчик. Я знаю, что мне лучше не напиваться."
    Max_07 "Да, тебя и от одного бокала развозит неплохо. Может, уже в сторону постельки выдвигаться будем, если тебя ещё ноги держат?"
    Ann_02 "Нет, сынок, я ещё посижу здесь... А ты иди спать, не переживай за меня." nointeract
    menu:
        "Хватит пить! Мы идём спать!":
            Ann_14 "А я не хочу!"
            Max_15 "А мне до лампочки, мам. Спать!"
            Ann_05 "Да? Ну, ладно... раз ты такой настойчивый..." nointeract
            menu:
                "{i}помочь маме добраться до кровати{/i}":
                    pass
        "{i}уйти{/i}" if not _in_replay:
            $ spent_time = 10
            jump Waiting

    # annroom-night-door-01 + annroom-night-door-01-ann&max-01 + annroom-night-door-01-ann-01a + annroom-night-door-01-max-(01b/01c)
    $ var_stage = '01'
    scene Ann_sleep_drink door
    Ann_07 "Вот и добрались! Если бы не ты, я бы точно не смогла сюда подняться, пришлось бы спать прямо на барной стойке. Хи-хи..."
    Max_01 "Нет, мам, до такой степени я не дам тебе опуститься. Вот и твоя кроватка..."

    # annroom-bedann-night-02 + annroom-bedann-night-02-ann&max-01 + annroom-bedann-night-02-ann-01a + annroom-bedann-night-02-max-(01b/01c)
    $ var_stage, var_pose = '02', '01'
    scene Ann_sleep_drink
    Ann_03 "Да... Моя постелька... Спасибо, мой милый, что помог. Можешь идти спать..."
    Max_07 "Ты рано легла, сначала нужно переодеться. Если приподнимешься, то я помогу тебе с этим..."

    # annroom-bedann-night-03 + annroom-bedann-night-03-ann&max-01 + annroom-bedann-night-03-max-01(b/c)02(b/c) + annroom-bedann-night-03-ann-01a
    $ var_stage = '03'
    Ann_02 "Ох... У меня почти нет на это сил... Дальше давай сам, только не подглядывай."
    Max_04 "Здесь темно, мам. Я работаю практически на ощупь. Но, не переживай, лишнего не трону."

    # annroom-bedann-night-03 + annroom-bedann-night-03-ann&max-02 + annroom-bedann-night-03-max-01(b/c)02(b/c) + annroom-bedann-night-03-ann-02b
    $ var_pose = '02'
    Ann_04 "Я не переживаю. Мне очень повезло с таким заботливым и деликатным сыном."
    Max_02 "Вот и всё! Твой лифчик там, где ему и положено быть. Теперь можно ложиться спать."

    # annroom-bedann-night-04 + annroom-bedann-night-04-ann&max-01 + annroom-bedann-night-04-ann-01b + annroom-bedann-night-04-max-01c
    $ var_stage, var_pose = '04', '01'
    Ann_14 "Хорошо... Если ты снова хочешь остаться здесь, то лучше не стоит. Если мне станет худо, то я справлюсь сама."
    Max_07 "Нет, мам. Я останусь однозначно. А чтобы тебя ничто не тревожило, одень свою маску для сна. Она поможет тебе лучше выспаться."
    Ann_08 "Надеюсь, так и будет. Спокойной ночи, сынок."
    Max_01 "Поцелую перед сном, чтобы ты ни о чём не переживала и отдыхала... Сладких снов."

    # annroom-bedann-n-01 + annroom-bedann-n-01-ann&max-sleep-01 + annroom-bedann-n-01-ann&max-sleep-01b + annroom-bedann-n-01-max-sleep-01c
    scene Ann_Max_sleep
    Max_19 "{m}Ну вот, теперь остаётся только ждать... Благодаря маске для сна, мама сможет в полной мере оторваться в своей фантазии. Если, конечно, не станет её снимать...{/m}" nointeract

    menu:
        "{i}дремать{/i}":
            scene black with dis5
            call screen after_a_while   # !!!ЧЕРЕЗ НЕКОТОРОЕ ВРЕМЯ...!!! #на тёмном экране
            scene black with dis5

    # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-01 + annroom-bedann-night-05-ann-01z + annroom-bedann-night-05-ann-01b + annroom-bedann-night-05-max-01c
    $ var_stage = '05'
    scene Ann_sleep_drink mask
    Max_04 "{m}О да! Мама снова лезет обниматься... Мой член уже в огромном предвкушении всяческих забав!{/m}"
    Ann_03 "Ммм... Наконец-то ты снова рядом, дорогой... Как же мне хорошо с тобой..." nointeract

    menu:
        "Мне тоже... Хочешь почувствовать, насколько?":
            jump .demonstrate

        "{i}притвориться спящим{/i}" if False:  #(!!!2-ой сезон!!!)
            pass

    label .demonstrate:
        # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-02 + annroom-bedann-night-05-ann-02z + annroom-bedann-night-05-ann-02b + annroom-bedann-night-05-max-02c
        $ var_pose = '02'
        Ann_05 "Ухх! Я ещё ничего не делала, а он уже такой твёрдый! Кто-то явно нацелен хорошенько порезвиться..."
        Max_02 "С такой горячей сексуальной женщиной как ты, только этим и хочется заниматься!" nointeract

        menu:
            "{i}целовать маму{/i}":
                pass

        # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-03 + annroom-bedann-night-05-ann-03z + annroom-bedann-night-05-ann-03b + annroom-bedann-night-05-max-03c
        $ var_pose = '03'
        Max_05 "{m}Ох, не знаю за кого мама меня принимает, но её поцелуи это что-то! А от того, как нежно её рука обхватила мой член, у меня внутри всё начинает трепетать от восторга...{/m}"
        # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-02 + annroom-bedann-night-05-ann-02z + annroom-bedann-night-05-ann-02b + annroom-bedann-night-05-max-02c
        $ var_pose = '02'
        Ann_08 "Становится слишком жарко, чтобы продолжать. Давай освободимся от всей одежды."
        Max_07 "Давай. Но я хочу, чтобы оставила маску. Так будет куда чувственнее..." nointeract

        menu:
            "{i}раздеться{/i}":
                pass
        # (annroom-bedann-night-07 + annroom-bedann-night-07-ann&max-01 + annroom-bedann-night-07-ann-01z) или (annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-01 + annroom-bedann-night-09-ann-01z)
        $ var_stage, var_pose = renpy.random.choice(['07', '09']), '01'
        scene Ann_sleep_drink mask naked
        Max_20 "{m}О да! Мама сразу же потянулась прямо вниз... Теперь её губки нежно скользят по концу моего члена, а язычок исследует и играет со всеми изгибами... Она никуда не торопится и просто наслаждается им. Фантастика!{/m}"
        Ann_07 "Ммм... Ты же любишь, когда я дразню твоего мальчика своим языком, прежде чем он попадёт ко мне в рот?"
        Max_19 "Да, мне очень нравится это, продолжай..."

        # (annroom-bedann-night-06 + annroom-bedann-night-06-ann&max-01 + annroom-bedann-night-06-ann-01z) или (annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-02 + annroom-bedann-night-09-ann-02z)
        $ var_stage, var_pose = ('09', '02') if var_pose == '09' else ('06', '01')
        Max_21 "{m}Пока она играется с моим членом, нужно пользоваться моментом и отвлечься на её киску. Иначе, я просто не выдержу и кончу. Мамина щёлочка слегка мокренькая, но так не пойдёт. Сейчас мои пальцы решат эту проблему...{/m}" nointeract

        menu:
            "отвлечься на её киску" if ann.dcv.drink.stage == 3:
                # 1-ый раз без привязки к навыку
                if not _in_replay:
                    $ poss['boss'].open(5)
                jump .no_restrain

            "отвлечься на её киску" ('sex', (2 + mgg.sex) * 2, 90) if ann.dcv.drink.stage > 3:
                if rand_result:
                    # (Удалось сдержаться!)
                    if not _in_replay:
                        $ poss['boss'].open(6)
                    jump .restrain
                else:
                    # (Не удалось сдержаться!)
                    jump .no_restrain

    label .no_restrain:
        # (Не удалось сдержаться!)
        # (annroom-bedann-night-07 + annroom-bedann-night-07-ann&max-01 + annroom-bedann-night-07-ann-01z + annroom-bedann-night-07-ann-01cum1) или (annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-01 + annroom-bedann-night-09-ann-01z + annroom-bedann-night-09-ann-01cum1)
        $ var_stage, var_pose = ('09', '01') if var_pose == '09' else ('07', '01')
        scene Ann_sleep_drink mask naked cum0
        Ann_13 "[norestrain!t]Ого! Ты уже кончил, дорогой... Не думала, что это будет так быстро, ведь я ещё даже не начала стараться!"
        Max_07 "Прости. Просто твои прикосновения и ласки меня перевозбудили."
        Ann_08 "Ничего страшного. Возможно, я так соскучилась по твоему члену, что немного увлеклась. Сейчас я приведу всё в порядок..."
        Max_19 "{m}Вот чёрт! От того, как тщательно и эротично она слизывает мою сперму запросто можно бы было кончить ещё раз! Просто невероятно, что это на самом деле происходит.{/m}"

        # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-02 + annroom-bedann-night-05-ann-02z
        $ var_stage, var_pose = '05', '02'
        scene Ann_sleep_drink mask naked
        Ann_05 "Обещаю, в следующий раз, я не буду так увлекаться и постараюсь растянуть наше удовольствие подольше."
        Max_04 "Но это в следующий раз. А сейчас я просто обязан постараться сделать всё, чтобы ты тоже кончила."

        # (annroom-bedann-night-02 + annroom-bedann-night-02-ann&max-02 + annroom-bedann-night-02-ann-02z) или (annroom-bedann-night-06 + annroom-bedann-night-06-ann&max-02 + annroom-bedann-night-06-ann-02z) или (annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-03 + annroom-bedann-night-09-ann-03z)
        $ var_stage, var_pose = renpy.random.choice([('02', '02'), ('09', '03')])
        Ann_09 "Ахх... Этого я и жду... Я вся в предвкушении того, что ты будешь для этого делать. Ох..."
        Max_03 "{m}Ммм... От такой сочной и пышной груди даже отрываться не хочется! Но у меня есть не менее интересные дела кое-где пониже! Только устроюсь поудобнее...{/m}"

        # (annroom-bedann-night-02 + annroom-bedann-night-02-ann&max-04 + annroom-bedann-night-02-ann-04z) или (annroom-bedann-night-04 + annroom-bedann-night-04-ann&max-03 + annroom-bedann-night-04-ann-03z)
        $ var_stage, var_pose = ('02', '04') if var_stage == '02' else ('04', '03')
        Ann_10 "Да... Как же меня возбуждают твои нежные прикосновения... Твои пальцы знают, как нужно ласкать мою киску. Ухх... Да... Ещё..."
        Max_02 "{m}Да, мои пальцы довольно легко скользят по маминой киске. Если бы она только знала, что это делаю я, всё в миг бы прекратилось. Но она не знает, так что нужно пользоваться моментом...{/m}"

        # (annroom-bedann-night-04 + annroom-bedann-night-04-ann&max-04 + annroom-bedann-night-04-ann-04z) или (annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-04 + annroom-bedann-night-05-ann-04z) или (annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-04)
        $ var_stage, var_pose = renpy.random.choice(['04', '05', '09']), '04'
        if var_stage == '09':
            show Ann_sleep_drink -mask

        Ann_14 "Ухх, да... Как же мне хорошо от твоих пальчиков... Да, продолжай... Ещё... Поглубже... Ммм... Я сейчас просто потеряю голову от наслаждения... Ах!" nointeract

        menu:
            "{i}ласкать маму языком{/i}":
                pass
        # annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-05 + annroom-bedann-night-05-ann-05z
        $ var_stage, var_pose = '05', '05'
        show Ann_sleep_drink mask
        Ann_11 "Ох, это... нет слов, как приятно... Ахх... Ты самый лучший мужчина на свете! Д-а-а! Твой язычок сводит меня с ума... Я... Я больше не могу... Я сейчас... Я кончаю! Д-а-а!"
        Max_05 "{m}Да, мам! Вот так... Её тело так классно содрогается от оргазма. Ради такой шикарной женщины грех не постараться.{/m}"

        jump .end_1

    label .restrain:
        # (Удалось сдержаться!)
        $ ann.flags.held_out += 1
        $ added_mem_var('s1_ann_drink.restrain')

        # (annroom-bedann-night-07 + annroom-bedann-night-07-ann&max-02 + annroom-bedann-night-07-ann-02z) или (annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-05 + annroom-bedann-night-09-ann-05z)
        $ var_stage, var_pose = renpy.random.choice([('07', '02'), ('09', '05')])
        scene Ann_sleep_drink mask naked
        Max_22 "[restrain!t]{m}Ох, она начала посасывать мой член... Это просто божественно! Я прямо чувствую, с каким удовольствием она это делает. Как же это приятно, мам, чёрт возьми!{/m}" nointeract

        menu:
            "{i}проникнуть пальцами в её киску{/i}":
                pass

        # annroom-bedann-night-08 + annroom-bedann-night-08-ann&max-01 + annroom-bedann-night-08-ann-01z
        $ var_stage, var_pose = '08', '01'
        Max_03 "{m}Ммм... Мои пальцы запросто проскользнули в неё. Обалденно, она стала сосать ещё активнее от моих ласк. Ох, мама... Знала бы ты, что сейчас вытворяешь! Вернее, с кем. Д-а-а...{/m}" nointeract

        menu:
            "{i}перебраться в позу 69{/i}":
                # annroom-bedann-night-04 + annroom-bedann-night-04-ann&max-05 + annroom-bedann-night-04-ann-05z
                $ var_stage, var_pose = '04', '05'
                Max_02 "{m}Ухх... Уткнуться в её сногсшибательную большую попку одно наслаждение! Теперь она сосёт и одновременно постанывает от того, что вытворяет мой язык с её сочной киской...{/m}" nointeract

                menu:
                    "{i}ласкать языком неспеша{/i}":
                        pass

                # (annroom-bedann-night-05 + annroom-bedann-night-05-ann&max-06 + annroom-bedann-night-05-ann-06z) или (annroom-bedann-night-08 + annroom-bedann-night-08-ann&max-02 + annroom-bedann-night-08-ann-02z)
                $ var_stage, var_pose = renpy.random.choice([('05', '06'), ('08', '02')])
                Max_20 "{m}Блин! Она ещё и рукой начала моими яичками играть! А уж про то, что она всё смачнее и глубже заглатывает мой член, я вообще молчу... Только стонать и остаётся. Долго я так не протяну...{/m}" nointeract

                menu:
                    "{i}кончить маме в рот{/i}":
                        pass

                # annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-06 + annroom-bedann-night-09-ann-06z + annroom-bedann-night-09-ann-06cum
                $ var_stage, var_pose = '09', '06'
                scene Ann_sleep_drink naked mask cum
                Max_21 "{m}Д-а-а! Ах, мама не отрываясь принимает всю мою сперму! Она умничка... Знает, как порадовать мужчину. Но я с кое-чем ещё не закончил...{/m}" nointeract

                menu:
                    "{i}продолжить ласкать языком{/i}":
                        pass

                # annroom-bedann-night-07 + annroom-bedann-night-07-ann&max-03 + annroom-bedann-night-07-ann-03z + annroom-bedann-night-07-ann-03cum
                $ var_stage, var_pose = '07', '03'
                Ann_10 "Да, дорогой... Уфф... Ты кончил так мощно! Я даже не смогла удержать всё в себе. Ммм... Я хочу кончить так же сильно, как ты. Пожалуйста... Ах-х-х..." nointeract

                menu:
                    "{i}ласкать языком активнее{/i}":
                        pass

                # annroom-bedann-night-09 + annroom-bedann-night-09-ann&max-07 + annroom-bedann-night-09-ann-07z + annroom-bedann-night-09-ann-07cum
                $ var_stage, var_pose = '09', '07'
                Ann_11 "Ох, это... нет слов, как приятно... Ахх... Ты самый лучший мужчина на свете! Д-а-а! Твой язычок сводит меня с ума... Я... Я больше не могу... Я сейчас... Я кончаю! Д-а-а!"

                # annroom-bedann-night-10-ann&max-01 + annroom-bedann-night-10-ann-01z
                $ var_stage, var_pose = '10', '01'
                scene Ann_sleep_drink naked mask no_bg
                Max_05 "{m}Да, мам! Вот так... Её тело так классно содрогается от оргазма. Ради такой шикарной женщины грех не постараться.{/m}"

                jump .end_1

            "другие позы" if False:     # (!!!2-ой сезон!!!)
                pass

    label .end_1:
        # annroom-bedann-night-04 + annroom-bedann-night-04-ann&max-01 + annroom-bedann-night-04-ann-01z
        $ var_stage, var_pose = '04', '01'
        scene Ann_sleep_drink mask naked
        Ann_08 "Ох... Это было... нечто! Я просто... Извини, не знаю даже, что сказать... Так хорошо..."
        Max_03 "Ты была великолепна! Теперь просто отдыхай... Спокойной ночи."

        if ann.dcv.drink.stage == 3:
            $ ann.dcv.drink.stage = 4
            # 1-ый раз
            Ann_07 "Спасибо, дорогой. Мне тоже понравилось. И тебе доброй ночи."
            Max_09 "{m}Надо бы натянуть шорты, а то утром будет много визга, когда мама проснётся голой. И ещё больше визга будет, если я буду лежать рядом такой же голый. И не исключено, что с утренним стояком...{/m}"

            # annroom-bedann-n-01 + annroom-bedann-n-01-ann&max-sleep-02 + annroom-bedann-n-01-ann&max-sleep-02z + annroom-bedann-n-01-max-sleep-02c
            $ var_pose = '02'
            scene Ann_Max_sleep mask ann_naked
            Max_19 "{m}Фух... Теперь можно и спать. Вот это мы с мамой выдали! Она фантазировала, а я, так сказать, сделал эту фантазию реальной. Эх, вот бы почаще так развлекаться...{/m}" nointeract

            menu:
                "{i}спать до утра{/i}":
                    if not _in_replay:
                        call s1_sleeping_with_anna from _call_s1_sleeping_with_anna

            # annroom-shot-03-02 + annroom-bedann-m-01-ann&max-01 + annroom-bedann-m-01-max-01c
            $ var_pose = '01'
            scene Ann_Max_wakeup
            Ann_17 "Охх... Моя голова... Что происходит?!"
            Max_20 "Доброе утро, мам."

            # annroom-bedann-m-01 + annroom-bedann-m-01-ann&max-02 + annroom-bedann-m-01-max-02c
            $ var_pose = '02'
            Ann_15 "Макс! Быстро отвернись! Ты что тут делаешь?!"
            Max_08 "Не помнишь? Ты вчера выпила и я решил остаться с тобой на случай, если тебе будет плохо."
            Ann_13 "Ах, ну да, точно... Но почему я голая?!"
            Max_07 "Ну, видимо тебе стало жарко. А я не стал этому возражать."
            Ann_14 "Макс, я же твоя мама! Это всё совсем не правильно... Надо было меня остановить!"
            Max_09 "Мне кажется, телу нужно дышать. Особенно в том состоянии, в котором ты находилась."
            Ann_17 "Может и так, но не в присутствии же собственного сына! Получается, я сама разделась?"
            Max_01 "Ага. Ты разделась и заснула."
            Ann_13 "Фух... А то, мне такой сон приснился... Там я тоже разделась, но не только... Ой, сынок, это ты из-за моего вида так возбудился?!"
            Max_07 "Нет, у меня часто такое по утрам. Лиза не даст соврать. Хотя, возможно, сегодня это произошло благодаря тебе."
            Ann_18 "Макс, что ты такое при маме говоришь! И вообще, хватит меня забалтывать и глазеть. Давай-ка отвернись уже и иди к себе, ты меня смущаешь." nointeract

        else:
            # периодически
            Ann_07 "Спасибо, дорогой. Мне тоже понравилось. И тебе доброй ночи." nointeract
            menu:
                "{i}натянуть шорты{/i}":
                    pass

            # annroom-bedann-n-01 + annroom-bedann-n-01-ann&max-sleep-02 + annroom-bedann-n-01-ann&max-sleep-02z + annroom-bedann-n-01-max-sleep-02c
            $ var_pose = '02'
            scene Ann_Max_sleep mask ann_naked
            Max_19 "{m}Фух... Теперь можно и спать. А когда рядом засыпает совершенно голая и невероятно сексуальная женщина, пускай это и моя мама, то засыпать одно удовольствие.{/m}" nointeract

            menu:
                "{i}спать до утра{/i}":
                    if not _in_replay:
                        call s1_sleeping_with_anna from _call_s1_sleeping_with_anna_1

            # annroom-shot-03-02 + annroom-bedann-m-01-ann&max-01 + annroom-bedann-m-01-max-01c
            $ var_pose = '01'
            scene Ann_Max_wakeup
            Ann_17 "Охх... Неужели опять... Я тут валяюсь совершенно голая, а мой сын лежит рядом с огромным возбуждением! Тебе не стыдно?"
            Max_20 "Ага, и тебе доброе утро. Почему мне должно быть стыдно, если ты сама разделась?"

            # annroom-bedann-m-01 + annroom-bedann-m-01-ann&max-02 + annroom-bedann-m-01-max-02c
            $ var_pose = '02'
            Ann_14 "Потому что это мягко говоря странно, когда сына возбуждает собственная мать. Это что-то нездоровое."
            Max_07 "Подумаешь, возбудился. Это же самый искренний комплимент для такой прекрасной женщины, как ты."
            Ann_12 "Ой, Макс, прекрати... Спасибо, конечно, но это неуместно! Ты не мог бы отвернуться?"
            Max_02 "А ты мне расскажешь, как спалось? Что снилось?"
            Ann_14 "Ты выбрал просто самое \"лучшее\" время, чтобы об этом поболтать. Спасибо, что присмотрел за мной, но прекращай глазеть. Давай шуруй к себе."
            Max_01 "Не за что, мам." nointeract

        menu:
            "{i}уйти к себе в комнату{/i}":
                $ renpy.end_replay()
                $ current_room = house[0]
                $ spent_time = 10
                jump Waiting


label s1_about_intimate_lessons:
    # 2-ой разговор с Анной об интимных уроках (убеждение)
    # в любом месте через несколько дней после 1-ого разговора в ванной комнате
    Ann_12 "Да, я подумала и приняла решение - ничего не получится. А теперь давай закончим этот разговор и сделаем вид, что ничего не было. Живут же другие семьи как-то без этих... уроков..."
    Max_10 "Но ведь ты была не против! Ты позволяла смотреть за тем, что вы с Эриком делали..."
    Ann_18 "Макс! Я всё сказала! Ты мой сын и делать такие вещи... Это неправильно!"
    Max_11 "Ты это серьёзно?"
    Ann_16 "Более чем! Нормальные мальчики, если ты не в курсе, находят себе девочку и осваивают всё с ней."
    Max_09 "Согласен, мам. Но у меня есть идейка получше... И ходить далеко не придётся..."
    Ann_15 "Не поняла! Что значит, \"ходить далеко не придётся\"?!"
    Max_07 "По-моему мы договорились о том, что никакого разговора не было? Так что я пошёл..."
    Ann_17 "Минуточку! Я тебя не отпускала! Ты что, уже подстраховался на случай моего отказа?"
    Max_09 "Ну... Я не особо надеялся на твою помощь... Поэтому пойду к тёте Кире. Она взрослая и опытная женщина... Уж она-то наверняка знает, как мужчине нужно ублажать женщину."
    Ann_13 "Господи, Макс, ты совсем с ума сошёл, просить о таком мою сестру?!"
    Max_07 "А что? Мне кажется, она как раз таки та женщина, которая действительно не отвернётся от своего любимого племянника, а не будет искать отговорки, как и думать, правильно это или нет."
    Ann_15 "Нет, Макс, я не отворачивалась от тебя! Просто... Я считаю, что мама не должна учить {b}ТАКОМУ{/b} своего сына."
    Max_09 "А смотреть, как ты занимаешься этим с Эриком - это должное? Или тебе нравилось, что я на вас смотрел?"
    Ann_14 "Господи, Макс, ну что ты такое говоришь? Я просто... Я..."
    Max_00 "Короче, я пошёл..."
    Ann_17 "О боже... Ну ладно, будь по-твоему, давай попробуем... Не хватало ещё, чтобы ты просил о подобной помощи кого-то ещё."
    Max_03 "Отлично! Когда начнём?"
    Ann_12 "Так, давай не торопиться! Вот как я вечером, после ванны, буду одна в гостиной отдыхать за просмотром ТВ, так и подходи. Будем разбираться..."
    Max_02 "Договорились. Кстати, можно было бы тогда посмотреть что-то... обучающего плана... Заодно, так сказать."
    Ann_13 "Пожалуй... Это будет весьма уместно. Но никому не говори об этом. И к Кире не вздумай ходить!"
    Max_01 "Конечно! Это будет нашим секретом, мам." nointeract
    menu:
        "{i}уйти{/i}":
            $ ann.dcv.private.stage = 2
            $ spent_time = 20
            jump Waiting


label s1_ann_intimate_lesson_1:
    # 1-ый интимный урок с Анной (ТВ)
    # "Проведём сегодня вечер с \"образовательной\" пользой?"

    # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(01/02/03)
    $ var_pose = pose3_1
    scene tv_talk ann
    Ann_01 "Проведём... Я же согласилась, на свою голову. Я, в общем-то, определилась, что тебе покажу..."
    Max_01 "Я весь в предвкушении!"

    # tv-watch-01 + ero_mov_03_01 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    $ var_film = 'ero3 '
    $ var_stage = '01'
    scene tv_watch ann mgg
    Ann_02 "Вот... Сейчас посмотришь, как девочки развлекают себя без мальчиков. Думаю, этого будет вполне достаточно, чтобы понять... основу..."
    Max_08 "Так, ладно... И в чем основа?"

    # tv-watch-01 + ero_mov_03_02 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    $ var_stage = '02'
    Ann_04 "В стимуляции... сам знаешь чего. У вас, мальчиков, с этим куда проще. Ты и сам, уж я думаю, прекрасно знаешь, как снять напряжение... самостоятельно."
    Max_07 "А у вас?"

    # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
    $ var_pose = pose3_3
    scene ann_tv_ero_01
    Ann_14 "А у нас множество нюансов, из-за которых добиться... оргазма сложнее. Женщинам важна и обстановка, максимально ли мы привлекательны, нет ли у нас в голове каких-то проблем, которые нас не оставят в покое..."
    Max_10 "О-о-о... Как всё печально."

    # tv-watch-01 + ero_mov_03_03 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    $ var_stage = '03'
    scene tv_watch ann mgg
    Max_09 "Но, мам, это какой-то уж совсем детский уровень. Я, например, уже взрослый, а потому хочу знать, как целовать девочек, как прикасаться к ним... Так что давай, показывай."
    Ann_01 "Ну да, я так и думала, что просмотром одного ролика мы не обойдёмся..."

    # tv-watch-01 + ero_mov_03_04 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    $ var_stage = '04'
    Max_03 "Во! Вот это уже ближе к теме... Такое мне нравится. Красиво!"
    Ann_02 "Тогда смотри и запоминай. Если будет что-то непонятно, я объясню."

    # tv-mass-07 + tv-ero-01-max-(03a/03b) + tv-ero-01-ann-(07/08/09)
    $ var_pose = {'01':'07', '02':'08', '03':'09'}[pose3_3]
    scene ann_tv_ero_03
    Max_07 "Да, вопросик есть. А что, ласки женской груди действительно настолько приятны, что эта девушка просто потеряла голову?"
    Ann_05 "Ну конечно! А вообще, у всех это бывает по-разному... Это зависит от чувствительности и возбудимости девушки..."

    # tv-watch-01 + ero_mov_03_05 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    $ var_stage = '05'
    scene tv_watch ann mgg
    Max_09 "И как это выяснить?"
    Ann_14 "В процессе сближения с девушкой. Иначе, просто никак."

    # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
    $ var_pose = {'01':'04', '02':'05', '03':'06'}[pose3_3]
    scene ann_tv_ero_02
    Max_11 "Хмм... Засада, однако..."
    Ann_01 "И почему ты так тяжко вздыхаешь? Разочарован, что не ко всему можно подготовиться заранее?"

    # tv-watch-01 + ero_mov_03_06 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    $ var_stage = '06'
    scene tv_watch ann mgg
    Max_04 "Ага. Так когда мы это всё попробуем, мам?"

    # tv-kiss-03 + tv-ero-00-max-(01a/01b) + tv-ero-00-ann-01
    $ var_pose = '01'
    scene ann_tv_ero_00
    Ann_13 "В смысле, \"мы\"?! Это же очень интимные процессы..."
    Max_07 "Поэтому я к тебе и обратился. И я же не прошу целоваться в губы, а так... Хотя бы в шею попробовать... Заодно и массаж сделаю..."
    Ann_12 "Даже не знаю... Как-то это всё..." nointeract
    menu:
        "{i}начать массаж{/i}":
            pass
    # tv-watch-01 + ero_mov_03_07 + tv-watch-01-max&ann-(01a/01b)
    $ var_stage = '07'
    scene tv_watch ann_max
    Ann_17 "Массаж и поцелуи, это всё, конечно, здорово, сынок... Но не когда это происходит с мамой."
    Max_01 "Да не напрягайся ты так, мам. Мы просто проверим, насколько я с этим справлюсь, вот и всё."

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
    scene ann_tv_ero_04 towel
    Ann_12 "И как, по-твоему, я должна оценивать твои поцелуи? Я вряд ли смогу сделать это, как женщина, потому что я твоя мать. Но, ладно, так уж и быть, я постараюсь..." nointeract
    menu:
        "{i}продолжить массаж с поцелуями в шею{/i}":
            pass

    # tv-kiss-03 + tv-ero-05-max-(02a/02b)-ann-02
    scene ann_tv_ero_05
    Max_04 "{m}Мама замолчала... И начала так глубоко дышать! Нужно постараться целовать её хоть немного неуклюже, чтобы не было похоже, что у меня есть в этом опыт. Вот только не так-то это и просто...{/m}"

    # tv-watch-01 + ero_mov_03_08 + tv-watch-01-max&ann-(01a/01b)
    $ var_stage = '08'
    scene tv_watch ann_max
    Ann_02 "Ну что я скажу... Получается у тебя, Макс, довольно неплохо. Я имею ввиду сами поцелуи. Но тебе нужно расширять область их применения."
    Max_09 "Эээ... То есть?"
    Ann_05 "Нужно не забывать и про остальное: ключицу, плечи, спину, мочку ушка. Раз уж ты взялся это осваивать..."
    Max_02 "Понял. Тогда я сейчас попробую..." nointeract
    menu:
        "{i}продолжить массаж и поцелуи{/i}":
            pass

    # tv-max&kira-sex03-01-f + tv-ero-05-max-(03a/03b)-ann-03
    scene ann_tv_ero_06
    Max_03 "{m}Всё перечисленное я с удовольствием попробую, пока мой массаж всё ближе и ближе подступает к маминой груди. Ох, вот бы их тоже помассировать...{/m}"
    Ann_03 "Ахх... Сынок, если ты не будешь так частить с поцелуями, а будешь повышать их качество продолжительностью, то в сочетании с твоими навыками массажа, все девочки будут терять голову... Ммм..."
    Max_04 "Ну... Если ты потеряешь голову, то твой прогноз однозначно верен."
    Ann_14 "Ох... Мне кажется, что ты сейчас не только о своём образовании заботишься, но и... Тебе не хватает кое-чего. И заниматься тебе этим нужно не со мной..."

    # tv-watch-01 + ero_mov_03_09 + tv-watch-01-max&ann-(01a/01b)
    $ var_stage = '09'
    scene tv_watch ann_max
    Max_07 "Мам, а с кем, как не с тобой, мне такое можно пробовать делать? С тобой мне как-то легче преодолеть страхи. А девочкам, как я слышал, нравятся уверенные мальчики!"
    Ann_12 "И что, я теперь из-за этого должна отбросить всё смущение и наслаждаться, как эта девушка на экране?"
    Max_09 "А почему нет? Для меня бесценный опыт, для тебя одно удовольствие. Тебе же нравится массаж?"

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01
    scene ann_tv_ero_04
    Ann_17 "Ну, Макс! Одно дело, когда это просто массаж и другое, когда сын начинает делать своей маме эротический массаж!"
    Max_07 "То есть, если бы я, например, начал массировать твою грудь, то тебе бы не понравилось?"
    Ann_12 "Зная твой талант в массаже, я не сомневаюсь, что мне бы понравилось. Но делать такое мы не будем!"
    Max_08 "Почему ты так сильно этого стесняешься? У тебя же просто невероятно прекрасная грудь! Мне же нужно знать, как массировать её так, чтобы женщине нравилось. Вдруг, мой массаж здесь не сработает и нужны иные движения рук!"

    # tv-max&kira-sex03-01-f + tv-ero-05-max-(03a/03b)-ann-03
    scene ann_tv_ero_06
    Ann_14 "Ох, сынок... Ты, видимо, не отстанешь, да? Хорошо, попробуем разок, чтобы ты знал, как это... делается... Я скажу, если ты будешь делать что-то не так." nointeract
    menu:
        "{i}массировать мамину грудь{/i}":
            pass

    # after-club-s04-f + tv-ero-05-max-(04a/04b)-ann-04
    $ var_pose = '04'
    scene ann_tv_ero_07
    Max_05 "{m}Неужто мои руки наконец дотянулись до этих самых потрясающих сисек на свете! Несмотря на свои годы, мамина грудь выглядит просто отлично, а на ощупь, вообще, обалденная! Но продолжать неуклюжничать, как с поцелуями, так же нужно не забывать...{/m}"
    Ann_08 "Да, Макс... У тебя довольно неплохо получается. Но с грудью, по крайней мере, поначалу, лучше обращаться как можно нежнее... А так, твои навыки в массаже здесь очень к месту. Охх..."
    Max_02 "Значит, как женщине, тебе нравится, как я это делаю? Может, ещё что-нибудь подскажешь?"
    Ann_03 "Да, не останавливайся только на груди. Продолжай массировать и всё то, что ты массировал до этого. Ммм... Но обязательно возвращайся... Как же пошло такое говорить своему сыну..."

    # after-club-s04-f + tv-ero-05-max-(05a/05b)-ann-05
    $ var_pose = '05'
    Max_03 "{m}Да, мять эти сочные сисечки одно удовольствие, как и целовать её в шею. Она дышит жарко и глубоко, ей явно приятно. Но вместе с этим, я всё ещё чувствую, как она напрягается от того, что всё это делаю я.{/m}"

    # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
    $ var_pose = '01'
    Ann_05 "Так, сынок, достаточно. Я думаю, ты вполне готов сводить с ума всех девочек, какие попадутся в твои умелые руки. Ты ещё талантливее, чем мне казалось."
    Max_07 "Супер! А как же остальное?"

    # tv-watch-01 + ero_mov_03_10 + tv-watch-01-max&ann-(01a/01b)
    $ var_stage = '10'
    scene tv_watch ann_max
    Ann_17 "Остальное? В смысле остальное? Ты о чём, Макс?"
    Max_01 "Ну как... Мне же ещё нужно попробовать доставить удовольствие женщине там... внизу... Там же можно не только руками, так ведь?"
    Ann_13 "Да, но это уже осваивай без меня. С мамой таким заниматься, даже в образовательных целях - уже чересчур!"
    Max_07 "Наверно, ты права. Лучше учиться у нескольких женщин. К тому же, у тёти Киры, наверно, такого опыта побольше, чем у тебя. Ты же не против, если я поучусь у неё?"

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
    scene ann_tv_ero_04 towel
    Ann_06 "Ага, хотела бы я посмотреть, как ты будешь её на это уговаривать. Думаю, она ещё не всю свою нравственность растеряла, чтобы заниматься таким."
    Max_09 "Но! Если что... Никаких претензий к ней или ко мне, хорошо?"
    Ann_07 "Ой, сынок, давай без этой ерунды. Найди уже себе девочку." nointeract
    menu:
        "{i}уйти{/i}":
            $ renpy.end_replay()
            $ poss['control'].open(16)
            $ ann.dcv.private.stage = 3
            jump Waiting


label s1_bait_for_ann:
    # Анна ловит Макса и Киру за горяченьким
    # с вс на пн, даже если 1-ый урок у ТВ с Анной был в вс

    if var_pose not in ['01', '02', '03']:
        $ var_pose = renpy.random.choice(['01', '02', '03'])
    $ renpy.scene()
    $ renpy.show('Kira night-swim ' + var_pose)
    Max_03 "Ого... Купаешься голой, тётя Кира?! Классно смотришься!"
    Kira_01 "А, Макс... Я думала, что все уже спят. Хотела немного поплавать... А ты чего не спишь?" nointeract
    menu:
        "Нужна твоя помощь. Пойдём на диван, расскажу...":
            pass
    Kira_14 "Ой, Макс, может лучше будем решать проблемы с утра? На свежую голову..."
    Max_07 "От тебя почти ничего не потребуется."
    Kira_01 "Оу... Ну раз так, то дай мне пару минут, я только загляну в ванную комнату."
    Max_04 "Без проблем, тётя Кира."

    scene black with dis5
    call screen after_some_minutes      # !!!ЧЕРЕЗ НЕСКОЛЬКО МИНУТ...!!! #на тёмном экране
    scene black with dis3

    # lounge-tv-01 + tv-kira-01 + tv-max-00b
    $ pose3_4 = '01'
    $ var_pose = '01'
    scene tv_talk kira
    Kira_06 "Ничего, если я включу что-нибудь \"горяченькое\"? Или это будет мешать?"
    Max_02 "Обязательно включай! Это как раз таки будет нам необходимо для того, чтобы задуманная мной постановка сработала."
    Kira_07 "О как! Ты решил перейти со мной на ролевые игры? Интересно! Я думала, ты сперва будешь просить попробовать со мной анальный секс..."
    Max_06 "Ух ты! А что, уже можно?!"
    Kira_05 "Можно? Макс, твой член уже столько раз побывал у меня во рту и вообще во мне, что просто грех для тебя, как мне кажется, не натянуть на него мою попку."
    Max_09 "Блин, тётя Кира! Как ты с этим не вовремя! У меня теперь моральная дилемма, между моей задумкой и твоей..."
    Kira_01 "Ну, ролевые игры - это тоже весьма интересный опыт."
    Max_07 "Да, это здорово, но мне сейчас нужно не совсем это. Нужна ролевая помощь с мамой!"
    Kira_15 "Эээ... Думаешь, она согласится на ролевой тройничок?!"
    Max_09 "Так, тётя Кира, давай серьёзнее! Помнишь, я говорил, что мама вытворяет вещи, которые до Эрика и не подумала бы делать?"

    # tv-watch-01 + porn-k-02_01 + tv-watch-01-kira-01 + tv-watch-01-max-01b
    $ var_film = 'kira-porn-02 '
    $ var_stage = '01'
    scene tv_watch kira mgg
    Kira_13 "Да, помню. А что, градус таких вещей стал ещё больше?"
    Max_07 "Ага, знаешь, я подглядывал за ними... Мама несколько раз меня за это наказала, но Эрик взял и убедил её, что нужно удовлетворить моё подростковое любопытство. Они во всех подробностях показали мне, что такое минет..."
    Kira_17 "Ничего себе! Хочешь сказать, моя сестра, которая довольно строго вас от этого всего старалась оберегать, теперь вытворяет такие номера? Вау!"
    Max_01 "Вот-вот. Но раз уж у нас теперь такие вот реалии наступили, то я начал упрашивать её на продолжение таких вот уроков, но в плане ублажения женщин."
    Kira_03 "Смело и находчиво, должна сказать! Только немного обидно, что меня тебе стало мало..."

    # lounge-tv-01 + tv-kira-m-01 + tv-max-04b
    $ var_pose = '04'
    scene tv_talk kira_m
    Max_03 "Что ты, тётя Кира! Ты вообще лучшая тётя на свете! Просто, я хочу получить такой опыт от разных женщин, чтобы расширить свои границы в сексе."
    Kira_04 "Ну... Не могу здесь с тобой не согласиться. И чему же тебя учит моя сестра-развратница?"
    Max_02 "Мы начали со слегка интимных поцелуев и эротического массажа. Ну как, эротического... Она разрешила поласкать её грудь."
    Kira_05 "Ухх... Моё воображение уже не слабо меня заводит от твоих рассказов. А дальше?"
    Max_07 "А дальше, всё. Большее - это уже слишком интимно, а потому дальше я должен завести девушку и постигать всё это с ней. И вот здесь мне и нужна твоя помощь."

    # tv-watch-01 + porn-k-02_02 + tv-watch-01-kira-01 + tv-watch-01-max-01b
    $ var_stage = '02'
    scene tv_watch kira mgg
    Kira_14 "Ты хочешь, чтобы я с ней об этом поговорила? Я, конечно, могу попробовать..."
    Max_04 "Это ни к чему. Я сказал ей, что наберусь опыта у тебя."
    Kira_15 "Да?! И как она на такое мощное заявление отреагировала?"
    Max_03 "Ха, она думает, что ты до такой степени нравственность ещё не потеряла. Как же много всего она не знает."
    Kira_06 "И хорошо, что не знает. Если бы знала, то точно не пустила бы меня сюда жить."

    # tv-mass-05 + tv-wp-02-max-01-kira-01
    $ var_stage = ''
    scene kira_watch_play_02
    Max_07 "Так вот, я надеюсь, что она сегодня пойдёт проверять, так ли она в тебе уверена. В другие дни ей не до этого, а вот сегодня..."
    Kira_16 "Макс, ты же понимаешь, что в таком случае ругани будет море. Не знаю, что она сделает с тобой, а вот мне точно придётся искать новое жильё."
    Max_09 "Не придётся, тётя Кира! Главное подыграй мне, если она начнёт спускаться по лестнице. А когда пойдут разборки, продолжай подыгрывать в направлении, что меня нужно готовить к взрослой жизни."
    Kira_07 "Ох, Макс... Рискованно... Но смело! Затея мне нравится."

    # tv-watch-01 + porn-k-02_03 + tv-watch-01-kira-01 + tv-watch-01-max-01b
    $ var_stage = '03'
    scene tv_watch kira mgg
    Max_02 "Так, а что ты там насчёт анального секса говорила?"
    Kira_05 "Я просто думала, что тебе уже неймётся это попробовать..."
    Max_04 "Честно говоря, было столько забот, что я и не успевал об этом думать... Попробуем?"
    Kira_04 "Обязательно! Но у меня давненько не было анального секса, поэтому мне нужно будет к этому немного подготовиться..."

    # after-club-s04-f + tv-caught-ann-(01a/01b) + tv-caught-max&kira-01
    scene ann_caught_01
    Max_08 "Тихо, а вот и мама! Самое время тебе раздвинуть ножки, тётя Кира. Начинаем..."

    # tv-cun-01 + tv-caught-max&kira-02
    scene ann_caught_02
    Kira_02 "Да, Макс... Всё правильно. Нужны именно вот-такие лёгкие прикосновения..."

    # tv-cun-01 + tv-caught-ann-(02a/02b) + tv-caught-max&kira-02
    scene ann_caught_02 ann
    Ann_20 "Это что тут такое происходит!!! Ну-ка немедленно прекратите! Кира! Макс! С ума сошли что ли?!"

    # after-club-s06-f + tv-caught-max&kira-03 + tv-caught-ann-(03a/03b)
    scene ann_caught_03
    Max_09 "Мам, давай потише, а то всех разбудишь! Ты же сама разрешила, помнишь? Никаких претензий..."
    Ann_18 "Вообще-то, я ничего такого не разрешала! Я подумала, ты сказал про Киру просто так, чтобы меня позлить..."
    Max_15 "Ну вот, будешь знать, что ко мне нужно относиться посерьёзнее. А теперь, будь добра, иди спать, не отвлекай..."
    Ann_16 "Ах вот так, значит! И вы считаете это нормальным, да? Чтобы родная тётя лежала тут с раздвинутыми ногами и учила своего племянника всяким непристойностям, если не сказать похуже!"
    Kira_16 "Не непристойностям, а взрослой жизни и её... важным аспектам. Раз уж ты сама отказалась помогать сыну, то кому, как не мне следует позаботиться о его воспитании..."

    # after-club-s04-f + tv-caught-ann-(04a/04b) + tv-caught-max&kira-04
    scene ann_caught_04
    Ann_17 "Вот пусть заведёт себе девочку и там осваивает все эти... занятия! Именно таким образом приходит этот опыт и знания, а не на диване со своей тётей."
    Kira_15 "Ой, Ань, а то ты не знаешь, какие бывают девочки по молодости глупые и жестокие. С ними ничему хорошему не научишься, а в добавок они ещё и сердце разобьют. И если второе Макса однозначно ждёт, то вот с первым мы как раз и можем действительно помочь."
    Ann_19 "Знаешь, тоже мне великая учительница нашлась. Ты-то как раз именно такой и была. Ещё не известно, какой похабщине ты его научишь..."
    Kira_13 "Если до тебя ещё вдруг не дошло, то твой мальчик вырос и его запросы тоже! И твоя задача, держать процесс воспитания детей в своих собственных руках, как ты и делала. Только уже интимной сферы жизни."
    Ann_14 "Но это... Одно дело обучать детей каким-то бытовым навыкам и совсем другое... интимным моментам. Это сложно."
    Max_07 "Может, хватит? Тётя Кира мне помочь хочет, в отличие от тебя. Кто не помогает, тот мешает."
    Ann_16 "Так, сынок, давай-ка отойдём и поговорим наедине..." nointeract
    menu:
        "{i}идти на кухню{/i}":
            pass

    # lounge-tv-talk-00 + tv-caught-ann-(05a/05b)
    scene ann_caught_05
    Ann_12 "Как я уже, наверное, говорила - ни стыда, ни совести у тебя, Макс. Вот что прикажешь с тобой делать? Я не знаю..."
    Max_09 "Давай, пока ты будешь думать, я пойду к Кире?"
    Ann_13 "Ну уж нет! Как представлю, чему тебя может научить моя сестра-оторва, аж страшно становится. Я лучше возьму эту задачу на себя, чем буду каждый день беспокоится об этом..."
    Max_10 "Здорово, но... Ты же всё время занята. Когда мы будем успевать?"
    Ann_12 "Что-нибудь придумаем. Можем попробовать тогда, когда я принимаю ванну. Там нам с этим не должны помешать."
    Max_07 "Отлично! Договорились. А ты уверена, что справишься с этим?"
    Ann_14 "Ну... Будет непросто, но я постараюсь. А теперь расходимся по комнатам и спим." nointeract
    menu:
        "{i}пойти спать{/i}":
            $ ann.dcv.private.stage = 4
            if get_rel_eric()[0] > 2:
                $ poss['control'].open(17)
            else:
                $ poss['control'].open(18)
            $ current_room = house[0]
            jump Sleep


label s1_ann_bath:

    scene location house bathroom door-evening

    Max_00 "{m}Сейчас, обычно, мама должна принимать ванну...{/m}" nointeract
    menu:
        "{i}постучаться{/i}":
            if check_is_home('eric') and eric.daily.sweets != 2:
                # Эрик на вилле и не находится под успокоительным
                Max_09 "{m}Пока Эрик у нас в доме, лучше не рисковать заходить к маме. Он в любой момент может зайти в ванную комнату.{/m}" nointeract
                menu:
                    "{i}воспользоваться стремянкой{/i}":
                        jump ann_bath.ladder
                    "{i}уйти{/i}":
                        jump ann_bath.end
            if ann.dcv.private.stage < 5:
                jump s1_ann_intimate_lesson_02
            if ann.dcv.private.stage < 6:
                jump s1_ann_intimate_lesson_03
            if ann.dcv.private.stage < 7:
                jump s1_ann_intimate_lesson_04
            if ann.dcv.private.stage == 7:
                jump s1_ann_rejection

        "{i}войти без стука{/i}":
            # bath-open-00 + bath-open-ann-01
            scene ann_in_bath_open with diss4
            Ann_15 "Макс! Ты почему так нагло врываешься?! Я тут вообще-то ванну принимаю..."
            if ann.dcv.private.stage == 7:
                # bathrooom-bath-02 + bathrooom-bath-02-ann-(01/02/03)
                $ var_pose = renpy.random.choice(['01', '02', '03'])
                scene ann_in_bath_enter with diss4
                Max_07 "Я просто спросить хотел..."
                Ann_12 "Никаких больше уроков. Я ведь уже сказала! А сейчас выйди." nointeract
            else:
                if ann.flags.crush < 1:
                    $ ann.flags.crush = 1
                Max_07 "У нас ведь есть дело, помнишь?"
                Ann_16 "Я не вижу смысла тебя чему-либо учить, Макс, пока ты не научишься стучаться перед тем, как войти!"
                Max_09 "Хорошо, в следующий раз постучусь."
                Ann_17 "Вот и урок наш состоится только в следующий раз, если постучишься. А сейчас выйди." nointeract
            menu:
                "{i}уйти{/i}":
                    jump ann_bath.end
        "{i}воспользоваться стремянкой{/i}":
            jump ann_bath.ladder
        "{i}уйти{/i}":
            jump ann_bath.end


label s1_ann_intimate_lesson_02:
    # 2-ой интимный урок с Анной (ванна)
    # в дни, когда Эрик на вилле и в воскресенье, если Анну удалось уговорить на продолжение интимных уроков

    scene location house bathroom door-evening

    Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
    Max_07 "Это я, Макс. Можно войти?"
    Ann "{b}Анна:{/b} Молодец, что постучался. Заходи, только смотри, чтобы никто не увидел..." nointeract
    menu:
        "{i}войти{/i}":
            pass

    # bathrooom-bath-02 + bathrooom-bath-02-ann-00
    $ var_pose = '00'
    scene ann_in_bath_enter with diss4
    Ann_12 "Только, сынок, это должно быть нашим с тобой огромным секретом, понял? Потому что маме с сыном нехорошо этим заниматься, неправильно."
    Max_01 "Ты же просто будешь меня учить. Что в этом плохого?"

    # after-club-bath01-max&alice-01-f + bathrooom-bath-03-ann&max-01 + Одежда(только Макс)
    $ var_stage, var_pose = '03', '01'
    scene ann_in_bath_talk
    Ann_14 "Да, но {b}ЧЕМУ{/b} учить! Для тебя это всё будет, наверняка, очень интересно... Но чтобы ты понимал, для меня не просто учить {b}ТАКОМУ{/b} своего сына."
    Max_09 "Ну... Уж кто и может научить {b}ТАКОМУ{/b} лучше всех, так это мама. Ты же заинтересована в том, чтобы я был лучшим во всём, в том числе и в {b}ЭТОМ{/b}?"
    Ann_13 "Ох, только такие мысли мне и помогают сейчас. Ладно, раздевайся и залазь ко мне в ванну." nointeract
    menu:
        "{i}раздеться{/i}":
            pass

    # bathrooom-bath-04 + bathrooom-bath-04-ann&max-01
    # $ var_pose, var_stage = '04', '01'
    $ var_stage, var_pose = '04', '01'
    scene ann_in_bath1 with diss4
    Ann_01 "Сейчас мы сядем и немного побеседуем. Ты девочку ещё не завёл?"
    Max_04 "Нет. Но на примете несколько есть."
    Ann_02 "Честно говоря, я рада, что ты интересуешься тем, как не только доставить удовольствие себе, но и твоей девушке."
    Max_03 "Я хочу наслаждаться этим по полной, чтобы хорошо было всем."

    # bathrooom-bath-05 + bathrooom-bath-05-ann&max-01
    $ var_stage = '05'
    Ann_04 "Приятно слышать. Значит будем учить тебя, как следует ласкать женские эрогенные зоны."
    Max_02 "Вверху я в тот раз ведь немного освоился?"
    Ann_14 "Да, но эрогенных зон у женщины очень много, сынок. При чём их уровень возбудимости у каждой женщины разный. Если одна женщина просто с ума сходит, когда ей массируют ножки, то другой это может не особо нравится."
    Max_07 "И определить, какой женщине что нравится, можно только \"прощупав реакцию\", да?"
    Ann_12 "Да, Макс. Всё правильно. Но меня мы \"прощупывать\" не будем. С этим, я думаю, и так всё понятно. А вот то, как нужно ласкать... Вот с этим нам нужно разобраться."

    # bathrooom-bath-06 + bathrooom-bath-06-ann&max-01
    $ var_stage = '06'
    Max_04 "К этому я готов. У меня, вроде, неплохо получалось тогда... на диване?"
    Ann_14 "Да, только вот там мы занимались детскими шалостями по сравнению с тем, чему я должна научить тебя дальше..."
    Max_01 "Мам, не напрягайся ты так. Это же всё в образовательных целях делается. С чего мы начнём?"
    Ann_12 "Ох, ну... Я думаю, сначала нужно проверить, как... как у тебя получится ласкать мою грудь. Даже не верится, что я тебе такое говорю. Давай, устраивайся поближе ко мне..." nointeract
    menu:
        "{i}устроиться между маминых ног{/i}":
            pass

    # bathrooom-bath-12 + bathrooom-bath-12-ann&max-01
    $ var_stage = '12'
    Ann_02 "С поцелуями и массажем у тебя более-менее, но женская грудь... Она куда чувствительнее, особенно сосочки. Поэтому с ней лучше обходиться понежнее. По крайней мере, сначала."
    Max_07 "А впоследствии?"
    Ann_05 "А дальше всё зависит от женщины. Может быть дальше она любит погрубее."
    Max_02 "А как любишь ты?"
    Ann_13 "Макс, ну что за вопрос такой? Мы же этим занимаемся в образовательных целях, а не для удовольствия и забавы."
    Max_03 "Да, но тебе же должно быть приятно, чтобы понять, что у меня хорошо получается?"
    Ann_12 "Макс, ты давай пробуй, а я в свою очередь сделаю какие-то замечания." nointeract
    menu:
        "{i}ласкать мамину грудь{/i}":
            pass

    # bathrooom-bath-08 + bathrooom-bath-08-ann&max-03
    $ var_stage, var_pose = '08', '03'
    Ann_09 "Ахх... Только поаккуратнее с моими сосочками, они очень чувствительные... Не нужно их так грубо ласкать языком! Нежнее, сынок..." nointeract
    menu:
        "{i}ласкать языком нежнее{/i}":
            pass

    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-07
    $ var_stage, var_pose = '10', '07'
    Ann_03 "Да-а... Всё правильно, вот так... Охх... Ты молодец. Продолжай..."
    Max_05 "{m}Какое блаженство играть с маминой грудью! У неё невероятно шикарные сиськи! Такие большие и аппетитные, а сосочки твёрденькие... Ласкал бы без отрыва. Ммм...{/m}"
    Ann_14 "Ухх... А руками уже можно работать более властно... По-хозяйски, так сказать. Ммм... Д-а-а! Ой, что же я такое говорю..."

    # bathrooom-bath-08 + bathrooom-bath-08-ann&max-01
    $ var_stage, var_pose = '08', '01'
    Max_07 "Ладно тебе, мам, не смущайся. Тебе понравилось?"
    Ann_17 "Сынок, ну вот как я должна на это ответить? Если \"да\", то получается я в конец больная, а если \"нет\", то лгунья... Как же неправильно то, что мы делаем!"
    Max_08 "Так может мне всё-таки к тёте Кире пойти, чтобы ты не мучилась?"
    Ann_18 "Нет уж! Раз взялась, то нужно проконтролировать твоё обучение. А там я понятия не имею, чему она тебя научит."

    # bathrooom-bath-06 + bathrooom-bath-06-ann&max-01
    $ var_stage = '06'
    Max_09 "Почему ты так плохо о ней думаешь в этом плане?"
    Ann_12 "Да у неё вся жизнь какая-то сомнительная. Ладно, не будем о ней. Давай закругляться. Продолжим в следующий раз."
    Max_10 "Это что, всё?! Я думал ещё что-то будет..."

    # bathrooom-bath-05 + bathrooom-bath-05-ann&max-01
    $ var_stage = '06'
    Ann_00 "Сынок, мне всё это очень непросто даётся делать. Так что дай маме отдохнуть и побыть одной. О многом нужно подумать."
    Max_00 "Хорошо. Тогда до следующего раза." nointeract
    menu:
        "{i}уйти{/i}":
            $ renpy.end_replay()
    $ poss['control'].open(19)
    $ ann.dcv.private.stage = 5
    $ spent_time += 30
    jump Waiting


label s1_ann_intimate_lesson_03:

    scene location house bathroom door-evening

    Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
    Max_07 "Это я, Макс. Можно войти?"
    Ann "{b}Анна:{/b} Молодец, что постучался. Заходи, только смотри, чтобы никто не увидел..." nointeract
    menu:
        "{i}войти{/i}":
            pass

    # bathrooom-bath-02 + bathrooom-bath-02-ann-00
    $ var_pose = '00'
    scene ann_in_bath_enter with diss4
    Ann_14 "Я надеюсь Лиза не видела, что ты пошёл в ванную комнату? Она же сейчас на кухне..."
    Max_00 "Да я как-то не смотрел, видела она или нет."
    Ann_18 "Макс, ты же понимаешь, как важно держать наши с тобой занятия в тайне! Если она видела..."
    Max_01 "Мам, это шутка была. Она не видела, так что расслабься."

    # after-club-bath01-max&alice-01-f + bathrooom-bath-03-ann&max-01 + Одежда(только Макс)
    $ var_stage, var_pose = '03', '01'
    scene ann_in_bath_talk
    Ann_13 "Фух... Не пугай меня так больше! Я и так на нервах из-за наших уроков."
    Max_07 "Извини. А ты почему прикрываешься? Я же ведь уже всё видел и не раз. И не только видел."
    Ann_16 "Смотри мне, договоришься сейчас! Если ты здесь только для того, чтобы поглазеть на голую маму, то урока сегодня не будет."
    Max_09 "Что ты! Я здесь ради знаний!"
    Ann_12 "Тогда хватит шутки шутить, залазь ко мне в ванну." nointeract
    menu:
        "{i}раздеться{/i}":
            pass
    # bathrooom-bath-04 + bathrooom-bath-04-ann&max-01
    $ var_stage, var_pose = '04', '01'
    scene ann_in_bath1 with diss4
    Ann_14 "Да, сынок... Не верится даже, что ты так подрос. Кажется, что ещё совсем недавно только в школу пошёл..."
    Max_03 "Ну ты, мам, вспомнила!"

    # bathrooom-bath-05 + bathrooom-bath-05-ann&max-01
    $ var_stage = '05'
    Ann_12 "Да, было время... А сейчас вон чем мы занимаемся! Дальше, я так полагаю, нужно показать тебе, как ласкать женщину... ну там, внизу..."
    Max_02 "Мне нравится слово \"киска\"!"
    Ann_02 "Пусть так. Честно говоря, я считаю, ты с этим справишься и без уроков, потому что пальчиками ты работаешь хорошо, массажист ты наш талантливый."
    Max_09 "Подожди! Но это всё равно же не одно и то же! Там же тоже, наверно, нужно как-то понежнее себя вести? Или нет?"

    # bathrooom-bath-06 + bathrooom-bath-06-ann&max-01
    $ var_stage = '06'
    Ann_04 "Ну... Там, на самом деле, можно по разному, то наращивая темп стимуляции, то сбавляя. А сначала лучше конечно понежнее и помедленнее. По крайней мере, мне так нравится... В смысле, я думаю, что так нравится всем женщинам."
    Max_07 "Ага... Но мне же всё равно нужно попробовать это сделать! Чтобы хоть представление иметь, как это вообще происходит..."
    Ann_13 "Ой, не знаю, сынок... Понимаю, что тебе это нужно, но может... Мне нравится, что у нас тобой такие близкие отношения, но делать {b}ТАКОЕ{/b}... В голове не укладывается."
    Max_01 "А мы всего разок попробуем и всё. Для образовательных целей же."

    # bathrooom-bath-07 + bathrooom-bath-07-ann&max-01
    $ var_stage = '07'
    Ann_12 "Так уж и быть. Ты уже меня видел, так что постараюсь не стесняться и покажу тебе, как это всё происходит."
    Max_04 "Ты лучшая мама на свете! Как же я благодарен тебе за эти знания и опыт. Это очень дорогого стоит. Ты самая-самая!"
    Ann_02 "Спасибо! Надеюсь, ты помнишь, как это делали в том эротическом ролике, что мы смотрели?"
    Max_07 "Ну, в общих чертах, да. Но, твои наставления однозначно нужны."

    # bathrooom-bath-09 + bathrooom-bath-09-ann&max-01
    $ var_stage = '09'
    Ann_04 "Для начала, попробуй просто поводить по ней пальчиком... вверх-вниз... нежно и аккуратно, не торопясь." nointeract
    menu:
        "{i}следовать маминому совету{/i}":
            pass
    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-02
    $ var_stage, var_pose = '10', '02'
    Ann_14 "Да, вот так... Можно до такой степени не осторожничать, не бойся. Поувереннее, сынок..."
    Max_10 "Я просто не знаю... Вдруг, я сделаю тебе больно!"
    Ann_09 "Не переживай из-за этого, всё хорошо. Нежно и уверенно... Ухх... Да... Хорошо... В смысле, у тебя хорошо получается."
    Max_07 "А что делать дальше?"

    # bathrooom-bath-08 + bathrooom-bath-08-ann&max-01
    $ var_stage, var_pose = '08', '01'
    Ann_08 "Теперь можешь попробовать водить пальчиками из стороны в сторону, а так же круговыми движениями. И темп уже можно понемногу наращивать."
    Max_01 "Ага, сейчас попробую..."

    # bathrooom-bath-09 + bathrooom-bath-09-ann&max-03
    $ var_stage, var_pose = '09', '03'
    Ann_09 "Ох, сынок... Никогда бы не подумала, что ты делаешь это впервые! Ммм... У тебя волшебные пальчики..."
    Max_05 "Правда?! Видимо, сказываются мои навыки в массаже."
    Ann_14 "Похоже на то... Д-а-а... Можно побыстрее. Помнишь, что я говорила? Ухх... Наращивать темп... О да! Вот так... Ещё... Ой, что я такое говорю!"
    Max_04 "Не напрягайся из-за этого, мам. По твоим эмоциям я лучше понимаю, что всё делаю правильно."
    Ann_09 "Я понимаю, но... Мне стоит держать себя в руках, иначе пропадёт вся серьёзность наших с тобой уроков."
    Max_07 "Так, а как мне действовать дальше?"

    # bathrooom-bath-12 + bathrooom-bath-12-ann&max-01
    $ var_stage, var_pose = '12', '01'
    Ann_13 "Ой, сынок, я даже не знаю... Дальше должно идти уже проникновение пальчиков... в киску. Но это..."
    Max_03 "О, круто! Значит, постимулировал снаружи, раззадорил, а теперь смещаю акцент внутрь?"
    Ann_17 "Смахиваешь на лету. Но я не уверена, что мы будем это делать."
    Max_08 "Но почему? Я же, вроде, всё нормально делал..."

    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-01
    $ var_stage, var_pose = '10', '01'
    Ann_12 "Ты молодец, Макс. Просто, проникнуть пальцами в свою маму... Тебе не кажется, что это уже совсем перебор? Не говоря уже о том, до какой степени матери с сыном неправильно заниматься {b}ТАКИМ{/b}..."
    Max_09 "Мы же учимся! Вернее, учусь я, а ты делишься со мной важными знаниями. Я же должен знать, какие движения делать там, внутри. Там явно будет иначе."
    Ann_14 "Ох, Макс... Надеюсь, я потом, после всего этого, смогу тебе в глаза смотреть и не краснеть. Что я делаю..."
    Max_07 "Так как мне лучше это сделать?"
    Ann_12 "Всё так же, нежно и не спеша. Просто вводи свои пальчики в мою киску..." nointeract
    menu:
        "{i}сделать, как сказала мама{/i}":
            pass
    # bathrooom-bath-09 + bathrooom-bath-09-ann&max-04
    $ var_stage, var_pose = '09', '04'
    Ann_09 "Ахх... Да... Не спеши, не проникай сразу как можно глубже. Вот так... Ммм..."
    Max_05 "Ух ты, мам! Это классно! Что дальше?"
    Ann_10 "Теперь двигай своими пальчиками, назад-вперёд... Постепенно наращивая темп... Ухх... Да, отлично..."
    Max_08 "Ой, мам, а там становится... мокренько! Это нормально или я что-то не так делаю?"

    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-04
    $ var_stage = '10'
    Ann_08 "Ах, Макс, ты всё делаешь правильно. Чем больше женщина возбуждена твоей прелюдией, тем влажнее становится её киска. Ммм..."
    Max_03 "Мои пальцы от этого проскальзывают в тебя всё легче и легче, хотя ты довольно узенькая."
    Ann_14 "Ой, сынок, не смущай меня ещё сильнее такими словами! Я вообще не ожидала такой реакции от себя... Ахх... Это очень странно."
    Max_07 "А ты думала, что тебе будет приятно, но при этом мокренькой ты становиться не будешь?"
    Ann_12 "Именно! Поэтому... На этот раз, я думаю, достаточно, сынок. Закругляемся."

    # bathrooom-bath-07 + bathrooom-bath-07-ann&max-01
    $ var_stage, var_pose = '07', '01'
    Max_04 "Ты только не переживай из-за этого, мам. Ну подумаешь, понравилось... Мне вот это всё очень нравится. Столько нового для себя открыл."
    Ann_17 "Да уж, но вот мои открытия меня больше озадачили... Всё, хватит глазеть." nointeract
    menu:
        "{i}освободить ванну{/i}":
            pass
    # bathrooom-bath-05 + bathrooom-bath-05-ann&max-02
    $ var_stage, var_pose = '05', '02'
    Ann_15 "Ой, Макс! Как же ты возбудился! Хотя, чего я удивляюсь. Я же здесь, перед тобой, с раздвинутыми ногами сидела и {b}ТАКОМУ{/b} учила..."
    Max_07 "Ну да. Я же сказал, что мне {b}ОЧЕНЬ{/b} понравилось."
    Ann_13 "Думаю, тебе нужно принять душ и сбросить... это напряжение. С учётом того, чем мы тут с тобой занимались, смысла стесняться нет. Давай бегом, я не буду смотреть."
    Max_01 "Хорошо, мам!"

    # bathrooom-bath-10 + bathrooom-bath-01-max-01 + bathrooom-bath-01-ann-02
    $ var_stage, var_pose = '10', '02'
    scene ann_in_bath2 with diss4
    Max_07 "{m}Это что-то с чем-то! Теперь мои пальцы побывали в маминой киске. В маминой!!! И не менее приятно то, что она от этого так потекла... Интересно, что она теперь будет делать после такого? Вдруг она решит прекратить эти уроки?!{/m}" nointeract
    menu:
        "{i}дрочить, глядя на маму{/i}":
            pass
    # bathrooom-bath-10 + bathrooom-bath-01-max-01 + bathrooom-bath-01-ann-03
    $ var_pose = '03'
    Ann_15 "Макс! А что это ты там делаешь?!"
    Max_08 "Эээ... Ну, как бы это... снимаю напряжение. Ты же сама разрешила."

    # bathrooom-bath-11 + bathrooom-bath-11-ann-01 + bathrooom-bath-11-max-01
    $ var_stage, var_pose = '11', '01'
    Ann_17 "Да, но... Я думала, ты хотя бы отвернёшься и будешь делать это не глядя на меня."
    Max_09 "А зачем мне отворачиваться и фантазировать о ком-то, когда всего в метре от меня, за стеклом {b}ТЫ{/b}? С твоей красотой ни одна фантазия не сравнится и близко!"
    Ann_12 "Очень приятно слышать, конечно, но это ненормально, когда сына так сильно возбуждает его собственная мать."
    Max_07 "Ты для меня и женщиной являешься. И очень сексуальной женщиной!"
    Ann_16 "И не стыдно тебе вот так демонстративно это делать прямо передо мной, а?" nointeract
    menu:
        "{i}кончить!{/i}":
            pass
    # bathrooom-bath-11 + bathrooom-bath-11-ann-02 + bathrooom-bath-11-max-02 + bathrooom-bath-11-max-02cum
    $ var_pose = '02'
    scene ann_in_bath2 cum
    Ann_17 "Ну Макс! Вот что ты наделал! Всё стекло заляпал... Даже не вздумай уходить, не прибравшись за собой! Безобразник."
    Max_20 "Фух... Конечно приберусь, не ругайся." nointeract
    menu:
        "{i}прибраться и уйти{/i}":
            $ renpy.end_replay()
    $ poss['control'].open(20)
    $ ann.dcv.private.stage = 6
    $ spent_time += 30
    jump Waiting


label s1_ann_intimate_lesson_04:

    scene location house bathroom door-evening

    Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
    Max_07 "Это я, Макс. Можно войти?"
    Ann "{b}Анна:{/b} Молодец, что постучался. Заходи, только смотри, чтобы никто не увидел..." nointeract
    menu:
        "{i}войти{/i}":
            pass

    # bathrooom-bath-02 + bathrooom-bath-02-ann-(01/02/03)
    $ var_pose = renpy.random.choice(['01', '02', '03'])
    scene ann_in_bath_enter with diss4
    Ann_02 "Ну... Что стоишь и глазеешь? Раздевайся и залазь в ванну."
    Max_09 "Я просто не был уверен, что наши уроки будут продолжаться."

    # after-club-bath01-max&alice-01-f + bathrooom-bath-03-ann&max-02 + Одежда(только Макс)
    $ var_stage, var_pose = '03', '02'
    scene ann_in_bath_talk
    Ann_05 "Уж как минимум закрепить пройденное надо, Макс. Если ты готов."
    Max_05 "Я всегда готов!" nointeract
    menu:
        "{i}раздеться{/i}":
            pass
    # bathrooom-bath-04 + bathrooom-bath-04-ann&max-01
    $ var_stage, var_pose = '04', '01'
    scene ann_in_bath1 with diss4
    Ann_12 "Надеюсь, на всех прошедших уроках ты не просто меня разглядывал, но и усвоил мои наставления."
    Max_01 "Я был очень внимательным! Ну... к наставлениям."

    # bathrooom-bath-05 + bathrooom-bath-05-ann&max-01
    $ var_stage = '05'
    Ann_04 "Тогда сегодня твоя задача, попытаться совместить знания со всех наших уроков. Думаю, ты справишься. Ты у меня талантливый." nointeract
    menu:
        "{i}устроиться между маминых ног{/i}":
            pass
    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-01
    $ var_stage = '10'
    Ann_02 "Сейчас я не буду тебе ничего подсказывать. Попробуешь полностью сам."
    Max_07 "Тогда ты должна не сдерживаться в выражении эмоций! Мне же нужен ориентир."
    Ann_13 "Ну... Хорошо, я буду вести себя так, как вела бы со своим мужчиной. Хоть мне и не очень удобно это делать..." nointeract
    menu:
        "{i}начать водить пальцами по маминой киске{/i}":
            pass
    # bathrooom-bath-09 + bathrooom-bath-09-ann&max-02
    $ var_stage, var_pose = '09', '02'
    Ann_14 "Оу! Ты решил начать сразу оттуда... Чему я тебя учила, сынок? А как же прелюдия?"
    Max_02 "Не переживай, она тоже будет."
    Ann_03 "Охх... Не знаю, что ты там придумал, но, так уж и быть, продолжай... Д-а-а..." nointeract
    menu:
        "{i}ласкать пальцами быстрее{/i}":
            pass
    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-03
    $ var_stage, var_pose = '10', '03'
    Ann_08 "Ммм... Должна признать, пальчиками ты работаешь очень приятно. Ахх... Как хорошо... что ты стал заниматься массажем."
    Max_03 "{m}Чёрт, как же мне хочется попробовать на вкус эти нежные губки... Интересно, она позволит мне это сделать? Лучше посильнее её раззадорить, чтобы она не смогла от этого отказаться.{/m}"

    # bathrooom-bath-09 + bathrooom-bath-09-ann&max-04
    $ var_stage, var_pose = '09', '04'
    Ann_09 "Да, как хорошо! Я хочу, чтобы твои пальчики двигались ещё быстрее... Ухх... Д-а-а... Вот так. Какой же ты у меня молодец!"
    Max_04 "{m}Ох, мама так завелась от удовольствия или же она просто отыгрывает роль? Как бы там ни было, самое время переходить к её груди... Все руки должны быть при деле!{/m}"

    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-05
    $ var_stage, var_pose = '10', '05'
    Ann_14 "Да, продолжай... Всё правильно. Свои ручки используй по максимуму. Д-а-а... А так же не забывай потренировать свой язычок на моих сосочках, потому что с этим у тебя куда меньше опыта..." nointeract
    menu:
        "{i}следовать маминому совету{/i}":
            pass
    # bathrooom-bath-10 + bathrooom-bath-10-ann&max-08
    $ var_stage, var_pose = '10', '08'
    Max_02 "{m}Мама даже и близко не представляет, сколько на самом деле у меня опыта и в том, и в том. Но языком всё же лучше работать не очень изобретательно. Если с руками ещё можно успехи списать на опыт в массаже, то с языком так не выйдет. Я же не чемпион по облизыванию Чупа-Чупсов.{/m}"
    Ann_10 "Ох, сынок... Ммм... Да... Очень неплохо. Думаю, я достаточно хорошо тебя подготовила... Ухх... Надо закругляться."

    # bathrooom-bath-12 + bathrooom-bath-12-ann&max-01
    $ var_stage, var_pose = '12', '01'
    Max_08 "Как это закругляться?! А мне разве не стоит побольше попрактиковаться языком, раз уж он у меня отстаёт от пальцев? Я хочу опробовать его на твоей киске."
    Ann_13 "Нет, Макс... Такое делать - это уже совсем уму не постижимо..." nointeract
    menu:
        "{i}ласкать мамину киску языком{/i}":
            pass
    # bathrooom-bath-07 + bathrooom-bath-07-ann&max-02
    $ var_stage, var_pose = '07', '02'
    Ann_14 "Охх... сынок... Что же ты вытворяешь! Нам нельзя... Ах... Это... невероятно... Я... я не могу сопротивляться... Это не в моих силах! Как же хорошо..." nointeract
    menu:
        "{i}не останавливаться{/i}":
            pass
    # bathrooom-bath-08 + bathrooom-bath-08-ann&max-05
    $ var_stage, var_pose = '08', '05'
    Ann_09 "Д-а-а... Кажется, я ошиблась... Ты и языком талантливо управляешься! Ухх... Ещё... Ох, это... нет слов, как приятно... Я и секунды больше не продержусь..."
    Max_07 "{m}Да, мама вот-вот кончит! Чёрт, да я и сам от её стонов уже на грани...{/m}" nointeract
    menu:
        "{i}проникнуть в маму пальцами{/i}":
            pass
    # bathrooom-bath-12 + bathrooom-bath-12-ann&max-03
    $ var_stage, var_pose = '12', '03'
    Ann_11 "Ещё быстрее... Моё тело меня больше не слушается... Ох, я кончаю, сынок... Д-а-а..." nointeract
    menu:
        "{i}тоже кончить!{/i}":
            pass
    # bathrooom-bath-12 + bathrooom-bath-12-ann&max-04 + bathrooom-bath-12-ann&max-04cum
    $ var_pose = '04'
    scene ann_in_bath1 cum
    Ann_17 "Макс! Ну что же ты делаешь?! Всю меня своей спермой забрызгал! Не мог отвернуться что ли?"
    Max_22 "Фух, извини... Перевозбудился... Хотелось просто кончить, а куда - неважно!"

    # bath-sex-01 + bathrooom-bath-05-ann&max-03 + bathrooom-bath-05-ann&max-03cum
    scene ann_in_bath3_cum
    Ann_12 "Пора, сынок, всё это заканчивать. Я имею ввиду, эти уроки. До добра это не доведёт точно. И зачем я только на это согласилась..."
    Max_08 "Но, мам..."
    Ann_16 "Не спорь! Всё это ты должен осваивать со своей девушкой, а не с мамой. Надеюсь, мы сможем представить, что на этих уроках ничего не было."
    Max_09 "Ну... Даже не знаю. После твоих стонов..."
    Ann_17 "Забыли, сынок! А теперь иди. Мне нужно привести себя в порядок." nointeract
    menu:
        "{i}уйти{/i}":
            $ renpy.end_replay()

    $ poss['control'].open(21)
    $ ann.dcv.private.stage = 7
    $ spent_time += 30
    jump Waiting


label s1_ann_rejection:

    scene location house bathroom door-evening

    Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
    Max_07 "Это я, Макс. Можно войти?"
    Ann "{b}Анна:{/b} Никаких больше уроков. Я ведь уже сказала! Не мешай..." nointeract
    menu:
        "{i}уйти{/i}":
            jump ann_bath.end

# всегда в конце файла
label start_room_navigation():

    call screen room_navigation

    jump AfterWaiting
