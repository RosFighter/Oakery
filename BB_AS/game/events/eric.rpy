
label Eric_talk_afterdinner:
    $ renpy.block_rollback()
    $ spent_time = 20
    $ current_room = house[6]

    scene BG char Max meet-eric-terrace-00
    show Eric meet 01a
    show Max meet-Eric 01a
    Eric_00 "Макс, пока твоя мама переодевается, я бы хотел с тобой поговорить. С глазу на глаз, так сказать..."
    if talk_var["empathic"] > 1:
        Max_01 "Конечно..."
        $ talk_var["empathic"] = 7
        menu:
            Eric_05 "Я заметил, что ты настроен вполне дружелюбно. Для меня важно подружиться с твоей семьёй, чтобы твоя мама не испытывала дискомфорт на этой почве, если ты меня понимаешь..."
            "Понимаю, хорошо...":
                jump .good
            "И зачем мне это?":
                jump .bad
    elif talk_var["empathic"] > 0:
        Max_00 "Ну, давай..."
        $ talk_var["empathic"] = 5
        menu:
            Eric_09 "Я знаю, что мы начали знакомство не идеально, но мне показалось, что мы можем найти общий язык. Для меня важно, чтобы твоя мама не испытывала какой-либо дискомфорт из-за этого..."
            "Понимаю, хорошо...":
                jump .good
            "И зачем мне это?":
                jump .bad
    else:
        Max_09 "У меня есть выбор?"
        $ talk_var["empathic"] = 3
        menu:
            Eric_13 "Ты знаешь, мы начали знакомство как-то совсем неудачно. Предлагаю как-то уладить этот конфликт. Я бы очень не хотел, чтобы твоя мама испытывала дискомфорт по этому поводу..."
            "Понимаю, хорошо...":
                jump .good
            "И зачем мне это?":
                jump .bad

    label .good:
        $ talk_var["empathic"] += 1
        show Eric meet 01a
        show Max meet-Eric 01a
        menu:
            Eric_01 "Отлично. Если мы подружимся, ты не пожалеешь, Макс. Но, чтобы убедиться, давай вернёмся к этому разговору через неделю. Если мы найдём общий язык, то всё будет отлично. Ну а если нет..."
            "А если нет, то что?":
                jump .what
            "Думаю, подружимся...":
                $ talk_var["empathic"] += 2
                jump .friend

    label .bad:
        show Max meet-Eric 01b
        show Eric meet 01b
        $ talk_var["empathic"] -= 1
        menu:
            Eric_01 "Я бы на твоём месте не искал врага там, где его нет. Предлагаю вернуться к этому разговору через неделю. Если мы подружимся, ты не пожалеешь. А вот если решишь со мной воевать, то ты точно проиграешь..."
            "Это ещё почему?":
                jump.what
            "Да я не собираюсь воевать...":
                $ talk_var["empathic"] += 1
                jump .friend

    menu .what:
        Eric_05 "Если решишь испытать судьбу, то сам всё скоро узнаешь. У меня есть влияние, деньги, харизма. А главное - я умею убеждать и подчинять других людей. А что есть у тебя?"
        "Да верю, верю. Я просто спросил и не хочу ссориться...":
            $ talk_var["empathic"] += 1
            jump .friend
        "Меня все любят и мне поверят, что ты мне угрожал!":
            $ talk_var["empathic"] -= 2
            show Max meet-Eric 01b
            show Eric meet 01b
            menu:
                Eric_02 "Правда? А я вот уже слышал, что Алиса относится к тебе как к маленькому извращенцу, Лиза рядом с тобой просто потому, что других защитников в доме не было, а мать смотрит на тебя как на неудачника..."
                "Не верю! Всё не так!":
                    jump .bullshit
                "Она так сказала?":
                    jump .shesaid
        "У меня есть мозги и я что-нибудь придумаю!":
            $ talk_var["empathic"] -= 2
            show Max meet-Eric 01b
            show Eric meet 01b
            menu:
                Eric_02 "Серьёзно? И как ты с этими мозгами довёл ситуацию до того, что Алиса в тебе видит маленького извращенца, подглядывающего из-за угла. Лиза рядом только потому, что других защитников не было, а мать... смотрит на тебя как на неудачника!"
                "Не верю! Всё не так!":
                    jump .bullshit
                "Она так сказала?":
                    jump .shesaid
    label .bullshit:
        menu:
            Eric_09 "Ну не знаю... Даже если что-то ещё и не так, то с моей помощью всё так и будет, поверь... Но повторюсь, я не хочу с тобой воевать и лучше бы ты был на моей стороне..."
            "Ладно, посмотрим...":
                jump .ok
            "Никогда. Отвали!":
                jump .no

    label .shesaid:
        Eric_09 "Ну не словами, но я же это вижу со стороны. Тебя выгнали из школы за отношения с учителем. Если ты не понял, то это такой зашквар, что вернуть себе репутацию будет непросто..."
        show Eric meet 01a
        menu:
            Eric_00 "Но повторюсь, я не хочу с тобой воевать. Наоборот, я бы хотел с тобой подружиться и если ты будешь на моей стороне, ты только выиграешь..."
            "Ладно, посмотрим... И что я выиграю?":
                jump .ok
            "Никогда. Отвали!":
                jump .no

    label .ok:
        show Max meet-Eric 01a
        show Eric meet 01a
        menu:
            Eric_05 "Смотря как пройдёт наше общение за следующую неделю. Если помиримся, то я буду помогать решать твои проблемы, ну а ты мои, если такие возникнут с твоей семьёй..."
            "Какие проблемы?":
                menu:
                    Eric_00 "Ты слишком забегаешь вперёд, Макс. Давай сначала посмотрим на то, как всё пойдёт. Дай мне хотя бы шанс тебя убедить..."
                    "Ну, ладно, убедил.":
                        jump .friend
                    "Нет, без вариантов...":
                        jump .no
            "Договорились...":
                jump .friend

    label .no:
        show Max meet-Eric 01b
        show Eric meet 01b
        menu:
            Eric_00 "Ну, как хочешь. Надеюсь, в тебе сейчас говорят эмоции, а не здравый смысл. У тебя есть неделя, чтобы передумать. Тогда и поговорим снова и будет ясно, как быть."
            "{i}промолчать{/i}":
                $ talk_var["empathic"] = 0
                jump Waiting

    label .friend:
        show Max meet-Eric 01a
        show Eric meet 01a
        Eric_05 "Я рад, правда. Ты не пожалеешь. Ладно, твоя мама уже идёт, мы поехали. Вернёмся к этому разговору через неделю..."
        Max_04 "Ага..."
        jump Waiting


