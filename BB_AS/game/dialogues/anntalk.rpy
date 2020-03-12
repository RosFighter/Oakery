
label AnnTalkStart:

    $ dial = TalkMenuItems()

    $ __CurShedRec = GetPlan(plan_ann, day, tm)
    if __CurShedRec.talklabel is not None:
        call expression __CurShedRec.talklabel from _call_expression_3

    if len(dial) > 0:
        $ dial.append((_("{i}уйти{/i}"), "exit"))
    else:
        $ dial.append((_("Нет, ничего..."), "exit"))


    Ann_00 "Что-то случилось, дорогой?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        $ __mood = GetMood("ann")[0]
        if __mood < talks[rez].mood:
            if __mood < -2: # Настроение -4... -3, т.е. всё ну совсем плохо
                jump Ann_badbadmood
            elif __mood < 0: # Настроение -2... -1, т.е. всё ещё всё очень плохо
                jump Ann_badmood
            else: # Настроение хорошее, но ещё недостаточное для разговора
                jump Ann_normalmood
        elif talks[rez].kd_id != "" and talks[rez].kd_id in cooldown and not ItsTime(cooldown[talks[rez].kd_id]):
            jump Ann_cooldown
        elif renpy.has_label(talks[rez].label): # если такая метка сушествует, запускаем ее
            call expression talks[rez].label from _call_expression_4
        jump AnnTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Ann_badbadmood:
    menu:
        Ann_18 "Макс, я сейчас в очень плохом настроении и не хочу с тобой разговаривать!"
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Ann_asksorry


label Ann_badmood:
    menu:
        Ann_18 "Макс, я сейчас не в настроении и не хочу разговаривать."
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Ann_asksorry


label Ann_asksorry:
    menu:
        Ann_01 "Да? Я тебя слушаю?"
        "В другой раз...":
            jump Waiting


label Ann_normalmood:
    menu:
        Ann_18 "Макс, не сейчас, хорошо?"
        "Ок...":
            jump Waiting


label Ann_cooldown:
    Ann_18 "Макс, давай сменим тему..."
    Max_00 "Ок, мам..."
    jump AfterWaiting


label ann_ask_money:

    $ __CurShedRec = GetPlan(plan_ann, day, tm)
    if __CurShedRec is None:
        "При нормальном развитии событий эта строка не должна была появится. Сообщите разработчику."
        return
    if __CurShedRec.name == "yoga": ## Анна занимается йогой
         menu:
            Ann_05 "Макс, ты же видишь, я сейчас занята... Выбери более подходящий момент, пожалуйста..."
            "Точно, извини...":
                jump AfterWaiting
    elif __CurShedRec.name == "swim" or __CurShedRec.name == "tv": ## Анна загорает, плавает или смотрит ТВ
         menu:
            Ann_05 "Очень смешно, Макс. Ты видишь у меня карманы? Нет? Выбери более подходящий момент, пожалуйста..."
            "Точно, извини...":
                jump AfterWaiting

    $ talk_var["ask_money"] = 1
    $ spent_time = 10
    menu:
        Ann_00 "Макс, тебе не стыдно просить деньги у мамы, хотя сам целыми днями дома сидишь и ничего не делаешь?"
        "Мне стыдно, но очень нужны деньги...":
            $ money += 20
            menu:
                Ann_04 "Ладно, держи. И найди себе уже работу, хотя бы через интернет. Нам лишние деньги не помешают..."
                "Ага! Спасибо, мам!":
                    jump AfterWaiting
                "Может быть, я могу что-то сделать?":
                    pass
        "Я могу сделать какую-то работу, чтобы не просто так выпрашивать деньги...":
            pass
        "Ты права, стыдно. В другой раз...":
            jump AfterWaiting

    menu .work:
        Ann_01 "И что же, например?"
        "Может быть, почистить бассейн?" if dcv["clearpool"].done:
            $ dcv["clearpool"].done = False
            $ dcv["clearpool"].stage = 1
            $ money += 40
            menu:
                Ann_04 "Отличная идея, Макс! Лучше уж я заплачу тебе $40, чем нанимать какого-то человека. Держи. Да, лучше это делать пока светло и никого нет."
                "Конечно!":
                    jump AfterWaiting
                "Может я могу ещё что-то сделать?":
                    jump .work
        "Ну, могу заказать продукты" if dcv["buyfood"].done:
            $ dcv["buyfood"].done = False
            $ dcv["buyfood"].stage = 1
            $ money += 60
            menu:
                Ann_04 "Хорошая мысль, Макс. Я дам тебе $50 на продукты и авансом $10 за твои услуги, так сказать. Устроит?"
                "Конечно!":
                    jump AfterWaiting
                "Может я могу ещё что-то сделать?":
                    jump .work
        # "Может быть, тебе что-то нужно из косметики?" if dcv["ordercosm"].done:
        #     $ dcv["ordercosm"].done = False
        #     $ money += 115
        #     menu:
        #         Ann_04 "Ты знаешь, мне и правда нужно кое-что заказать. Купи для меня набор косметики, вот $100 и $15 сверху за твои труды, хорошо?"
        #         "Конечно!":
        #             jump AfterWaiting
        #         "Может я могу ещё что-то сделать?":
        #             jump .work
        "Не знаю. Видимо, ничего...":
            jump AfterWaiting


