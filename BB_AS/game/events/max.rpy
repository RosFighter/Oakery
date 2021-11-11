label StartDialog:
    $ renpy.block_rollback()
    if mgg.energy < 10:
        Max_10 "{m}Я чувствую себя слишком уставшим для этого. Было бы неплохо сначала вздремнуть и набраться сил...{/m}"
        jump AfterWaiting

    if len(current_room.cur_char) == 1:
        if current_room.cur_char[0] == 'lisa':
            jump LisaTalkStart
        elif current_room.cur_char[0] == 'alice':
            jump AliceTalkStart
        elif current_room.cur_char[0] == 'ann':
            jump AnnTalkStart
        elif current_room.cur_char[0] == 'kira':
            jump KiraTalkStart
        elif current_room.cur_char[0] == 'eric':
            jump EricTalkStart
    elif len(current_room.cur_char) == 2:
        if sorted(current_room.cur_char) == sorted(['lisa', 'olivia']):
            jump OliviaTalkStart

    jump AfterWaiting


################################################################################
## события Макса

label Sleep:
    $ renpy.block_rollback()
    scene BG char Max bed-night-01
    menu:
        Max_00 "{m}Пожалуй, пора ложиться спать...{/m}"
        "{i}установить будильник{/i}" if mgg.energy>40:
            menu:
                Max_00 "{m}В каком часу мне будет лучше проснуться?{/m}"
                "{i}в 6 утра{/i}":
                    $ alarm_time = '06:00'
                "{i}в 7 утра{/i}":
                    $ alarm_time = '07:00'

        "{i}спать до утра{/i}":
            $ alarm_time = '08:00'
    $ renpy.show('Max sleep-night '+pose3_3)
    $ renpy.show('FG Max sleep-night '+pose3_3)

    call bedtime_thoughts from _call_bedtime_thoughts

    Max_19 "{m}Как же в этом доме хорошо...{/m}"

    $ number_autosave += 1
    $ current_room = house[0]
    $ renpy.loadsave.force_autosave(True, True)
    $ spent_time = 360
    $ status_sleep = True
    jump Waiting # спим 360 минут или до наступления 8 утра


label Wearied:
    $ renpy.block_rollback()
    # прождали все доступное время - спим до восьми
    scene BG char Max bed-night-01
    $ renpy.show('Max sleep-night '+pose3_1)
    $ renpy.show('FG Max sleep-night '+pose3_1)
    menu:
        Max_10 "{m}Моя голова уже совсем не соображает, нужно ложиться спать...{/m}"
        "{i}спать до утра{/i}":
            Max_19 "{m}Как же в этом доме хорошо...{/m}"
            $ alarm_time = '08:00'

    $ spent_time = 360
    $ number_autosave += 1
    $ renpy.loadsave.force_autosave(True, True)
    $ current_room = house[0]
    $ status_sleep = True
    jump Waiting


label LittleEnergy:
    $ renpy.block_rollback()
    if '11:00' < tm <= '19:00':
        scene BG char Max bed-mde-01
    else:
        scene BG char Max bed-night-01
    menu:
        Max_10 "{m}Я слишком вымотался, нужно хоть немного вздремнуть...{/m}"
        "{i}вздремнуть{/i}":
            if '11:00' < tm <= '19:00':
                $ renpy.show('Max nap '+pose3_1+mgg.dress)
            else:
                $ renpy.show('Max sleep-night '+pose3_1)
                $ renpy.show('FG Max sleep-night '+pose3_1)
                call bedtime_thoughts from _call_bedtime_thoughts_1

            Max_19 "{m}Как же в этом доме хорошо...{/m}"
            $ number_autosave += 1
            # $ NewSaveName()
            $ renpy.loadsave.force_autosave(True, True)
            $ current_room = house[0]

            if '11:00' < tm <= '19:00':
                $ alarm_time = '19:00'
            else:
                $ alarm_time = '06:00'
            $ spent_time = 600
            $ status_sleep = True

            jump Waiting


label Nap:
    $ renpy.block_rollback()
    scene BG char Max bed-mde-01
    if mgg.energy > 40.0:
        $ txt = _("{m}Я сейчас не очень хочу спать, но немного вздремнуть лишним не будет...{/m}")
    else:
        $ txt = _("{m}Ох и вымотался же я сегодня, надо немного вздремнуть...{/m}")

    menu:
        Max_00 "[txt!t]"
        "{i}подремать пару часов{/i}":
            $ spent_time = 2 * 60
        "{i}подремать 3 часа{/i}" if tm <= '16:00':
            $ spent_time = 3 * 60
        "{i}подремать 4 часа{/i}" if tm <= '15:00':
            $ spent_time = 4 * 60
        "{i}подремать 5 часов{/i}" if tm <= '14:00':
            $ spent_time = 5 * 60
        "{i}не-а, может позже...{/i}":
            jump AfterWaiting

    $ renpy.show('Max nap ' + pose3_1)
    $ renpy.show('FG Max nap ' + pose3_1 + mgg.dress)
    Max_19 "{m}Как же в этом доме хорошо...{/m}"
    $ status_sleep = True
    jump Waiting


label Alarm:
    $ renpy.block_rollback()
    scene BG char Max bed-night-01
    menu:
        Max_00 "{m}В каком часу мне будет лучше проснуться?{/m}"
        "{i}в 6 утра{/i}":
            $ alarm_time = '06:00'
        "{i}в 7 утра{/i}":
            $ alarm_time = '07:00'
        "{i}не-а, может позже...{/i}":
            jump AfterWaiting
    $ renpy.show('Max sleep-night '+pose3_2)
    $ renpy.show('FG Max sleep-night '+pose3_2)

    call bedtime_thoughts from _call_bedtime_thoughts_2

    Max_19 "{m}Как же в этом доме хорошо...{/m}"
    $ number_autosave += 1
    $ renpy.loadsave.force_autosave(True, True)
    $ spent_time = 420
    $ status_sleep = True
    jump Waiting


