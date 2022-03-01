
label AnnTalkStart:

    $ dial = TalkMenuItems()

    $ __cur_plan = ann.get_plan()
    if __cur_plan.talklabel is not None:
        call expression __cur_plan.talklabel from _call_expression_7

    if len(dial) > 0:
        $ dial.append((_("{i}уйти{/i}"), "exit"))
    else:
        jump Waiting

    $ renpy.block_rollback()

    if flags.eric_wallet == 2:
        if not ann.flags.talkblock:
            jump ann_about_wallet
        else:
            menu:
                Ann_17 "Уйди, Макс. Нам не о чем говорить, пока ты не вернёшь Эрику деньги и не извинишься перед ним и всеми нами!"
                "{i}уйти{/i}":
                    $ alice.hourly.talkblock = 1
                    jump AfterWaiting

    Ann_00 "Что-то случилось, дорогой?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        $ __mood = ann.GetMood()[0]
        if rez in gifts['ann']:
            if renpy.has_label(rez.label):
                call expression rez.label from _call_expression_8
        elif __mood < talks[rez].mood:
            if __mood < -2: # Настроение -4... -3, т.е. всё ну совсем плохо
                jump Ann_badbadmood
            elif __mood < 0: # Настроение -2... -1, т.е. всё ещё всё очень плохо
                jump Ann_badmood
            else: # Настроение хорошее, но ещё недостаточное для разговора
                jump Ann_normalmood
        elif talks[rez].kd_id != "" and talks[rez].kd_id in cooldown and not ItsTime(cooldown[talks[rez].kd_id]):
            jump Ann_cooldown
        elif renpy.has_label(talks[rez].label): # если такая метка сушествует, запускаем ее
            call expression talks[rez].label from _call_expression_9
        jump AnnTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label Ann_badbadmood:
    menu:
        Ann_18 "Макс, я сейчас в очень плохом настроении и не хочу с тобой разговаривать!"
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Ann_asksorry


label Ann_badmood:
    menu:
        Ann_18 "Макс, я сейчас не в настроении и не хочу разговаривать."
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Ann_asksorry


label Ann_asksorry:
    menu:
        Ann_01 "Да? Я тебя слушаю?"
        "В другой раз...":
            jump Waiting


label Ann_normalmood:
    menu:
        Ann_18 "Макс, не сейчас, хорошо?"
        "Ок...":
            jump Waiting


label Ann_cooldown:
    Ann_18 "Макс, давай сменим тему..."
    Max_00 "Ок, мам..."
    jump AfterWaiting


label ann_ask_money:

    if ann.plan_name is None:
        "При нормальном развитии событий эта строка не должна была появится. Сообщите разработчику."
        return
    if ann.plan_name == 'yoga': ## Анна занимается йогой
         menu:
            Ann_05 "Макс, ты же видишь, я сейчас занята... Выбери более подходящий момент, пожалуйста..."
            "Точно, извини...":
                jump AfterWaiting
    elif ann.plan_name in ['swim', 'sun', 'tv']: ## Анна загорает, плавает или смотрит ТВ
         menu:
            Ann_05 "Очень смешно, Макс. Ты видишь у меня карманы? Нет? Выбери более подходящий момент, пожалуйста..."
            "Точно, извини...":
                jump AfterWaiting

    $ ann.daily.ask_money = 1
    $ spent_time = 10
    menu:
        Ann_00 "Макс, тебе не стыдно просить деньги у мамы, хотя сам целыми днями дома сидишь и ничего не делаешь?"
        "Мне стыдно, но очень нужны деньги...":
            $ mgg.ask(1)
            menu:
                Ann_04 "Ладно, держи. И найди себе уже работу, хотя бы через интернет. Нам лишние деньги не помешают..."
                "Ага! Спасибо, мам!":
                    jump AfterWaiting
                "Может быть, я могу что-то сделать?":
                    pass
        "Я могу сделать какую-то работу, чтобы не просто так выпрашивать деньги...":
            pass
        "Ты права, стыдно. В другой раз...":
            jump AfterWaiting

    menu .work:
        Ann_01 "И что же, например?"
        "Может быть, почистить бассейн?" if dcv.clearpool.done and dcv.clearpool.stage in [0, 2]:
            $ dcv.clearpool.stage = 1
            $ mgg.ask(2)
            menu:
                Ann_04 "Отличная идея, Макс! Лучше уж я заплачу тебе $40, чем нанимать какого-то человека. Держи. Да, лучше это делать пока светло и никого нет."
                "Конечно!":
                    jump AfterWaiting
                "Может я могу ещё что-то сделать?":
                    jump .work
        "Ну, могу заказать продукты" if dcv.buyfood.done and dcv.buyfood.stage in [0, 2]:
            $ dcv.buyfood.stage = 1
            $ mgg.ask(3)
            menu:
                Ann_04 "Хорошая мысль, Макс. Я дам тебе $50 на продукты и авансом $10 за твои услуги, так сказать. Устроит?"
                "Конечно!":
                    jump AfterWaiting
                "Может я могу ещё что-то сделать?":
                    jump .work
        "Не знаю. Видимо, ничего...":
            jump AfterWaiting


label ann_aboutfood:
    menu:
        Ann_05 "Спасибо, Макс. Продукты я или Алиса заберём, когда привезут. Об этом не беспокойся."
        "Супер!":
            pass
    $ AddRelMood('ann', 0, 50)
    if flags.about_earn:
        $ dcv.buyfood.stage = 3
    else:
        $ dcv.buyfood.stage = 0
    return


label ann_aboutpool:
    menu:
        Ann_05 "Спасибо, Макс, на недельку этого должно хватить."
        "Ага...":
            pass
    $ AddRelMood('ann', 0, 50)
    if flags.about_earn:
        $ dcv.clearpool.stage = 3
    else:
        $ dcv.clearpool.stage = 0
    return


label ann_talk_tv:
    $ ann.daily.tvwatch = 1
    if not ann.flags.erofilms:
        jump .first_movie

    menu:
        Ann_00 "Да так, всё подряд. Садись рядом, если хочешь..."
        "Конечно! Что смотреть будем?":
            $ SetCamsGrow(house[4], 140)
            # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(01/02/03)
            scene BG lounge-tv-01
            $ renpy.show("Ann tv-closer "+pose3_3)
            $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
            Ann_05 "Да вот, по кабельному какой-то фильм сейчас начнётся... Да и сериалов полно..."

            if poss['mom-tv'].st() == 7:
                jump ann_tv_casual_1
            elif poss['mom-tv'].st() > 7:
                jump ann_tv_casual_r

            jump ann_tv_casual_0

        "А я прикупил фильм на вечер. Посмотрим?" if all([items['erofilm2'].have, ann.dcv.feature.stage==5]):
            $ ann.dcv.feature.stage = 6
            jump erofilm2_1
        "Мы не досмотрели один фильм. Помнишь?" if all([items['erofilm2'].have, ann.dcv.feature.stage==6]):
            $ ann.dcv.feature.stage = 7
            jump erofilm2_2
        "В другой раз...":
            menu:
                Ann_05 "Как хочешь, дорогой. А я что-нибудь посмотрю..."
                "Не буду тебе мешать...":
                    pass
    jump Waiting

    label .first_movie:
        if _in_replay:
            call ann_tv_closer from _call_ann_tv_closer
        ## "Что смотришь?"
        menu:
            Ann_01 "Да так, всякую ерунду. Хотела какой-нибудь фильм посмотреть. Садись рядом, если тоже делать нечего..."
            "Конечно! Что смотреть будем?":
                $ ann.flags.erofilms = 1
                $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
            "В другой раз..." if not _in_replay:
                Ann_05 "Ну, как хочешь!"
                Max_01 "Не буду тебе мешать..."
                jump Waiting
    menu:
        Ann_04 "Я не знаю. Мне вот подруга посоветовала фильм с Томом Крузом и Николь Кидман, называется \"С широко закрытыми глазами\". Смотрел?"
        "Нет, не слышал о таком. Давай смотреть!":
            menu:
                Ann_05 "Отлично! Вот сейчас и посмотрим, что там подруга насоветовала..."
                "{i}начать просмотр{/i}":
                    jump .start
        "Да, слышал кое-что о нём...":
            menu:
                Ann_02 "Да? И что ты о нём слышал? Хороший фильм? Стоит смотреть?"
                "Да, отзывы отличные":
                    menu:
                        Ann_05 "Ну, раз отзывы хорошие, тогда, давай смотреть!"
                        "{i}начать просмотр{/i}":
                            jump .start

    label .start:
        scene BG tv-watch-01
        show tv ews 01 at tv_screen
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)
    Max_01 "{m}Интересно, мама хотя бы подозревает, что это эротика?... Посмотрим...{/m}"
    show tv ews 02 at tv_screen
    Ann_13 "Ой, кажется, я не посмотрела какой возрастной рейтинг у фильма..."
    Max_04 "Да всё в порядке!"
    show tv ews 03 at tv_screen
    Ann_14 "Да уж... В порядке. Ну, если ты стесняешься, можешь закрыть глаза..."
    Max_02 "Я уже взрослый! И не такое видел!"
    show tv ews 04 at tv_screen
    Ann_04 "Да ты что? И где, интересно мне знать? Я когда подключала интернет, выбрала самый безопасный вариант, чтобы оградить вас от такого... Так где ты что там видел?"
    Max_03 "Да это не важно. В любом случае, это же популярный фильм с известными актёрами, что тут такого может быть..."
    show tv ews 05 at tv_screen
    Ann_13 "Да, ты прав. Действительно, что... Макс! Чем дальше, тем больше я уверена, что этот фильм не для тебя..."
    Max_02 "Ну сама подумай, стали бы Том Круз и Николь Кидман сниматься в эротике?"
    show tv ews 06 at tv_screen
    menu:
        Ann_15 "Надеюсь, ты закрыл глаза, потому-что это уже слишком!"
        "Я не смотрю, а что там?":
            pass
        "Я уже взрослый!":
            pass
    show tv ews 07 at tv_screen
    Ann_14 "Я уже десять раз пожалела, что выбрала этот фильм. Подруге ещё нужно будет сказать \"спасибо\" за то, что не предупредила..."
    Max_07 "Ты до 30 лет будешь меня оберегать от такого?"
    show tv ews 08 at tv_screen
    Ann_02 "Ты знаешь, может быть... Но да, ты прав. Фильм и правда хороший оказался. Хотя и не для детей, однозначно..."
    Max_04 "Мне тоже понравилось!"
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer "+pose3_3)
    $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
    Ann_05 "Жаль, что мы редко с тобой вместе вот так сидим, что-то смотрим. Ну, надеюсь, начало традиции положено. И пусть в следующий раз будет нечто менее... волнующее..."
    Max_01 "Конечно, мам!"
    $ renpy.end_replay()
    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ AddRelMood('ann', 10, 100)
    $ SetCamsGrow(house[4], 180)
    $ poss['mom-tv'].open(0)
    jump Waiting

