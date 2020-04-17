
label after_breakfast:
    $ dishes_washed = False  # посуда грязная, кто-то должен ее помыть
    $ spent_time = 60
    $ current_room = house[5]
    $ AvailableActions['dishes'].enabled = True

    jump Waiting


label typical_breakfast:
    menu:
        Ann_00 "Всех ещё раз с добрым утром, всем приятного аппетита! Давайте сегодня покушаем в тишине, если вы не возражаете..."
        "Конечно, мам...":
            Ann_05 "Спасибо за понимание, Макс! Ну, приступим..."
            Max_00 "Приятного аппетита!"
        "А что, что-то случилось?":
            Ann_05 "Нет, просто ещё не проснулась, нужно собраться с мыслями..."
            Max_00 "Понятно. Приятного аппетита!"
    jump after_breakfast


label breakfast_first:
    Ann_07 "Ну, дети, как вам живётся на новом месте? Как спалось в первую ночь?"
    menu:
        Alice_07 "Просто нет слов! После той нашей съёмной квартиры это какой-то рай! А кровать какая удобная..."
        "Посмотрим, какой ещё счёт придёт за жильё...":
            menu:
                Ann_12 "Да, меня тоже этот вопрос беспокоит. Но на новой работе мне обещают очень хорошую зарплату. Может быть, не всё так плохо. Кстати, за электричество платить не нужно..."
                "Почему не нужно?":
                    jump .bf_roof
                "Ну, я тоже попробую заработать":
                    jump .bf_earn
        "Да, это небо и земля. Ещё бы знать, где кидают?":
            menu:
                Lisa_01 "А вдруг, нигде не кидают? Хотя я папу и не помню, но мне кажется, что никто не стал бы дарить целый дом только чтобы как-то кинуть..."
                "Как знать. Может быть, у него не всё чисто с законом и дом отберут":
                    jump .bf_change
                "Верно. У нас толком ничего и не было, чтобы планировать что-то отобрать":
                    jump .bf_change
                "Хотелось бы так думать...":
                    jump .bf_change
        "А вот у меня кровать точно такая же...":
            menu:
                Lisa_03 "Это потому, что у нас с тобой наши старые кровати. Ты забыл? Кстати, мне нравится моя. Даже не хочу менять её на новую..."
                "Меня моя тоже устраивает":
                    menu:
                        Ann_00 "Если что, мебель всегда можно будет купить..."
                        "Ага. Кстати, я планирую уже начать зарабатывать!":
                            jump .bf_earn
                "Вот заработаю и куплю себе новую кровать!":
                    jump .bf_earn

    label .bf_change:
        menu:
            Ann_00 "Так, хватит. Давайте сменим тему. Например, сегодня у нас Лиза первый раз идёт в новую школу."
            "Поздравляю, Лиза!":
                menu:
                    Lisa_02 "Спасибо, Макс. Честно говоря, не знаю даже чего ожидать. Новое место, новая школа, новый коллектив..."
                    "Если нужна помощь - обращайся":
                        menu:
                            Alice_13 "Ага, помощник. Самого выгнали, а он учить собрался..."
                            "Меня не за знания выгнали":
                                menu:
                                    Alice_06 "Да все мы знаем за что тебя выгнали. Но это не значит, что и учился ты хорошо..."
                                    "Да пошла ты!":
                                        jump .bf_change2
                                    "Обязательно меня доставать?":
                                        jump .bf_change2
                                    "Нормально я учился...":
                                        jump .bf_change2
                            "Ну, кое-что я знаю...":
                                menu:
                                    Alice_06 "Ага, знаешь как к учителям приставать. Этому планируешь научить Лизу?"
                                    "А сама, такая умная, даже помощь сестрёнке не предложила!":
                                        jump .bf_change2
                                    "Чему смогу, тому и научу...":
                                        jump .bf_change2
                    "Ну, ты справишься!":
                        menu:
                            Lisa_01 "Ага, деваться то некуда. Кстати, после завтрака я буду уже собираться, в 11 выхожу. А часам к 4 уже вернусь"
                            "Сегодня укороченный день?":
                                menu:
                                    Lisa_02 "Нет, не только сегодня. Вообще, уроки короткие в этой школе. Так что, соскучиться не успеете!"
                                    "Мы в тебя верим...":
                                        jump .bf_time3
                            "Всего 5 часов?":
                                jump .bf_time2
                            "Ну, удачи тебе в школе!":
                                jump .bf_time3
            "Кстати, в какое время начинается учёба?":
                menu:
                    Lisa_00 "Видимо, после завтрака буду уходить и возвращаться часам к 4-м."
                    "А почему так мало?":
                        jump .bf_time2
                    "Мы в тебя верим...":
                        jump .bf_time3
            "А школа платная?":
                menu:
                    Lisa_03 "Нет, представляешь! Говорят, ещё и район хороший. А учимся мы, вообще, всего 4 или 5 часов!"
                    "А почему так мало?":
                        jump .bf_time2
                    "Мы в тебя верим...":
                        jump .bf_time3

    label .bf_time2:
        menu:
            Lisa_02 "Ну, у нас в этой школе так. Меня всё устраивает. Мы ещё и учимся всего пять дней в неделю! Правда, про каникулы ничего не знаю..."
            "Мы в тебя верим...":
                jump .bf_time3

    label .bf_time3:
        Lisa_03 "Спасибо. Постараюсь не подвести!"
        jump .bf_change2

    label .bf_earn:
        menu:
            Alice_06 "Ага, и как же ты заработаешь? Образования нет, ничего толком не умеешь. Только дома сидишь всё время в своём ноуте..."
            "Ой. Кого же мне это всё напоминает?":
                $ talk_var['blog'] = 1
                menu:
                    Alice_14 "Может быть, себя? У меня то хоть свой блог есть, а вот у тебя ни-че-го!"
                    "И что твой блог тебе даёт?":
                        menu:
                            Alice_13 "Он даёт подписчиков, аудиторию. Когда начну рекламу крутить, то деньги польются рекой!"
                            "Смотри, не захлебнись... рекой":
                                jump .bf_change
                            "Ну, посмотрим на твою реку...":
                                jump .bf_change
                    "Много уже на нём заработала?":
                        menu:
                            Alice_13 "Ещё нет, но я только набираю аудиторию. А когда придёт время, запущу рекламу и стану богатой!"
                            "Ага, как Кардашьян":
                                jump .bf_change
                            "Может быть, тебе подарить губозакатывательную машинку?":
                                jump .bf_change
                    "А у меня есть мозги!":
                        menu:
                            Alice_07 "Мозги? У тебя?! А кого же из школы тогда выперли? Слишком умный для них был, да?"
                            "Да поумнее некоторых...":
                                jump .bf_change
                            "Меня не за оценки выперли!":
                                jump .bf_change
                            "Да мне школа и не нужна":
                                jump .bf_change
            "А вот и заработаю. Научусь что-то делать и сразу заработаю!":
                menu:
                    Alice_02 "Ага, просиживать штаны ты научишься. Объявлений с предложением работы полно. Выбирай - не хочу."
                    "Да ты сама дома целыми днями сидишь!":
                        jump .bf_change
                    "Ага, дворником или посудомойкой?":
                        jump .bf_change
                    "Вот сама бы и шла работать по объявлению!":
                        jump .bf_change
            "Ну а ты разве не дома сидишь в своём ноуте? Ты как зарабатывать планируешь?":
                jump .bf_earn3

    label .bf_earn3:
        $ talk_var['blog'] = 1
        menu:
            Alice_13 "Я делом занимаюсь. Раскручиваю свой блог, набираю аудиторию. А потом, когда придёт время, начну крутить рекламу и всё!"
            "Ага, всё же так просто...":
                menu:
                    Alice_00 "А я и не говорю, что это просто. В любом случае, я хоть чем-то занимаюсь, в отличие, от некоторых..."
                    "Да уж, делом. Деловая...":
                        jump .bf_change
                    "Не перетрудись!":
                        jump .bf_change
                    "Я хотя бы реалист!":
                        jump .bf_change
            "И что ты будешь рекламировать?":
                menu:
                    Alice_00 "А это не важно. Что нужно будет, то и буду рекламировать. А вообще, у меня бьюти-блог!"
                    "Бьюти-блогеров как грязи. Чем ты лучше их?":
                        jump .bf_change
                    "Думаешь, кому-то нужна твоя реклама?":
                        jump .bf_change
                    "Всё фантазируешь...":
                        jump .bf_change
            "Сколько миллионов подписчиков у тебя, говоришь?":
                menu:
                    Alice_00 "Я не говорила, что у меня миллион подписчиков, но будет. И не один. А вот у тебя вообще ничего нет!"
                    "У меня есть планы и идеи":
                        jump .bf_change
                    "Я тоже что-то придумаю":
                        jump .bf_change
                    "Ага, десять миллионов...":
                        jump .bf_change

    label .bf_roof:
        Ann_01 "У нас вся крыша состоит из солнечных панелей. Тут какой-то накопитель есть и своей энергии вполне хватает. Даже на отопление хватило бы, если бы не было так жарко!"
        menu:
            Lisa_09 "Да, кстати, очень жарко тут. Я ещё не привыкла к этому климату. С другой стороны, не так жалко ту одежду, что пропала во время переезда."
            "Ты им звонила, мам, узнала где наши вещи?":
                menu:
                    Ann_00 "Звонила. Говорят, отправили в другой город по ошибке, а потом и вовсе потеряли. Обещают компенсировать, но когда - пока неизвестно..."
                    "Ну и обойдёмся без неё":
                        $ talk_var['blog'] = 1
                        menu:
                            Alice_00 "Ты и рад, наверное, голым ходить, а у меня там были хорошие вещички, в которых я блог веду обычно..."
                            "Может и рад. Мне стесняться нечего!":
                                menu:
                                    Alice_06 "Ну да, на словах все такие храбрые. А на деле..."
                                    "Что, богатый жизненный опыт?":
                                        jump .bf_change
                                    "Да я хоть сейчас покажу!":
                                        jump .bf_change
                                    "На слабо берёшь?":
                                        jump .bf_change
                            "Да всем плевать, в чём ты там что ведёшь":
                                menu:
                                    Alice_06 "Это тебе плевать! А бьюти-блогер должна каждый раз выглядеть по-новому!"
                                    "Да на тебя вещей не напасёшься!":
                                        jump .bf_change
                                    "У тебя репа не треснет с такими запросами?":
                                        jump .bf_change
                            "Раз ты такой успешный блогер, купишь новые":
                                menu:
                                    Alice_00 "Ну, когда-нибудь, когда раскручусь. А вот ты чем будешь заниматься? Штаны просиживать?"
                                    "И что ты там раскручиваешь?":
                                        jump .bf_earn3
                                    "Я придумаю и заработаю!":
                                        jump .bf_earn
                    "Вот заработаю и куплю всё, что потеряли...":
                        jump .bf_buy_new
            "Ничего страшного, купим новую!":
                jump .bf_buy_new
            "Я не понял, а где кондиционеры?":
                menu:
                    Ann_00 "Про кондиционеры я всё узнала. Дом не успели достроить и не вся техника и мебель была закуплена. А теперь уже и не знаю. Видимо, самим придётся всё остальное докупать."
                    "Ну и купим, без проблем":
                        jump .bf_buy_new
                    "Вот попробую заработать и всё наладится":
                        jump .bf_earn
                    "Ну что, копим на кондиционеры?":
                        menu:
                            Ann_15 "Да и без кондиционеров проживём. Как-то же справлялись. Да, здесь климат совсем другой, но человек ко всему привыкает. Да и не до того пока."
                            "Ну а если что, всегда можно снять лишнее":
                                menu:
                                    Alice_09 "Ага, специально для тебя все сейчас разденемся до гола!"
                                    "Я не против!":
                                        menu:
                                            Alice_07 "Никто и не сомневается. Может быть, сам и покажешь пример?"
                                            "Да я хоть сейчас!":
                                                jump .bf_change
                                            "На слабо разводишь?":
                                                jump .bf_change
                                            "Я тебе покажу. Всё покажу...":
                                                jump .bf_change
                                    "Начинай, я уже в предвкушении...":
                                        menu:
                                            Alice_07 "Никто и не сомневается. Может быть, сам и покажешь пример?"
                                            "Да я хоть сейчас!":
                                                jump .bf_change
                                            "На слабо разводишь?":
                                                jump .bf_change
                                            "Я тебе покажу. Всё покажу...":
                                                jump .bf_change
                                    "Ну и ходи в своих джинсах дома":
                                        menu:
                                            Alice_13 "А больше ничего и не остаётся. Вещей то нет. Может быть, на шоппинг сходим, если деньги будут..."
                                            "Кто о чём, а Алиса о шоппинге...":
                                                jump .bf_change
                                            "Сначала заработай":
                                                jump .bf_change
                            "Да я бы и в трусах не прочь ходить":
                                menu:
                                    Alice_07 "Дикарь! Ты в одной комнате с младшей сестрёнкой живёшь, забыл?"
                                    "А может быть, Лиза и не против?":
                                        jump .bf_change
                                    "Я же в трусах, а не без них":
                                        jump .bf_change
                                    "А это тут причём?":
                                        jump .bf_change

    label .bf_buy_new:
        menu:
            Alice_06 "Ага, вот только купилка у некоторых не выросла ещё!"
            "Да моей купилке любой позавидует!":
                menu:
                    Alice_15 "Так ты ею будешь зарабатывать? Любопытно..."
                    "Да пошла ты!":
                        jump .bf_change
                    "А ты чем зарабатываешь?":
                        jump .bf_earn3
            "А у самой то денег куры не клюют, да?":
                menu:
                    Alice_14 "Я ещё не раскрутилась. Но со временем всё будет в шоколаде!"
                    "И что ты там раскручиваешь?":
                        jump .bf_earn3
                    "Не всё то шоколад, что коричневого цвета!":
                        jump .bf_change
            "Ну вот возьму и заработаю":
                jump .bf_earn

    label .bf_change2:
        menu:
            Ann_00 "Так, всем спасибо за завтрак. А мне уже пора убегать на работу. Алиса, как всегда, моет посуду после завтрака, а Лиза после ужина. Макс, если захочешь помочь сёстрам, они будут только рады."
            "Не сомневаюсь":
                pass
            "Вот ещё...":
                pass
            "Посмотрим...":
                pass
        menu:
            Ann_00 "Да, Макс. Я когда прибиралась, нашла какие-то коробки. Видимо, остались с ремонта. Посмотри, если ничего ценного нет, потом выбросим. Сейчас они у тебя в комнате."
            "Хорошо, я посмотрю":
                jump .end_bf
            "А что за коробки?":
                menu:
                    Ann_00 "Если бы я знала, то не стала бы у тебя спрашивать. Я в электронике не разбираюсь. Посмотри сам."
                    "Понял. Посмотрю...":
                        jump .end_bf

    label .end_bf:
        $ AvailableActions['unbox'].enabled = True
        $ dishes_washed = False  # посуда грязная, кто-то должен ее помыть
        $ spent_time = 60
        $ current_room = house[6]
        $ AvailableActions['dishes'].enabled = True

        jump Waiting


