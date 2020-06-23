
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

    $ EventsByTime['back_shoping'].stage += 1
    $ current_room = house[6]
    scene BG incoming-00
    show other shopping-go-02

    if EventsByTime['back_shoping'].stage == 1:
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
        $ poss['Swimsuit'].OpenStage(2)

    elif EventsByTime['back_shoping'].stage == 2:
        ## --- Девчонки возвращаются со второго шоппинга

        Ann_05 "Привет, Макс! Мы вернулись..."
        Max_04 "Рассказывайте, что купили?"
        if poss['Swimsuit'].stn == 2:
            $ poss['Swimsuit'].OpenStage(4)
            $ lisa.gifts.append('bikini')
            # $ items['bathrobe'].InShop = True
            if lisa.inferic is not None:
                $ lisa.inferic = clip(lisa.inferic+20.0, 0.0, 100.0)
            else:
                $ lisa.infmax = 20.0
            if lisa.infmax is not None:
                $ lisa.infmax = clip(lisa.infmax-10.0, 0.0, 100.0)
            Lisa_03 "А мне Эрик подарил купальник! Именно такой, как я и хотела! Красный, представляешь?!"
            Max_11 "Ясно..."
            Lisa_02 "Что? Ты за меня не рад? Я же теперь смогу загорать в нормальном виде!"
            Max_09 "Конечно, рад... Что-то ещё хорошее купили?"
        else:
            Lisa_02 "Да так, вскую ерунду... Для нас, девочек. Тебе это не интересно..."
            Max_00 "Понятно..."
        if poss['nightclub'].stn < 4:
            Alice_07 "Ты забыла про самое главное, Лиза. Мне Эрик купил платье! Представляешь?!"
            Max_10 "Да, это чудесно..."
            Alice_04 "Вот именно! Теперь я смогу ходить по клубам, а не сидеть дома вечерами! Эрик такой молодец. Я в восторге!"
            Max_11 "Поздравляю..."
            if poss['nightclub'].stn == 1:
                $ poss['nightclub'].OpenStage(2)
            else:
                $ poss['nightclub'].OpenStage(3)
            if alice.inferic is not None:
                $ alice.inferic = clip(alice.inferic+20.0, 0.0, 100.0)
            else:
                $ alice.infmax = 20.0
            if alice.infmax is not None:
                $ alice.infmax = clip(alice.infmax-10.0, 0.0, 100.0)
            $ alice.gifts.append('dress')
            Ann_07 "Макс, ты какой-то грустный. Что-то случилось? Или мне показалось?"
            Max_00 "Показалось, мам..."
        Alice_02 "Не переживай. Ты всегда можешь заработать и купить себе сам всё, что хочешь..."
        Max_09 "Спасибо за совет..."
    $ spent_time = 10
    jump Waiting


label MeetingEric:
    # устанавливаем новое расписание для Анны и Эрика
    call AddEric from _call_AddEric

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
                $ talk_var['empathic'] = 2
                jump Waiting

    label .middle:
        show Ann meet-Eric 01b
        show Max meet-Eric 01a
        show Eric meet 01a
        menu:
            Ann_17 "Макс, мы с тобой потом поговорим. Ну, Эрик, проходи к столу. Мы обычно ужинаем, да и завтракаем на открытом воздухе, тут у нас веранда..."
            "{i}идти к столу{/i}":
                $ talk_var['empathic'] = 1
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

        $ talk_var['empathic'] = 0
        jump Waiting


