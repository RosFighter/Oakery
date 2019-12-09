
label AnnTalkStart:

    $ dial = TalkMenuItems()
    if len(dial) == 0:
        jump AfterWaiting

    $ __CurShedRec = GetScheduleRecord(schedule_ann, day, tm)[0]
    if __CurShedRec.talklabel is not None:
        call expression __CurShedRec.talklabel from _call_expression_6

    $ dial.append((_("{i}уйти{/i}"), "exit"))

    Ann_00 "Что-то случилось, дорогой?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        if renpy.has_label(rez): # если такая метка сушествует, запускаем ее
            call expression rez from _call_expression_7
        jump AnnTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Ann_cooldown:
    Ann_18 "Макс, давай сменим тему..."
    Max_00 "Ок, мам..."
    return
