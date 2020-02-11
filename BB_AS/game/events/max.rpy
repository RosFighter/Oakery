label StartDialog:
    $ renpy.block_rollback()
    if mgg.energy < 10:
        Max_10 "Я чувствую себя слишком уставшим для этого. Было бы неплохо сначала вздремнуть и набраться сил..."
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
    scene BG char Max bed-night-01
    $ renpy.show("Max sleep-night "+pose3_3)
    menu:
        Max_00 "{i}Пожалуй, пора ложиться спать...{/i}"
        "{i}спать до утра{/i}":
            Max_19 "Как же в этом доме хорошо..."
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
    scene BG char Max bed-night-01
    $ renpy.show("Max sleep-night "+pose3_1)
    menu:
        Max_10 "{i}Моя голова уже совсем не соображает, нужно ложиться спать...{/i}"
        "{i}спать до утра{/i}":
            Max_19 "Как же в этом доме хорошо..."
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ current_room = house[0]
            $ status_sleep = True
            $ alarm_time = "08:00"
            jump Waiting


label LittleEnergy:
    $ renpy.block_rollback()
    if "11:00" < tm <= "19:00":
        scene BG char Max bed-day-01
    else:
        scene BG char Max bed-night-01
    menu:
        Max_10 "{i}Я слишком вымотался, нужно хоть немного вздремнуть...{/i}"
        "{i}вздремнуть{/i}":
            if "11:00" < tm <= "19:00":
                $ renpy.show("Max nap "+pose3_1+mgg.dress)
            else:
                $ renpy.show("Max sleep-night "+pose3_1)
            Max_19 "Как же в этом доме хорошо..."
            $ number_autosave += 1
            $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ current_room = house[0]

            if "11:00" < tm <= "19:00":
                $ alarm_time = "19:00"
            else:
                $ alarm_time = "06:00"
            $ spent_time = 600
            $ status_sleep = True
            jump Waiting


label Nap:
    $ renpy.block_rollback()
    scene BG char Max bed-day-01
    if mgg.energy > 40.0:
        $ txt = _("{i}Я сейчас не очень хочу спать, но немного вздремнуть лишним не будет...{/i}")
    else:
        $ txt = _("{i}Ох и вымотался же я сегодня, надо немного вздремнуть...{/i}")

    menu:
        Max_00 "[txt!t]"
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

    $ renpy.show("Max nap "+pose3_1+mgg.dress)
    Max_19 "Как же в этом доме хорошо..."
    $ status_sleep = True
    jump Waiting


label Alarm:
    $ renpy.block_rollback()
    scene BG char Max bed-night-01
    menu:
        Max_00 "{i}В каком часу мне будет лучше проснуться?{/i}"
        # "{i}в 5 утра{/i}":
        #     $ alarm_time = "05:00"
        "{i}в 6 утра{/i}":
            $ alarm_time = "06:00"
        "{i}в 7 утра{/i}":
            $ alarm_time = "07:00"
        "{i}не-а, может позже...{/i}":
            jump AfterWaiting
    $ renpy.show("Max sleep-night "+pose3_2)
    Max_19 "Как же в этом доме хорошо..."
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
        Max_19 "Всё-таки чистым быть намного лучше. Хотя не всегда хочется..."
        "{i}закончить{/i}":
            $ mgg.cleanness = 100

    if "ladder" in flags and flags["ladder"] == 1:
        scene BG char Max shower-window-01
        Max_03 "Ага! Я только сейчас обратил внимание на то, что здесь есть ещё заднее окно! И, как мне кажется, через него на ванну откроется просто шикарный вид... Конечно же дело не в самой ванне, а в том, кто будет её принимать."
        Max_09 "Только вот расположено оно высоковато... Нужно достать что-то, с чего будет удобно подглядывать и что не вызовет, в случае чего, подозрений..."
        Max_01 "Возможно подойдёт лестница, а ещё лучше стремянка. О да, пожалуй, это будет то, что нужно!"
        $ items["ladder"].InShop = True
        $ flags["ladder"] = 2

    $ spent_time = 30
    jump Waiting