label ann_tv_casual_0:
    $ renpy.dynamic('mood', 'ch')

    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_01 + tv-watch-01-ann-01 + tv-watch-01-max-(01/01a/01b)
    scene BG tv-watch-01
    $ renpy.show('tv serial 0'+str(renpy.random.randint(1, 7))+'-01', at_list=[tv_screen,]) # tv_screen
    show Ann tv-watch 01
    $ renpy.show('Max tv-watch 01'+mgg.dress)
    Max_02 "{m}Мама так близко... В одном полотенце... Даже не знаю о чём сериал, о нём я думать точно не могу...{/m}"

    if mgg.dress == 'a':
        # tv-mass-05 + tv-ero-01-max-02 + tv-ero-01-ann-(04/05/06)
        scene BG tv-mass-05
        show Max tv-ero 02a
        $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))

        Max_08 "{m}Вот чёрт! Зря я представлял, что там у мамы под полотенцем... В джинсах стало прям очень тесно, член стоит как памятник! Хорошо, что мама из-за моей одежды это не увидит...{/m}"
        if poss['mom-tv'].st() < 1:
            $ poss['mom-tv'].open(1)
    elif mgg.dress == 'b':
        if poss['mom-tv'].st() < 6:
            #(может спалиться 25%) с каждым последующим просмотром ТВ с Анной % будет увеличиваться на 25
            $ ch = 25 + 25 * ann.flags.incident
            $ ann.flags.incident += 1
        else:
            # после того, как Анна заметит стояк - будет стабильно 40%
            $ ch = 40

        menu:
            Max_08 "{m}Вот чёрт! Зря я представлял, что там у мамы под полотенцем... Если мама увидит мой стояк, то просмотр для меня точно закончится. Хотя, на мне майка... Может она и не заметит, но не факт.{/m}"
            "сидеть и надеяться на лучшее":
                if not random_outcome(ch):
                    if poss['mom-tv'].st() < 2:
                        $ poss['mom-tv'].open(2)
                else:
                    # (Не повезло!)
                    # tv-kiss-03 + tv-ero-00-max-01a + tv-ero-00-ann-01
                    scene BG tv-kiss-03
                    show Max tv-ero 00-01b
                    show Ann tv-ero 00-01

                    Ann_15 "[unlucky!t]Макс! Это мне кажется или у тебя... Я не поняла! Ты почему такой возбуждённый? Я конечно всё понимаю, ты подросток и такое бывает, но сейчас-то в честь чего?"
                    Max_10 "Я не знаю! Оно само, как-то..."
                    Ann_18 "Как же, само... Давай прикрывайся, бессовестный, и беги к себе в комнату, пока не наказала. И Лизу не вздумай напугать своей возбуждённостью!"
                    menu:
                        Max_14 "Хорощо, мам. Извини за это."
                        "{i}уйти{/i}":
                            $ poss['mom-tv'].open(6)
                            jump .end
    elif mgg.dress == 'c':
        #если Макс только в шортах
        if poss['mom-tv'].st() < 4:
            #(может спалиться 50%), с каждым последующим просмотром ТВ с Анной % будет увеличиваться на 25
            $ ch = 50 + 25 * ann.flags.incident
            $ ann.flags.incident += 1
        else:
            # после того, как Анна заметит стояк - будет стабильно 70%
            $ ch = 70

        # tv-mass-05 + tv-ero-01-max-02b + tv-ero-01-ann-(04/05/06)
        scene BG tv-mass-05
        show Max tv-ero 02c
        $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))

        menu:
            Max_08 "{m}Вот чёрт! Зря я представлял, что там у мамы под полотенцем... Если мама увидит мой стояк, то просмотр для меня точно закончится. В этих шортах я точно свой член сейчас не спрячу! Может, конечно, она и не заметит, но вряд ли.{/m}"
            "сидеть и надеяться на лучшее":
                if not random_outcome(ch):
                    if poss['mom-tv'].st() < 3:
                        $ poss['mom-tv'].open(3)
                else:
                    # (Не повезло!)
                    # tv-kiss-03 + tv-ero-00-max-01b + tv-ero-00-ann-01
                    scene BG tv-kiss-03
                    show Max tv-ero 00-01c
                    show Ann tv-ero 00-01

                    if poss['mom-tv'].st() < 4:
                        if items['max-a'].have:
                            $ poss['mom-tv'].open(4)
                        else:
                            $ poss['mom-tv'].open(5)

                    Ann_15 "[unlucky!t]Макс! Это что такое?! Я не поняла! Ты почему такой возбуждённый? Я конечно всё понимаю, ты подросток и такое бывает, но сейчас-то в честь чего?"
                    Max_10 "Я не знаю! Оно само, как-то..."
                    Ann_18 "Как же, само... Давай прикрывайся, бессовестный, и беги к себе в комнату, пока не наказала. И Лизу не вздумай напугать своей возбуждённостью!"
                    menu:
                        Max_14 "Хорощо, мам. Извини за это."
                        "{i}уйти{/i}":
                            jump.end

    # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(01/02/03)
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer "+pose3_3)
    $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
    if mgg.dress == 'a':
        Ann_05 "Ну что, отличный сериал, как мне кажется! А тебе понравилось, Макс?" nointeract
    else:
        Ann_05 "[lucky!t]Ну что, отличный сериал, как мне кажется! А тебе понравилось, Макс?" nointeract

    menu:
        "Да, очень!":
            $ mood = 50
            Ann_07 "Ну я рада. Ладно, спасибо что посидел со мной. Пойду в свою комнату, хватит глаза портить на сегодня..."
            Max_04 "Ага, давай..."
        "Почти также, как сидеть рядом с тобой...":
            $ mood = 40
            Ann_12 "Что, прости? Не поняла..."
            Max_00 "Не бери в голову, это я так, пошутил неудачно..."
            Ann_05 "Ясно. Ну, спасибо за компанию. Пойду в свою комнату, хватит глаза портить на сегодня..."
            Max_03 "Ага, хорошо посидели..."

    label .end:
        $ spent_time = max((60 - int(tm[-2:])), 40)
        $ AddRelMood('ann', 0, mood)
        $ cur_ratio = 0.5
        jump Waiting

label ann_tv_casual_1:
    $ renpy.dynamic('film')
    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_01 + tv-watch-01-ann-01 + tv-watch-01-max-(01/01a/01b)
    scene BG tv-watch-01
    $ film = '0' + str(renpy.random.randint(1, 7))
    $ renpy.show('tv serial '+film+'-01', at_list=[tv_screen,]) # tv_screen
    show Ann tv-watch 01
    $ renpy.show('Max tv-watch 01'+mgg.dress)
    Max_02 "{m}Мама так близко... В одном полотенце... Какая разница, что там на экране происходит, когда рядом ТАКАЯ женщина! Не могу перестать представлять то, что скрыто под её полотенцем...{/m}"

    # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
    scene BG tv-mass-03
    $ renpy.show('Max tv-ero 01'+mgg.dress)
    $ renpy.show('Ann tv-ero 01-'+pose3_3)
    show screen Cookies_Button

    if mgg.dress == 'b':
        # Макс в майке и шортах
        Max_08 "{m}Зря я это представил... Если мама увидит мой стояк, то просмотр для меня точно закончится. Хотя, на мне майка... Может она и не заметит, но не факт.{/m}" nointeract
    else:
        # Макс только в шортах
        Max_08 "{m}Зря я это представил... Если мама увидит мой стояк, то просмотр для меня точно закончится. В этих шортах я точно свой член сейчас не спрячу! Может, конечно, она и не заметит, но вряд ли.{/m}" nointeract

    menu:
        "{i}перестраховаться (массаж){/i}":
            Max_07 "Мам, а зачем без дела, сидеть и смотреть в экран... Хочешь, я тебе массаж сделаю?"
    Ann_02 "Я слышала от твоих сестёр, что ты начал этим увлекаться и делаешь успехи... Неужели этому можно научиться на интернет-курсах?"

    hide screen Cookies_Button
    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_02 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    scene BG tv-watch-01
    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,]) # tv_screen
    show Ann tv-watch 01
    $ renpy.show('Max tv-watch 01'+mgg.dress)
    Max_04 "Если руки не кривые, то можно! И это ведь не лечебный массаж, а скорее лёгкий и поверхностный. Но расслабляет хорошо. Тебе такое точно не помешало бы..."

    # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
    scene BG tv-mass-05
    $ renpy.show('Max tv-ero 02'+mgg.dress)
    $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))

    Ann_04 "Верно, Алиса говорила, что у тебя талант... Ладно, давай посмотрим, на что ты способен... Помассируешь мне плечи?"
    Max_01 "Конечно, мам!"

    # tv-mass-05 + tv-ero-02-max-(01a/01b)-ann-01
    scene BG tv-mass-05
    $ renpy.show('Ann tv-ero 02-01'+mgg.dress)
    Ann_05 "Ого, Макс... Алиса была права. Ты делаешь это и правда очень хорошо..."
    Max_03 "Спасибо!"

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
    scene BG char Kira after-club-s08a-f
    $ renpy.show('Max tv-ero 03-01'+mgg.dress)
    show Ann tv-ero 03-01

    Ann_06 "Это здорово, Макс! Я очень рада, что ты умеешь кое-что, что в жизни может пригодится. Конечно, работа массажистом это не то, о чём я думаю, ты мечтаешь, но..."
    Max_04 "Это просто хобби... И для своих, мне в радость этим заниматься."

    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_03 + tv-watch-01-max&ann-(01a/01b)
    scene BG tv-watch-01
    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,]) # tv_screen
    $ renpy.show('Max tv-watch ann-01'+mgg.dress)

    Ann_08 "Ну, бывает так, что хобби становится работой... Кажется, я и правда хорошо расслабилась, как будто поспала несколько часов... Я буду рада, если ты будешь делать мне такой массаж иногда..."
    Max_01 "С удовольствием, мам!"

    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ AddRelMood('ann', 10, 50)
    $ cur_ratio = 0.5
    $ poss['mom-tv'].open(8)
    $ ann.flags.handmass = True
    jump Waiting

label ann_tv_casual_r:
    $ renpy.dynamic('film')
    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_01 + tv-watch-01-ann-01 + tv-watch-01-max-(01/01a/01b)
    scene BG tv-watch-01
    $ film = '0' + str(renpy.random.randint(1, 7))
    $ renpy.show('tv serial '+film+'-01', at_list=[tv_screen,]) # tv_screen
    show Ann tv-watch 01
    $ renpy.show('Max tv-watch 01'+mgg.dress)

    Max_02 "{m}Мама так близко... В одном полотенце... Какая разница, что там на экране происходит, когда рядом ТАКАЯ женщина! Не могу перестать представлять то, что скрыто под её полотенцем...{/m}"

    # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
    scene BG tv-mass-03
    $ renpy.show('Max tv-ero 01'+mgg.dress)
    $ renpy.show('Ann tv-ero 01-'+pose3_3)
    show screen Cookies_Button

    menu:
        Max_08 "{m}Зря я это представил... Надеюсь, она не заметит, что у меня стоит... Но не факт, может стоит подстраховаться и предложить ей массаж?{/m}"
        "Мам, хочешь массаж?":
            hide screen Cookies_Button
            if ann.flags.handmass:
                # предыдущий массаж был успешным
                # tv-mass-07 + tv-ero-01-max-(03a/03b) + tv-ero-01-ann-(07/08/09)
                scene BG tv-mass-07
                $ renpy.show('Max tv-ero 03'+mgg.dress)
                $ renpy.show('Ann tv-ero 01-0'+str(6+int(pose3_3)))
                Ann_04 "Ой, я думала, ты и не предложишь. В прошлый раз ты так хорошо мне плечи и шею помассировал, что я буду очень рада, если ты это повторишь..."
                Max_04 "С удовольствием, мам!"
            else:
                # предыдущий массаж не был успешным
                # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
                scene BG tv-mass-05
                $ renpy.show('Max tv-ero 02'+mgg.dress)
                $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
                Ann_02 "Ой, я думала, ты и не предложишь. Надеюсь, сегодня ты отнесёшься к массажу с большим вниманием, чем в прошлый раз?"
                Max_01 "Да, мам, я постараюсь..."

    # tv-mass-05 + tv-ero-02-max-(01a/01b)-ann-01
    scene BG tv-mass-05
    $ renpy.show('Ann tv-ero 02-01'+mgg.dress)
    Ann_05 "Ой, Макс! Как же чудесно... Как хорошо, что ты у меня есть... Твои руки просто нереально расслабляют!"
    Max_03 "Спасибо! Я рад, что тебе нравится."

    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_02 + tv-watch-01-max&ann-(01a/01b)
    scene BG tv-watch-01
    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,]) # tv_screen
    $ renpy.show('Max tv-watch ann-01'+mgg.dress)
    Ann_08 "У тебя это очень хорошо получается... Такая лёгкость наступает. С таким талантом ты можешь много достичь в этом деле!"
    menu:
        Max_02 "Очень надеюсь, что так и будет."
        "{i}продолжать массаж{/i}" ('mass', mgg.massage) if not ann.flags.showdown_e:
            if rand_result:
                # (Маме понравился массаж!)
                # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
                scene BG char Kira after-club-s08a-f
                $ renpy.show('Max tv-ero 03-01'+mgg.dress)
                show Ann tv-ero 03-01
                Max_06 "[ann_good_mass!t]{m}Неплохой у меня вид открывается! Под полотенцем слегка виднеются её аппетитные сосочки... Это возбуждает ещё сильнее. Вот бы её полотенце начало сползать... Возможно, она бы даже не сразу это поняла, особенно, если ей очень понравился массаж.{/m}"

                # tv-ero-04 + tv-ero-04-max-(01a/01b)-ann-01 + tv-ero-04-ann-01a
                scene BG tv-ero-04
                $ renpy.show('Max tv-ero 04-01'+mgg.dress)
                show Ann tv-ero 04-01

                Ann_07 "Ой, Макс! Это чудесно... Такая лёгкость. Ты знаешь как сделать приятно. Мне очень понравилось... Обязательно буду ждать следующего раза!"
                Max_01 "Класс! Я тоже буду ждать, мам. Отдыхай."
                $ ann.flags.m_shoulder += 1
                $ ann.flags.handmass = True
                $ AddRelMood('ann', 5, 30)
            else:
                # (Маме не понравился массаж!)
                # tv-watch-01 + serial_(01/02/03/04/05/06/07)_03 + tv-watch-01-max&ann-(01a/01b)
                scene BG tv-watch-01
                $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,]) # tv_screen
                $ renpy.show('Max tv-watch ann-01'+mgg.dress)
                Ann_14 "[ann_bad_mass!t]Ой, Макс... Нет, теперь уже не так хорошо... Что-то даже мышцам немного больно стало. Давай в другой раз продолжим... Но всё равно, спасибо!"
                Max_10 "Извини. Наверно, на сериал засмотрелся... Я пойду."
                $ ann.flags.handmass = False
        "{i}продолжать массаж{/i}" if get_rel_eric()[0] < 0 and ann.flags.showdown_e:
            # вражда, Эрик изгнан, состоялся первый разговор на балконе
            jump ann_tv_continuation_massage
        "{i}продолжать массаж{/i}" if all([get_rel_eric()[0] == 2, flags.voy_stage == 8, poss['control'].used(10)]):
            jump ann_tv_continuation_massage

    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ cur_ratio = 0.5
    jump Waiting

