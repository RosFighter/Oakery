
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
        "Ну, могу заказать продукты" if dcv.buyfood.done  and dcv.buyfood.stage in [0, 2]:
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
            $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
            Ann_05 "Да вот, по кабельному какой-то фильм сейчас начнётся..."
            scene BG tv-watch-01
            show tv 00 at tv_screen
            show Ann tv-watch 01a
            $ renpy.show('Max tv-watch 01'+mgg.dress)
            Max_02 "{i}( Мама так близко... В одном полотенце... Даже не знаю о чём фильм, о нём я думать точно не могу... ){/i}"
            scene BG lounge-tv-01
            $ renpy.show("Ann tv-closer "+pose3_3+'a')
            $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
            menu:
                Ann_05 "Ну что, отличный фильм, как мне кажется! А тебе понравилось, Макс?"
                "Да, очень!":
                    $ __mood = 50
                    Ann_07 "Ну я рада. Ладно, спасибо что посидел со мной. Пойду в свою комнату, хватит фильмов на сегодня..."
                    Max_04 "Ага, давай..."
                "Почти также, как сидеть рядом с тобой...":
                    $ __mood = 40
                    Ann_12 "Что, прости? Не поняла..."
                    Max_00 "Не бери в голову, это я так, пошутил неудачно..."
                    Ann_05 "Ясно. Ну, спасибо за компанию. Пойду в свою комнату, хватит с меня фильмов на сегодня..."
                    Max_03 "Ага, хорошо посидели..."
            $ spent_time = max((60 - int(tm[-2:])), 40)
            $ AddRelMood('ann', 0, __mood)
            $ cur_ratio = 0.5
        "В другой раз...":
            menu:
                Ann_05 "Как хочешь, дорогой. А я что-нибудь посмотрю..."
                "Не буду тебе мешать...":
                    pass
    jump Waiting

    label .first_movie:
        ## "Что смотришь?"
        menu:
            Ann_01 "Да так, всякую ерунду. Хотела какой-нибудь фильм посмотреть. Садись рядом, если тоже делать нечего..."
            "Конечно! Что смотреть будем?":
                $ ann.flags.erofilms += 1
                $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
            "В другой раз...":
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
        "Да это же эротика!":
            jump .ero
        "Да, слышал кое-что о нём...":
            menu:
                Ann_02 "Да? И что ты о нём слышал? Хороший фильм? Стоит смотреть?"
                "Да, отзывы отличные":
                    menu:
                        Ann_05 "Ну, раз отзывы хорошие, тогда, давай смотреть!"
                        "{i}начать просмотр{/i}":
                            jump .start
                "Ну, это эротика...":
                    jump .ero
    menu .ero:
        Ann_13 "Правда?! Ой, Макс, извини, я не знала. Тогда, нам с тобой его точно смотреть вместе не следует. А подруге я всё скажу, за то, что не предупредила..."
        "Да всё в порядке, я уже взрослый!":
            Ann_01 "Нет, Макс. Не в этот раз. Я лучше посмотрю новости или какой-нибудь сериал... Извини, что тебя обнадёжила..."
            Max_01 "Ладно, не буду мешать..."
        "Ну, как скажешь. Я тогда пойду...":
            pass
    jump Waiting

    label .start:
        scene BG tv-watch-01
        show tv ews 01 at tv_screen
        show Ann tv-watch 01a
        $ renpy.show('Max tv-watch 01'+mgg.dress)
    Max_01 "{i}( Интересно, мама хотя бы подозревает, что это эротика?... Посмотрим... ){/i}"
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
    $ renpy.show("Ann tv-closer "+pose3_3+'a')
    $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
    Ann_05 "Жаль, что мы редко с тобой вместе вот так сидим, что-то смотрим. Ну, надеюсь, начало традиции положено. И пусть в следующий раз будет нечто менее... волнующее..."
    Max_01 "Конечно, мам!"
    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ AddRelMood('ann', 10, 100)
    $ SetCamsGrow(house[4], 180)
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
        "Да это просто Алиса курила!":
            show Max talk-terrace 02a
            $ renpy.show("Ann talk-terrace 02"+ann.dress)
            jump .smoke
    menu:
        Ann_00 "Точно? Макс, ты ничего не хочешь рассказать?"
        "Нет, мам, нечего рассказывать":
            Ann_01 "Да? Ну, может и правда показалось. Или от соседей надуло... Ладно, давайте ужинать..."
            $ poss['smoke'].open(2)
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

        "Вообще-то, Алиса курила...":
            show Max talk-terrace 02a
            $ renpy.show("Ann talk-terrace 02"+ann.dress)
            jump .smoke

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

    menu .smoke:
        Ann_13 "Что?! Ты уверен?"
        "Да, но ей не говори, что это я её сдал!":
            show Max talk-terrace 01a
        "Абсолютно. Сам видел. Днём курила у бассейна!":
            show Max talk-terrace 03a
        "Может быть, мне показалось...":
            pass
    $ poss['smoke'].open(1)
    menu:
        Ann_20 "Алиса! Иди сюда, бегом!"
        "Мам, ну не так же...":
            pass
        "Мам, меня не сдавай...":
            pass
    show Alice talk-terrace 01a
    Alice_13 "Что случилось, мам?"
    Ann_19 "Что случилось?! Не притворяйся тут невинной овечкой! Макс говорит, что видел, как ты курила!"
    show Max talk-terrace 02a
    Max_14 "Ну..."

    if alice.req.req == 'money':
        $ __mood -= 300
        Alice_17 "Ну и придурок же ты, Макс! Мы же договорились, а ты..."
        Max_09 "Я передумал..."
    else:
        $ __mood -= 200
        Alice_17 "Ну и придурок же ты, Макс! Стукач!"
        Max_09 "Сама виновата..."

    Ann_12 "Так, всё, Алиса, сейчас я тебя накажу! Снимай свои джинсы!"
    scene BG punish-evening 01
    show Alice punish-evening 01a
    $ renpy.show("Ann punish-evening 01"+ann.dress)
    Max_07 "Ого..."
    Alice_12 "Что?! Я уже взрослая! Могу делать что хочу, даже курить!"
    Max_08 "Ой, плохой ответ..."
    Ann_19 "Взрослая? С каких пор? Пока ты живёшь со мной под одной крышей, ты моя дочь! Без разговоров, быстро снимай и ложись на мои колени!"
    show Alice punish-evening 02a
    Alice_13 "Мам, но тут же Макс... Что, прямо при нём будешь? Пусть он уйдёт!"
    Ann_18 "Нет, Алиса, пусть смотрит. Это ждёт любого, кто меня разозлит. Быстро ложись на мои колени, кому сказала!"
    scene BG punish-evening 02
    $ renpy.show("Ann punish-evening alice-01"+ann.dress)
    Alice_13 "Ладно... Только не больно, чтобы, ладно? Ай! Ма-ам!"
    Ann_16 "Давай не мамкай тут! Ты знаешь, что я ненавижу сигареты и мои дети точно курить не будут. Особенно, в моём доме, ясно?!"
    $ renpy.show("Ann punish-evening alice-02"+ann.dress)
    Alice_13 "Да, ясно, мам... Ай! Я всё поняла! Я больше не буду!"
    scene BG punish-evening 01
    show Alice punish-evening 03a
    $ renpy.show("Ann punish-evening 01"+ann.dress)
    Ann_12 "Очень на это надеюсь. Так, теперь надевай штаны и садимся ужинать."
    scene BG talk-terrace-00
    show Max talk-terrace 01a
    show Alice talk-terrace 03a
    menu:
        Alice_17 "Ну ты и гад, Макс. Доволен? Ну теперь держись..."
        "Извини, я не хотел, чтобы так...":
            show Max talk-terrace 03a
            $ __mood += 50
            menu:
                Alice_16 "Не хочу тебя больше видеть. Жаль, что придётся..."
                "{i}начать ужин{/i}":
                    pass
        "И что ты сделаешь? Я тебя не боюсь!":
            show Max talk-terrace 04a
            menu:
                Alice_16 "Я не буду тебе ничего говорить, сам всё поймёшь в своё время. Карма штука жестокая, но справедливая..."
                "{i}начать ужин{/i}":
                    pass
    call set_alice_cant_smoke from _call_set_alice_cant_smoke   # теперь Алиса не будет курить на вилле
    $ AddRelMood('alice', -10, __mood)
    $ current_room = house[5]
    $ Distribution()
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

    $ ann.dcv.feature.stage += 1    # 2
    $ spent_time += 10
    jump Waiting