label Bath:
    $ renpy.block_rollback()
    scene BG char Max bath-00
    $ renpy.show("Max bath "+pose3_2)

    menu:
        Max_19 "Всё-таки чистым быть намного лучше. Хотя не всегда хочется..."
        "{i}закончить{/i}":
            $ mgg.cleanness = 100

    if "ladder" in flags and flags["ladder"] == 1:
        scene BG char Max bath-window-01
        Max_03 "Ага! Я только сейчас обратил внимание на то, что здесь есть ещё заднее окно! И, как мне кажется, через него на ванну откроется просто шикарный вид... Конечно же дело не в самой ванне, а в том, кто будет её принимать."
        Max_09 "Только вот расположено оно высоковато... Нужно достать что-то, с чего будет удобно подглядывать и что не вызовет, в случае чего, подозрений..."
        Max_01 "Возможно подойдёт лестница, а ещё лучше стремянка. О да, пожалуй, это будет то, что нужно!"
        $ items["ladder"].InShop = True
        $ flags["ladder"] = 2

    $ spent_time = 30
    jump Waiting


label Box:
    $ renpy.block_rollback()
    $ mgg.energy -= 5.0
    scene Max unbox 01
    Max_08 "Так, мама попросила разобрать коробки. Сейчас глянем, что тут у нас..."
    scene Max unbox 02
    Max_09 "Жаль, но все коробки пустые... Но что это такое? Какая-то камера?"
    scene Max unbox 03
    Max_01 "Тут внутри какая-то инструкция, описание... Да это скрытая камера! Любопытно, зачем она понадобилась отцу?"
    scene Max unbox 04
    $ SetPossStage("cams", 0)
    menu:
        Max_10 "Может быть, она установлена где-то в доме и за нами кто-то наблюдает?! Нужно будет осмотреть дом..."
        "{i}закончить{/i}":
            pass
        "{i}узнать подробнее о \"Возможностях\"{/i}" if flags["about_poss"]:
            call about_poss from _call_about_poss
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
        $ renpy.show("Max laptop-day 01"+mgg.dress)
    else:
        scene BG char Max laptop-night-00
        $ renpy.show("Max laptop-night 01"+mgg.dress)

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

    if possibility["cams"].stn == 1:
        $ search_theme.append((_("{i}почитать о камерах{/i}"), "about_cam"))
    if possibility["blog"].stn == 0:
        $ search_theme.append((_("{i}читать о блогах{/i}"), "about_blog"))
    if possibility["secretbook"].stn == 1:
        $ search_theme.append((_("{i}узнать о книге Алисы{/i}"), "about_secretbook"))

    call screen LaptopScreen


label LaptopShop:
    if "06:00" <= tm < "21:00":
        scene BG char Max laptop-day-01
    else:
        scene BG char Max laptop-night-01
    show interface laptop e-shop:
        xpos 221 ypos 93
        # size (1475, 829)

    $ renpy.block_rollback()
    call screen OnlineShop


label nothing_search:
    Max_00 "Сейчас мне нечего искать..."
    jump Laptop


label buyfood:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop grocery-1:
        xpos 221 ypos 93
    Max_04 "Так... Посмотрим список продуктов... Ага. Сейчас всё закажем..."
    Max_04 "Готово. Да это же самая лёгкая задача!"
    $ spent_time = 50
    $ dcv["buyfood"].stage = 2
    $ dcv["buyfood"].lost = 2
    $ money -= 50
    jump Laptop


label courses_start:
    ## временно отсутствует
    jump Laptop


label create_site:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop cam-inf-2:
        xpos 221 ypos 93
    menu:
        Max_00 "Итак, пришло время заняться своим сайтом. Для начала нужно купить домен, хостинг, шаблон дизайна и оплатить услуги стримингового сервиса. На всё в сумме нужно $100"
        "Оплатить всё ($100)":
            pass
        "В другой раз...":
            jump Laptop
    show interface laptop cam-inf-3:
        xpos 221 ypos 93
    menu:
        Max_04 "Отлично! Теперь у меня есть свой сайт и домен! Осталось только соединить поток данных от камеры со стриминговым сервисом..."
        "Настроить работу сайта":
            pass
    show interface laptop cam-inf-4:
        xpos 221 ypos 93
    Max_04 "Да! Всё работает! Теперь люди смогут заходить на мой сайт и смотреть шоу. Конечно, если они каким-то образом узнают про мой сайт... Ладно, подумаю ещё что можно сделать..."
    $ spent_time = 60
    $ SetPossStage("cams", 4)
    $ money -= 100
    $ items["hide_cam"].InShop = True
    $ house[4].cams.append(HideCam())
    $ house[4].cams[0].grow = 100

    jump Waiting