label ann_tv_continuation_massage:
    $ renpy.dynamic('film')
    $ film = '0' + str(renpy.random.randint(1, 7))
    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
    scene BG char Kira after-club-s08a-f
    $ renpy.show('Max tv-ero 03-01'+mgg.dress)
    show Ann tv-ero 03-01
    Max_06 "{m}Неплохой у меня вид открывается! Под полотенцем слегка виднеются её аппетитные сосочки... Это возбуждает ещё сильнее. Вот бы её полотенце начало сползать... Возможно, она бы даже не сразу это поняла, особенно, если ей очень понравился массаж.{/m}"
    # tv-ero-04 + tv-ero-04-max-(01a/01b)-ann-01 + tv-ero-04-ann-01a
    scene BG tv-ero-04
    $ renpy.show('Max tv-ero 04-01'+mgg.dress)
    show Ann tv-ero 04-01
    Ann_07 "Ой, Макс! Это чудесно... Ты знаешь как сделать приятно. Мне очень понравилось... Ты большой молодец у меня!" nointeract
    menu:
        "Массаж спины?" if _in_replay or not any([poss['mom-tv'].used(13), poss['mom-tv'].used(14)]):
            # 1-ый массаж спины Анны
            Ann_05 "Обожаю массаж спины... Не знаю, хватит ли у тебя для этого силы, но давай попробуем. Может у тебя уже было достаточно практики и ты со мной справишься..."
            Max_04 "Ты не пожалеешь!"
            # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
            scene BG after-club-s04-f
            $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
            Ann_14 "Ох, даже не знаю, как лучше развернуть это полотенце, чтобы ты мог до моей спины спокойно добраться. Ты лучше глаза закрой, а то мало ли у меня не получится..."
            Max_02 "{m}Как же здорово будет, если не получится! У меня только от одних мыслей об этом член стоит, как гора, а уж если она что-нибудь засветит...{/m}"
            # tv-kiss-03 + tv-ero-06-max-(01a/01b)-ann-01
            scene BG tv-kiss-03
            $ renpy.show('Ann tv-ero 06-01'+mgg.dress)
            Ann_02 "Вот так, мне кажется, будет нормально... Только хочу тебя сразу предупредить, я совсем голая под полотенцем. Я там не сильно... открыта?"
            Max_03 "Нет. Открыто именно то, что мне надо!" nointeract
            jump .massage
        "Полотенце приспустишь?" if not _in_replay and any([poss['mom-tv'].used(13), poss['mom-tv'].used(14)]):   #периодический массаж спины
            Ann_05 "Конечно! Когда дело доходит до моей спины, я очень требовательна, сынок, потому что обожаю это. Надеюсь, ты справишься."
            Max_04 "Ты не пожалеешь!"
            # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
            scene BG after-club-s04-f
            $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
            Ann_14 "Ох, даже не знаю, как лучше развернуть это полотенце, чтобы ты мог до моей спины спокойно добраться. Ты лучше глаза закрой, а то мало ли у меня не получится..."
            Max_02 "{m}Как же здорово будет, если не получится! У меня только от одних мыслей об этом член стоит, как гора, а уж если она что-нибудь засветит...{/m}"
            # tv-kiss-03 + tv-ero-06-max-(01a/01b)-ann-01
            scene BG tv-kiss-03
            $ renpy.show('Ann tv-ero 06-01'+mgg.dress)
            Ann_02 "Вот так, мне кажется, будет нормально... Только хочу тебя сразу предупредить, я совсем голая под полотенцем. Я там не сильно... открыта?"
            Max_03 "Нет. Открыто именно то, что мне надо!" nointeract
            jump .massage
        "{i}закончить массаж{/i}" if not _in_replay:
            Max_01 "Спасибо за похвалу! Жду не дождусь следующего раза, мам. Отдыхай." nointeract
            jump .end

    menu .massage:
        "{i}массировать маме спину{/i}" ('mass', mgg.massage): #(навык массажа)
            if rand_result:
                # (Маме понравился массаж!)
                # tv-mass-07 + tv-ero-06-max-(02a/02b)-ann-02
                scene BG tv-mass-07
                $ renpy.show('Ann tv-ero 06-02'+mgg.dress)
                Ann_03 "[ann_good_mass!t]Да, Макс... Твои руки приносят мне огромное удовольствие. В смысле, у тебя получается очень хорошо... Как будто сходила к профессионалу..."
                Max_06 "{m}Вау... Какая у неё шикарная и почти голая попка! Блин, как же хочется прижаться к ней членом, прямо по серединке, и тереться... Но лучше не отвлекаться, а то запросто можно массаж запороть!{/m}" nointeract
                menu:
                    "{i}продолжить массаж{/i}" ('mass', mgg.massage): #(навык массажа)
                        if rand_result:
                            # (Маме понравился массаж!)
                            # tv-ero-07 + tv-ero-07-max-(01a/01b)-ann-01
                            scene BG char Ann tv-ero-07
                            $ renpy.show('Ann tv-ero 07-01'+mgg.dress)
                            Ann_09 "[ann_good_mass!t]Ох, как здорово, сынок... Такие нежные, но сильные руки у тебя! Но они уже опустились так низко, а я не чувствую по полотенцу, что оно тебе хоть как-то мешает. Оно там не сползло слишком низко?" nointeract
                            menu:
                                "Нет, мам. Не переживай." ('soc', mgg.social, 90): #(убеждение)
                                    if rand_result:
                                        # (Убеждение удалось!)
                                        Ann_08 "[succes!t]Фух... А то я сижу, наслаждаюсь массажем и про всё остальное забыла. Такая лёгкость. Мне очень понравилось!" nointeract
                                        menu:
                                            "{i}закончить массаж{/i}":
                                                $ ann.flags.m_back += 1
                                        # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
                                        scene BG after-club-s04-f
                                        $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
                                        Ann_07 "Я обязательно буду ждать следующего раза, сынок!"
                                        Max_01 "Класс! Я тоже буду ждать, мам. Отдыхай." nointeract
                                    else:
                                        # (Убеждение не удалось!)
                                        # after-club-s05-f + tv-ero-00-ann-02 + tv-ero-00-max-(02a/02b)
                                        scene BG char Kira after-club-s05-f
                                        show Ann tv-ero 00-02
                                        $ renpy.show('Max tv-ero 00-02'+mgg.dress)
                                        Ann_17 "[failed!t]Обманщик ты, Макс! Это что такое?! Как тебе не стыдно! У тебя встал на собственную маму! Что у тебя в голове творится... Почему ты не сказал, что я тут голая сижу?"
                                        Max_07 "Просто засмотрелся на тебя по ходу дела. А не сказал, потому что хотел массаж закончить. Хорошо же получилось?"
                                        Ann_12 "Получилось-то хорошо, вот только... не должно так быть..."
                                        Max_10 "Ну мам, ты же красивая! Вот я и это... возбудился... слегка..."
                                        Ann_13 "Ничего себе, слегка! Так, ладно, представим, что ничего не было. Иди куда-нибудь, развейся..." nointeract
                                "Есть немного...":
                                    # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
                                    scene BG after-club-s04-f
                                    $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
                                    Ann_15 "Ничего себе! Ты почему сидишь и молчишь об этом, а, Макс?! Я же предупредила, что голая под ним..."
                                    Max_07 "Так оно под самый конец только сползло, а я хотел массаж закончить. Хорошо же получилось?"
                                    # tv-watch-01 + serial_(01/02/03/04/05/06/07)_03 + tv-watch-01-max&ann-(01a/01b)
                                    scene BG tv-watch-01
                                    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,]) # tv_screen
                                    $ renpy.show('Max tv-watch ann-01'+mgg.dress)
                                    Ann_14 "Очень! Но в следующий раз, лучше не молчи об этом... Хорошо?"
                                    Max_11 "Ладно, скажу."
                                    Ann_07 "А за массаж огромное тебе спасибо, мне очень понравилось! Обязательно буду ждать следующего раза!"
                                    Max_01 "Класс! Я тоже буду ждать, мам. Отдыхай." nointeract
                            $ ann.flags.handmass = True
                            jump .end
                        else:
                            jump .bad_massage
            else:
                jump .bad_massage
    label .bad_massage:
        # (Маме не понравился массаж!)
        # tv-watch-01 + serial_(01/02/03/04/05/06/07)_03 + tv-watch-01-max&ann-(01a/01b)
        scene BG tv-watch-01
        $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,]) # tv_screen
        $ renpy.show('Max tv-watch ann-01'+mgg.dress)
        Ann_14 "[ann_bad_mass!t]Ой, нет, Макс... Твой хвалёный массаж не так хорош, как ты рекламировал... Думаю, надо прекратить. Давай в другой раз продолжим... Но всё равно, спасибо!"
        $ ann.flags.handmass = False
        Max_10 "Извини. Наверно, на сериал засмотрелся... В следующий раз я буду лучше стараться." nointeract

    menu .end:
        "{i}уйти{/i}":
            $ renpy.end_replay()
    if not any([poss['mom-tv'].used(13), poss['mom-tv'].used(14)]):
        if get_rel_eric()[0] == 2:      # первый массаж спины Фальшивая дружба
            $ poss['mom-tv'].open(13)
        else:   # if get_rel_eric()[0] < 0:
            $ poss['mom-tv'].open(14)   # первый массаж спины Откровенная вражда

    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ cur_ratio = 0.5
    jump Waiting


label Ann_MorningWood:
    Ann_01 "Макс, не переживай ты так. Я всё прекрасно понимаю, у мальчиков это бывает..."
    Max_04 "Я рад, что ты понимаешь"
    menu:
        Ann_14 "Но Макс. Лиза ещё маленькая и постарайся, чтобы она не видела твой... тебя. В общем, ты меня понял, да?"
        "А что такого?":
            menu:
                Ann_04 "Что такого? Да то, что девочка не должна видеть здоровенный член своего брата, когда просыпается утром!"
                "Ого, мам...":
                    menu:
                        Ann_07 "Извини, что-то меня занесло. Просто, даже я в шоке была, когда увидела, а что уж говорить про Лизу..."
                        "Значит, тебе понравилось?":
                            Ann_12 "Макс! Я конечно рада, что ты у меня уже такой... большой... Но вообще, я всё сказала. Постарайся ей не показываться в таком виде, ладно?"
                            Max_00 "Ладно, мам..."
                        "Ладно, я всё понял...":
                            pass
                "Разве это должно пугать?":
                    menu:
                        Ann_12 "Ну, взрослую женщину это даже притягивает, но девочке явно рано на такое смотреть, ты меня понял?"
                        "Взрослую женщину притягивает?":
                            Ann_05 "Ну, Макс! Я же не это имела в виду... В общем, этот разговор окончен. Постарайся не травмировать психику Лизы, хорошо?"
                            Max_01 "Хорошо, мам..."
                        "Да, я всё понял!":
                            pass
        "Хорошо, постараюсь...":
            Ann_05 "Вот и молодец. А если такое повторится, просто прикройся, как будто ничего нет..."
            Max_03 "Ну, ты же знаешь, что мне с моим размером это трудно сделать..."
            Ann_12 "Да, понимаю, конечно... Но беседа ушла куда-то не туда. В общем, постарайся не травмировать её психику, хорошо?"
            Max_00 "Хорошо, мам..."
    $ dcv.mw.stage = 2
    $ spent_time = 20
    jump Waiting


