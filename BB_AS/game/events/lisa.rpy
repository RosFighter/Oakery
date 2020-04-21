################################################################################
## события Лизы

label lisa_sleep_night:
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
    if peeping['lisa_shower'] > 3:
        menu:
            Max_00 "Лиза сейчас принимает душ..."
            "{i}уйти{/i}":
                jump .end_peeping2
    elif peeping['lisa_shower'] > 2:
        Max_14 "Лиза уже поймала меня на подглядывании. Грозилась рассказать маме. Не стоит злить ее еще больше."
        jump .end_peeping2
    elif peeping['lisa_shower'] > 1:
        Max_09 "Сегодня я уже чуть не попался Лизе при подглядывании. Повезло, что успел вовремя сбежать. Не стоит рисковать еще раз."
        jump .end_peeping2
    elif peeping['lisa_shower'] > 0:
        Max_01 "Сегодня я уже подсматривал за Лизой. Повезло, что она меня не заметила. Не стоит рисковать еще раз."
        jump .end_peeping2

    $ renpy.block_rollback()
    $ peeping['lisa_shower'] = 4
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
                                    $ peeping['lisa_shower'] = 4
                                    jump .end_peeping
                        "Хорошо, я подожду":
                            $ peeping['lisa_shower'] = 4
                            jump .end_peeping
                "{i}уйти{/i}":
                    $ peeping['lisa_shower'] = 4
                    jump .end_peeping
        "{i}заглянуть со двора{/i}":
            if sorry_gifts['lisa'].owe:
                Max_10 "Хочется, конечно, ещё разок взглянуть на голую сестрёнку, но я ещё не отдал ей обещанное..."
                jump .end_peeping2
            jump .start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags['ladder'] > 2:
            jump .ladder
        "{i}уйти{/i}":
            $ peeping['lisa_shower'] = 4
            jump .end_peeping

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ __list = ['c', ]
        if lisa.nopants:
            $ __list.append('d')
        if 'bathrobe' in lisa.gifts:
            $ __list.append('a')
            if lisa.nopants:
                $ __list.append('b')
        $ __r1 = renpy.random.choice(__list)

        scene BG bathroom-morning-00
        $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1)
        show FG bathroom-morning-00
        $ notify_list.append(_("Скрытность Макса капельку повысилась"))
        $ mgg.stealth += 0.05
        if __r1 == 'a':
            Max_03 "Класс! Лиза смотрится в подаренном мною халатике очень соблазнительно... Особенно когда так хорошо видно её упругие сисечки!"
        elif __r1 == 'b':
            Max_05 "Охх... Хорошо, что я уговорил её не носить трусики! Похоже, Лизе и самой приятно, что под халатиком больше ничего нет... а уж мне-то как приятно."
        elif __r1 == 'c':
            Max_07 "О, да! Моя обворожительная сестрёнка в одних трусиках... Так и хочется зайти и стянуть их с её прекрасной попки!"
        else:
            Max_06 "Ого! Утро может быть действительно очень добрым, если удаётся полюбоваться совершенно голенькой Лизой! Да... её тело завораживает..."

        $ spent_time += 10
        Max_00 "Хоть и не хочется, но пока меня не заметили, лучше уходить..."
        jump .end_peeping

    label .start_peeping:
        $ peeping['lisa_shower'] = 1
        $ notify_list.append(_("Скрытность Макса капельку повысилась"))
        $ mgg.stealth += 0.03
        $ __ran1 = renpy.random.randint(1, 4)

        $ _chance = GetChance(mgg.stealth, 3, 900)
        $ _chance_color = GetChanceColor(_chance)
        $ ch_vis = str(int(_chance/10)) + "%"
        $ renpy.scene()
        $ renpy.show('Lisa shower 0'+str(__ran1))
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Отлично! Моя младшая сестрёнка принимает душ... Даже видно кое-что... Много кое-чего! Только бы она меня не заметила..."
            "{i}продолжить смотреть\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
                jump .closer_peepeng
            "{i}немного пошуметь{/i}" if 1 <= len(sorry_gifts['lisa'].give) < 4:
                jump .pinded
            "{i}уйти{/i}":
                jump .end_peeping

    label .closer_peepeng:
        $ spent_time += 10
        if RandomChance(_chance):
            $ peeping['lisa_shower'] = 1
            $ mgg.stealth += 0.2
            $ notify_list.append(_("Скрытность Макса повысилась"))
            $ lisa.dress_inf = '00a'
            $ __ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            $ renpy.show('Lisa shower-closer 0'+str(__ran1))
            show FG shower-closer
            if 1 < __ran1 < 5:
                Max_02 "[undetect!t]Лиза вся такая мокренькая... класс! Фигурка и всё остальное у неё – что надо... Как же хочется потрогать!"
            else:
                Max_03 "[undetect!t]О, да! За тем, как вода стекает по её обворожительной попке, хочется смотреть не отрываясь..."
        elif RandomChance(_chance) or len(sorry_gifts['lisa'].give) > 3:
            $ peeping['lisa_shower'] = 2
            $ mgg.stealth += 0.1
            $ notify_list.append(_("Скрытность Макса немного повысилась"))
            $ lisa.dress_inf = '00a'
            $ __ran1 = renpy.random.randint(7, 8)
            scene BG shower-closer
            $ renpy.show('Lisa shower-closer 0'+str(__ran1))
            show FG shower-closer
            Max_12 "{color=[orange]}{i}Кажется, Лиза что-то заподозрила!{/i}{/color}\nО нет! Похоже, она что-то заметила... Надо бежать!"
        else:
            jump .pinded
        jump .end_peeping

    label .pinded:
        $ peeping['lisa_shower'] = 3
        $ punreason[0] = 1
        $ mgg.stealth += 0.05
        $ notify_list.append(_("Скрытность Макса чуть-чуть повысилась"))
        $ __ran1 = renpy.random.choice(['09', '10'])
        scene BG shower-closer
        $ renpy.show('Lisa shower-closer '+__ran1)
        show FG shower-closer
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


