
label AliceTalkStart:

    $ dial = TalkMenuItems()
    if len(dial) == 0:
        jump AfterWaiting

    $ __CurShedRec = GetScheduleRecord(schedule_alice, day, tm)[0]
    if __CurShedRec.talklabel is not None:
        call expression __CurShedRec.talklabel from _call_expression_4

    $ dial.append((_("{i}уйти{/i}"), "exit"))

    Alice_00 "Ну, Макс, чего надо?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        if renpy.has_label(rez): # если такая метка сушествует, запускаем ее
            call expression rez from _call_expression_5
        jump AliceTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Alice_cooldown:
    Alice_09 "Макс... Не сейчас."
    Max_00 "Ладно..."
    jump AfterWaiting


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
                            call Waiting(__ts, 2) from _call_Waiting_8
        "Нет, просто хотел поглазеть":
            menu:
                Alice_09 "Знаешь что, вали отсюда, пока мокрой тряпкой по голове не получил!"
                "{i}уйти{/i}":
                    call Waiting(10) from _call_Waiting_9

    return


label talkblog1:
    if "blog" in cooldown:
        if ItsTime(cooldown["blog"]): # кулдаун прошел, можно поговорить
            $ del cooldown["blog"]
        else:
            jump Alice_cooldown

    menu:
        Alice_00 "А типа ты не знаешь? Позлорадствовать пришёл?"
        "Нет, хотел просто больше узнать":
            menu:
                Alice_02 "Что, даже не начнёшь подкалывать? И что ты хотел узнать?"
                "Расскажи, что ты там делаешь":
                    menu:
                        Alice_13 "Ну, пока наши вещи не пропали во время переезда, я показывала как наносить лак, как применять различные средства и делилась разными хитростями..."
                        "Хитростями? А откуда ты сама всё это узнала?":
                            menu:
                                Alice_22 "Да у других таких же блогеров подсмотрела, конечно. Все так делают! Ну и сама в интернете разное читаю, изучаю..."
                                "Тема бьюти разве единственная?":
                                    menu:
                                        Alice_00 "Нет, но мне это всё как-то по душе. Говорят, у человека лучше получается то, что нравится. А мне это нравится..."
                                        "Давай что-то придумаем вместе!":
                                            jump .together
                                        "Может быть, изменить твой блог?":
                                            jump .otherway
                                "Понятно. Ну, и что теперь?":
                                    jump .whatnow
                        "И что теперь без этих своих вещей делать будешь?":
                            jump .whatnow
                "Как планируешь развиваться?":
                    menu:
                        Alice_00 "Развиваться? Шутишь? Все мои вещи, лаки, материалы и прочее было в том контейнере, который пропал. Теперь у меня нет ничего..."
                        "Что, совсем всё пропало?":
                            menu:
                                Alice_13 "Совсем всё. У меня даже нет подходящей одежды, чтобы вести блог. Нельзя же постоянно быть в одной майке перед зрителями..."
                                "Может, это твоя фишка. Да и майка счастливая...":
                                    menu:
                                        Alice_00 "Ага, потому что единственная, да? А ещё какая фишка? Нет материалов, нечего показывать?"
                                        "Да уж, грусть-печаль...":
                                            jump .sad
                                        "Тебе как-то можно помочь?":
                                            jump .help
                                "Разве это важно?":
                                    menu:
                                        Alice_00 "Очень важно. Ну, ладно, чёрт с ней, с одеждой, а что мне в блоге показывать? Как себя правильно расчёсывать? У меня нет ничего..."
                                        "Да уж, грусть-печаль...":
                                            jump .sad
                                        "Тебе как-то можно помочь?":
                                            jump .help
                        "Постой, и что теперь будет?":
                            jump .whatnow
        "Много подписчиков уже?":
            menu:
                Alice_13 "Да ты издеваешься, да?"
                "Нет. С чего ты взяла?":
                    pass
                "Ты о чём, вообще?":
                    pass
            menu .no:
                Alice_00 "Типа ты не в курсе, что у нас пропала большая часть вещей во время переезда?"
                "Да ладно?":
                    $ cooldown["blog"] = CooldownTime("03:00")
                    Alice_09 "Знаешь что, Макс, отвали!"
                    Max_00 "Ну и ладно..."
                    $ characters["alice"].mood -=5
                    $ characters["alice"].relmax -= 5
                    $ HintRelMood("lisa", -5, -5)
                    jump .end
                "В курсе, конечно":
                    menu:
                        Alice_13 "Ну, вот среди тех вещей было всё, что я использовала для ведения своего блога. Одежда, различные лаки, кремы... вообще всё!"
                        "Мне очень жаль...":
                            jump .sad
                        "И как тебе помочь?":
                            jump .help
        "Заработала уже на нём что-то?":
            menu:
                Alice_13 "Макс, тебе заняться нечем, кроме как меня доставать? Ты же знаешь, что у меня всё пропало!"
                "Что пропало? Ты о чём?":
                    jump .no
                "Ты о тех вещах во время переезда?":
                    menu:
                        Alice_00 "Конечно! Там же было вообще всё, что мне нужно для ведения блога. Шмотки, мои любимые лаки, косметика... вообще всё!"
                        "Да, печально...":
                            jump .sad
                        "Тебе можно как-то помочь?":
                            jump .help
    menu .sad:
        Alice_13 "Вот-вот... Надо было всё с собой брать, а не складывать в тот контейнер.."
        "Может быть, попробуем вместе найти решение?":
            jump .together
        "Я обязательно придумаю, что можно с этим сделать":
            jump .findout

    menu .help:
        Alice_07 "Ты у нас внезапно стал миллионером? Или просто деньги появились? Самый простой способ - это купить недостающее. Ну, или найти то, что пропало"
        "Денег у меня нет...":
            menu:
                Alice_13 "А без денег тут ничем не поможешь. Вообще, я в депрессии из-за всей этой истории. Вся жизнь перевернулась..."
                "Вся жизнь? Но это всё к лучшему же. Такой дом, бассейн, место отличное!":
                    menu:
                        Alice_00 "Да, в этом плане ты прав, Макс. Но я хотела чего-то добиться. Стать известным блогером и заработать кучу денег. А теперь..."
                        "Давай что-то придумаем вместе!":
                            jump .together
                        "Ты всё ещё можешь. Может быть, просто смени формат блога":
                            jump .otherway
                "Не грусти. Могло быть и хуже":
                    menu:
                        Alice_00 "Верно. Но всё равно, это всё очень грустно. Я даже не представляю, как теперь быть..."
                        "Давай что-то придумаем вместе!":
                            jump .together
                        "Ты всё ещё можешь. Может быть, просто смени формат блога":
                            jump .otherway
                "Может быть, зарабатывать на чём-то другом?":
                    jump .otherway
        "Я не детектив, чтобы искать вещи...":
            menu:
                Alice_00 "А кто ты тогда? Чем же именно можешь помочь?"
                "Ну, у меня много разных идей":
                    menu:
                        Alice_07 "Много разных идей? Например?"
                        "Давай что-то придумаем вместе!":
                            jump .together
                        "Может быть, изменить твой блог?":
                            jump .otherway
                "Советами!":
                    menu:
                        Alice_06 "И кому уже помогли твои советы? Знаешь, советчиков много. Лучше бы что-то конкретное предложил..."
                        "Давай что-то придумаем вместе!":
                            jump .together
                        "Может быть, изменить твой блог?":
                            jump .otherway

    menu .whatnow:
        Alice_00 "Не знаю, если честно. Мне даже показаться перед зрителями не в чем. Какой же я бьюти-блогер, если на мне всегда одна и та же одежда..."
        "Тебе как-то можно помочь?":
            jump .help
        "Может быть, заняться чем-то другим?":
            jump .otherway
        "Да уж, грусть-печаль...":
            jump .sad

    menu .otherway:
        Alice_00 "Ты о чём? Есть какие-то мысли?"
        "Мы можем с тобой вместе что-то придумать":
            jump .together
        "Давай, я подумаю и, когда будут мысли, продолжим разговор":
            jump .findout
        "Пока нет, но я подумаю что можно сделать":
            jump .findout

    label .together:
        $ talk_var["blog"] = 2
        menu:
            Alice_14 "Вместе? Ещё ничего нет, а уже в партнёры набиваешься?"
            "Ну если придумаю что-то, то почему нет?":
                Alice_07 "Ну, если придумаешь. Если. Да и смотря что... Сильно удаляться от этой темы не хочется. Но попробовать что-то новое можно... В общем, когда что-то придумаешь, тогда и поговорим..."
                Max_00 "Хорошо!"
            "Конечно! Будет у нас семейный бизнес!":
                menu:
                    Alice_07 "Семейный бизнес? На моём блоге? Может ещё и сам вести будешь?"
                    "Ну да, многие так делают!":
                        pass
                    "Нет, из меня ведущий так себе...":
                        pass
                    "Попробовать то можем?":
                        pass
                Alice_00 "Знаешь, мне кажется, что это всё пустые разговоры. Сначала что-то предложи, тогда и обсудим..."
                Max_00 "Хорошо, я подумаю"
            "Ну, можно попробовать же?":
                Alice_00 "Попробовать можно, но сначала надо понять что. Ты пока ничего конкретного не предложил. Когда будут идеи, тогда и подходи..."
                Max_00 "Ладно, когда будут идеи, обсудим..."
        jump .end

    label .findout:
        $ talk_var["blog"] = 2
        menu:
            Alice_07 "Ну, давай. Сомневаюсь, конечно, что это не пустая болтовня, но вдруг... Удиви меня!"
            "Постараюсь...":
                Alice_00 "Постарайся. Я тоже буду думать. Но бросать блог не хочу. Может быть и правда стоит сменить формат, но на какой?"
                Max_00 "Договорились!"
            "Но ничего не обещаю":
                Alice_00 "А я другого и не жду. Если бы у тебя были мысли, ты бы и сам мог на таком заработать... В общем, будем думать..."
                Max_00 "Ага..."
            "Обещаю, что-нибудь придумаю":
                Alice_06 "Обещание, конечно, обнадёживает... Но я бы не стала на твоём месте что-то обещать. Конечно, если у тебя уже нет идей. Так или иначе, я тоже буду думать. Может быть, и правда не всё так плохо..."
                Max_00 "Да прорвёмся!"

    label .end:
        if talk_var["blog"] == 2:
            call Waiting(30) from _call_Waiting_11
        return
