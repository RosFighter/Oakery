
label EricTalkStart:

    $ dial = TalkMenuItems()

    $ __cur_plan = eric.get_plan()
    if __cur_plan.talklabel is not None:
        call expression __cur_plan.talklabel from _call_expression_13

    if len(dial) > 0:
        $ dial.append((_("{i}В другой раз...{/i}"), "exit"))
    else:
        jump Waiting

    $ renpy.block_rollback()
    Eric_01 "Чего хотел, Макс?" nointeract
    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        if renpy.has_label(talks[rez].label): # если такая метка сушествует, запускаем ее
            call expression talks[rez].label from _call_expression_14
        jump EricTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label eric_needmoney:
    # стартовая фраза "Мне нужны деньги..."
    Eric_09 "Ну так заработай! Причём тут я?"
    Max_09 "Мы договаривались..."
    Eric_03 "Да? Ну, ладно... Держи. Только на глаза не попадайся..."
    Max_01 "Хорошо..."

    $ mgg.ask(5, talk_var['eric.fee'])
    $ dcv['eric.money'].set_lost(1)

    return


label eric_voy_wtf:

    # стартовая фраза "Эрик, мы же договорились!"

    Eric_05 "А можно конкретнее? О чём речь?"
    Max_15 "Меня наказали за подглядывания!"
    Eric_08 "Ну, и что здесь не так? Подглядывал - наказали... Преступление и наказание. Классика!"
    Max_09 "Ты обещал, что можно будет подглядывать без наказаний!"

    menu:
        Eric_06 "Я такое обещал? Хм... Может быть. То есть, ты хочешь, чтобы я убедил твою маму, что это нормально, когда она трахается на твоих глазах и нужно молчать?"
        "Э... Ну не совсем так...":
            Eric_03 "А как? Через раз? Один раз можно, другой нет? Так чего именно ты хочешь?"

        "А так можно?":
            Eric_03 "Ну у тебя и запросы, Макс! Я даже не знаю... Ты точно этого хочешь?"

    Max_07 "Я хочу смотреть и чтобы мне ничего за это не было!"

    menu:
        Eric_01 "Да уж. Ну, раз мы с тобой теперь друзья, я что-нибудь придумаю. Только это будет не сразу, а постепенно, но думаю, что смогу настроить маму так, как нужно..."
        "Кстати, как ты это делаешь?":
            Eric_02 "Не понял. Как я делаю... что?"
            Max_09 "Ну... Манипулируешь мамой, например..."

            menu:
                Eric_03 "Так я тебе и выдал свой секрет! Не сейчас. Может быть, однажды расскажу. Но поверь, мой способ очень эффективен! Так что, слушайся меня и я не буду настраивать никого против тебя..."
                "Это угроза?":
                    Eric_04 "А, думай что хочешь. Но то, что теперь твоя жизнь в моих руках, это факт. И теперь я тебе буду давать немного меньше денег, раз у тебя такие специфичные требования насчёт мамы..."
                    Max_10 "Так не честно! Мы об этом сразу договаривались!"

                "Хорошо, Эрик!":
                    Eric_00 "Да, раз у тебя такие необычные запросы насчёт твоей мамы, то теперь я тебе буду давать чуть меньше денег, чем собирался..."
                    Max_10 "Так не честно! Мы об этом сразу договаривались!"

        "Отлично! Спасибо, Эрик.":
            Eric_00 "Да, раз у тебя такие необычные запросы насчёт твоей мамы, то теперь я тебе буду давать чуть меньше денег, чем собирался..."
            Max_10 "Так не честно! Мы об этом сразу договаривались!"
    menu:
        Eric_01 "Вообще, жизнь - штука несправедливая. А учитывая, что твоя ещё и в моих руках, то жаловаться никому не стоит, даже мне. Ну всё, иди займись чем-нибудь..."
        "{i}уйти{/i}":
            pass

    $ talk_var['eric.voy.stage'] = 2
    $ talk_var['eric.fee'] -= 10
    return


