
label after_evening:
    $ dishes_washed = False  # посуда грязная, кто-то должен ее помыть
    $ tm = "20:00"
    $ current_room = house[5]
    $ current_room.cur_bg = "location house terrace evening-b"

    $ Distribution()
    jump AfterWaiting


label typical_evening:
    Max_00 "А здесь диалог самого обычного дня, когда больше ничего не происходит"

    jump after_evening



# диалоги и события за ужином
label evening:
    scene BG breakfast breakfast-e-01
    Max_00 "Здесь будут разговоры за ужином. В зависимости от тех или иных переменных будут разные варианты"

    if day == 1:
        Max_00 "Самый первый ужин"
    else:
        jump typical_evening

    jump after_evening
