
label AliceTalkStart:

    $ dial = TalkMenuItems()
    if len(dial) == 0:
        jump AfterWaiting

    $ __CurShedRec = GetScheduleRecord(schedule_alice, day, tm)[0]
    if __CurShedRec.talklabel is not None:
        call expression __CurShedRec.talklabel

    $ dial.append((_("{i}уйти{/i}"), "exit"))

    Alice_00 "Ну, Макс, чего надо?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        if renpy.has_label(rez): # если такая метка сушествует, запускаем ее
            call expression rez
        jump AliceTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Alice_cooldown:
    Alice_09 "Макс... Не сейчас."
    Max_00 "Ладно..."
    return


label wash_dishes_alice:
    $ talk_var["alice_dw"] = 1
    menu:
        Alice_13 "Хочешь о посуде поговорить или пришёл помочь?"
        "Давай, я домою остальное":
            menu:
                Alice_07 "Что это с тобой? Но я не откажусь. И... спасибо."
                "{i}мыть посуду{/i}":
                    $ characters["alice"].mood += 6
                    if characters["alice"].relmax < 400:
                        $ characters["alice"].relmax += 10
                        $ HintRelMood("alice", 10, 6)
                    else:
                        $ HintRelMood("alice", 0, 6)
                    $ dishes_washed = True
                    $ __ts = max((60 - int(tm[-2:])), 30)
                    hide Alice
                    $ renpy.show("Max crockery-morning 01"+dress_suf["max"])
                    menu:
                        Max_11 "И почему здесь нет посудомоечной машины..."
                        "{i}закончить{/i}":
                            call Waiting(__ts, 2)
        "Нет, просто хотел поглазеть":
            menu:
                Alice_09 "Знаешь что, вали отсюда, пока мокрой тряпкой по голове не получил!"
                "{i}уйти{/i}":
                    call Waiting(10)

    return
