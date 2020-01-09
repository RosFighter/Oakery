################################################################################
## события Лизы

label lisa_sleep:
    if tm < "06:00":
        scene BG char Lisa bed-night
        $ AvailableActions["touch"].active = True
        $ renpy.show("Lisa sleep-night "+pose3_1+characters["lisa"].dress)
    else:
        scene BG char Lisa bed-morning
        $ renpy.show("Lisa sleep-morning "+pose3_1+characters["lisa"].dress)
    return


label lisa_shower:
    scene location house bathroom door-morning
    if peeping["lisa_shower"] > 3:
        menu:
            Max_00 "Лиза сейчас принимает душ..."
            "{i}уйти{/i}":
                jump .end_peeping2
    elif peeping["lisa_shower"] > 2:
        Max_14 "Лиза уже поймала меня на подглядывании. Грозилась рассказать маме. Не стоит злить ее еще больше."
        jump .end_peeping2
    elif peeping["lisa_shower"] > 1:
        Max_09 "Сегодня я уже чуть не попался Лизе при подглядывании. Повезло, что успел вовремя сбежать. Не стоит рисковать еще раз."
        jump .end_peeping2
    elif peeping["lisa_shower"] > 0:
        Max_01 "Сегодня я уже подсматривал за Лизой. Повезло, что она меня не заметила. Не стоит рисковать еще раз."
        jump .end_peeping2
    else:
        $ renpy.block_rollback()
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
                                        $ peeping["lisa_shower"] = 4
                                        jump .end_peeping
                            "Хорошо, я подожду":
                                $ peeping["lisa_shower"] = 4
                                jump .end_peeping
                    "{i}уйти{/i}":
                        $ peeping["lisa_shower"] = 4
                        jump .end_peeping
            "{i}заглянуть с улицы{/i}":
                jump .start_peeping
            "{i}уйти{/i}":
                $ peeping["lisa_shower"] = 4
                jump .end_peeping

    label .start_peeping:
        $ peeping["lisa_shower"] = 1
        $ renpy.notify(_("Скрытность Макса капельку повысилась"))
        $ max_profile.stealth += 0.01
        $ __ran1 = renpy.random.randint(1, 4)

        $ _chance = GetChance(max_profile.stealth, 3)
        $ ch_vis = int(round(_chance))
        if ch_vis < 33:
            $ _chance_color = red
        elif ch_vis > 67:
            $ _chance_color = lime
        else:
            $ _chance_color = orange
        $ ch_vis = str(ch_vis) + "%"
        scene image ("Lisa shower 0"+str(__ran1))
        $ renpy.show("FG shower 00"+max_profile.dress)
        menu:
            Max_04 "Лиза принимает душ"
            "{i}присмотреться\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
                jump .closer_peepeng
            "{i}уйти{/i}":
                jump .end_peeping

    label .closer_peepeng:
        if RandomChance(_chance):
            $ peeping["lisa_shower"] = 1
            $ max_profile.stealth += 0.1
            $ renpy.notify(_("Скрытность Макса повысилась"))
            $ characters["lisa"].dress_inf = "00a"
            $ __ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            show image ("Lisa shower-closer 0"+str(__ran1))
            show FG shower-closer
            Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nОх, повезло! Хороша сестренка."
        elif RandomChance(_chance):
            $ peeping["lisa_shower"] = 2
            $ max_profile.stealth += 0.05
            $ renpy.notify(_("Скрытность Макса немного повысилась"))
            $ characters["lisa"].dress_inf = "00a"
            $ __ran1 = renpy.random.randint(7, 8)
            scene BG shower-closer
            show image ("Lisa shower-closer 0"+str(__ran1))
            show FG shower-closer
            Max_09 "{color=[orange]}{i}Кажется, Лиза что-то заподозрила!{/i}{/color}\nПора сматываться."
        else:
            $ peeping["lisa_shower"] = 3
            $ max_profile.stealth += 0.02
            $ renpy.notify(_("Скрытность Макса чуть-чуть повысилась"))
            $ __ran1 = renpy.random.choice(["09", "10"])
            scene BG shower-closer
            show image ("Lisa shower-closer "+__ran1)
            show FG shower-closer
            menu:
                Lisa_12 "{color=[orange]}{i}Неудалось незаметно подкрасться!{/i}{/color}\nМакс!!! Ты за мной подглядываешь?! Я всё маме расскажу!!!"
                "{i}уйти{/i}":
                    jump .end_peeping
        jump .end_peeping

    label .end_peeping2:
        $ current_room, prev_room = prev_room, current_room
        jump AfterWaiting
    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label lisa_read:

    scene BG char Lisa reading
    $ renpy.show("Lisa reading "+pose3_1+characters["lisa"].dress)
    return


