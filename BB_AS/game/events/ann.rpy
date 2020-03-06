################################################################################
## события Анны

label ann_sleep:
    scene location house annroom door-night
    if peeping["ann_sleep"] == 0:
        $ peeping["ann_sleep"] = 1
        menu:
            Max_00 "В это время мама обычно спит.\nМне кажется, не стоит её будить..."
            "{i}заглянуть в окно{/i}":
                scene BG char Ann bed-night-01
                $ renpy.show("Ann sleep-night "+pose3_3)
                $ renpy.show("FG ann-voyeur-night-00"+mgg.dress)
                if pose3_3 == "01":
                    Max_01 "Класс! Мама спит... Даже не верится, что у этой конфетки трое детей... В жизни бы в такое не поверил!" nointeract
                elif pose3_3 == "02":
                    Max_04 "О, да! Какая у мамы попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь... Просто супер!" nointeract
                else:
                    Max_07 "Обалденно! Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!" nointeract
                $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), "sneak"), (_("{i}уйти{/i}"), "exit")])
                if rez != "exit":
                    $ spent_time += 10
                    scene BG char Ann bed-night-02
                    $ renpy.show("Ann sleep-night-closer "+pose3_3)
                    if pose3_3 == "01":
                        Max_03 "Чёрт, у меня самая аппетитная мама на свете! Вот бы снять с неё всё белье и пристроиться сзади... Но лучше потихоньку уходить, пока она не проснулась." nointeract
                    elif pose3_3 == "02":
                        Max_02 "Ухх! Так и хочется прижаться к этой обворожительной попке и шалить всю ночь... Но пора уходить, а то она может проснуться." nointeract
                    else:
                        Max_05 "Вот это да! От вида этих раздвинутых ножек становится всё равно, что она моя мама... Слишком соблазнительно! Только бы она сейчас не проснулась..." nointeract
                    $ rez = renpy.display_menu([(_("{i}уйти{/i}"), "exit")])
            "{i}уйти{/i}":
                pass
        $ spent_time = 10
        jump Waiting
    return