label breakfast_2:
    $ __mood = 0

    Ann_07 "Всем приятного аппетита... Хотя, постойте. Вчера Лиза сходила в школу и я забыла спросить про оценки. Что-нибудь проверяли, спрашивали?"
    Lisa_09 "Ну... Так... Немного..."
    Ann_01 "Лиза, что спрашивали и что ты ответила?"
    Lisa_00 "Ну мам... У нас в прошлой школе не было анатомии, а тут химико-биологический класс с углублённым изучением. Конечно, я не смогла ответить!"
    scene BG punish-morning 00
    $ renpy.show("Ann punish-morning 00"+ann.dress)
    menu:
        Ann_01 "Что значит конечно не смогла? Хочешь, чтобы и тебя выперли из школы, как этого балбеса?"
        "Я не балбес! Я всё знаю!":
            pass
        "Меня не за знания выгнали!":
            pass
    Ann_00 "Ну раз ты такой умный, Макс, то вот и помогай своей младшей сестре. А ты, Лиза, иди сюда. Сейчас я тебя накажу, чтобы ты взялась за ум!"
    scene BG punish-morning 01
    show Lisa punish-morning 01
    $ renpy.show("Ann punish-morning 01"+ann.dress)
    $ poss['sg'].OpenStage(0)
    menu:
        Lisa_09 "Ну мам... Я же не специально. Я обещаю, что всё выучу!"
        "{i}Наблюдать{/i}":
            Ann_01 "Быстро! На этот раз можешь джинсы не снимать. Но в следующий раз получишь по голой заднице у всех на глазах. Иди сюда!"
            ## наказание Лизы
            scene BG punish-morning 02
            $ renpy.show("Ann punish-morning lisa-01"+ann.dress)
            $ __mood -= 50 # если Лизу наказывают, ее настроение портится
            $ talk_var['lisa.pun'] += 1
            Lisa_10 "Ой... Мам! Больно!"
            $ renpy.show("Ann punish-morning lisa-02"+ann.dress)
            Ann_01 "Давай терпи. За двойки я всегда наказываю. В этот раз не сильно, чтобы ты понимала, что никакие отговорки или причины меня интересовать не будут. Получила двойку, получила по заднице у всех на глазах. Ясно?"
            Lisa_09 "Ой. Да. Ясно, мам. Я всё поняла!"
            scene BG punish-morning 01
            show Lisa punish-morning 02
            $ renpy.show("Ann punish-morning 01"+ann.dress)
            Ann_00 "Вот и хорошо, что поняла. Теперь иди садись. Прошу прощения, что пришлось прервать завтрак, но иначе нельзя."
            scene BG punish-morning 00
            $ renpy.show("Ann punish-morning 00"+ann.dress)
            menu:
                Ann_00 "И да, если узнаю, что кто-то мне врёт, тот получит гораздо сильнее. Больше всего ненавижу ложь. Всё ясно?"
                "Ясно...":
                    pass
                "Я тут вообще ни при чём":
                    $ __mood -= 20
                "{i}молчать{/i}":
                    pass
            ## опять усадить всех за стол
            $ seat_Breakfast()
            Ann_05 "Так, всё, вернёмся к нашему завтраку. Кто нужно сделал выводы, а остальным бояться нечего. Приятного аппетита!"
            Max_00 "Приятного аппетита"
        "Мама! Лиза права. Дай ей шанс подготовиться. Я ей помогу!":
            $ __mood += 120
            Ann_00 "Лиза! Скажи спасибо своему брату, что он за тебя заступился."
            Max_01 "Да не стоит..."
            ## опять усадить всех за стол
            $ seat_Breakfast()
            menu:
                Lisa_02 "Спасибо, Макс! Ты же мне поможешь с уроками?"
                "Конечно, Лиза!":
                    $ __mood += 30
                "Посмотрим...":
                    $ __mood -= 30
            Ann_00 "Так, хватит, потом разберётесь. Сейчас пора завтракать. А то на работу опоздаю. Давайте садитесь, приятного аппетита!"
            Max_00 "Приятного аппетита"
    menu:
        Ann_00 "Давайте сменим тему. Скажите, только меня смущают картины, которые висят в наших комнатах?"
        "Какие картины?":
            menu:
                Alice_01 "Макс, не притворяйся, что не видел. В наших спальнях с мамой уже была вся мебель и картины, в том числе. Наверняка, пялился на них, когда увидел..."
                "И ничего я не пялился!":
                    Alice_07 "Ага. Где же ещё увидеть такие картинки, раз в интернете провайдер всё блокирует, правда?"
                    Max_03 "А вот и нет! Но картины красивые..."
                "Ну и что. Хорошие картины...":
                    Alice_01 "Да ты любым будешь рад, особенно таким... Но да, я согласна с Максом, красивые. Лично меня всё устраивает!"
        "Ты про тех голых женщин в ваших спальнях?":
            Alice_01 "Да, Макс, про тех. А что мам тебе не нравится? Там же нет ничего такого. Думаю, что это даже искусство... Лично меня всё устраивает!"
    Ann_05 "Ну, если вы так говорите... Я сначала хотела их снять, чтобы не смущать никого. Ваш отец, видимо, холостяцкий дом строил и оформлял соответственно... Но если никого не смущает, то и меня всё устраивает."
    Lisa_10 "Кстати, про него не было новостей?"
    Ann_01 "Нет, и слава богу. Конечно, я рада этому подарку, этому дому. Хотя, до сих пор не понимаю с чего он так расщедрился. Но даже так не компенсировать пропущенные годы вашего воспитания и семейной жизни..."
    menu:
        Ann_00 "Так, всем спасибо за завтрак, мне пора на работу. Сегодня мне позвонили и сказали, что приедет машина, довезёт до работы. Нельзя опаздывать..."
        "Что, от Эрика?":
            menu:
                Ann_12 "Да... Видимо, так компания старается поддерживать новичков..."
                "Что-то я сомневаюсь...":
                    pass
                "Может быть. Тогда, поспеши!":
                    jump .ok
        "Что, сам Эрик приедет?":
            menu:
                Ann_05 "Нет, Макс, что ты. Он большой начальник. Босс моего босса. Его тоже возит свой водитель. Просто... Я думаю, что так компания поддерживает новичков..."
                "Что-то я сомневаюсь...":
                    pass
                "Может быть. Тогда, поспеши!":
                    jump.ok
        "Тогда поспеши!":
            jump .ok

    Ann_00 "Кто знает. Посмотрим, к чему это всё приведёт. В любом случае, я рада, что не придётся трястись в общественном транспорте и теперь точно успею. Ну всё, я побежала!"
    Max_00 "Давай, удачи..."
    $ AddRelMood("lisa", 0, __mood)
    jump after_breakfast

    label .ok:
        Ann_07 "Ну всё, ещё раз всем спасибо. А тебе, Лиза, удачи в школе. Не подведи меня!"
        Max_01 "Пока, мам..."
        $ AddRelMood("lisa", 0, __mood)
        jump after_breakfast