label ann_aboutfood:
    menu:
        Ann_05 "Спасибо, Макс. Продукты я или Алиса заберём, когда привезут. Об этом не беспокойся."
        "Супер!":
            pass
    $ AddRelMood("ann", 0, 50)
    $ dcv["buyfood"].stage = 0
    return


label ann_aboutpool:
    menu:
        Ann_05 "Спасибо, Макс, на недельку этого должно хватить."
        "Ага...":
            pass
    $ AddRelMood("ann", 0, 50)
    $ dcv["clearpool"].stage = 0
    return


label ann_talk_tv:
    $ talk_var["ann_tv"] = 1
    menu:
        Ann_00 "Да так, всё подряд. Садись рядом, если хочешь..."
        "Конечно! Что смотреть будем?":
            $ SetCamsGrow(house[4], 140)
            $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
            Ann_05 "Да вот, по кабельному какой-то фильм сейчас начнётся..."
            Max_02 "{i}Мама так близко... В одном полотенце... Даже не знаю о чём фильм, о нём я думать точно не могу...{/i}"
            menu:
                Ann_05 "Ну что, отличный фильм, как мне кажется! А тебе понравилось, Макс?"
                "Да, очень!":
                    $ __mood = 50
                    Ann_07 "Ну я рада. Ладно, спасибо что посидел со мной. Пойду в свою комнату, хватит фильмов на сегодня..."
                    Max_04 "Ага, давай..."
                "Почти также, как сидеть рядом с тобой...":
                    $ __mood = 40
                    Ann_12 "Что, прости? Не поняла..."
                    Max_00 "Не бери в голову, это я так, пошутил неудачно..."
                    Ann_05 "Ясно. Ну, спасибо за компанию. Пойду в свою комнату, хватит с меня фильмов на сегодня..."
                    Max_03 "Ага, хорошо посидели..."
            $ spent_time = max((60 - int(tm[-2:])), 40)
            $ AddRelMood("ann", 0, __mood)
            $ cur_ratio = 0.5
        "В другой раз...":
            menu:
                Ann_05 "Как хочешь, дорогой. А я что-нибудь посмотрю..."
                "Не буду тебе мешать...":
                    pass
    jump Waiting


