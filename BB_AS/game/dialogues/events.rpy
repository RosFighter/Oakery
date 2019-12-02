
################################################################################
## события Макса

label Sleep:
    menu:
        Max_19 "Как же я хочу спать..."

        "Спать до утра":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            call Waiting(360, 1, True, "08:00") from _call_Waiting # спим 360 минут или до наступления 8 утра

    return


label StartDialog:

    if len(current_room.cur_char) == 1:
        if current_room.cur_char[0] == "lisa":
            jump LisaTalkStart
        elif current_room.cur_char[0] == "alice":
            jump AliceTalkStart
        elif current_room.cur_char[0] == "ann":
            jump AnnTalkStart

    jump AfterWaiting


label Wearied:
    # прождали все доступное время - спим до восьми
    menu:
        Max_19 "Я без сил и хочу спать..."

        "Спать до утра":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ current_room = house[0]
            call Waiting(270, 1, True, "08:00") from _call_Waiting_1

    return


label Nap:
    if max_profile.energy > 40.0:
        $ txt = _("Я сейчас не очень хочу спать, но если я хочу сохранить силы...")
    else:
        $ txt = _("Что-то я сегодня устал, надо бы вздремнуть...")

    menu:
        Max_19 "[txt!t]"

        "Подремать пару часов":
            $ t = 2 * 60
        "Подремать 3 часа" if tm <= "16:00":
            $ t = 3 * 60
        "Подремать 4 часа" if tm <= "15:00":
            $ t = 4 * 60
        "Подремать 5 часов" if tm <= "14:00":
            $ t = 5 * 60
        "Не-а, может позже...":
            jump AfterWaiting

    call Waiting(t, 1, True) from _call_Waiting_5
    return


label Alarm:

    menu:
        Max_00 "В каком часу я должен встать?"

        "В 5 утра":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ t = TimeDifference(tm, "05:00")
            call Waiting(t, 1, True, "05:00") from _call_Waiting_6
        "В 6 утра":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ t = TimeDifference(tm, "06:00")
            call Waiting(t, 1, True, "06:00") from _call_Waiting_7
        "В 7 утра":
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ t = TimeDifference(tm, "07:00")
            call Waiting(t, 1, True, "07:00") from _call_Waiting_8
        "Не-а, может позже...":
            jump AfterWaiting
    return


label Box:
    $ max_profile.energy -= 5.0
    scene Max unbox 01
    # в оригинале 15, временно ставлю 8
    Max_08 "Так, мама попросила разобрать коробки. Сейчас глянем, что тут у нас..."
    scene Max unbox 02
    Max_09 "Жаль, но все коробки пустые... Но что это такое? Какая-то камера?"
    scene Max unbox 03
    Max_01 "Тут внутри какая-то инструкция, описание... Да это скрытая камера! Любопытно, зачем она понадобилась отцу?"
    scene Max unbox 04
    menu:
        Max_10 "Может быть, она установлена где-то в доме и за нами кто-то наблюдает?! Нужно будет осмотреть дом...\n\n{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность!\"{/i}{/color}"
        "закончить":
            pass
        "узнать подробнее о \"Возможностях\"" if flags["about_poss"]:
            call about_poss from _call_about_poss

    $ possibility["cams"].stage_number = 0
    $ possibility["cams"].stages[0].used = True
    $ AvailableActions["unbox"].enabled = False
    $ AvailableActions["searchcam"].enabled = True
    $ InspectedRooms.clear()
    if CurPoss == "":
        $ CurPoss = "cams"

    call Waiting(30) from _call_Waiting_2


label SearchCam:

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
        call Waiting(30, 2.0) from _call_Waiting_3
    else:
        Max_14 "Кажется, здесь нет никаких камер... Может быть, стоит поискать в другой комнате?"
        $ InspectedRooms.append(current_room)
        call Waiting(60, 2.0) from _call_Waiting_4