label eric_resting:
    scene BG char Ann relax-evening-01
    $ renpy.show("Eric relax "+pose3_1+characters["eric"].dress)
    return

label eric_ann_tv:
    scene BG lounge-tv-00
    if tv_scene == "":
        $ renpy.show("Eric tv "+pose3_3+characters["eric"].dress)
    else:
        $ renpy.show("Eric tv "+tv_scene+pose2_3+characters["eric"].dress)
    return

label eric_ann_fucking:
    scene location house annroom door-night
    if peeping["ann_eric_sex1"] > 0:
        return
    else:
        $ peeping["ann_eric_sex1"] = 1

    menu:
        Max_00 "Судя по звукам, мама с Эриком чем-то занимаются. Открыть дверь точно не стоит, влетит..."
        "{i}заглянуть в окно{/i}":
            pass
        "{i}уйти{/i}":
            $ current_room = house[1]
            jump AfterWaiting

    $ spent_time += 10
    $ fuck_scene = renpy.random.randint(1, 5)
    if fuck_scene == 3:
        scene BG char Eric bed-02
    else:
        scene BG char Eric bed-02
    $ renpy.show("Eric fuck 0"+str(fuck_scene))
    if fuck_scene == 3:
        $ renpy.show("FG ann&eric-voyeur-02")
    else:
        $ renpy.show("FG ann&eric-voyeur-01")

    if fuck_scene == 1:
        Max_10 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nБоже мой, что моя мама творит?! Неужели ей действительно нравится отсасывать этому придурку?!" nointeract
    elif fuck_scene == 2:
        Max_07 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nВот это да! Прямо как в крутом порнофильме! Я даже представить себе не мог, что моя строгая мама способна на такое. Да и Эрик от неё не отстаёт... Кажется, ей это очень нравится!" nointeract
    elif fuck_scene == 3:
        Max_10 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nЧто?! Моя мама сосёт этому уроду? Эрик, гад, он же... трахает её в рот, как какую-то дешёвую уличную шлюху! Почему она ему это позволяет?!" nointeract
    elif fuck_scene == 4:
        Max_08 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nНу вот, Эрик трахает маму сзади, да так активно... Кажется, у неё просто нет сил противиться этому, хотя, может быть, ей это даже нравится!" nointeract
    elif fuck_scene == 5:
        Max_07 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nНичего себе! Вот это страсть! Моя мама скачет на Эрике как сумасшедшая! Я даже представить себе не мог, что она способна на такое! Кажется, они так увлечены друг другом, что не заметят, если я выйду из-за угла..." nointeract

    $ max_profile.stealth += 0.1
    $ renpy.notify(_("Скрытность Макса повысилась"))

    $ rez = renpy.display_menu([(_("{i}продолжить смотреть{/i}"), 0), (_("{i}уйти{/i}"), 1)])
    if rez > 0:
        $ current_room = house[1]
        jump Waiting

    $ renpy.show("Eric fuck 0"+str(fuck_scene)+"a")
    if fuck_scene == 1:
        Max_09 "Чёрт, этот удачливый ублюдок кончил ей прямо в рот, причём, судя по довольному лицу мамы, ей это понравилось! Ну почему таким уродам всегда везёт?! Ладно, надо уходить, а то они сейчас меня заметят..."
    elif fuck_scene == 2:
        Max_08 "Ого! Похоже, мама кончила и... Эрик тоже... Хорошо, что хоть не маме в рот... А она у нас та ещё проказница! Пора сматываться, пока меня не заметили!"
    elif fuck_scene == 3:
        Max_11 "Чёрт, эта сволочь кончила ей прямо в рот и... похоже мама не в восторге от всего этого. Бедная моя мама... это нельзя так просто оставлять! А пока лучше скорее уходить, не хватал ещё чтобы меня увидели..."
    elif fuck_scene == 4:
        Max_10 "Ох, чёрт... наконец-то Эрик кончил и... хорошо, что не в маму... Вот же счастливый сукин сын... залил ей своей спермой всю спину... Пожалуй, не стоит здесь задерживаться, они могут меня увидеть."
    elif fuck_scene == 5:
        Max_10 "Чёрт возьми... он не сдержался и уже кончил... Хотя, это не удивительно, после таких-то скачек! Вот же повезло этой сволочи Эрику! И надо уже уходить, пока меня не заметили!"

    $ spent_time += 20
    $ max_profile.stealth += 0.1
    $ renpy.notify(_("Скрытность Макса повысилась"))
    $ current_room = house[1]
    jump Waiting