label talk_about_smoking:
    $ renpy.block_rollback()
    $ __mood = 0

    scene BG talk-terrace-00
    show Max talk-terrace 01a
    $ renpy.show("Ann talk-terrace 01"+ann.dress)
    menu:
        Ann_12 "Макс. Я не уверена, но мне кажется, что чувствую запах сигаретного дыма. К нам кто-то приходил?"
        "Нет, никого не было...":
            pass
        "Может быть, показалось?":
            pass
    menu:
        Ann_00 "Точно? Макс, ты ничего не хочешь рассказать?"
        "Нет, мам, нечего рассказывать":
            Ann_01 "Да? Ну, может и правда показалось. Или от соседей надуло... Ладно, давайте ужинать..."
            $ poss['smoke'].open(1)
            hide Ann
            show Alice talk-terrace 02a
            menu:
                Alice_03 "Спасибо, Макс, что не сдал меня... Я это ценю."
                "Всегда пожалуйста, сестрёнка!":
                    show Max talk-terrace 03a
                    Alice_05 "Вот можешь же быть не полным придурком... иногда..."
                    Max_01 "Ага. Ладно, давай ужинать"
                    $ AddRelMood('alice', 20, 100)
                    jump StartPunishment
                "Может, ещё сдам...":
                    show Max talk-terrace 02a
                    show Alice talk-terrace 03a
                    menu:
                        Alice_16 "Макс! Ты невыносим. Я уже подумала, что ты нормальный брат, а ты..."
                        "Да я пошутил...":
                            jump .joke
                        "Извини...":
                            jump .sorry
                        "Всё в твоих руках...":
                            jump .sorry
                "Если сделаешь кое-что, то и не сдам...":
                    show Max talk-terrace 02a
                    show Alice talk-terrace 03a
                    menu:
                        Alice_13 "Макс! Опять ты за своё? Не будь придурком!"
                        "Да я пошутил...":
                            jump .joke
                        "Извини...":
                            jump .sorry
                        "Всё в твоих руках...":
                            jump .sorry

    label .joke:
        show Max talk-terrace 03a
        show Alice talk-terrace 02a
        Alice_12 "Шутник... В общем, я надеюсь, что с этим вопросом разобрались. Уже пора ужинать"
        Max_01 "Ага, пора."
        jump StartPunishment

    label .sorry:
        show Max talk-terrace 03a
        show Alice talk-terrace 02a
        Alice_13 "Макс... А, ничего не буду говорить, бесполезно. Давай ужинать..."
        Max_01 "Ага, давай."
        jump StartPunishment


label ann_about_kiss:
    $ renpy.block_rollback()
    Ann_02 "Вот это вопрос, Макс. Неожиданный, я бы сказала... А зачем тебе? Нашёл девушку и хочешь её впечатлить?"
    Max_01 "Да, точно!"
    menu:
        Ann_04 "Ого! Поздравляю, Макс. Наконец-то ты нашёл кого-то. Расскажи, какая она?"
        "Да это не важно...":
            Ann_05 "Макс, что-то ты хитришь. Кстати, а где ты с нею познакомился? Ты же всё время дома сидишь... Через интернет?"
        "Ну, красивая...":
            Ann_05 "И где ты с этой девушкой познакомился? В интернете?"
    Max_07 "Типа того..."
    Ann_02 "Понятно. Ну что я могу тебе сказать. Буть естественным, будь самим собой. Девушки это ценят. Если ты попытаешься выдавать себя за ловеласа, она это раскусит и бросит тебя..."
    Max_08 "Ну мне всё равно надо научиться..."
    Ann_04 "Ну вот с этой девушкой и научишься целоваться. Лучше учителя тебе всё равно не найти!"
    Max_00 "Эх... Спасибо, мам..."
    Ann_07 "Не за что, Макс. Обращайся, если будет нужен ещё какой-то совет..."
    Max_01 "Ага, обязательно..."

    $ flags.how_to_kiss.append('ann')
    $ spent_time += 10
    return


label ann_about_ann_secret1:    # Попытка разузнать у Анны её секрет
    # стартовая фраза  "Мам, Кира отправила меня к тебе..."

    Ann_13 "Кира? Для чего, я не понимаю..."
    Max_07 "Она сказала, чтобы я поговорил с тобой про какой-то случай из твоего детства..."
    Ann_14 "Кира совсем не умеет держать язык за зубами... Макс, это точно не та история, которую я хочу тебе рассказать. Давай сменим тему."
    Max_09 "Вот теперь мне ещё больше интересно!"
    Ann_16 "Макс! Я же сказала, что не хочу об этом. А теперь иди, занимайся своими делами!"
    Max_08 "Ну а тётя может мне рассказать об этом?"
    Ann_17 "Нет, Макс. Это тебя не касается и я не хочу возвращаться к этой теме!"
    Max_11 "Я понял..."

    $ ann.dcv.feature.stage = 2
    $ poss['aunt'].open(14) # попытка разговора с Анной о случае из детства
    $ spent_time += 10
    jump Waiting


label ann_yoga_with_max0:       # первая совместная йога
    # стартовая фраза  "С тобой можно?"
    $ ann.dcv.feature.set_lost(1)   # следующая попытка на следующий день

    # Анна заметила, что Макс подглядывает за ней в душе перед йогой и убеждение не удалось
    if (punreason[3] or punreason[2]):
        jump yoga_after_peeping

    $ ann.dcv.feature.stage = 5
    $ poss['yoga'].open(0)

    # Макс не был замечен за подглядыванием в душе перед йогой или вовсе не подглядывал (или его заметили, но убеждение удалось)
    Ann_05 "Ты решил заняться йогой? Вот это да, Макс! Не ожидала! Но я буду рада твоей компании... Прямо сейчас планируешь начать?"
    Max_01 "Не совсем. Мы просто очень мало времени вместе проводим, вот я и решил присоединиться."
    Ann_14 "Да, знаю сынок. Я бы и сама хотела проводить со всеми вами больше времени..."
    Max_03 "Знаешь, я бы сначала просто посмотрел, что ты делаешь. Ну и может, помог чем. Расскажешь мне об этой йоге?"

    # yoga-01 + yoga-01-ann-01 + yoga-01-max-(01a/01b)
    # scene BG char Ann yoga 01
    # show Ann yoga 01-01a
    # $ renpy.show('Max yoga 01'+mgg.dress)
    $ var_pose = '01'
    $ var_stage = '01'
    scene Ann_yoga
    with fade4
    play music yoga

    Ann_04 "Вообще-то не очень удобно, выполнять упражнения и одновременно говорить. Но так уж и быть, сегодня я сделаю исключение."
    Max_07 "Тебе не больно так делать?"
    Ann_06 "Когда-то было, когда я только начинала это осваивать. Когда Алиса появилась на свет... Ох, как это было давно!"
    Max_09 "Так в чём суть?"

    # yoga-02 + yoga-02-max-(01a/01b) + yoga-02-ann-01
    # scene BG char Ann yoga 02
    # $ renpy.show('Max yoga 02'+mgg.dress)
    # show Ann yoga 02-01a
    $ var_stage = '02'
    # scene Ann_yoga
    show screen Cookies_Button
    Ann_07 "Ну, для начала, то что я делаю нельзя назвать йогой. Это скорее растяжка, в которой есть некоторые позы из упражнений по йоге."
    Max_04 "Для укрепления здоровья?"
    Ann_08 "Да. Здесь тебе и развитие гибкости, и оздоровление организма в целом, а так же выносливость и умиротворение. В моём возрасте это всё имеет очень важное значение, сынок."
    Max_05 "Да ты выглядишь получше многих старшеклассниц, мам!"
    Ann_05 "Спасибо, Макс! Приятно такое слышать. Значит, я не зря этим занимаюсь и это работает..."
    Max_02 "Ещё как работает! Может, я чем-то могу помочь?"

    hide screen Cookies_Button
    # yoga-03 + yoga-03-max-(01a/01b)-ann-01
    # scene BG char Ann yoga 03
    # $ renpy.show('Ann yoga 03-01a'+mgg.dress)
    $ var_stage = '03'
    Ann_02 "Тебе со стороны должно быть хорошо видно, всё ли я делаю правильно. У меня должна быть прямая спина и прямые ноги..."
    Max_01 "Ну да, почти. Разве что, ножки держи попрямее. Я тебя немножко придержу, чтобы ты лучше чувствовала, правильно ли всё делаешь..."
    Ann_06 "Ага, я поняла... Здесь важно правильно выстроить позу и просто дышать, стараясь максимально расслабиться."
    Max_09 "Сложно представить, что в таком положении можно расслабиться!"
    Ann_07 "Это приходит со временем, Макс. Сам-то попробовать не хочешь?"
    Max_07 "Пока что нет. Я лучше за тобой понаблюдаю и знаний наберусь сперва."

    # yoga-04 + yoga-04-max-(01a/01b)-ann-01
    # scene BG char Ann yoga 04
    # $ renpy.show('Ann yoga 04-01a'+mgg.dress)
    $ var_stage = '04'
    Ann_04 "Слегка придержи меня, чтобы я равновесие нашла... Только совсем легонько."
    Max_03 "Конечно. А ты на шпагат садишься?"
    Ann_13 "Ох, сынок, давно не пробовала. Честно говоря, побаиваюсь. Возраст всё-таки..."
    Max_04 "По-моему ты очень гибкая! Выглядишь прекрасно! И не важно сколько тебе лет, главное - на сколько ты себя чувствуешь."
    Ann_08 "Ой, ну всё, засмущал маму своими комплиментами. Пора заканчивать..."
    Max_05 "Хорошего понемножку, да?"

    # yoga-05 + yoga-05-ann-00 + yoga-05-max-(00a/00b)
    # scene BG char Ann yoga 05
    # show Ann yoga 05a
    # $ renpy.show('Max yoga 05'+mgg.dress)
    $ var_stage = '05'
    $ var_pose = '00'
    stop music
    Ann_05 "Именно так, Макс. Спасибо за компанию, вместе куда веселее... Буду только рада, если решишь снова присоединиться ко мне."
    menu:
        Max_01 "Хорошо, мам. Это я с радостью!"
        "{i}уйти{/i}":
            $ AddRelMood('ann', 0, 50)
    $ spent_time = max((60 - int(tm[-2:])), 30)
    jump Waiting


label yoga_after_peeping:       # попался на подглядывании в душе и провалил убеждение
    if flags.voy_stage < 4:     # (уроков для Макса у Анны и Эрика не было)
        Ann_17 "Макс, ты мне всё настроение испортил своим подглядыванием! Даже не думай отвлекать меня!"
    else:                       # был хотя бы один урок у Анны и Эрика
        Ann_17 "Макс, ты мне всё настроение испортил своим подглядыванием! Даже не думай отвлекать меня!"
        Max_09 "Значит за тобой с Эриком смотреть можно, а засмотреться, как ты принимаешь душ, нет?!"
        Ann_16 "Так, с Эриком - это совсем другое! Там это всё мы тебе показываем... для образовательных целей... А в душе или где-то ещё - это уже просто нахальство!"

    Max_11 "Ладно, понял..."
    jump Waiting