label Shower:
    $ renpy.block_rollback()
    scene BG shower-closer
    $ renpy.show('Max shower '+renpy.random.choice(['01', '02', '03']))
    show FG shower-water

    menu:
        Max_19 "{m}Всё-таки чистым быть намного лучше. Хотя не всегда хочется...{/m}"
        "{i}закончить{/i}":
            $ mgg.cleanness = 100

    if flags.ladder == 1:
        scene BG char Max shower-window-01
        Max_03 "{m}Ага! Я только сейчас обратил внимание на то, что здесь есть ещё заднее окно! И, как мне кажется, через него на ванну откроется просто шикарный вид... Конечно же дело не в самой ванне, а в том, кто будет её принимать.{/m}"
        Max_09 "{m}Только вот расположено оно высоковато... Нужно достать что-то, с чего будет удобно подглядывать и что не вызовет, в случае чего, подозрений...{/m}"
        Max_01 "{m}Возможно подойдёт лестница, а ещё лучше стремянка. О да, пожалуй, это будет то, что нужно!{/m}"
        $ items['ladder'].unblock()
        $ flags.ladder = 2
        $ notify_list.append(_("В интернет-магазине доступен новый товар."))

    $ spent_time = 30
    jump Waiting


label Bath:
    $ renpy.block_rollback()
    scene BG char Max bath-00
    $ renpy.show('Max bath '+pose3_2)

    menu:
        Max_19 "{m}Всё-таки чистым быть намного лучше. Хотя не всегда хочется...{/m}"
        "{i}закончить{/i}":
            $ mgg.cleanness = 100

    if flags.ladder == 1:
        scene BG char Max bath-window-01
        Max_03 "{m}Ага! Я только сейчас обратил внимание на то, что здесь есть ещё заднее окно! И, как мне кажется, через него на ванну откроется просто шикарный вид... Конечно же дело не в самой ванне, а в том, кто будет её принимать.{/m}"
        Max_09 "{m}Только вот расположено оно высоковато... Нужно достать что-то, с чего будет удобно подглядывать и что не вызовет, в случае чего, подозрений...{/m}"
        Max_01 "{m}Возможно подойдёт лестница, а ещё лучше стремянка. О да, пожалуй, это будет то, что нужно!{/m}"
        $ items['ladder'].unblock()
        $ flags.ladder = 2
        $ notify_list.append(_("В интернет-магазине доступен новый товар."))

    $ spent_time = 30
    jump Waiting


label Box:
    $ renpy.block_rollback()
    $ mgg.energy -= 5.0
    scene Max unbox 01
    Max_08 "{m}Так, мама попросила разобрать коробки. Сейчас глянем, что тут у нас...{/m}"
    scene Max unbox 02
    Max_09 "{m}Жаль, но все коробки пустые... Но что это такое? Какая-то камера?{/m}"
    scene Max unbox 03
    Max_01 "{m}Тут внутри какая-то инструкция, описание... Да это скрытая камера! Любопытно, зачем она понадобилась отцу?{/m}"
    scene Max unbox 04
    $ poss['cams'].open(0)
    menu:
        Max_10 "{m}Может быть, она установлена где-то в доме и за нами кто-то наблюдает?! Нужно будет осмотреть дом...{/m}"
        "{i}закончить{/i}":
            pass
        "{i}узнать подробнее о \"Возможностях\"{/i}" if sum([1 if sum(poss[ps].stages) else 0 for ps in poss_dict]) < 2:
            call about_poss from _call_about_poss
    $ AvailableActions['unbox'].enabled = False
    $ AvailableActions['searchcam'].enabled = True
    $ InspectedRooms.clear()
    if CurPoss == '':
        $ CurPoss = 'cams'
    $ spent_time = 30
    jump Waiting


label Notebook:
    $ view_cam = None
    if current_room == house[5]:
        jump Laptop
    $ renpy.block_rollback()
    if ('06:00' <= tm < '22:00') or ('lisa' in house[0].cur_char and lisa.plan_name not in ['sleep', 'sleep2']):
        scene BG char Max laptop-day-00
        $ renpy.show('Max laptop-day 01'+mgg.dress)
    else:
        scene BG char Max laptop-night-00
        $ renpy.show('Max laptop-night 01'+mgg.dress)

    Max_00 "{m}Итак, чем интересным я займусь?{/m}"
    jump Laptop


label Laptop:
    if '06:00' <= tm < '22:00':
        if current_room == house[5]:
            scene BG char Max laptop-day-01t
        else:
            scene BG char Max laptop-day-01
    else:
        if current_room == house[5]:
            scene BG char Max laptop-night-01t
        elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
            scene BG char Max laptop-day-01
        else:
            scene BG char Max laptop-night-01

    show interface laptop start page at laptop_screen

    show video1_movie:
        xpos 221 ypos 93

    $ renpy.block_rollback()

    $ search_theme.clear()

    if poss['cams'].st() == 1:
        $ search_theme.append((_("{i}почитать о камерах{/i}"), 'about_cam'))
    if poss['blog'].st() == 0:
        $ search_theme.append((_("{i}читать о блогах{/i}"), 'about_blog'))
    if poss['secretbook'].st() == 1:
        $ search_theme.append((_("{i}узнать о книге Алисы{/i}"), 'about_secretbook'))
    if poss['spider'].st() == 0:
        $ search_theme.append((_("{i}читать о пауках{/i}"), 'about_spider'))
    if flags.credit == 1:
        $ search_theme.append((_("{i}искать информацию по кредитам{/i}"), 'about_credit'))

    call screen LaptopScreen


label LaptopShop:
    if '06:00' <= tm < '22:00':
        if current_room == house[5]:
            scene BG char Max laptop-day-01t
        else:
            scene BG char Max laptop-day-01
    else:
        if current_room == house[5]:
            scene BG char Max laptop-night-01t
        elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
            scene BG char Max laptop-day-01
        else:
            scene BG char Max laptop-night-01
    show interface laptop e-shop at laptop_screen

    $ renpy.block_rollback()
    call screen OnlineShop


