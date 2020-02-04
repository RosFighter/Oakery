
label LisaTalkStart:

    $ dial = TalkMenuItems()
    if len(dial) == 0:
        jump AfterWaiting

    $ __CurShedRec = GetScheduleRecord(schedule_lisa, day, tm)
    if __CurShedRec.talklabel is not None:
        call expression __CurShedRec.talklabel from _call_expression_5

    $ dial.append((_("{i}уйти{/i}"), "exit"))

    Lisa_00 "Макс, решил поболтать?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        $ __mood = GetMood("lisa")[0]
        if __mood < talks[rez].mood:
            if __mood < -2: # Настроение -4... -3, т.е. всё ну совсем плохо
                jump Lisa_badbadmood
            elif __mood < 0: # Настроение -2... -1, т.е. всё ещё всё очень плохо
                jump Lisa_badmood
            else: # Настроение хорошее, но ещё недостаточное для разговора
                jump Lisa_normalmood
        elif talks[rez].kd_id != "" and talks[rez].kd_id in cooldown and not ItsTime(cooldown[talks[rez].kd_id]):
            jump Lisa_cooldown
        elif renpy.has_label(talks[rez].label): # если такая метка сушествует, запускаем ее
            call expression talks[rez].label from _call_expression_6
        jump LisaTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Lisa_badbadmood:
    menu:
        Lisa_09 "Макс, уйди. Не хочу тебя видеть!"
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Lisa_asksorry


label Lisa_badmood:
    menu:
        Lisa_09 "Макс, уйди пожалуйста. Не хочу сейчас общаться."
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Lisa_asksorry


label Lisa_asksorry:
    menu:
        Lisa_09 "Извиниться? Как?"
        "Кажется, я передумал...":
            jump Waiting


label Lisa_normalmood:
    menu:
        Lisa_09 "Не сейчас, Макс..."
        "Ок...":
            jump Waiting


label Lisa_cooldown:
    Lisa_09 "Макс, давай поговорим об этом в другой раз."
    Max_00 "Хорошо, Лиза..."
    jump AfterWaiting


label MorningWood:

    scene BG char Lisa morning-oops-01
    show Lisa morning-oops 01
    menu:
        Lisa_11 "Макс! Это что такое?! Я сейчас маму позову!"
        "Что? Ты о чём?":
            pass
        "Что случилось?":
            pass

    Lisa_12 "Ты чем таким занимался при мне?!"
    Max_12 "Да ты о чём, вообще?"
    scene BG char Lisa morning-oops-02
    show Lisa morning-oops 02
    menu:
        Lisa_13 "Ма-ам! Иди сюда, скорее!"
        "Да это не то, о чём ты думаешь...":
            menu:
                Lisa_12 "Не то, о чём думаю? Это явно то, о чём я думаю! Ма-ам!"
                "Да не ори ты так!":
                    pass
                "Ничего же не случилось...":
                    pass
        "Просто, так бывает утром иногда...":
            menu:
                Lisa_12 "Так я тебе и поверила! Ма-ам!"
                "Ну что же ты орёшь так...":
                    pass
                "Давай всё мирно уладим...":
                    pass
    scene Lisa morning-oops 03
    Ann_15 "Лиза? Что случилось?!"
    scene BG char Lisa morning-oops-04-05
    show Lisa morning-oops 04
    Lisa_12 "Мам! Смотри, что у него!"
    menu:
        Ann_19 "Макс! Объяснишь, чем ты занимался при сестре?!"
        "Да я просто спал, это само...":
            Ann_09 "Ну, если ничего не делал и само... Тогда, Лиза, Макс ни в чём не виноват. Так бывает у мальчиков..."

        "Так бывает по утрам, я не специально...":
            Ann_09 "Ну, да, Лиза. Так у мальчиков иногда бывает по утрам. Не нужно паниковать..."
    Max_11 "Я так сразу и сказал..."
    Lisa_12 "Это не правда! Так не может быть... само. Он что-то делал, наверняка..."
    Max_10 "Да ничего я не делал!"
    show Lisa morning-oops 05
    Ann_08 "Ты сама видела, чтобы Макс чем-то {i}таким{/i} занимался при тебе?"
    Lisa_09 "Нет, но мам... Я просто испугалась."
    scene Lisa morning-oops 06
    Ann_04 "Лиза. Ты, похоже, совсем ничего не знаешь о мальчиках. С одной стороны, я рада, что ты у меня такая. А с другой..."
    Lisa_10 "А что с другой? Я хочу всё знать!"
    menu:
        Ann_09 "Нет, Лиза, тебе ещё рано таким интересоваться. Вот подрастёшь, тогда и поговорим. На этом всё. Сделаем вид, что ничего не было. Ясно?"

        "Ясно...":
            pass

    $ flags["morning_erect"] = 1
    $ SetPossStage("seduction", 0)
    $ spent_time = 30
    jump Waiting