label lessons_from_Eric:
    $ _stockings = RandomChance(500) # шанс, что Аня будет в чулках, 50%
    if talk_var['eric.voy.stage']==4:
        jump .first_bj
    elif talk_var['eric.voy.stage']==5:
        jump .second_bj
    elif talk_var['eric.voy.stage']==6:
        jump .third_bj
    else:
        "{b}Продолжение в следующей версии...{/b}"
        jump eric_ann_fucking.voyeur  # временный уход на успешное подглядывание

    label .first_bj:

        scene BG char Eric annroom-watch-01
        show Eric watch 01-bj01
        if _stockings:
            show other Eric watch 01-bj01a
        $ renpy.show('Max annroom-watch 01'+mgg.dress)
        #annroom-watch-01 + annroom-watch-01-ann&eric-bj(01-01a) + annroom-watch-01-max-(01-01b)

        Max_07 "К вам ведь можно?"
        Eric_03 "Да, Макс, проходи..."

        scene BG char Eric annroom-watch-02-bj01
        show Eric watch 02-bj01
        if _stockings:
            show other Eric watch 02-bj01a
        $ renpy.show('Max annroom-watch 02-bj01'+mgg.dress)
        #annroom-watch-02-bj01 + annroom-watch-02-bj01-ann&eric-(01-01a) + annroom-watch-02-bj01-max-(01-01b)

        Ann_14 "Эрик! Ты правда хочешь, чтобы он смотрел, как мы с тобой... здесь..."
        Eric_09 "Ань, расслабься! Детям нужно об этом от кого-то узнать. Или ты хочешь, чтобы они выросли неприспособленными к нормальной социальной жизни!?"
        Ann_13 "Конечно я хочу, чтобы с детьми всё было в порядке! Но, как его пребывание с нами поможет? Это просто неправильно!"
        Eric_00 "Мы не можем изменить наш образ жизни, чтобы всем угодить. Ты всё время на работе и со мной. Макс остаётся без внимания и более того, без родителей. Как думаешь, выйдет из него что-нибудь толковое, если он будет предоставлен самому себе!?"
        Ann_15 "Нет... Теперь я понимаю, почему он пытается подглядывать за нами. Ему не хватает родительского внимания!"

        scene BG char Eric annroom-watch-01
        show Eric watch 01-bj01
        if _stockings:
            show other Eric watch 01-bj01a
        $ renpy.show('Max annroom-watch 01'+mgg.dress)
        #annroom-watch-01 + annroom-watch-01-ann&eric-bj(01-01a) + annroom-watch-01-max-(01-01b)

        Eric_01 "Именно, Ань! И лишь в такие интимные моменты ты можешь показать ему, как ты о нём заботишься и как он для тебя важен."
        Ann_14 "Прости, Макс... Я была такой никудышной матерью по отношению к тебе..."
        Max_00 "Всё хорошо, мам! Я думаю, это всё сможет нас сблизить!"

        scene BG char Eric annroom-watch-02-bj01
        show Eric watch 02-bj01
        if _stockings:
            show other Eric watch 02-bj01a
        $ renpy.show('Max annroom-watch 02-bj01'+mgg.dress)
        #annroom-watch-02-bj01 + annroom-watch-02-bj01-ann&eric-(01-01a) + annroom-watch-02-bj01-max-(01-01b)

        Eric_02 "А теперь Ань, ты должна вести себя так, как вела бы, если бы мы были только вдвоём! Давай, продолжай то, на чём мы остановились..."
        Ann_12 "Да, ты прав, я должна сделать это, ради Макса..."
        menu:
            Eric_03 "А ты Макс, подсаживайся, не стесняйся..."
            "{i}сесть на кровать{/i}":
                pass

        scene BG char Eric annroom-watch-03-bj01
        show Eric watch 03-bj01
        if _stockings:
            show other Eric watch 03-bj01a
        $ renpy.show('Max annroom-watch 03-bj01'+mgg.dress)
        #annroom-watch-03-bj01 + annroom-watch-03-bj01-ann&eric-(01-01a) + annroom-watch-03-bj01-max-(01-01b)

        Max_08 "{i}( Вау! Мама продолжила отсасывать Эрику! При мне... Хотя, видно что делает она это не так чувственно, как раньше. ){/i}"
        Eric_05 "Смотри Макс, как хороша твоя мама! А ты Ань, не стесняйся, делай это уверенно... Покажи Максу, каким удовольствием делятся любящие друг друга люди."
        Max_07 "{i}( Главное не перевозбуждаться настолько, чтобы мой член меня выдал... Хотя, сложно не представлять себя на месте Эрика! ){/i}"
        menu:
            Eric_04 "Ух, детка, да... Прервись ненадолго, я хочу лечь поудобнее..."
            "{i}слегка подвинуться{/i}":
                pass

        scene BG char Eric annroom-watch-04-bj01
        show Eric watch 04-bj01
        if _stockings:
            show other Eric watch 04-bj01a
        $ renpy.show('Max annroom-watch 04-bj01'+mgg.dress)
        #annroom-watch-04-bj01 + annroom-watch-04-bj01-ann&eric-(01-01a) + annroom-watch-04-bj01-max-(01-01b)

        Max_10 "{i}( Какая же она обалденная! Такую женщину я бы с удовольствием ласкал часами... Она это заслуживает! ){/i}"
        Eric_01 "Твоя мама ещё довольно скована, так что для первого раза думаю достаточно. Нет ничего такого в том, чтобы делиться близостью, но ей нужно время, чтобы привыкнуть."
        menu:
            Max_00 "Хорошо, я тогда пошёл... Продолжайте!"
            "{i}уйти{/i}":
                jump .end

    label .second_bj:

        scene BG char Eric annroom-watch-01
        show Eric watch 01-bj02
        if _stockings:
            show other Eric watch 01-bj02a
        $ renpy.show('Max annroom-watch 01'+mgg.dress)
        #annroom-watch-01 + annroom-watch-01-ann&eric-bj(02-02a) + annroom-watch-01-max-(01-01b)

        Max_07 "К вам ведь можно?"
        Eric_03 "Да, Макс, проходи... Твоей маме как раз есть о чём тебе рассказать!"

        scene BG char Eric annroom-watch-02-bj02
        show Eric watch 02-bj02
        if _stockings:
            show other Eric watch 02-bj02a
        $ renpy.show('Max annroom-watch 02-bj01'+mgg.dress)
        #annroom-watch-02-bj02 + annroom-watch-02-bj02-ann&eric-(01-01a) + annroom-watch-02-bj01-max-(01-01b)

        Ann_13 "А вам не кажется, что это уже слишком!?"
        Max_01 "{i}( Похоже, я застал маму в очень... открытом положении. Она уже не так враждебна, как в первый раз, но очень смущена! ){/i}"
        Eric_05 "По мне, так это отличный способ для того, чтобы мужчине и женщине ещё больше сблизиться. Вы достаточно открыты друг для друга и все при деле..."
        Max_00 "Ясно. Вы продолжайте, а я посмотрю... как это..."
        Ann_14 "Эрик, ты уверен, что это правильно, так откровенно показывать меня сыну!? Я в больших сомнениях!"
        Eric_03 "Не напрягайся из-за этого, Ань. Всё, что мы с тобой делаем - это естественно. И Максу нужно это знать и увидеть..."
        Ann_12 "Да, Эрик. Если ты в этом уверен, то и я тоже..."
        menu:
            Eric_01 "Вот и отлично! Присаживайся, Макс."
            "{i}сесть на кровать{/i}":
                pass

        scene BG char Eric annroom-watch-03-bj02
        show Eric watch 03-bj02
        if _stockings:
            show other Eric watch 03-bj02a
        $ renpy.show('Max annroom-watch 03-bj02'+mgg.dress)
        #annroom-watch-03-bj02 + annroom-watch-03-bj02-ann&eric-(01-01a) + annroom-watch-03-bj02-max-(01-01b)

        Max_07 "{i}( Так близко к голой маминой попке я ещё не был! А она ведь ещё при этом Эрику отсасывает... Да уж, это что-то нереальное! ){/i}"
        Eric_04 "Ого, Ань! Мне кажется или ты стала ещё более мокренькой, чем всегда?"
        Ann_15 "Эрик! Не говори такое при Максе! Всё это и так меня очень смущает..."
        menu:
            Eric_02 "А по-моему это смущение делает тебя только слаще! Только посмотри, как твоя мама меня любит, Макс..."
            "{i}смотреть, как мама сосёт{/i}":
                pass

        scene BG char Eric annroom-watch-04-bj02
        show Eric watch 04-bj02
        if _stockings:
            show other Eric watch 04-bj02a
        $ renpy.show('Max annroom-watch 04-bj02'+mgg.dress)
        #annroom-watch-04-bj02 + annroom-watch-04-bj02-ann&eric-(01-01a) + annroom-watch-04-bj02-max-(01-01b)

        Max_04 "{i}( Не могу перестать представлять себя на месте Эрика! Я бы намертво вцепился в её шикарную попку, пока она не кончила бы... ){/i}"
        Eric_01 "Я думаю, на сегодня ты увидел достаточно, Макс. Твою маму ещё немного смущает, что ты смотришь."
        menu:
            Max_00 "Хорошо, я тогда пошёл... Продолжайте!"
            "{i}уйти{/i}":
                jump .end

    label .third_bj:

        scene BG char Eric annroom-watch-01
        show Eric watch 01-bj03
        if _stockings:
            show other Eric watch 01-bj03a
        $ renpy.show('Max annroom-watch 01'+mgg.dress)
        #annroom-watch-01 + annroom-watch-01-ann&eric-bj(03-03a) + annroom-watch-01-max-(01-01b)

        Max_07 "К вам ведь можно?"
        Eric_03 "Да, Макс, как раз вовремя... Мы кое-что тебе покажем, да Ань!?"


        scene BG char Eric annroom-watch-02-bj03
        show Eric watch 02-bj03
        if _stockings:
            show other Eric watch 02-bj03a
        $ renpy.show('Max annroom-watch 02-bj03'+mgg.dress)
        #annroom-watch-02-bj03 + annroom-watch-02-bj03-ann&eric-(01-01a) + annroom-watch-02-bj03-max-(01-01b)

        Ann_12 "Ты правда думаешь, что ему нужно такое показывать?"
        Eric_05 "Просто расслабься, детка... И делай, что нужно! Такое Максу тоже не лишним будет знать."
        Max_09 "А о чём идёт речь?"
        menu:
            Eric_04 "О чувственном и глубоком минете, Макс! Там есть несколько... моментов, на которые я обращу внимание. Ты садись и смотри. И ты Ань начинай..."
            "{i}сесть на кровать{/i}":
                pass

        scene BG char Eric annroom-watch-03-bj03
        $ renpy.show('Max annroom-watch 03-bj03'+mgg.dress)
        show Eric watch 03-bj03
        if _stockings:
            show other Eric watch 03-bj03a
        #annroom-watch-03-bj03 + annroom-watch-03-bj03-ann&eric-(01-01a) + annroom-watch-03-bj03-max-(01-01b)

        Max_08 "{i}( Ого! Мама уже так спокойно стала сосать его член при мне, вот это да... Реально поражаюсь тому, как Эрик манипулирует и обрабатывает людей! ){/i}"
        Eric_06 "Да-а-а, детка, вот так... Скоро, Макс, ты уже будешь знать об этом всё, что только можно!"
        Max_07 "Ага. Но ты хотел рассказать мне о каких-то моментах?"
        Eric_03 "Да, точно! Так вот, здесь важно чувствовать, в каком темпе и как глубоко ты можешь двигаться. Это чувствуешь по тому, как женщина к тебе прикасается..."
        Max_01 "Ясно. А что ещё?"
        menu:
            Eric_01 "Ань, давай ложись на спину. Покажем Максу ещё кое-что..."
            "{i}пересесть{/i}":
                pass

        scene BG char Eric annroom-watch-04-bj03
        show Eric watch 04-bj03
        if _stockings:
            show other Eric watch 04-bj03a
        $ renpy.show('Max annroom-watch 04-bj03'+mgg.dress)
        #annroom-watch-04-bj03 + annroom-watch-04-bj03-ann&eric-(01-01a) + annroom-watch-04-bj03-max-(01-01b)

        Max_04 "{i}( Как только этот Эрик не крутит мамой! Хотя, такую фигуристую красотку я бы тоже покрутил на своём члене... ){/i}"
        Eric_04 "Главное, Макс, это двигаться уверенно, чтобы и она чувствовала, чего ты хочешь. Если она захочет сильнее, глубже или быстрее, то сама направит тебя своими прикосновениями..."
        Max_03 "Круто!"
        Eric_03 "А то! В дополнение, можешь массировать её грудь и вообще всё, до чего дотянешься. Видишь, с какой страстью она от этого сосёт!?"
        Max_07 "Вижу... Что ещё расскажешь?"
        Eric_01 "Вообще-то, тебе и этого более чем хватит на сегодня. Давай, иди гуляй..."
        menu:
            Max_00 "Хорошо. Уже ушёл..."
            "{i}уйти{/i}":
                jump .end

    label .end:
        $ renpy.end_replay()
        $ talk_var['eric.voy.stage']+=1
        $ spent_time += max((60 - int(tm[-2:])), 30)
        $ current_room = house[0]
        jump Waiting