label nothing_search:
    Max_00 "{m}Сейчас мне нечего искать...{/m}"
    jump Laptop


label buyfood:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop grocery-1 at laptop_screen
    Max_04 "{m}Так... Посмотрим список продуктов... Ага. Сейчас всё закажем...{/m}"
    if dcv.buyfood.stage == 1:
        Max_04 "{m}Готово. Да это же самая лёгкая задача!{/m}"
        $ dcv.buyfood.stage = 2
    else:
        Max_01 "{m}Готово. То, что я делаю это без маминой финансовой помощи точно пойдёт мне только в плюс.{/m}"
        $ dcv.buyfood.stage = 4
    $ spent_time = 50
    $ dcv.buyfood.set_lost(2)
    $ mgg.pay(50)
    jump Laptop


label courses_start:
    if '06:00' <= tm < '22:00':
        if current_room == house[5]:
            scene BG char Max laptop-day-01t
        else:
            scene BG char Max laptop-day-01
    else:
        if current_room == house[5]:
            scene BG char Max laptop-night-01t
        elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
            scene BG char Max laptop-day-01
        else:
            scene BG char Max laptop-night-01
    show interface laptop e-shop at laptop_screen

    $ renpy.block_rollback()
    call screen OnlineCources

    # jump Laptop


label create_site:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop cam-inf-2 at laptop_screen
    menu:
        Max_00 "{m}Итак, пришло время заняться своим сайтом. Для начала нужно купить домен, хостинг, шаблон дизайна и оплатить услуги стримингового сервиса. На всё в сумме нужно $100{/m}"
        "Оплатить всё ($100)":
            pass
        "В другой раз...":
            jump Laptop
    show interface laptop cam-inf-3 at laptop_screen
    menu:
        Max_04 "{m}Отлично! Теперь у меня есть свой сайт и домен! Осталось только соединить поток данных от камеры со стриминговым сервисом...{/m}"
        "Настроить работу сайта":
            pass
    show interface laptop cam-inf-4 at laptop_screen
    Max_04 "{m}Да! Всё работает! Теперь люди смогут заходить на мой сайт и смотреть шоу. Конечно, если они каким-то образом узнают про мой сайт... Ладно, подумаю ещё что можно сделать...{/m}"
    $ spent_time = 60
    $ poss['cams'].open(4)
    $ mgg.pay(100)
    $ items['hide_cam'].unblock()
    $ house[4].cams.append(HideCam())
    $ house[4].cams[0].grow = 100

    jump Waiting


label open_site:
    if '06:00' <= tm < '22:00':
        if current_room == house[5]:
            scene BG char Max laptop-day-01t
        else:
            scene BG char Max laptop-day-01
    else:
        if current_room == house[5]:
            scene BG char Max laptop-night-01t
        elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
            scene BG char Max laptop-day-01
        else:
            scene BG char Max laptop-night-01
    show interface laptop CoverBBCams at laptop_screen

    $ create_cam_list() # обновим список камер для отображения

    $ renpy.block_rollback()
    call screen MySite


label about_cam:
    hide video1_movie
    show interface laptop cam-inf-1 at laptop_screen
    Max_09 "{m}Так, любопытно... Эти камеры можно настроить так, чтобы они транслировали изображение в интернет!{/m}"
    Max_07 "{m}Но что ещё интереснее, некоторые люди готовы платить за доступ к таким камерам...{/m}"
    Max_09 "{m}Может быть, мне сделать свой сайт и пусть люди мне платят за просмотр видео? Но я не умею ничего толком...{/m}"
    $ items['manual'].unblock()
    $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    $ spent_time += 20
    $ poss['cams'].open(2)
    jump Laptop


label about_blog:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop blog-inf-1 at laptop_screen
    menu:
        Max_00 "{m}Итак, попробуем что-то найти о блогах. С чего начать?{/m}"
        "Собрать статистику":
            menu:
                Max_10 "{m}Ох... Сколько цифр. Неужели, во всём этом можно разобраться?{/m}"
                "Проанализировать результаты":
                    $ _text = _("Хм... Так... Ага. Это сюда запишем, это сюда...")
                "Построить таблицу":
                    $ _text = _("Так. Из этой таблицы мы делаем вывод. Ага. Вот это значит, что... Нет, не так. Вот. Вроде получилось...")
                "Нарисовать график":
                    $ _text = _("Рисователь графиков из меня ещё тот. Но попробуем. Так, это шкала популярности, это... Ага. Кажется, всё сходится...")
        "Просмотреть популярные блоги":
            menu:
                Max_04 "{m}Прикольно... Ага. Котики. Не, устарели. Киски. Ну, смотря какие...{/m}"
                "Составить список":
                    $ _text = _("Так, вычёркиваем из списка этих, вот этих и тех. Что тут у нас остаётся?")
                "Отсортировать...":
                    $ _text = _("Так, сравниваем аудиторию. Время публикации... Исключаем сомнительный контент...")
                "Сравнить количество лайков...":
                    $ _text = _("Сортируем по количеству лайков. Убираем тех, кто с дизлайками больше этого процента...")
        "Почитать комменты на блогах":
            menu:
                Max_14 "{m}Ух. Сколько гадости в комментах... Ладно, попробуем найти в этом крупицу смысла...{/m}"
                "Воспользоваться поиском":
                    $ _text = _("Так, в поиске мы видим любопытные результаты. Так, выберем то что нам подходит...")
                "Читать всё подряд":
                    $ _text = _("Ох. Всё оказалось ещё хуже. Кажется, тут нет ничего полезного... Хотя. Думаю, можно сделать даже какой-то вывод...")
                "Выбрать лучшие комменты":
                    $ _text = _("Так, топовые комменты все сводятся к одному. Не может быть?")

    menu:
        Max_09 "{m}[_text!t]{/m}"
        "Сделать вывод...":
            Max_01 "{m}Это что же получается. Неужели, всё так просто? Главное - сиськи! Не важно о чём блог, важно что на экране. И если там сиськи, всё в порядке с популярностью! Но я и так об этом догадывался...{/m}"
            Max_00 "{m}И зачем я только что-то изучал...{/m}"


    $ poss['blog'].open(1)
    $ spent_time += 30
    jump Laptop