label eric_ann_sleep:
    scene location house annroom door-night
    if peeping["ann_sleep"] == 0:
        $ peeping["ann_sleep"] = 1
        menu:
            Max_00 "Кажется, все спят..."
            "{i}заглянуть в окно{/i}":
                scene BG char Ann bed-night-01
                $ renpy.show("Eric sleep-night "+pose3_1)
                $ renpy.show("FG ann-voyeur-night-00"+max_profile.dress)
                if pose3_1 == "01":
                    Max_01 "Похоже, они крепко спят... Совершенно голые! Чёрт, жаль только мама лежит за Эриком и её почти не видно... Почему он такой здоровый?" nointeract
                elif pose3_1 == "02":
                    Max_07 "О, да! Этой ночью мама предстала во всей красе... Полностью голенькая... такая соблазнительная. Только вот обезьяна здесь лишняя повисла!" nointeract
                else:
                    Max_04 "Класс! У моей мамы лучшая попка в мире... а голая она просто сводит с ума! Ещё бы эта гора мышц около неё не лежала..." nointeract
                $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), "sneak"), (_("{i}уйти{/i}"), "exit")])
                if rez != "exit":
                    $ spent_time += 10
                    scene BG char Ann bed-night-02
                    $ renpy.show("Eric sleep-night-closer "+pose3_1)
                    if pose3_1 == "01":
                        Max_03 "Они действительно крепко спят... Может самого интересного и не видно, но мама так элегантно, по-женски, закинула на него свою ножку... Хорошо, что такая жара и дома нет кондиционеров... Так, пора уходить." nointeract
                    elif pose3_1 == "02":
                        Max_02 "Просто с ума сойти можно! Она лежит всего в метре от меня... совсем голая... и мне видно её киску... такая красивая! А этот ублюдок, Эрик, так по-хозяйски облапал её... Врезать бы ему, гаду... Ладно, пора бы мне уже уходить, а то они ещё проснутся." nointeract
                    else:
                        Max_05 "Мама такая красивая... а её кругленькая оттопыренная попка просто чудо! Так завораживает! Как бы мне хотелось потрогать её... Ох, мечты... Только бы они сейчас не проснулась..." nointeract
                    $ rez = renpy.display_menu([(_("{i}уйти{/i}"), "exit")])
            "{i}уйти{/i}":
                pass
        $ spent_time = 10
        jump Waiting
    return