label AfterSchoolFD:
    $ current_room = house[6]
    scene BG incoming-00
    show Lisa incoming-01
    Lisa_01 "Привет, Макс! Я вернулась."
    Max_03 "Супер! Как первый день?"
    Lisa_02 "Да ничего так. Но потом поболтаем. Сейчас переоденусь и прыгну в бассейн. Только об этом и мечтала целый день!"
    Max_04 "Хорошо, здесь и поговорим"

    $ spent_time = 10
    jump Waiting


label about_school:
    $ talk_var["lisa_fd"] += 1
    menu:
        Lisa_00 "Неужели, я дома! До сих пор не могу поверить, что ЭТО наш дом!"
        "Да я сам в шоке!":
            menu:
                Lisa_03 "Вот-вот! Целый день думала о нашем бассейне. Неужели, здесь всегда такая погода?"
                "Да, мы почти в раю":
                    menu:
                        Lisa_02 "Хотелось бы так думать..."
                        "Ну, как дела в школе?":
                            jump .school
                        "Нашла дорогу домой от школы?":
                            jump .way
                "Может быть, тут ураганы бывают?":
                    menu:
                        Lisa_02 "Ага! И сезон дождей 11 месяцев в году!"
                        "Ну, как дела в школе?":
                            jump .school
                        "Нашла дорогу домой от школы?":
                            jump .way
        "Так как дела в школе?":
            jump .school
        "Не заблудилась по дороге?":
            jump .way

    menu .way:
        Lisa_02 "Ты знаешь, тут школа совсем рядом! Пять минут и я на месте. К тому же, топографическим кретинизмом не страдаю... Ты же поэтому из дома не выходишь, да?"
        "Очень смешно!":
            menu:
                Lisa_01 "Ну а почему же ты тогда всё время дома сидишь? Что в старой квартире, что тут. Ты же сегодня даже из дома не выходил?"
                "А меня всё устраивает":
                    Lisa_10 "Бедняжка. Ну, ничего. И тебя вылечат!"
                    Max_04 "Так что там в школе?"
                    jump .school
                "Здесь я никого не знаю":
                    menu:
                        Lisa_09 "Понимаю. Я тоже никого не знаю... почти."
                        "Почти? С кем-то познакомилась?":
                            menu:
                                Lisa_02 "Может быть... А что, любопытно? Или ревнуешь?"
                                "Так кто он?":
                                    jump .who
                                "И ничего я не ревную":
                                    menu:
                                        Lisa_03 "Ну и правильно! Ты же мой брат и останешься самым любимым мужчиной в моей жизни!"
                                        "Вот это признание!":
                                            pass
                                        "Я тоже тебя люблю, сестрёнка":
                                            pass
                                    Lisa_02 "Но ты слишком не зазнавайся. И никому не рассказывай!"
                                    Max_04 "Договорились!"
                                    jump .ok
                                "Ну и не рассказывай, если не хочешь...":
                                    jump .want
                        "Так что там в школе?":
                            jump .school
                "Просто... не люблю людей":
                    menu:
                        Lisa_03 "Вот это признание! А нас ты просто терпишь, да?"
                        "Ну, приходится...":
                            Lisa_10 "Бедняжка. Ну, ничего. И тебя вылечат!"
                            Max_04 "Так что там в школе?"
                            jump .school
                        "Вы - исключение":
                            Lisa_02 "Ну спасибо и на том. Если что, то ты тоже ничего..."
                            Max_04 "Так что там в школе?"
                            jump .school
                        "Да я пошутил":
                            Lisa_02 "Я так и поняла! Вообще, шутки у тебя... как всегда!"
                            Max_04 "Так что там в школе?"
                            jump .school
        "Хм... Ты слишком счастливая. Что-то случилось в школе?":
            jump .school

    label .school:
        Lisa_00 "Ты знаешь, школа отличная! Меня хорошо приняли, все такие доброжелательные... А некоторые особенно..."
        Max_05 "Некоторые? Ты о ком?"
        Lisa_02 "Да так. Познакомилась кое-с-кем..."
        Max_02 "О, рассказывай! Кто он?"
        jump .who

    menu .who:
        Lisa_03 "А почему сразу он? Может быть, я завела подругу?"
        "Так кто он?":
            jump .boy
        "Что за подружка?":
            menu:
                Lisa_02 "Обычная такая подружка... Какие подружки бывают обычно, вот у меня такая!"
                "Что-то ты мне голову морочишь...":
                    menu:
                        Lisa_03 "А что здесь такого? Это же весело!"
                        "Что-то я совсем запутался":
                            jump .ok
                        "Ну и не рассказывай, если не хочешь...":
                            jump .want
                "А имя у твоей подружки не мужское, случайно?":
                    Lisa_00 "Эх... Раскусил ты меня. Да, это не подружка..."
                    Max_00 "Так кто он?"
                    jump .boy

    menu .ok:
        Lisa_00 "Как у тебя день прошёл?"
        "Да как обычно...":
            menu:
                Lisa_03 "Обычно? Это ты свой первый день в таком месте и таком доме называешь обычным?!"
                "Ну, теперь то это будет обычно":
                    menu:
                        Lisa_02 "Это если нам повезёт и нас отсюда не выгонят. За неуплату чего-то..."
                        "Ты же у нас оптимист обычно?":
                            Lisa_00 "Обычно да, но до сих пор не верится, что наша жизнь так изменилась!"
                            Max_00 "Ладно, не будем о грустном"
                            jump .sad
                        "Ага. Или адвокат не заметит ошибку в документах какую-нибудь...":
                            Lisa_00 "Ладно, Макс, не будем о грустном. Может быть, всё будет хорошо!"
                            Max_00 "Да, ты права"
                            jump .sad
                "Ты права...":
                    jump .sad
        "Привыкаю ко всему":
            menu:
                Lisa_03 "Да уж, задача сложная. Невыносимые условия жизни и всё такое, да?"
                "Ну, я постараюсь":
                    jump .sad
                "Человек как таракан, ко всему привыкает":
                    jump .sad

    menu .sad:
        Lisa_02 "Так что планируешь делать, чем займёшься?"
        "Ещё не решил. Что посоветуешь?":
            Lisa_03 "Я бы посоветовала тебе искупаться, для начала. Собственно, я этим и планирую заняться!"
            Max_04 "Хорошая идея..."
            jump .goodplan
        "Придумаю ещё. А у тебя какие планы?":
            Lisa_03 "Лично я буду купаться и загорать. Загорать и купаться. Пока не надоест. А потом повторю!"
            Max_04 "Отличный план!"
            jump .goodplan
        "Буду думать как заработать":
            Lisa_00 "Что, прямо с первого дня? Отдохни, искупайся для начала. Может быть, мысли появятся..."
            Max_00 "Может, ты и права..."
            jump .goodplan

    menu .want:
        Lisa_00 "Может быть, в другой раз..."
        "А если я настаиваю?":
            menu:
                Lisa_02 "Что, ты правда такой любопытный? Не знала!"
                "Короче, рассказывай!":
                    jump .boy
                "Ой, всё...":
                    jump .ok
        "Договорились":
            jump .ok

    label .boy:
        $ talk_var["boy"] += 1
        $ cooldown["lisa_boy"] = CooldownTime("01:30")
        menu:
            Lisa_10 "Ну... его зовут Алекс. Мы учимся в одном классе. Даже сидим рядом..."
            "А подробнее?":
                Lisa_02 "А какие тут могут быть подробности? Мы учимся вместе, сидим в одном классе за одной партой... Ну и он со мной заговорил..."
                Max_00 "И что он сказал?"
                jump .say
            "И как вы познакомились?":
                Lisa_02 "Макс. Ну как ещё я могла познакомиться в первый день в школе с парнем? К тому же, если ещё и сидим рядом... Просто, он со мной заговорил..."
                Max_00 "И что он сказал?"
                jump .say
            "Расскажи о нём":
                menu:
                    Lisa_02 "Ну, парень как парень. Вот как ты, только не такой зануда и красивый."
                    "Я не зануда!":
                        Lisa_03 "Ещё какой зануда! Достаёшь меня допросами о моём парне..."
                        Max_06 "Ого, так он уже твой парень?!"
                        menu:
                            Lisa_10 "Нет, ну... я не так выразилась. Мы только познакомились и, конечно, он не мой парень!"
                            "А хотела бы, чтобы он им стал?":
                                menu:
                                    Lisa_01 "Думаю, что да. У меня ещё никогда не было парня. А этот..."
                                    "Значит, он тебе нравится?":
                                        jump .like
                                    "И что теперь?":
                                        jump .whatnow
                            "Я, между прочим, тоже ничего...":
                                menu:
                                    Lisa_03 "Ты мой братишка! Не говори ерунду. Мы и так с тобой спим вместе. Ну, в одной комнате!"
                                    "А ты своему парню скажешь, что спишь со своим братом?":
                                        pass
                                    "Спим вместе!":
                                        pass
                                menu:
                                    Lisa_00 "Дурак! Я же в шутку это сказала. И, вообще, прекращай меня доставать!"
                                    "Ладно, ладно. Ну а что он говорил?":
                                        jump .say
                                    "И что теперь?":
                                        jump .whatnow
                    "Значит, нравится мой типаж?":
                        menu:
                            Lisa_03 "А какой у тебя типаж? Неудачника, который достаёт младшую сестрёнку?"
                            "Эй, я не неудачник!":
                                jump .hey
                            "Я разве достаю? Просто интересуюсь твоей жизнью":
                                jump .hey
                    "А я тебе нравлюсь?":
                        menu:
                            Lisa_03 "Ну, когда не зануда, вполне!"
                            "А кто тебе нравится больше? Я или он?":
                                menu:
                                    Lisa_12 "Вот теперь ты зануда и нравишься мне с каждой секундой всё меньше и меньше..."
                                    "Ладно, ладно, извини...":
                                        menu:
                                            Lisa_03 "То-то же! А то ведёшь себя как придурок..."
                                            "А вот теперь я могу обидеться...":
                                                jump .hey
                                            "Я же в шутку. И, кстати, придурок - это обидно!":
                                                jump .hey
                                    "А он, значит, теперь нравится больше?":
                                        jump .like
                                    "И всё-таки?":
                                        Lisa_10 "Всё, Макс, достал меня. Дай отдохнуть, поплавать, позагорать..."
                                        Max_00 "Эх..."
                                        jump .end
                            "Значит, он тебе нравится?":
                                jump .like
                            "И что теперь?":
                                jump .whatnow

    menu .hey:
        Lisa_00 "Извини. Я не подумала. Кстати, спасибо, что со мной болтаешь. Я обычно о таком Алисе рассказывала, но она стала слишком взрослой и мы как-то отдалились..."
        "Ну, со мной ты всегда можешь поболтать":
            pass
        "Можешь на меня рассчитывать":
            pass
        "Только не превращай меня в свою подушку!":
            menu:
                Lisa_09 "Ну вот, только я хотела тебе поплакаться о разбитой любви, а ты..."
                "Что? Он уже тебя бросил?!":
                    menu:
                        Lisa_03 "Ага, два раза! Он ещё даже не знает, что мне нравится..."
                        "Значит, он тебе нравится?":
                            jump .like
                        "И что теперь?":
                            jump .whatnow
                "А я не убежал и всё ещё здесь!":
                    menu:
                        Lisa_03 "Ну, тогда терпи меня!"
                        "Значит, он тебе нравится?":
                            jump .like
                        "И что теперь?":
                            jump .whatnow
    menu:
        Lisa_02 "Ладно, буду иметь в виду!"
        "Значит, он тебе нравится?":
            jump .like
        "И что теперь?":
            jump .whatnow

    menu .say:
        Lisa_03 "А вот это уже тебя не касается. Что сказал, то сказал. Мне понравилось. Так и познакомились..."
        "Он тебе нравится?":
            jump .like
        "И что теперь?":
            jump .whatnow
        "Думаю, у вас всё получится":
            jump .willbeok

    menu .whatnow:
        Lisa_00 "Я не знаю. Это же только первый день. Посмотрим, как всё пойдёт. Может быть, он уже с кем-то встречается, а тут пришла я такая красивая..."
        "Всё будет хорошо":
            jump .willbeok
        "Если что, я всегда помогу советом":
            jump .help
        "А не рано тебе с кем-то встречаться?":
            menu:
                Lisa_12 "Ты в моём возрасте уже тусил с этой своей, как её... Правда, она тебя бросила..."
                "Это я её бросил":
                    menu:
                        Lisa_02 "Ну да, потом её караулил под окнами, чтобы сказать, как ты её не любишь..."
                        "Всё было не так!":
                            jump .no
                        "В любом случае, у меня опыта больше":
                            jump .xp
                        "Это всё в прошлом...":
                            jump .no
                "Так что, у меня есть опыт":
                    jump .xp

    label .no:
        Lisa_03 "Так или иначе, я не слышала, чтобы у тебя было много побед на любовном фронте..."
        Max_00 "Я же не обо всём рассказывал..."
        jump .yes

    menu .xp:
        Lisa_03 "Да уж, ты у нас опытный любовник!"
        "Я же не обо всём рассказывал...":
            jump .yes
        "Именно поэтому за советами обращайся ко мне":
            jump .so

    label .yes:
        menu:
            Lisa_02 "Любопытно... И о чём же ты умолчал?"
            "У меня было много девушек":
                Lisa_11 "Куча девушек? Надувных? Где же ты их всех прятал?"
                Max_14 "Парни о таком не рассказывают"
            "А вот это - секрет!":
                pass
            "Тебе лучше не знать...":
                pass
        menu:
            Lisa_12 "Так я тебе и поверила..."
            "В школе по мне все девушки с ума сходили":
                menu:
                    Lisa_02 "Ладно, ладно. Если ты так говоришь, пусть так."
                    "В любом случае, нужна будет помощь или совет - подходи":
                        jump .help
                    "Так или иначе, о парнях я знаю больше тебя...":
                        jump .so
            "Не хочешь - не верь. Но опыт у меня есть":
                jump .help

    label .so:
        Lisa_02 "Я подумаю над твоим предложением. А пока, мы что-то заболтались. Я бы хотела искупаться и позагорать..."
        Max_00 "Хорошо..."
        jump .end

    menu .like:
        Lisa_03 "Ну конечно! Что за глупые вопросы. Вот только я не знаю как правильно себя вести, что говорить..."
        "Я знаю как мыслят парни. Так что, могу помочь советом...":
            jump.help
        "Если будет нужна помощь, обращайся":
            jump.help

    label .help:
        Lisa_00 "Хорошо, Макс, буду иметь в виду. И спасибо, что поболтал со мной. А пока ты не против, если я немного отдохну?"
        Max_00 "Конечно! А я пойду..."
        jump .end

    label .willbeok:
        Lisa_02 "Спасибо, Макс. Приятно слышать, что кому-то не всё равно..."
        Max_04 "Если будет нужна помощь, обращайся"
        jump .help

    label .goodplan:
        Lisa_00 "В общем, если что, я тут."
        Max_00 "Хорошо..."
        jump .end

    label .end:
        $ spent_time = 20
        jump Waiting

    return


