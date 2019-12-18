

label StartDialog:
    $ renpy.block_rollback()
    if max_profile.energy < 10:
        Max_00 "Я слишком устал. Надо бы вздремнуть..."
        jump AfterWaiting

    if len(current_room.cur_char) == 1:
        if current_room.cur_char[0] == "lisa":
            jump LisaTalkStart
        elif current_room.cur_char[0] == "alice":
            jump AliceTalkStart
        elif current_room.cur_char[0] == "ann":
            jump AnnTalkStart
    jump AfterWaiting


################################################################################
## события Макса

label Sleep:
    $ renpy.block_rollback()
    menu:
        Max_19 "{i}Как же я хочу спать...{/i}"
        "{i}спать до утра{/i}":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ spent_time = 360
            $ status_sleep = True
            $ alarm_time = "08:00"
            jump Waiting # спим 360 минут или до наступления 8 утра


label Wearied:
    $ renpy.block_rollback()
    # прождали все доступное время - спим до восьми
    menu:
        Max_19 "{i}Я без сил и хочу спать...{/i}"
        "{i}спать до утра{/i}":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ current_room = house[0]
            $ status_sleep = True
            $ alarm_time = "08:00"
            jump Waiting


label Nap:
    $ renpy.block_rollback()
    if max_profile.energy > 40.0:
        $ txt = _("{i}Я сейчас не очень хочу спать, но если я хочу сохранить силы...{/i}")
    else:
        $ txt = _("{i}Что-то я сегодня устал, надо бы вздремнуть...{/i}")

    menu:
        Max_19 "[txt!t]"
        "{i}подремать пару часов{/i}":
            $ spent_time = 2 * 60
        "{i}подремать 3 часа{/i}" if tm <= "16:00":
            $ spent_time = 3 * 60
        "{i}подремать 4 часа{/i}" if tm <= "15:00":
            $ spent_time = 4 * 60
        "{i}подремать 5 часов{/i}" if tm <= "14:00":
            $ spent_time = 5 * 60
        "{i}не-а, может позже...{/i}":
            jump AfterWaiting

    $ status_sleep = True
    jump Waiting


label Alarm:
    $ renpy.block_rollback()
    menu:
        Max_00 "{i}В каком часу я должен встать?{/i}"
        # "{i}в 5 утра{/i}":
        #     $ alarm_time = "05:00"
        "{i}в 6 утра{/i}":
            $ alarm_time = "06:00"
        "{i}в 7 утра{/i}":
            $ alarm_time = "07:00"
        "{i}не-а, может позже...{/i}":
            jump AfterWaiting
    $ number_autosave += 1
    $ NewSaveName()
    $ renpy.loadsave.force_autosave(True, True)
    $ spent_time = 420
    $ status_sleep = True
    jump Waiting


label Shower:
    $ renpy.block_rollback()
    scene BG shower-closer
    $ renpy.show("Max shower "+renpy.random.choice(["01", "02", "03"]))
    show FG shower-water

    menu:
        Max_19 "Хорошо быть чистым..."
        "{i}закончить{/i}":
            $ max_profile.cleanness = 100

    $ spent_time = 30
    jump Waiting


label Box:
    $ renpy.block_rollback()
    $ max_profile.energy -= 5.0
    scene Max unbox 01
    Max_08 "Так, мама попросила разобрать коробки. Сейчас глянем, что тут у нас..."
    scene Max unbox 02
    Max_09 "Жаль, но все коробки пустые... Но что это такое? Какая-то камера?"
    scene Max unbox 03
    Max_01 "Тут внутри какая-то инструкция, описание... Да это скрытая камера! Любопытно, зачем она понадобилась отцу?"
    scene Max unbox 04
    menu:
        Max_10 "Может быть, она установлена где-то в доме и за нами кто-то наблюдает?! Нужно будет осмотреть дом...\n\n{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность!\"{/i}{/color}"
        "{i}закончить{/i}":
            pass
        "{i}узнать подробнее о \"Возможностях\"{/i}" if flags["about_poss"]:
            call about_poss from _call_about_poss
    $ possibility["cams"].stage_number = 0
    $ possibility["cams"].stages[0].used = True
    $ AvailableActions["unbox"].enabled = False
    $ AvailableActions["searchcam"].enabled = True
    $ InspectedRooms.clear()
    if CurPoss == "":
        $ CurPoss = "cams"
    $ spent_time = 30
    jump Waiting


label Notebook:
    $ renpy.block_rollback()
    if "06:00" <= tm < "21:00":
        scene BG char Max laptop-day-00
        $ renpy.show("Max laptop-day 01"+dress_suf["max"])
    else:
        scene BG char Max laptop-night-00
        $ renpy.show("Max laptop-night 01"+dress_suf["max"])


    Max_00 "Итак, чем интересным я займусь?"