label ann_shower:
    scene location house bathroom door-morning
    if peeping["ann_shower"] == 3:
        Max_00 "Я уже попался сегодня на подглядывании за мамой. Не стоит злить ее еще больше."
        return
    elif peeping["ann_shower"] == 1:
        Max_00 "Я уже подсматривал сегодня за мамой. Не стоит искушать судьбу слишком часто."
        return
    elif  peeping["ann_shower"] == 2:
        Max_00 "Сегодня мама и так сегодня едва не поймала меня. Не стоит искушать судьбу слишком часто."
        return
    elif peeping["ann_shower"] > 3:
        menu:
            Max_00 "Мама сейчас принимает душ..."
            "{i}уйти{/i}":
                return
    else:
        $ peeping["ann_shower"] = 4
        menu:
            Max_00 "Похоже, мама принимает душ..."
            "{i}заглянуть со двора{/i}":
                jump .start_peeping
            "{i}воспользоваться стремянкой{/i}" if flags["ladder"] > 2:
                jump .ladder
            "{i}уйти{/i}":
                jump .end_peeping

    label .ladder:
        $ renpy.scene()
        $ renpy.show("Max bathroom-window-morning 01"+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ __r1 = renpy.random.choice(['a','b','c','d'])

        scene BG bathroom-morning-00
        $ renpy.show("Ann bath-window-morning "+renpy.random.choice(['01', '02', '03'])+__r1)
        show FG bathroom-morning-00
        if __r1 == 'a':
            Max_07 "Да-а... Распахнутый халатик на маме - это просто изумительное шоу! Такие соблазнительные сосочки... да ещё и так близко... Ммм..."
        elif __r1 == 'b':
            Max_05 "О, да! Мама решила не надевать трусики и правильно сделала, потому что увидеть эту киску с утра пораньше - просто сказка!"
        elif __r1 == 'c':
            Max_03 "Вот это повезло... Мама в одних лишь трусиках, а её упругая грудь предстаёт передо мной во всей своей красе! Так бы любовался и любовался ей..."
        else:
            Max_06 "Ничего себе! Такое зрелище не каждый раз увидишь - она же совершенно голая! Только бы со стремянки не упасть от такого вида... Как было бы круто потискать все ёё округлости!"

        Max_00 "Ладно, пора уходить, а то еще заметит неровён час..."
        jump .end_peeping

    label .start_peeping:
        $ notify_list.append(_("Скрытность Макса капельку повысилась"))
        $ mgg.stealth += 0.03
        $ __ran1 = renpy.random.randint(1, 4)

        $ _chance = GetChance(mgg.stealth, 3)
        $ _chance_color = GetChanceColor(_chance)
        $ ch_vis = str(int(_chance/10)) + "%"
        scene image ("Ann shower 0"+str(__ran1))
        $ renpy.show("FG shower 00"+mgg.dress)
        menu:
            Max_07 "Ух, аж завораживает! Повезло же, что у меня такая сексуальная мама...  Надеюсь, она меня не заметит..."
            "{i}продолжить смотреть\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
                jump .closer_peepeng
            "{i}уйти{/i}":
                jump .end_peeping

    label .closer_peepeng:
        if RandomChance(_chance):
            $ peeping["ann_shower"] = 1
            $ mgg.stealth += 0.2
            $ notify_list.append(_("Скрытность Макса повысилась"))
            $ chars["ann"].dress_inf = "00a"
            $ __ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            show image ("Ann shower-closer 0"+str(__ran1))
            show FG shower-closer
            if __ran1 % 2 > 0:
                Max_03 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nОбалдеть можно! Не каждый день выпадает такое счастье, любоваться этой красотой! Её большая упругая грудь и стройная фигурка просто загляденье..."
            else:
                Max_05 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nО, да! Зрелище просто потрясающее... Такой сочной попке может позавидовать любая женщина! Какая мокренькая..."
        elif RandomChance(_chance):
            $ peeping["ann_shower"] = 2
            $ mgg.stealth += 0.1
            $ notify_list.append(_("Скрытность Макса немного повысилась"))
            $ chars["ann"].dress_inf = "00a"
            $ __ran1 = renpy.random.randint(7, 8)
            scene BG shower-closer
            show image ("Ann shower-closer 0"+str(__ran1))
            show FG shower-closer
            Max_12 "{color=[orange]}{i}Кажется, мама что-то заподозрила!{/i}{/color}\nУпс... надо бежать, пока она меня не увидела!"
            jump .end_peeping
        else:
            $ peeping["ann_shower"] = 3
            $ mgg.stealth += 0.05
            $ notify_list.append(_("Скрытность Макса чуть-чуть повысилась"))
            $ __ran1 = renpy.random.choice(["09", "10"])
            scene BG shower-closer
            show image ("Ann shower-closer "+__ran1)
            show FG shower-closer
            menu:
                Ann_16 "{color=[orange]}{i}Вас заметили!{/i}{/color}\nМакс!!! Ты что, подглядываешь за мной? Тебе должно быть стыдно! Быстро отвернись!!! Нас ждёт серьёзный разговор..."
                "{i}Бежать{/i}":
                    jump .end_peeping

    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting


label ann_yoga:
    scene BG char Ann yoga-00
    if int(tm[3:4])%3 == 0: # смена позы каждые 10 минут
        $ renpy.show("Ann yoga "+pose3_1)
    elif int(tm[3:4])%3 == 1:
        $ renpy.show("Ann yoga "+pose3_2)
    else:
        $ renpy.show("Ann yoga "+pose3_3)
    return


label ann_cooking:
    scene BG cooking-00
    $ renpy.show("Ann cooking 01"+chars["ann"].dress)
    return


label ann_cooking_closer:
    scene BG cooking-01
    $ renpy.show("Ann cooking-closer "+pose3_3+chars["ann"].dress)
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
                    $ chars["ann"].dress_inf = "02"
                elif __ran1 == "02":
                    $ chars["ann"].dress_inf = "02b"
                elif __ran1 == "03":
                    $ chars["ann"].dress_inf = "02a"
                else:
                    $ chars["ann"].dress_inf = "00"
                menu:
                    Ann_13 "Макс! Я же учила тебя стучаться!"
                    "Хорошо выглядишь, мам!":
                        $ __mood += 30
                        Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?"
                        Max_00 "Конечно, мам!"
                    "Отличный зад!":
                        $ __mood -= 30
                        Ann_19 "Что?! Макс! А ну-ка быстро выйди и закрой дверь!"
                        Max_00 "Как скажешь, мам..."
                    "Ой, извини. Я забыл...":
                        $ __mood -= 10
                        Ann_07 "Ну, бывает. Я сама ещё не привыкла к тому, что замков нигде нет. Ладно, дорогой. Подожди за дверью, пока мама одевается. хорошо?"
                        Max_00 "Хорошо, мам..."
                $ AddRelMood("ann", 0, __mood)
            "{i}заглянуть в окно{/i}":
                scene BG char Ann voyeur-00
                if __ran1 == "01":
                    $ chars["ann"].dress_inf = "02c"
                elif __ran1 == "02":
                    $ chars["ann"].dress_inf = "02d"
                elif __ran1 == "03":
                    $ chars["ann"].dress_inf = "02a"
                else:
                    $ chars["ann"].dress_inf = "02b"

                $ renpy.show("Ann voyeur "+__ran1)
                $ renpy.show("FG voyeur-morning-00"+mgg.dress)
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
                        $ __mood += 30
                        Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?"
                        Max_00 "Конечно, мам!"
                    "Ой, извини...":
                        Ann_07 "И Макс... Постарайся больше не входить без стука, хорошо?"
                        Max_00 "Хорошо, мам..."
                $ AddRelMood("ann", 0, __mood)
            # "{i}заглянуть в окно{/i}":
            #     # if __ran1 == "01":
            #     #     $ chars["lisa"].dress_inf = "02d"
            #     # else:
            #     #     $ chars["lisa"].dress_inf = "02c"
            #
            #     scene image "Ann voyeur "+__ran1
            #     $ renpy.show("FG voyeur-morning-00"+mgg.dress)
            #     Max_01 "Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но если заметит меня в зеркало, мне конец."
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label ann_resting:
    if tm < "19:00":
        scene BG char Ann relax-morning-01
        $ renpy.show("Ann relax-morning "+pose3_3+chars["ann"].dress)
    else:
        scene BG char Ann relax-evening-01
        $ renpy.show("Ann relax-evening "+pose3_3+chars["ann"].dress)
    return


label ann_read:
    scene BG reading
    $ renpy.show("Ann reading "+pose3_3+chars["ann"].dress)
    return


label ann_swim:

    scene image "Ann swim "+pose3_3+"a"
    return


label ann_sun:
    scene BG char Ann sun
    $ renpy.show("Ann sun "+pose3_3+"a")
    return


label ann_alice_sun:
    scene BG char Ann Alice 2sun-00
    $ renpy.show("Alice 2sun "+pose3_2)
    $ renpy.show("Ann 2sun "+pose3_3)
    return


label ann_alice_swim:
    $ renpy.scene()
    $ renpy.show("BG char Ann Alice 2swim-"+pose3_1)
    return


label ann_bath:
    scene location house bathroom door-evening
    if peeping["ann_bath"] != 0:
        return

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
                    jump .end
                "{i}уйти{/i}":
                    jump .end
        "{i}заглянуть со двора{/i}" if "ladder" not in flags or flags["ladder"] < 2:
            scene Ann bath 01
            $ renpy.show("FG voyeur-bath-00"+mgg.dress)
            Max_00 "Эх... жаль, что стекло частично матовое. Так ничего не разглядеть! А если подобраться ближе, то мама может заметить..."
            menu:
                Max_09 "Нужно что-нибудь придумать..."
                "{i}уйти{/i}":
                    $ flags["ladder"] = 1
                    jump .end
        "{i}установить стремянку{/i}" if items["ladder"].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show("Max bathroom-window-evening 01"+mgg.dress)
            Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
            $ flags["ladder"] = 3
            $ items["ladder"].have = False
            $ items["ladder"].InShop = False
            jump .ladder
        "{i}воспользоваться стремянкой{/i}" if flags["ladder"] > 2:
            jump .ladder
        "{i}уйти{/i}":
            jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show("Max bathroom-window-evening 02"+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."

        $ __r1 = renpy.random.randint(1, 4)

        scene BG bath-00
        $ renpy.show("Ann bath-window 0"+str(__r1))
        show FG bath-00
        if __r1 == 1:
            menu:
                Max_03 "Ох, как горячо! Разумеется, я не про воду, а про её внешний вид. Ухх... Мама потрясающе выглядит..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show("Ann bath-window "+renpy.random.choice(["02", "03", "04"]))
                    menu:
                        Max_05 "Ух ты, аж завораживает! Мамины водные процедуры могут посоперничать с самыми горячими эротическими роликами! Эта упругая грудь и эти длинные стройные ножки сведут с ума кого угодно..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ chars["ann"].dress_inf = "00a"
                            jump .end
                "{i}уйти{/i}":
                    jump .end
        else:
            menu:
                Max_05 "Ух ты, аж завораживает! Мамины водные процедуры могут посоперничать с самыми горячими эротическими роликами! Эта упругая грудь и эти длинные стройные ножки сведут с ума кого угодно..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Ann bath-window 05
                    menu:
                        Max_07 "Эх! Похоже, самое интересное закончилось... Хотя, смотреть как мама вытирает своё мокрое и соблазнительное тело не менее приятно! Ох, какая же у неё попка..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ chars["ann"].dress_inf = "04a"
                            jump .end
                "{i}уйти{/i}":
                    jump .end

    label .end:
        $ config.menu_include_disabled = False
        $ spent_time += 10
        jump Waiting


label ann_tv:
    scene BG lounge-tv-00
    $ renpy.show("Ann tv "+pose3_3)
    return


label ann_tv_closer:
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer "+pose3_3)
    $ renpy.show("Max tv 00"+mgg.dress)
    return