label talk_swim:
    $ SetPossStage("Swimsuit", 0)
    menu:
        Lisa_10 "Как... так?"
        "Ну, чего ты в закрытом купальнике лежишь?":
            pass
        "Тебе не жарко в таком купальнике?":
            pass
    menu:
        Lisa_09 "Ну, у меня другого и нет. Ты же знаешь, что наши вещи пропали. Вот там и все мои купальники были..."
        "Очень жаль... Я могу чем-то помочь?":
            menu:
                Lisa_02 "Спасибо. Да, а чем ты можешь помочь, Макс?"
                "Могу как-то решить твою проблему...":
                    jump .findout
                "Я что-нибудь придумаю!":
                    jump .findout

        "Так загорай голая!":
            menu:
                Lisa_01 "Очень смешно, Макс. Что же ты сам так не загораешь?"
                "А давай разденемся вместе!":
                    pass
                "Да легко!":
                    pass
                "Боюсь тебя шокировать..." if flags["morning_erect"] == 0:
                    Lisa_00 "Не поняла. В каком смысле?"
                    Max_00 "Извини, шутки у меня дурацкие... А какой купальник ты хочешь?"
                    jump .want
                "Боюсь тебя снова шокировать..." if flags["morning_erect"] > 0:
                    menu:
                        Lisa_12 "Фу, Макс! Опять твои шуточки... Не надо мне такого счастья. Держи свою штуку там, в штанах..."
                        "Ну, ты сама спросила почему я не раздеваюсь...":
                            menu:
                                Lisa_02 "Извини, не подумала... В общем, другого купальника у меня нет."
                                "А какой ты хочешь?":
                                    jump .want
                                "Я что-нибудь придумаю!":
                                    jump .findout

                        "Точно? А то мне есть что тебе показать...":
                            Lisa_13 "Да, Макс, точно! Я точно уверена, что не хочу это ещё раз видеть. И, вообще, отвали!"
                            Max_00 "Ну, как скажешь..."
                            $ AddRelMood("lisa", 0, -50)
                            jump .end
            menu:
                Lisa_02 "Очень смешно, Макс!"
                "А я и не шучу...":
                    menu:
                        Lisa_00 "И это тоже не смешно. В общем, я тут поваляюсь, если ты не против..."
                        "Извини, шутки у меня дурацкие... А какой купальник ты хочешь?":
                            jump .want
                        "Конечно, одыхай...":
                            $ AddRelMood("lisa", 0, -60)
                            jump .end
                "Ладно. А какой купальник ты хочешь?":
                    jump .want

    label .want:
        Lisa_10 "Ну такой... Максимально открытый. Но не совсем чтобы полностью. И цвет такой красивый, но не чтобы слишком тёмный или холодный... И лямочки такие..."
        Max_09 "Ясно... {i}(или нет){/i}"
        Lisa_02 "В общем, на твоё усмотрение. Только чтобы не хуже, чем этот. Хотя, куда уж хуже..."
        Max_00 "Хорошо, я тебя понял!"
        jump .end

    label .findout:
        Lisa_00 "Например? У тебя же нет денег, ты нигде не работаешь и я что-то сомневаюсь, что ты умеешь шить купальники..."
        Max_04 "Вот увидишь!"
        menu:
            Lisa_02 "Ну, ладно. Посмотрим... Если у меня будет новый купальник, я тебя даже... в щёчку поцелую!"
            "И всё?":
                Lisa_00 "Ну, скажу спасибо..."
                Max_01 "Ладно, идёт!"
            "Договорились!":
                pass
    label .end:
        $ spent_time = 30
        jump Waiting
    return


