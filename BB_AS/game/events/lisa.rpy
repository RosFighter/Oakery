################################################################################
## события Лизы

label lisa_sleep_night:
    if all([flags.film_punish, not lisa.dcv.special.done, tm < '00:30']):
        call lisa_select_movie from _call_lisa_select_movie

    scene BG char Lisa bed-night
    $ AvailableActions['touch'].active = True
    $ renpy.show('Lisa sleep-night '+pose3_1+lisa.dress)
    return


label lisa_sleep_morning:
    scene BG char Lisa bed-morning
    $ renpy.show('Lisa sleep-morning '+pose3_1+lisa.dress)
    return


label lisa_shower:
    scene location house bathroom door-morning
    if lisa.daily.shower > 3:
        menu:
            Max_00 "Лиза сейчас принимает душ..."
            "{i}уйти{/i}":
                jump .end_peeping2
    elif lisa.daily.shower > 2:
        Max_14 "Лиза уже поймала меня на подглядывании. Грозилась рассказать маме. Не стоит злить её ещё больше."
        jump .end_peeping2
    elif lisa.daily.shower > 1:
        Max_09 "Сегодня я уже чуть не попался Лизе при подглядывании. Повезло, что успел вовремя сбежать. Не стоит рисковать ещё раз."
        jump .end_peeping2
    elif lisa.daily.shower > 0:
        Max_01 "Сегодня я уже подсматривал за Лизой. Повезло, что она меня не заметила. Не стоит рисковать ещё раз."
        jump .end_peeping2

    $ renpy.block_rollback()
    $ renpy.dynamic('r1')
    $ lisa.daily.shower = 4
    menu:
        Max_09 "Кажется, Лиза что-то делает в ванной..."
        "{i}постучаться{/i}":
            menu:
                Lisa "{b}Лиза:{/b} Кто там? Я ещё не закончила. Подождите немного..."
                "Это я, Макс!":
                    menu:
                        Lisa "{b}Лиза:{/b} Макс, чего хотел? Я же говорю, скоро выйду!"
                        "Можно я войду? Мне очень нужно...":
                            menu:
                                Lisa "{b}Лиза:{/b} Нет, Макс. Жди за дверью. Я скоро!"
                                "Ладно, ладно...":
                                    $ lisa.daily.shower = 4
                                    jump .end_peeping
                        "Хорошо, я подожду":
                            $ lisa.daily.shower = 4
                            jump .end_peeping
                "{i}уйти{/i}":
                    $ lisa.daily.shower = 4
                    jump .end_peeping
        "{i}заглянуть со двора{/i}":
            if lisa.sorry.owe:
                Max_10 "Хочется, конечно, ещё разок взглянуть на голую сестрёнку, но я ещё не отдал ей обещанное..."
                jump .end_peeping2
            jump .start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump .ladder
        "{i}уйти{/i}":
            $ lisa.daily.shower = 4
            jump .end_peeping

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        # назначим или определим одёжку
        if lisa.dress_inf != '04a':
            $ r1 = {'04c':'a', '04d':'b', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
        else:
            $ __list = ['a', 'b', 'c', 'd'] if 'bathrobe' in lisa.gifts else ['c', 'd']
            $ r1 = renpy.random.choice(__list)
            $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[r1]

        scene BG bathroom-morning-00
        $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        if r1 in ['a', 'b']:
            Max_03 "Класс! Лиза смотрится в подаренном мною халатике очень соблазнительно... Особенно когда так хорошо видно её упругие сисечки!"
        elif r1 == 'c':
            Max_07 "О, да! Моя обворожительная сестрёнка в одних трусиках... Так и хочется зайти и стянуть их с её прекрасной попки!"
        else:
            Max_06 "Ого! Утро может быть действительно очень добрым, если удаётся полюбоваться совершенно голенькой Лизой! Да... её тело завораживает..."

        Max_00 "Хоть и не хочется, но пока меня не заметили, лучше уходить..."
        jump .end_peeping

    label .start_peeping:
        $ lisa.daily.shower = 1
        $ Skill('hide', 0.03)
        $ r1 = renpy.random.randint(1, 4)

        $ _ch1 = GetChance(mgg.stealth, 3, 900)
        $ _ch2 = GetChance(mgg.stealth, 2, 900)
        $ renpy.scene()
        $ renpy.show('Lisa shower 0'+str(r1))
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Отлично! Моя младшая сестрёнка принимает душ... Даже видно кое-что... Много кое-чего! Только бы она меня не заметила..."
            "{i}продолжить смотреть\n{color=[_ch1.col]}(Скрытность. Шанс: [_ch1.vis]){/color}{/i}":
                jump .closer_peepeng
            "{i}взглянуть со стороны\n{color=[_ch2.col]}(Скрытность. Шанс: [_ch2.vis]){/color}{/i}":
                jump .alt_peepeng
            "{i}немного пошуметь{/i}" if 1 <= len(lisa.sorry.give) < 4 or (poss['SoC'].stn<0 and _ch1.ch>600):
                jump .pinded
            "{i}немного пошуметь{/i}" if len(lisa.sorry.give) == 4:
                jump .pinded
            "{i}уйти{/i}":
                jump .end_peeping

    label .alt_peepeng:
        if not RandomChance(_ch2.ch):
            jump .not_luck
        $ spent_time += 10
        $ lisa.daily.shower = 1
        $ Skill('hide', 0.2)
        $ lisa.dress_inf = '00a'
        $ r1 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Lisa shower-alt 0'+str(r1))
        show FG shower-water
        if 1 < r1 < 5:
            Max_02 "[undetect!t]Лиза вся такая мокренькая... класс! Фигурка и всё остальное у неё – что надо... Как же хочется потрогать!"
        else:
            Max_03 "[undetect!t]О, да! За тем, как вода стекает по её обворожительной попке, хочется смотреть не отрываясь..."
        jump .end_peeping

    label .closer_peepeng:
        $ spent_time += 10
        if RandomChance(_ch1.ch):
            $ lisa.daily.shower = 1
            $ Skill('hide', 0.2)
            $ lisa.dress_inf = '00a'
            $ r1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            $ renpy.show('Lisa shower-closer 0'+str(r1))
            show FG shower-closer
            if 1 < r1 < 5:
                Max_02 "[undetect!t]Лиза вся такая мокренькая... класс! Фигурка и всё остальное у неё – что надо... Как же хочется потрогать!"
            else:
                Max_03 "[undetect!t]О, да! За тем, как вода стекает по её обворожительной попке, хочется смотреть не отрываясь..."
            jump .end_peeping
        else:
            jump .not_luck

    label .not_luck:
        if RandomChance(_ch1.ch) or len(lisa.sorry.give) > 3:
            $ lisa.daily.shower = 2
            $ Skill('hide', 0.1)
            $ lisa.dress_inf = '00a'
            $ r1 = renpy.random.choice(['07', '08'])
            scene BG shower-closer
            $ renpy.show('Lisa shower-closer '+r1)
            show FG shower-closer
            Max_12 "{color=[orange]}{i}Кажется, Лиза что-то заподозрила!{/i}{/color}\nО нет! Похоже, она что-то заметила... Надо бежать!"
        else:
            jump .pinded
        jump .end_peeping

    label .pinded:
        if flags.film_punish:
            $ lisa.dcv.special.set_lost(1)
        else:
            $ lisa.daily.shower = 3
            $ punreason[0] = 1
        if lisa_was_topless():
            # после второго ТВ с Оливией
            $ r1 = renpy.random.choice(['07', '08'])
        else:
            $ Skill('hide', 0.05)
            $ r1 = renpy.random.choice(['09', '10'])
        scene BG shower-closer
        $ renpy.show('Lisa shower-closer '+r1)
        show FG shower-closer
        if lisa_was_topless():
            menu:
                Lisa_09 "[spotted!t]Ну, Макс! Опять ты подглядываешь... Если так неймётся ужастики смотреть со мной, то считай ты попал! А сейчас, кыш отсюда..."
                "{i}уйти{/i}":
                    jump .end_peeping
        else:
            menu:
                Lisa_12 "[spotted!t]Макс! Ты подглядываешь за мной? Как тебе не стыдно?! Я всё маме расскажу!"
                "{i}Бежать{/i}":
                    jump .end_peeping

    label .end_peeping2:
        $ current_room, prev_room = prev_room, current_room
        jump AfterWaiting
    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting
    return


label lisa_read:
    scene BG char Lisa reading
    $ renpy.show('Lisa reading '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa reading '+pose3_1+lisa.dress+'b'
    return


label lisa_read_closer:
    scene BG char Lisa reading
    $ renpy.show('Lisa reading-closer 01'+lisa.dress)
    return


label lisa_dressed_school:
    scene location house myroom door-morning

    $ renpy.dynamic('r1', 'mood', 'rel', 'suf')
    $ mood = 0
    $ rel = 0
    if lisa.hourly.dressed == 0:
        $ lisa.hourly.dressed = 1
        jump .lisa_dressed
    else:
        return

    menu .lisa_dressed:
        Max_09 "{i}( Похоже, Лиза собирается в школу... ){/i}"
        "{i}постучаться{/i}":
            menu:
                "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
                "Это я, Макс. Можно войти?":
                    jump .come_in
                "Можно войти на секунду? Я только ноутбук возьму..." if flags.warning:
                    jump get_laptop
                "Хорошо, я подожду...":
                    $ spent_time = 10
                    jump .rel_mood

        "{i}открыть дверь{/i}":
            if lisa_was_topless():
                jump .open_door2
            else:
                jump .open_door
        "{i}заглянуть в окно{/i}":
            jump .look_window
        "{i}уйти{/i}":
            $ spent_time = 10
            jump .rel_mood

    label .look_window:
        $ spent_time = 10
        $ r1 = renpy.random.choice(['01', '02', '03', '04'])
        $ lisa.dress_inf = {'01':'02h', '02':'02e', '03':'02b', '04':'02c'}[r1]

        if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
            scene BG char Lisa voyeur-01
            $ renpy.show('Lisa voyeur alt-'+r1)
            $ renpy.show('FG voyeur-lisa-01'+mgg.dress)
        else:
            scene BG char Lisa voyeur-00
            $ renpy.show('Lisa voyeur '+r1)
            $ renpy.show('FG voyeur-lisa-00'+mgg.dress)

        $ Skill('hide', 0.03)
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "{i}уйти{/i}":
                jump .end

    label .come_in:
        scene BG char Lisa morning

        $ spent_time = 60 - int(tm.split(":")[1])
        if not lisa_was_topless():
            $ lisa.dress_inf = '01b'
            $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
            $ renpy.show('Lisa school-dressed 01'+suf)
            menu:
                Lisa_00 "Макс, ну чего ломишься? Ты же знаешь, что мне в школу пора...\n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "Это и моя комната!":
                    if lisa.GetMood()[0] < 0: # настроение не очень и ниже
                        show Lisa school-dressed 01
                        Lisa_12 "Так и знала, что тебя надо было на диванчики в гостиную отправлять... Ладно, я уже оделась, входи уж... А я в школу побежала."
                        Max_00 "Удачи"
                        $ rel  -= 5 # при плохом настроении отношения и настроение снижаются
                        $ mood -= 25
                    else: # нейтральное настроение
                        Lisa_02 "В любом случае, я уже оделась, так что, входи. А я побежала в школу."
                        Max_00 "Удачи"
                "Да чего я там не видел...":
                    if GetRelMax('lisa')[0] < 1: # отношения прохладные и ниже
                        Lisa_12 "Что бы ты там не видел, но подождать немного за дверью можно было? Так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                        Max_00 "Пока, Лиза!"
                        $ rel  -= 5 # при низком отношении отношения и настроение снижаются
                        $ mood -= 25
                    elif GetRelMax('lisa')[0] < 2: # Неплохие отношения
                        Lisa_01 "А за дверью постоять не мог? А ладно, входи... Я уже оделась и побежала в школу."
                        Max_00 "Пока, Лиза!"
                    else: # хорошие и выше отношения
                        Lisa_02 "Но за дверью подождать немного ты всё равно мог! Хотя бы для приличия..."
                        show Lisa school-dressed 01a
                        Lisa_01 "Как бы там ни было, проходи... Я уже оделась и побежала в школу. Вернусь часа в четыре."
                        Max_00 "Пока, Лиза!"
                        $ mood += 25 # при хорошем отношении настроение повышается
                "Извини":
                    if GetRelMax('lisa')[0] < 2: # Неплохие отношения
                        Lisa_03 "Да ты у нас джентльмен! В общем, я тут закончила и побежала в школу. Пока!"
                    else:
                        Lisa_03 "Да ты у нас, оказывается, джентльмен!"
                        show Lisa school-dressed 01a
                        Lisa_01 "В общем, я тут закончила и побежала в школу. Пока!"
                    Max_00 "Пока, Лиза!"
                    $ mood += 25 # при извинении настроение повышается
        else:
            $ r1 = '0'+str(renpy.random.randint(3, 4))
            $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
            $ renpy.show('Lisa school-dressed '+r1+suf)
            menu:
                Lisa_09 "Макс, я в школу одеваюсь! И ты прекрасно это знал..."
                "Могла бы и не прикрываться...":
                    #спрайт в блузке и трусиках
                    show Lisa school-dressed 01b
                    if GetRelMax('lisa')[0] < 0:
                        # настроение не очень и ниже отношения и настроение снижаются
                        $ rel  -= 5
                        $ mood -= 25
                        Lisa_12 "А ты бы мог и за дверью подождать немного! Хотя бы для приличия..."
                        #одетая
                        show Lisa school-dressed 01
                        Lisa_00 "Ладно, я уже оделась, входи уж... А я в школу побежала."
                        Max_01 "Удачи!"
                    else:
                        # настроение нейтральное и выше
                        Lisa_02 "Могла бы... Но не буду, пока тут такие любознательные личности, как ты, лазят!"
                        #одетая
                        show Lisa school-dressed 01a
                        Lisa_01 "Ладно, я уже оделась, входи уж... А я в школу побежала."
                        Max_01 "Удачи!"
                "У тебя классная грудь, не стесняйся..." if r1==3:   # Лиза без верха
                    #спрайт в блузке и трусиках
                    show Lisa school-dressed 01b
                    if GetRelMax('lisa')[0] < 1:
                        # отношения прохладные и ниже отношения и настроение снижаются
                        $ rel  -= 5
                        $ mood -= 25
                        Lisa_12 "И что теперь, тебе можно на неё глазеть, когда захочешь?! Нет уж, не угадал!"
                        #одетая
                        show Lisa school-dressed 01
                        Lisa_00 "Так или иначе, я уже оделась и побежала в школу."
                        Max_01 "Удачи!"
                    elif GetRelMax('lisa')[0] < 2:
                        # неплохие отношения
                        Lisa_00 "Ага, красивая... Но это не значит, что из-за этого я должна её тебе показывать!"
                        #одетая
                        show Lisa school-dressed 01
                        Lisa_01 "Ладно, я уже оделась, входи уж... А я в школу побежала."
                        Max_01 "Удачи!"
                    else:
                        # при хорошем (и выше) отношении настроение повышается
                        $ mood += 25
                        Lisa_02 "Спасибо! Но ты и так слишком часто её видишь... Хорошего должно быть понемножку!"
                        Max_03 "Не так часто, как хотелось бы."
                        #одетая
                        show Lisa school-dressed 01a
                        Lisa_01 "Ладно, я уже оделась, входи уж... А я в школу побежала."
                        Max_01 "Удачи!"
                "Подумаешь, твою очаровательную попку без трусиков увижу..." if r1==4:   # Лиза без низа
                    #спрайт в маечке и трусиках
                    $ renpy.show('Lisa school-dressed 02'+suf)
                    if GetRelMax('lisa')[0] < 1:
                        # отношения прохладные и ниже отношения и настроение снижаются
                        $ rel  -= 5
                        $ mood -= 25
                        Lisa_12 "Мог бы и за дверью подождать немного! Хотя бы для приличия..."
                        #спрайт в юбке
                        show Lisa school-dressed 01c
                        Lisa_09 "Прекращай пялиться! Припёрся ни раньше и ни позже..."
                        #одетая
                        show Lisa school-dressed 01
                        Lisa_00 "Можешь входить... А я в школу побежала."
                        Max_01 "Удачи!"
                    elif GetRelMax('lisa')[0] < 2:
                        # неплохие отношения
                        Lisa_00 "Так, на мою попку сильно не глазеть! Я тут переодеваюсь не для того, чтобы тебя порадовать."
                        #спрайт в юбке
                        show Lisa school-dressed 01c
                        Lisa_09 "Отвернись, Макс! Я чувствую, как ты пялишься на меня..."
                        #одетая
                        show Lisa school-dressed 01
                        Lisa_01 "Можешь входить... А я в школу побежала."
                        Max_01 "Удачи!"
                    else:
                        #при хорошем (и выше) отношении настроение повышается
                        $ mood += 25
                        Lisa_02 "А вот и не увидишь! Когда надо, я могу их так быстренько одеть, как тебе и не снилось!"
                        Max_03 "Это правда! В моих снах ты делаешь это очень медленно..."
                        #спрайт в юбке
                        show Lisa school-dressed 01c
                        Lisa_05 "Так же медленно, как и эту юбку?"
                        Max_05 "О да! Примерно так же..."
                        #одетая
                        show Lisa school-dressed 01a
                        Lisa_01 "Так, представим, что я ничего не слышала! Можешь входить... А я в школу побежала."
                        Max_01 "Удачи!"

        jump .rel_mood

    label .open_door2:
        # Лиза уже снимала майку во время ТВ
        $ spent_time = 20
        $ r1 = renpy.random.randint(3, 5)
        $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
        $ lisa.dress_inf = {2:'02a', 3:'02c', 4:'02b', 5:'00'}[r1]
        scene BG char Lisa morning
        $ renpy.show('Lisa school-dressed 0'+str(r1)+suf)

        if r1 < 5:
            # Лиза без верха или без низа
            menu:
                Lisa_12 "Макс! Ты почему без стука входишь? Я не одета..."
                "У тебя классная грудь, не стесняйся..." if r1==3:
                    if GetRelMax('lisa')[0] < 1:
                        # отношения прохладные и ниже отношения и настроение снижаются
                        $ rel  -= 5
                        $ mood -= 25
                        Lisa_12 "И что теперь, тебе можно на неё глазеть, когда захочешь?! Нет уж, не угадал! Выйди быстро, пока маму не позвала!" nointeract
                    elif GetRelMax('lisa')[0] < 2:
                        # неплохие отношения
                        Lisa_00 "Ага, красивая... Но это не значит, что из-за этого я должна её тебе показывать! Выйди, пожалуйста..." nointeract
                    else:
                        # при хорошем (и выше) отношении настроение повышается
                        $ mood += 25
                        Lisa_02 "Спасибо! Но ты и так слишком часто её видишь... Хорошего должно быть понемножку! А теперь выйди, дай переодеться..." nointeract
                "Подумаешь, твою очаровательную попку без трусиков увижу..." if r1==4:
                    if GetRelMax('lisa')[0] < 1:
                        # отношения прохладные и ниже отношения и настроение снижаются
                        $ rel  -= 5
                        $ mood -= 25
                        Lisa_12 "Так, быстро выйди и жди за дверью! Хотя бы для приличия... Или мне маму позвать?" nointeract
                    elif GetRelMax('lisa')[0] < 2:
                        # неплохие отношения
                        Lisa_00 "Так, на мою попку сильно не глазеть! Будь добр, выйди и дверь закрой..." nointeract
                    else:
                        # при хорошем (и выше) отношении настроение повышается
                        $ mood += 25
                        Lisa_02 "А вот и не увидишь! Дай переодеться спокойно, нечего тут всяким любопытным личностям лазить..." nointeract
        else:
            # Лиза голая
            menu:
                Lisa_12 "Макс! Я не одета! Быстрой закрой дверь с той стороны!"
                "Извини, я думал, что ты уже оделась. Хотя бы немного...":
                    pass
            if GetRelMax('lisa')[0] < 1:
                # отношения прохладные и ниже отношения и настроение снижаются
                $ rel  -= 5
                $ mood -= 25
                Lisa_12 "И что теперь, можно заходить когда вздумается и без стука?! Нет уж, не угадал! Выйди быстро, пока маму не позвала!" nointeract
            elif GetRelMax('lisa')[0] < 2:
                # неплохие отношения
                Lisa_00 "Не оделась... Но это не значит, что ты можешь вот просто так заходить без стука! Выйди, пожалуйста..." nointeract
            else:
                # при хорошем (и выше) отношении настроение повышается
                $ mood += 25
                Lisa_02 "Ещё нет! Считай, тебе повезло, но дай мне пожалуйста переодеться..."
        menu:
            "{i}уйти{/i}":
                scene location house myroom door-morning
                jump .rel_mood

    label .open_door:
        # Лиза ещё не снимала майку во время ТВ
        $ spent_time = 20
        $ r1 = renpy.random.randint(2, 5)
        $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
        $ lisa.dress_inf = {2:'02a', 3:'02c', 4:'02b', 5:'00'}[r1]
        scene BG char Lisa morning
        $ renpy.show('Lisa school-dressed 0'+str(r1)+suf)

        $ mood -= 50 # настроение портится в любом случае
        if r1 < 3: # Лиза практически одета
            menu:
                Lisa_12 "Макс! Стучаться надо! А вдруг я была бы голая?! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "Ну, тогда мне бы повезло":
                    $ rel -= 5
                    Lisa_13 "Ну ты хам! Быстро закрой дверь с той стороны!"
                    Max_00 "Хорошо..."
                "Извини, я забыл...":
                    Lisa_01 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
                    Max_00 "Хорошо..."
                    $ mood += 50
        elif r1 < 5: # Лиза частично одета
            menu:
                Lisa_12 "Макс! Не видишь, я собираюсь в школу! Быстро закрой дверь! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "Извини... Кстати, отличный зад!" if __ran1 < 3:
                    if GetRelMax('lisa')[0] < 2:
                        $ rel -= 5
                "Извини..." if __ran1 > 2:
                    $ mood += 50
        else: # Лиза полностью голая
            menu:
                Lisa_12 "Макс! Я не одета! Быстрой закрой дверь с той стороны! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "А у тебя сиськи подросли!":
                    $ rel -= 5
                    menu:
                        Lisa_11 "Что?! Я всё маме расскажу!"
                        "Всё, всё, ухожу!":
                            pass
                        "Уже ухожу, но сиськи - супер!":
                            $ rel -= 5
                            menu:
                                Lisa_12 "..."
                                "{i}Бежать{/i}":
                                    pass
                "Извини, я не хотел...":
                    Lisa_12 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
                    Max_00 "Хорошо..."
                    if GetRelMax('lisa')[0] > 1:
                        $ mood += 50

        scene location house myroom door-morning

    label .rel_mood:
        $ AddRelMood('lisa', rel, mood)

    label .end:
        jump Waiting


label lisa_dressed_shop:
    scene location house myroom door-morning

    if lisa.hourly.dressed != 0:
        return

    $ __mood = 0
    $ __rel = 0
    $ __warned = False
    $ lisa.hourly.dressed = 1
    $ spent_time = 10 #60 - int(tm[-2:])
    menu .lisa_dressed:
        Max_09 "Кажется, все собираются на шоппинг и Лиза сейчас переодевается..."
        "{i}постучаться{/i}":
            jump .knock
        "{i}открыть дверь{/i}":
            jump .open_door
        "{i}заглянуть в окно{/i}":
            jump .look_window
        "{i}уйти{/i}":
            $ spent_time = 10
            jump .rel_mood

    menu .knock:
        Lisa "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
        "Это я, Макс. Можно войти?":
            menu:
                Lisa "{b}Лиза:{/b} Нет, Макс, нельзя! Я переодеваюсь. Жди там."
                "{i}открыть дверь{/i}":
                    $ __warned = True
                    jump .open_door
                "Хорошо...":
                    jump .rel_mood
        "Можно войти на секунду? Я только ноутбук возьму..." if flags.warning:
            jump get_laptop
        "Хорошо, я подожду...":
            jump .rel_mood

    label .open_door:
        $ spent_time = 20
        $ __ran1 = renpy.random.randint(3, 5)
        $ lisa.dress_inf = {3:'02c',4:'02b',5:'00'}[__ran1]
        scene BG char Lisa morning
        if GetRelMax('lisa')[0] < 0:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1))
        elif GetRelMax('lisa')[0] < 2:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1)+'a')
        elif lisa.free < 200:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1)+'b')
        else:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1)+'c') # пока отсутствует

        if __warned:
            $ __mood -= 150
            $ __rel -= 15
            $ phrase = _("Я же сказала, что я не одета! ")
        else:
            $ __mood -= 50 # настроение портится в любом случае
            $ phrase = _("Я не одета! ")

        menu:
            Lisa_12 "Макс! [phrase!t]Быстрой закрой дверь с той стороны!"
            "Извини... Кстати, отличный зад!" if __ran1 == 2:
                if GetRelMax('lisa')[0] < 2:
                    $ __rel -= 5
            "А у тебя сиськи подросли!":
                menu:
                    Lisa_11 "Что?! Я всё маме расскажу!"
                    "Всё, всё, ухожу!":
                        jump .rel_mood
                    "Уже ухожу, но сиськи - супер!":
                        $ __mood -= 50
                        $ __rel -= 5
                        menu:
                            Lisa_12 "..."
                            "{i}Бежать{/i}":
                                jump .rel_mood
            "Извини, я не хотел...":
                $ __mood += 50
                $ __rel += 5
                jump .rel_mood

    label .look_window:
        $ spent_time = 10
        $ __ran1 = renpy.random.choice(['03', '04', '05', '06'])
        $ lisa.dress_inf ={'03':'02b', '04':'02c', '05':'02i', '06':'02g'}[__ran1]
        scene BG char Lisa voyeur-00
        $ renpy.show('Lisa voyeur '+__ran1)
        $ renpy.show('FG voyeur-lisa-00'+mgg.dress)
        $ Skill('hide', 0.03)
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "{i}уйти{/i}":
                jump .rel_mood

    scene location house myroom door-morning

    label .rel_mood:
        $ AddRelMood('lisa', __rel, __mood)

    jump Waiting