label open_site:
    if "06:00" <= tm < "21:00":
        scene BG char Max laptop-day-01
    else:
        scene BG char Max laptop-night-01
    show interface laptop CoverBBCams:
        xpos 221 ypos 93

    $ renpy.block_rollback()
    call screen MySite


label about_cam:
    hide video1_movie
    show interface laptop cam-inf-1:
        xpos 221 ypos 93
        size (1475, 829)
    Max_09 "Так, любопытно... Эти камеры можно настроить так, чтобы они транслировали изображение в интернет!"
    Max_07 "Но что ещё интереснее, некоторые люди готовы платить за доступ к таким камерам..."
    Max_09 "Может быть, мне сделать свой сайт и пусть люди мне платят за просмотр видео? Но я не умею ничего толком..."
    $ items["manual"].InShop = True
    $ renpy.notify(_("В интернет-магазине доступен новый товар."))
    $ spent_time += 20
    $ SetPossStage("cams", 2)
    jump Laptop


label SearchCam:
    $ renpy.block_rollback()
    if current_room == house[4]:
        scene Max cam
        $ FoundCamera = True
        Max_04 "Ого! Вот же она! Кто-то её так хорошо запрятал в стену, что найти камеру можно только точно зная, что ищешь..."
        Max_09 "Так... Но она ни к чему не подключена сейчас. Видимо, отец так следил за ходом строительства и ремонта, а сейчас уже некому следить и не за чем..."
        Max_04 "Но если её подключить, то можно подглядывать и за кое-чем другим. Вот только нужно во всём как следует разобраться!"
        $ random_loc_ab = "b"
        $ AvailableActions["searchcam"].enabled = False
        $ InspectedRooms.clear()
        $ SetPossStage("cams", 1)
    else:
        Max_14 "Кажется, здесь нет никаких камер... Может быть, стоит поискать в другой комнате?"
        $ InspectedRooms.append(current_room)
    $ spent_time = 30
    $ cur_ratio = 2
    jump Waiting


label ClearPool:
    $ renpy.block_rollback()
    scene BG char Max cleeningpool-00
    $ renpy.show("Max cleaning-pool 01"+mgg.dress)
    Max_11 "Эх... Не лёгкая это работа, но нужно отработать те деньги, что мама уже заплатила..."
    $ dcv["clearpool"].stage = 2
    $ dcv["clearpool"].lost = 6
    $ spent_time = 60
    $ cur_ratio = 2.5
    jump Waiting


label DishesWashed:
    $ renpy.block_rollback()
    if tm < "16:00":
        scene BG crockery-morning-00
        $ renpy.show("Max crockery-morning 01"+mgg.dress)
    else:
        scene BG crockery-evening-00
        $ renpy.show("Max crockery-evening 01"+mgg.dress)
    menu:
        Max_00 "Эх... столько посуды. И почему в этом огромном доме нет маленькой посудомоечной машины?"
        "{i}закончить{/i}":
            pass
    if (day+2) % 7 != 6:
        if (day+2) % 7 == 0:
            $ __name_label = GetPlan(plan_alice, day, "10:30").label
        else:
            $ __name_label = GetPlan(plan_alice, day, "11:30").label
        if __name_label == "alice_dishes":
            if GetRelMax("alice")[0] < 3:
                $ AddRelMood("alice", 10, 60)
            else:
                $ AddRelMood("alice", 0, 60)
    $ dishes_washed = True
    $ spent_time = max((60 - int(tm[-2:])), 50)
    $ cur_ratio = 2
    jump Waiting


label delivery:
    $ renpy.block_rollback()

    $ __StrDev = GetDeliveryString() # сформируем строку накладной

    scene BG NoImage
    "Здравствуйте! По этому адресу на сегодня назначена доставка. Распишитесь?"
    Max_00 "Конечно! А что тут?"
    $ renpy.say("", __StrDev)
    Max_00 "Да, то что нужно. Спасибо!"
    $ current_room = house[6]

    $ DeletingDeliveryTempVar() # удалим временные переменные и очистим список доставки
    jump AfterWaiting


