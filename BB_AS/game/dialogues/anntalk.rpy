
label AnnTalkStart:

    $ dial = TalkMenuItems()

    $ __CurShedRec = GetScheduleRecord(schedule_ann, day, tm)
    if __CurShedRec.talklabel is not None:
        call expression __CurShedRec.talklabel

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
            call expression talks[rez].label
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

    $ __CurShedRec = GetScheduleRecord(schedule_ann, day, tm)
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
            $ renpy.show("Max tv-closer "+pose3_1+max_profile.dress)
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
