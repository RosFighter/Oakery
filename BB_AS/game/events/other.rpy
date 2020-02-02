
label shoping:
    $ renpy.block_rollback()
    $ current_room = house[6]
    scene BG shopping-go-00
    show other shopping-go-01
    show FG shopping-go-00

    menu:
        Ann_05 "Макс! Мы ушли на шоппинг. Не скучай тут без нас, хорошо? Вернёмся часа через 3..."
        "Удачи":
            pass
    jump Waiting


label back_shoping:
    $ renpy.block_rollback()

    $ EventsByTime["back_shoping"].stage += 1
    $ current_room = house[6]
    scene BG incoming-00
    show other shopping-go-02

    if EventsByTime["back_shoping"].stage == 1:
        ## --- Девчонки возвращаются с первого шоппинга
        Lisa_02 "Привет, Макс! Мы вернулись..."
        Max_04 "Ну как, удачно сходили?"
        Alice_13 "Ну, так... Платье мне, конечно, не купили. Даже то очень длинное, которое чуть выше колен..."
        Max_07 "А почему не купили?"
        Alice_01 "А вот у мамы спроси..."
        Max_00 "Мам?"
        menu:
            Ann_01 "Алиса, мы это уже обсуждали. Я против платьев, где у тебя всё видно. То, что оно длинное, не значит, что твою задницу не видно через разрез до ушей..."
            "Да, жаль, что не купили его...":
                pass
            "Я бы с удовольствием на это посмотрел...":
                pass
        Alice_02 "Ну, теперь остаётся только мечтать. Спасибо тебе мама за чудесный шоппинг... Лизе тоже понравилось, видимо..."
        Max_01 "А что с Лизой? Купальник купили?"
        menu:
            Lisa_09 "Нет. Мама сказала, что тот который я хотела, слишком дорогой, а остальные слишком открытые..."
            "Слишком дорогой это сколько?":
                Ann_01 "Купальник не может стоить таких денег, а она выбрала дизайнерский какой-то. Как будто мы тут миллионеры все..."
                Max_05 "Ясно. А насколько открытыми были остальные?"
            "Насколько открытые?":
                pass
        Ann_05 "Ну тебе бы точно понравилось, как и всем мужикам, кто её бы увидел, но Лиза ещё маленькая, чтобы в таком виде появляться на публике. Так что..."
        Max_03 "Всё ясно..."
        Alice_13 "В общем, бесполезно потратили время. Но Эрик обещал, что на следующий шоппинг купит нам всё, что мы захотим, да, мам?"
        Max_10 "Что?!"
        menu:
            Ann_01 "Алиса, хватит мечтать. Это всё выглядит так, как будто вы хотите из него выкачать как можно больше денег. Успокойтесь и будьте скромнее..."
            "Верно, сами разберёмся без Эрика":
                Ann_05 "Вот, Макс понимает, что это некрасиво клянчить деньги у других..."
                Max_09 "Кстати, где он?"
            "Кстати, где он?":
                pass
        Ann_00 "Эрик подъедет к ужину. Сейчас у него какие-то дела. Не переживай, сегодня ты его увидишь."
        Max_08 "Да я и не переживаю..."
        Ann_05 "Вот и отлично. Ладно, поболтаем позже..."
        Max_00 "Ага..."
        $ SetPossStage("Swimsuit", 2)

    elif EventsByTime["back_shoping"].stage == 2:
        ## --- Девчонки возвращаются со второго шоппинга

        Ann_05 "Привет, Макс! Мы вернулись..."
        Max_04 "Рассказывайте, что купили?"
        if possibility["Swimsuit"].stage_number == 2:
            $ SetPossStage("Swimsuit", 4)
            Lisa_03 "А мне Эрик подарил купальник! Именно такой, как я и хотела! Красный, представляешь?!"
            Max_11 "Ясно..."
            Lisa_02 "Что? Ты за меня не рад? Я же теперь смогу загорать в нормальном виде!"
            Max_09 "Конечно, рад... Что-то ещё хорошее купили?"
        else:
            Lisa_02 "Да так, вскую ерунду... Для нас, девочек. Тебе это не интересно..."
            Max_00 "Понятно..."
        if possibility["nightclub"].stage_number < 4:
            Alice_07 "Ты забыла про самое главное, Лиза. Мне Эрик купил платье! Представляешь?!"
            Max_10 "Да, это чудесно..."
            Alice_04 "Вот именно! Теперь я смогу ходить по клубам, а не сидеть дома вечерами! Эрик такой молодец. Я в восторге!"
            Max_11 "Поздравляю..."
            if possibility["nightclub"].stage_number == 1:
                $ SetPossStage("nightclub", 2)
            else:
                $ SetPossStage("nightclub", 3)
            Ann_07 "Макс, ты какой-то грустный. Что-то случилось? Или мне показалось?"
            Max_00 "Показалось, мам..."
        Alice_02 "Не переживай. Ты всегда можешь заработать и купить себе сам всё, что хочешь..."
        Max_09 "Спасибо за совет..."
    $ spent_time = 10
    jump Waiting