label BookRead:
    scene BG char Max reading-00
    $ renpy.show("Max reading 01"+mgg.dress)
    menu:
        Max_00 "Пришло время почитать что-то..."
        "{i}читать \"WEB STANDARDS\"{/i}" if items["manual"].have and items["manual"].read < 5:
            jump .manual

    label .manual:
        $ items["manual"].read += 1
        if items["manual"].read < 2:
            Max_00 "Хм... куча непонятных слов. Кажется, нужно будет заново перечитать первые главы...\n\n{color=[orange]}{i}(Книга изучена на 20%%){/i}{/color}"
        elif items["manual"].read < 3:
            Max_00 "Так, ну с этим я уже разобрался, хорошо... А это что такое? Не ясно. Нужно будет всё осмыслить...\n\n{color=[orange]}{i}(Книга изучена на 40%%){/i}{/color}"
        elif items["manual"].read < 4:
            Max_00 "Ого, вот это здорово! Уже можно делать сайт? А, нет... Ещё не всё понятно... Ну, разберусь в другой раз.\n\n{color=[orange]}{i}(Книга изучена на 60%%){/i}{/color}"
        elif items["manual"].read < 5:
            Max_00 "Так, ну теперь картина вырисовывается. Осталось разобраться только с мелочами... Или это не мелочи?\n\n{color=[orange]}{i}(Книга изучена на 80%%){/i}{/color}"
        else:
            Max_00 "Всё, вот теперь точно всё понятно! Я уже могу сделать свой сайт и транслировать на него изображение! Но как получать за это деньги?"
            $ SetPossStage("cams", 3)
            $ items["manual"].InShop = False
            jump .end

    label .end:
        $ cooldown["learn"] = CooldownTime("04:00") # час на этап чтения и 3 часа кулдаун
        $ spent_time = 60
        $ cur_ratio = 0.6
        jump Waiting


label SearchSecretBook:

    menu:
        Max_10 "Так... И с чего начать поиск? И нужно поспешить: если Алиса меня поймает, то сначала убьёт, а только потом поздоровается..."
        "{i}искать под подушкой{/i}":
            jump .pillow
        "{i}искать под кроватью{/i}":
            jump .bed
        "{i}искать в шкафу{/i}":
            jump .wardrobe
        "{i}искать в столе{/i}":
            jump .table
        "{i}прекратить поиски{/i}":
            jump Waiting

    label .pillow:
        $ spent_time += 10
        menu:
            Max_14 "Нет, здесь её нет... Ну где же эта чёртова книга? Шаги? Нет, показалось..."
            "{i}искать под кроватью{/i}":
                jump .bed
            "{i}искать в шкафу{/i}":
                jump .wardrobe
            "{i}искать в столе{/i}":
                jump .table
            "{i}прекратить поиски{/i}":
                jump Waiting

    label .bed:
        $ spent_time += 10
        menu:
            Max_14 "Нет, тут её точно нет. Ну где же она? Кажется, я слышу шум..."
            "{i}искать под подушкой{/i}":
                jump .pillow
            "{i}искать в шкафу{/i}":
                jump .wardrobe
            "{i}искать в столе{/i}":
                jump .table
            "{i}прекратить поиски{/i}":
                jump Waiting


    label .table:
        $ spent_time += 10
        menu:
            Max_14 "Может быть, её здесь нет? Или попытаться ещё поискать, на свой страх и риск?"
            "{i}искать под подушкой{/i}":
                jump .pillow
            "{i}искать под кроватью{/i}":
                jump .bed
            "{i}искать в шкафу{/i}":
                jump .wardrobe
            "{i}искать в столе{/i}":
                jump .table
            "{i}прекратить поиски{/i}":
                jump Waiting

    label .wardrobe:
        $ spent_time += 10
        scene BG char Max secretbook-00
        Max_04 "Вот же она! И зачем её так прятать? Любопытная обложка. Запомню-ка я название. Интересно, о чём эта книга? Может быть, погуглить? Так, всё, надо уходить..."
        $ SetPossStage("secretbook", 1)
        $ AvailableActions["searchbook"].enabled = False
        jump Waiting


