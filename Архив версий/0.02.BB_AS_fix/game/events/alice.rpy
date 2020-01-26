

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
            "{i}заглянуть со двора{/i}" if "ladder" not in flags or flags["ladder"] < 2:
                scene Alice bath 01
                $ renpy.show("FG voyeur-bath-00"+max_profile.dress)
                Max_00 "Кажется, Алиса и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но подходить ближе опасно - может заметить..."
                menu:
                    Max_09 "Нужно что-нибудь придумать..."
                    "{i}уйти{/i}":
                        $ flags["ladder"] = 1
            "{i}установить стремянку{/i}" if items["ladder"].have:
                scene BG char Max bathroom-window-00
                $ renpy.show("Max bathroom-window 01"+max_profile.dress)
                Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."

                $ renpy.scene()
                $ renpy.show("Max bathroom-window 02"+max_profile.dress)
                Max_04 "Посмотрим, что у нас тут..."

                $ __r1 = renpy.random.randint(1, 4)

                scene BG bath-00
                $ renpy.show("Alice bath-window 0"+str(__r1))
                show FG bath-00
                if __r1 == 1:
                    menu:
                        Max_03 "Вот это повезло! Алиса как раз собирается принять ванну... Её шикарная попка меня просто завораживает! Так бы любовался и любовался..."
                        "{i}смотреть ещё{/i}":
                            $ spent_time += 10
                            $ renpy.show("Alice bath-window "+renpy.random.choice(["02", "03", "04"]))
                            menu:
                                Max_05 "Чёрт возьми, она меня что, специально дразнит своей мокренькой грудью... Может моя старшая сестренка и стерва, но какая же она горячая! Очень сексуальна..."
                                "{i}уйти{/i}":
                                    $ spent_time += 10
                                    $ characters["alice"].dress_inf = "00aa"
                                    pass
                        "{i}уйти{/i}":
                            pass
                else:
                    menu:
                        Max_05 "Чёрт возьми, она меня что, специально дразнит своей мокренькой грудью... Может моя старшая сестренка и стерва, но какая же она горячая! Очень сексуальна..."
                        "{i}смотреть ещё{/i}":
                            $ spent_time += 10
                            show Alice bath-window 05
                            menu:
                                Max_07 "Эх! Самое интересное продолжалось недолго... Единственное, что напоследок остаётся сделать, это насладится её бесподобной попкой!"
                                "{i}уйти{/i}":
                                    $ spent_time += 10
                                    $ characters["alice"].dress_inf = "04aa"
                                    pass
                        "{i}уйти{/i}":
                            pass

            "{i}уйти{/i}":
                pass
        $ spent_time += 10
        jump Waiting
    return


label alice_sleep_night:
    scene location house aliceroom door-night
    if peeping["alice_sleep"] == 0:
        $ peeping["alice_sleep"] = 1
        menu:
            Max_00 "Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья..."
            "{i}заглянуть в окно{/i}":
                $ spent_time = 10
                scene BG char Alice bed-night-01
                $ renpy.show("Alice sleep-night "+pose3_2)
                $ renpy.show("FG alice-voyeur-night-00"+max_profile.dress)
                if pose3_2 == "01":
                    Max_07 "О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела в этом полупрозрачном белье хочется смотреть вечно!" nointeract
                elif pose3_2 == "02":
                    Max_04 "Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою попку для меня во всей красе." nointeract
                else:
                    Max_01 "Обалденно! Сестрёнка спит выгнув спину, отчего её грудь торчит, как два холмика... Соблазнительно..." nointeract
                $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), "sneak"), (_("{i}уйти{/i}"), "exit")])
                if rez != "exit":
                    $ spent_time += 10
                    scene BG char Alice bed-night-02
                    $ renpy.show("Alice sleep-night-closer "+pose3_2)
                    if pose3_2 == "01":
                        Max_03 "Да уж... Её обворожительной попкой можно любоваться бесконечно... Так и хочется по ней шлёпнуть... Правда, тогда это будет последнее, что я сделаю в жизни. Так что лучше потихоньку уходить..." nointeract
                    elif pose3_2 == "02":
                        Max_02 "Класс! Может Алиса мне и сестра, но рядом с этой упругой попкой я бы пристроился с огромным удовольствием... Но пора уходить, а то ещё проснётся..." nointeract
                    else:
                        Max_01 "Чёрт, какая же она притягательная, когда лежит вот так... Так и хочется занырнуть между этих сисечек и её стройных ножек! Только бы она сейчас не проснулась..." nointeract
                    $ rez = renpy.display_menu([(_("{i}уйти{/i}"), "exit")])
            "{i}уйти{/i}":
                pass
        jump Waiting
    return