label lisa_dressed_school:
    scene location house myroom door-morning

    $ __mood = 0
    $ __rel = 0
    if peeping["lisa_dressed"] == 0:
        $ peeping["lisa_dressed"] = 1
        jump .lisa_dressed
    else:
        return

    menu .lisa_dressed:
        Max_09 "{i}Похоже, Лиза собирается в школу...{/i}"
        "{i}постучаться{/i}" if characters["lisa"].mindedness < 200:
            menu:
                "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
                "Это я, Макс. Можно войти?":
                    jump .come_in
                "Хорошо, я подожду...":
                    $ spent_time = 10
                    jump .rel_mood
        "{i}открыть дверь{/i}" if characters["lisa"].mindedness < 200:
            jump .open_door
        "{i}заглянуть в окно{/i}"  if characters["lisa"].mindedness < 200:
            jump .look_window
        #"войти в комнату" if characters["lisa"].mindedness >= 200:
        #    pass
        "{i}уйти{/i}":
            $ spent_time = 10
            jump .rel_mood

    label .look_window:
        $ spent_time = 10
        $ __ran1 = renpy.random.choice(["01", "02", "03", "04"])

        if __ran1 == "01":
            $ characters["lisa"].dress_inf = "02d"
        elif __ran1 == "02":
            $ characters["lisa"].dress_inf = "02e"
        elif __ran1 == "03":
            $ characters["lisa"].dress_inf = "02b"
        else:
            $ characters["lisa"].dress_inf = "02c"

        scene BG char Lisa voyeur-00
        $ renpy.show("Lisa voyeur "+__ran1)
        $ renpy.show("FG voyeur-lisa-00"+max_profile.dress)
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "{i}уйти{/i}":
                jump .end

    label .come_in:
        scene BG char Lisa morning
        if characters["lisa"].relmax < 0:
            show Lisa school-dressed 01
            $ characters["lisa"].dress_inf = "01b"
        elif characters["lisa"].relmax < 250:
            show Lisa school-dressed 01a
            $ characters["lisa"].dress_inf = "01b"
        elif characters["lisa"].relmax < 700:
            show Lisa school-dressed 01b
            $ characters["lisa"].dress_inf = "02a"
        else:
            show Lisa school-dressed 01c # пока отсутствует
            $ characters["lisa"].dress_inf = "00"

        $ spent_time = 60 - int(tm.split(":")[1])
        menu:
            Lisa_00 "Макс, ну чего ломишься? Ты же знаешь, что мне в школу пора...\n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
            "Это и моя комната!":
                if characters["lisa"].mood < -15: # настроение не очень и ниже
                    show Lisa school-dressed 01
                    Lisa_12 "Так и знала, что тебя надо было на диванчики в гостиную отправлять... Ладно, я уже оделась, входи уж... А я в школу побежала."
                    Max_00 "Удачи"
                    $ __rel  -= 5 # при плохом настроении отношения и настроение снижаются
                    $ __mood -= 5
                else: # нейтральное настроение
                    Lisa_02 "В любом случае, я уже оделась, так что, входи. А я побежала в школу."
                    Max_00 "Удачи"
            "Да чего я там не видел...":
                if characters["lisa"].relmax < 100: # отношения прохладные и ниже
                    Lisa_12 "Откуда я знаю, что ты видел, а что ещё нет? Но так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                    Max_00 "Пока, Лиза!"
                    $ __rel  -= 5 # при низком отношении отношения и настроение снижаются
                    $ __mood -= 5
                elif characters["lisa"].relmax < 250: # Неплохие отношения
                    Lisa_01 "Откуда я знаю, что ты видел, а что ещё нет? Но так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                    Max_00 "Пока, Лиза!"
                else: # хорошие и выше отношения
                    Lisa_02 "Откуда я знаю, что ты видел, а что ещё нет?"
                    show Lisa school-dressed 01a
                    Lisa_01 "Но так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
                    Max_00 "Пока, Лиза!"
                    $ __mood += 5 # при хорошем отношении настроение повышается
            "Извини":
                if characters["lisa"].relmax < 250: # Неплохие отношения
                    Lisa_03 "Да ты у нас джентльмен! В общем, я тут закончила и побежала в школу. Пока!"
                else:
                    Lisa_03 "Да ты у нас, оказывается, джентльмен!"
                    show Lisa school-dressed 01a
                    Lisa_01 "В общем, я тут закончила и побежала в школу. Пока!"
                Max_00 "Пока, Лиза!"
                $ __mood += 5 # при извинении отношение и настроение повышаются
                $ __rel += 5

        jump .rel_mood

    label .open_door:
        $ spent_time = 20
        $ __ran1 = renpy.random.randint(2, 5)
        if __ran1 == 2:
            $ characters["lisa"].dress_inf = "02a"
        elif __ran1 == 3:
            $ characters["lisa"].dress_inf = "02c"
        elif __ran1 == 4:
            $ characters["lisa"].dress_inf = "02b"
        else:
            $ characters["lisa"].dress_inf = "00"
        scene BG char Lisa morning
        if characters["lisa"].relmax < 0:
            $ renpy.show("Lisa school-dressed 0"+str(__ran1))
        elif characters["lisa"].relmax < 250:
            $ renpy.show("Lisa school-dressed 0"+str(__ran1)+"a")
        elif characters["lisa"].relmax < 700:
            $ renpy.show("Lisa school-dressed 0"+str(__ran1)+"b")
        else:
            $ renpy.show("Lisa school-dressed 0"+str(__ran1)+"c") # пока отсутствует

        $ __mood -= 5 # настроение портится в любом случае
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
                    $ __mood += 5
        elif __ran1 < 5: # Лиза частично одета
            menu:
                Lisa_12 "Макс! Не видишь, я собираюсь в школу! Быстро закрой дверь! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
                "Извини... Кстати, отличный зад!" if __ran1 < 3:
                    if characters["lisa"].relmax < 250:
                        $ __rel -= 5
                "Извини..." if __ran1 > 2:
                    $ __mood += 5
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
                            $ __rel-= 5
                            menu:
                                Lisa_12 "..."
                                "{i}Бежать{/i}":
                                    pass
                "Извини, я не хотел...":
                    Lisa_12 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
                    Max_00 "Хорошо..."
                    if characters["lisa"].relmax >= 250:
                        $ __mood += 5

    scene location house myroom door-morning

    label .rel_mood:
        $ HintRelMood("lisa", __rel, __mood)
        $ characters["lisa"].relmax += __rel
        $ characters["lisa"].mood   += __mood

    label .end:
        jump Waiting