label lisa_dressed_school:
    scene location house myroom door-morning

    $ __mood = 0
    $ __rel = 0
    if peeping['lisa_dressed'] == 0:
        $ peeping['lisa_dressed'] = 1
        jump .lisa_dressed
    else:
        return

    menu .lisa_dressed:
        Max_09 "{i}Похоже, Лиза собирается в школу...{/i}"
        "{i}постучаться{/i}" if lisa.free < 200:
            menu:
                "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
                "Это я, Макс. Можно войти?":
                    jump .come_in
                "Хорошо, я подожду...":
                    $ spent_time = 10
                    jump .rel_mood
        "{i}открыть дверь{/i}" if lisa.free < 200:
            jump .open_door
        "{i}заглянуть в окно{/i}"  if lisa.free < 200:
            jump .look_window
        #"войти в комнату" if lisa.free >= 200:
        #    pass
        "{i}уйти{/i}":
            $ spent_time = 10
            jump .rel_mood

    label .look_window:
        $ spent_time = 10
        $ __ran1 = renpy.random.choice(['01', '02', '03', '04'])
        $ lisa.dress_inf = {'01':'02h', '02':'02e', '03':'02b', '04':'02c'}[__ran1]
        scene BG char Lisa voyeur-00
        $ renpy.show('Lisa voyeur '+__ran1)
        $ renpy.show('FG voyeur-lisa-00'+mgg.dress)
        $ notify_list.append(_("Скрытность Макса капельку повысилась"))
        $ mgg.stealth += 0.03
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "{i}уйти{/i}":
                jump .end

    label .come_in:
        scene BG char Lisa morning
        if GetRelMax('lisa')[0] < 0:
            show Lisa school-dressed 01
            $ lisa.dress_inf = '01b'
        elif GetRelMax('lisa')[0] < 2:
            show Lisa school-dressed 01a
            $ lisa.dress_inf = '01b'
        elif lisa.free < 200:
            show Lisa school-dressed 01b
            $ lisa.dress_inf = '02a'
        else:
            show Lisa school-dressed 01c # пока отсутствует
            $ lisa.dress_inf = '00'

        $ spent_time = 60 - int(tm.split(":")[1])
        menu:
            Lisa_00 "Макс, ну чего ломишься? Ты же знаешь, что мне в школу пора...\n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
            "Это и моя комната!":
                if lisa.GetMood()[0] < 0: # настроение не очень и ниже
                    show Lisa school-dressed 01
                    Lisa_12 "Так и знала, что тебя надо было на диванчики в гостиную отправлять... Ладно, я уже оделась, входи уж... А я в школу побежала."
                    Max_00 "Удачи"
                    $ __rel  -= 5 # при плохом настроении отношения и настроение снижаются
                    $ __mood -= 25
                else: # нейтральное настроение
                    Lisa_02 "В любом случае, я уже оделась, так что, входи. А я побежала в школу."
                    Max_00 "Удачи"
            "Да чего я там не видел...":
                if GetRelMax('lisa')[0] < 1: # отношения прохладные и ниже
                    Lisa_12 "Откуда я знаю, что ты видел, а что ещё нет? Но так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                    Max_00 "Пока, Лиза!"
                    $ __rel  -= 5 # при низком отношении отношения и настроение снижаются
                    $ __mood -= 30
                elif GetRelMax('lisa')[0] < 2: # Неплохие отношения
                    Lisa_01 "Откуда я знаю, что ты видел, а что ещё нет? Но так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                    Max_00 "Пока, Лиза!"
                else: # хорошие и выше отношения
                    Lisa_02 "Откуда я знаю, что ты видел, а что ещё нет?"
                    show Lisa school-dressed 01a
                    Lisa_01 "Но так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                    Max_00 "Пока, Лиза!"
                    $ __mood += 30 # при хорошем отношении настроение повышается
            "Извини":
                if GetRelMax('lisa')[0] < 2: # Неплохие отношения
                    Lisa_03 "Да ты у нас джентльмен! В общем, я тут закончила и побежала в школу. Пока!"
                else:
                    Lisa_03 "Да ты у нас, оказывается, джентльмен!"
                    show Lisa school-dressed 01a
                    Lisa_01 "В общем, я тут закончила и побежала в школу. Пока!"
                Max_00 "Пока, Лиза!"
                $ __mood += 30 # при извинении настроение повышается

        jump .rel_mood

    label .open_door:
        $ spent_time = 20
        $ __ran1 = renpy.random.randint(2, 5)
        $ lisa.dress_inf = {2:'02a', 3:'02c', 4:'02b', 5:'00'}[__ran1]
        scene BG char Lisa morning
        if GetRelMax('lisa')[0] < 0:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1))
        elif GetRelMax('lisa')[0] < 2:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1)+'a')
        elif lisa.free < 200:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1)+'b')
        else:
            $ renpy.show('Lisa school-dressed 0'+str(__ran1)+'c') # пока отсутствует

        $ __mood -= 50 # настроение портится в любом случае
        if __ran1 < 3: # Лиза практически одета
            menu:
                Lisa_12 "Макс! Стучаться надо! А вдруг я была бы голая?! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "Ну, тогда мне бы повезло":
                    $ __rel -= 5
                    Lisa_13 "Ну ты хам! Быстро закрой дверь с той стороны!"
                    Max_00 "Хорошо..."
                "Извини, я забыл...":
                    Lisa_01 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
                    Max_00 "Хорошо..."
                    $ __mood += 50
        elif __ran1 < 5: # Лиза частично одета
            menu:
                Lisa_12 "Макс! Не видишь, я собираюсь в школу! Быстро закрой дверь! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "Извини... Кстати, отличный зад!" if __ran1 < 3:
                    if GetRelMax('lisa')[0] < 2:
                        $ __rel -= 5
                "Извини..." if __ran1 > 2:
                    $ __mood += 50
        else: # Лиза полностью голая
            menu:
                Lisa_12 "Макс! Я не одета! Быстрой закрой дверь с той стороны! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "А у тебя сиськи подросли!":
                    $ __rel -= 5
                    menu:
                        Lisa_11 "Что?! Я всё маме расскажу!"
                        "Всё, всё, ухожу!":
                            pass
                        "Уже ухожу, но сиськи - супер!":
                            $ __rel -= 5
                            menu:
                                Lisa_12 "..."
                                "{i}Бежать{/i}":
                                    pass
                "Извини, я не хотел...":
                    Lisa_12 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
                    Max_00 "Хорошо..."
                    if GetRelMax('lisa')[0] > 1:
                        $ __mood += 50

    scene location house myroom door-morning

    label .rel_mood:
        $ AddRelMood('lisa', __rel, __mood)

    label .end:
        jump Waiting