label about_secretbook:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop secretbook-inf-1 at laptop_screen
    menu:
        Max_00 "{m}Так... Сейчас погуглим. Как там она называлась? \"Sugar Daddies\"?... Любовный роман? И что в нём такого может быть?{/m}"
        "{i}читать о книге{/i}":
            Max_06 "{m}Ого! Да это не простой любовный роман... Это же эротика. Да ещё какая! Теперь понятно, почему Алиса не хотела рассказывать, что читает...{/m}"

    $ items['erobook_1'].unblock()
    $ poss['secretbook'].open(2)
    $ spent_time += 30
    jump Laptop


label about_spider:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop spider-inf-1 at laptop_screen

    menu:
        Max_00 "{m}Так... Пауки. Ох, сколько видов... Какие же тут водятся...{/m}"
        "Искать виды насекомых по регионам":
            Max_00 "{m}Ага, отлично. Выбираем наш регион, сортируем по видам пауков...{/m}"
        "Читать где водятся какие пауки":
            Max_00 "{m}Так, пауки. Смотрим какие водятся в этом климате...{/m}"
    Max_00 "{m}Так, и что у нас получается?{/m}"
    menu:
        Max_01 "{m}Ну вот, подходит. Самый популярный паук в наших краях. Ага! Теперь узнаем как его поймать...{/m}"
        "Выяснить, чем питается...":
            menu:
                Max_09 "{m}Так, питается комарами и мошками. Как это обычно... нет, это ничего не даёт...{/m}"
                "Почитать о повадках...":
                    pass
        "Почитать о повадках...":
            pass
    Max_04 "{m}Вот, отлично! Ночью отлично маскируются, значит, не подходит, а вот как только солнце начинает прогревать землю, выползают из травы проверить добычу. А это у нас часов 10-11?{/m}"
    Max_01 "{m}Будем искать!{/m}"

    $ poss['spider'].open(1)
    $ AvailableActions['catchspider'].enabled = True
    $ AvailableActions['hidespider'].enabled = True
    $ SpiderKill = 0
    $ SpiderResp = 0
    $ spent_time += 30
    jump Laptop


label SearchCam:
    $ renpy.block_rollback()
    if current_room == house[4]:
        scene Max cam
        $ FoundCamera = True
        Max_04 "{m}Ого! Вот же она! Кто-то её так хорошо запрятал в стену, что найти камеру можно только точно зная, что ищешь...{/m}"
        Max_09 "{m}Так... Но она ни к чему не подключена сейчас. Видимо, отец так следил за ходом строительства и ремонта, а сейчас уже некому следить и не за чем...{/m}"
        Max_04 "{m}Но если её подключить, то можно подглядывать и за кое-чем другим. Вот только нужно во всём как следует разобраться!{/m}"
        $ random_loc_ab = 'b'
        $ AvailableActions['searchcam'].enabled = False
        $ InspectedRooms.clear()
        $ poss['cams'].open(1)
    else:
        if current_room == house[6]:
            # двор
            Max_14 "{m}Кажется, здесь нет никаких камер... Нужно поискать в самом доме!{/m}"
        else:
            Max_14 "{m}Кажется, здесь нет никаких камер... Может быть, стоит поискать в другой комнате?{/m}"
        $ InspectedRooms.append(current_room)
    $ spent_time = 30
    $ cur_ratio = 2
    jump Waiting


label ClearPool:
    $ renpy.block_rollback()
    scene BG char Max cleeningpool-00
    $ renpy.show('Max cleaning-pool 01'+mgg.dress)
    if dcv.clearpool.stage == 1:
        Max_11 "{m}Эх... Не лёгкая это работа, но нужно отработать те деньги, что мама уже заплатила...{/m}"
        $ dcv.clearpool.stage = 2
    else:
        Max_01 "{m}Эх... Работа нудная, но важно, чтобы мои девочки плескались в чистой водичке. И теперь, я слежу за этим сам.{/m}"
        $ dcv.clearpool.stage = 4
    if day > 10:
        $ dcv.clearpool.set_lost(6)
    else:
        $ dcv.clearpool.set_lost(9)
    $ spent_time = 60
    $ cur_ratio = 2.5
    jump Waiting


label DishesWashed:
    $ renpy.block_rollback()
    if tm < '16:00':
        scene BG crockery-morning-00
        $ renpy.show('Max crockery-morning 01'+mgg.dress)
    else:
        scene BG crockery-evening-00
        $ renpy.show('Max crockery-evening 01'+mgg.dress)
    menu:
        Max_00 "{m}Эх... столько посуды. И почему в этом огромном доме нет маленькой посудомоечной машины?{/m}"
        "{i}закончить{/i}":
            pass
    if weekday != 6:
        if weekday == 0:
            $ __name_label = alice.get_plan(day, '10:30').label
        else:
            $ __name_label = alice.get_plan(day, '11:30').label
        if __name_label == 'alice_dishes':
            $ AddRelMood('alice', 10, 60, 2)
    $ dishes_washed = True
    $ spent_time = max((60 - int(tm[-2:])), 50)
    $ cur_ratio = 2
    jump Waiting


label delivery1:
    $ renpy.block_rollback()

    if 'choco' in delivery_list[0]:
        $ kol_choco += 20
        $ items['choco'].block()
        $ poss['nightclub'].open(6)
    $ __StrDev = GetDeliveryString(0) # сформируем строку накладной

    scene BG delivery-00
    Max_07 "{m}Звонок в ворота! Похоже, к нам кто-то приехал...{/m}"
    scene BG delivery-01
    show Sam delivery 01
    Sam_00 "Здравствуйте! По этому адресу на сегодня назначена доставка. Распишитесь?"
    Max_00 "Конечно! А что тут?"
    $ renpy.say(Sam_00, __StrDev)
    Max_00 "Да, то что нужно. Спасибо!"
    $ current_room = house[6]
    $ flags.courier1 += 1
    $ DeletingDeliveryTempVar(0) # удалим временные переменные и очистим список доставки
    jump AfterWaiting