label Laptop:
    if "06:00" <= tm < "21:00":
        scene BG char Max laptop-day-01
    else:
        scene BG char Max laptop-night-01

    show interface laptop start page:
        xpos 221 ypos 93
        size (1475, 829)

    show video1_movie:
        xpos 221 ypos 93

    $ renpy.block_rollback()

    $ search_theme.clear()

    if possibility["cams"].stage_number == 1:
        $ search_theme.append((_("{i}почитать о камерах{/i}"), "about_cam"))
    if possibility["Blog"].stage_number == 0:
        $ search_theme.append((_("{i}читать о блогах{/i}"), "about_blog"))
    if possibility["secretbook"].stage_number == 1:
        $ search_theme.append((_("{i}узнать о книге Алисы{/i}"), "about_secretbook"))

    call screen LaptopScreen


label nothing_search:
    Max_00 "Сейчас мне нечего искать..."
    jump Laptop

label about_cam:
    Max_09 "Так, любопытно... Эти камеры можно настроить так, чтобы они транслировали изображение в интернет!"
    Max_07 "Но что ещё интереснее, некоторые люди готовы платить за доступ к таким камерам..."
    Max_09 "Может быть, мне сделать свой сайт и пусть люди мне платят за просмотр видео? Но я не умею ничего толком..."
    $ spent_time = 20
    jump Laptop


label SearchCam:
    $ renpy.block_rollback()
    if current_room == house[4]:
        $ FoundCamera = True
        Max_04 "Ого! Вот же она! Кто-то её так хорошо запрятал в стену, что найти камеру можно только точно зная, что ищешь..."
        Max_09 "Так... Но она ни к чему не подключена сейчас. Видимо, отец так следил за ходом строительства и ремонта, а сейчас уже некому следить и не за чем..."
        Max_04 "Но если её подключить, то можно подглядывать и за кое-чем другим. Вот только нужно во всём как следует разобраться!"
        $ random_ab = "b"
        $ AvailableActions["searchcam"].enabled = False
        $ InspectedRooms.clear()
        $ possibility["cams"].stage_number = 1
        $ possibility["cams"].stages[1].used = True
    else:
        Max_14 "Кажется, здесь нет никаких камер... Может быть, стоит поискать в другой комнате?"
        $ InspectedRooms.append(current_room)
    $ spent_time = 30
    $ cur_ratio = 2
    jump Waiting

label DishesWashed:
    $ renpy.block_rollback()
    if tm < "16:00":
        scene BG crockery-morning-00
        $ renpy.show("Max crockery-morning 01"+dress_suf["max"])
    else:
        scene BG crockery-evening-00
        $ renpy.show("Max crockery-evening 01"+dress_suf["max"])
    menu:
        Max_00 "Эх... столько посуды. И почему в этом огромном доме нет маленькой посудомоечной машины?"
        "{i}закончить{/i}":
            pass
    if (day+2) % 7 != 6:
        if (day+2) % 7 == 0:
            $ __name_label = GetScheduleRecord(schedule_alice, day, "10:30").label
        else:
            $ __name_label = GetScheduleRecord(schedule_alice, day, "11:30").label
        if __name_label == "alice_dishes":
            $ characters["alice"].mood += 6
            if characters["alice"].relmax < 400:
                $ HintRelMood("alice", 10, 6)
                $ characters["alice"].relmax += 10
            else:
                $ HintRelMood("alice", 0, 6)
    $ dishes_washed = True
    $ spent_time = max((60 - int(tm[-2:])), 30)
    $ cur_ratio = 2
    jump Waiting


################################################################################
## события Лизы