label DishesWashed:
    scene Max crockery-01
    menu:
        Max_00 "Эх... столько посуды. И почему в этом огромном доме нет маленькой посудомоечной машины?"
        "закончить":
            pass
    if (day+2) % 7 != 6:
        if (day+2) % 7 == 0:
            $ __name_label = GetScheduleRecord(schedule_alice, day, "10:30")[0].label
        else:
            $ __name_label = GetScheduleRecord(schedule_alice, day, "11:30")[0].label
        if __name_label == "alice_dishes":
            $ characters["alice"].mood += 6
            if characters["alice"].relmax < 400:
                $ HintRelMood("alice", 10, 6)
                $ characters["alice"].relmax += 10
            else:
                $ HintRelMood("alice", 0, 6)

    $ dishes_washed = True

    call Waiting(60, 2) from _call_Waiting_11


################################################################################
## события Лизы

label lisa_sleep:
    $ AvailableActions["talk"].enabled = False

    if tm < "06:00":
        scene BG char Lisa bed-night
        $ AvailableActions["touch"].active = True
        show image "Lisa sleep-night "+random3_1+dress_suf["lisa-sleepwear"]
    else:
        scene BG char Lisa bed-morning
        show image "Lisa sleep-morning "+random3_1+dress_suf["lisa-sleepwear"]
    return


label lisa_shower:
    scene location house bathroom door-morning
    if peeping["lisa_shower"] > 3:
        menu:
            Max_00 "Лиза сейчас принимает душ..."
            "Уйти":
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
        menu:
            Max_09 "Кажется, Лиза что-то делает в ванной..."
            "Постучаться":
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
                    "Уйти":
                        $ peeping["lisa_shower"] = 4
                        jump .end_peeping
            "Заглянуть с улицы":
                jump .start_peeping
            "Уйти":
                $ peeping["lisa_shower"] = 4
                jump .end_peeping

    label .start_peeping:
        $ peeping["lisa_shower"] = 1
        $ renpy.notify(_("Скрытность Макса капельку повысилась"))
        $ max_profile.stealth += 0.01
        $ _ran1 = renpy.random.randint(1, 4)

        $ _chance = GetChance(max_profile.stealth, 3)
        $ __chance_vis = int(round(_chance))
        if __chance_vis < 33:
            $ _chance_color = red
        elif __chance_vis > 67:
            $ _chance_color = lime
        else:
            $ _chance_color = orange
        scene image ("Lisa shower 0"+str(_ran1))
        show image "shower fg 00"+dress_suf["max"]
        menu:
            Max_04 "Лиза принимает душ"
            "Присмотреться\n{color=[_chance_color]}(Скрытность. Шанс: [__chance_vis]\%){/color}":
                jump .closer_peepeng
            "Уйти":
                jump .end_peeping

    label .closer_peepeng:
        if RandomChance(_chance):
            $ peeping["lisa_shower"] = 1
            $ max_profile.stealth += 0.1
            $ renpy.notify(_("Скрытность Макса повысилась"))
            $ lisa_dress["naked"] = "00a"
            $ _ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            show image ("Lisa shower-closer 0"+str(_ran1))
            show shower-closer_fg
            Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nОх, повезло! Хороша сестренка."
        elif RandomChance(_chance):
            $ peeping["lisa_shower"] = 2
            $ max_profile.stealth += 0.05
            $ renpy.notify(_("Скрытность Макса немного повысилась"))
            $ lisa_dress["naked"] = "00a"
            $ _ran1 = renpy.random.randint(7, 8)
            scene BG shower-closer
            show image ("Lisa shower-closer 0"+str(_ran1))
            show shower-closer_fg
            Max_09 "{color=[orange]}{i}Кажется, Лиза что-то заподозрила!{/i}{/color}\nПора сматываться."
            jump .end_peeping
        else:
            $ peeping["lisa_shower"] = 3
            $ max_profile.stealth += 0.02
            $ renpy.notify(_("Скрытность Макса чуть-чуть повысилась"))
            $ _ran1 = renpy.random.choice(["09", "10"])
            scene BG shower-closer
            show image ("Lisa shower-closer "+_ran1)
            show shower-closer_fg
            menu:
                Lisa_12 "{color=[orange]}{i}Неудалось незаметно подкрасться!{/i}{/color}\nМакс!!! Ты за мной подглядываешь?! Я всё маме расскажу!!!"
                "Уйти":
                    jump .end_peeping
    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        call Waiting(10) from _call_Waiting_10
    label .end_peeping2:
        $ current_room, prev_room = prev_room, current_room
        jump AfterWaiting
    return