label delivery2:
    $ renpy.block_rollback()

    if 'solar' in delivery_list[1]:
        $ kol_cream += 30
        $ items['solar'].block()
    if 'max-a' in delivery_list[1]:
        # $ mgg.clothes.casual.sel.insert(1, Garb('b', '01b', 'МУЖСКИЕ МАЙКА И ШОРТЫ', True))
        # $ mgg.clothes.casual.cur = 1
        $ mgg.clothes.casual.enable(1, 1)
        $ items['max-a'].block()
        $ added_mem_var('max-a')
    if 'dress' in delivery_list[1] and not poss['nightclub'].used(3):
        $ poss['nightclub'].open(1)
    if 'bikini' in delivery_list[1] and not poss['Swimsuit'].used(4):
        $ poss['Swimsuit'].open(3)

    $ __StrDev = GetDeliveryString(1) # сформируем строку накладной

    scene BG delivery-00
    Max_07 "{m}Звонок в ворота! Похоже, к нам кто-то приехал...{/m}"
    scene BG delivery-01
    $ __dress = renpy.random.choice(['a', 'b'])
    $ renpy.show('Christine delivery 01'+__dress)
    Christine_00 "Здравствуйте! По этому адресу на сегодня назначена доставка. Распишитесь?"
    Max_00 "Конечно! А что тут?"
    $ renpy.say(Christine_00, __StrDev)
    Max_00 "Да, то что нужно. Спасибо!"
    $ current_room = house[6]
    $ flags.courier2 += 1
    if 'nightie2' in delivery_list[1]:
        #при доставке сорочки для Киры первый разговор с Кристиной
        call christina_first_talk(__dress) from _call_christina_first_talk
    if 'sexbody2' in delivery_list[1]:
        # поступило первое бельё для опережения Эрика
        if alice.dcv.intrusion.stage<5 and weekday in [4, 5]:
            # Макс успевает
            Max_02 "{m}Боди у меня! Теперь, нужно подарить его Алисе и больше всего мне может повезти, когда она занимается своим блогом. Она и так в это время в нижнем белье, а с учётом того, что она получит боди раньше времени, то вполне может переодеться и при мне...{/m}"
        else:
            Max_10 "{m}Боди у меня! Вот только поздно... Эрик уже купил Алисе то, что она хотела. Остаётся лишь выставить на ebay, так хотя бы половину стоимости верну.{/m}"

    $ DeletingDeliveryTempVar(1) # удалим временные переменные и очистим список доставки
    $ ChoiceClothes()
    jump AfterWaiting


label BookRead:
    scene BG char Max reading-00
    $ renpy.show('Max reading 01'+mgg.dress)
    menu:
        Max_00 "Пришло время почитать что-то..."
        "{i}читать \"WEB STANDARDS\"{/i}" if items['manual'].have and items['manual'].read < 5:
            jump .manual
        "{i}читать \"СЕКС-ОБРАЗОВАНИЕ\"{/i}" if items['sex.ed'].have and items['sex.ed'].read < 4:
            jump .sex_ed

    label .manual:
        $ items['manual'].read += 1
        if items['manual'].read < 2:
            Max_00 "Хм... куча непонятных слов. Кажется, нужно будет заново перечитать первые главы...\n\n{color=[orange]}{i}(Книга изучена на 20%%){/i}{/color}"
        elif items['manual'].read < 3:
            Max_00 "Так, ну с этим я уже разобрался, хорошо... А это что такое? Не ясно. Нужно будет всё осмыслить...\n\n{color=[orange]}{i}(Книга изучена на 40%%){/i}{/color}"
        elif items['manual'].read < 4:
            Max_00 "Ого, вот это здорово! Уже можно делать сайт? А, нет... Ещё не всё понятно... Ну, разберусь в другой раз.\n\n{color=[orange]}{i}(Книга изучена на 60%%){/i}{/color}"
        elif items['manual'].read < 5:
            Max_00 "Так, ну теперь картина вырисовывается. Осталось разобраться только с мелочами... Или это не мелочи?\n\n{color=[orange]}{i}(Книга изучена на 80%%){/i}{/color}"
        else:
            Max_00 "Всё, вот теперь точно всё понятно! Я уже могу сделать свой сайт и транслировать на него изображение! Но как получать за это деньги?"
            $ poss['cams'].open(3)
            $ items['manual'].block()
        jump .end

    label .sex_ed:
        $ items['sex.ed'].read += 1
        if items['sex.ed'].read < 2:
            # выбрали читать книгу
            $ poss['seduction'].open(13)
            $ items['sex.ed'].block()
            Max_01 "Ага. У каждого есть свои особенности, а то я не знал! Вот, строение половых органов девочки-подростка, то что надо... Будем читать и разглядывать.\n\n{color=[orange]}{i}(Книга изучена на 25%%){/i}{/color}"
        elif items['sex.ed'].read < 3:
            Max_03 "Так, это не особо интересно... А вот сексуалное поведение подростков - это как раз про меня! Ещё про мои утренние стояки написали бы, было бы вообще супер...\n\n{color=[orange]}{i}(Книга изучена на 50%%){/i}{/color}"
        elif items['sex.ed'].read < 4:
            Max_07 "Ого, здесь даже есть краткий исторический очерк о сексуальном воспитании детей и подростков... Как только голову не дурили за всё это время!\n\n{color=[orange]}{i}(Книга изучена на 75%%){/i}{/color}"
        else:
            # чтение завершено, можно дарить
            $ poss['seduction'].open(14)
            Max_04 "Вот и последние главы... Всё-таки прикосновения очень важны! Да я и на практике уже это понял... Эх, надо было раньше эту книжку купить! Но лучше поздно, чем никогда. Материал усвоен и теперь можно дарить её Лизе."
        jump .end

    label .end:
        $ cooldown['learn'] = CooldownTime('03:40') # 40 мин на этап чтения и 3 часа кулдаун
        $ spent_time = max((60 - int(tm[-2:])), 40)
        $ cur_ratio = 0.6
        jump Waiting