label lisa_sleep:
    if tm < "06:00":
        scene BG char Lisa bed-night
        $ AvailableActions["touch"].active = True
        $ renpy.show("Lisa sleep-night "+random3_1+dress_suf["lisa-sleepwear"])
    else:
        scene BG char Lisa bed-morning
        $ renpy.show("Lisa sleep-morning "+random3_1+dress_suf["lisa-sleepwear"])
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
        $ renpy.show("FG shower 00"+dress_suf["max"])
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
            $ lisa_dress["naked"] = "00a"
            $ __ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            show image ("Lisa shower-closer 0"+str(__ran1))
            show FG shower-closer
            Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nОх, повезло! Хороша сестренка."
        elif RandomChance(_chance):
            $ peeping["lisa_shower"] = 2
            $ max_profile.stealth += 0.05
            $ renpy.notify(_("Скрытность Макса немного повысилась"))
            $ lisa_dress["naked"] = "00a"
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
    $ renpy.show("Lisa reading "+random3_2+dress_suf["lisa"])
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
        $ __ran1 = renpy.random.choice(["01", "02a", "03", "04"])

        if __ran1 == "01":
            $ lisa_dress["dressed"] = "02d"
        elif __ran1 == "02":
            $ lisa_dress["dressed"] = "02e"
        elif __ran1 == "03":
            $ lisa_dress["dressed"] = "02b"
        else:
            $ lisa_dress["dressed"] = "02c"

        scene image "BG char Lisa voyeur-00"
        $ renpy.show("Lisa voyeur "+__ran1)
        $ renpy.show("FG voyeur-lisa-00"+dress_suf["max"])
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "{i}уйти{/i}":
                jump .end

    label .come_in:
        scene BG char Lisa morning
        if characters["lisa"].relmax < 0:
            show Lisa school-dressed 01
            $ lisa_dress["dressed"] = "01b"
        elif characters["lisa"].relmax < 250:
            show Lisa school-dressed 01a
            $ lisa_dress["dressed"] = "01b"
        elif characters["lisa"].relmax < 700:
            show Lisa school-dressed 01b
            $ lisa_dress["dressed"] = "02a"
        else:
            show Lisa school-dressed 01c # пока отсутствует
            $ lisa_dress["dressed"] = "00"

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
            $ lisa_dress["dressed"] = "02a"
        elif __ran1 == 3:
            $ lisa_dress["dressed"] = "02c"
        elif __ran1 == 4:
            $ lisa_dress["dressed"] = "02b"
        else:
            $ lisa_dress["dressed"] = "00"
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
                $ lisa_dress["dressed"] = "02c"
            elif __ran1 == 4:
                $ lisa_dress["dressed"] = "02b"
            else:
                $ lisa_dress["dressed"] = "00"
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
                $ phrase = _("Я же сказала, что я не одета!")

            menu:
                Lisa_12 "Макс! [phrase!t] Быстрой закрой дверь с той стороны!"
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
            $ __ran1 = renpy.random.choice(["03", "04", "05a", "06a"])

            if __ran1 == "03":
                $ lisa_dress["dressed"] = "02b"
            elif __ran1 == "04":
                $ lisa_dress["dressed"] = "02c"
            elif __ran1 == "05":
                $ lisa_dress["dressed"] = "02f"
            else:
                $ lisa_dress["dressed"] = "02g"

            scene image "Lisa voyeur "+__ran1
            $ renpy.show("FG voyeur-lisa-00"+dress_suf["max"])
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


label lisa_dressed_somewhere:
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

    if int(tm[:2])%3 == 0:
        $ __scene = random3_1
    elif int(tm[:2])%3 == 1:
        $ __scene = random3_2
    else:
        $ __scene = random3_3

    if __scene == "03":
        if swim_suf["lisa"] == "a":
            $ lisa_dress["swim"] = "03a"
        else:
            $ lisa_dress["swim"] = "03c"
    else:
        if swim_suf["lisa"] == "a":
            $ lisa_dress["swim"] = "03"
        else:
            $ lisa_dress["swim"] = "03b"
    scene image "Lisa swim "+__scene+swim_suf["lisa"]
    return


label lisa_sun:

    scene image "BG char Lisa sun-"+random3_2
    $ renpy.show("Lisa sun "+random3_2+swim_suf["lisa"])
    return


label lisa_dishes:
    scene BG crockery-evening-00
    $ renpy.show("Lisa crockery-evening 01"+dress_suf["lisa"])
    return


label lisa_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show("Lisa crockery-closer "+random3_1+dress_suf["lisa"])
    return


label lisa_phone:

    scene BG char Lisa bed-evening
    $ renpy.show("Lisa phone-evening "+random3_3+dress_suf["lisa"])
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
                $ renpy.show("FG voyeur-bath-00"+dress_suf["max"])
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
                    $ lisa_dress["naked"] = "00a"
                    show Lisa bath-open 02
                    Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
                else:
                    $ lisa_dress["naked"] = "00a"
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
                    $ lisa_dress["naked"] = "00a"
                    show Lisa bath-open 02
                else:
                    $ lisa_dress["naked"] = "00a"
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
    $ renpy.show("Lisa lessons "+random3_1+dress_suf["lisa-learn"])
    return


################################################################################
## события Анны

label ann_sleep:
    if tm < "05:00":
        scene location house annroom door-night
    else:
        scene location house annroom door-evening
    if peeping["ann_sleep"] == 0:
        $ peeping["ann_sleep"] = 1
        menu:
            Max_00 "В это время мама обычно спит.\nМне кажется, не стоит её будить..."
            "{i}заглянуть в окно{/i}":
                if tm < "06:00":
                    scene BG char Ann bed-night-01
                    $ renpy.show("Ann sleep-night "+random3_1)
                    $ renpy.show("FG ann-voyeur-night-00"+dress_suf["max"])
                else:
                    scene BG char Ann bed-morning-01
                    $ renpy.show("Ann sleep-morning "+random3_2)
                    $ renpy.show("FG ann-voyeur-morning-00"+dress_suf["max"])
                menu:
                    Max_07 "Какая попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь..."
                    "{i}уйти{/i}":
                        pass
            "{i}уйти{/i}":
                pass
        $ spent_time = 10
        jump Waiting
    return