label breakfast_3:
    $ __mood = 0
    Ann_05 "Всем приятного аппетита! Хотя, за завтраком обычно не принято болтать, но в нашей семье это уже давно не так. Поэтому, рассказывайте - у кого какие новости?"
    Alice_02 "У меня не совсем новость, а скорее вопрос. Скоро же выходные, да?"
    Max_01 "А тебе какая разница?"
    Alice_01 "Отвали, Макс. Дело в том, что я бы хотела сходить в ночной клуб, а у меня ни одного подходящего платья нет!"
    menu:
        Ann_01 "Алиса, мы не в том положении, чтобы покупать тебе платья для клубов. Да и о чём ты говоришь? Ты бы делом занялась, а не о клубах думала!"
        "Мама всё правильно говорит!":
            $ __mood -= 50
        "{i}молчать{/i}":
            pass
    Alice_13 "Мам! Я молодая, красивая, мне надо развлекаться. Ты сама рассказывала, как раньше зажигала, а мне не даёшь?"
    menu:
        Ann_14 "Ну, Алиса... Я тебя понимаю, конечно. Но ты же хочешь какое-то дорогое платье, наверняка? Сейчас у нас не очень много денег, ты сама знаешь..."
        "Может быть, помочь?":
            Ann_01 "Ого, Макс! Да ты у нас тайный миллионер? И откуда у тебя доходы? Не я ли тебе деньги даю на карманные расходы?"
            Max_00 "Ну да, погорячился..."
        "{i}молчать{/i}":
            pass
    Alice_06 "Мам, да мне не обязательно дорогое. Главное, чтобы стильное, красивое, короткое..."
    Ann_01 "Что значит короткое? Ты там чем собралась заниматься в своём клубе? Я не хочу, чтобы моя дочь в таком виде разгуливала по ночным клубам!"
    Alice_13 "Мам, ну не слишком короткое... В общем, любое. Главное, чтобы можно было пойти! Ну ма-ам..."
    menu:
        Ann_01 "Ну не знаю, Алиса. Посмотрим. Кстати, завтра после завтрака вы все едем на шоппинг. Ну, кроме Макса, наверное..."
        "Э... Почему кроме меня?":
            menu:
                Ann_05 "Ты знаешь, мне кажется, что тебе будут мало интересны магазины со шмотками. У тебя всё есть, а нам, девочкам, нужно кое-что прикупить..."
                "Так у вас же денег нет?":
                    jump .nomany
                "И кто вас повезёт?":
                    jump .driver
        "Не очень то и хотелось...":
            menu:
                Ann_05 "Вот и я так подумала. Разве тебе будут интересны наши девчачьи магазины? А вот нам очень. Как раз всем нам нужно кое-что прикупить..."
                "Так у вас же денег нет?":
                    jump .nomany
                "И кто вас повезёт?":
                    jump .driver
    label .nomany:
        Ann_00 "Ну мы же не будем крупные покупки делать типа дорогих вечерних платьев, так, по мелочи..."
        Max_07 "Ясно. И кто вас повезёт?"

    menu .driver:
        Ann_01 "Макс, ну я же уже говорила про Эрика, вот он за нами отправит машину, а с ним мы встретимся уже в магазине..."
        "Так ты знакомишь Эрика с семьёй? Без меня?":
            Ann_00 "Ну это не совсем так. Раз уж он нам... мне так помогает во всём, было бы неприлично отказываться и от предложения свозить нас на шоппинг..."
            Max_09 "Надеюсь, я то его увижу, когда вернётесь?"
        "Надеюсь, я то его увижу, когда вернётесь?":
            pass
    Ann_00 "Не знаю, Макс, посмотрим. Возможно, завтра вечером после шоппинга он заедет к нам на ужин, там ты с ним и познакомишься..."
    Lisa_01 "И какой он, мам? Рассказывай! Значит, у вас всё серьёзно, да? А вы уже целовались?"
    menu:
        Ann_04 "Лиза! Какие вопросы... Нельзя же так спрашивать в лоб! Возможно, у нас всё серьёзно, да. Я давно не встречала такого мужчину. Честно говоря, вообще никогда таких не встречала. Он почти идеален!"
        "Ага! Почти?":
            Ann_01 "Макс, ну мы ещё недостаточно друг друга знаем, вдруг окажется, что у него есть какие-то секреты. Поэтому, я и говорю \"почти\". Но думаю, что это тот самый мужчина..."
            Max_08 "Ты не слишком торопишься с выводами?"
            menu:
                Ann_05 "Думаю, что нет. Но... посмотрим. Кажется, вы нас женили ещё до того, как мы признались друг другу в симпатии..."
                "А вы уже признались?":
                    jump .conf
                "Кто говорит о свадьбе?":
                    jump .wedd
                "А ты сама не слишком спешишь?!":
                    jump .hurry

        "И какие недостатки?":
            menu:
                Alice_04 "Макс, тебе не всё ли равно? Очевидно же, что маме нравится этот Эрик. Лучше порадуйся за неё!"
                "А я рад. Правда.":
                    menu:
                        Ann_05 "Спасибо, Макс. Для меня очень важна поддержка семьи. Хотя, меня немного смущает, что вы как будто нас уже поженили мысленно ещё до того, как мы признались друг другу в симпатии..."
                        "А вы уже признались?":
                            jump .conf
                        "Кто говорит о свадьбе?":
                            jump .wedd
                        "А ты сама не слишком спешишь?!":
                            jump .hurry
                "Мне просто любопытно!":
                    menu:
                        Ann_05 "Не сомневаюсь, что любопытно. Не стоит забегать вперёд. Меня даже немного смущает, что вы как будто нас уже поженили мысленно ещё до того, как мы признались друг другу в симпатии..."
                        "А вы уже признались?":
                            jump .conf
                        "Кто говорит о свадьбе?":
                            jump .wedd
                        "А ты сама не слишком спешишь?!":
                            jump .hurry
    label .conf:
        Ann_01 "Макс! Мне кажется, стоит сменить тему. Я не хочу пока об этом говорить..."
        Max_00 "Хорошо..."
        jump .end

    label .wedd:
        Ann_14 "Ну я образно... И, вообще, давайте сменим тему!"
        Max_00 "Хорошо..."
        jump .end

    label .hurry:
        Alice_13 "Макс! Ну сколько можно? Мама сама разберётся. Лично я очень за неё рада. Думаю, Лиза тоже. А вот ты... не знаю. Ладно, давайте сменим тему, а то Макс что-то докапывается..."
        Max_09 "И ничего я не докапываюсь..."

    menu .end:
        Ann_00 "Так, ладно. Кажется, завтрак закончен, все уже наелись. Мне пора на работу, а Лизе в школу. Алиса, не забудь вымыть посуду!"
        "{i}закончить завтрак{/i}":
            pass

    $ AddRelMood("alice", 0, __mood)
    jump after_breakfast