label ann_yoga_with_max0:       # первая совместная йога
    # стартовая фраза  "С тобой можно?"
    $ ann.dcv.feature.set_lost(1)   # следующая попытка на следующий день

    #если Анна заметила, что Макс подглядывает за ней в душе перед йогой и убеждение не удалось
    if (punreason[3] or punreason[2]):
        jump yoga_after_peeping

    $ ann.dcv.feature.stage += 1    # 5

    #если Макс не был замечен за подглядыванием в душе перед йогой или вовсе не подглядывал (или его заметили, но убеждение удалось)
    Ann_05 "Ты решил заняться йогой? Вот это да, Макс! Не ожидала! Но я буду рада твоей компании... Прямо сейчас планируешь начать?"
    Max_01 "Не совсем. Мы просто очень мало времени вместе проводим, вот я и решил присоединиться."
    Ann_14 "Да, знаю сынок. Я бы и сама хотела проводить со всеми вами больше времени..."
    Max_03 "Знаешь, я бы сначала просто посмотрел, что ты делаешь. Ну и может, помог чем. Расскажешь мне об этой йоге?"

    #yoga-01 + yoga-01-ann-01 + yoga-01-max-(01a/01b)
    scene BG char Ann yoga 01
    show Ann yoga 01-01a
    $ renpy.show('Max yoga 01'+mgg.dress)
    Ann_04 "Вообще-то не очень удобно, выполнять упражнения и одновременно говорить. Но так уж и быть, сегодня я сделаю исключение."
    Max_07 "Тебе не больно так делать?"
    Ann_06 "Когда-то было, когда я только начинала это осваивать. Когда Алиса появилась на свет... Ох, как это было давно!"
    Max_09 "Так в чём суть?"

    #yoga-02 + yoga-02-max-(01a/01b) + yoga-02-ann-01
    scene BG char Ann yoga 02
    $ renpy.show('Max yoga 02'+mgg.dress)
    show Ann yoga 02-01a
    Ann_07 "Ну, для начала, то что я делаю нельзя назвать йогой. Это скорее растяжка, в которой есть некоторые позы из упражнений по йоге."
    Max_04 "Для укрепления здоровья?"
    Ann_08 "Да. Здесь тебе и развитие гибкости, и оздоровление организма в целом, а так же выносливость и умиротворение. В моём возрасте это всё имеет очень важное значение, сынок."
    Max_05 "Да ты выглядишь получше многих старшеклассниц, мам!"
    Ann_05 "Спасибо, Макс! Приятно такое слышать. Значит, я не зря этим занимаюсь и это работает..."
    Max_02 "Ещё как работает! Может, я чем-то могу помочь?"

    #yoga-03 + yoga-03-max-(01a/01b)-ann-01
    scene BG char Ann yoga 03
    $ renpy.show('Ann yoga 03-01a'+mgg.dress)
    Ann_02 "Тебе со стороны должно быть хорошо видно, всё ли я делаю правильно. У меня должна быть прямая спина и прямые ноги..."
    Max_01 "Ну да, почти. Разве что, ножки держи попрямее. Я тебя немножко придержу, чтобы ты лучше чувствовала, правильно ли всё делаешь..."
    Ann_06 "Ага, я поняла... Здесь важно правильно выстроить позу и просто дышать, стараясь максимально расслабиться."
    Max_09 "Сложно представить, что в таком положении можно расслабиться!"
    Ann_07 "Это приходит со временем, Макс. Сам-то попробовать не хочешь?"
    Max_07 "Пока что нет. Я лучше за тобой понаблюдаю и знаний наберусь сперва."

    #yoga-04 + yoga-04-max-(01a/01b)-ann-01
    scene BG char Ann yoga 04
    $ renpy.show('Ann yoga 04-01a'+mgg.dress)
    Ann_04 "Слегка придержи меня, чтобы я равновесие нашла... Только совсем легонько."
    Max_03 "Конечно. А ты на шпагат садишься?"
    Ann_13 "Ох, сынок, давно не пробовала. Честно говоря, побаиваюсь. Возраст всё-таки..."
    Max_04 "По-моему ты очень гибкая! Выглядишь прекрасно! И не важно сколько тебе лет, главное - на сколько ты себя чувствуешь."
    Ann_08 "Ой, ну всё, засмущал маму своими комплиментами. Пора заканчивать..."
    Max_05 "Хорошего понемножку, да?"

    #yoga-05 + yoga-05-ann-00 + yoga-05-max-(00a/00b)
    scene BG char Ann yoga 05
    show Ann yoga 05a
    $ renpy.show('Max yoga 05'+mgg.dress)
    Ann_05 "Именно так, Макс. Спасибо за компанию, вместе куда веселее... Буду только рада, если решишь снова присоединиться ко мне."
    menu:
        Max_01 "Хорошо, мам. Это я с радостью!"
        "{i}уйти{/i}":
            pass
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

    #если Анна заметила, что Макс подглядывает за ней в душе перед йогой и убеждение не удалось
    if (punreason[3] or punreason[2]):
        jump yoga_after_peeping

    menu:
        Ann_05 "Конечно, Макс, зачем спрашиваешь... Если ты ещё не созрел проверить свою гибкость, то просто смотри и помогай, если я попрошу. Ну и запоминай, что я делаю..."
        "Тебе не жарко, мам?" if ann.flags.help == 4:
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
            #открывается возможность купить новую одежду для йоги
        "Продолжай, мам. Я весь во внимании...":
            pass

    #yoga-01 + yoga-01-ann-(01/01a или 02/02a или 03/03a) + yoga-01-max-(01a/01b)
    scene BG char Ann yoga 01
    $ renpy.show('Ann yoga 01-0'+str(renpy.random.randint(1, 3))+ann.dress)
    $ renpy.show('Max yoga 01'+mgg.dress)
    Ann_02 "Я рада, что хоть так мы успеваем побыть вместе... Какие у тебя планы на день? Надеюсь, не за компьютером будешь всё время сидеть..."
    Max_04 "Ага... Класс..."
    Ann_12 "Это в смысле - да, будешь сидеть?"
    Max_03 "А, что? Я просто засмотрелся и немного прослушал, что ты говорила..."

    #yoga-02 + yoga-02-ann-(01/01a или 02/02a или 03/03a) + yoga-02-max-(01a/01b)
    scene BG char Ann yoga 02
    $ renpy.show('Max yoga 02'+mgg.dress)
    $ renpy.show('Ann yoga 02-0'+str(renpy.random.randint(1, 3))+ann.dress)
    Ann_04 "Макс, будь повнимательнее... Я ведь хочу, чтобы ты хоть чему-то научился от меня."
    Max_02 "О, мам, поверь, я сейчас очень внимателен!"
    Ann_06 "Тогда подержишь меня немножко, чтобы я всё правильно сделала?"
    Max_01 "Да, мам. Сейчас..."

    #yoga-03 + yoga-03-max-(a/b)-ann-(01/01a или 02/02a или 03/03a)
    scene BG char Ann yoga 03
    $ renpy.show('Ann yoga 03-0'+str(renpy.random.randint(1, 3))+ann.dress+mgg.dress)
    Max_05 "{i}( Она такая гибкая! Главное всё не испортить, хотя, как же хочется прикоснуться ко всему, что я перед собой сейчас вижу... Мама у меня конфетка! ){/i}"
    Ann_08 "Макс, ты чего молчишь? Это мне говорить не очень удобно, потому что я стараюсь расслабиться и сосредоточиться на дыхании..."
    Max_03 "Да что тут скажешь, красота да и только!"

    #yoga-04 + yoga-04-max-(a/b)-ann-(01/01a или 02/02a) или yoga-05 + yoga-05-max-(a/b)-ann-(03/03a)
    if renpy.random.randint(0, 1):
        scene BG char Ann yoga 04
        $ renpy.show('Ann yoga 04-0'+str(renpy.random.randint(1, 2))+ann.dress+mgg.dress)
    else:
        scene BG char Ann yoga 05
        $ renpy.show('Ann yoga 05-03'+ann.dress+mgg.dress)
    Ann_07 "Приятно каждый раз от тебя слышать, что я не зря этим занимаюсь... Это прекрасно мотивирует."
    Max_04 "Тебе явно эти занятия идут только на пользу. А чувствуешь себя как?"
    Ann_06 "Немного устала, но в целом, мне хорошо. Появляется такое ощущение... лёгкости..."
    Max_05 "Здорово, мам! Ещё немного потянись и будет идеально..."
    Ann_14 "Главное - не перенапрячься с утра пораньше... А то буду еле живая на работе..."

    #yoga-05 + yoga-05-ann-(00/00a) + yoga-05-max-(00a/00b)
    scene BG char Ann yoga 05
    $ renpy.show('Ann yoga 05'+ann.dress)
    $ renpy.show('Max yoga 05'+mgg.dress)
    Ann_04 "Фух... На этом, пожалуй, закончим. Спасибо, что составил компанию. Буду только рада, если решишь снова присоединиться ко мне."
    menu:
        Max_01 "С радостью, мам! Обязательно..."
        "{i}уйти{/i}":
            pass

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
    Max_07 "{i}( Надеюсь, она не станет возмущаться, насколько там всё коротенькое в одежде... С другой стороны, эта одежда не короче её бикини. ){/i}"
    Ann "{b}Анна:{/b} Сынок, с размером всё в порядке. Вроде, сидит отлично. Только вот..."

    #annroom-morning-01 + ann-dresses-morning-05b
    scene BG char Ann morning
    show Ann dressed 05b
    Max_06 "Ого, мам! Тебе очень идёт! Выглядишь обалденно! Удобно?"
    Ann_14 "Да, Макс, удобно... Просто... Не слишком ли всё открыто?"
    Max_07 "Так, а где что открыто? Главное, чтобы было легко и комфортно. Тут такое солнце, даже ранним утром, что эта одежда - идеальный вариант."
    Ann_02 "Не могу не согласиться. Ладно, посмотрим, удобно ли будет в этой одежде заниматься..."
    Max_04 "Я уверен, что будет..."
    Ann_05 "Спасибо, что делаешь маме приятно... Иди ко мне, я тебя обниму, как следует..."
    #annroom-morning-01 + (hugging-annroom-01-max-(01a/01b)-ann-01b или hugging-annroom-02-max-(01a/01b)-ann-01b)
    $ renpy.show('Ann hugging morning-annroom 0'+str(renpy.random.randint(1, 2))+'-1c'+mgg.dress)
    Max_05 "{i}( О да... У мамы такое потрясающее тело! Так приятно прижиматься к ней... её упругой груди... Что точно хорошо в новой одежде, так это то, что мне прекрасно видны очертания её сосочков через эту тонкую ткань! ){/i}"
    #annroom-morning-01 + (hugging-annroom-01-max-(02a/02b)-ann-02b или hugging-annroom-02-max-(02a/02b)-ann-02b)
    $ renpy.show('Ann hugging morning-annroom 0'+str(renpy.random.randint(1, 2))+'-2c'+mgg.dress)
    menu:
        Ann_04 "Ну всё, мой дорогой, не будем же мы так часами стоять обниматься, пора делами заняться..."
        "Давай ещё?! Ты такая классная!":
            Ann_05 "Ты сегодня очень мил, Макс! За это я тебя даже в щёчку поцелую, чтобы ты почаще старался меня радовать..."
            #annroom-morning-01 + (hugging-annroom-01-max-(03a/03b)-ann-03b или hugging-annroom-02-max-(03a/03b)-ann-03b)
            $ renpy.show('Ann hugging morning-annroom 0'+str(renpy.random.randint(1, 2))+'-3c'+mgg.dress)
            Max_06 "{i}( Ухх, а как хочется притянуть маму к себе за её аппетитную и подтянутую попку... Ммм... Вот это было бы очень сладко! ){/i}"
            menu:
                Ann_04 "Ну вот, дорогой. Теперь, давай заниматься своими делами..."
                "Хорошо... Я тебя люблю, мам!":
                    Ann_07 "И я тебя, Макс..."
                "Конечно, мам! Не скучай...":
                    Ann_02 "Спасибо, сынок! И ты тоже..."
        "Конечно, мам! Не скучай...":
            Ann_02 "Спасибо, сынок! И ты тоже..."

    $ items['fit1'].give()
    $ ann.gifts.append('fit1')
    $ setting_clothes_by_conditions()
    $ spent_time = 30
    jump Waiting