label lisa_dressed_shop:
    scene location house myroom door-morning

    if peeping["lisa_dressed"] != 0:
        return
    else:
        $ __mood = 0
        $ __rel = 0
        $ __warned = False
        $ peeping["lisa_dressed"] = 1
        $ spent_time = 60 - int(tm.split(":")[1])
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
            if __ran1 == 3:
                $ characters["lisa"].dress_inf = "02c"
            elif __ran1 == 4:
                $ characters["lisa"].dress_inf = "02b"
            else:
                $ characters["lisa"].dress_inf = "00"
            scene BG char Lisa morning
            if characters["lisa"].relmax < 0:
                $ renpy.show("Lisa school-dressed 0"+str(__ran1))
            elif characters["lisa"].relmax < 250:
                $ renpy.show("Lisa school-dressed 0"+str(__ran1)+"a")
            elif characters["lisa"].relmax < 700:
                $ renpy.show("Lisa school-dressed 0"+str(__ran1)+"b")
            else:
                $ renpy.show("Lisa school-dressed 0"+str(__ran1)+"c") # пока отсутствует

            if __warned:
                $ __mood -= 15
                $ __rel -= 15
                $ phrase = _("Я не одета!")
            else:
                $ __mood -= 5 # настроение портится в любом случае
                $ phrase = _("Я же сказала, что я не одета! ")

            menu:
                Lisa_12 "Макс! [phrase!t]Быстрой закрой дверь с той стороны!"
                "Извини... Кстати, отличный зад!" if __ran1 == 2:
                    if characters["lisa"].relmax < 250:
                        $ __rel -= 5
                "А у тебя сиськи подросли!":
                    menu:
                        Lisa_11 "Что?! Я всё маме расскажу!"
                        "Всё, всё, ухожу!":
                            jump .rel_mood
                        "Уже ухожу, но сиськи - супер!":
                            $ __mood -= 5
                            $ __rel -= 5
                            menu:
                                Lisa_12 "..."
                                "{i}Бежать{/i}":
                                    jump .rel_mood
                "Извини, я не хотел...":
                    $ __mood += 5
                    $ __rel += 5
                    jump .rel_mood

        label .look_window:
            # Max_00 "Кажется, всё самое интересное я уже пропустил..."
            $ spent_time = 10
            $ __ran1 = renpy.random.choice(["03", "04", "05", "06"])

            if __ran1 == "03":
                $ characters["lisa"].dress_inf = "02b"
            elif __ran1 == "04":
                $ characters["lisa"].dress_inf = "02c"
            elif __ran1 == "05":
                $ characters["lisa"].dress_inf = "02f"
            else:
                $ characters["lisa"].dress_inf = "02g"

            scene BG char Lisa voyeur-00
            $ renpy.show("Lisa voyeur "+__ran1)
            $ renpy.show("FG voyeur-lisa-00"+max_profile.dress)
            menu:
                Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
                "{i}уйти{/i}":
                    jump .rel_mood


        scene location house myroom door-morning

        label .rel_mood:
            $ HintRelMood("lisa", __rel, __mood)
            $ characters["lisa"].relmax += __rel
            $ characters["lisa"].mood   += __mood

    jump Waiting