label Ann_MorningWood:
    Ann_01 "Макс, не переживай ты так. Я всё прекрасно понимаю, у мальчиков это бывает..."
    Max_04 "Я рад, что ты понимаешь"
    menu:
        Ann_14 "Но Макс. Лиза ещё маленькая и постарайся, чтобы она не видела твой... тебя. В общем, ты меня понял, да?"
        "А что такого?":
            menu:
                Ann_04 "Что такого? Да то, что девочка не должна видеть здоровенный член своего брата, когда просыпается утром!"
                "Ого, мам...":
                    menu:
                        Ann_07 "Извини, что-то меня занесло. Просто, даже я в шоке была, когда увидела, а что уж говорить про Лизу..."
                        "Значит, тебе понравилось?":
                            Ann_12 "Макс! Я конечно рада, что ты у меня уже такой... большой... Но вообще, я всё сказала. Постарайся ей не показываться в таком виде, ладно?"
                            Max_00 "Ладно, мам..."
                        "Ладно, я всё понял...":
                            pass
                "Разве это должно пугать?":
                    menu:
                        Ann_12 "Ну, взрослую женщину это даже притягивает, но девочке явно рано на такое смотреть, ты меня понял?"
                        "Взрослую женщину притягивает?":
                            Ann_05 "Ну, Макс! Я же не это имела в виду... В общем, этот разговор окончен. Постарайся не травмировать психику Лизы, хорошо?"
                            Max_01 "Хорошо, мам..."
                        "Да, я всё понял!":
                            pass
        "Хорошо, постараюсь...":
            Ann_05 "Вот и молодец. А если такое повторится, просто прикройся, как будто ничего нет..."
            Max_03 "Ну, ты же знаешь, что мне с моим размером это трудно сделать..."
            Ann_12 "Да, понимаю, конечно... Но беседа ушла куда-то не туда. В общем, постарайся не травмировать её психику, хорошо?"
            Max_00 "Хорошо, мам..."
    $ flags["morning_erect"] = 2
    $ spent_time = 20
    jump Waiting


