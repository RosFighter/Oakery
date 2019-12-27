
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
    $ talk_var["ask_money"] = 1
    menu:
        Ann_00 "Макс, тебе не стыдно просить деньги у мамы, хотя сам целыми днями дома сидишь и ничего не делаешь?"
        "Мне стыдно, но очень нужны деньги...":
            menu:
                Ann_04 "Ладно, держи. И найди себе уже работу, хотя бы через интернет. Нам лишние деньги не помешают..."
                "Ага! Спасибо, мам!":
                    return
                "Может быть, я могу что-то сделать?":
                    pass
        "Я могу сделать какую-то работу, чтобы не просто так выпрашивать деньги...":
            pass
        "Ты права, стыдно. В другой раз...":
            return

    menu .work:
        Ann_01 "И что же, например?"
        "Может быть, почистить бассейн?":
            pass
        "Ну, могу заказать продукты":
            pass
        "Может быть, тебе что-то нужно из косметики?":
            pass
        "Не знаю. Видимо, ничего...":
            return
