label splashscreen:

    if not persistent.choose_lang:
        $ persistent.choose_lang = True
        jump language_chooser

    return

label language_chooser:
    scene BG villa-door

    call screen choice_lang

    $ renpy.utter_restart()


label start:
    show screen watermark
    show screen notify_check
    call InitHouse from _call_InitHouse
    call InitCharacters from _call_InitCharacters
    call InitActions from _call_InitActions
    call InitStuff from _call_InitStuff
    call InitPoss from _call_InitPoss
    call InitTalksEvents from _call_InitTalksEvents
    call InitVariable from _call_InitVariable
    call InitPunish from _call_InitPunish
    call InitCources from _call_InitCources

    jump intro


label intro:
    $ NewSaveName()
    scene BG intro max
    $ renpy.block_rollback()
    menu:
        Max_00 "Меня зовут Макс. Я обычный парень из обычной семьи. Ну как обычной... нормальной. Хотя, кого я обманываю. Нормального в моей семье мало. Но обо всём по порядку."
        "{i}далее{/i}":
            if persistent.orint:
                Max_01 "Недавно меня выперли из школы. Официально - за низкую успеваемость. Хотя оценки были так себе, но настоящая причина в математичке. Говорят, я приставал... Да она сама глазки строила! Директору, её мужу, это почему-то не понравилось..."
            else:
                Max_00 "Когда мне было 3 года эта семья усыновила меня и сейчас никто уже и не вспоминает, что я приёмный. Мои же настоящие родители таинственно исчезли и их так и не нашли. Надеюсь, что когда-нибудь об этом хоть что-то станет известно..."
                Max_01 "На кануне девятнадцатилетия, когда я уже вот-вот должен был закончить школу, меня из неё выперли. Официально - за низкую успеваемость. Хотя оценки были так себе, но настоящая причина в математичке. Говорят, я приставал... Да она сама глазки строила! Директору, её мужу, это почему-то не понравилось..."
            Max_14 "В общем, сейчас я с неоконченным средним образованием. Без работы и конкретных планов на будущее... Но всё должно измениться, обязательно!"
            scene BG intro ann
            if persistent.orint:
                Max_04 "Это Анна, моя мама. Сама воспитывает нас с двумя сёстрами уже несколько лет. Работает в офисе какой-то компании. Хотя, зарплата у неё вполне приличная, но почти всё уходит на оплату съёмного жилья, еду и одежду."
            else:
                Max_04 "Это Анна, моя приёмная мама. У неё есть две родные дочери и она воспитывает нас троих уже много лет одна. Работает в офисе какой-то компании. Хотя, зарплата у неё вполне приличная, но почти всё уходит на оплату съёмного жилья, еду и одежду."
            scene BG intro oldroom
            Max_00 "Ну а это наша квартира. Тот ещё тараканник! Мама пытается заработать на первый взнос, чтобы взять ипотеку, но пока что-то не получается. Все мы мечтаем отсюда съехать, но куда?"
            scene BG intro alice
            if persistent.orint:
                Max_08 "Алиса, моя старшая сестра. Недавно закончила школу и, так же, как и я, ищет свой путь. Целыми днями сидит в ноутбуке и занимается каким-то своим блогом. Как это часто бывает с братьями и старшими сёстрами, мы не очень ладим..."
            else:
                Max_08 "Алиса, моя старшая сестра. Хоть она мне и не родная, но тем не менее, мы росли под одной крышей с самых малых лет, так что косички я ей подёргал за это время на славу. Уже несколько лет, как закончила школу, но до сих пор ищет свой путь, так же, как и я теперь. Целыми днями сидит в ноутбуке и занимается каким-то своим блогом. Как это часто бывает с братьями и старшими сёстрами, мы не очень ладим..."
            scene BG intro lisa
            if persistent.orint:
                Max_00 "Лиза, младшая сестрёнка, ещё учится в школе. Не знаю как учится, но если не выгнали как меня, значит всё в порядке. С Лизой мы общаемся на одной волне, хотя изредка ссоримся. Но если что-то случается, защиты ищет именно у меня."
            else:
                Max_00 "Лиза, младшая сестрёнка, ещё учится в школе, но последний год. Не знаю как учится, но, если не выгнали как меня, значит всё в порядке. С Лизой мы практически ровесники, ей уже восемнадцать лет. Мы общаемся на одной волне, хотя изредка ссоримся. Но если что-то случается, защиты ищет именно у меня."
            scene BG intro max
            if persistent.orint:
                Max_14 "Отца я плохо помню. Он ушёл, когда мне было лет пять. Мама не хочет рассказывать, что тогда случилось... Ходили слухи, что дела у него пошли в гору. С тех пор мы о нём ничего не слышали. До прошлого месяца, когда пришла та девушка..."
            else:
                Max_14 "Приёмного отца я плохо помню. Он ушёл, когда мне было лет восемь. Мама не хочет рассказывать, что тогда случилось... Ходили слухи, что дела у него пошли в гору. С тех пор мы о нём ничего не слышали. До прошлого месяца, когда пришла та девушка..."
            scene BG intro lawyer
            Maya_01 "Здравствуйте, меня зовут Майя, я адвокат вашего бывшего мужа. У вас найдётся для меня минутка?"
            Ann_00 "Здравствуйте, да, конечно. Меня зовут Анна, но вы и так это знаете похоже. Так в чём дело? С ним что-то случилось?"
            Maya_03 "Не переживайте, он жив-здоров, но сам приехать не смог. Сказал, что вы будете не очень рады, хотя новости у меня для вас отличные!"
            Ann_01 "Любопытно. И что же это за новости спустя столько лет?"
            Maya_02 "Я принесла документы на недвижимость, которую он решил передать вам. Если вы их подпишите, то станете полноправным владельцем."
            Ann_17 "Что-то я не поняла. Это совсем на него не похоже. Какая недвижимость? О чём речь?"
            Maya_01 "Это двухэтажный дом на юге страны, который построила его компания. А насчёт того, что это на него не похоже... В последние пару лет он очень изменился. Не уверена, что эти изменения пошли на пользу бизнесу."
            Ann_01 "Что-то вы меня озадачили. В чём подвох? Я что-то должна? Столько лет никаких вестей, ничего, и тут... дом. И что там с его бизнесом?"
            Maya_02 "В данный момент он продал большую часть недвижимости, чтобы погасить налоговую задолженность, но этот дом решил передать вам. Я не знаю причин, да они меня и не касаются."
            Ann_00 "Вы знаете, Майя, я не могу принять такой... подарок. Во-первых, я не в курсе его махинаций или что он там придумал, а во-вторых, мы с ним уже столько лет не общались, и мне не нужно от него ничего!"
            Maya_01 "Да, он предупреждал меня о такой вашей реакции... С юридической точки зрения дом абсолютно чист, и вы ничем не рискуете. Кроме того, ваши дети растут и им нужно место, своё личное пространство..."
            Ann_14 "С этим не поспоришь. У меня есть время подумать обо всём?"
            menu:
                Maya_03 "Конечно, Анна. Вот моя визитка. Позвоните, когда будете готовы принять решение. Также я оставлю копии всех документов. До свидания."
                "{i}пару недель спустя...{/i}":
                    pass
            scene location house courtyard day-b
            Max_04 "К счастью, мама приняла верное решение. Когда мы увидели дом, не поверили своим глазам! Вживую он оказался гораздо больше и красивее, чем на фотографиях. Но самым приятным сюрпризом оказался бассейн!"
            scene location house aliceroom day-a
            Max_00 "Алиса сразу заняла одну из спален. Кстати, их оказалось всего две. Несмотря на огромную гостиную с кухней и просторную ванную, в доме всего три отдельные комнаты: две спальни и кабинет."
            scene BG intro newroom
            Max_08 "В кабинете мебели почти не оказалось, и мне пришла в голову отличная идея разместить здесь наши с Лизой кровати из старой квартиры."
            if persistent.orint:
                Ann_01 "Что-то мне не нравится эта твоя идея, Макс. Вы уже взрослые, чтобы спать в одной комнате. Давай этот офис выделим тебе, а вторую спальню - Лизе. Ну а я буду спать в гостиной. Там отличные диванчики..."
            else:
                Ann_01 "Что-то мне не нравится эта твоя идея, Макс. Вы уже совсем взрослые, чтобы спать в одной комнате. Давай этот офис выделим тебе, а вторую спальню - Лизе. Ну а я буду спать в гостиной. Там отличные диванчики..."
            Max_01 "Мам, мы и так все жили как селёдки в бочке, нам не привыкать. А тут такие огромные комнаты. Нам с Лизой места хватит. Правда, сестрёнка?"
            Lisa_02 "Конечно! Мам, мы нормально с Максом уживаемся. А если будет косячить, выгоню его в эту самую гостиную! А ты свою комнату точно заслужила. И не спорь. Мы все так думаем."
            menu:
                Ann_07 "Ну хорошо. Транспортная компания сообщила, что наши вещи задерживаются. Что-то я уже жалею, что с ними связалась... Так или иначе, через неделю переезжаем!"
                "{i}спустя неделю...{/i}":
                    pass
            scene BG intro max
            Max_00 "Спустя неделю часть наших вещей из старой квартиры доставили. Но только часть. Как я понял, кое-что потерялось в пути. Надеюсь, компенсируют это как-то..."
            menu:
                Max_04 "Мама устроилась на новую работу. Лиза пошла в местную школу. Алиса так и сидит в своём ноуте, а я... На этом мой рассказ заканчивается и начинается что-то новое и интересное!"
                "{i}Начать игру{/i}":
                    $ spent_time = 10
                    jump Waiting
                "{i}Повторить историю{/i}":
                    jump intro
        "{i}пропустить{/i}":
            $ spent_time = 10
            jump Waiting

label about_poss:
    $ flags['about_poss'] = False
    scene BG intro max
    Max_00 "\"Возможности\" - это особые пути, по которым можно пройти, чтобы достичь какого-то результата. Обычно они скрыты и не очень очевидны."
    Max_03 "Некоторые действия в игре открывают такие \"возможности\". Увидеть их можно на соответствующем экране, который можно открыть через верхнее меню."
    Max_00 "Некоторые \"возможности\" временные. Некоторые могут привести к нежелательному результату. Не стоит хвататься за первую попавшуюся и слепо следовать подсказкам!"
    menu:
        Max_04 "Но и бояться их не стоит. Именно благодаря \"возможностям\" можно добиться того, о чём некоторые даже не мечтают!"
        "{i}всё ясно{/i}":
            pass
        "{i}повторить{/i}":
            jump about_poss

    return