label Kira_arrival:
    # устанавливаем новое расписание для Киры и девчонок

    $ renpy.block_rollback()
    scene BG delivery-01
    $ renpy.show("Kira arrival 01"+ann.dress)
    Ann_05 "Ну что, дети, дождались? Встречайте, к нам приехала тётя Кира!"
    Max_05 "Супер!"
    menu:
        Kira_01 "Это кто тут у нас? Макс? Я тебя не узнала! Почти настоящий мужчина!"
        "Здравствуй, тётя Кира!":
            pass
        "Что значит почти? Я настоящий мужчина!":
            Kira_06 "Да я шучу, Макс. Конечно, ты уже мужчина. Вижу, всё у тебя в порядке. И как ты только держишься среди таких девчонок? Кстати, где Лиза и Алиса?"
            Max_04 "Уже бегут..."
    scene BG shopping-go-00  ## правильный ли фон? использован фон, где девчонки уходят в магазин...
    $ renpy.show("Kira arrival 02"+lisa.dress)
    $ renpy.show("Ann Kira-arrival 01"+ann.dress)
    Kira_07 "Лиза? Алиса? Неужели, это вы? Все такие большие, с меня ростом!"
    Lisa_03 "Тётя Кира! Ура! Я так соскучилась!"
    Max_02 "Хорошую подушку ты нашла..."
    Alice_07 "Я так рада, что ты приехала! Ты же надолго, да?"
    Kira_04 "Что, уже выгоняете?!"
    menu:
        Ann_04 "Что ты, Кира, оставайся хоть навсегда! Я тоже очень рада тебя видеть, сестрёнка!"
        "А мне можно тоже обнять свою тётю?":
            Lisa_05 "Нет! Она моя! Никому не отдам!"
            Max_00 "Ну и ладно. Я тогда... потом."
        "{i}далее{/i}":
            pass
    Ann_01 "Кира, ты меня удивляешь! Не в мини-юбке... да ещё и такая нарядная! Неужели, прямо в таком виде летела в самолёте?"
    Max_07 "Да, кстати..."
    menu:
        Kira_05 "Нет, что ты. Я прилетела пару дней назад и остановилась в гостинице. Просто... нужно было разобраться кое с чем. Но с делами покончено и специально ради вас я наряжалась всё утро!"
        "В гостинице?":
            pass
        "Дела?":
            Kira_02 "Ага. Не буду утомлять вас подробностями, это никому не интересно. Скажу лишь, что всё улажено и теперь я свободна для своей семьи!"
            jump .end_yard
        "Так ты два дня здесь?":
            pass
    Kira_03 "Да, я прошу прощения, что не предупредила, но не могла завалиться к вам, чтобы тут же убежать. Но я со всем разобралась, всё в порядке, теперь я тут!"
    jump .end_yard

    label .end_yard:
        Max_07 "А мне любопытно, что за дела?"
        Ann_02 "Макс, ну хватит пытать свою тётю. Она сама расскажет, если захочет, верно? А теперь пойдёмте все в дом, скоро будем завтракать."

    ## в гостиной
    scene BG char Kira arrival-03
    show Kira arrival 03
    $ renpy.show("Ann Kira-arrival 03"+ann.dress)
    $ renpy.show("Lisa Kira-arrival 03"+lisa.dress)
    show Alice Kira-arrival 03

    Kira_01 "Так как у меня было время подготовиться к встрече с вами, я приехала не с пустыми руками и привезла вам кое-что..."
    Max_03 "Ух-ты!"
    Kira_07 "Я уже в курсе вашей истории с потерянным вещами. Поэтому, я уточнила у вашей мамы ваши размеры и купила лёгкую домашнюю одежду. И, кажется, правильно сделала. В такую жару, дома, лучше носить что-нибудь лёгкое!"
    Lisa_02 "Ой! Я обожаю новые вещички. А что ты мне привезла, тётя Кира, а?"
    Max_01 "Я думал у нас Алиса шмотки любит..."
    Lisa_01 "Макс, какой ты глупый, кошмар! Шмотки любят все девушки! Ну так что там?"
    menu:
        Kira_05 "Так, вы все давайте держите новую одежду, переодевайтесь и встречаемся за столом, где вы завтракаете. Посмотрим, всем ли всё подошло. А тебе, Макс, я ничего не купила. Подумала, что ты можешь и в шортах ходить. Но подарок тебе сделаю, позже решим какой..."
        ## какой подарок будет сделан Максу?
        "Да не стоит...":
            pass
        "Хорошо, тётя Кира!":
            pass
    ## Примерка Лизы
    scene BG punish-morning 00
    show Kira arrival 04-lisa-01
    menu:
        Lisa_02 "Ну как вам? Такой классный топ и юбочка и мой любимый цвет, представляете!"
        "Выглядит отлично!":
            Ann_01 "Да, вот только меня немного смущает длина юбки. Видимо, Кира, ты на свой вкус выбирала. Лиза, покрутись, пожалуйста..."
        "Ну-ка, повернись...":
            pass
    show Kira arrival 04-lisa-01a
    Lisa_03 "Мне кажется, что не слишком коротко. В самый раз! И теперь так свободно и легко... Спасибо тебе, тётя Кира!"
    Max_03 "Да, длина в самый раз..."
    ## Примерка Алисы
    show Kira arrival 04-alice-01
    Alice_02 "Ну всё, теперь моя очередь! Как вам? Лично мне очень нравится! Давно надо было раздеться."
    Max_04 "Именно!"
    menu:
        Ann_02 "Я не поняла. А трусы то на тебе хоть есть? Ты же не планируешь в таком виде ходить дома, Алиса?"
        "А что такого? Пусть ходит, я не против...":
            Alice_03 "Спасибо, Макс! Мам, а что такого? Ты не представляешь как жарко было в джинсах, а теперь хоть тело дышит. Да и жара такая на улице и дома..."
            Ann_01 "Ладно, а что там сзади? Ну-ка покрутись..."
        "{i}промолчать{/i}":
            Alice_05 "Мам, да всё в порядке. На мне шорты, ничего не видно. Вот, смотри..."
    show Kira arrival 04-alice-01a
    Ann_12 "Алиса, у тебя же всё видно, аж грудь вываливается! Смотри, как Макс таращится. Кажется, он даже завис..."
    Max_07 "Э... Ну... да..."
    Alice_02 "Мам, я дома могу одеваться так, как мне нравится. Ну и что, что Макс. Я из-за него не буду целыми днями ходить в парандже! Мне удобно, выглядит отлично! Ну а если и увидит что-то, пусть радуется, мне всё равно..."
    Max_02 "Отличная речь, сестрёнка!"
    ## Примерка Анны
    show Kira arrival 04-ann-01
    menu:
        Ann_04 "Ну, теперь и моя очередь. Как вам? Не слишком откровенно?"
        "Нет, мам, всё отлично!":
            pass
        "А можешь немного повернуться?":
            pass
    show Kira arrival 04-ann-01a
    menu:
        Ann_07 "Мне кажется, шортики слишком короткие... Я в них еле влезла, если честно. Надо худеть..."
        "Ты знаешь, длина оптимальная!":
            pass
            $ __mood = 0
        "Мне нравится, мам!":
            $ __mood = 30
    Kira_03 "Ань, всё сидит на тебе просто отлично. И очень идёт этот цвет, кстати... Ну а теперь моя очередь. Сейчас покажу, что себе прикупила..."
    Max_01 "Интересно..."
    ## Примерка Киры
    show Kira arrival 04-kira-01
    menu:
        Kira_05 "Ну, как я вам? Хороша? И Ань, ни слова больше. Тебе всё кажется слишком открытое или откровенное."
        "Мне нравится. Просто и со вкусом!":
            pass
        "Отличные... вещички!":
            pass
        "И почти ничего не видно...":
            pass
    Kira_07 "Вот, слышала, Ань, детям нравится. Естественно, если в семье есть мужчина, это накладывает свои ограничения, но нельзя же быть настолько зажатыми..."
    Max_04 "Верно!"
    Ann_04 "Ладно, посмотрим. Кира, мне кажется, что не стоило тратиться на подарки. Мы рады, что ты сама смогла к нам приехать... Но всё равно, большое спасибо!"
    Max_07 "Давайте уже завтракать, а то остыло почти всё..."

    $ spent_time = 20
    call AddKira

    $ AddRelMood('ann', 0, __mood)
    jump Waiting