label breakfast_4:
    Ann_01 "Всем приятного аппетита. Это наш первый выходной в новом доме и сегодня у нас в планах кое-что приятное, правда?"
    Max_11 "Если ты о шоппинге, то меня вы всё равно не берёте..."
    Ann_01 "Макс, ну мы же это уже обсуждали. Тебе с нами будет не интересно. А с Эриком ты и так познакомишься, просто чуть позже, вечером"
    Max_00 "Как скажешь, мам..."
    menu:
        Alice_01 "Макс, мне показалось или ты как-то предвзято относишься к Эрику? Как будто уже его ненавидишь..."
        "Ну, я его не знаю...":
            Ann_01 "Макс, я тебя прекрасно понимаю и тоже сомневалась бы на твоём месте, но поверь, у тебя будет возможность с ним познакомиться и узнать лучше..."
            Max_00 "Ну, хорошо..."

        "А вдруг он не тот, за кого себя выдаёт":
            menu:
                Lisa_03 "И за кого он себя выдаёт? За человека, которому нравится мама, а на само деле он... кто?"
                "Ну не знаю. Может, он маньяк...":
                    Ann_01 "Макс, ты слишком много сериалов смотришь. Стоит допустить на миг, что не все кругом маньяки, убийцы и насильники."
                    Max_00 "Хорошо. Извини, мам..."
                "Дело не в этом, я не знаю его мотивов...":
                    Ann_01 "Вот и не стоит раньше времени предполагать худшее. Познакомишься уже сегодня и выяснишь для себя всё, что нужно..."
                    Max_00 "Ну, хорошо..."
                "Может он очередной придурок!":
                    Alice_06 "Ой, кто бы говорил! Очередной... Маму повысили в первую неделю, дали личного водителя, на шоппинг вот везут, а ты всё ворчишь. Не веди себя сам как придурок и люди к тебе потянутся!"
                    Max_09 "Ладно, посмотрим на вашего Эрика..."
        "Я переживаю о маме":
            menu:
                Alice_02 "Да ты не переживать должен, а радоваться, что у мамы налаживается её личная жизнь! К тому же, ещё и с работой так повезло и даже повышение в первую неделю светит..."
                "Ладно, ладно. Посмотрим...":
                    pass
                "Да я рад...":
                    pass
    Ann_05 "Вот и отлично! Хватит уже про Эрика, давайте обсудим что планируем купить.."
    if poss['Swimsuit'].stn < 0:
        Lisa_03 "Я знаю! Мне нужен купальник! Такой, чтобы можно было загорать и чтобы такой, ну вы понимаете, да?"
        $ poss['Swimsuit'].OpenStage(1)
    else:
        Lisa_03 "Я знаю! Мне нужен купальник! Такой, чтобы можно было загорать и чтобы такой, ну вы понимаете, да?"
    Max_03 "Конечно, как тут не понять..."
    Alice_01 "Лиза! Хватит тараторить. Купальник у тебя уже есть, а вот клубного платья у меня нет ни одного вообще. Так что, сначала мне!"
    Max_05 "Не подеритесь!"
    Lisa_12 "У меня купальник закрытый и в нём не позагорать. А клубы твои ничем хорошим не заканчиваются... Особенно, когда..."
    Max_07 "Что особенно? Подробнее, пожалуйста..."
    Alice_09 "Лиза! Заткнись, пожалуйста. Хватит об этом. Ладно, сначала тебе купальник, потом мне платье..."
    Max_08 "Я не понял. Что это было? О чём Лиза ты хотела рассказать?"
    Lisa_10 "Мне кажется, Алиса не хочет, чтобы я что-то рассказывала... Так что сам с ней разбирайся..."
    Max_02 "Обязательно разберёмся. Мне же интересно!"
    Ann_00 "Не знаю о чём речь, но думаю, вы и правда между собой всё выясните. А сейчас пора собираться на шоппинг. Всем спасибо за завтрак!"
    Max_01 "Да, спасибо..."
    jump after_breakfast


