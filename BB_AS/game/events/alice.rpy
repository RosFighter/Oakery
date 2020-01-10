

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
                $ renpy.show("FG voyeur-bath-00"+max_profile.dress)
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
                    $ renpy.show("Alice sleep-night "+pose3_2)
                    $ renpy.show("FG alice-voyeur-night-00"+max_profile.dress)
                else:
                    scene BG char Alice bed-morning-01
                    $ renpy.show("Alice sleep-morning "+pose3_2)
                    $ renpy.show("FG alice-voyeur-morning-00"+max_profile.dress)
                menu:
                    Max_07 "О, да! Моя старшая сестренка выглядит потрясающе... \nНа изгибы ее тела в этом полупрозрачном белье хочется смотреть вечно!"
                    "{i}прокрасться в комнату{/i}":
                        $ spent_time += 10
                        if tm < "06:00":
                            scene BG char Alice bed-night-02
                            $ renpy.show("Alice sleep-night-closer "+pose3_2)
                        else:
                            scene BG char Alice bed-morning-02
                            $ renpy.show("Alice sleep-morning-closer "+pose3_2)
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
            $ renpy.show("FG shower 00"+max_profile.dress)
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
                $ characters["alice"].dress_inf = "00aa"
                $ __ran1 = renpy.random.randint(1, 6)
                scene BG shower-closer
                show image ("Alice shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_01 "{color=[lime]}{i}Удалось незаметно подкрасться!{/i}{/color} \nМожно целую вечность смотреть, как сестренка принимает душ. Лишь бы она меня не заметила..."
            elif RandomChance(_chance):
                $ peeping["alice_shower"] = 2
                $ max_profile.stealth += 0.05
                $ renpy.notify(_("Скрытность Макса немного повысилась"))
                $ characters["alice"].dress_inf = "00aa"
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
    $ renpy.show("Alice morning 01"+characters["alice"].dress)
    return


label alice_rest_evening:
    scene BG char Alice evening
    $ renpy.show("Alice evening 01"+characters["alice"].dress)
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
                    $ characters["alice"].dress_inf = "02a"
                else:
                    $ characters["alice"].dress_inf = "02b"

                scene BG char Alice voyeur-00
                $ renpy.show("Alice voyeur "+__ran1)
                $ renpy.show("FG voyeur-morning-00"+max_profile.dress)
                Max_01 "Алиса переодевается... Какой вид! Так. Пора сваливать. Вдруг, кто-то заметит!"
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label alice_dishes:
    scene BG crockery-morning-00
    $ renpy.show("Alice crockery-morning 01"+characters["alice"].dress)
    return


label alice_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show("Alice crockery-closer "+pose3_2+characters["alice"].dress)
    return


label alice_read:
    scene BG reading
    $ renpy.show("Alice reading "+pose3_2+characters["alice"].dress)
    return


label alice_dressed_friend:
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
                #     $ characters["lisa"].dress_inf = "02d"
                # else:
                #     $ characters["lisa"].dress_inf = "02c"

                scene BG char Alice voyeur-00
                $ renpy.show("Alice voyeur "+__ran1)
                $ renpy.show("FG voyeur-morning-00"+max_profile.dress)
                Max_01 "Алиса переодевается... Какой вид! Так. Пора сваливать. Вдруг, кто-то заметит!"
            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label alice_sun:
    scene BG char Alice sun
    $ renpy.show("Alice sun "+pose2_2+characters["alice"].dress)
    return


label alice_swim:

    scene image "Alice swim "+pose3_2+characters["alice"].dress
    return


label alice_cooking_dinner:
    scene BG cooking-00
    $ renpy.show("Alice cooking 01"+characters["alice"].dress)
    return


label alice_cooking_closer:
    scene BG cooking-01
    $ renpy.show("Alice cooking-closer "+pose3_2+characters["alice"].dress)
    return


label alice_tv:
    scene BG lounge-tv-00
    $ renpy.show("Alice tv "+pose3_2+characters["alice"].dress)
    return


label alice_tv_closer:
    scene BG lounge-tv-01
    $ renpy.show("Alice tv-closer "+pose3_2+characters["alice"].dress)
    return


label alice_morning_closer:
    scene BG char Alice morning-closer
    $ renpy.show("Alice morning-closer "+pose3_2+characters["alice"].dress)

    return


label alice_evening_closer:
    scene BG char Alice evening-closer
    $ renpy.show("Alice evening-closer "+pose3_2+characters["alice"].dress)
    return