label MeetingEric:
    # устанавливаем новое расписание для Анны и Эрика
    call AddEric

    $ renpy.block_rollback()
    $ spent_time = 10
    scene BG char Max meet-eric-villa-00
    show Ann meet-Eric 01a
    show Eric meet 01a
    Ann_00 "Макс, подойди пожалуйста. К нам приехал Эрик. Знакомься..."
    show Max meet-Eric 01a
    menu:
        Ann_05 "Знакомься, это - Эрик. Эрик, это Макс, мой сын..."
        "Очень приятно...":
            hide Eric
            show Max meet-Eric 01c
            menu:
                Eric_01 "Мне тоже. Как жизнь, Макс, чем занимаешься?"
                "Всё отлично. Ищу себя, так сказать...":
                    Eric_06 "Отличные слова, Макс. Ну, надеюсь, найдёшь то, что ищешь..."
                    Max_03 "Ага, спасибо..."
                    jump .good
                "Да то тем, то этим...":
                    show Ann meet-Eric 01a
                    show Max meet-Eric 01a
                    show Eric meet 01a
                    Eric_00 "Понятно. Воздух пинаешь... Ну ничего, в своё время всё изменится..."
                    Max_08 "Я не пинаю воздух..."
                    jump .middle
                "Отвечаю вот на дурацкие вопросы...":
                    show Ann meet-Eric 01b
                    show Max meet-Eric 01b
                    show Eric meet 01b
                    Eric_09 "Ого, какие мы дружелюбные, ну что же, не буду тебя утомлять своими вопросами..."
                    Max_09 "Ну и ладно..."
                    jump .bad
        "{i}промолчать{/i}":
            menu:
                Eric_09 "Очень приятно, Макс. А ты у нас не очень разговорчивый, да?"
                "Стараюсь больше слушать...":
                    Eric_06 "Вот это да! Молодец, Макс. Вот это правильный подход."
                    Max_01 "Спасибо..."
                    jump .good
                "Типа того...":
                    Eric_02 "Всё ясно с тобой. У нас тут скромный мальчик. Ну, не буду тебя утомлять больше..."
                    Max_00 "Отлично..."
                    jump .middle
                "Да было бы о чём говорить...":
                    show Ann meet-Eric 01b
                    show Max meet-Eric 01b
                    show Eric meet 01b
                    Eric_02 "Ань, а ты не говорила, что у тебя сын такой агрессивный..."
                    Max_09 "Ты и не спрашивал..."
                    jump .bad
        "Я думал он выше...":
            show Ann meet-Eric 01b
            show Max meet-Eric 01b
            show Eric meet 01b
            menu:
                Eric_02 "Извини, Макс, что не оправдал твои ожидания. В любом случае, приятно с тобой познакомиться..."
                "Да, мне тоже. Извините...":
                    show Ann meet-Eric 01a
                    show Max meet-Eric 01a
                    show Eric meet 01a
                    Eric_05 "Макс, давай сразу на ты. Никаких формальностей. Это же семейный ужин. Так что, давайте будем проще..."
                    Max_01 "Как скажешь..."
                    jump .good
                "Ага...":
                    show Ann meet-Eric 01a
                    show Max meet-Eric 01a
                    show Eric meet 01a
                    Eric_01 "Понятно. Видимо, Макс слишком скромный. Ну ничего страшного, я в его возрасте тоже смущался..."
                    Max_08 "И ничего я не смущаюсь..."
                    jump .middle
                "А мне вот не очень...":
                    menu:
                        Eric_09 "И что со мной не так? Вот так с первого взгляда делаешь выводы о человеке? Не очень умно... Но для твоего возраста это нормально..."
                        "Да мне всё равно...":
                            pass
                        "{i}промолчать{/i}":
                            pass
                    jump .bad
    label .good:
        show Ann meet-Eric 01a
        show Max meet-Eric 01a
        show Eric meet 01a
        menu:
            Ann_07 "Ну, я рада, что вы познакомились и, вроде бы, нашли общий язык. Прошу, Эрик, к столу. Мы завтракаем и ужинаем на свежем воздухе, на веранде, пойдём покажу."
            "{i}идти к столу{/i}":
                $ talk_var["empathic"] = 2
                jump Waiting

    label .middle:
        show Ann meet-Eric 01b
        show Max meet-Eric 01a
        show Eric meet 01a
        menu:
            Ann_17 "Макс, мы с тобой потом поговорим. Ну, Эрик, проходи к столу. Мы обычно ужинаем, да и завтракаем на открытом воздухе, тут у нас веранда..."
            "{i}идти к столу{/i}":
                $ talk_var["empathic"] = 1
                jump Waiting

    label .bad:
        show Ann meet-Eric 01b
        show Max meet-Eric 01b
        show Eric meet 01b
        menu:
            Ann_20 "Макс! Ты почему себя так ведёшь? Это не только тебя не красит, но и меня позорит, что я тебя так воспитала!"
            "Извини, Эрик, я просто не в духе...":
                show Ann meet-Eric 01a
                show Max meet-Eric 01a
                show Eric meet 01a
                Ann_01 "Вот, так уже лучше. Ладно, надеюсь, это недоразумение из-за голодного желудка. Пойдёмте все к столу, пора ужинать..."

            "Нормально себя веду...":
                Ann_01 "Нет, Макс, это точно не нормально. Спишем на то, что ты голодный... Пойдём, Эрик, покажу где мы ужинаем, да и завтракаем. Макс, ты тоже иди ужинать."

            "{i}промолчать{/i}":
                Ann_01 "Молчишь? Нечего сказать или стыдно? Будем считать, что ты просто голодный, а не специально хотел нахамить Эрику. Ладно, пойдёмте ужинать..."

        $ talk_var["empathic"] = 0
        jump Waiting