label breakfast_5:
    Ann_01 "Всем доброе утро, приятного аппетита..."
    Max_07 "Ну что, как всё прошло?"
    menu:
        Ann_14 "Ты о чём, Макс? Я не понимаю..."
        "Как о чём? Про ночь с Эриком!":
            pass
        "Я про визит к Эрику...":
            pass
    Ann_01 "Всё в порядке, спасибо. Не думаю, что стоит это сейчас обсуждать..."
    Max_00 "Как скажешь, мам..."
    Lisa_02 "А ты часто теперь будешь к нему ездить так... на ночь?"
    Max_09 "Хороший вопрос..."
    Ann_12 "Лиза, я даже не знаю что тебе сказать... Я и Эрик... нравимся друг другу. И иногда он будет приходить к нам. Иногда я к нему. Это нормально для взрослых. Ты же меня понимаешь?"
    menu:
        Alice_04 "Да всё мы понимаем, мам. Не переживай. Просто, ты так долго была одна и тут такой... Эрик... Мы очень рады, что у тебя налаживается твоя личная жизнь. И мы не будем тебе мешать, да, Макс?"
        "А что сразу я? Но да, я согласен с Алисой...":
            pass
        "Конечно!":
            pass
    Ann_05 "Я очень рада, что вы у меня такие... сообразительные."
    Max_07 "Значит, Эрик будет и к нам приходить на ночь?"
    Alice_01 "Макс! Ну вот опять. Мы же сказали, что не будем вмешиваться и лезть с вопросами..."
    Max_08 "Да я просто спросил..."
    menu:
        Ann_01 "Да всё в порядке, Алиса. Я понимаю, Максу любопытно. Это же и нарушение вашего личного пространства, когда кто-то посторонний начинает посещать наш общий дом."
        "Да, вот интересно, как часто он будет нарушать это пространство...":
            $ __ann = -20
        "Ага, мне просто любопытно...":
            $ __ann = 0
    menu:
        Ann_12 "Ещё рано об этом говорить, но... может быть... будем с ним встречаться через день-два, то у него, то у нас... Может быть..."
        "Ого, так часто?":
            Alice_09 "Макс! Это уже не смешно. Завязывай с допросом. Мама сама разберётся когда ей и с кем встречаться! Да, мам?"
            Ann_00 "Да, Алиса. Если вы все подружитесь с Эриком, я буду очень рада. Для меня это очень важно. Ну а пока, хватит о нём. Думаю, завтрак окончен. Всем большое спасибо!"
            Max_00 "Спасибо..."
            jump after_breakfast
        "Может, ему переехать сюда тогда?":
            Ann_14 "Ну пока рано об этом говорить. Мы только познакомились. Посмотрим, может быть, однажды..."
            Max_08 "Ого!"
            Ann_01 "Макс, я уже сказала, что это возможно, но будет ли и когда - неизвестно. Так что, не будем гадать. Кстати, завтрак затянулся... Всем большое спасибо!"
            Max_00 "Спасибо..."
            jump after_breakfast
        "Может, тебе к нему переехать?":
            Ann_01 "Макс! Не говори глупостей. Я ваша мать и буду рядом с вами, конечно. Никуда я не уеду. Не переживай."
            Max_04 "Это хорошо..."
        "Понятно...":
            menu:
                Ann_05 "В любом случае, для вас ничего не изменится. А если вы подружитесь с Эриком, я буду очень рада!"
                "Может быть...":
                    pass
                "Никогда!":
                    Ann_00 "Очень жаль, Макс, что ты так настроен. Эрик очень хороший человек и мне кажется, ты просто в нём не разглядел то, что вижу я. Но хватит об Эрике. Завтрак затянулся. Всем большое спасибо!"
                    Max_00 "Спасибо..."

    Ann_05 "Конечно, я буду очень рада, если вы все найдёте общий язык с Эриком и подружитесь. Но хватит о нём. Думаю, завтрак окончен. Всем большое спасибо!"
    Max_00 "Спасибо..."
    $ AddRelMood("ann", 0, __ann)
    jump after_breakfast


label breakfast:
    $ current_room = house[5]
    $ Distribution()

    if day > 1 and 'smoke' not in dcv:
        ## Добавляем возможность курения Алисы
        $ dcv['smoke'] = Daily(done=True, enabled=True)
        # $ AddSchedule(plan_alice,
        $ alice.add_schedule(
            Schedule((1, 2, 3, 4, 5), "13:0", "13:29", "smoke", _("курит"), "house", 6, "alice_smoke", glow=105, variable="dcv['smoke'].done"),
            Schedule((1, 2, 3, 4, 5), "13:0", "13:29", "swim", _("в бассейне"), "house", 6, "alice_swim", glow=105, variable="not dcv['smoke'].done"),
            )
        $ flags['smoke.request'] = None # требование при курении
        $ flags['smoke'] = None
        $ talk_var['smoke'] = False

    jump StartPunishment


label breakfast_after_punishment:
    $ renpy.block_rollback()

    $ seat_Breakfast()

    if day == 1:
        jump breakfast_first
    elif day == 2:
        jump breakfast_2
    elif day == 3:
        jump breakfast_3
    elif day == 4:
        jump breakfast_4
    elif day == 5:
        jump breakfast_5
    else:
        jump typical_breakfast

    jump after_breakfast