label lisa_dressed_shop:
    scene location house myroom door-morning

    if peeping['lisa_dressed'] != 0:
        return
    else:
        $ __mood = 0
        $ __rel = 0
        $ __warned = False
        $ peeping['lisa_dressed'] = 1
        $ spent_time = 60 - int(tm[-2:])
        menu .lisa_dressed:
            Max_09 "Кажется, все собираются на шоппинг и Лиза сейчас переодевается..."
            "{i}постучаться{/i}":
                jump .knock
            "{i}открыть дверь{/i}":
                jump .open_door
            "{i}заглянуть в окно{/i}":
                jump .look_window

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
            $ notify_list.append(_("Скрытность Макса капельку повысилась"))
            $ mgg.stealth += 0.03
            menu:
                Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
                "{i}уйти{/i}":
                    jump .rel_mood


        scene location house myroom door-morning

        label .rel_mood:
            $ AddRelMood('lisa', __rel, __mood)

    jump Waiting


label lisa_dressed_repetitor:
    scene location house myroom door-morning

    if peeping['lisa_dressed'] != 0:
        return

    menu:
        Max_09 "Кажется, Лиза куда-то собирается, но дверь закрыта..."
        "{i}уйти{/i}":
            $ peeping['lisa_dressed'] = 1

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
    $ persone_button1 = 'Lisa crockery-evening 01'+lisa.dress
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


