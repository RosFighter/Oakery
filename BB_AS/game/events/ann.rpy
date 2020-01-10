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
                    $ renpy.show("Ann sleep-night "+pose3_3)
                    $ renpy.show("FG ann-voyeur-night-00"+max_profile.dress)
                else:
                    scene BG char Ann bed-morning-01
                    $ renpy.show("Ann sleep-morning "+pose3_3)
                    $ renpy.show("FG ann-voyeur-morning-00"+max_profile.dress)
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
            $ renpy.show("FG shower 00"+max_profile.dress)
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
                $ characters["ann"].dress_inf = "00a"
                $ __ran1 = renpy.random.randint(1, 6)
                scene BG shower-closer
                show image ("Ann shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color} \nУх, аж завораживает! Хоть бы меня не заметила..."
            elif RandomChance(_chance):
                $ peeping["ann_shower"] = 2
                $ max_profile.stealth += 0.05
                $ renpy.notify(_("Скрытность Макса немного повысилась"))
                $ characters["ann"].dress_inf = "00a"
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
        $ renpy.show("Ann yoga "+pose3_1)
    elif int(tm[3:4])%3 == 1:
        $ renpy.show("Ann yoga "+pose3_2)
    else:
        $ renpy.show("Ann yoga "+pose3_3)
    return


label ann_cooking:
    scene BG cooking-00
    $ renpy.show("Ann cooking 01"+characters["ann"].dress)
    return


label ann_cooking_closer:
    scene BG cooking-01
    $ renpy.show("Ann cooking-closer "+pose3_3+characters["ann"].dress)
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
                    $ characters["ann"].dress_inf = "02"
                elif __ran1 == "02":
                    $ characters["ann"].dress_inf = "02b"
                elif __ran1 == "03":
                    $ characters["ann"].dress_inf = "02a"
                else:
                    $ characters["ann"].dress_inf = "00"
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
                $ characters["ann"].mood += __mood
            "{i}заглянуть в окно{/i}":
                scene BG char Ann voyeur-00
                if __ran1 == "01":
                    $ characters["ann"].dress_inf = "02c"
                elif __ran1 == "02":
                    $ characters["ann"].dress_inf = "02d"
                elif __ran1 == "03":
                    $ characters["ann"].dress_inf = "02a"
                else:
                    $ characters["ann"].dress_inf = "02b"

                $ renpy.show("Ann voyeur "+__ran1)
                $ renpy.show("FG voyeur-morning-00"+max_profile.dress)
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
            #     #     $ characters["lisa"].dress_inf = "02d"
            #     # else:
            #     #     $ characters["lisa"].dress_inf = "02c"
            #
            #     scene image "Ann voyeur "+__ran1
            #     $ renpy.show("FG voyeur-morning-00"+max_profile.dress)
            #     Max_01 "Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но если заметит меня в зеркало, мне конец."
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label ann_resting:
    scene BG char Ann relax-morning-01
    $ renpy.show("Ann relax-morning "+pose3_3+characters["ann"].dress)
    return


label ann_read:
    scene BG reading
    $ renpy.show("Ann reading "+pose3_3+characters["ann"].dress)
    return


label ann_swim:

    scene image "Ann swim "+pose3_3+characters["ann"].dress
    return


label ann_sun:
    scene BG char Ann sun
    $ renpy.show("Ann sun "+pose3_3)
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
                $ renpy.show("FG voyeur-bath-00"+max_profile.dress)
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
    $ renpy.show("Ann tv "+pose3_3)
    return


label ann_tv_closer:
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer "+pose3_3)
    return