label ann_shower:
    scene location house bathroom door-morning
    if peeping["ann_shower"] == 3:
        Max_00 "Я уже попался сегодня на подглядывании за мамой. Не стоит злить ее еще больше."
    elif peeping["ann_shower"] == 1:
        Max_00 "Я уже подсматривал сегодня за мамой. Не стоит искушать судьбу слишком часто."
    elif  peeping["ann_shower"] == 2:
        Max_00 "Сегодня мама и так сегодня едва не поймала меня. Не стоит искушать судьбу слишком часто."
    elif peeping["ann_shower"] > 3:
        menu:
            Max_00 "Мама сейчас принимает душ..."
            "{i}уйти{/i}":
                pass
    else:
        $ peeping["ann_shower"] = 4
        menu:
            Max_00 "Похоже, мама принимает душ..."
            "{i}заглянуть с улицы{/i}":
                jump .start_peeping
            "{i}уйти{/i}":
                jump .end_peeping

        label .start_peeping:
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
            scene image ("Ann shower 0"+str(__ran1))
            $ renpy.show("FG shower 00"+dress_suf["max"])
            menu:
                Max_00 "Как же она все-таки красива..."
                "{i}присмотреться\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
                    jump .closer_peepeng
                "{i}уйти{/i}":
                    jump .end_peeping

        label .closer_peepeng:
            if RandomChance(_chance):
                $ peeping["ann_shower"] = 1
                $ max_profile.stealth += 0.1
                $ renpy.notify(_("Скрытность Макса повысилась"))
                $ ann_dress["naked"] = "00a"
                $ __ran1 = renpy.random.randint(1, 6)
                scene BG shower-closer
                show image ("Ann shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color} \nУх, аж завораживает! Хоть бы меня не заметила..."
            elif RandomChance(_chance):
                $ peeping["ann_shower"] = 2
                $ max_profile.stealth += 0.05
                $ renpy.notify(_("Скрытность Макса немного повысилась"))
                $ ann_dress["naked"] = "00a"
                $ __ran1 = renpy.random.randint(7, 8)
                scene BG shower-closer
                show image ("Ann shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_09 "{color=[orange]}{i}Кажется, мама что-то заподозрила!{/i}{/color}\nПора сматываться."
                jump .end_peeping
            else:
                $ peeping["ann_shower"] = 3
                $ max_profile.stealth += 0.02
                $ renpy.notify(_("Скрытность Макса чуть-чуть повысилась"))
                $ __ran1 = renpy.random.choice(["09", "10"])
                scene BG shower-closer
                show image ("Ann shower-closer "+__ran1)
                show FG shower-closer
                menu:
                    Ann_19 "{color=[orange]}{i}Неудалось незаметно подкрасться!{/i}{/color}\nМакс! Подглядываешь за мной? Как тебе не стыдно?!"
                    "{i}Бежать{/i}":
                        jump .end_peeping

        label .end_peeping:
            $ current_room, prev_room = prev_room, current_room
            $ spent_time = 10
            jump Waiting

    return


label ann_yoga:
    scene BG char Ann yoga-00
    if int(tm[3:4])%3 == 0:
        $ renpy.show("Ann yoga "+random3_1)
    elif int(tm[3:4])%3 == 1:
        $ renpy.show("Ann yoga "+random3_2)
    else:
        $ renpy.show("Ann yoga "+random3_3)
    return


label ann_cooking:
    scene BG cooking-00
    $ renpy.show("Ann cooking 01"+random_suf)
    return


label ann_cooking_closer:
    scene BG cooking-01
    $ renpy.show("Ann cooking-closer "+random3_1+random_suf)
    return


label ann_dressed_work:
    scene location house aliceroom door-evening
    if peeping["ann_dressed"] == 0:
        $ peeping["ann_dressed"] = 1
        $ __ran1 = renpy.random.choice(["01", "02", "03", "04"])
        $ __mood = 0
        menu:
            Max_09 "Сейчас 10 часов, а значит, мама собирается на работу..."
            "{i}постучаться{/i}":
                menu:
                    Ann "{b}Анна:{/b} Кто там?"
                    "Это я, Макс. Можно войти?":
                        Ann "{b}Анна:{/b} Макс, я не одета. Собираюсь на работу. Подожди немного, дорогой."
                        Max_00 "Хорошо, мам"
                    "{i}уйти{/i}":
                        pass
            "{i}открыть дверь{/i}":
                scene BG char Ann morning
                $ renpy.show("Ann dressed-work "+__ran1)
                if __ran1 == "01":
                    $ ann_dress["dressed"] = "02"
                elif __ran1 == "02":
                    $ ann_dress["dressed"] = "02b"
                elif __ran1 == "03":
                    $ ann_dress["dressed"] = "02a"
                else:
                    $ ann_dress["dressed"] = "00"
                menu:
                    Ann_13 "Макс! Я же учила тебя стучаться!"
                    "Хорошо выглядишь, мам!":
                        $ __mood += 3
                        Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?"
                        Max_00 "Конечно, мам!"
                    "Отличный зад!":
                        $ __mood -= 3
                        Ann_19 "Что?! Макс! А ну-ка быстро выйди и закрой дверь!"
                        Max_00 "Как скажешь, мам..."
                    "Ой, извини. Я забыл...":
                        $ __mood -= 1
                        Ann_07 "Ну, бывает. Я сама ещё не привыкла к тому, что замков нигде нет. Ладно, дорогой. Подожди за дверью, пока мама одевается. хорошо?"
                        Max_00 "Хорошо, мам..."
                $ HintRelMood("ann", 0, __mood)
                # $ characters["ann"].relmax += __rel
                $ characters["ann"].mood   += __mood
            "{i}заглянуть в окно{/i}":
                if __ran1 == "01":
                    $ ann_dress["dressed"] = "02c"
                elif __ran1 == "02":
                    $ ann_dress["dressed"] = "02d"
                elif __ran1 == "03":
                    $ ann_dress["dressed"] = "02a"
                else:
                    $ ann_dress["dressed"] = "02b"

                scene image "Ann voyeur "+__ran1
                $ renpy.show("FG voyeur-morning-00"+dress_suf["max"])
                Max_01 "Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но пора уходить, а то вдруг увидит меня в зеркало!"
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label ann_dressed_shop:
    scene location house aliceroom door-evening
    if peeping["ann_dressed"] == 0:
        $ peeping["ann_dressed"] = 1
        $ __ran1 = renpy.random.choice(["01", "02", "03", "04"])
        $ __mood = 0
        menu:
            Max_09 "Сегодня суббота, день шоппинга. Видимо, мама собирается..."
            "{i}постучаться{/i}":
                menu:
                    Ann "{b}Анна:{/b} Кто там?"
                    "Это я, Макс. Можно войти?":
                        Ann "{b}Анна:{/b} Нет, Макс. Я переодеваюсь. Подожди немного, дорогой."
                        Max_00 "Хорошо, мам"
                    "{i}уйти{/i}":
                        pass
            "{i}открыть дверь{/i}":
                scene BG char Ann morning
                $ renpy.show("Ann dressed-work "+__ran1)
                menu:
                    Ann_13 "Макс! Я же учила тебя стучаться!"
                    "Хорошо выглядишь, мам!":
                        $ __mood += 3
                        Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?"
                        Max_00 "Конечно, мам!"
                    "Ой, извини...":
                        Ann_07 "И Макс... Постарайся больше не входить без стука, хорошо?"
                        Max_00 "Хорошо, мам..."
                $ HintRelMood("ann", 0, __mood)
                # $ characters["ann"].relmax += __rel
                $ characters["ann"].mood   += __mood
            # "{i}заглянуть в окно{/i}":
            #     # if __ran1 == "01":
            #     #     $ lisa_dress["dressed"] = "02d"
            #     # else:
            #     #     $ lisa_dress["dressed"] = "02c"
            #
            #     scene image "Ann voyeur "+__ran1
            #     $ renpy.show("FG voyeur-morning-00"+dress_suf["max"])
            #     Max_01 "Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но если заметит меня в зеркало, мне конец."
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label ann_resting:
    if tm <= "14:00":
        scene BG char Ann relax-morning-01
        $ renpy.show("Ann relax-morning "+random3_3+"a")
    elif tm <= "19:00":
        scene BG char Ann relax-morning-01
        $ renpy.show("Ann relax-morning "+random3_3+"b")
    else:
        scene BG char Ann relax-evening-01
        $ renpy.show("Ann relax-evening "+random3_3+random_ab)
    return


label ann_read:
    scene BG reading
    if tm < "14:00":
        $ renpy.show("Ann reading "+random3_2+"a")
    else:
        $ renpy.show("Ann reading "+random3_3+"b")
    return


label ann_swim:
    if int(tm[:2])%3 == 0:
        $ __scene = random3_1
    elif int(tm[:2])%3 == 1:
        $ __scene = random3_2
    else:
        $ __scene = random3_3

    if __scene == "03":
        $ ann_dress["swim"] = "03a"
    else:
        $ ann_dress["swim"] = "03"

    scene image "Ann swim "+__scene+swim_suf["ann"]
    return


label ann_sun:
    scene BG char Ann sun
    if int(tm[:2])%3 == 0:
        $ renpy.show("Ann sun "+random3_1)
    elif int(tm[:2])%3 == 1:
        $ renpy.show("Ann sun "+random3_2)
    else:
        $ renpy.show("Ann sun "+random3_3)
    return


label ann_bath:
    scene location house bathroom door-evening
    if peeping["ann_bath"] == 0:
        $ peeping["ann_bath"] = 1
        menu:
            Max_00 "Видимо, мама принимает ванну..."
            "{i}постучаться{/i}":
                menu:
                    Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
                    "Это я, Макс.":
                        menu:
                            Ann "{b}Анна:{/b} Дорогой, что ты хотел?"
                            "Можно я войду?":
                                $ config.menu_include_disabled = True
                                menu:
                                    Ann "{b}Анна:{/b} Ну... хорошо, входи. Только не смотри!"
                                    "{i}Войти{/i} \n(в следующей версии...)" if False: ## пока нет изображений
                                        menu:
                                            Ann_01 "Макс, так что там у тебя такое срочное, что ты не мог подождать пол часа?"
                                            "Просто, я соскучился!":
                                                Ann_07 "Макс! Я думала, что-то случилось, а ты просто балуешься. Подожди меня за дверью. Я скоро!"
                                                Max_00 "Хорошо..."
                                                jump .end
                                            "Ну это, хотел поглазеть...":
                                                Ann_13 "Что?! А ну-ка быстро выметайся отсюда! Я скоро закончу."
                                                Max_00 "Как скажешь!"
                                                jump .end
                                            "Я собирался спать и хотел принять душ перед сном":
                                                ###############################
                                                pass
                                            "Ой, не буду тебе мешать":
                                                jump .end
                                    "Ой, нет, я передумал":
                                        jump .end
                            "Нет, ничего":
                                pass
                            "Я подожду...":
                                pass
                        Ann "{b}Анна:{/b} Хорошо, я скоро закончу..."
                        Max_00 "Ага..."
                    "{i}уйти{/i}":
                        pass
            "{i}подглядывать с улицы{/i}":
                scene Ann bath 01
                $ renpy.show("FG voyeur-bath-00"+dress_suf["max"])
                Max_00 "Эх... жаль, что стекло частично матовое. Так ничего не разглядеть! А если подобраться ближе, то мама может заметить..."
                menu:
                    Max_09 "Нужно что-нибудь придумать..."
                    "{i}уйти{/i}":
                        pass
            "{i}уйти{/i}":
                pass
        label .end:
            $ config.menu_include_disabled = False
            # $ current_room, prev_room = prev_room, current_room
            $ spent_time = 10
            jump Waiting
    return


label ann_tv:
    scene BG lounge-tv-00
    $ renpy.show("Ann tv "+random3_3)
    return

label ann_tv_closer:
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer"+random3_3)
    return


################################################################################
## события Алисы

label alice_bath:
    scene location house bathroom door-evening
    if peeping["alice_bath"] == 0:
        $ peeping["alice_bath"] = 1
        menu:
            Max_00 "Если полночь, значит Алиса отмокает в ванне... Входить без стука - опасно для жизни."
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кому там не спится? Я ванну набираю..."
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Макс, ты глухой? Я же сказала, буду в ванне плескаться. Жди как минимум час!"
                        Max_00 "Ладно, ладно..."
                    "{i}уйти{/i}":
                        pass
            "{i}подглядывать с улицы{/i}":
                scene Alice bath 01
                $ renpy.show("FG voyeur-bath-00"+dress_suf["max"])
                Max_00 "Кажется, Алиса и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но подходить ближе опасно - может заметить..."
                menu:
                    Max_09 "Нужно что-нибудь придумать..."
                    "{i}уйти{/i}":
                        pass
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label alice_sleep:
    if tm < "06:00":
        scene location house aliceroom door-night
    else:
        scene location house aliceroom door-evening
    if peeping["alice_sleep"] == 0:
        $ peeping["alice_sleep"] = 1
        menu:
            Max_00 "Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья..."
            "{i}заглянуть в окно{/i}":
                $ spent_time = 10
                if tm < "06:00":
                    scene BG char Alice bed-night-01
                    $ renpy.show("Alice sleep-night "+random3_1)
                    $ renpy.show("FG alice-voyeur-night-00"+dress_suf["max"])
                else:
                    scene BG char Alice bed-morning-01
                    $ renpy.show("Alice sleep-morning "+random3_2)
                    $ renpy.show("FG alice-voyeur-morning-00"+dress_suf["max"])
                menu:
                    Max_07 "О, да! Моя старшая сестренка выглядит потрясающе... \nНа изгибы ее тела в этом полупрозрачном белье хочется смотреть вечно!"
                    "{i}прокрасться в комнату{/i}":
                        $ spent_time += 10
                        if tm < "06:00":
                            scene BG char Alice bed-night-02
                            $ renpy.show("Alice sleep-night-closer "+random3_1)
                        else:
                            scene BG char Alice bed-morning-02
                            $ renpy.show("Alice sleep-morning-closer "+random3_2)
                        menu:
                            Max_07 "Класс! Так бы и прилег рядышком, но пора уходить... Если она проснется, мне точно не поздоровится..."
                            "{i}уйти{/i}":
                                pass
                    "{i}уйти{/i}":
                        pass
            "{i}уйти{/i}":
                pass
        jump Waiting
    return


label alice_shower:
    scene location house bathroom door-morning
    if peeping["alice_shower"] == 3:
        Max_00 "Алиса меня уже поймала сегодня. Не стоит злить ее еще больше, а то точно что-нибудь оторвет."
    elif peeping["alice_shower"] == 1:
        Max_00 "Я уже подсматривал сегодня за Алисой. Не стоит искушать судьбу слишком часто."
    elif  peeping["alice_shower"] == 2:
        Max_00 "Алиса меня и так сегодня едва не поймала. Не стоит искушать судьбу слишком часто."
    elif peeping["alice_shower"] > 3:
        menu:
            Max_00 "Алиса сейчас принимает душ..."
            "{i}уйти{/i}":
                pass
    else:
        $ peeping["alice_shower"] = 4
        menu:
            Max_00 "Похоже, Алиса принимает душ..."
            "{i}заглянуть с улицы{/i}":
                jump .start_peeping
            "{i}уйти{/i}":
                jump .end_peeping

        label .start_peeping:
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
            scene image ("Alice shower 0"+str(__ran1))
            $ renpy.show("FG shower 00"+dress_suf["max"])
            menu:
                Max_00 "Ого... Голая Алиса всего в паре метров от меня!"
                "{i}присмотреться\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
                    jump .closer_peepeng
                "{i}уйти{/i}":
                    jump .end_peeping

        label .closer_peepeng:
            if RandomChance(_chance):
                $ peeping["alice_shower"] = 1
                $ max_profile.stealth += 0.1
                $ renpy.notify(_("Скрытность Макса повысилась"))
                $ alice_dress["naked"] = "00aa"
                $ __ran1 = renpy.random.randint(1, 6)
                scene BG shower-closer
                show image ("Alice shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color} \nМожно целую вечность смотреть, как сестренка принимает душ. Лишь бы она меня не заметила..."
            elif RandomChance(_chance):
                $ peeping["alice_shower"] = 2
                $ max_profile.stealth += 0.05
                $ renpy.notify(_("Скрытность Макса немного повысилась"))
                $ alice_dress["naked"] = "00aa"
                $ __ran1 = renpy.random.randint(7, 8)
                scene BG shower-closer
                show image ("Alice shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_09 "{color=[orange]}{i}Кажется, Алиса что-то заподозрила!{/i}{/color}\nПора сматываться."
                jump .end_peeping
            else:
                $ peeping["Alice_shower"] = 3
                $ max_profile.stealth += 0.02
                $ renpy.notify(_("Скрытность Макса чуть-чуть повысилась"))
                $ __ran1 = renpy.random.choice(["09", "10"])
                scene BG shower-closer
                show image ("Alice shower-closer "+__ran1)
                show FG shower-closer
                menu:
                    Alice_12 "{color=[orange]}{i}Неудалось незаметно подкрасться!{/i}{/color}\nМакс!!! Ты за мной подглядываешь?! Ты труп! Твоё счастье, что я сейчас голая. Но ничего, я маме всё расскажу, она тебя накажет!"
                    "{i}Бежать{/i}":
                        jump .end_peeping

        label .end_peeping:
            $ current_room, prev_room = prev_room, current_room
            $ spent_time = 10
            jump Waiting
    return


label alice_rest_morning:

    scene BG char Alice morning
    $ renpy.show("Alice morning 01"+dress_suf["alice"])
    return


label alice_rest_evening:
    scene BG char Alice evening
    $ renpy.show("Alice evening 01"+dress_suf["alice"])
    return


label alice_dressed_shop:

    scene location house aliceroom door-evening
    if peeping["alice_dressed"] == 0:
        $ peeping["alice_dressed"] = 1
        menu:
            Max_09 "Кажется, все собираются на шоппинг и Алиса сейчас переодевается..."
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кто там? Я переодеваюсь!"
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Даже не вздумай! Прибью на месте! Жди там. А лучше свали подальше, чтобы под дверью не сопел тут."
                        Max_00 "Хорошо..."
                    "Хорошо, я подожду...":
                        pass
            "{i}заглянуть в окно{/i}":
                $ __ran1 = renpy.random.choice(["01", "02"])

                if __ran1 == "01":
                    $ alice_dress["dressed"] = "02a"
                else:
                    $ alice_dress["dressed"] = "02b"

                scene image "Alice voyeur "+__ran1
                $ renpy.show("FG voyeur-morning-00"+dress_suf["max"])
                Max_01 "Алиса переодевается... Какой вид! Так. Пора сваливать. Вдруг, кто-то заметит!"
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label alice_dishes:
    scene BG crockery-morning-00
    $ renpy.show("Alice crockery-morning 01"+dress_suf["alice"])
    return


label alice_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show("Alice crockery-closer "+random3_1+dress_suf["alice"])
    return


label alice_read:
    scene BG reading
    if int(tm[:2])%3 == 0:
        $ renpy.show("Alice reading "+random3_1+dress_suf["alice"])
    elif int(tm[:2])%3 == 1:
        $ renpy.show("Alice reading "+random3_2+dress_suf["alice"])
    else:
        $ renpy.show("Alice reading "+random3_3+dress_suf["alice"])
    return


label alice_dressed_somewhere:
    scene location house aliceroom door-evening
    if peeping["alice_dressed"] == 0:
        $ peeping["alice_dressed"] = 1
        menu:
            Max_09 "Кажется, Алиса куда-то собирается..."
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кто там? Я переодеваюсь!"
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Даже не вздумай! Прибью на месте! Жди там. А лучше свали подальше, чтобы под дверью не сопел тут."
                        Max_00 "Хорошо..."
                    "Хорошо, я подожду...":
                        pass
            "{i}заглянуть в окно{/i}":
                $ __ran1 = renpy.random.choice(["01", "02"])

                # if __ran1 == "01":
                #     $ lisa_dress["dressed"] = "02d"
                # else:
                #     $ lisa_dress["dressed"] = "02c"

                scene image "Alice voyeur "+__ran1
                $ renpy.show("FG voyeur-morning-00"+dress_suf["max"])
                Max_01 "Алиса переодевается... Какой вид! Так. Пора сваливать. Вдруг, кто-то заметит!"
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label alice_sun:
    scene BG char Alice sun
    if int(tm[:2])%3 == 0:
        $ renpy.show("Alice sun "+random2_1+swim_suf["alice"])
    elif int(tm[:2])%3 == 1:
        $ renpy.show("Alice sun "+random2_2+swim_suf["alice"])
    else:
        $ renpy.show("Alice sun "+random2_3+swim_suf["alice"])
    return


label alice_swim:
    if int(tm[:2])%3 == 0:
        $ __scene = random3_1
    elif int(tm[:2])%3 == 1:
        $ __scene = random3_2
    else:
        $ __scene = random3_3

    if __scene == "03":
        $ alice_dress["swim"] = "03a"
    else:
        $ alice_dress["swim"] = "03"

    scene image "Alice swim "+__scene+swim_suf["alice"]
    return


label alice_cooking_dinner:
    scene BG cooking-00
    $ renpy.show("Alice cooking 01"+dress_suf["alice"])
    return


label alice_cooking_closer:
    scene BG cooking-01
    $ renpy.show("Alice cooking-closer "+random3_2+dress_suf["alice"])
    return


label alice_tv:
    scene BG lounge-tv-00
    if int(tm[:2])%2 == 0:
        $ renpy.show("Alice tv "+random3_1+dress_suf["alice"])
    else:
        $ renpy.show("Alice tv "+random3_3+dress_suf["alice"])
    return


label alice_tv_closer:
    scene BG lounge-tv-01
    if int(tm[:2])%2 == 0:
        $ renpy.show("Alice tv-closer "+random3_1+dress_suf["alice"])
    else:
        $ renpy.show("Alice tv-closer "+random3_3+dress_suf["alice"])
    return


label alice_morning_closer:
    scene BG char Alice morning-closer
    if int(tm[:2])%3 == 0:
        $ renpy.show("Alice morning-closer "+random3_1+dress_suf["alice"])
    elif int(tm[:2])%3 == 1:
        $ renpy.show("Alice morning-closer "+random3_2+dress_suf["alice"])
    else:
        $ renpy.show("Alice morning-closer "+random3_3+dress_suf["alice"])

    return


label alice_evening_closer:
    scene BG char Alice evening-closer
    if int(tm[:2])%3 == 0:
        $ renpy.show("Alice evening-closer "+random3_2+dress_suf["alice"])
    elif int(tm[:2])%3 == 1:
        $ renpy.show("Alice evening-closer "+random3_1+dress_suf["alice"])
    else:
        $ renpy.show("Alice evening-closer "+random3_3+dress_suf["alice"])
    return