label lisa_read:

    if tm < "11:00":
        scene BG char Lisa bed-morning
        show image "Lisa reading-morning "+random3_2+dress_suf["lisa"]
    else: ## временно. спрайты будут заменены по готовности
        scene BG char Lisa bed-evening
        show image "Lisa reading-morning "+random3_2+dress_suf["lisa"]
    return


label lisa_dressed_school:
    scene location house myroom door-morning

    $ __mood = 0
    $ __rel = 0
    if peeping["lisa_dressed"] == 0:
        $ peeping["lisa_dressed"] = 1
        $ __wait = 60 - int(tm.split(":")[1])
        jump .lisa_dressed
    else:
        jump .end

    menu .lisa_dressed:
        Max_09 "{i}Похоже, Лиза собирается в школу...{/i}"
        "постучаться" if characters["lisa"].mindedness < 200:
            menu:
                "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
                "Это я, Макс. Можно войти?":
                    jump .come_in
                "Хорошо, я подожду...":
                    $ __wait = 10
                    jump .rel_mood
        "открыть дверь" if characters["lisa"].mindedness < 200:
            jump .open_door
        "заглянуть в окно"  if characters["lisa"].mindedness < 200:
            jump .look_window
        #"войти в комнату" if characters["lisa"].mindedness >= 200:
        #    pass
        "уйти":
            $ __wait = 10
            jump .rel_mood

    label .look_window:
        $ __wait = 10
        $ __ran1 = renpy.random.choice(["01", "02", "03", "04"])

        if __ran1 == "01":
            $ lisa_dress["dressed"] = "02d"
        elif __ran1 == "02":
            $ lisa_dress["dressed"] = "02e"
        elif __ran1 == "03":
            $ lisa_dress["dressed"] = "02b"
        else:
            $ lisa_dress["dressed"] = "02c"

        scene image "Lisa window "+__ran1
        show image "FG lisa-window-00"+dress_suf["max"]
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "уйти":
                jump .rel_mood


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
        $ __wait = 20
        $ __ran1 = renpy.random.randint(2, 5)
        if __ran1 == 2:
            $ lisa_dress["dressed"] = "01b"
        elif __ran1 == 3:
            $ lisa_dress["dressed"] = "02c"
        elif __ran1 == 4:
            $ lisa_dress["dressed"] = "02b"
        else:
            $ lisa_dress["dressed"] = "00"
        scene BG char Lisa morning
        if characters["lisa"].relmax < 0:
            show image "Lisa school-dressed 0"+str(__ran1)
        elif characters["lisa"].relmax < 250:
            show image "Lisa school-dressed 0"+str(__ran1)+"a"
        elif characters["lisa"].relmax < 700:
            show image "Lisa school-dressed 0"+str(__ran1)+"b"
        else:
            show image "Lisa school-dressed 0"+str(__ran1)+"c" # пока отсутствует

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
                                "Бежать":
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

    call Waiting(__wait) from _call_Waiting_17

    label .end:
        return