label SearchSecretBook:

    menu:
        Max_10 "{m}Так... И с чего начать поиск? И нужно поспешить: если Алиса меня поймает, то сначала убьёт, а только потом поздоровается...{/m}"
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
            Max_14 "{m}Нет, здесь её нет... Ну где же эта чёртова книга? Шаги? Нет, показалось...{/m}"
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
            Max_14 "{m}Нет, тут её точно нет. Ну где же она? Кажется, я слышу шум...{/m}"
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
            Max_14 "{m}Может быть, её здесь нет? Или попытаться ещё поискать, на свой страх и риск?{/m}"
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
        $ renpy.scene()
        $ renpy.show('BG char Max secretbook-00'+mgg.dress)
        Max_04 "{m}Вот же она! И зачем её так прятать? Любопытная обложка. Запомню-ка я название. Интересно, о чём эта книга? Может быть, погуглить? Так, всё, надо уходить...{/m}"
        $ poss['secretbook'].open(1)
        $ AvailableActions['searchbook'].enabled = False
        jump Waiting


label InstallCam:
    if current_location != house:
        jump AfterWaiting

    if GetKolCams(house) < 7 and len(current_room.cams) > 0:
        Max_00 "{m}Здесь уже есть камера. Пожалуй, стоит установить её в другом месте.{/m}"
        jump AfterWaiting

    if len(current_room.cams) >= current_room.max_cam:
        jump AfterWaiting

    if current_room == house[0]:
        menu:
            Max_04 "{m}В этой комнате столько всего может происходить... Думаю, зрителям понравится! Главное - спрятать все провода, чтобы Лиза не заметила новую микро-камеру...{/m}"
            "{i}закончить{/i}":
                $ house[0].cams.append(HideCam())
                $ house[0].cams[0].grow = 100
    elif current_room == house[1]:
        menu:
            Max_04 "{m}Пусть зрители посмотрят, чем Алиса занимается в своей комнате, когда её не видят... Я бы и сам был бы рад посмотреть, но пока такой функции у меня нет...{/m}"
            "{i}закончить{/i}":
                $ house[1].cams.append(HideCam())
                $ house[1].cams[0].grow = 100
    elif current_room == house[2]:
        menu:
            Max_04 "{m}Конечно, здесь редко происходят события. Зато, когда они происходят, то здесь такое... Думаю, зрители будут рады таким моментам...{/m}"
            "{i}закончить{/i}":
                $ house[2].cams.append(HideCam())
                $ house[2].cams[0].grow = 100
    elif current_room == house[3]:
        if current_room.cams:
            menu:
                Max_03 "{m}Теперь через обе камеры можно увидеть всё самое интересное! Девочки любят покрасоваться у зеркала, а моя мама и Эрик, как я заметил, стараются не упустить возможность потрахаться перед этим же зеркалом... Моим зрителям это явно понравится!{/m}"
                "{i}закончить{/i}":
                    $ house[3].cams.append(HideCam())
                    $ house[3].cams[1].grow = 100
        else:
            menu:
                Max_04 "{m}Конечно, с точки зрения морали ставить камеру в ванной сомнительно. Однако, тут и так окно во всю стену. Так что, формально я лишь приоткрыл это окно...{/m}"
                "{i}закончить{/i}":
                    $ house[3].cams.append(HideCam())
                    $ house[3].cams[0].grow = 100
    elif current_room == house[5]:
        menu:
            Max_04 "{m}Уж не знаю, будет ли какой-то толк от этой камеры... Тут так редко что-то происходит... Ну пусть будет. Раз уж взялся всё подключать...{/m}"
            "{i}закончить{/i}":
                $ house[5].cams.append(HideCam())
                $ house[5].cams[0].grow = 100
    elif current_room == house[6]:
        if len(current_room.cams) > 0:
            menu:
                Max_04 "{m}Вот теперь зрители смогут насладится всеми мокрыми и блестящими красотами, происходящими во дворе...{/m}"
                "{i}закончить{/i}":
                    $ house[6].cams.append(HideCam())
                    $ house[6].cams[1].grow = 100
        else:
            menu:
                Max_04 "{m}Двор... Тут почти всё время кто-то есть и что-то делает, пока светит солнце. Думаю, тут зрители будут зависать постоянно в надежде увидеть кого-то с голыми сиськами...{/m}"
                "{i}закончить{/i}":
                    Max_09 "{m}Пожалуй, из-за большой площади мне стоило бы установить здесь несколько камер, чтобы зрители смогли лучше разглядеть каждую попку, которая тут бывает...{/m}"
                    $ house[6].cams.append(HideCam())
                    $ house[6].cams[0].grow = 100

    $ items['hide_cam'].use()
    $ cur_ratio = 1.5
    $ spent_time = 30
    if GetKolCams(house)>7:
        $ poss['cams'].open(5)
        if house[3].max_cam < 2:
            $ items['hide_cam'].block()

    if GetKolCams(house)==9:
        $ poss['cams'].open(6)
        $ items['hide_cam'].block()
    jump Waiting


label SearchSpider:
    scene BG char Max spider-search-00
    $ renpy.show('Max spider search-00'+mgg.dress)
    $ renpy.dynamic('ch')
    $ ch = {
        0 : 100,
        1 : {
            0 : 40,
            1 : 50,
            2 : 70}[SpiderKill],
        2 : {
            0 : 0,
            1 : 15,
            2 : 40}[SpiderKill],
        3 : 5}[SpiderResp]
    menu:
        Max_00 "{m}Так, нужно хорошенько рассмотреть траву...{/m}"
        "{i}искать...{/i}" ('lucky', ch):
            if rand_result:
                $ renpy.scene()
                $ renpy.show('BG char Max spider-search-01'+mgg.dress)
                Max_04 "Ага! Попался! Отлично..."
                $ poss['spider'].open(2)
                $ items['spider'].have = True
            else:
                Max_00 "{m}Нет, ничего похожего на большого страшного паука тут нет... Может быть, я всех переловил и стоит подождать денёк-другой?{/m}"
            $ spent_time = 30
            $ cur_ratio = 1.5
        "{i}уйти{/i}":
            pass

    jump Waiting