label eric_ann_shower:
    scene location house bathroom door-morning
    if peeping["ann_shower"] == 0:
        $ peeping["ann_shower"] = 1
        $ spent_time = 10
        menu:
            Max_00 "Похоже, мама вместе с Эриком принимают душ... Или что они там ещё могут делать?"
            "{i}заглянуть со двора{/i}":
                pass
            "{i}уйти{/i}":
                return

        $ renpy.notify(_("Скрытность Макса капельку повысилась"))
        $ max_profile.stealth += 0.01
        $ __r1 = renpy.random.choice(["01", "02", "03"])
        $ _chance = GetChance(max_profile.stealth, 3)
        if _chance < 333:
            $ _chance_color = red
        elif _chance > 666:
            $ _chance_color = lime
        else:
            $ _chance_color = orange
        $ ch_vis = str(int(_chance/10)) + "%"
        $ renpy.scene()
        $ renpy.show("Eric shower "+ __r1)
        $ renpy.show("FG shower 00"+max_profile.dress)
        menu:
            Max_07 "Вот это да... Похоже намечается что-то большее, чем просто принять душ! Боюсь даже представить, что будет, если меня поймают, пока я подглядываю... за этим..."
            "{i}продолжить смотреть\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
                pass
            "{i}уйти{/i}":
                jump Waiting
        $ max_profile.stealth += 0.1
        $ renpy.notify(_("Скрытность Макса повысилась"))
        $ characters["ann"].dress_inf = "00a"
        $ spent_time += 10
        if __r1 == "01":
            $ __r2 = renpy.random.choice(["01", "02", "03"])
        elif __r1 == "02":
            $ __r2 = renpy.random.choice(["04", "05"])
        else:
            $ __r2 = renpy.random.choice(["06", "07"])
        scene BG shower-closer
        $ renpy.show("Eric shower-closer "+__r2)
        show FG shower-closer
        if __r1 == "01":
            Max_04 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nОхх... Вот же Эрику повезло... Ведь у мамы такие нежные и ласковые руки! Уже только от одного вида её совершенно голого и мокрого тела можно кончить..." nointeract
        elif __r1 == "02":
            Max_06 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nОхренеть! Вот это страсть! Кажется, они так увлечены друг другом, что им всё равно, увидит их кто-то или нет... И похоже, маме это очень нравится!" nointeract
        else:
            Max_05 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nОго! Эрик трахает маму сзади, да так активно... И... кажется, ей это очень нравится, она даже двигается ему навстречу... и изнывает от страсти!" nointeract
        $ rez = renpy.display_menu([(_("{i}смотреть до конца{/i}"), "sneak"), (_("{i}уйти{/i}"), "exit")])
        if rez == "exit":
            $ current_room = house[6]
            jump Waiting

        $ renpy.show("Eric shower-closer "+__r2+"a")
        if __r1 == "01":
            Max_01 "Ну да! Кто бы сомневался, что Эрик не продержится слишком долго. Мама своё дело знает! Ладно, надо сматываться, пока они меня не заметили!" nointeract
        elif __r1 == "02":
            Max_07 "Ох, чёрт... Эрик уже кончил... Хорошо, что не в маму... Счастливый сукин сын... И она ещё улыбается?! Пора бы мне уходить, а то ещё заметят..." nointeract
        else:
            Max_08 "Чёрт возьми... он уже кончил... Счастливый ублюдок... забрызгал маме всю спину с попкой своей спермой! Нужно уходить, а то они вот-вот меня заметят..." nointeract
        $ rez = renpy.display_menu([(_("{i}уйти{/i}"), "exit")])
        $ current_room = house[6]
        jump Waiting

    return