label lisa_dressed_shop:
    scene location house myroom door-morning

    $ __mood = 0
    $ __rel = 0
    $ __warned = False
    if peeping["lisa_dressed"] == 0:
        $ peeping["lisa_dressed"] = 1
        $ __wait = 60 - int(tm.split(":")[1])
        jump .lisa_dressed
    else:
        jump .end

    menu .lisa_dressed:
        Max_09 "Кажется, все собираются на шоппинг и Лиза сейчас переодевается..."
        "постучаться":
            jump .knock
        "открыть дверь":
            jump .open_door
        "заглянуть в окно":
            jump .look_window

    menu .knock:
        Lisa "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
        "Это я, Макс. Можно войти?":
            menu:
                Lisa "{b}Лиза:{/b} Нет, Макс, нельзя! Я переодеваюсь. Жди там."
                "открыть дверь":
                    $ __warned = True
                    jump .open_door
                "Хорошо...":
                    jump .rel_mood
        "Хорошо, я подожду...":
            jump .rel_mood

    label .open_door:
        $ __wait = 20
        $ __ran1 = renpy.random.randint(3, 5)
        if __ran1 == 3:
            $ lisa_dress["dressed"] = "02c"
        elif __ran1 == 4:
            $ lisa_dress["dressed"] = "02b"
        else:
            $ lisa_dress["dressed"] = "00"
        scene BG char Lisa morning
        if characters["lisa"].relmax < 0:
            show image "Lisa school-dressed 0"+str(__ran1)
        elif characters["lisa"].relmax < 250:
            show image "Lisa school-dressed 0"+str(__ran1)+"a"
        elif characters["lisa"].relmax < 700:
            show image "Lisa school-dressed 0"+str(__ran1)+"b"
        else:
            show image "Lisa school-dressed 0"+str(__ran1)+"c" # пока отсутствует

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
                            "Бежать":
                                jump .rel_mood
            "Извини, я не хотел...":
                $ __mood += 5
                $ __rel += 5
                jump .rel_mood

    label .look_window:
        # Max_00 "Кажется, всё самое интересное я уже пропустил..."
        $ __wait = 10
        $ __ran1 = renpy.random.choice(["03", "04", "05", "06"])

        if __ran1 == "03":
            $ lisa_dress["dressed"] = "02b"
        elif __ran1 == "04":
            $ lisa_dress["dressed"] = "02c"
        elif __ran1 == "05":
            $ lisa_dress["dressed"] = "02f"
        else:
            $ lisa_dress["dressed"] = "02g"

        scene image "Lisa window "+__ran1
        show image "FG lisa-window-00"+dress_suf["max"]
        menu:
            Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
            "уйти":
                jump .rel_mood


    scene location house myroom door-morning

    label .rel_mood:
        $ HintRelMood("lisa", __rel, __mood)
        $ characters["lisa"].relmax += __rel
        $ characters["lisa"].mood   += __mood

    call Waiting(__wait) from _call_Waiting_18

    label .end:
        return


label lisa_dressed_somewhere:
    scene location house myroom door-morning

    if peeping["lisa_dressed"] != 0:
        jump .end

    menu:
        Max_09 "Кажется, Лиза куда-то собирается, но дверь закрыта..."
        "уйти":
            $ peeping["lisa_dressed"] = 1

    label .end:
        return


label lisa_swim:

    scene image "Lisa swim "+random3_1+swim_suf["lisa"]
    return


label lisa_sun:

    scene image "BG char Lisa sun-"+random3_2
    show image "Lisa sun "+random3_2+swim_suf["lisa"]
    return


label lisa_dishes:

    scene BG crockery-evening-00
    show image "Lisa crockery-evening 01"+dress_suf["lisa"]
    return


label lisa_phone:

    scene BG char Lisa bed-evening
    show image "Lisa phone-evening "+random3_3
    return


label lisa_bath:
    scene location house bathroom door-evening
    ## диалог

    return


label lisa_homework:
    scene BG char Lisa lessons
    show image "Lisa lessons "+random3_1+dress_suf["lisa-learn"]
    return


################################################################################
## события Анны

label ann_shower:
    scene location house bathroom door-morning
    if peeping["ann_shower"] == 2:
        Max_00 "Я уже попался сегодня на подглядывании за мамой. Не стоит злить ее еще больше."
        jump .end_peeping
    elif peeping["ann_shower"] == 1:
        Max_00 "Я уже подсматривал сегодня за мамой. Не стоит искушать судьбу слишком часто."
        jump .end_peeping
    elif peeping["ann_shower"] == 3:
        menu:
            Max_00 "Мама сейчас принимает душ..."
            "Уйти":
                jump .end_peeping
    else:
        $ peeping["ann_shower"] = 1
        menu:
            Max_00 "Похоже, мама принимает душ..."
            "Заглянуть с улицы":
                jump .start_peeping
            "Уйти":
                jump .end_peeping

    label .start_peeping:
        $ renpy.notify(_("Скрытность Макса капельку повысилась"))
        $ max_profile.stealth += 0.01
        $ __ran1 = renpy.random.randint(1, 4)
        scene image ("Ann shower 0"+str(__ran1))
        show image "shower fg 00"+dress_suf["max"]
        menu:
            Max_00 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nУх, аж завораживает! Хоть бы меня не заметила..."
            "Уйти":
                jump .end_peeping

    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        call Waiting(10)