label HideSpider:

    $ renpy.dynamic('ch')
    if '00:40' < tm < '01:00':
        Max_00 "{m}Я могу не успеть как следует припрятать паука, прежде чем Алиса вернется из ванной.{/m}"
        jump Waiting

    $ ch = {'00:00' <= tm <= '00:40' : 80, '23:00' <= tm <= '23:59' : 70, '20:00' <= tm <= '22:59' : 50, '01:00' <= tm <= '19:59' : 0,}[True]
    menu:
        Max_00 "{m}Интересно, что будет, если Алиса заметит паука ночью? Она прибежит за помощью? Вот только этот монстр может сбежать... Так что, чем позже я его спрячу, тем больше шансов на успех...{/m}"
        "{i}Подложить сейчас{/i}" ('lucky', ch):
            scene BG char Alice spider
            Max_00 "{m}Что ж, будем надеяться, что паук не сбежит до того, как Алиса ляжет спать...{/m}"
            $ SpiderKill = 0
            $ SpiderResp = 1
            if rand_result and 'spider' not in NightOfFun:
                $ NightOfFun.append('spider')
            $ items['spider'].use()
            $ spent_time = 10

        "В другой раз...":
            pass
    jump Waiting


label ViewLesson:

    if '06:00' <= tm < '22:00':
        if current_room == house[5]:
            scene BG char Max laptop-day-01t
        else:
            scene BG char Max laptop-day-01
    else:
        if current_room == house[5]:
            scene BG char Max laptop-night-01t
        elif 'lisa' in house[0].cur_char and lisa.plan_name != 'sleep':
            scene BG char Max laptop-day-01
        else:
            scene BG char Max laptop-night-01

    $ renpy.show('interface laptop '+CurCource.img+'-'+str(CurCource.current)+'-'+str(CurCource.cources[CurCource.current].less), [laptop_screen])

    if CurCource.skill == 'social':
        $ mgg.social += round(renpy.random.randint(1000, 1000*CurCource.cources[CurCource.current].grow) / 1000.0, 2)
    elif CurCource.skill == 'massage':
        $ mgg.massage += round(renpy.random.randint(1000, 1000*CurCource.cources[CurCource.current].grow) / 1000.0, 2)
    $ CurCource.cources[CurCource.current].less += 1
    if CurCource.cources[CurCource.current].less == CurCource.cources[CurCource.current].total: # Последний урок текущейго курса
        if CurCource.current < len(CurCource.cources):
            $ CurCource.current += 1

    $ cooldown['learn'] = CooldownTime('03:40') # 40 мин на этап чтения и 3 часа кулдаун
    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ cur_ratio = 0.6
    $ notify_list.append(_("Вы просматриваете видеоурок и повышаете свои навыки."))
    Max_00 "{m}Хорошая штука эти онлайн-курсы - можно научиться всему, не входя из дома! Вот только и стоит это немало...{/m}"
    jump Waiting


label SearchCigarettes:
    scene BG char Max cigarettes-00

    Max_09 "{m}Так... Где же Алиса спрятала сигареты сегодня?{/m}" # nointeract

    call screen search_cigarettes

    label .bedside:
        if (random_sigloc == 'n' and alice.dcv.special.done
                and alice.plan_name not in['at_friends','smoke']):
            jump .yes
        else:
            jump .no

    label .table:
        if (random_sigloc == 't' and alice.dcv.special.done
                and alice.plan_name not in['at_friends','smoke']):
            jump .yes
        else:
            jump .no

    menu .no:
        Max_10 "{m}Кажется, здесь их нет... Пора уходить, а то если кто-то заметит меня...{/m}"
        "{i}уйти{/i}":
            $ spent_time += 30
            jump Waiting

    label .yes:
        $ renpy.show('Max cigarettes 01'+mgg.dress)
        menu:
            Max_04 "{m}Ага, нашёл! Так... Теперь их нужно положить таким образом, чтобы мама их заметила, если заглянет в комнату...{/m}"
            "{i}подставить Алису{/i}":
                if ((tm < '13:00' and alice.plan_name == 'smoke')
                    or (tm < '17:00') and alice.plan_name == 'at_friends'):
                        pass  # если сегодня Алиса ещё не курила или будет у подружки, подставлять бесполезно, она переложит сигареты
                else:
                    $ punalice[0][1] = 1
            "{i}не подставлять Алису{/i}":
                pass
    $ alice.dcv.set_up.set_lost(1)
    $ spent_time += 30
    jump Waiting


label need_money:
    $ current_room = house[0]
    $ renpy.block_rollback()
    scene Max unbox 04
    Max_10 "{m}Сегодня уже четверг. Последний день когда я могу заказать подарки девчонкам, чтобы опередить Эрика.{/m}"
    if ((items['bikini'].InShop and not (items['bikini'].have or items['bikini'].bought)) and
                (items['dress'].InShop and not (items['dress'].have or items['dress'].bought))):
        if mgg.money >= 500:
            jump cheat_money
        elif 300 <= mgg.money < 500:
            Max_11 "{m}Нужно скорее купить платье Алисе и купальник для Лизы, а денег у меня хватает лишь на что-то одно...{/m}"
        else:
            Max_11 "{m}Нужно скорее купить платье Алисе и купальник для Лизы, а денег мне не хватит даже на что-то одно...{/m}"
    elif not (items['dress'].InShop and not (items['dress'].have or items['dress'].bought)):
        if mgg.money >= 220:
            jump cheat_money
        else:
            Max_11 "{m}Я уже купил платье Алисе, но на купальник для Лизы мне не хватит денег...{/m}"
    elif not (items['bikini'].InShop and not (items['bikini'].have or items['bikini'].bought)):
        if mgg.money >= 280:
            jump cheat_money
        else:
            Max_11 "{m}Я уже купил купальник для Лизы, но на платье Алисе мне не хватит денег...{/m}"
    else:
        jump cheat_money
    if len(house[4].cams) > 0 and house[4].cams[0].total > 0:
        Max_08 "{m}Сайт у меня есть и уже приносит какую-то прибыль, но нужно время, чтобы раскрутить его.{/m}"
    else:
        Max_08 "{m}К сожалению, у меня нет источника доходов, все мои деньги я получаю только от мамы. Ну и от Алисы ещё могу...{/m}"
    Max_09 "{m}Нужно поискать какую-нибудь информацию в интернете, может есть возможность получить кредит.{/m}"
    $ flags.credit = 1
    $ spent_time += 10
    jump Waiting