label about_secretbook:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop secretbook-inf-1:
        xpos 221 ypos 93
    menu:
        Max_00 "Так... Сейчас погуглим. Как там она называлась? \"Sugar Daddies\"?... Любовный роман? И что в нём такого может быть?"
        "{i}читать о книге{/i}":
            Max_06 "Ого! Да это не простой любовный роман... Это же эротика. Да ещё какая! Теперь понятно, почему Алиса не хотела рассказывать, что читает..."
    $ items["erobook_1"].InShop = True
    $ items["erobook_2"].InShop = True
    $ items["erobook_3"].InShop = True
    $ items["erobook_4"].InShop = True
    $ items["erobook_5"].InShop = True
    $ renpy.notify(_("В интернет-магазине доступен новый товар."))
    $ SetPossStage("secretbook", 2)
    $ spent_time += 30
    jump Laptop


label InstallCam:
    if current_location != house:
        jump AfterWaiting

    if GetKolCams(house) < 7 and len(current_room.cams) > 0:
        Max_00 "Здесь уже есть камера. Пожалуй, стоит установить ее в другом месте."
        jump AfterWaiting

    if current_room == house[0]:
        menu:
            Max_04 "{i}В этой комнате столько всего может происходить... Думаю, зрителям понравится! Главное - спрятать все провода, чтобы Лиза не заметила новую микро-камеру...{/i}"
            "{i}закончить{/i}":
                $ house[0].cams.append(HideCam())
                $ house[0].cams[0].grow = 100
    elif current_room == house[1]:
        menu:
            Max_04 "{i}Пусть зрители посмотрят, чем Алиса занимается в своей комнате, когда её не видят... Я бы и сам был бы рад посмотреть, но пока такой функции у меня нет...{/i}"
            "{i}закончить{/i}":
                $ house[1].cams.append(HideCam())
                $ house[1].cams[0].grow = 100
    elif current_room == house[2]:
        menu:
            Max_04 "{i}Конечно, здесь редко происходят события. Зато, когда они происходят, то здесь такое... Думаю, зрители будут рады таким моментам...{/i}"
            "{i}закончить{/i}":
                $ house[2].cams.append(HideCam())
                $ house[2].cams[0].grow = 100
    elif current_room == house[3]:
        menu:
            Max_04 "{i}Конечно, с точки зрения морали ставить камеру в ванной сомнительно. Однако, тут и так окно во всю стену. Так что, формально я лишь приоткрыл это окно...{/i}"
            "{i}закончить{/i}":
                $ house[3].cams.append(HideCam())
                $ house[3].cams[0].grow = 100
    elif current_room == house[5]:
        menu:
            Max_04 "{i}Уж не знаю, будет ли какой-то толк от этой камеры... Тут так редко что-то происходит... Ну пусть будет. Раз уж взялся всё подключать...{/i}"
            "{i}закончить{/i}":
                $ house[5].cams.append(HideCam())
                $ house[5].cams[0].grow = 100
    elif current_room == house[6]:
        if len(current_room.cams) > 0:
            menu:
                Max_04 "{i}Вот теперь зрители смогут насладится всеми мокрыми и блестящими красотами, происходящими во дворе...{/i}"
                "{i}закончить{/i}":
                    $ house[6].cams.append(HideCam())
                    $ house[6].cams[1].grow = 100
        else:
            menu:
                Max_04 "{i}Двор... Тут почти всё время кто-то есть и что-то делает, пока светит солнце. Думаю, тут зрители будут зависать постоянно в надежде увидеть кого-то с голыми сиськами...{/i}"
                "{i}закончить{/i}":
                    Max_09 "{i}Пожалуй, из-за большой площади мне стоило бы установить здесь несколько камер, чтобы зрители смогли лучше разглядеть каждую попку, которая тут бывает...{/i}"
                    $ house[6].cams.append(HideCam())
                    $ house[6].cams[0].grow = 100

    $ items["hide_cam"].have = False
    $ cur_ratio = 1.5
    $ spent_time = 30
    jump Waiting