label ann_yoga_with_maxr:       # повторяемая совместная йога

    $ ann.dcv.feature.set_lost(1)   # следующая попытка на следующий день

    # Анна заметила, что Макс подглядывает за ней в душе перед йогой и убеждение не удалось
    if not _in_replay and (punreason[3] or punreason[2]):
        jump yoga_after_peeping

    if _in_replay:
        call ann_yoga from _call_ann_yoga

    menu:
        Ann_05 "Конечно, Макс, зачем спрашиваешь... Если ты ещё не созрел проверить свою гибкость, то просто смотри и помогай, если я попрошу. Ну и запоминай, что я делаю..."
        "Тебе не жарко, мам?" if ann.flags.help >= 4 and not poss['yoga'].used(1):
            Max_07 "Посмотри на себя! Какой ещё лишний вес?"
            Ann_04 "Вот потому я и выгляжу хорошо. И чувствую себя отлично, в тонусе, так сказать..."
            Max_09 "Ты хорошо выглядишь, потому что растяжкой занимаешься, а тело должно дышать."
            Ann_01 "И что ты предлагаешь?"
            Max_02 "Нужно прикупить для тебя спортивную одежду полегче, вот что."
            Ann_02 "Ну... может ты и прав. Пожалуй, на выходных мы с Эриком съездим и что-нибудь присмотрим."
            Max_07 "А давай я сам и за свои деньги?"
            Ann_13 "Сам? Ну не знаю, Макс... А тебе накопленных денег разве не жалко?"
            Max_03 "Для тебя, мам, ничего не жалко!"
            Ann_04 "Ну смотри, сынок... Я, конечно, рада твоему вниманию и заботе, но ты же понимаешь, что это должно быть что-то приличное и не слишком короткое?"
            Max_04 "Естественно. Ты будешь довольна!"
            Ann_12 "Надеюсь... Так, ты меня совсем заболтал разговорами своими. Давай уже делом заниматься..."
            Max_01 "Да, давай..."
            # открывается возможность купить новую одежду для йоги
            $ items['fit1'].unblock()
            $ poss['yoga'].open(1)
            $ notify_list.append(_("В интернет-магазине доступен новый товар."))
        "Продолжай, мам. Я весь во внимании...":
            pass

    # yoga-01 + yoga-01-ann-(01/01a или 02/02a или 03/03a) + yoga-01-max-(01a/01b)
    $ var_pose = renpy.random.choice(['01', '02', '03'])
    $ var_stage = '01'
    $ renpy.retain_after_load()
    scene Ann_yoga
    with fade4
    play music yoga

    Ann_02 "Я рада, что хоть так мы успеваем побыть вместе... Какие у тебя планы на день? Надеюсь, не за компьютером будешь всё время сидеть..."
    Max_04 "Ага... Класс..."
    Ann_12 "Это в смысле - да, будешь сидеть?"
    Max_03 "А, что? Я просто засмотрелся и немного прослушал, что ты говорила..."

    # yoga-02 + yoga-02-ann-(01/01a или 02/02a или 03/03a) + yoga-02-max-(01a/01b)
    $ var_pose = renpy.random.choice(['01', '02', '03'])
    $ var_stage = '02'
    $ renpy.retain_after_load()
    scene Ann_yoga
    show screen Cookies_Button
    Ann_04 "Макс, будь повнимательнее... Я ведь хочу, чтобы ты хоть чему-то научился от меня."
    Max_02 "О, мам, поверь, я сейчас очень внимателен!"
    Ann_06 "Тогда подержишь меня немножко, чтобы я всё правильно сделала?"
    Max_01 "Да, мам. Сейчас..."

    hide screen Cookies_Button
    # yoga-03 + yoga-03-max-(a/b)-ann-(01/01a или 02/02a или 03/03a)
    $ var_pose = renpy.random.choice(['01', '02', '03'])
    $ var_stage = '03'
    $ renpy.retain_after_load()
    Max_05 "{m}Она такая гибкая! Главное всё не испортить, хотя, как же хочется прикоснуться ко всему, что я перед собой сейчас вижу... Мама у меня конфетка!{/m}"
    Ann_08 "Макс, ты чего молчишь? Это мне говорить не очень удобно, потому что я стараюсь расслабиться и сосредоточиться на дыхании..."
    if any([
        all([_in_replay, 'yoga_truehelp' not in persistent.mems_var]),  # повтор, ещё не было расширенной йоги
        not _in_replay and all([ann.flags.showdown_e < 2, get_rel_eric()[0] < 0]),         # НАХ, Эрик
        not _in_replay and all([not poss['mom-tv'].used(13), get_rel_eric()[0] == 2]),     # Д-, ещё не делал массаж спины Анне
        ]):
        Max_03 "Да что тут скажешь, красота да и только!"
    elif ann.flags.defend < 5:
        $ ann.flags.defend += 1
        # (yoga-06 + yoga-06-max&ann-01 + Одежда(Анна перекрывает Макса))
        # (yoga-06 + yoga-06-max&ann-02 + Одежда(перекрытие неважно))
        # (yoga-04 + yoga-06-max&ann-03 + Одежда(перекрытие неважно))
        $ var_stage, var_pose = renpy.random.choice([('06', '01'), ('06', '02'), ('04', '03')])
        $ renpy.retain_after_load()
        Max_04 "Я смотрю, чтобы всё правильно делалось. Ты же этого хотела?"
        Ann_13 "А тебе, Макс, не кажется, что твои руки не совсем на месте?"
        Max_07 "А по-моему, именно там где надо. Иначе ты большей гибкости не добьёшься, мам. Или тебе этого не надо?"
        Ann_14 "Надо, но... Меня несколько смущает, что тебе для этого нужно руками контролировать мой зад..."
        Max_09 "Почему? Что тут такого? Я помогаю и к тому же, легонько. Ты лучше сосредоточься на дыхании и не зажимайся."
        Ann_03 "Да, Макс, верно. Мне лучше расслабиться. Продолжаем..."
        Max_05 "Правильно. Очень классно начинать день с такой красоты, как ты."
    else:
        # (yoga-06 + yoga-06-max&ann-01 + Одежда(Анна перекрывает Макса))
        # (yoga-06 + yoga-06-max&ann-02 + Одежда(перекрытие неважно))
        # (yoga-04 + yoga-06-max&ann-03 + Одежда(перекрытие неважно))
        $ var_stage, var_pose = renpy.random.choice([('06', '01'), ('06', '02'), ('04', '03')])
        $ renpy.retain_after_load()
        Max_04 "Я смотрю, чтобы всё правильно делалось. Ты же этого хотела?"
        Ann_03 "Только не держи меня так крепко, Макс! Придерживай легонько, я справлюсь."
        Max_05 "Хорошо, придерживаю слегка. Расслабься и сосредоточься на дыхании. Ты прогибаешься просто шикарно!"

    # yoga-04 + yoga-04-max-(a/b)-ann-(01/01a или 02/02a)
    # yoga-05 + yoga-05-max-(a/b)-ann-(03/03a)
    $ var_stage, var_pose = renpy.random.choice([('04', '01'), ('04', '02'), ('05', '03')])
    $ renpy.retain_after_load()
    Ann_07 "Приятно каждый раз от тебя слышать, что я не зря этим занимаюсь... Это прекрасно мотивирует."
    Max_04 "Тебе явно эти занятия идут только на пользу. А чувствуешь себя как?"
    Ann_06 "Немного устала, но в целом, мне хорошо. Появляется такое ощущение... лёгкости..."

    if any([
        all([_in_replay, 'yoga_truehelp' not in persistent.mems_var]),  # повтор, ещё не было расширенной йоги
        not _in_replay and all([ann.flags.showdown_e < 2, get_rel_eric()[0] < 0]), # Откровенная вражда, Эрик ещё не изгнан
        not _in_replay and all([poss['mom-tv'].used(13), get_rel_eric()[0] == 2]), # Фальшивая дружба, Макс делал Анне массаж спины
        ]):
        Max_05 "Здорово, мам! Ещё немного потянись и будет идеально..."
        Ann_14 "Главное - не перенапрячься с утра пораньше... А то буду еле живая на работе..."
        # yoga-05 + yoga-05-ann-(00/00a) + yoga-05-max-(00a/00b)
        $ var_pose = '00'
        $ var_stage = '05'
        $ renpy.retain_after_load()
        Ann_04 "Фух... На этом, пожалуй, закончим. Спасибо, что составил компанию. Буду только рада, если решишь снова присоединиться ко мне."
        stop music
        menu:
            Max_01 "С радостью, мам! Обязательно..."
            "{i}уйти{/i}":
                $ AddRelMood('ann', 0, 50)
                jump .end
    else:
        # (yoga-06 + yoga-07-max&ann-01 + Одежда(перекрытие неважно))
        # (yoga-06 + yoga-07-max&ann-02 + Одежда(перекрытие неважно))
        # (yoga-07-max&ann-03 + Одежда(Макс перекрывает Анну))
        $ var_pose = renpy.random.choice(['01', '02', '03'])
        $ var_stage = '07'
        $ renpy.retain_after_load()
        scene Ann_yoga seven
        Max_05 "Здорово, мам! Ещё немного потянись и будет идеально..."
        Ann_05 "Главное - не перенапрячься с утра пораньше... А то буду еле живая на работе... Но с твоей поддержкой, кажется, мне это не грозит."
        if not _in_replay:
            if not any([poss['yoga'].used(6), poss['yoga'].used(5)]):
                if get_rel_eric()[0] < 0:
                    $ poss['yoga'].open(6)
                else:   # if get_rel_eric()[0] == 2
                    $ poss['yoga'].open(5)

        if mgg.dress != 'b':
            Max_14 "{m}Ага, у меня сейчас в шортах такая твёрдая опора от всех этих сексуальных изгибов, что мама вот-вот заметит. А не думать о её шелковистом теле просто невозможно! И зачем я без майки этим занимаюсь?{/m}" nointeract
            menu:
                "{i}постараться успокоиться{/i}" ('sex', mgg.sex * 3, 90):
                    if rand_result:
                        $ ann.dcv.seduce.set_lost(2)
                        # yoga-05 + yoga-05-ann-(00/00a) + yoga-05-max-00b
                        $ var_stage = '05'
                        $ var_pose = '00'
                        $ ann.flags.truehelp += 1
                        $ renpy.retain_after_load()
                        $ added_mem_var('yoga_truehelp')
                        scene Ann_yoga
                        if ann.flags.defend == 1:
                            # для 1-ой йоги после 2-ого разговора с Анной на балконе
                            Ann_04 "[succes_hide!t]Ой, спасибо, сынок, что помог. Фух... На этом, пожалуй, закончим. Буду только рада, если решишь снова присоединиться ко мне."
                            Max_01 "С радостью, мам! Обязательно..."
                            Ann_02 "Но, давай хотя бы через день. Чтобы я могла без твоей помощи попробовать сделать то же самое."
                            Max_04 "Хорошо, как скажешь. До следующего раза, мам." nointeract
                        else:
                            # для последующих
                            Ann_04 "[succes_hide!t]Ой, спасибо, сынок, что помог. Фух... На этом, пожалуй, закончим. Завтра я сама попробую это повторить без тебя, а дальше присоединяйся, если захочешь. Я буду только рада."
                            Max_01 "С радостью, мам! Обязательно..." nointeract
                    else:
                        $ ann.dcv.seduce.set_lost(4)
                        # yoga-05 + yoga-05-ann-(01a/01b) + yoga-05-max-01c
                        $ var_stage = '05'
                        $ var_pose = '01'
                        $ renpy.retain_after_load()
                        scene Ann_yoga
                        if not ann.dcv.seduce.stage:
                            $ ann.dcv.seduce.stage = 1  # Анна засекла стояк Макса (йога)
                            # для 1-ого спаливания со стояком на йоге
                            Ann_15 "Ой, спасибо, сынок, что помог. Фух... А это что такое?! Как тебе не стыдно! Это у тебя на меня такая реакция?!"
                            Max_07 "Ну... Говорил же, красиво..."
                            Ann_14 "Макс, красивое не должно так возбуждать! Вернее, я не должна тебя так возбуждать. Другие женщины, да, но не я, сынок."
                            Max_09 "Хоть ты и моя мама, но ты так же и очень красивая женщина! Знаешь, мне кажется, что ЭТО - самый искренний комплимент твоей фигуре."
                            Ann_16 "Да уж, комплимент... Значит так, Макс! Ближайшие три дня можешь ко мне не подходить во время йоги. А в дальнейшем, можешь помогать через день. Всё понятно?"
                        else:
                            # для последующих
                            Ann_14 "Ой, спасибо, сынок, что помог. Фух... Да что же это такое! Ты опять перевозбудился..."
                            Max_07 "Ага, виновен..."
                            Ann_16 "И вот что прикажешь с тобой делать?"
                            Max_09 "Понять и простить. Я же мужчина всё-таки..."
                            Ann_17 "Ох, Макс, горе ты моё... Значит так, в ближайшие три дня можешь ко мне не подходить во время йоги, а дальше смотри сам, можешь присоединяться, но чтобы такое не повторялось. Всё понятно?"
                        Max_10 "Как скажешь, мам. До следующего раза..." nointeract
        else:
            $ ann.dcv.seduce.set_lost(2)
            Max_02 "Под моим присмотром у тебя всегда будет великолепная фигура!"
            # yoga-05 + yoga-05-ann-(00/00a) + yoga-05-max-00a
            $ var_stage = '05'
            $ var_pose = '00'
            $ ann.flags.truehelp += 1
            if not _in_replay:
                $ added_mem_var('yoga_truehelp')
            $ renpy.retain_after_load()
            scene Ann_yoga
            if ann.flags.defend == 1:
                # для 1-ой йоги после 2-ого разговора с Анной на балконе
                Ann_04 "Ой, спасибо, сынок, что помог. Фух... На этом, пожалуй, закончим. Буду только рада, если решишь снова присоединиться ко мне."
                Max_01 "С радостью, мам! Обязательно..."
                Ann_02 "Но, давай хотя бы через день. Чтобы я могла без твоей помощи попробовать сделать то же самое."
                Max_04 "Хорошо, как скажешь. До следующего раза, мам." nointeract
            else:
                # для последующих
                Ann_04 "Ой, спасибо, сынок, что помог. Фух... На этом, пожалуй, закончим. Завтра я сама попробую это повторить без тебя, а дальше присоединяйся, если захочешь. Я буду только рада."
                Max_01 "С радостью, мам! Обязательно..." nointeract

        menu:
            "{i}уйти{/i}":
                pass

    label .end:
        $ renpy.end_replay()
    $ ann.flags.help += 1
    $ spent_time = max((60 - int(tm[-2:])), 30)
    jump Waiting