label get_laptop:
    scene BG char Lisa morning
    show Lisa school-dressed 02b
    Lisa_00 "Мог бы и подождать немного. Ты что, без ноутбука и часа прожить не можешь?"
    Max_00 "Лиза, мне ноутбук нужен для дела."
    Lisa_00 "Какого дела? Ты дома сидишь целыми днями и ничего не делаешь..."
    Lisa_00 "Ладно, неважно... Забирай свой ноутбук и уходи. Дай мне уже переодеться..."
    $ spent_time += 10
    $ at_comp = True
    $ current_room = house[5]
    $ cam_flag.append('notebook_on_terrace')
    jump Laptop


label lisa_dressed_repetitor:
    scene location house myroom door-morning

    if lisa.hourly.dressed != 0:
        return

    # добавить возможность подглядываать после начала секс.обучения Лизы у АиЭ
    menu:
        Max_09 "Кажется, Лиза куда-то собирается, но дверь закрыта..."
        "{i}уйти{/i}":
            $ lisa.hourly.dressed = 1

    label .end:
        jump Waiting


label lisa_swim:
    scene image 'Lisa swim '+pose3_1+lisa.dress
    $ persone_button1 = 'Lisa swim '+pose3_1+lisa.dress+'b'
    return


label lisa_sun:
    scene image 'BG char Lisa sun-'+pose3_1
    $ renpy.show('Lisa sun '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa sun '+pose3_1+lisa.dress+'b'
    return


label lisa_dishes:
    scene BG crockery-evening-00
    $ renpy.show('Lisa crockery-evening 01'+lisa.dress)
    $ persone_button1 = 'Lisa crockery-evening 01'+lisa.dress+'b'
    return


label lisa_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show('Lisa crockery-closer '+pose3_1+lisa.dress)
    return


label lisa_phone:
    scene BG char Lisa bed-evening
    $ renpy.show('Lisa phone-evening '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa phone-evening '+pose3_1+lisa.dress+'b'
    return


label lisa_phone_closer:
    scene BG char Lisa bed-evening
    $ renpy.show('Lisa phone-closer 01'+lisa.dress)
    return


label lisa_bath:
    scene location house bathroom door-evening
    if lisa.daily.bath != 0:
        return

    $ lisa.daily.bath = 1
    $ __mood = 0
    $ __rel = 0
    menu:
        Max_00 "В это время Лиза обычно плескается в ванне..."
        "{i}постучаться{/i}":
            jump .knock
        "{i}открыть дверь{/i}":
            jump .open
        "{i}заглянуть со двора{/i}" if flags.ladder < 2:
            scene Lisa bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "Кажется, Лиза и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но ближе подойти опасно - может заметить..."
            Max_09 "Нужно что-нибудь придумать..."
            $ flags.ladder = 1
            jump .end
        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
            $ flags.ladder = 3
            $ items['ladder'].give()
            # $ items['ladder'].have = False
            # $ items['ladder'].InShop = False
            jump .ladder
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump .ladder
        "{i}уйти{/i}":
            jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-evening 02'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ spent_time += 10

        $ __r1 = renpy.random.randint(1, 4)

        scene BG bath-00
        $ renpy.show('Lisa bath-window 0'+str(__r1))
        show FG bath-00
        $ Skill('hide', 0.03)
        if __r1 == 1:
            menu:
                Max_03 "Кажется, Лиза как раз собирается принять ванну... О да, моя младшая сестрёнка хороша... а голенькая, так особенно!"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Lisa bath-window '+renpy.random.choice(['02', '03', '04']))
                    $ Skill('hide', 0.03)
                    menu:
                        Max_05 "Ох, вот это повезло! Лиза демонстрирует свои прелестные сисечки словно специально! Разумеется, она не знает, что я смотрю, а то крику бы было..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ lisa.dress_inf = '00a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end
        else:
            menu:
                Max_05 "Ох, вот это повезло! Лиза демонстрирует свои прелестные сисечки словно специально! Разумеется, она не знает, что я смотрю, а то крику бы было..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Lisa bath-window 05
                    $ Skill('hide', 0.03)
                    menu:
                        Max_07 "Эх! Вот и закончились водные процедуры... Ухх... И с этой обворожительной киской я живу в одной комнате! Красота..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ lisa.dress_inf = '04a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end

    menu .knock:
        Lisa "{b}Лиза:{/b} Кто там? Я принимаю ванну..."
        "Это я, Макс! Можно войти?":
            menu:
                Lisa "{b}Лиза:{/b} Я же сказала, что в ванне. Закончу, тогда и войдёшь! А пока жди..."
                "Хорошо, я подожду...":
                    jump .end
                "{i}открыть дверь{/i}":
                    jump .open_knock
                "{i}уйти{/i}":
                    jump .end
        "{i}открыть дверь{/i}":
            jump .open_knock
        "{i}уйти{/i}":
            jump .end

    label .open_knock:
        if poss['seduction'].stn < 31:
            $ __mood -= 50
            scene BG bath-open-00
            if GetRelMax('lisa')[0] < 0:
                show Lisa bath-open 01
                Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
            elif GetRelMax('lisa')[0] < 2:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 02
                Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
            else:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 03
                Lisa_11 "Макс! Я же предупредила, что моюсь! Хочешь со мной поссориться?"
            Max_00 "Упс! Уже ушёл..."

            jump .end
        else:
            Max_00 "В следующих версиях..."
            jump .end

    label .open:
        if poss['seduction'].stn < 31:
            scene BG bath-open-00
            if GetRelMax('lisa')[0] < 0:
                show Lisa bath-open 01
            elif GetRelMax('lisa')[0] < 2:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 02
            else:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 03
            menu:
                Lisa_11 "Макс! А постучаться? Я же голая!"
                "Извини, дверь была открыта и я подумал...":
                    pass
                "А ты симпатичная...":
                    pass
                "И что такого? Сестра стесняется брата?":
                    pass
            Lisa_12 "Макс, выйди немедленно!"
            Max_00 "Хорошо, уже ухожу..."
        else:
            Max_00 "В следующих версиях..."

    label .end:
        $ AddRelMood('lisa', __rel, __mood)
        $ spent_time = 10
        jump Waiting


label lisa_homework:
    scene BG char Lisa lessons
    $ renpy.show('Lisa lessons '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa lessons '+pose3_1+lisa.dress+'b'
    return


label lisa_select_movie:
    if lisa.dcv.special.stage < 1:
        # первый просмотр романтического фильма
        jump lisa_romantic_movie_0

    elif lisa.dcv.special.stage < 4:
        # периодический просмотр романтического фильма
        jump lisa_romantic_movie_r

    elif lisa.dcv.special.stage < 5:
        # первый просмотр ужастика
        jump lisa_horor_movie_0

    elif lisa.dcv.special.stage < 8:
        # периодический просмотр ужастика
        jump lisa_horor_movie_r


label lisa_romantic_movie_0:

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    Max_01 "Да, смотрим. Сейчас всё подготовлю..."
    Lisa_02 "А я пока свет выключу."

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    $ renpy.show("Lisa horror-myroom 00-01"+lisa.dress)
    Max_04 "Давай, запрыгивай! Ты уже знаешь, что будем смотреть?"
    Lisa_09 "В смысле, \"запрыгивай\"? К тебе на кровать, что ли?"
    Max_07 "Да, ко мне. Или к тебе, если хочешь."
    Lisa_10 "Я думала каждый со своей кровати будет смотреть!"
    Max_09 "Здесь же у нас не такой экран, как в гостиной. Смотреть надо близко."
    Lisa_00 "Ну... ладно. Подвинься тогда."

    scene BG char Lisa horror-myroom 01
    $ renpy.show("Lisa horror-myroom 01-01"+lisa.dress)
    Max_00 "Ну так... каким фильмом ты собиралась меня мучить?"
    Lisa_01 "Точно не знаю. Напиши в поиске \"лучшие романтические фильмы\" и я что-нибудь выберу."
    Max_03 "Вот, смотри... Выбирай... Может вот этот? Постер уж очень интересный!"
    Lisa_02 "Нет, мы будем смотреть то, что интересно мне! Хочу вон тот фильм! Давай, включай..."
    play music romantic
    Max_07 "{i}( Да уж, это конечно намного лучше, чем получать при всех от мамы по заднице, но так скучно! Хотя бы с сестрёнкой рядом на одной кровати полежу. А смотреть можно и вполглаза... ){/i}"
    Lisa_13"Макс, не спи! Ты должен смотреть - это твоё наказание! Если будешь спать, то я буду тебя пихать..."

    scene BG char Lisa horror-myroom 01a
    $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)
    Max_02 "{i}( Я бы тоже с огромным удовольствием попихал в тебя чем-нибудь! А если бы она ещё и уснула со мной в обнимку это было бы... ){/i}"
    Lisa_10 "Ой-ёй-ёй! У фильма же вроде семейный рейтинг?! Почему они раздеваются?"
    Max_03 "А вот это уже будет поинтереснее смотреть! Хороший момент, мне нравится..."
    Lisa_11 "Давай промотаем! Мне как-то неудобно... Ого! А что это он там делает ей?!"
    Max_05 "Я не против, что персонажей в этой сцене решили... хорошенько раскрыть..."
    Lisa_12 "Чем это ты ноутбук шевелишь? У тебя рука что ли трясётся или..."
    Max_07 "Ну... почти."

    scene BG char Lisa horror-myroom 04
    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
    Lisa_11 "Макс! У тебя встал что ли?"
    Max_08 "Да, немного. Такой уж фильм ты выбрала!"
    Lisa_13 "Немного?! Это не немного! Какой же ты озабоченный!"
    Max_09 "Вообще-то, так все мужчины реагируют на такое!"
    Lisa_12 "Молодец, Макс! Испортил весь просмотр."
    Max_07 "А ты на экран смотри, а не на член."
    Lisa_10 "Да не могу я смотреть на экран, когда и там и у тебя такое... Всё, я спать!"
    stop music fadeout 1.0
    Max_08 "Погоди, но это ведь считается, что я отбыл наказание?"
    Lisa_09 "Да ну тебя!"
    Max_01 "Ладно. Доброй ночи тогда."

    $ lisa.dcv.special.stage = 1
    $ lisa.dcv.special.disable()
    $ poss['SoC'].open(10)
    $ infl[lisa].add_m(12)
    $ spent_time += 60
    $ flags.cur_series = 1
    jump Waiting


label lisa_romantic_movie_r:

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    Max_01 "Да, смотрим. Сейчас всё подготовлю..."
    Lisa_02 "А я пока свет выключу."

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    $ renpy.show("Lisa horror-myroom 00-01"+lisa.dress)
    if flags.cur_series < 2:
        Max_04 "Давай, запрыгивай! Будем досматривать тот фильм?"   #если не досмотрели фильм
        Lisa_09 "Да, но промотай тот момент, ну ты понял..."
        play music romantic
        Max_03 "Считай, что уже сделано. Я к отбытию наказания готов!"
        Lisa_02 "И смотри чтобы ничего у тебя там не шевелилось больше!"
    else:
        Max_04 "Давай, запрыгивай! Ты уже знаешь, что будем смотреть?"   #если досмотрели фильм
        Lisa_01 "Нет. Выводи список романтический фильмов и я выберу. Только давай нормальные фильмы, а не как в прошлый раз!"
        play music romantic
        Max_03 "Ты сама выбирала, моё дело маленькое. Вот этот вроде ничего должен быть..."
        Lisa_02 "Ага, давай его. И твоё маленькое дело - это смотреть фильм, мучиться и чтобы у тебя ничего не шевелилось!"

    if renpy.random.randint(1, 2) < 2:
        scene BG char Lisa horror-myroom 01
        $ renpy.show("Lisa horror-myroom 01-01"+lisa.dress)
    else:
        scene BG char Lisa horror-myroom 01a
        $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)

    Max_07 "{i}( Легко говорить, чтобы ничего не шевелилось! Достаточно просто представить, как Лиза лежит рядом со мной, совсем обнажённая... Ой, лучше не думать! ){/i}"
    Lisa_03 "Что, Макс, заскучал? Будешь знать, как за мной подглядывать! И не вздумай спать, а то я начну тебя щипать..."
    Max_02 "Так я и ответить могу тем же, если ты не в курсе!"
    Lisa_13 "Эй! Нет, меня нельзя щипать! Ой, ну вот опять откровенные сцены начались..."
    Max_04 "{i}( Вовремя! А то у меня уже слегка привстал, ведь в голову пришло уже столько пошлых мыслей от того, что Лиза лежит так близко ко мне. ){/i}"

    scene BG char Lisa horror-myroom 04
    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)

    if poss['seduction'].stn>7 and lisa.dcv.special.stage == 3:
        #как только открываются уроки поцелуев с Лизой и посмотрели 3 раза романтику
        Lisa_10 "Макс, у тебя опять стоит! Ну сколько можно?"
        Max_01 "Фильмы такие! Что тут поделать..."
        Lisa_01 "А я знаю что! Мы будем смотреть что-нибудь такое, на что ты не будешь реагировать так, как сейчас."
        Max_05 "Например? О, давай боевики?! Или комедии? А ещё лучше - комедийные боевики!"
        Lisa_02 "Нет, мы будем смотреть ужастики!"
        Max_09 "Ужастики?! Ты уверена, что смотреть ужастики в тёмное время суток - это то, что нужно?"
        Lisa_03 "Что, Макс, струсил?! Это то, что мне и нужно. Наверняка, ты будешь визжать от страха, как маленькая девочка!"
        Max_16 "Не дождёшься! Считай, что вызов я принял! Ещё увидим, кто будет визжать..."
        Lisa_02 "Да, да... Не удивлюсь, если подглядывания за мной... прекратятся."
        Max_09 "У тебя, кстати, есть своя кровать, помнишь?"
        Lisa_01 "Тогда я пойду спать, а то ты сегодня что-то не в духе."
        stop music fadeout 1.0
        Max_15 "Да, будь так добра..."
        $ poss['SoC'].open(11)
        $ lisa.dcv.special.stage = 4

    elif flags.cur_series > 1:
        # чередующийся вариант окончания просмотра
        Lisa_12 "Ну и ты следом сразу возбудился! Это вообще нормально?"
        Max_07 "Спроси хоть у кого и ответ будет всегда один - да, это нормальная реакция."
        Lisa_10 "Ну и как теперь дальше фильм смотреть, а Макс?"
        Max_02 "Как и до этого смотрела, просто с небольшим бонусом."
        Lisa_09 "Ага! Очень такой \"небольшой\" бонус, аж в трусах не умещается... Всё, я спать!"
        Max_07 "Ничего, если я тут досмотрю этот момент, интересно, как закончится?"
        Lisa_12 "Нет! Выключай всё! А то это уже не наказание получается."
        stop music fadeout 1.0
        Max_01 "Ладно. Тогда спим..."
    else:
        # чередующийся вариант окончания просмотра
        Lisa_10 "Макс, может уже хватит меня смущать?! Почему ты такой озабоченный?"
        Max_02 "Не понимаю о чём ты говоришь, у меня всё нормально."
        Lisa_13 "Ага, развалился тут со своим членом на всю кровать и довольный! А это вообще-то наказание!"
        Max_07 "Ну а что я сделаю, если они там решили поразвлечься?!"
        Lisa_09 "Опять ты весь просмотр испортил! Я пошла спать..."
        Max_04 "Ну давай, а я ещё немного посмотрю..."
        Lisa_10 "Нет уж! Давай выключай! А то лицо у тебя слишком довольное стало."
        Max_03 "И не только лицо..."
        Lisa_09 "Да ну тебя!"
        stop music fadeout 1.0
        Max_01 "Ладно. Доброй ночи тогда."

    if lisa.dcv.special.stage < 3:
        $ lisa.dcv.special.stage += 1

    $ lisa.dcv.special.disable()
    $ infl[lisa].add_m(12)
    $ spent_time += 60
    $ flags.cur_series = {1:2, 2:1}[flags.cur_series]
    jump Waiting