################################################################################
## события Алисы

label alice_bath:
    scene location house bathroom door-evening
    ## диалог

    return


label alice_sleep:

    if tm < "05:00":
        scene location house aliceroom door-night
    else:
        scene location house aliceroom door-evening

    ## диалог


    return


label alice_shower:
    scene location house bathroom door-morning
    if peeping["alice_shower"] == 2:
        Max_00 "Алиса меня уже поймала сегодня. Не стоит злить ее еще больше, а то точно что-нибудь оторвет."
        jump .end_peeping
    elif peeping["alice_shower"] == 1:
        Max_00 "Я уже подсматривал сегодня за Алисой. Не стоит искушать судьбу слишком часто."
        jump .end_peeping
    elif peeping["alice_shower"] == 3:
        menu:
            Max_00 "Алиса сейчас принимает душ..."
            "Уйти":
                jump .end_peeping
    else:
        $ peeping["alice_shower"] = 1
        menu:
            Max_00 "Похоже, Алиса принимает душ..."
            "Заглянуть с улицы":
                jump .start_peeping
            "Уйти":
                jump .end_peeping

    label .start_peeping:
        $ renpy.notify(_("Скрытность Макса капельку повысилась"))
        $ max_profile.stealth += 0.01
        $ __ran1 = renpy.random.randint(1, 4)
        scene image ("Alice shower 0"+str(__ran1))
        show image "shower fg 00"+dress_suf["max"]
        menu:
            Max_00 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nМожно целую вечность смотреть, как сестренка принимает душ. Лишь бы она меня не заметила..."
            "Уйти":
                jump .end_peeping

    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        call Waiting(10)


label alice_resting:

    # if tm < "19:00"
    scene BG char Alice morning
    show image "Alice morning 01"+dress_suf["alice"]

    return


label alice_dressed_shop:

    scene location house aliceroom door-evening

    return


label alice_dishes:
    scene BG crockery-morning-00
    show image "Alice crockery-morning 01"+dress_suf["alice"]

    return


label alice_read:
    scene BG char Alice reading
    if tm[:2] == "10":
        show image "Alice reading "+random3_2+dress_suf["alice"]
    elif tm[:2] == "11":
        show image "Alice reading "+random3_1+dress_suf["alice"]
    elif tm[:2] == "16":
        show image "Alice reading "+random3_3+dress_suf["alice"]
    elif tm[:2] == "17":
        show image "Alice reading "+random3_2+dress_suf["alice"]
    else:
        show image "Alice reading "+random3_1+dress_suf["alice"]

    return


label alice_dressed_somewhere:
    scene location house aliceroom door-evening

    return


label alice_sun:
    scene BG char Alice sun
    if tm[:2] == "12":
        show image "Alice sun "+random2_1+swim_suf["alice"]
    elif tm[:2] == "15":
        show image "Alice sun "+random2_2+swim_suf["alice"]
    else:
        show image "Alice sun "+random2_3+swim_suf["alice"]
    return


label alice_swim:
    if tm[:2] == "13":
        scene image "Alice swim "+random3_3+swim_suf["alice"]
    elif tm[:2] == "14":
        scene image "Alice swim "+random3_1+swim_suf["alice"]
    else:
        scene image "Alice swim "+random3_2+swim_suf["alice"]
    return


label alice_cooking_dinner:
    scene BG cooking-00
    show image "Alice cooking 01"+dress_suf["alice"]
    return


label alice_tv:
    scene BG lounge-tv-00
    if tm[:2] == "22":
        show image "Alice tv "+random3_1
    else:
        show image "Alice tv "+random3_2
    return