label cheat_money:
    if poss['cams'].st() < 4:
        if all([
                items['bikini'].InShop and not any([items['bikini'].have, items['bikini'].bought]),
                items['dress'].InShop and not any([items['dress'].have, items['dress'].bought]),
                mgg.money <= 600
            ]):
                jump .strateg
        elif mgg.money < 320 and not all([items['dress'].InShop, not any([items['dress'].have, items['dress'].bought])]):
            jump .strateg
        elif mgg.money < 380 and not all([items['bikini'].InShop, not any([items['bikini'].have, items['bikini'].bought])]):
            jump .strateg
        else:
            pass
    "На данном этапе игры у Макса не может быть такой суммы. Взлом игры может привести к непредсказуемым последствиям, в частности, к потере некоторых возможностей и функционала игры, а так же к возникновению критических ошибок, которые не позволят вам продолжить игру."
    jump AfterWaiting

    label .strateg:
        "Вы либо аккуратный взломщик, либо хороший стратег. В любом случае вы не нуждаетесь в дополнительных методах получения денег. Учтите, взлом игры может привести к непредсказуемым последствиям, в частности, к потере некоторых возможностей и функционала игры, а так же к возникновению критических ошибок, которые не позволят вам продолжить игру."


label about_credit:
    $ renpy.block_rollback()
    hide video1_movie
    show interface laptop bank-inf-1 at laptop_screen

    Max_00 "{m}Итак, поищем, где можно простому парню разжиться деньгами...{/m}"
    Max_09 "{m}Это не подходит... Здесь нужно иметь официальное трудоустройство на работе...{/m}"
    Max_07 "{m}Ага, а вот это может и подойти - краткосрочные займы начинающим интернет-предпринимателям. О, да, это про меня...{/m}"
    Max_01 "Бла, бла, бла... ... если у Вас есть работающий проект в интернете, мы предоставляем займы на раскрутку Вашего бизнеса..."
    if len(house[4].cams) > 0 and house[4].cams[0].total > 0:
        Max_04 "{m}Подытожим условия: \n{b}В течение месяца нужно вернуть всю сумму займа + 10%% \nВ случае не погашения в срок, сумма долга утраивается каждые 30 дней, а с моего сайта будут ежедневно изымать половину прибыли. И занять ещё раз уже не получится...{/b} \n\nЛучше, конечно же, до такого не доводить.{/m}"
        Max_05 "{m}Регистрируюсь... Указываю свои реквизиты... Свой сайт в качестве источника дохода... Готово!{/m}"
        Max_02 "{m}Теперь я могу взять кредит, если срочно понадобятся деньги. Главное вовремя его погасить, чтобы проблем не было...{/m}"
        $ mgg.credit.level = 1
    else:
        Max_16 "{m}Вот чёрт, а у меня нет никакого проекта! Получается, что денег мне никто не даст.{/m}"

    $ flags.credit = 2
    $ spent_time += 30
    jump Laptop


label getting_load:
    show screen Bank
    menu:
        Max_00 "{m}Сколько мне сейчас нужно занять?{/m}"
        "$500":
            $ mgg.credit_getting(500)
        "$1000" if mgg.credit.level > 1:
            $ mgg.credit_getting(1000)
        "$2000" if mgg.credit.level > 2:
            $ mgg.credit_getting(2000)
        "$5000" if mgg.credit.level > 3:
            $ mgg.credit_getting(5000)
        "{i}не сейчас{/i}":
            pass
    call screen Bank


label return_part_loan:
    show screen Bank
    menu:
        Max_00 "{m}Сколько я верну сейчас?{/m}"
        "$50":
            $ mgg.credit_part(50)
        "$100" if mgg.money >= 100 and mgg.credit.debt >= 100:
            $ mgg.credit_part(100)
        "$200" if mgg.money >= 200 and mgg.credit.debt >= 200:
            $ mgg.credit_part(200)
        "$500" if mgg.money >= 500 and mgg.credit.debt >= 500:
            $ mgg.credit_part(500)
        "$1000" if mgg.money >= 1000 and mgg.credit.debt >= 1000:
            $ mgg.credit_part(1000)
        "$2000" if mgg.money >= 2000 and mgg.credit.debt >= 2000:
            $ mgg.credit_part(2000)
        "{i}не сейчас{/i}":
            pass
    call screen Bank


label bedtime_thoughts:
    # Мысли Макса перед сном

    if flags.lisa_sexed == 6 and lisa.dcv.battle.stage not in [1, 4]:
        # о том, как напакостить Эрику
        Max_07 "{m}Как же напакостить Эрику, чтобы он хотя бы на время перестал лезть к моим сёстрам... и Кире... да и к маме тоже... Хм... У меня была бы отличная возможность что-нибудь подмешать в его еду за ужином, если помочь Алисе накрыть на стол! Стоит посмотреть в интернет-магазине, можно ли что-то такое купить...{/m}"
        if lisa.dcv.intrusion.stage == 4:
            $ poss['seduction'].open(25)
        elif GetRelMax('eric')[0] < 0:
            $ poss['seduction'].open(24)

        $ flags.lisa_sexed = 7
        $ items['laxative'].unblock()
        $ items['sedative'].unblock()

    return