label lisa_dressed_repetitor:
    scene location house myroom door-morning

    if peeping["lisa_dressed"] != 0:
        return

    menu:
        Max_09 "Кажется, Лиза куда-то собирается, но дверь закрыта..."
        "{i}уйти{/i}":
            $ peeping["lisa_dressed"] = 1

    label .end:
        jump Waiting


label lisa_swim:

    scene image "Lisa swim "+pose3_1+characters["lisa"].dress
    return


label lisa_sun:

    scene image "BG char Lisa sun-"+pose3_1
    $ renpy.show("Lisa sun "+pose3_1+characters["lisa"].dress)
    return


label lisa_dishes:
    scene BG crockery-evening-00
    $ renpy.show("Lisa crockery-evening 01"+characters["lisa"].dress)
    return


label lisa_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show("Lisa crockery-closer "+pose3_1+characters["lisa"].dress)
    return


label lisa_phone:

    scene BG char Lisa bed-evening
    $ renpy.show("Lisa phone-evening "+pose3_1+characters["lisa"].dress)
    return


label lisa_bath:
    scene location house bathroom door-evening
    if peeping["lisa_bath"] == 0:
        $ peeping["lisa_bath"] = 1
        $ __mood = 0
        $ __rel = 0
        menu:
            Max_00 "В это время Лиза обычно плескается в ванне..."
            "{i}постучаться{/i}":
                jump .knock
            "{i}открыть дверь{/i}":
                jump .open
            "{i}подглядывать с улицы{/i}":
                scene Lisa bath 01
                $ renpy.show("FG voyeur-bath-00"+max_profile.dress)
                Max_00 "Кажется, Лиза и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но ближе подойти опасно - может заметить..."
                Max_09 "Нужно что-нибудь придумать..."
                jump .end_peeping
            "{i}уйти{/i}":
                jump .end_peeping

        menu .knock:
            Lisa "{b}Лиза:{/b} Кто там? Я принимаю ванну..."
            "Это я, Макс! Можно войти?":
                menu:
                    Lisa "{b}Лиза:{/b} Я же сказала, что в ванне. Закончу, тогда и войдёшь! А пока жди..."
                    "Хорошо, я подожду...":
                        jump .end_peeping
                    "{i}открыть дверь{/i}":
                        jump .open_knock
                    "{i}уйти{/i}":
                        jump .end_peeping
            "{i}открыть дверь{/i}":
                jump .open_knock
            "{i}уйти{/i}":
                jump .end_peeping

        label .open_knock:
            if possibility["seduction"].stage_number < 31:
                $ __mood -= 5
                scene BG bath-open-00
                if characters["lisa"].relmax < 0:
                    show Lisa bath-open 01
                    Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
                elif characters["lisa"].relmax < 250:
                    $ characters["lisa"].dress_inf = "00a"
                    show Lisa bath-open 02
                    Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
                else:
                    $ characters["lisa"].dress_inf = "00a"
                    show Lisa bath-open 03
                    Lisa_11 "Макс! Я же предупредила, что моюсь! Хочешь со мной поссориться?"
                Max_00 "Упс! Уже ушёл..."

                jump .end_peeping
            else:
                Max_00 "В следующих версиях..."
                jump .end_peeping

        label .open:
            if possibility["seduction"].stage_number < 31:
                scene BG bath-open-00
                if characters["lisa"].relmax < 0:
                    show Lisa bath-open 01
                elif characters["lisa"].relmax < 250:
                    $ characters["lisa"].dress_inf = "00a"
                    show Lisa bath-open 02
                else:
                    $ characters["lisa"].dress_inf = "00a"
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

        label .end_peeping:
            $ HintRelMood("lisa", __rel, __mood)
            $ characters["lisa"].relmax += __rel
            $ characters["lisa"].mood   += __mood
            # $ current_room, prev_room = prev_room, current_room
            $ spent_time = 10
            jump Waiting
    return


label lisa_homework:
    scene BG char Lisa lessons
    $ renpy.show("Lisa lessons "+pose3_1+characters["lisa"].dress)
    return