label talk_about_smoking:
    $ renpy.block_rollback()
    $ __mood = 0

    scene BG char Max talk-terrace-00
    show Max talk-terrace 01a
    $ renpy.show("Ann talk-terrace 01"+chars["ann"].dress)
    menu:
        Ann_12 "Макс. Я не уверена, но мне кажется, что чувствую запах сигаретного дыма. К нам кто-то приходил?"
        "Нет, никого не было...":
            pass
        "Может быть, показалось?":
            pass
        "Да это просто Алиса курила!":
            show Max talk-terrace 02a
            $ renpy.show("Ann talk-terrace 02"+chars["ann"].dress)
            jump .smoke
    menu:
        Ann_00 "Точно? Макс, ты ничего не хочешь рассказать?"
        "Нет, мам, нечего рассказывать":
            Ann_01 "Да? Ну, может и правда показалось. Или от соседей надуло... Ладно, давайте ужинать..."
            $ SetPossStage('smoke', 2)
            hide Ann
            show Alice talk-terrace 02a
            menu:
                Alice_03 "Спасибо, Макс, что не сдал меня... Я это ценю."
                "Всегда пожалуйста, сестрёнка!":
                    show Max talk-terrace 03a
                    Alice_05 "Вот можешь же быть не полным придурком... иногда..."
                    Max_01 "Ага. Ладно, давай ужинать"
                    $ AddRelMood('alice', 20, 100)
                    jump StartPunishment
                "Может, ещё сдам...":
                    show Max talk-terrace 02a
                    show Alice talk-terrace 03a
                    menu:
                        Alice_16 "Макс! Ты невыносим. Я уже подумала, что ты нормальный брат, а ты..."
                        "Да я пошутил...":
                            jump .joke
                        "Извини...":
                            jump .sorry
                        "Всё в твоих руках...":
                            jump .sorry
                "Если сделаешь кое-что, то и не сдам...":
                    show Max talk-terrace 02a
                    show Alice talk-terrace 03a
                    menu:
                        Alice_13 "Макс! Опять ты за своё? Не будь придурком!"
                        "Да я пошутил...":
                            jump .joke
                        "Извини...":
                            jump .sorry
                        "Всё в твоих руках...":
                            jump .sorry

        "Вообще-то, Алиса курила...":
            show Max talk-terrace 02a
            $ renpy.show("Ann talk-terrace 02"+chars["ann"].dress)
            jump .smoke

    label .joke:
        show Max talk-terrace 03a
        show Alice talk-terrace 02a
        Alice_12 "Шутник... В общем, я надеюсь, что с этим вопросом разобрались. Уже пора ужинать"
        Max_01 "Ага, пора."
        jump StartPunishment

    label .sorry:
        show Max talk-terrace 03a
        show Alice talk-terrace 02a
        Alice_13 "Макс... А, ничего не буду говорить, бесполезно. Давай ужинать..."
        Max_01 "Ага, давай."
        jump StartPunishment

    menu .smoke:
        Ann_13 "Что?! Ты уверен?"
        "Да, но ей не говори, что это я её сдал!":
            show Max talk-terrace 01a
        "Абсолютно. Сам видел. Днём курила у бассейна!":
            show Max talk-terrace 03a
        "Может быть, мне показалось...":
            pass
    $ SetPossStage('smoke', 1)
    menu:
        Ann_20 "Алиса! Иди сюда, бегом!"
        "Мам, ну не так же...":
            pass
        "Мам, меня не сдавай...":
            pass
    show Alice talk-terrace 01a
    Alice_13 "Что случилось, мам?"
    Ann_19 "Что случилось?! Не притворяйся тут невинной овечкой! Макс говорит, что видел, как ты курила!"
    show Max talk-terrace 02a
    Max_14 "Ну..."

    if flags['smoke.request'] == "money":
        $ __mood -= 300
        Alice_17 "Ну и придурок же ты, Макс! Мы же договорились, а ты..."
        Max_09 "Я передумал..."
    else:
        $ __mood -= 200
        Alice_17 "Ну и придурок же ты, Макс! Стукач!"
        Max_09 "Сама виновата..."

    Ann_12 "Так, всё, Алиса, сейчас я тебя накажу! Снимай свои джинсы!"
    scene BG punish-evening 01
    show Alice punish-evening 01a
    $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)
    Max_07 "Ого..."
    Alice_12 "Что?! Я уже взрослая! Могу делать что хочу, даже курить!"
    Max_08 "Ой, плохой ответ..."
    Ann_19 "Взрослая? С каких пор? Пока ты живёшь со мной под одной крышей, ты моя дочь! Без разговоров, быстро снимай и ложись на мои колени!"
    show Alice punish-evening 02a
    Alice_13 "Мам, но тут же Макс... Что, прямо при нём будешь? Пусть он уйдёт!"
    Ann_18 "Нет, Алиса, пусть смотрит. Это ждёт любого, кто меня разозлит. Быстро ложись на мои колени, кому сказала!"
    scene BG punish-evening 02
    $ renpy.show("Ann punish-evening alice-01"+chars["ann"].dress)
    Alice_13 "Ладно... Только не больно, чтобы, ладно? Ай! Ма-ам!"
    Ann_16 "Давай не мамкай тут! Ты знаешь, что я ненавижу сигареты и мои дети точно курить не будут. Особенно, в моём доме, ясно?!"
    $ renpy.show("Ann punish-evening alice-02"+chars["ann"].dress)
    Alice_13 "Да, ясно, мам... Ай! Я всё поняла! Я больше не буду!"
    scene BG punish-evening 01
    show Alice punish-evening 03a
    $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)
    Ann_12 "Очень на это надеюсь. Так, теперь надевай штаны и садимся ужинать."
    scene BG char Max talk-terrace-00
    show Max talk-terrace 01a
    show Alice talk-terrace 03a
    menu:
        Alice_17 "Ну ты и гад, Макс. Доволен? Ну теперь держись..."
        "Извини, я не хотел, чтобы так...":
            show Max talk-terrace 03a
            $ __mood += 50
            menu:
                Alice_16 "Не хочу тебя больше видеть. Жаль, что придётся..."
                "{i}начать ужин{/i}":
                    pass
        "И что ты сделаешь? Я тебя не боюсь!":
            show Max talk-terrace 04a
            menu:
                Alice_16 "Я не буду тебе ничего говорить, сам всё поймёшь в своё время. Карма штука жестокая, но справедливая..."
                "{i}начать ужин{/i}":
                    pass
    $ AddSchedule(plan_alice, Schedule((1, 2, 3, 4, 5), "13:0", "13:29", "swim", _("в бассейне"), "house", 6, "alice_swim", glow=105))
    $ AddRelMood('alice', -10, __mood)
    $ current_room = house[5]
    $ Distribution()
    jump StartPunishment