label lisa_bath:
    scene location house bathroom door-evening
    if peeping['lisa_bath'] != 0:
        return

    $ peeping['lisa_bath'] = 1
    $ __mood = 0
    $ __rel = 0
    menu:
        Max_00 "В это время Лиза обычно плескается в ванне..."
        "{i}постучаться{/i}":
            jump .knock
        "{i}открыть дверь{/i}":
            jump .open
        "{i}заглянуть со двора{/i}" if 'ladder' not in flags or flags['ladder'] < 2:
            scene Lisa bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "Кажется, Лиза и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но ближе подойти опасно - может заметить..."
            Max_09 "Нужно что-нибудь придумать..."
            $ flags['ladder'] = 1
            jump .end
        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
            $ flags['ladder'] = 3
            $ items['ladder'].have = False
            $ items['ladder'].InShop = False
            jump .ladder
        "{i}воспользоваться стремянкой{/i}" if flags['ladder'] > 2:
            jump .ladder
        "{i}уйти{/i}":
            jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-evening 02'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."

        $ __r1 = renpy.random.randint(1, 4)

        scene BG bath-00
        $ renpy.show('Lisa bath-window 0'+str(__r1))
        show FG bath-00
        $ notify_list.append(_("Скрытность Макса капельку повысилась"))
        $ mgg.stealth += 0.03
        if __r1 == 1:
            menu:
                Max_03 "Кажется, Лиза как раз собирается принять ванну... О да, моя младшая сестрёнка хороша... а голенькая, так особенно!"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Lisa bath-window '+renpy.random.choice(['02', '03', '04']))
                    $ notify_list.append(_("Скрытность Макса капельку повысилась"))
                    $ mgg.stealth += 0.03
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
                    $ notify_list.append(_("Скрытность Макса капельку повысилась"))
                    $ mgg.stealth += 0.03
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