label lisa_horor_movie_0:

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    Max_01 "Да, смотрим. Сейчас всё подготовлю..."
    Lisa_02 "А я пока свет выключу. Тебе уже страшно?"

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    show Lisa horror-myroom 00-01b
    Max_07 "Как бы не так! Ты уже знаешь, что будем смотреть?"
    menu:
        Lisa_03 "Я думала посмотреть все части \"Кошмара на улице Вязов\" или \"Пятницы 13-е\". Мне в школе посоветовали. Но выбирать тебе, ты же будешь бояться."
        "{i}смотреть \"Кошмар на улице Вязов\"{/i}":   #после выбора начинает играть соответствующая фильму музыка
            $ flags.cur_movies = ['hes', 1, 0, 0]
            play music hes
        "{i}смотреть \"Пятница 13-е\"{/i}":   #после выбора начинает играть соответствующая фильму музыка
            $ flags.cur_movies = ['f13', 0, 1, 0]
            play music f13
        "{i}смотреть \"Крик\"{/i}":
            $ flags.cur_movies = ['scr', 0, 0, 1]
            play music scream

    scene BG char Lisa horror-myroom 01
    show Lisa horror-myroom 01-01b
    Lisa_02 "Макс, если тебе будет сильно страшно, то так и скажи! В этом нет ничего такого, мы сразу всё выключим."
    Max_03 "Мне нечего бояться, с моей стороны стена, так что никто из под кровати на меня не нападёт. Чего не могу сказать о твоём положении, ты сильно рискуешь!"

    scene BG char Lisa horror-myroom 01a
    show Lisa horror-myroom 01a-01b
    Lisa_00 "Хорошая попытка, но меня этим не напугаешь, наверно... Вот молчал бы и я об этом сейчас не думала бы!"
    Max_02 "Но если тебе всё же начнёт казаться, как что-то тянется из темноты к твоей ноге, то сразу скажи. И мы сразу всё выключим!"

    scene BG char Lisa horror-myroom 03
    show Lisa horror-myroom 03-01b
    Lisa_09 "Не пугай меня, Макс! И так фильм страшный, так ты тут ещё жути нагоняешь!"
    Max_00 "Не бойся, мне тоже страшно!"
    Lisa_10 "Правда? По тебе не скажешь..."
    Max_04 "Есть немного, но трусишка у нас ты... Но мне это нравится, очень мило."

    scene BG char Lisa horror-myroom 02
    show Lisa horror-myroom 02-01b
    $ renpy.show("FG horror-myroom "+flags.cur_movies[0]+" 01-01")
    Lisa_11 "Ой-ёй-ёй... Зря мы это смотрим! Кажется, я теперь от таких ужасов не смогу заснуть..."
    Max_09 "Ну, ты не одна в комнате, так что бояться нечего. Всех монстров я возьму на себя!"
    Lisa_13 "Макс, это что мне в ногу такое твёрдое упёрлось?!"
    Max_07 "Ноутбук, должно быть."

    scene BG char Lisa horror-myroom 04
    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
    Lisa_12 "Ага, ноутбук, как же! Сейчас-то у тебя от чего встал?!"
    Max_08 "Ты ко мне прижалась, вот я и возбудился. Пора бы тебе уже спокойно на это реагировать и не обращать внимание."
    Lisa_09 "Да как тут внимание не обращать, ты же меня своим членом сейчас трогал?!"
    Max_09 "Во-первых, не трогал, а ты просто положила на него свою ногу, а во-вторых, ты же к моей ноге своей киской тоже прижалась... Так что всё честно!"

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    show Lisa horror-myroom 00-02b
    Lisa_10 "Ничем таким я к тебе не прижималась! И вообще, я спать пошла... только страшно..."
    stop music fadeout 1.0
    Max_01 "Ладно. И попку давай береги по пути, а то монстры любят хватать за что-нибудь такое!"
    Lisa_11 "Ой ой ой!"

    $ spent_time += 60
    $ lisa.dcv.special.stage = 5
    $ lisa.dcv.special.disable()
    $ poss['SoC'].open(12)
    $ infl[lisa].add_m(12)
    $ flags.cur_series = 1
    jump Waiting