label alice_sleep_morning:
    scene location house aliceroom door-morning
    if peeping["alice_sleep"] == 0:
        $ peeping["alice_sleep"] = 1
        menu:
            Max_00 "Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья..."
            "{i}заглянуть в окно{/i}":
                $ spent_time = 10
                scene BG char Alice bed-morning-01
                $ renpy.show("Alice sleep-morning "+pose3_2)
                $ renpy.show("FG alice-voyeur-morning-00"+max_profile.dress)
                if pose3_2 == "01":
                    Max_07 "Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть ее классную, почти голую фигурку как следует... " nointeract
                elif pose3_2 == "02":
                    Max_01 "Чёрт! Хоть она и спит, но прямо лицом ко мне... И тем не менее, насладится красотой её тела я могу, и ещё как..." nointeract
                else:
                    Max_02 "Вот это да! От таких соблазнительных изгибов можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка!" nointeract
                $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), "sneak"), (_("{i}уйти{/i}"), "exit")])
                if rez != "exit":
                    $ spent_time += 10
                    scene BG char Alice bed-morning-02
                    $ renpy.show("Alice sleep-morning-closer "+pose3_2)
                    if pose3_2 == "01":
                        Max_05 "/Ох, от такого вида в голове остаются лишь самые пошлые мысли... Как же я хочу помять эту попку! И стянуть эти трусики... и ещё... пожалуй, пока она не проснулась, тихонько отсюда уйти." nointeract
                    elif pose3_2 == "02":
                        Max_03 "О, да! Не лечь и не приобнять эту нежную попку – настоящее преступление... Только вот Алиса посчитает иначе и оторвёт мне голову прямо здесь. Так что лучше потихоньку уходить..." nointeract
                    else:
                        Max_02 "Вот чёрт! С каким же огромным удовольствием я бы сел рядом с ней, запустил свои руки под её белье и ласкал эти упругие сисечки всё утро... Эх, хороша сестрёнка, но пора уходить... Если она проснётся, мне точно не поздоровится." nointeract
                    $ rez = renpy.display_menu([(_("{i}уйти{/i}"), "exit")])
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
            "{i}заглянуть со двора{/i}":
                jump .start_peeping
            "{i}уйти{/i}":
                jump .end_peeping

        label .start_peeping:
            $ renpy.notify(_("Скрытность Макса капельку повысилась"))
            $ max_profile.stealth += 0.01
            $ __ran1 = renpy.random.randint(1, 4)

            $ _chance = GetChance(max_profile.stealth, 3, 900)
            if _chance < 333:
                $ _chance_color = red
            elif _chance > 666:
                $ _chance_color = lime
            else:
                $ _chance_color = orange
            $ ch_vis = str(int(_chance/10)) + "%"
            scene image ("Alice shower 0"+str(__ran1))
            $ renpy.show("FG shower 00"+max_profile.dress)
            menu:
                Max_07 "Ого... Голая Алиса всего в паре метров от меня! Как же она хороша... Главное, чтобы она меня не заметила, а то ведь убьёт на месте."
                "{i}продолжить смотреть\n{color=[_chance_color]}(Скрытность. Шанс: [ch_vis]){/color}{/i}":
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
                if __ran1 % 2 > 0:
                    Max_01 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nСупер! С распущенными волосами моя старшая сестрёнка становится очень сексуальной... Ухх, помылить бы эти сисечки, как следует..."
                else:
                    Max_01 "{color=[lime]}{i}Вы остались незамеченным!{/i}{/color} \nО, да... Перед мокренькой Алисой сложно устоять! Особенно, когда она так соблазнительно крутит своей попкой..."
            elif RandomChance(_chance):
                $ peeping["alice_shower"] = 2
                $ max_profile.stealth += 0.05
                $ renpy.notify(_("Скрытность Макса немного повысилась"))
                $ characters["alice"].dress_inf = "00aa"
                $ __ran1 = renpy.random.randint(7, 8)
                scene BG shower-closer
                show image ("Alice shower-closer 0"+str(__ran1))
                show FG shower-closer
                Max_09 "{color=[orange]}{i}Кажется, Алиса что-то заподозрила!{/i}{/color}\nОх, чёрт! Нужно скорее уносить ноги, пока они ещё есть..."
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
                    Alice_12 "{color=[orange]}{i}Вас заметили!{/i}{/color}\nМакс!!! Ты за мной подглядываешь?! Ты труп! Твоё счастье, что я сейчас голая... Но ничего, я маме всё расскажу, она тебя накажет!"
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
    $ renpy.show("Max tv 00"+max_profile.dress)
    return


label alice_morning_closer:
    scene BG char Alice morning-closer
    $ renpy.show("Alice morning-closer "+pose3_2+characters["alice"].dress)

    return


label alice_evening_closer:
    scene BG char Alice evening-closer
    $ renpy.show("Alice evening-closer "+pose3_2+characters["alice"].dress)
    return
