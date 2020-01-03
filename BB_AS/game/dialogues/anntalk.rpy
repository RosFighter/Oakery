
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
        if renpy.has_label(rez): # если такая метка сушествует, запускаем ее
            call expression rez
        jump AnnTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Ann_cooldown:
    Ann_18 "Макс, давай сменим тему..."
    Max_00 "Ок, мам..."
    return


label ann_ask_money:

    $ __CurShedRec = GetScheduleRecord(schedule_ann, day, tm)
    if __CurShedRec is None:
        "При нормальном развитии событий эта строка не должна была появится. Сообщите разработчику."
        return
    if __CurShedRec.dress == "yoga": ## Анна занимается йогой
         menu:
            Ann_05 "Макс, ты же видишь, я сейчас занята... Выбери более подходящий момент, пожалуйста..."
            "Точно, извини...":
                jump AfterWaiting
    elif __CurShedRec.dress == "swim" or __CurShedRec.dress == "casual3": ## Анна загорает, плавает или смотрит ТВ
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
    $ characters["ann"].mood += 5
    $ HintRelMood("ann", 0, 5)
    $ dcv["buyfood"].stage = 0
    return


label ann_aboutpool:
    menu:
        Ann_05 "Спасибо, Макс, на недельку этого должно хватить."
        "Ага...":
            pass
    $ characters["ann"].mood += 5
    $ HintRelMood("ann", 0, 5)
    $ dcv["clearpool"].stage = 0
    return