label lisa_horor_movie_r:

    if lisa.dcv.other.stage>1 and lisa.dcv.other.done:
        $ lisa.dress = 'c'

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    if lisa.dcv.other.stage==1 and lisa.dcv.other.done:
        Max_01 "Да, смотрим. Сейчас всё подготовлю... Не стесняйся, снимай маечку."
        Lisa_02 "Сейчас сниму, только свет сначала выключу. Тебе уже страшно?"
        $ lisa.dcv.other.stage=2
        $ lisa.dress = 'c'
    else:
        Max_01 "Да, смотрим. Сейчас всё подготовлю..."
        Lisa_02 "А я пока свет выключу. Тебе уже страшно?"

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    $ renpy.show('Lisa horror-myroom 00-01'+lisa.dress)

    if flags.cur_series < 2:
        #если не досмотрели фильм
        Max_07 "Как бы не так! Будем досматривать тот фильм, который тогда смотрели?"
        menu:
            Lisa_00 "Ой, я даже не знаю... Главное, чтобы и тебе было страшно! И желательно, чтобы больше, чем мне."
            "Тогда досматриваем... (продолжаем смотреть \"Кошмар на улице Вязов\")" if flags.cur_movies[0] == 'hes':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_series = 2
                play music hes
            "Тогда досматриваем... (продолжаем смотреть \"Пятница 13-е\")" if flags.cur_movies[0] == 'f13':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_series = 2
                play music f13
            "Тогда досматриваем... (продолжаем смотреть \"Крик\")" if flags.cur_movies[0] == 'scr':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_series = 2
                play music scream
            "{i}смотреть \"Кошмар на улице Вязов\"{/i}" if flags.cur_movies[0]!='hes':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'hes'
                if flags.cur_movies[1] < 5:
                    $ flags.cur_movies[1] += 1
                else:
                    $ flags.cur_movies[1] = 1
                play music hes
            "{i}смотреть \"Пятница 13-е\"{/i}" if flags.cur_movies[0]!='f13':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'f13'
                if flags.cur_movies[2] < 5:
                    $ flags.cur_movies[2] += 1
                else:
                    $ flags.cur_movies[2] = 1
                play music f13
            "{i}смотреть \"Крик\"{/i}" if flags.cur_movies[0]!='scr':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'scr'
                if flags.cur_movies[3] < 4:
                    $ flags.cur_movies[3] += 1
                else:
                    $ flags.cur_movies[3] = 1
                play music scream
    else:
        #если досмотрели фильм
        Max_07 "Как бы не так! Будем смотреть следующий фильм в той серии, которую начали?"
        $ flags.cur_series = 1
        menu:
            Lisa_00 "Ой, я даже не знаю... Главное, чтобы и тебе было страшно! И желательно, чтобы больше, чем мне."
            "Тогда смотрим дальше... (продолжаем смотреть серию фильмов \"Кошмар на улице Вязов\")"  if flags.cur_movies[0] == 'hes':
                if flags.cur_movies[1] < 5:
                    $ flags.cur_movies[1] += 1
                else:
                    $ flags.cur_movies[1] = 1
                play music hes
            "Тогда смотрим дальше...  (продолжаем смотреть серию фильмов \"Пятница 13-е\")" if flags.cur_movies[0] == 'f13':
                if flags.cur_movies[2] < 5:
                    $ flags.cur_movies[2] += 1
                else:
                    $ flags.cur_movies[2] = 1
                play music f13
            "Тогда смотрим дальше...  (продолжаем смотреть серию фильмов \"Крик\")" if flags.cur_movies[0] == 'scr':
                if flags.cur_movies[3] < 4:
                    $ flags.cur_movies[3] += 1
                else:
                    $ flags.cur_movies[3] = 1
                play music scream
            "{i}смотреть \"Кошмар на улице Вязов\"{/i}" if flags.cur_movies[0]!='hes':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'hes'
                if flags.cur_movies[1] < 5:
                    $ flags.cur_movies[1] += 1
                else:
                    $ flags.cur_movies[1] = 1
                play music hes
            "{i}смотреть \"Пятница 13-е\"{/i}" if flags.cur_movies[0]!='f13':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'f13'
                if flags.cur_movies[2] < 5:
                    $ flags.cur_movies[2] += 1
                else:
                    $ flags.cur_movies[2] = 1
                play music f13
            "{i}смотреть \"Крик\"{/i}" if flags.cur_movies[0]!='scr':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'scr'
                if flags.cur_movies[3] < 4:
                    $ flags.cur_movies[3] += 1
                else:
                    $ flags.cur_movies[3] = 1
                play music f13


    if renpy.random.randint(1, 2) < 2:
        scene BG char Lisa horror-myroom 01
        $ renpy.show("Lisa horror-myroom 01-01"+lisa.dress)
    else:
        scene BG char Lisa horror-myroom 01a
        $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)

    Lisa_09 "Может хоть для приличия испугаешься? А то иначе я уже не знаю, как тебя наказать, разве что маме тебя сдать..."
    Max_14 "Я боюсь! Теперь стало намного страшнее после твоих слов."

    scene BG char Lisa horror-myroom 03
    $ renpy.show('Lisa horror-myroom 03-01'+lisa.dress)
    Lisa_10 "Вот и хорошо, а то я не хочу одна бояться. Ну вот что они делают?! Это же точно ничем хорошим не закончится!"
    Max_02 "{i}( Хорошо, что в ужастиках куча тупых персонажей, потому что это гарантирует мне крепкие объятия от Лизы! Главное стараться не думать, какими прелестями она ко мне прижимается. ){/i}"

    scene BG char Lisa horror-myroom 02
    $ renpy.show('Lisa horror-myroom 02-01'+lisa.dress)
    $ renpy.dynamic('h_film', 'r1')
    $ h_film = {'hes':1, 'f13':2, 'scr':3}[flags.cur_movies[0]]
    $ renpy.show('FG horror-myroom '+flags.cur_movies[0]+' 0'+str(flags.cur_movies[h_film]+1)+"-0"+str(flags.cur_series))
    Lisa_11 "Ой-ёй-ёй... Зря мы это смотрим! Кажется, я теперь от таких ужасов не смогу заснуть..."

    $ _ch3 = GetChance(mgg.sex+5, 3, 900)
    if lisa.dress>'b':
        Max_10 "{i}( Только бы у меня не встал! У меня тут полный эффект погружения... Ладно в ужастике сиськи голые периодически мелькают, а вот голая грудь моей сестрёнки, которой она слегка трётся о меня, вот это проблема... Как тут сдерживаться? ){/i}" nointeract
    else:
        Max_10 "{i}( Только бы у меня не встал! Ещё периодически сиськи голые в ужастике мелькают... Как тут сдерживаться? ){/i}" nointeract
    menu:
        "{i}сдерживаться{/i} \n{color=[_ch3.col]}(Сексуальный опыт. Шанс: [_ch3.vis]){/color}":
            if (not _in_replay and not RandomChance(_ch3.ch)) or (_in_replay and lisa.flags.kiss_lesson<12):
                # (не получилось сдержаться)
                $ Skill('sex', 0.1)
                Lisa_13 "[norestrain!t]Макс, мне кажется или у меня под ногой сейчас что-то увеличивается?"
                jump .not_restrain

            # (получилось сдержаться)
            $ Skill('sex', 0.2)
            if flags.cur_series < 2:
                # если начали новый фильм
                Lisa_09 "[restrain!t]Макс, я уже спать хочу. Давай закругляться. Да и набоялась я уже слишком..."
            else:
                 #если продолжили смотреть
                Lisa_09 "[restrain!t]Наконец-то фильм заканчивается, а то я набоялась уже сполна..."
            #  выключается музыка
            stop music fadeout 1.0
            Max_04 "Ага, я тоже. Было страшно, но я рад, что ты была рядом. Это приятно."

            #horror-myroom-01a + horror-myroom-01a-max&lisa-02
            scene BG char Lisa horror-myroom 01a
            $ renpy.show('Lisa horror-myroom 01a-02'+lisa.dress)
            Lisa_10 "Мне только страшно до своей кровати идти теперь..."
            Max_03 "Так не иди. Спи со мной. Я очень даже не против!"
            menu:
                Lisa_05 "Чтобы со мной рядом кое-что шевелилось? Так я точно не усну. Мне нужно как-то храбрости набраться..."
                "{i}поцеловать Лизу{/i}" if lisa.flags.kiss_lesson > 6:   #если открыты поцелуи с прикосновениями
                    $ added_mem_var('horror_kiss')
                    #horror-myroom-02 + horror-myroom-02-max&lisa-02 или horror-myroom-02a + horror-myroom-02-max&lisa-03
                    $ r1 = '0'+str(renpy.random.randint(2, 3))
                    $ renpy.scene()
                    $ renpy.show('BG char Lisa horror-myroom '+r1)
                    $ renpy.show('Lisa horror-myroom 02-'+r1+lisa.dress)
                    if lisa.dress>'b':
                        Max_05 "{i}( Нежный поцелуй с сестрёнкой перед сном точно отвлечёт её от всяких страхов. Целуя её, вообще забываешь о том, что там было перед этим... Лишь её сочные губки и нежная грудь, которой она касается меня... ){/i}"
                        if lisa.dcv.special.stage < 7:
                            $ lisa.dcv.special.stage = 7
                    else:
                        Max_05 "{i}( Нежный поцелуй с сестрёнкой перед сном точно отвлечёт её от всяких страхов. Целуя её, вообще забываешь о том, что там было перед этим... Лишь её сочные губки... ){/i}"

                    scene BG char Lisa horror-myroom 01a
                    $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)
                    Lisa_02 "Да, так уже совсем не страшно. Я пойду... Спокойной ночи, Макс."
                    Max_01 "Ага. Приятных снов."
                    if lisa.dcv.special.stage < 6:
                        $ lisa.dcv.special.stage = 6
                    $ poss['SoC'].open(13)
                    jump .end

                "Просто иди и всё..." if not _in_replay:
                    Lisa_13 "Ну ага, просто иди! А вдруг меня что-то схватит?!"
                    Max_07 "У нас в комнате нет никаких монстров! Если конечно не считать того, что у меня в трусах."

                    scene BG char Lisa horror-myroom 04
                    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
                    Lisa_01 "Ой, с тобой и правда страшно спать будет! Я пошла к себе..."
                    Max_01 "Ага. Спокойной ночи."
                    jump .end

        "{i}да пофиг!{/i}":
            Lisa_13 "Макс, мне кажется или у меня под ногой сейчас что-то увеличивается?"
            jump .not_restrain

    label .not_restrain:
        Max_07 "Однозначно кажется..."

        scene BG char Lisa horror-myroom 04
        $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
        stop music fadeout 1.0
        if lisa.dress>'b':
            Lisa_12 "Ага, кажется, как же! Опять ты возбудился... Хотя, ничего удивительного, я была почти уверена, что так и будет."
            Max_09 "Ну встал и встал, подумаешь. Спрячу под ноутбуком."
        else:
            Lisa_12 "Ага, кажется, как же! Опять ты возбудился... Я же твоя сестра, тебе стыдно должно быть!"
            Max_09 "Стыдно?! Ну встал и встал, подумаешь."

        scene BG char Lisa horror-myroom 00
        show Max horror-myroom 01a
        $ renpy.show('Lisa horror-myroom 00-02'+lisa.dress)
        Lisa_10 "Хватит уже похабно думать обо мне! Я ушла спать... Ой! Как страшно..."
        Max_04 "Проводить тебя до кровати?"
        Lisa_13 "Сама справлюсь! Ой ой ой!"
        jump .end

    label .end:
        $ renpy.end_replay()
        if lisa.dcv.other.stage>1 and lisa.dcv.other.done:
            $ lisa.dress = 'b'
        $ spent_time += 60
        $ infl[lisa].add_m(12)
        $ lisa.dcv.special.disable()
        jump Waiting