label ann_gift_fit1:
    # стартовая фраза   "Мам, я купил тебе одежду полегче!"
    Ann_06 "Для моих занятий по утрам? Спасибо, дорогой! Ждала с нетерпением, показывай..."
    if ann.plan_name == 'resting':   #если Анна отдыхает в своей комнате
        Max_01 "Переодевайся... Хочу посмотреть, всё ли хорошо с размером."
        Ann_04 "Хорошо. Подожди минутку за дверью. Я тебя позову..."
    else:                           #если Анна читает или загорает
        Max_01 "Пойдём, переоденешься... Хочу посмотреть, всё ли хорошо с размером."
        Ann_04 "Хорошо. Пойдем в мою комнату. Я быстренько переоденусь, а ты подождёшь за дверью..."

    $ renpy.scene()
    $ renpy.show('location house annroom door-'+get_time_of_day())
    menu:
        "..."
        "{i}ждать{/i}":
            pass
    # #на фоне двери в комнату Анны
    Max_07 "{m}Надеюсь, она не станет возмущаться, насколько там всё коротенькое в одежде... С другой стороны, эта одежда не короче её бикини.{/m}"
    Ann "{b}Анна:{/b} Сынок, с размером всё в порядке. Вроде, сидит отлично. Только вот..."

    # annroom-morning-01 + ann-dresses-morning-05b
    # scene BG char Ann mde-01
    # show Ann dressed 07i # 05b
    $ var_pose, var_dress = '07', 'i'
    scene Ann_dressing
    with fade4
    Max_06 "Ого, мам! Тебе очень идёт! Выглядишь обалденно! Удобно?"
    Ann_14 "Да, Макс, удобно... Просто... Не слишком ли всё открыто?"
    Max_07 "Так, а где что открыто? Главное, чтобы было легко и комфортно. Тут такое солнце, даже ранним утром, что эта одежда - идеальный вариант."
    Ann_02 "Не могу не согласиться. Ладно, посмотрим, удобно ли будет в этой одежде заниматься..."
    Max_04 "Я уверен, что будет..."
    Ann_05 "Спасибо, что делаешь маме приятно... Иди ко мне, я тебя обниму, как следует..."
    # annroom-morning-01 + (hugging-annroom-01-max-(01a/01b)-ann-01b или hugging-annroom-02-max-(01a/01b)-ann-01b)
    # $ renpy.show('Ann hugging morning-annroom 0'+str(renpy.random.randint(1, 2))+'-1c'+mgg.dress)
    $ var_pose, var_dress = renpy.random.choice(['01', '02']), 'c'
    scene Ann_gift hug1
    Max_05 "{m}О да... У мамы такое потрясающее тело! Так приятно прижиматься к ней... её упругой груди... Что точно хорошо в новой одежде, так это то, что мне прекрасно видны очертания её сосочков через эту тонкую ткань!{/m}"
    # annroom-morning-01 + (hugging-annroom-01-max-(02a/02b)-ann-02b или hugging-annroom-02-max-(02a/02b)-ann-02b)
    # $ renpy.show('Ann hugging morning-annroom 0'+str(renpy.random.randint(1, 2))+'-2c'+mgg.dress)
    scene Ann_gift hug2
    menu:
        Ann_04 "Ну всё, мой дорогой, не будем же мы так часами стоять обниматься, пора делами заняться..."
        "Давай ещё?! Ты такая классная!":
            Ann_05 "Ты сегодня очень мил, Макс! За это я тебя даже в щёчку поцелую, чтобы ты почаще старался меня радовать..."
            # annroom-morning-01 + (hugging-annroom-01-max-(03a/03b)-ann-03b или hugging-annroom-02-max-(03a/03b)-ann-03b)
            # $ renpy.show('Ann hugging morning-annroom 0'+str(renpy.random.randint(1, 2))+'-3c'+mgg.dress)
            scene Ann_gift hug3
            Max_06 "{m}Ухх, а как хочется притянуть маму к себе за её аппетитную и подтянутую попку... Ммм... Вот это было бы очень сладко!{/m}"
            menu:
                Ann_04 "Ну вот, дорогой. Теперь, давай заниматься своими делами..."
                "Хорошо... Я тебя люблю, мам!":
                    Ann_07 "И я тебя, Макс..."
                "Конечно, мам! Не скучай...":
                    Ann_02 "Спасибо, сынок! И ты тоже..."
        "Конечно, мам! Не скучай...":
            Ann_02 "Спасибо, сынок! И ты тоже..."

    $ items['fit1'].give()
    if get_rel_eric()[0] < 0:
        $ poss['yoga'].open(4)  # новая спортивка, Откровенная вражда
    elif get_rel_eric()[0] == 2:
        $ poss['yoga'].open(3)  # новая спортивка, Фальшивая дружба
    else:
        $ poss['yoga'].open(2)  # новая спортивка, Настоящая дружба

    $ ann.gifts.append('fit1')
    $ setting_clothes_by_conditions()
    $ spent_time = 30
    $ AddRelMood('ann', 50, 150)
    jump Waiting


# 1-ая половина фильма
label erofilm2_1:
    # "А я прикупил фильм на вечер. Посмотрим?"

    # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(00a/00b)
    scene BG lounge-tv-01
    $ renpy.show('Ann tv-closer '+pose3_3)
    $ renpy.show("Max tv 00"+mgg.dress)
    Ann_02 "Я не против. По кабельному всё равно ничего интересного я не нашла. А что за фильм?"

    # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(04a/04b)
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer "+pose3_3)
    $ renpy.show("Max tv-closer 04"+mgg.dress)
    Max_01 "Называется \"Цвет ночи\", триллер-детектив с Брюсом Уиллисом. Не смотрела?"
    Ann_05 "Нет, я не смотрела. Но название какое-то знакомое... Где-то я его слышала... Но не могу вспомнить."
    Max_04 "Может, когда будем смотреть, вспомнишь..."

    # tv-watch-01 + ero_mov_02_01 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    scene BG tv-watch-01
    show tv ero2 01 at tv_screen
    show Ann tv-watch 01
    $ renpy.show('Max tv-watch 01'+mgg.dress)
    Ann_04 "В каком году вышел этот фильм? Судя по качеству картинки, ему уже немало лет..."
    Max_03 "Ага. В 1994 году вышел. Постарше меня будет."

    # tv-watch-01 + ero_mov_02_02 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    show tv ero2 02 at tv_screen
    Ann_13 "Судя по тому, что происходит, у фильма должен быть высокий возрастной рейтинг..."
    Max_09 "Высокий, но это же триллер-детектив, мам! Без крови и смертей не обойдётся..."
    Ann_14 "Вот я и думаю, стоит ли тебе такое на ночь глядя смотреть."
    Max_07 "Не переживай, мам. Смотри, у его друга дом почти как у нас!"

    # tv-watch-01 + ero_mov_02_03 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    show tv ero2 03 at tv_screen
    Max_02 "{m}Только в кино в твою машину может въехать такая красивая девушка! Я бы с её задним \"бампером\" такое навытворял... И так, и этак!{/m}"

    # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
    scene BG tv-mass-03
    $ renpy.show('Max tv-ero 01'+mgg.dress)
    $ renpy.show('Ann tv-ero 01-0'+str(renpy.random.randint(1, 3)))
    show screen Cookies_Button
    menu:
        Max_08 "{m}Зря я это представил... Если мама увидит мой стояк, то просмотр для меня точно закончится. Хорошо, что есть проверенный и приятный способ его скрыть...{/m}"
        "Мам, хочешь массаж?":
            hide screen Cookies_Button
            if ann.flags.handmass:
                # предыдущий массаж был успешным
                # tv-mass-07 + tv-ero-01-max-(03a/03b) + tv-ero-01-ann-(07/08/09)
                scene BG tv-mass-07
                $ renpy.show('Max tv-ero 03'+mgg.dress)
                $ renpy.show('Ann tv-ero 01-0'+str(6+int(pose3_3)))
                Ann_04 "Ой, я думала, ты и не предложишь. В прошлый раз ты так хорошо мне плечи и шею помассировал, что я буду очень рада, если ты это повторишь..."
                Max_04 "С удовольствием, мам!"
            else:
                # предыдущий массаж не был успешным
                # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
                scene BG tv-mass-05
                $ renpy.show('Max tv-ero 02'+mgg.dress)
                $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
                Ann_02 "Ой, я думала, ты и не предложишь. Надеюсь, сегодня ты отнесёшься к массажу с большим вниманием, чем в прошлый раз?"
                Max_01 "Да, мам, я постараюсь..."

    # tv-mass-05 + tv-ero-02-max-(01a/01b)-ann-01
    scene BG tv-mass-05
    $ renpy.show('Ann tv-ero 02-01'+mgg.dress)
    Ann_05 "Ой, Макс! Как же чудесно... Как хорошо, что ты у меня есть... Твои руки просто нереально расслабляют!"
    Max_03 "Спасибо! Я рад, что тебе нравится."

    # tv-watch-01 + ero_mov_02_04 + tv-watch-01-max&ann-(01a/01b)
    scene BG tv-watch-01
    show tv ero2 04 at tv_screen
    $ renpy.show('Max tv-watch ann-01'+mgg.dress)
    Ann_08 "У тебя это очень хорошо получается... Такая лёгкость наступает. С таким талантом ты у нас дома будешь нарасхват! Да и вне его..."
    Max_02 "Очень надеюсь, что так и будет."

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01
    scene BG char Kira after-club-s08a-f
    $ renpy.show('Max tv-ero 03-01'+mgg.dress)
    $ renpy.dynamic('pose')
    menu:
        Max_05 "{m}Уххх... А у мамы ведь полотенце сползло... И она это ещё не заметила! Должно быть, мой массаж действительно её хорошо расслабил! Надо продолжать... Может оно тогда ещё больше спадёт...{/m}"
        "{i}продолжать массаж{/i}" ('mass', mgg.massage):
            pass
    if rand_result:
        # (Маме понравился массаж!)
        # tv-ero-04 + tv-ero-04-max-(01a/01b)-ann-01
        scene BG tv-ero-04
        $ renpy.show('Max tv-ero 04-01'+mgg.dress)
        Max_06 "[ann_good_mass!t]{m}О да! Полотенце сползает всё больше и больше... Какие у неё милые и тёмные сосочки! Интересно, что будет, если я потяну руки ниже, как с Лизой? Вряд ли что-то хорошее...{/m}"

        # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
        scene BG after-club-s04-f
        $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
        Ann_15 "Ой! Ничего себе! Макс, ты почему не сказал, что у меня полотенце сползло?! Чуть голой не осталась!"
        Max_02 "Так я не видел! Фильм же смотрю..."

        Ann_04 "А ты молодец, если умудряешься и фильм одновременно смотреть и массаж так хорошо делать!"
        Max_01 "Ты же сама сказала - талант."

        # tv-watch-01 + ero_mov_02_05 + tv-watch-01-max&ann-(01a/01b)
        scene BG tv-watch-01
        show tv ero2 05 at tv_screen
        $ renpy.show('Max tv-watch ann-01'+mgg.dress)
        Ann_14 "Так, как-то здесь всё слишком откровенно начало развиваться... Прямо очень откровенно! Ты специально такой фильм купил?"
        Max_07 "Нет. Меня начало описания к фильму заинтересовало. Наверно, нужно было дочитать до конца..."

        # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
        scene BG char Kira after-club-s08a-f
        $ renpy.show('Max tv-ero 03-01'+mgg.dress)
        show Ann tv-ero 03-01

        $ pose = 'good'

        $ ann.flags.m_shoulder += 1
        $ ann.flags.handmass = True
        $ AddRelMood('ann', 5, 30)
    else:
        # (Маме не понравился массаж!)
        # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
        scene BG after-club-s04-f
        $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
        menu:
            Ann_15 "[ann_bad_mass!t]Ой! Ничего себе! Макс, ты почему не сказал, что у меня полотенце сползло?! Чуть голой не осталась! Давай-ка прервёмся с массажем... и досмотрим фильм. А то ты уж слишком много отвлекаешься."
            "{i}закончить массаж и попытаться скрыть стояк{/i}":
                #(может спалиться 25% в майке и шортах / может спалиться 50% в шортах)
                $ ann.flags.handmass = False

        if random_outcome(60 if mgg.dress == 'b' else 40):
            # (Повезло!)
            # tv-watch-01 + ero_mov_02_05 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
            scene BG tv-watch-01
            show tv ero2 05 at tv_screen
            show Ann tv-watch 01
            $ renpy.show('Max tv-watch 01'+mgg.dress)
            Ann_14 "[lucky!t]Так, как-то здесь всё слишком откровенно начало развиваться... Прямо очень откровенно! Ты специально такой фильм купил?"
            Max_07 "Нет. Меня начало описания к фильму заинтересовало. Наверно, нужно было дочитать до конца..."

            # tv-mass-07 + tv-ero-01-max-(03a/03b) + tv-ero-01-ann-(07/08/09)
            scene BG tv-mass-07
            $ renpy.show('Max tv-ero 03'+mgg.dress)
            $ renpy.show('Ann tv-ero 01-0'+str(6+int(pose3_3)))

            $ pose = 'lucky'

        else:
            # (Не повезло!)
            # tv-kiss-03 + tv-ero-00-max-(01a/01b) + tv-ero-00-ann-01
            scene BG tv-kiss-03
            $ renpy.show('Max tv-ero 00-01'+mgg.dress)
            show Ann tv-ero 00-01
            Ann_15 "[unlucky!t]Макс! Это что такое?! Ты почему такой возбуждённый? Из-за фильма? А, ну да, конечно, я ещё спрашиваю..."
            Max_08 "Похоже на то. Там ведь очень откровенные сцены пошли..."

            # tv-watch-01 + ero_mov_02_05 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
            scene BG tv-watch-01
            show tv ero2 05 at tv_screen
            show Ann tv-watch 01
            $ renpy.show('Max tv-watch 01'+mgg.dress)
            Ann_14 "Ты специально такой фильм купил?"
            Max_07 "Нет. Меня начало описания к фильму заинтересовало. Наверно, нужно было дочитать до конца..."

            $ pose = 'unlucky'

    Ann_15 "Всё, Макс! Такое мы дальше смотреть не будем. По крайней мере {b}ТЫ{/b} не будешь смотреть!"
    Max_09 "Я же всё равно досмотрю этот фильм. Только без тебя это не так интересно..."

    scene BG tv-watch-01
    show tv ero2 06 at tv_screen
    if pose == 'good':
        # tv-watch-01 + ero_mov_02_06 + tv-watch-01-max&ann-(01a/01b)
        $ renpy.show('Max tv-watch ann-01'+mgg.dress)
    else:
        # tv-watch-01 + ero_mov_02_06 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)

    Ann_13 "Сынок, смотреть такую откровенную эротику со своей мамой не очень-то правильно."
    if flags.voy_stage>3 and GetRelMax('eric')[0]>0:
        # у Макса были уроки у Анны и Эрика
        Max_07 "А на то, что вы с Эриком делаете смотреть значит можно? И просмотр эротического фильма точно не дотягивает до вас!"
    else:
        # Анна и Эрик ловили Макса за подглядыванием
        Max_07 "Я ведь уже не раз видел, как вы с Эриком такое делаете! И просмотр эротического фильма точно не дотягивает до вас!"

    if pose == 'good':
        # tv-mass-05 + tv-ero-02-max-(01a/01b)-ann-01
        scene BG tv-mass-05
        $ renpy.show('Ann tv-ero 02-01'+mgg.dress)
    elif pose == 'lucky':
        # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
        scene BG tv-mass-03
        $ renpy.show('Max tv-ero 01'+mgg.dress)
        $ renpy.show('Ann tv-ero 01-0'+str(renpy.random.randint(1, 3)))
        show screen Cookies_Button
    else:
        pass

    Ann_14 "Мне всё кажется, что ты ещё недостаточно взрослый, для таких вещей."
    Max_09 "Мам, а если у меня девушка появится, ты что, думаешь мы только за ручку будем гулять и розового единорога почёсывать?"

    hide screen Cookies_Button
    scene BG tv-watch-01
    show tv ero2 07 at tv_screen
    if pose == 'good':
        # tv-watch-01 + ero_mov_02_07 + tv-watch-01-max&ann-(01a/01b)
        $ renpy.show('Max tv-watch ann-01'+mgg.dress)
    else:
        # tv-watch-01 + ero_mov_02_07 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)

    Ann_12 "Да, ты прав. Но пока у тебя эта самая девушка не появилась..."
    Max_00 "А пока я буду смотреть эротику с тобой! Под твоим контролем."

    if pose == 'good':
        # tv-ero-04 + tv-ero-04-max-(01a/01b)-ann-01 + tv-ero-04-ann-01a
        scene BG tv-ero-04
        $ renpy.show('Max tv-ero 04-01'+mgg.dress)
        show Ann tv-ero 04-01
    else:
        # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
        scene BG tv-mass-05
        $ renpy.show('Max tv-ero 02'+mgg.dress)
        $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))

    Ann_14 "Ну не знаю, Макс. Я уже поняла, что смотреть такое со мной, тебя абсолютно не смущает. А вот меня ещё как!"
    Max_07 "Это уже хорошая возможность побольше рассказать мне о взрослой жизни."
    Ann_15 "Хорошо, сынок, я подумаю... Ого! А я и не знала, что это кино идёт больше двух часов! Давай досмотрим в следующее воскресенье? Если, конечно, я не передумаю..."
    Max_01 "Ладно."

    $ renpy.end_replay()
    $ ann.flags.erofilms = 2
    $ poss['mom-tv'].open(9)
    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ SetCamsGrow(house[4], 180)
    jump Waiting