label about_boy:

    # if ItsTime(cooldown["lisa_boy"]): # кулдаун прошел, можно поговорить
    #     $ del cooldown["lisa_boy"]
    $ talk_var["boy"] = 2

    menu:
        Lisa_00 "Моего парня? Какого? У меня нет никого..."
        "Я про Алекса, ты же сама рассказывала...":
            jump .so
        "Ты уверена? Его вроде Алекс зовут...":
            jump .so
        "И правильно. Рано ещё тебе парней заводить":
            menu:
                Lisa_12 "А ты кто, моя мамочка, чтобы такие советы давать?"
                "Думаю, она со мной согласилась бы":
                    pass
                "Я знаю, что говорю":
                    pass
                "Значит, он твой парень?":
                    jump .so
            menu:
                Lisa_02 "Думаешь, ты такой пришёл, высказал своё мнение и я побежала его бросила?"
                "Ага, так он твой парень?!":
                    jump .so
                "Ну, да...":
                    pass
                "Это было бы правильное решение...":
                    pass
            menu:
                Lisa_03 "Ага, щаз. Даже если бы он и был моим парнем, только потому, что вы все попросите одновременно, я никого не брошу!"
                "Так у нас тут бунтарка!":
                    jump .reason
                "А вот это мне в тебе нравится!":
                    jump .reason
                "Ну и зря. Иногда большинство бывает право...":
                    Lisa_00 "Угу, миллионы мух не могут ошибаться... Ну ты и зануда, Макс! Не хочу больше об этом разговаривать..."
                    Max_00 "Ну и ладно!"
                    jump .end
    menu .so:
        Lisa_02 "Да никакой он мне не парень. Я же говорю, только познакомилась. Просто... он мне понравился."
        "Да расслабься...":
            jump .reason
        "Ладно, ладно, верю!":
            jump .reason

    menu .reason:
        Lisa_02 "Так ты что-то сказать хотел или зачем эту тему поднял?"
        "Я подумал, что тебе нужна моя помощь":
            menu:
                Lisa_00 "Помощь? Мне? В чём? Если мне будет нужна помощь, я попрошу. Нет проблемы, нечего и решать..."
                "Как скажешь...":
                    jump .end
                "Если что, ты знаешь где меня искать":
                    jump .end
        "Хотел дать тебе один совет...":
            menu:
                Lisa_00 "Знаешь что, Макс. Оставь свои советы при себе. Я что-то не в духе. Да и не о чем сейчас разговаривать. Он мне не парень и у меня нет проблем, чтобы их решать!"
                "Хорошо, хорошо...":
                    jump .end
                "Ну, если что, я тут":
                    jump .end
        "Да, забей...":
            jump .end

    label .end:
        $ spent_time = 30
        jump Waiting

    return


