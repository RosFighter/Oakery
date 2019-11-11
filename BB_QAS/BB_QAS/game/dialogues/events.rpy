
label Sleep:
    menu:
        Max_19 "Как же я хочу спать..."

        "Спать до утра":
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
        Max_19 "Как же я хочу спать..."

        "Спать до утра":
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
            $ t = TimeDifference(tm, "05:00")
            call Waiting(t, 1, True, "05:00") from _call_Waiting_6
        "В 6 утра":
            $ t = TimeDifference(tm, "06:00")
            call Waiting(t, 1, True, "06:00") from _call_Waiting_7
        "В 7 утра":
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
        "узнать подробнее о \"Возможностях\"":
            pass

    $ AvailableActions["unbox"].enabled = False
    $ AvailableActions["searchcam"].enabled = True
    $ InspectedRooms.clear()
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
    $ dishes_washed = True
    if (day+2) % 7 != 6:
        if (day+2) % 7 == 0:
            $ __name_label = GetScheduleRecord(schedule_alice, day, "10:30")[0].label
        else:
            $ __name_label = GetScheduleRecord(schedule_alice, day, "11:30")[0].label
        if __name_label == "alice_dishes":
            $ characters["alice"].mood += 6
            if characters["alice"].relmax < 400:
                $ characters["alice"].relmax += 10

    call Waiting(60, 2)

label lisa_sleep:
    $ AvailableActions["talk"].enabled = False

    if tm < "06:00":
        scene BG char Lisa bed-night
        $ AvailableActions["touch"].active = True
        show image "Lisa sleep-night "+random3_1
    else:
        scene BG char Lisa bed-morning
        show image "Lisa sleep-morning "+random3_1
    return


label lisa_read:
    $ AvailableActions["talk"].enabled = True

    if tm < "11:00":
        scene BG char Lisa bed-morning
        show image "Lisa reading-morning "+random3_2
    else:
        pass
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
        show water fg
        show shower fg
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
            $ lisa_dress["naked"] = "00a"
            $ _ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            show image ("Lisa shower-closer 0"+str(_ran1))
            show shower-closer_fg
            Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nОх, повезло! Хороша сестренка."
        elif RandomChance(_chance):
            $ peeping["lisa_shower"] = 2
            $ max_profile.stealth += 0.05
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


label lisa_dressed_school:
    scene location house myroom door-morning

    if peeping["lisa_dressed"] == 0:
        menu:
            Max_09 "{i}Похоже, Лиза собирается в школу...{/i}"
            "постучаться":
                pass
            "открыть дверь":
                pass
            "заглянуть в окно":
                if 0 < (day+2) % 7 < 6:
                    $ __ran1 = renpy.random.choice(["01", "02", "03", "04"])
                else:
                    $ __ran1 = renpy.random.choice(["03", "04", "05", "06"])
                scene image "Lisa window "+__ran1
                show FG lisa-window
                menu:
                    Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
                    "уйти":
                        $ peeping["lisa_dressed"] = 1
                        call Waiting(10)
            "войти в комнату":
                pass
            "уйти":
                $ peeping["lisa_dressed"] = 1
                call Waiting(10)
    return



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
        menu:
            Max_00 "Похоже, мама принимает душ..."
            "Заглянуть с улицы":
                jump .start_peeping
            "Уйти":
                $ peeping["ann_shower"] = 3
                jump .end_peeping

    label .start_peeping:
        $ __ran1 = renpy.random.randint(1, 4)
        scene image ("Ann shower 0"+str(__ran1))
        show water fg
        show shower fg
        menu:
            Max_00 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color}\nУх, аж завораживает! Хоть бы меня не заметила..."
            "Уйти":
                $ peeping["ann_shower"] = 1
                jump .end_peeping

    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        call Waiting(10) from _call_Waiting_9