label erofilm2_2:
    # 2-ая половина фильма
    # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(00a/00b)
    scene BG lounge-tv-01
    $ renpy.show('Ann tv-closer '+pose3_3)
    $ renpy.show("Max tv 00"+mgg.dress)
    # "Мы не досмотрели один фильм. Помнишь?"
    $ ann.flags.erofilms = 3
    Ann_01 "Ох, Макс... Как же такое не помнить. Глупо было надеяться, что ты забудешь..."

    # lounge-tv-01 + tv-ann-(01/02/03) + tv-max-(04a/04b)
    scene BG lounge-tv-01
    $ renpy.show("Ann tv-closer "+pose3_3)
    $ renpy.show("Max tv-closer 04"+mgg.dress)
    Max_07 "Так досматриваем или ты не хочешь?"
    Ann_12 "Нет, я хочу. Просто... Меня не покидает ощущение, что я делаю что-то неправильно."
    Max_09 "Хочешь сказать, готовить меня ко взрослой жизни - это неправильно? Брось... По-моему, всё дело в том, что ты не хочешь, чтобы я повзрослел."

    # tv-watch-01 + ero_mov_02_08 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    scene BG tv-watch-01
    show tv ero2 08 at tv_screen
    show Ann tv-watch 01
    $ renpy.show('Max tv-watch 01'+mgg.dress)
    Ann_02 "Конечно хочу, сынок. Просто... Кажется ещё недавно вы с Лизой были совсем малютками... А сейчас..."
    Max_04 "Ни одной малютки не осталось... Все выросли..."

    # tv-watch-01 + ero_mov_02_09 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
    show tv ero2 09 at tv_screen
    Ann_13 "Ой, снова эротика пошла... Сюрпризы от этой героини, конечно, меня поражают всё больше и больше!"
    Max_02 "По мне, так классная идея, готовить в одном фартуке! Тебе стоит взять это себе на заметку, мам..."
    Ann_15 "Сынок, ну ты что такое говоришь!"
    Max_03 "А что? Качество твоей готовки от этого не стало бы хуже! Зато какой вид..."

    # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
    scene BG tv-mass-03
    $ renpy.show('Max tv-ero 01'+mgg.dress)
    $ renpy.show('Ann tv-ero 01-0'+str(renpy.random.randint(1, 3)))
    show screen Cookies_Button
    Ann_17 "Так, Макс... В этот раз представим, что я ничего не слышала, но за подобные мысли я и наказать могу. И даже представлять меня не вздумай в одном лишь фартуке!"
    menu:
        Max_08 "{m}Эх, мам... Уже поздно. И о таком зрелище я точно в ближайшее время не смогу забыть! Надеюсь, она не заметит, что у меня стоит...{/m}"
        "Мам, хочешь массаж?":
            hide screen Cookies_Button
            if ann.flags.handmass:
                # предыдущий массаж был успешным
                # tv-mass-07 + tv-ero-01-max-(03a/03b) + tv-ero-01-ann-(07/08/09)
                scene BG tv-mass-07
                $ renpy.show('Max tv-ero 03'+mgg.dress)
                $ renpy.show('Ann tv-ero 01-0'+str(6+int(pose3_3)))
                Ann_04 "Ой, я думала, ты и не предложишь. В прошлый раз ты так хорошо мне плечи и шею помассировал, что я буду очень рада, если ты это повторишь..."
                Max_04 "С удовольствием, мам!"
            else:
                # предыдущий массаж не был успешным
                # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
                scene BG tv-mass-05
                $ renpy.show('Max tv-ero 02'+mgg.dress)
                $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
                Ann_02 "Ой, я думала, ты и не предложишь. Надеюсь, сегодня ты отнесёшься к массажу с большим вниманием, чем в прошлый раз?"
                Max_01 "Да, мам, я постараюсь..."

    # tv-mass-05 + tv-ero-02-max-(01a/01b)-ann-01
    scene BG tv-mass-05
    $ renpy.show('Ann tv-ero 02-01'+mgg.dress)
    Ann_05 "Ой, Макс! Как же чудесно... Как хорошо, что ты у меня есть... Твои руки просто нереально расслабляют!"
    Max_03 "Спасибо! Я рад, что тебе нравится."

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
    scene BG char Kira after-club-s08a-f
    $ renpy.show('Max tv-ero 03-01'+mgg.dress)
    show Ann tv-ero 03-01
    Ann_08 "У тебя это очень хорошо получается... Такая лёгкость наступает. С таким талантом ты у нас дома будешь нарасхват! Довольны будут все..."
    Max_02 "Очень надеюсь, что так и будет."

    # tv-watch-01 + ero_mov_02_10 + tv-watch-01-max&ann-(01a/01b)
    scene BG tv-watch-01
    show tv ero2 10 at tv_screen
    $ renpy.show('Max tv-watch ann-01'+mgg.dress)
    Ann_06 "Не могу не признаться, но эротические моменты в этом фильме прекрасно сняты. Никогда бы не подумала, что буду говорить такое при собственном сыне. И что я за мать!"
    Max_04 "Самая лучшая на свете!"
    Ann_02 "Спасибо, сынок. Но вряд ли твоё мнение разделили бы нормальные родители."
    Max_07 "А откуда ты знаешь, что они нормальные? Ничего плохого мы сейчас не делаем."

    # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01
    scene BG char Kira after-club-s08a-f
    $ renpy.show('Max tv-ero 03-01'+mgg.dress)
    menu:
        Max_05 "{m}У мамы снова полотенце сползает, а она не чувствует... Надо продолжать, раз ей так нравится массаж... Или лучше сказать?{/m}"
        "Мам, у тебя полотенце сползает...":

            # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
            scene BG after-club-s04-f
            $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
            Ann_13 "Ой, Макс! Хорошо, что предупредил... Чуть голой не осталась! И давно я сижу вся такая довольная без полотенца?"
            Max_01 "Не знаю. Я как заметил, так сразу и сказал."
            menu:
                Ann_04 "Давай-ка на сегодня прервёмся с массажем... и досмотрим фильм. Это не значит, что мне не понравилось! Ты молодец!"
                "{i}закончить массаж и попытаться скрыть стояк{/i}":
                    if random_outcome(60 if mgg.dress == 'b' else 40) or _in_replay:
                        jump .lucky
                    else:
                        jump .unlucky

        "{i}продолжать массаж{/i}" ('mass', mgg.massage):
            if rand_result:
                # (Маме понравился массаж!)
                # tv-ero-04 + tv-ero-04-max-(01a/01b)-ann-01
                scene BG tv-ero-04
                $ renpy.show('Max tv-ero 04-01'+mgg.dress)
                Max_06 "[ann_good_mass!t]{m}Ммм... Полотенце сползает всё больше и больше... Вот бы однажды помассировать эти сочные дыньки! Ох, как же сложно удержаться и не запустить туда вниз свои руки...{/m}"

                # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
                scene BG after-club-s04-f
                $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
                Ann_15 "Ой! Ничего себе! Макс, ты почему не сказал, что у меня полотенце сползло?! Чуть голой не осталась!"
                Max_02 "Так я не видел! Фильм же смотрю..."
                Ann_04 "А ты молодец, если умудряешься и фильм одновременно смотреть и массаж так хорошо делать!"
                Max_01 "Ты же сама сказала - талант."

                # tv-watch-01 + ero_mov_02_11 + tv-watch-01-max&ann-(01a/01b)
                scene BG tv-watch-01
                show tv ero2 11 at tv_screen
                $ renpy.show('Max tv-watch ann-01'+mgg.dress)
                Ann_04 "Помимо всего прочего, в фильме музыка очень хороша. Мне прямо нравится!"

                # after-club-s08a-f + tv-ero-03-max-(01a/01b)-ann-01 + tv-ero-03-ann-01a
                scene BG char Kira after-club-s08a-f
                $ renpy.show('Max tv-ero 03-01'+mgg.dress)
                show Ann tv-ero 03-01
                Max_05 "{m}Интересно, а у мамы было что-нибудь... с женщинами... О да! За такой картиной я бы с удовольствиям подсмотрел! Хотя, не отказался бы и поучаствовать...{/m}"

                # tv-watch-01 + ero_mov_02_12 + tv-watch-01-max&ann-(01a/01b)
                scene BG tv-watch-01
                show tv ero2 12 at tv_screen
                $ renpy.show('Max tv-watch ann-01'+mgg.dress)
                Ann_05 "Судя по времени, дела идут к развязке. Забавно за ними всеми наблюдать... Как они только сейчас понимают то, что зритель понял уже давно."

                # tv-mass-05 + tv-ero-02-max-(01a/01b)-ann-01
                scene BG tv-mass-05
                $ renpy.show('Ann tv-ero 02-01'+mgg.dress)
                Max_04 "Да, намёки для зрителей были местами очень жирные."

                # tv-watch-01 + ero_mov_02_13 + tv-watch-01-max&ann-(01a/01b)
                scene BG tv-watch-01
                show tv ero2 13 at tv_screen
                $ renpy.show('Max tv-watch ann-01'+mgg.dress)
                Ann_06 "Вот и досмотрели. Интересный детектив... Мне понравился. Но этот фильм и близко не для детей снят..."
                menu:
                    Max_03 "А где ты тут детей видишь?"
                    "{i}закончить массаж и попытаться скрыть стояк{/i}":
                        # (может спалиться 25% в майке и шортах / может спалиться 50% в шортах)
                        $ ann.flags.m_shoulder += 1
                        $ ann.flags.handmass = True
                        $ AddRelMood('ann', 5, 30)

                if random_outcome(60 if mgg.dress == 'b' else 40) or _in_replay:
                    # (Повезло!)
                    # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
                    scene BG tv-mass-05
                    $ renpy.show('Max tv-ero 02'+mgg.dress)
                    $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
                    Ann_04 "[lucky!t]Да, знаю... знаю... Ты уже взрослый. Почти..."
                    jump .end

                else:
                    # (Не повезло!)
                    # tv-kiss-03 + tv-ero-00-max-(01a/01b) + tv-ero-00-ann-01
                    scene BG tv-kiss-03
                    $ renpy.show('Max tv-ero 00-01'+mgg.dress)
                    show Ann tv-ero 00-01
                    Ann_15 "[unlucky!t]Макс! Это что такое?! Ты почему такой возбуждённый? В фильме же откровенные сцены давно были..."
                    Max_08 "Я не знаю! Видимо, мысли об этих сценах ещё не выветрились из головы."
                    Ann_17 "Вот я так и знала! Зря мы этот фильм смотрели!"
                    Max_09 "Подумаешь, возбудился... Значит фильм оправдал свою эротическую составляющую."
                    Ann_13 "Макс, мама не должна видеть своего сына таким..."
                    Max_07 "А ты просто возьми и не смотри! Я же не маленький ребёнок, а..."

                    # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
                    scene BG tv-mass-05
                    $ renpy.show('Max tv-ero 02'+mgg.dress)
                    $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
                    Ann_04 "Да, знаю... знаю... Ты уже взрослый. Почти..."
                    jump .end

            else:
                # (Маме не понравился массаж!)
                # after-club-s04-f + tv-ero-05-max-(01a/01b)-ann-01
                scene BG after-club-s04-f
                $ renpy.show('Ann tv-ero 05-01'+mgg.dress)
                menu:
                    Ann_15 "[ann_bad_mass!t]Ой! Ничего себе! Макс, ты почему не сказал, что у меня полотенце сползло?! Чуть голой не осталась! Давай-ка прервёмся с массажем... и досмотрим фильм. А то ты уж слишком много отвлекаешься."
                    "{i}закончить массаж и попытаться скрыть стояк{/i}":
                        $ ann.flags.handmass = True
                # (может спалиться 25% в майке и шортах / может спалиться 50% в шортах)
                if random_outcome(60 if mgg.dress == 'b' else 40):
                    jump .lucky
                else:
                    jump .unlucky

    label .lucky:
        # (Повезло!)
        # tv-watch-01 + ero_mov_02_11 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        scene BG tv-watch-01
        show tv ero2 11 at tv_screen
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)
        Ann_04 "[lucky!t]Помимо всего прочего, в фильме музыка очень хороша. Мне прямо нравится!"

        # tv-mass-07 + tv-ero-01-max-(03a/03b) + tv-ero-01-ann-(07/08/09)
        scene BG tv-mass-07
        $ renpy.show('Max tv-ero 03'+mgg.dress)
        $ renpy.show('Ann tv-ero 01-0'+str(6+int(pose3_3)))
        Max_05 "{m}Интересно, а у мамы было что-нибудь... с женщинами... О да! За такой картиной я бы с удовольствиям подсмотрел! Хотя, не отказался бы и поучаствовать...{/m}"

        # tv-watch-01 + ero_mov_02_12 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        scene BG tv-watch-01
        show tv ero2 12 at tv_screen
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)
        Ann_05 "Судя по времени, дела идут к развязке. Забавно за ними всеми наблюдать... Как они только сейчас понимают то, что зритель понял уже давно."

        # tv-mass-03 + tv-ero-01-max-(01a/01b) + tv-ero-01-ann-(01/02/03)
        scene BG tv-mass-03
        $ renpy.show('Max tv-ero 01'+mgg.dress)
        $ renpy.show('Ann tv-ero 01-'+pose3_3)
        show screen Cookies_Button
        Max_04 "Да, намёки для зрителей были местами очень жирные."

        hide screen Cookies_Button
        # tv-watch-01 + ero_mov_02_13 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        scene BG tv-watch-01
        show tv ero2 13 at tv_screen
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)
        Ann_06 "Вот и досмотрели. Интересный детектив... Мне понравился. Но этот фильм и близко не для детей снят..."
        Max_03 "А где ты тут детей видишь?"

        # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
        scene BG tv-mass-05
        $ renpy.show('Max tv-ero 02'+mgg.dress)
        $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
        Ann_04 "Да, знаю... знаю... Ты уже взрослый. Почти..."
        jump .end

    label .unlucky:
        # (Не повезло!)
        # tv-kiss-03 + tv-ero-00-max-(01a/01b) + tv-ero-00-ann-01
        scene BG tv-kiss-03
        $ renpy.show('Max tv-ero 00-01'+mgg.dress)
        show Ann tv-ero 00-01
        Ann_15 "[unlucky!t]Макс! Это что такое?! Ты почему такой возбуждённый? Из-за фильма? А, ну да, конечно, я ещё спрашиваю..."
        Max_08 "Похоже на то. Там ведь очень откровенные сцены были, а теперь эти дамочки что-то интересное затевают..."

        # tv-watch-01 + ero_mov_02_11 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        scene BG tv-watch-01
        show tv ero2 11 at tv_screen
        show Ann tv-watch 01
        $ renpy.show('Max tv-watch 01'+mgg.dress)
        Ann_17 "Рановато тебе ещё такое смотреть! Хотя, по сравнению с тем, что ты уже увидел до этого..."
        Max_05 "{m}Интересно, а у мамы было что-нибудь... с женщинами... О да! За такой картиной я бы с удовольствиям подсмотрел! Хотя, не отказался бы и поучаствовать...{/m}"

        #tv-watch-01 + ero_mov_02_12 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        show tv ero2 12 at tv_screen
        Ann_05 "Судя по времени, дела идут к развязке. Забавно за ними всеми наблюдать... Как они только сейчас понимают то, что зритель понял уже давно."
        Max_04 "Да, намёки для зрителей были местами очень жирные."

        #tv-watch-01 + ero_mov_02_13 + tv-watch-01-ann-01 + tv-watch-01-max-(01a/01b)
        show tv ero2 13 at tv_screen
        Ann_06 "Вот и досмотрели. Интересный детектив... Мне понравился. Но этот фильм и близко не для детей снят..."
        Max_03 "А где ты тут детей видишь?"

        # tv-mass-05 + tv-ero-01-max-(02a/02b) + tv-ero-01-ann-(04/05/06)
        scene BG tv-mass-05
        $ renpy.show('Max tv-ero 02'+mgg.dress)
        $ renpy.show('Ann tv-ero 01-0'+str(3+int(pose3_3)))
        Ann_04 "Да, знаю... знаю... Ты уже взрослый. Почти..."
        jump .end

    label .end:
        pass

    Max_02 "В следующий раз посмотрим что-нибудь ещё подобное?"
    Ann_02 "Только будь поскромнее. Этот фильм оказался очень волнующим..."
    Max_01 "Конечно, мам!"

    $ renpy.end_replay()
    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ SetCamsGrow(house[4], 180)
    $ items['erofilm2'].block()
    if get_rel_eric()[0] < 0:
        $ poss['mom-tv'].open(12)
    elif get_rel_eric()[0] == 2:
        $ poss['mom-tv'].open(11)
    else:
        $ poss['mom-tv'].open(10)
    jump Waiting