label wash_dishes_lisa:
    $ talk_var["lisa_dw"] = 1
    menu:
        Lisa_09 "А что насчёт посуды?"
        "Хочешь, я помогу тебе домыть остальное?":
            menu:
                Lisa_01 "А вот знаешь... хочу! Да, спасибо, Макс!"
                "{i}мыть посуду{/i}":
                    scene BG crockery-evening-00
                    $ renpy.show("Max crockery-evening 01"+max_profile.dress)
                    if GetRelMax("lisa")[0] < 3:
                        $ AddRelMood("lisa", 10, 60)
                    else:
                        $ AddRelMood("lisa", 0, 60)
                    $ dishes_washed = True
                    $ spent_time = max((60 - int(tm[-2:])), 30)
                    $ cur_ratio = 2
                    Max_00 "И чего я этим занимаюсь? Делать нечего, что ли..."
                    menu:
                        Max_00 "А с другой строны - неплохой способ улучшить отношения с Лизой..."
                        "{i}закончить{/i}":
                            jump Waiting
        "Нет, ничего...":
            menu:
                Lisa_12 "Ну раз ничего, то нечего меня отвлекать. Иди делом займись!"
                "Хорошо, пойду займусь":
                    $ spent_time = 10
                    jump Waiting

    return


label about_boy2: # разговор с Лизой после того, как на ужине вся семья узнала про Алекса
    Lisa_00 "Макс, давай сменим тему..."
    Max_11 "Ну Лиза..."
    if talk_var["boy"] == 3: # bad
        menu:
            Lisa_09 "Макс, я тебе рассказала по секрету, а ты меня спалил маме. Не хочу ничего рассказывать больше..."
            "Извини, я забыл, что обещал":
                Lisa_00 "Вот и как тебе что-то рассказывать по секрету, если ты можешь забыть, что это секрет? А?"
            "Извини, но было же весело?":
                Lisa_00 "Нет, Макс, мне не было весело. Нарушать своё слово это совсем совсем не весело!"
            "Извини, я не подумал...":
                Lisa_00 "Не подумал. Я же просила, а ты... Как тебе рассказывать что-то, если ты не думаешь?"
        Max_08 "Извини ещё раз, я не хотел"
    elif talk_var["boy"] == 5: # good
        Lisa_02 "Ну ладно, ладно. Кстати, спасибо, что меня не выдал. Мне нравится, что я могу на тебя положиться."
        Max_04 "Всегда пожалуйста!"
    else: # normal
        menu:
            Lisa_01 "Макс, ты чего такой любопытный? Я же не выпытываю с кем ты встречаешься..."
            "Я ни с кем не встречаюсь. В моей жизни есть только ты!":
                Lisa_12 "Не подлизывайся, Макс! Сознавайся, чего задумал?"
                Max_00 "Да ничего, просто любопытно..."
            "Если бы и был кто-то, ты бы точно свой нос совала!":
                Lisa_03 "Ха! Ты меня хорошо знаешь. Но ты как-то необычайно настойчиво интересуешься..."
                Max_00 "Ну, мне просто любопытно..."

    Lisa_02 "Ну ладно, Макс. Так чего ты хотел узнать?"
    Max_00 "Да всё! Что тебе удалось выяснить?"
    menu:
        Lisa_00 "Об Алексе? Ну, у него есть подружка, оказывается. Самая красивая девочка в школе, говорят..."
        "Они всё врут. Ты - самая красивая!":
            Lisa_01 "Макс, ты такой сегодня... Спасибо за комплимент, но все мальчики без ума от подружки Алекса..."
        "Ты уверена, что она самая красивая?":
            Lisa_10 "Ну, так говорят все мальчики..."
    Max_00 "А ты её сама видела?"
    menu:
        Lisa_02 "Конечно! Мы же в одном классе учимся. Зовут Оливия."
        "Наверное, стерва?":
            menu:
                Lisa_00 "Нет, Макс. Наоборот, она такая хорошая, тихая, скромная, но почему-то всем нравится... Хотя, и правда симпатичная очень..."
                "В твоём вкусе?":
                    Lisa_12 "В смысле? Мне мальчики нравятся, я же говорила уже. Но да, мне она кажется симпатичной..."
                "Странно...":
                    Lisa_02 "Почему странно? Думаешь, мальчикам нравятся только всякие оторвы? Таких полный класс. Именно этим она и выделяется, что не похожа на других"
        "И какая она?":
            menu:
                Lisa_00 "Ну, она такая хорошая, тихая, скромная. И очень симпатичная..."
                "В твоём вкусе?":
                    Lisa_12 "В смысле? Мне мальчики нравятся, я же говорила уже. Но да, мне она кажется симпатичной..."
                "Странно...":
                    Lisa_02 "Почему странно? Думаешь, мальчикам нравятся только всякие оторвы? Таких полный класс. Именно этим она и выделяется, что не похожа на других"
    Max_00 "Понятно..."
    Lisa_00 "А мне вот не понятно что теперь делать... Кажется, у меня нет никаких шансов..."
    Max_08 "Подожди, а он сильно в неё влюблён?"
    menu:
        Lisa_02 "Ну мы не очень много общались, но она ему нравится, это точно. Хотя, я ему тоже нравлюсь, похоже... Чуть-чуть..."
        "Ну вот видишь, не всё потеряно!":
            Lisa_00 "Ну да, не всё. Но около того. Я даже не представляю что мне делать. Он мне так нравится..."
        "Значит, у тебя есть шанс!":
            Lisa_00 "Шанс? Один из миллиона, может быть... Я не знаю как и что мне делать. Он мне так нравится..."
    $ SetPossStage("Schoolmate", 0)
    Max_00 "Ты знаешь, я что-нибудь придумаю, хорошо?"
    Lisa_01 "Хорошо. Спасибо, Макс, что поговорил. Мне это было нужно..."
    Max_04 "Всегда пожалуйста!"
    $ AddRelMood("lisa", 0, 100)
    $ spent_time += 30
    $ talk_var["boy"] = 6
    $ cooldown["lisa_boy"] = CooldownTime("05:00")
    jump Waiting