label ann_about_wallet:

    Ann_16 "Ты вернул Эрику бумажник и деньги?"
    Max_09 "Да не крал я у него ничего! Он всех обманывает!"
    Ann_18 "Пока не вернёшь, даже не подходи ко мне, Макс! Всё настроение от тебя только портится. А уж как мне перед Эриком стыдно..."
    Max_11 "Как скажешь, мам."

    $ notify_list.append(__("{b}Оповещение:{/b} Анна больше не хочет взаимодействовать с Максом"))

    $ spent_time = 10
    $ ann.hourly.talkblock = 1
    $ ann.flags.talkblock = 1
    jump Waiting


# первый разговор с Анной о ночёвке Оливии
label ann_about_olivia0:
    # "Мам, нужно поговорить об Оливии."
    $ spent_time = 10
    Ann_00 "Да, Макс, что такое?"
    Max_07 "Можно она будет приходить к нам с ночёвкой по пятницам?"
    Ann_13 "С ночёвкой? Ну, не знаю, сынок. А её родители, что скажут? И кто за вами будет присматривать?"
    Max_09 "За нами не нужно присматривать, мы уже взрослые. И раз это для тебя так важно, то я присмотрю за Оливией и Лизой."
    Ann_17 "А заниматься вы чем планируете? С натуризмом Оливии даже боюсь представить..."
    Max_01 "Мы может ТВ посмотрим или в бассейне поплаваем. Может в комнате поиграем."
    Ann_14 "Ох, вот насчёт бассейна я сильно сомневаюсь. Придётся не ложиться спать и караулить, как бы чего не произошло..."
    Max_08 "Мам, я же сказал, я за ними присмотрю. К тому же, хоть Оливия и натуристка, но во всём остальном она девочка целомудренная. Днём ты же нас не караулишь."
    Ann_12 "Одно дело днём, Макс, и совсем другое - ночью... Ох, не знаю..." nointeract
    menu:
        "Ну пожалуйста! Всё будет хорошо." ('soc', mgg.social * .7, 90):   # (убеждение)
            pass
    if rand_result:
        # (Убеждение удалось!)
        Ann_14 "[succes!t]Вроде и запретить вам хочу, но не известно, как на это может Лиза отреагировать. Ещё начнёт в отместку из дома убегать..."
        jump .succes
    else:
        # (Убеждение не удалось!)
        $ lisa.flags.showdown_e = 4     # поговорил о ночёвке Оливии, но убедить Анну не удалось
        $ ann.dcv.special.set_lost(3)
        Ann_17 "[failed!t]Извини, Макс, но мне нужно подумать. Мне кажется, я вся изведусь, зная, что вы там ночью у бассейна играете."
        Max_09 "Ладно, подумай пару дней." nointeract
        # продолжение во 2-ом разговоре
        jump .end

    label .succes:
        # продолжение
        $ spent_time += 10
        $ lisa.flags.showdown_e = 5     # Анна разрешила ночные посиделки с Оливией
        Max_10 "Ну да, это ещё хуже."
        Ann_12 "Но меня здесь смущает даже больше не Оливия со своим натуризмом, а то, как ты на это реагируешь. Ладно она к этому у себя дома привыкла. А Лиза?"
        Max_09 "А что Лиза? Ты вспомни, чему вы с Эриком её учили..."
        Ann_15 "Ой! Лучше не напоминай, Макс. Что я тогда творила, ужас..."
        Max_07 "Вот-вот. Лизу теперь это тоже, как и Оливию, совершенно не смущает."
        Ann_14 "Видимо, из-за Эрика я стала слишком подозрительной. Пытаюсь снова уберечь Лизу от всего на свете. Хотя, прямо перед этим, сама же такое ей показывала..."
        Max_09 "И вспомни, кто вывел Эрика на чистую воду? Я! И я же тебе говорю, что присмотрю за Лизой и Оливией."
        Ann_17 "Хорошо, я разрешу вам собираться по ночам, но! Если мне будет слишком неспокойно, я могу взять и проверить, чем вы занимаетесь."
        Max_01 "Не проблема, мам. Приходи в любое время."
        Ann_04 "Договорились. Ведите себя хорошо." nointeract

    menu .end:
        "{i}уйти{/i}":
            jump Waiting


# второй разговор о ночёвке Оливии, если в первый раз не удалось убедить (через 3 дня)
label ann_about_olivia1:
    # "Мам, ты подумала об Оливии?"
    Ann_14 "Подумала... Вроде и запретить вам хочу, но не известно, как на это может Лиза отреагировать. Ещё начнёт в отместку из дома убегать..."
    jump ann_about_olivia0.succes