label Lisa_MorningWood: # Разговор с Лизой после утреннего инцидента
    menu:
        Lisa_00 "Макс, я не хочу об этом говорить!"
        "Да ты послушай!":
            Lisa_09 "Макс, я не хочу. Хватит!"
            Max_14 "Ладно, в другой раз..."
            $ cooldown["talkcooldown"] = CooldownTime("03:00")
            $ AddRelMood("lisa", 0, -50)
            $ spent_time = 10
            jump Waiting
        "Я хотел извиниться...":
            pass
    Lisa_02 "Извиниться? Значит, ты и правда что-то там делал?"
    Max_00 "Нет, я хотел извиниться, что не говорил с тобой об этом раньше."
    Lisa_00 "Не поняла. Какое-то странное извинение. О чём ты со мной раньше не говорил?"
    Max_09 "Ты пробовала с мамой о чём-то... взрослом поговорить?"
    Lisa_09 "А причём тут это? Ну да, она всегда говорит, что я ещё маленькая..."
    Max_01 "Вот именно. Я, как старший брат должен был бы тебя подготовить..."
    Lisa_02 "Постой. Во-первых, ты не старший. Хотя старше, да. А во-вторых, подготовить к чему?"
    Max_04 "Ну вот ты что знаешь о мальчиках?"
    Lisa_03 "Знаю, что если все такие же, как ты, то я стану лесбиянкой!"
    Max_08 "Э..."
    Lisa_02 "Да шучу я. Ну я поняла, к чему ты клонишь. Вот только не уверена, что ты тот, кто должен мне что-то объяснять..."
    Max_07 "А ты знаешь много желающих тебе что-то объяснить?"
    Lisa_09 "Тоже верно... Ну ладно. И к чему весь этот разговор?"
    Max_05 "Я могу помочь тебе стать взрослой."
    Lisa_02 "Ты же понимаешь, как это звучит? Лучше уточни, что ты имеешь в виду..."
    Max_03 "Я поделюсь с тобой знаниями, которые тебе помогут..."
    Lisa_01 "Помогут с чем? Мне мама говорит, что ещё рано о таком думать."
    Max_01 "И что, ты не думаешь об этом?"
    Lisa_10 "Думаю... Но я не знаю. О таком вроде не с мальчиками говорят, особенно с братом..."
    Max_07 "У Алисы свои заботы, а мама тебе уже всё сказала..."
    Lisa_00 "Ну, я подумаю. Ты как-то слишком настойчиво помощь предлагаешь. Как будто у тебя свой интерес какой-то..."
    Max_04 "Хочу только помочь младшей сестрёнке."
    Lisa_02 "Ну да, ну да... В общем, я подумаю. Только вот не уверена, что ты всё-таки подходишь на роль такого... наставника, если ты меня понимаешь..."
    Max_09 "Что, моё мнение недостаточно авторитетно для тебя?"
    Lisa_01 "Ну не знаю. Посмотрим..."
    Max_01 "Посмотрим..."

    $ SetPossStage("seduction", 1)
    $ spent_time = 30
    jump Waiting
