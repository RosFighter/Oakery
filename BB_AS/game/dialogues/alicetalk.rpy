label AliceTalkStart:

    $ dial = TalkMenuItems()

    $ __cur_plan = alice.get_plan()

    if __cur_plan.name == 'tv' and alice.daily.mistress == 1:
        #начиная с этого момента, если Макс отбыл наказание у Алисы в комнате, то отправляясь в гостиную, если Алиса смотрит ТВ, Макс не сможет составить ей компанию
        #ракурс с экраном ТВ и смотрящей на него Алисой
        if alice.daily.drink:
            # при наказании удалось дать конфету с ликёром
            Max_07 "{m}Алиса сейчас как раз должна отходить от конфеты с ликёром, так что лучше оставить её на сегодня в покое...{/m}"
        else:
            # при наказании не удалось дать конфету с ликёром
            Max_09 "{m}Впечатлений от времяпрепровождения с Алисой мне и в её комнате хватило. Сегодня к ней лучше больше не лезть...{/m}"
        $ alice.daily.mistress = 2
        jump Waiting
    elif __cur_plan.name == 'tv' and alice.daily.mistress:
        jump Waiting

    if __cur_plan.talklabel is not None:
        call expression __cur_plan.talklabel from _call_expression_1

    if len(dial) > 0:
        $ dial.append((_("{i}уйти{/i}"), "exit"))
    else:
        jump Waiting

    $ renpy.block_rollback()

    if flags.eric_wallet == 2:
        if not alice.flags.talkblock:
            jump alice_about_wallet
        else:
            menu:
                Alice_17 "Тебя выпнуть, Макс, или сам отвалишь?"
                "{i}уйти{/i}":
                    $ alice.hourly.talkblock = 1
                    jump AfterWaiting

    Alice_00 "Ну, Макс, чего надо?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        $ __mood = alice.GetMood()[0]
        if rez in gifts['alice']:
            if renpy.has_label(rez.label):
                call expression rez.label from _call_expression_2
        elif __mood < talks[rez].mood:
            if __mood < -2: # Настроение -4... -3, т.е. всё ну совсем плохо
                jump Alice_badbadmood
            elif __mood < 0: # Настроение -2... -1, т.е. всё ещё всё очень плохо
                jump Alice_badmood
            else: # Настроение хорошее, но ещё недостаточное для разговора
                jump Alice_normalmood
        elif talks[rez].kd_id != "" and talks[rez].kd_id in cooldown and not ItsTime(cooldown[talks[rez].kd_id]):
            jump Alice_cooldown
        elif renpy.has_label(talks[rez].label): # если такая метка сушествует, запускаем ее
            call expression talks[rez].label from _call_expression_3
        jump AliceTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump Waiting            # если же выбрано "уйти", уходим в после ожидания


label Alice_badbadmood:
    menu:
        Alice_09 "Да пошёл ты! Не хочу тебя видеть даже!"
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Alice_asksorry


label Alice_badmood:
    menu:
        Alice_09 "Макс, отвали! Я не хочу с тобой разговаривать."
        "Ок...":
            jump Waiting
        "Я хотел извиниться":
            jump Alice_asksorry


label Alice_asksorry:
    menu:
        Alice_13 "Хотел извиниться? Каким образом?"
        "Ты знаешь, я передумал...":
            jump Waiting


label Alice_normalmood:
    menu:
        Alice_09 "Макс, давай не сейчас..."
        "Ок...":
            jump Waiting


label Alice_cooldown:
    Alice_09 "Макс... Не сейчас."
    Max_00 "Ладно..."
    jump AfterWaiting


label wash_dishes_alice:
    $ alice.daily.dishes = 1
    menu:
        Alice_13 "Хочешь о посуде поговорить или пришёл помочь?"
        "Давай, я домою остальное":
            menu:
                Alice_07 "Что это с тобой? Но я не откажусь. И... спасибо."
                "{i}мыть посуду{/i}":
                    $ AddRelMood('alice', 10, 60, 2)
                    $ dishes_washed = True
                    $ spent_time = max((60 - int(tm[-2:])), 30)
                    scene BG crockery-morning-00
                    $ renpy.show("Max crockery-morning 01"+mgg.dress)
                    menu:
                        Max_11 "{m}И почему здесь нет посудомоечной машины...{/m}"
                        "{i}закончить{/i}":
                            $ cur_ratio = 2
                            jump Waiting
        "Нет, просто хотел поглазеть":
            menu:
                Alice_09 "Знаешь что, вали отсюда, пока мокрой тряпкой по голове не получил!"
                "{i}уйти{/i}":
                    $ spent_time = 10
                    jump Waiting


label talkblog1:
    if "blog" in cooldown:
        if ItsTime(cooldown['blog']): # кулдаун прошел, можно поговорить
            $ del cooldown['blog']
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
                                Alice_01 "Да у других таких же блогеров подсмотрела, конечно. Все так делают! Ну и сама в интернете разное читаю, изучаю..." # Alice_02
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
                    $ cooldown['blog'] = CooldownTime("03:00")
                    Alice_09 "Знаешь что, Макс, отвали!"
                    Max_00 "Ну и ладно..."
                    $ AddRelMood('alice', -5, -50)
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
        Alice_01 "Ты у нас внезапно стал миллионером? Или просто деньги появились? Самый простой способ - это купить недостающее. Ну, или найти то, что пропало" # Alice_07
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
        $ alice.flags.crush = 2
        menu:
            Alice_14 "Вместе? Ещё ничего нет, а уже в партнёры набиваешься?"
            "Ну если придумаю что-то, то почему нет?":
                Alice_01 "Ну, если придумаешь. Если. Да и смотря что... Сильно удаляться от этой темы не хочется. Но попробовать что-то новое можно... В общем, когда что-то придумаешь, тогда и поговорим..." # Alice_07
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
        $ alice.flags.crush = 2
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
        $ spent_time = 10
        jump Waiting


# === просмотр ТВ с Алисой ===
# стартовый диалог при просмотре ТВ
label alice_talk_tv:
    if _in_replay:
        call alice_tv_closer from _call_alice_tv_closer
    else:
        if 'alice_talk_tv' not in persistent.memories:
            $ persistent.memories['alice_talk_tv'] = 0
        if not alice.dcv.mistress.done:
            Alice_12 "Вот так вот просто? Как будто утром было всё так, как должно быть! Где извинения, Макс?!"
            Max_07 "Извини, я больше так не буду."
            jump alice_mistress_0

    Alice_00 "Нет, садись. Тут места много..."
    $ alice.daily.tvwatch = 1
    $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
    Max_00 "Хорошо. Что смотришь?"
    $ SetCamsGrow(house[4], 110)
    menu:
        Alice_13 "Да так, всякую ерунду. Я просто отдыхаю, и мне без разницы, что смотреть. Поэтому смотрю всё подряд..."
        "Ну, давай смотреть всё подряд..." if not _in_replay:
            Max_11 "{m}По телику сегодня нет ничего интересного... Ни порнушки, ни даже эротики... А было бы забавно посмотреть такое с сестрёнкой...{/m}"
            Max_00 "Ладно, пойду я..."
            jump alice_talk_tv_end

        "Тебе сделать массаж ног?" if _in_replay or all([not alice.daily.massage, learned_foot_massage()]):
            $ alice.daily.drink = 0
            jump alice_tv_massage_starter

# окончание просмотра ТВ
label alice_talk_tv_end:
    $ renpy.end_replay()
    $ alice.daily.drink = 0
    $ spent_time = max((60 - int(tm[-2:])), 40)
    $ AddRelMood('alice', 0, 50)
    $ cur_ratio = 0.5
    jump Waiting

# реакция на предложение массажа и первый выбор пути (трезвый/пьяный)
label alice_tv_massage_starter:

    $ renpy.show("Max tv-closer 04"+mgg.dress)
    $ alice.daily.massage = 1

    if alice.flags.m_foot > 6:
        # было больше 5 успешных массажей, убеждать больше не нужно
        menu:
            Alice_07 "Дай-ка подумаю... Да! Я готова..."
            "Хорошо {i}(начать массаж){/i}" if not _in_replay:
                jump alice_talk_tv_massage      # трезвый массаж

            "Может конфетку перед массажем?" if kol_choco or _in_replay:  ### если Макс знает о слабости Алисы
                jump alice_talk_tv_choco        # попытка предложить конфету

    if alice.flags.m_foot == 0:
        # Первая беседа о массаже
        Alice_02 "Что-то новенькое... А ты умеешь?"
        Max_01 "Само собой!"
        Alice_01 "Могу я спросить откуда? Раньше ты, вроде бы, не умел. Да и не представляю, где бы ты мог этому научиться..."
        Max_02 "Онлайн-курсы!"
        menu:
            Alice_02 "Очень смешно, Макс. Разве можно научиться массажу через ютуб?"
            "Почему ютуб? Это платные курсы...":
                Alice_01 "А, ну если ты им ещё и заплатил, то это всё меняет!" nointeract

            "Конечно! Я же научился...":
                Alice_01 "Что-то я очень сомневаюсь, Макс..." nointeract

        menu:
            "Так тебе продемонстрировать или как?" ('soc', mgg.social * 4, 90):
                $ alice.flags.m_foot = 1

    else:
        menu:
            Alice_02 "Ну, не знаю, не знаю..."
            "Тебе понравится!"  ('soc', mgg.social * 4, 90):
                pass

    if not rand_result: ###Убеждение не удалось
        Alice_02 "[failed!t]Нет, Макс, в другой раз. Что-то я сомневаюсь. Вдруг, ты мне что-то сломаешь... Нет, спасибо."
        Max_08 "Ну, как хочешь... Не буду тебе мешать..."
        jump alice_talk_tv_end

    ### Убеждение удалось
    if not _in_replay:
        $ poss['naughty'].open(0)

    Alice_03 "[succes!t]Ну, давай. Только я очень привередлива в вопросах массажа. Если сделаешь что-то не так, сразу закончим." nointeract

    menu:
        "Хорошо {i}(начать массаж){/i}":
            jump alice_talk_tv_massage      # трезвый массаж

        "Может конфетку перед массажем?" if kol_choco:  ### если Макс знает о слабости Алисы
            jump alice_talk_tv_choco        # попытка предложить конфету

# попытка предложить конфету
label alice_talk_tv_choco:
    if alice.flags.hip_mass > 4:    # был "расширенный" трезвый массаж ног
        menu:
            Alice_02 "Как же без неё. Но только одну... Вкусно... Теперь я готова, начинай массаж!"
            "Хорошо {i}(начать массаж){/i}":
                $ give_choco()
                $ alice.daily.drink = 1
                jump alice_talk_tv_massage      # попытка успешная, массаж с конфетой

    if alice.dcv.seduce.done:
        menu:
            Alice_02 "У меня такое чувство, что ты чего-то от меня хочешь... Но не сознаешься ведь?"
            "Хочу тебя!" if not _in_replay:
                menu:
                    Alice_15 "Макс! Вали нахрен отсюда со своими шуточками. Дай спокойно телевизор посмотреть!"
                    "{i}уйти{/i}":
                        jump alice_talk_tv_end

            "Просто я такой хороший парень!":
                Alice_05 "Угу... Точно! Извини, а где мой брат Макс?"
                Max_01 "Очень смешно. Так ты хочешь конфеты?"

            "Ты узнаешь... В своё время...":
                Alice_02 "Звучит очень зловеще... И что же я узнаю, интересно? Ах да. Это же секрет... Самому не смешно?"
                Max_01 "Да, да, очень! Так ты хочешь конфеты?"

    menu:
        Alice_13 "Честно говоря, не знаю. Конфеты я люблю, но не хочу портить фигуру..."
        "От конфетки не поправишься!"  ('soc', mgg.social * 3, 90):
            if rand_result:
                ## Алиса съела конфетку
                $ give_choco()
                if not _in_replay:
                    $ poss['naughty'].open(2)
                $ alice.dcv.seduce.set_lost(3)
                $ alice.daily.drink = 1
                menu:   ### Убеждение удалось
                    Alice_07 "[succes!t]Эх.. Уболтал, чертяка языкастый! Давай сюда конфетку. Но только одну... Вкусно... Теперь я готова, начинай массаж!"
                    "Ну, хорошо {i}(начать массаж){/i}":
                        jump alice_talk_tv_massage      # попытка успешная, массаж с конфетой

            else:
                $ alice.dcv.seduce.set_lost(2)
                menu:   ###Убеждение не удалось
                    Alice_01 "[failed!t]Нет, Макс. Спасибо, конечно, но рисковать я не буду. Ну так что, массаж делать будешь или забыл, что собирался?"
                    "Ну, хорошо {i}(начать массаж){/i}":
                        jump alice_talk_tv_massage      # попытка провалилась, трезвый массаж

# первый этап массажа
label alice_talk_tv_massage:
    $ var_pose = {'01':'01', '03':'02', '02':renpy.random.choice(['01','02'])}[pose3_2]
    ### сцена массажа 01 или 02
    scene BG tv-mass-01
    $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+alice.dress)
    show screen Cookies_Button
    menu:
        Max_03 "{m}Какая у Алисы нежная кожа... Интересно, о чём она сейчас думает?{/m}"
        "{i}продолжить{/i}" ('mass', mgg.massage * (10 if alice.daily.drink else 7)):   # с конфетой шанс успеха чуть-чуть выше
            hide screen Cookies_Button
    if rand_result:  ### {i}Алисе понравился массаж!{/i}
        $ alice.flags.m_foot += 1
        # var_pose - 01/02
        $ var_pose = get_pose({'01':'03', '02':'04'}, var_pose)
        scene BG tv-mass-03
        $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+alice.dress)
        Alice_04 "[alice_good_mass!t]А ты неплох сегодня в этом деле... Хорошо, что ты никакой не работяга. Руки у тебя нежные. Приятно очень..." nointeract
        jump alice_talk_tv_choice_mass

    else:
        menu: ### {i}Алисе не понравился массаж!{/i}
            Alice_12 "[alice_bad_mass!t]Ой, Макс, больно! Не надо так. Ты чуть лодыжку не вывихнул мне... Иди ещё потренируйся там на кошках или в ютубе поучись!"
            "{i}закончить{/i}":
                # if alice.flags.m_foot in range(2, 6):
                    # $ alice.flags.m_foot -= 1
                jump alice_talk_tv_end

# выбор дальнейшего развития массажа (предложить вторую конфету, снять джинсы, продолжить/закончить массаж)
label alice_talk_tv_choice_mass:
    # $ _dress = mgg.dress+alice.dress
    # $ renpy.dynamic('rez', 'dial')

    # вторая конфета нужна, если Макс видел развлечение Алисы через камеру
    # если пройден трезвый путь, достаточно одной конфеты, за исключением джинсов на Алисе // уже не актуально
    # $ can_double_choko = alice.daily.drink and kol_choco>0 and (5 > alice.flags.hip_mass > 0 or alice.dress=='a')
    $ can_double_choko = alice.daily.drink and kol_choco>0 and alice.flags.hip_mass > 0

    menu .create_menu:
        # заполнение пунктов меню
        "Может, ещё конфетку?" ('soc', mgg.social * 3, 90) if can_double_choko:
            $ rez = 'double_drink'

        "Тебе джинсы не мешают?" ('soc', mgg.social * 2, 90) if all([alice.dress=='a', alice.flags.hip_mass < 5]):
            # Алиса в джинсах
            $ rez = 'jeans'

        "Тебе джинсы не мешают?" if all([alice.dress=='a', alice.flags.hip_mass > 4, not alice.daily.drink]):
            # Алиса в джинсах, трезвый fj получен, без конфет
            $ rez = 'jeans'

        "Тебе джинсы не мешают? Может, снять..." if all([alice.dress=='a', alice.flags.hip_mass > 4, alice.daily.drink]):
            # Алиса в джинсах, трезвый fj получен, Алиса под конфетой
            $ rez = 'jeans_off'

        "{i}продолжить{/i}" ('mass', mgg.massage * 10) if all([alice.dress!='a', alice.daily.drink]):
            # всё, кроме джинсов, продолжение массажа с одной конфетой
            $ rez = 'mass'

        "{i}высунуть член{/i}" if all([alice.dress!='a', alice.flags.touched, 5 > alice.flags.hip_mass > 1, not alice.daily.drink]):
            # всё, кроме джинсов, продолжение массажа без конфет, начата ветка "трезвого пути
            $ rez = 'sober'

        "{i}высунуть член{/i}" if all([alice.dress!='a', alice.flags.hip_mass > 4, not alice.daily.drink]):
            # всё, кроме джинсов, продолжение массажа без конфет, трезвый fj получен
            $ rez = 'sober_r'

        "{i}продолжить{/i}" ('soc', mgg.massage * 6) if all([alice.dress!='a', alice.flags.hip_mass < 3, not alice.daily.drink]):
            # всё, кроме джинсов, продолжение массажа без конфет, просто трезвый массаж
            $ rez = 'mass'

        "{i}закончить массаж{/i}" if not _in_replay:
            $ rez = 'end_mass'

    # меню создано
    $ can_double_choko = False

    # обрабатываем результат выбора
    if rez == 'jeans_off':
        # трезвый fj получен, Алиса под конфетой
        # Макс стаскивает джинсы с Алисы
        jump alice_talk_tv_jeans_off

    elif rez == 'mass':
        # второй этап массажа
        jump alice_talk_tv_massage_next

    elif rez == 'sober':
        # трезвый путь
        jump alice_talk_tv_sober_mass

    elif rez == 'sober_r':
        # периодический трезвый fj
        jump alice_talk_tv_sober_mass_r

    elif rez == 'double_drink':
        # предложение второй конфеты
        if rand_result:
            $ alice.daily.drink = 2
            $ give_choco()
            Alice_02 "[succes!t]Макс, ну какой же ты... А, ладно, давай ещё одну... Но это последняя, больше не предлагай, а то пну сам знаешь куда! А эта конфета, кажется, ещё вкуснее той! От них стало так жарко..."
            if alice.dress != 'a':
                # второй этап массажа
                jump alice_talk_tv_massage_next

            Max_01 "Может, тогда тебе стоит снять джинсы? Не будет так жарко..."
            # Макс стаскивает джинсы с Алисы
            jump alice_talk_tv_jeans_off

        else:
            Alice_03 "[failed!t]Нет, мне хватит одной... А то я мигом фигуру испорчу. Лучше продолжай массировать мои ножки..." nointeract
            jump .create_menu   # заново создаём меню выбора вариантов, предложение второй конфеты недоступно

    elif rez == 'jeans':
        if any([rand_result, alice.flags.hip_mass > 4,]):
            # Алиса снимает джинсы
            jump alice_talk_tv_jeans

        else:
            menu:   ### Убеждение не удалось!
                Alice_05 "[failed!t]Это так ты к девушкам подкатываешь, сразу предлагаешь снять штаны?"
                "Э... Я к тебе не подкатываю. Просто, жарко же...":
                    pass
                "Ну у тебя и фантазии, Алиса... Я не подкатываю!":
                    pass
            Alice_01 "Да шучу я. Но джинсы снимать не стану. Даже не надейся. Кстати, ты закончил с массажем? Спасибо большое, можешь идти..."
            Max_00 "Вот так вот..."
            jump alice_talk_tv_end

    else:
        Alice_07 "Как, всё? А мне понравилось... Спасибо, Макс. Вот ты и сделал девушке приятно!"
        Max_07 "Я и не так могу..."
        Alice_05 "Ах ты и не так можешь? Боюсь даже представить, как... Но не буду. И тебе не советую. Так что давай, дуй отсюда!"
        Max_00 "Угу..."
        jump alice_talk_tv_end

# Алиса согласна снять джинсы
label alice_talk_tv_jeans:
    if alice.flags.hip_mass > 4:
        # без убеждения
        if alice.req.result == 'nopants':   # Алиса без трусиков
            Alice_02 "Да, что-то тесновато в них и так жарко... Хотя... Не-е-ет, нет, нет! Не буду снимать я сейчас джинсы. Не дождёшься!" nointeract
        else:
            Alice_04 "Ты знаешь, мешают. И очень жарко. Пожалуй, порадую тебя немного, раз ты так хорошо массаж делаешь..."
    else:
        if alice.req.result == 'nopants':   # Алиса без трусиков
            Alice_02 "[succes!t]Да, что-то тесновато в них и так жарко... Хотя... Не-е-ет, нет, нет! Не буду снимать я сейчас джинсы. Не дождёшься!" nointeract
        else:
            Alice_04 "[succes!t]Ты знаешь, мешают. И очень жарко. Пожалуй, порадую тебя немного, раз ты так хорошо массаж делаешь..."

    ### Убеждение снять джинсы удалось
    if alice.req.result == 'nopants':  # Алиса сейчас без трусиков
        menu:   ### Убеждение удалось (или не требуется), но Алиса без трусов
            "Почему?":
                Alice_01 "Сам догадайся, глупый. Но я намекну: возможно, под джинсами ничего нет. Понял? Всё, а теперь иди отсюда, фантазируй..."
                Max_01 "Ух, пойду тогда... Пофантазирую где-нибудь..."
                jump alice_talk_tv_end

            "Потому-что ты без трусиков?":
                Alice_03 "Сам догадался, или кто подсказал? Ну всё, теперь ты всё обо мне знаешь, иди и фантазируй о чём хочешь..."
                Max_01 "Ладно, пойду пофантазирую где-нибудь..."
                jump alice_talk_tv_end

    else:
        Max_07 "{m}Ого...{/m}"
        ### Алиса без джинсов
        # $ _dress = mgg.dress+'c'
        # var_pose - 03/04
        $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress + 'c')
        if not _in_replay:
            $ poss['naughty'].open(1)
    jump alice_talk_tv_jeans_not_jeans

# Алиса позволяет Максу стянуть с неё джинсы
label alice_talk_tv_jeans_off:
    Alice_04 "Только давай ты снимешь их с меня сам, а то я уже так расслабилась, что двигаться не хочется."
    Max_03 "О, это я с радостью сделаю!"
    Alice_07 "Я немного приподнимусь, чтобы тебе было проще их стянуть..."   #спрайт со стягиванием джинсов

    # var_pose - 03/04
    if alice.req.result == 'nopants':
        $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+alice.dress+'-2')
        Max_06 "О да, это ты классно придумала!"   #если на Алисе нет трусиков

        if all([alice.daily.drink > 1, alice.flags.hip_mass > 4]):
            # получен трезвый fj, Алиса съела две конфеты
            # продолжать массаж без трусиков
            $ alice.dress = 'c'
            jump alice_nopants_massage

    else:
        $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+alice.dress+'-1')
        Max_05 "О да, так гораздо лучше..."   #если на Алисе есть трусики


    Alice_05 "Ты только там сильно не заглядывайся, куда не нужно! Лучше скорее продолжай массаж, пока я не расхотела..."
    if alice.req.result == 'nopants':

        Max_07 "Ну да... точно... я же... это... массаж делал."   #если на Алисе нет трусиков
        menu:
            Alice_03 "Ты чего там так тормозишь? Как будто в трусиках меня никогда не видел..."
            "{i}стянуть джинсы до конца{/i}":
                pass

        $ renpy.show('Alice tv-mass '+var_pose+'-3cn')#+alice.dress)
        $ renpy.show('Max tv-mass '+var_pose+'-3'+mgg.dress)
        Alice_15 "Ой, Макс, я же сегодня без них! Вот чёрт! Чего глазеешь, иди отсюда, ты и так увидел больше положенного..."   #спрайт с прикрыванием
        Max_05 "Ладно, но это было так сногсшибательно, что я аж забыл, как ходить!"
        Alice_18 "Макс!!!"
        Max_04 "Всё, ушёл."

        $ renpy.end_replay()
        $ current_room = house[0]
        jump alice_talk_tv_end

    else:
        Max_02 "Ага, сейчас продолжим..."   #если на Алисе есть трусики
        # Дальше все продолжается, как и в случае, если Алиса сама сняла джинсы.
        # $ _dress = mgg.dress+'c'
        $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+'c')
        jump alice_talk_tv_jeans_not_jeans

# Макс стянул джинсы с Алисы, Алиса без трусов, съела две конфеты (ответвление после получения трезвого fj) продолжается до куни
label alice_nopants_massage:

    menu:
        Alice_05 "Ты только там сильно не заглядывайся, куда не нужно! Я только сейчас поняла, что ты меня подловил со своим уговором не носить трусики. Лучше скорее продолжай массаж, пока я не расхотела..."
        "{i}продолжить массаж{/i}":
            pass

    label .not_nopants:
        pass

    # var_pose - 03/04
    $ var_pose = get_pose({'03':'05', '04':'06'}, var_pose)

    # tv-mass-05 + tv-mass-(05/06)-max-(01a/01b) + tv-mass-(05/06)-alice-01b + tv-mass-(05/06)-alice-01bn
    scene BG tv-mass-05
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + 'c')
    $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
    Alice_07 "Макс... Обожаю то, какие чудеса творят твои руки... Но будь осторожен, высовывая свой член... Мне не должно быть слишком щекотно..."
    Max_02 "Не будет."

    # var_pose - 05/06
    $ var_pose = get_pose({'05':'07', '06':'08'}, var_pose)

    # tv-mass-07 + tv-mass-(07/08)-max-(01a/01b) + tv-mass-(07/08)-alice-01b + tv-mass-(07/08)-alice-01bn
    scene BG tv-mass-07
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + 'c')
    $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
    menu:
        Alice_08 "Ты так в себе уверен, Макс... Ну посмотрим... Просто продолжай массировать мои ножки. Они у меня любят твой твёрдый... настрой."
        "{i}массировать её ноги выше{/i}":
            pass

    # var_pose - 07/08
    $ var_pose = get_pose({'07':'09', '08':'10'}, var_pose)

    # tv-mass-03 + tv-mass-(09/10)-max-(01a/01b) + tv-mass-(09/10)-alice-01b + tv-mass-(09/10)-alice-01bn
    scene BG tv-mass-03
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + 'c')
    $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
    Alice_07 "Да, моим ножкам становится так легко от твоих прикосновений... И они очень тебе благодарны. Чувствуешь, насколько?"
    Max_03 "А как же... Они у тебя шаловливые..."
    menu:
        Alice_04 "Они у меня такие... Любят помассировать кое-что большое и твёрдое..."
        "{i}массировать ещё выше{/i}":
            pass

    # var_pose - 09/10
    $ var_pose = get_pose({'09':'11', '10':'12'}, var_pose)

    # tv-mass-11 + tv-mass-(11/12)-max-alice + tv-mass-(11/12)-alice-01bn
    scene BG char Alice tv-mass-11
    $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress + 'c')
    $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
    menu:
        Max_04 "{m}Похоже, Алиса не на шутку завелась! Она всё активнее дрочит мне своими ножками... Почему бы и мне не поласкать её киску, она ведь так близко и ничем на этот раз не прикрыта...{/m}"
        "{i}ласкать её киску пальцами{/i}":
            pass

    # var_pose - 11/12
    $ var_pose = get_pose({'11':'13', '12':'14'}, var_pose)

    # tv-mass-07 + tv-mass-(13/14)-max-(01a/01b) + tv-mass-(13/14)-alice-01b + tv-mass-(13/14)-alice-01bn
    scene BG tv-mass-07
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + 'c')
    $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
    Alice_09 "Ммм, Макс... Да... Какой же у меня похотливый брат! Как приятно!"
    Max_02 "{m}Ухх... Алиса начала сама тереться об мои пальцы! Теперь, она уже не хочет останавливаться...{/m}"
    menu:
        Alice_11 "Мне так тепло... там внизу... Кажется, я уже близко... Как хорошо... Да..."
        "{i}ласкать её киску быстрее{/i}":
            # var_pose - 13/14
            $ var_pose = get_pose({'13':'15', '14':'16'}, var_pose)

            # tv-mass-15 + tv-mass-(15/16)-max-alice + tv-mass-(15/16)-alice-01bn
            scene BG char Alice tv-mass-15
            $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress + 'c')
            $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
            Max_05 "{m}Алиса так жарко и классно трётся об мои пальцы своей киской! Её киска такая мокренькая от возбуждения, что никакого масла для массажа не надо...{/m}"
            Alice_10 "Ох, чёрт... Макс... Я больше не могу! Только не убирай свою руку оттуда... Я уже кончаю... Ахх!"
            Max_06 "{m}Моя старшая сестрёнка совсем сошла с ума... Её ноги дрожат от того, как сладко она кончила!{/m}"

            # var_pose - 15/16
            $ var_pose = get_pose({'15':'09', '16':'10'}, var_pose)

            # tv-mass-03 + tv-mass-(09/10)-max-(01a/01b) + tv-mass-(09/10)-alice-01b + tv-mass-(09/10)-alice-01bn
            scene BG tv-mass-03
            $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
            $ renpy.show('Alice tv-mass ' + var_pose + 'c')
            $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')
            Alice_07 "Да... Такой массаж мне нравится... Вот бы всё время так!"
            Max_01 "Это запросто, Алиса! Наверно, хочешь теперь побыть одна и отдохнуть?"
            Alice_05 "Ага. Давай, засовывай свой член обратно, а то все ноги мне испачкаешь... Массаж классный, Макс... Спасибо!"
            Max_03 "Тебе спасибо..."

            jump advanced_massage1_end

        "{i}не торопиться{/i}":
            # var_pose - 13/14
            $ var_pose = get_pose({'13':'17', '14':'18'}, var_pose)

            # tv-cun-01 + tv-mass-17-max-(01a/01b) + tv-mass-17-alice-01b + tv-mass-17-alice-01bn
            # tv-mass-07 + tv-mass-18-max-(01a/01b) + tv-mass-18-alice-01b + tv-mass-18-alice-01bn
            if var_pose == '17':
                scene BG tv-cun-01
            else:
                scene BG tv-mass-07
            $ renpy.show('Alice tv-mass ' + var_pose + 'c')
            $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
            $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')

            Alice_06 "Макс, ты почему замедлился? Я хочу ещё, не останавливайся!"
            Max_03 "Хочешь узнать, что я умею делать языком?"
            Alice_08 "Ммм... Макс... Я же твоя сестра, а ты... ведёшь себя со мной... как будто я твоя девушка... Но я могу это представить, ненадолго... Так что успевай."
            Max_02 "Ты правда хочешь, чтобы это было быстро?"

            # var_pose - 17/18
            $ var_pose = get_pose({'17':'19', '18':'20'}, var_pose)

            if var_pose == '19':
                scene tv-mass-01
            else:
                scene tv-mass-07
            # tv-mass-01 + tv-mass-19-max-(01a/01b) + tv-mass-19-alice-01b
            # tv-mass-07 + tv-mass-20-max-(01a/01b) + tv-mass-20-alice-01b
            $ renpy.show('Alice tv-mass ' + var_pose + 'c')
            $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)

            # $ renpy.show('cloth1 Alice tv-mass ' + var_pose + 'n')

            jump advanced_massage1_cuni

# выбор варианта массажа после снятия джинсов
label alice_talk_tv_jeans_not_jeans:
    # $ renpy.dynamic('rez')

    # var_pose - 03/04
    menu:
        Alice_05 "Да, так гораздо лучше. Только ты не пялься, куда не надо. Вижу, краем глаза пытаешься что-то разглядеть. Вот не надо. Лучше, продолжай массаж..."
        "А почему на тебе трусики?" if alice.req.result == 'not_nopants':
            Alice_07 "А с чего бы мне быть без них!"
            Alice_14 "Ой..."

            if _in_replay or alice.daily.drink or poss['risk'].st()>2:
                Max_09 "Вот ты и попалась! Я значит тут со всей любезностью массаж сестрёнке делаю, конфетами угощаю, а она..."
            else:
                Max_09 "Вот ты и попалась! Я значит тут со всей любезностью массаж сестрёнке делаю, а она..."

            Alice_12 "Просто забыла..."
            Max_07 "Тогда, если хочешь продолжения массажа, то снимай их!"

            if all([alice.daily.drink > 1, alice.flags.hip_mass > 4]):
                # получен трезвый fj, Алиса съела две конфеты
                Alice_06 "Макс! Какой же ты... Ладно, только снимай их с меня сам. И когда продолжишь массаж, не пялься на меня!"
                menu:
                    Max_03 "Да, да, конечно."
                    "{i}стянуть с неё трусики и продолжить массаж{/i}":
                        # можно продолжать массаж без трусиков
                        $ alice.dress = 'c'
                        jump alice_nopants_massage.not_nopants
            else:
                Alice_06 "Макс! Какой же ты... Ладно, только не смотри. И когда продолжишь массаж, не пялься на меня!"

            Max_03 "Да, да, конечно."

            $ renpy.show('Alice tv-mass '+var_pose+'-3cn')#+alice.dress)
            $ renpy.show('Max tv-mass '+var_pose+'-3'+mgg.dress)


            Alice_13 "Хотя, нет, не пойдёт! У меня так всё видно будет... И хватит уже пялиться! Лучше иди уже по своим делам."   #спрайт с прикрыванием
            Max_05 "Как скажешь. Трусы не потеряй."

            $ renpy.end_replay()
            $ added_mem_var('alice_not_nopants')
            $ current_room = house[0]
            $ alice.dcv.prudence.set_lost(renpy.random.randint(2, 5))
            $ punalice[2][0]=10  #ставим на три дня раньше требование Макса, чтобы ослушание Алисы наступило раньше, чем при требовании во время курения
            jump alice_talk_tv_end

        "{i}продолжить{/i}" ('mass', mgg.massage * 12) if alice.daily.drink > 1:
            $ alice.dress = 'c'
            jump alice_talk_tv_massage_next

        "{i}продолжить{/i}" ('mass', mgg.massage * 10) if alice.daily.drink == 1:
            $ alice.dress = 'c'
            jump alice_talk_tv_massage_next

        "{i}продолжить{/i}" ('mass', mgg.massage * 7) if not alice.daily.drink:
            $ alice.dress = 'c'
            jump alice_talk_tv_massage_next

        "{i}высунуть член{/i}" if all([not alice.daily.drink, 5 > alice.flags.hip_mass > 1, alice.flags.touched]):
            $ alice.dress = 'c'
            jump alice_talk_tv_sober_mass

        "{i}высунуть член{/i}" if all([not alice.daily.drink, alice.flags.hip_mass > 4]):  # эпизодический
            $ alice.dress = 'c'
            jump alice_talk_tv_sober_mass_r

# второй этап массажа
label alice_talk_tv_massage_next:
    # $ renpy.dynamic('ch')

    if not rand_result:
        ### Алисе не понравился массаж!
        Alice_13 "[alice_bad_mass!t]Ой, нет, что-то не то. Ты же так хорошо начал, и что-то неприятно стало... Иди, ещё поучись этому своему массажу на ютубе. Так не пойдёт..."
        Max_00 "Ладно..."
        jump alice_talk_tv_end

    elif rand_result and not alice.daily.drink:
        # понравился массаж, конфету Алиса не ела
        $ infl[alice].add_m(12)
        Alice_03 "[alice_good_mass!t]Ух, как хорошо... Макс, а ты молодец сегодня! Не ожидала такой чувственности и в то же время силы... Ну всё спасибо, иди..."
        Max_04 "Не за что..."
        jump alice_talk_tv_end

    else:
        # понравился массаж, Алиса съела конфетку
        # или без конфеты после прохождения трезвого пути ???
        pass

    # массаж понравился

    # var_pose - 03/04
    $ var_pose = get_pose({'03':'05', '04':'06'}, var_pose)
    scene BG tv-mass-05
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    menu:
        Alice_07 "[alice_good_mass!t]Макс... Сегодня твои ручки творят чудеса... А во что это моя нога упёрлась? Это часть программы или как?"
        "Да, это будет на десерт...":
            menu:
                Alice_08 "Ты так в себе уверен, Макс... Забыл, что я твоя сестра? Не говори глупости... Просто продолжай массировать мои ножки. Если ты ещё не в курсе, они у меня целиком - эрогенная зона..."
                "{i}попытаться приставать{/i}" if all([alice.daily.drink < 2, not _in_replay, not alice.flags.hip_mass]):
                    jump .fail

                "{i}массировать её ноги выше{/i}" if alice.daily.drink > 1 and alice.flags.hip_mass:
                    jump advanced_massage1

                "{i}массировать её ноги выше{/i}" if alice.daily.drink == 1 and alice.flags.hip_mass > 4:
                    jump advanced_massage1

                "{i}продолжать массаж{/i}" if not _in_replay:
                    pass

                "{i}продолжать массаж{/i}" if _in_replay and (not alice.flags.hip_mass or (alice.flags.hip_mass > 4 and not alice.daily.drink)):
                    pass

        "{i}продолжать молча{/i}":
            menu:
                Alice_04 "Эх, Макс... А я бы захотела продолжения, если бы ты был моим парнем... Жаль, что ты только мой брат..."
                "Ну я могу стать твоим парнем... Хотя бы на час... или насколько захочешь..." if not _in_replay:
                    menu:
                        Alice_05 "На сколько захочу? На секунду! Ой. Она прошла... Всё, Макс, твоё время вышло... Ладно, засовывай свою штуку обратно. Что-то голова кружится... Макс, уйди по хорошему, а..."
                        "{i}уйти{/i}":
                            jump alice_talk_tv_end

                "{i}попытаться приставать{/i}" if alice.daily.drink < 2 and not _in_replay and not alice.flags.hip_mass:
                    jump .fail

                "{i}массировать её ноги выше{/i}" if all([alice.daily.drink > 1, alice.flags.hip_mass, 'kira' in chars]):
                    jump advanced_massage1

                "{i}массировать её ноги выше{/i}" if alice.daily.drink == 1 and alice.flags.hip_mass > 4:
                    jump advanced_massage1

                "{i}продолжать массаж{/i}" if not _in_replay:
                    pass

                "{i}продолжать массаж{/i}" if _in_replay and (not alice.flags.hip_mass or (alice.flags.hip_mass > 4 and not alice.daily.drink)):
                    pass

    # пьяный fj получен
    # var_pose - 05/06
    $ var_pose = get_pose({'05':'07', '06':'08'}, var_pose)
    scene BG tv-mass-07
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    Alice_04 "Ну всё, кажется хватит. Во всяком случае, тебе. А то мне ногу испачкаешь... Но ручки у тебя - что надо. Даже не ожидала такого от тебя..."
    Max_05 "Я тоже не ожидал... такого..."
    Alice_08 "Значит, мы оба полны сюрпризов. Ну всё, хорошего помаленьку. Давай, засовывай свой член обратно, а то до добра это всё дело не дойдёт... Да, и спасибо за массаж..."
    Max_03 "Тебе спасибо..."
    $ renpy.end_replay()
    $ alice.stat.footjob += 1
    if alice.daily.drink > 0:
        $ alice.daily.massage = 3

    $ persistent.memories['alice_talk_tv'] = 1
    $ poss['naughty'].open(3)
    jump alice_talk_tv_end

    menu .fail:
        Alice_12 "Макс! Ещё одно лишнее движение, и я дам тебе по шарам вот это самой ногой. Ты меня понял? Всё, массаж окончен, вали отсюда!"
        "{i}уйти{/i}":
            jump alice_talk_tv_end

# 1-3 этапы пути к получению трезвого fj
label alice_talk_tv_sober_mass:
    # var_pose - 03/04
    $ var_pose = get_pose({'03':'05', '04':'06'}, var_pose)

    # tv-mass-05 + tv-mass-(05/06)-max-(01a/01b) + tv-mass-(05/06)-alice-(01a/01b/01c)
    scene BG tv-mass-05
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)

    if alice.flags.hip_mass < 3:
        ###в 1-ый раз###
        $ alice.flags.hip_mass = 3
        $ poss['naughty'].open(7)
        Alice_07 "Макс... Сегодня твои ручки творят чудеса... Но мне немного щекотно. Раньше ты массировал мне ножки без этого..."
        Max_02 "Ты права. Без этого... Не нравится?"
        Alice_04 "Нет, мне очень нравится! Просто, я пока не поняла, что изменилось и как ты это делаешь... А хотя... Подожди-ка..."
        Max_07 "Знай, я не специально."

        # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03a/03b/03c)
        scene BG tv-mass-03
        $ renpy.show('Max tv-mass 04-3' + mgg.dress)
        $ renpy.show('Alice tv-mass 04-3' + alice.dress)    # b/c/d
        Alice_15 "Так я об член твой тёрлась?! Ну, Макс! Ты зачем так сделал, совсем что ли извращенец? Хотя, зачем я спрашиваю..."
        Max_04 "У тебя такая нежная кожа, вот у меня и встал. И несмотря на это, я хотел закончить массаж... для своей дорогой сестрёнки."
        Alice_16 "Да ты что! А если бы я так и не поняла, что ты мне ножки членом своим щекочешь?!"
        Max_03 "Ты же сама сказала, что тебе очень нравится! А для меня это главное."
        Alice_17 "Ещё бы! Должно быть, это очень приятно, делать массаж ног, когда тебе в ответ дрочат. Пнуть бы тебя за это сам знаешь куда!"
        Max_07 "Алиса, зачем этого стыдиться? Тебе же понравилось..."
        Alice_06 "Макс, это ведь грязно! Я твоя сестра!"
        Max_09 "И что теперь, мне нельзя что-то приятное сделать для тебя? Это не круто."
        Alice_12 "Можно, но не так же..."
        Max_08 "Смотри... Тогда буду массировать руками."
        Alice_00 "Вот именно! Но уже в следующий раз. На сегодня хватит. Я так уж и быть, представлю, что ничего не было, потому что твой массаж мне нравится."
        Max_00 "Хорошо."

    elif alice.flags.hip_mass < 4:
        ###во 2-ой раз###
        $ alice.flags.hip_mass = 4
        $ poss['naughty'].open(8)
        Alice_07 "Макс... Сегодня твои ручки творят чудеса... Мне снова щекотно... Это что, снова твой член! Ты же сказал, что будешь массировать руками!"
        Max_02 "Так и есть."
        Alice_06 "Я ведь и пнуть могу, если не уберёшь свою штуку!"
        Max_04 "Я бы убрал, если бы ты перестала тереться об него своими ножками."

        # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03a/03b/03c)
        scene BG tv-mass-03
        $ renpy.show('Max tv-mass 04-3' + mgg.dress)
        $ renpy.show('Alice tv-mass 04-3' + alice.dress)    # b/c/d
        Alice_14 "Ничего я не тёрлась! Просто по инерции... немного... Это всё массаж твой. Мне становится так хорошо, что я не осознаю, что делаю."
        Max_03 "Ну и делай себе дальше, если тебе нравится. Будет у нас маленький секретик."
        Alice_06 "Да мне просто стыдно, что я тут делаю со своим братом на диване!"
        Max_07 "Подумаешь! Я просто хочу сделать приятно своей сестрёнке, а уж как - не важно."
        Alice_13 "Мило, Макс. Хочешь сказать, мне стоило бы просто дать тебе закончить вот такой массаж и ни о чём не думать?"
        Max_02 "Попробовала бы разок. Уверен, ты останешься весьма довольной."
        Alice_05 "Ты так в себе уверен?! Что ж, в следующий раз я попробую. И если мне хоть что-то, хоть немного не понравится... тебе будет плохо."
        Max_01 "Не будет."

    else: # alice.flags.hip_mass < 5:
        ###в 3-ий раз###
        $ alice.flags.hip_mass = 5
        $ poss['naughty'].open(9)
        Alice_07 "Макс... Сегодня твои ручки творят чудеса... Но будь осторожен, высовывая свой член... Мне не должно быть слишком щекотно..."
        Max_02 "Не будет."

        # var_pose - 05/06
        $ var_pose = get_pose({'05':'07', '06':'08'}, var_pose)

        # tv-mass-07 + tv-mass-(07/08)-max-(01a/01b) + tv-mass-(07/08)-alice-(01a/01b/01c)
        scene BG tv-mass-07
        $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
        $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
        menu:
            Alice_08 "Ты так в себе уверен, Макс... Ну посмотрим... Просто продолжай массировать мои ножки. Если ты ещё не в курсе, они у меня целиком - эрогенная зона..."
            "{i}продолжать массаж{/i}":
                Alice_04 "Эх, Макс... Хоть мне и хорошо, но нам пора закругляться. Мне кажется, ты уже близок к тому, чтобы испачкать меня или диван."
                Max_09 "Как бы не так!"

        # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03a/03b/03c)
        scene BG tv-mass-03
        $ renpy.show('Max tv-mass 04-3' + mgg.dress)
        $ renpy.show('Alice tv-mass 04-3' + alice.dress)    # b/c/d
        Alice_12 "Да ты что! Хочешь сказать, для тебя это было не так уж и приятно?!"
        Max_03 "Шутишь? Было супер! Но этого мало, чтобы я тебя испачкал."
        Alice_05 "Даже так... Ну, проверять мы это, пожалуй, не будем. Спасибо за массаж, Макс. Мне понравилось. Но это будет только нашей вечерней шалостью, так что не думай, что к тебе будет особенное отношение во всё остальное время."
        Max_01 "Хотя бы так."

    $ alice.stat.footjob += 1
    $ alice.free += 1   # 3 максимум
    $ infl[alice].add_m(16)
    jump alice_talk_tv_end

# периодический трезвый массаж после получения трезвого fj
label alice_talk_tv_sober_mass_r:
    # var_pose - 03/04
    $ var_pose = get_pose({'03':'05', '04':'06'}, var_pose)

    # tv-mass-05 + tv-mass-(05/06)-max-(01a/01b) + tv-mass-(05/06)-alice-(01a/01b/01c)
    scene BG tv-mass-05
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    Alice_07 "Макс... Обожаю то, какие чудеса творят твои руки... Но будь осторожен, высовывая свой член... Мне не должно быть слишком щекотно..."
    Max_02 "Не будет."

    # var_pose - 05/06
    $ var_pose = get_pose({'05':'07', '06':'08'}, var_pose)

    # tv-mass-07 + tv-mass-(07/08)-max-(01a/01b) + tv-mass-(07/08)-alice-(01a/01b/01c)
    scene BG tv-mass-07
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)

    menu:
        Alice_08 "Ты так в себе уверен, Макс... Ну посмотрим... Просто продолжай массировать мои ножки. Они у меня любят твой твёрдый... настрой."
        "{i}продолжать массаж{/i}":
            # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03a/03b/03c)
            scene BG tv-mass-03
            $ renpy.show('Max tv-mass 04-3' + mgg.dress)
            $ renpy.show('Alice tv-mass 04-3' + alice.dress)    # b/c/d
            Alice_03 "Ух, как хорошо... Но пора закругляться. Ты молодец, Макс! Мне нравится эта чувственность и в то же время сила... Спасибо тебе."

        "{i}массировать её ноги выше{/i}" ('mass', mgg.massage * 3):
            if rand_result:
                # (Ей нравится!)
                # var_pose - 07/08
                $ var_pose = get_pose({'07':'09', '08':'10'}, var_pose)

                # tv-mass-03 + tv-mass-(09/10)-max-(01a/01b) + tv-mass-(09/10)-alice-(01a/01b/01c)
                scene BG tv-mass-03
                $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
                $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
                Alice_07 "[like!t]Да, моим ножкам становится так легко от твоих прикосновений... И они очень тебе благодарны. Чувствуешь, насколько?"
                Max_03 "А как же... Они у тебя шаловливые..."
                menu:
                    Alice_04 "Они у меня такие... Любят помассировать кое-что большое и твёрдое... Главное, не перестараться и чувствовать, когда нужно заканчивать..."
                    "{i}закончить массаж{/i}":
                        # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03a/03b/03c)
                        scene BG tv-mass-03
                        $ renpy.show('Max tv-mass 04-3' + mgg.dress)
                        $ renpy.show('Alice tv-mass 04-3' + alice.dress)    # b/c/d
                        Alice_03 "Ух, как хорошо... Макс, а ты молодец! Мне нравится эта чувственность и в то же время сила... Спасибо тебе."

                    # "{i}массировать ещё выше{/i} (навык массажа)" if False:   #в следующей версии
                    #     pass

                $ alice.stat.footjob += 1
                $ add_lim('alice.free', 0.1, 5)
                $ infl[alice].add_m(16)

            else:
                # (Ей не нравится!)
                # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03a/03b/03c)
                scene BG tv-mass-03
                $ renpy.show('Max tv-mass 04-3' + mgg.dress)
                $ renpy.show('Alice tv-mass 04-3' + alice.dress)
                Alice_03 "[dont_like!t]Было хорошо, Макс! Но ты немного поспешил двигаться выше... Но ручки у тебя - что надо. До следующего раза... и спасибо..."

    Max_04 "Не за что..."
    jump alice_talk_tv_end

# расширенный массаж (массаж бёдер и киски) открывается после того, как Макс увидит ночные развлечения Алисы через камеру
label advanced_massage1:
    if not _in_replay:
        $ poss['naughty'].open(5)
    $ added_mem_var('advanced_massage1')

    # var_pose - 05/06
    $ var_pose = get_pose({'05':'09', '06':'10'}, var_pose)

    # tv-mass-09-10
    scene BG tv-mass-03
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)

    if alice.flags.hip_mass < 2:
        #только при первом расширенном массаже
        Max_08 "{m}Я раньше и внимания не обращал, а ведь Алиса всегда намекала на то, что мне можно массировать не только её ступни! Вот я олух...{/m}"
        $ alice.flags.hip_mass = 2

    $ added_mem_var('double_mass_alice')

    if alice.flags.hip_mass > 4:
        Alice_07 "Да, моим ножкам становится так легко от твоих прикосновений... И они очень тебе благодарны. Чувствуешь, насколько?"
        Max_03 "А как же... Они у тебя шаловливые..."

    else:
        Alice_07 "Да, моим ножкам становится так легко от твоих прикосновений... У меня ведь красивые ноги, правда?"
        Max_03 "Очень красивые, сестрёнка! Такие мягкие, но упругие... Массировать их - одно удовольствие! А ещё они у тебя шаловливые..."

    menu:
        Alice_04 "Они у меня такие... Любят помассировать кое-что большое и твёрдое..."
        "{i}массировать ещё выше{/i}":
            pass

    # var_pose - 09/10
    $ var_pose = get_pose({'09':'11', '10':'12'}, var_pose)

    # tv-mass-11-12
    scene BG char Alice tv-mass-11
    $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+alice.dress)
    menu:
        Max_04 "{m}Похоже, Алиса не на шутку завелась! Она всё активнее дрочит мне своими ножками... Почему бы и мне не поласкать её киску, она ведь так близко...{/m}"
        "{i}ласкать её киску через одежду{/i}":
            pass
    scene BG tv-mass-07

    # var_pose - 11/12
    $ var_pose = get_pose({'11':'13', '12':'14'}, var_pose)

    # tv-mass-13-14
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    Alice_09 "Ммм, Макс... Да... Какой же у меня похотливый брат! Как приятно!"
    Max_02 "{m}Ухх... Алиса начала сама тереться об мои пальцы! Конфеты сделали своё дело и теперь она уже не хочет останавливаться...{/m}"
    menu:
        Alice_11 "Мне так тепло... там внизу... Кажется, я уже близко... Как хорошо... да..."
        "{i}ласкать её киску быстрее{/i}" if not _in_replay or (_in_replay and not alice.dcv.intrusion.stage in [5, 7]):
            # не воспоминание или воспоминание "Помассирую не только ножки"
            jump advanced_massage1_faster

        "{i}не торопиться{/i}" if alice.dcv.intrusion.stage in [5, 7]:
            # Макс подарил Алисе кружевное боди, опередив Эрика
            jump advanced_massage1_no_rush

# окончание расширенного массажа
label advanced_massage1_end:
    $ renpy.end_replay()
    # $ current_room = house[0]
    $ alice.daily.massage = 4
    $ alice.daily.drink = 0
    jump alice_talk_tv_end

# заканчиваем расширенный массаж доведением до оргазма пальцами
label advanced_massage1_faster:

    # var_pose - 13/14
    $ var_pose = get_pose({'13':'15', '14':'16'}, var_pose)

    # tv-mass-15-16
    scene BG char Alice tv-mass-15
    $ renpy.show('Alice tv-mass ' + var_pose + mgg.dress+alice.dress)
    Max_05 "{m}Алиса так жарко и классно трётся об мои пальцы своей киской! Хоть на ней и есть одежда, но я чувствую через неё всё...{/m}"
    Alice_10 "Ох, чёрт... Макс... я больше не могу! Только не убирай свою руку оттуда... Я уже кончаю... Ахх!"
    Max_06 "{m}Моя старшая сестрёнка совсем сошла с ума... Её ноги дрожат от того, как сладко она кончила!{/m}"

    # var_pose - 15/16
    $ var_pose = get_pose({'15':'09', '16':'10'}, var_pose)

    # tv-mass-09-10
    scene BG tv-mass-03
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    Alice_07 "Да... такой массаж мне нравится... Вот бы всё время так!"
    Max_01 "Это запросто, Алиса! Наверно, хочешь теперь побыть одна и отдохнуть?"
    Alice_05 "Ага. Давай, засовывай свой член обратно, а то все ноги мне испачкаешь... Массаж классный, Макс... Спасибо!"
    Max_03 "Тебе спасибо..."

    jump advanced_massage1_end

# подготовка Алисы к куни
label advanced_massage1_no_rush:

    # var_pose - 13/14
    $ var_pose = get_pose({'13':'17', '14':'18'}, var_pose)

    # tv-mass-17-18
    if var_pose == '17':
        scene BG tv-cun-01
    else:
        scene BG tv-mass-07
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
    Alice_06 "Макс, ты почему замедлился? Я хочу ещё, не останавливайся!"
    Max_03 "Хочешь узнать, что я умею делать языком?"
    menu:
        Alice_08 "Ммм... Макс... Я же твоя сестра, а ты... ведёшь себя со мной... как будто я твоя девушка... Но я могу это представить, ненадолго... Так что успевай."
        "{i}снять с Алисы трусики{/i}" if alice.dress == 'c':
            pass

        "{i}снять с Алисы шортики{/i}" if alice.dress != 'c':
            pass

    # var_pose - 17/18
    $ var_pose = get_pose({'17':'19', '18':'20'}, var_pose)

    # tv-mass-19-20
    if var_pose == '19':
        scene BG tv-mass-01
    $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
    $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)

    jump advanced_massage1_cuni

# куни (а также получение намёка на необходимость сближения с Алисой без алкоголя
label advanced_massage1_cuni:
    Alice_07 "Мне любопытно узнать, сможешь ли ты что-то противопоставить тем, кто это делал до тебя... А это, между прочим, были девушки, которые куда больше твоего знают, как это надо делать."
    Max_07 "Сомневаешься во мне?"

    menu :
        Alice_05 "А ты болтай поменьше... Может и перестану."
        "{i}ласкать её киску языком{/i}" ('sex', mgg.sex * 5, 90):
            pass
    if rand_result:
        # (Ей нравится!)
        # var_pose - 19/20
        $ var_pose = get_pose({'19':'21', '20':'22'}, var_pose)

        # tv-mass-21-22
        if var_pose == '21':
            scene BG tv-sex03-01
        else:
            scene BG tv-mass-01
        $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
        $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
        Alice_09 "[like!t]Да, Макс, да! Я уже так близко... Не останавливайся... У тебя такой быстрый и ловкий язычок, Макс... Ммм... Как хорошо!"
        menu:
            Max_04 "{m}Я сейчас устрою твоей сладкой киске такое, чего ты точно не забудешь! Хотя... нет, ты забудешь... Да и ладно.{/m}"
            "{i}ещё быстрее работать языком{/i}":
                pass

        # var_pose - 20/21
        $ var_pose = get_pose({'21':'23', '22':'24'}, var_pose)

        # tv-mass-23-24
        if var_pose == '23':
            scene BG tv-mass-01
        else:
            scene BG tv-sex03-01
        $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
        $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
        Alice_11 "Ах! Я больше не могу, Макс... Кончаю! Да... Как же это было классно! Ох... Это было потрясающе..."
        Max_02 "Будешь ещё сомневаться в моих навыках?"

        # var_pose - 23/24
        $ var_pose = get_pose({'23':'19', '24':'20'}, var_pose)

        # tv-mass-19-20
        if var_pose == '20':
            scene BG tv-mass-07
        $ renpy.show('Alice tv-mass ' + var_pose + alice.dress)
        $ renpy.show('Max tv-mass ' + var_pose + mgg.dress)
        Alice_07 "Ах, Макс! И где ты такому научился?! Неужто, просмотр порнушки может такому научить?"
        Max_05 "Просто сделал всё так, как хотел бы, чтобы сделали мне..."

        if all([alice.flags.touched, alice.flags.hip_mass > 4, alice.daily.drink>1]):
            # две конфеты, пройден "трезвый" путь с fj у ТВ
            jump advanced_massage1_reciprocity      # ответная услуга

        else:
            Alice_05 "Да... такой массаж мне нравится... Вот бы всё время так! А сейчас, давай-ка засовывай свой член обратно, а то все ноги мне испачкаешь... Массаж классный, Макс... Спасибо!"
            Max_03 "Тебе спасибо..."
            if alice.flags.hip_mass < 3 and alice.flags.touched:      #подсказка, если не было развития по трезвому пути
                Max_09 "{m}С Алисой нужно как-то сближаться без конфет. Только как?! Она стала более адекватно воспринимать мои стояки, после случая с пауком во дворе... Так может, и при массаже ног у ТВ без конфет у меня что-то выгорит?{/m}"
                if not _in_replay:
                    $ poss['naughty'].open(6)

    else:
        # (Ей не нравится!)
        # tv-mass-03 + tv-mass-03-max-(03a/03b) + tv-mass-03-alice-(03/03a/03c)
        scene BG tv-mass-03
        $ renpy.show('Max tv-mass 03-3' + mgg.dress)
        $ renpy.show('Alice tv-mass 03-3' + alice.dress)    # b/c/d

        Alice_03 "[dont_like!t]Всё, Макс! Я передумала! Массаж был неплохой, но на этом мы закончим..."
        Max_08 "Да ладно, Алиса! Я же ещё ничего не успел сделать!"
        Alice_05 "Слишком много болтал. Вот и передумала. Но за массаж, спасибо! Давай, засовывай свой член обратно и гуляй..."
        Max_10 "Ладно..."

    jump advanced_massage1_end

# "ответная услуга" от Алисы
label advanced_massage1_reciprocity:
    # две конфеты, пройден "трезвый" путь с fj у ТВ
    # Max - 'b', 'c'; Alice - 'b', 'c', 'd'

    # tv-mass-03 + tv-mass-04-max-(03a/03b) + tv-mass-04-alice-(03/03a/03c)
    scene BG tv-mass-03
    $ renpy.show('Max tv-mass 04-3' + mgg.dress)
    $ renpy.show('Alice tv-mass 04-3' + alice.dress+'n')
    Alice_02 "Ты даришь мне столько удовольствия, что я просто вынуждена ответить тебе взаимностью."
    Max_02 "Значит, это будет что-то приятное?"

    # tv-mass-05 + tv-mass-hj01-max-(02a/02b) + tv-mass-hj01-alice-(02a/02b/02c)
    scene BG tv-mass-05
    $ renpy.show('Max tv-mass hj-02' + mgg.dress)
    $ renpy.show('Alice tv-mass hj-02' + alice.dress)
    Alice_03 "Думаю, тебе будет настолько хорошо, что закачаешься... Ты ведь наверняка об этом мечтал кучу раз?"
    Max_04 "Хорошо, что мечты сбываются!"

    if not _in_replay:
        $ poss['naughty'].open(10)

    if renpy.random.randint(0, 1):
        # (tv-max&kira-sex03-01-f + tv-mass-lick01-max-(01a/01b) + tv-mass-lick01-alice-(01a/01b/01c))
        scene BG tv-sex03-01
        $ renpy.show('Max tv-mass lick-01' + mgg.dress)
        $ renpy.show('Alice tv-mass lick-01' + alice.dress)

    else:
        # (after-club-s04-f + tv-mass-lick01-max-(02a/02b) + tv-mass-lick01-alice-(02a/02b/02c))
        scene BG after-club-s04-f
        $ renpy.show('Max tv-mass lick-02' + mgg.dress)
        $ renpy.show('Alice tv-mass lick-02' + alice.dress)

    menu:
        Alice_08 "И ещё как! Я уже приласкала тебя своими ножками... А как тебе мой язычок? Вижу, тебе это нравится... Я буду исследовать им твой член столько, сколько ты сможешь сдержаться!"
        "{i}сдерживаться{/i}" ('sex', mgg.sex * 4, 90):
            pass

    if rand_result:
        # (Удалось сдержаться!)
        # tv-mass-03 + tv-mass-hj01-max-(01a/01b) + tv-mass-hj01-alice-(01a/01b/01c)
        scene BG tv-mass-03
        $ renpy.show('Max tv-mass hj-01' + mgg.dress)
        $ renpy.show('Alice tv-mass hj-01' + alice.dress)
        Alice_05 "[restrain!t]А ты стойкий, Макс! Похоже, без помощи моих губ тебя не удастся удовлетворить. Ну, держись..."

        # lounge-tv-01 + tv-mass-bj01-max-(01a/01b) + tv-mass-bj01-alice-(01a/01b/01c)
        scene BG lounge-tv-01
        $ renpy.show('Max tv-mass bj-01' + mgg.dress)
        $ renpy.show('Alice tv-mass bj-01' + alice.dress)

        menu:
            Max_21 "{m}Ох, как это классно! Алиса с явным наслаждением посасывает мой член. Мой массаж её определённо очень возбуждает, раз она делает мне минет с таким смаком. Д-а-а, это кайф!{/m}"
            "{i}сдерживаться{/i}" ('sex', mgg.sex * 2, 90):
                if rand_result:
                    # (Удалось сдержаться!)

                    # tv-max&kira-sex02-01-f + tv-mass-bj01-max-(02a/02b) + tv-mass-bj01-alice-(02a/02b/02c)
                    scene BG tv-sex02-01
                    $ renpy.show('Max tv-mass bj-02' + mgg.dress)
                    $ renpy.show('Alice tv-mass bj-02' + alice.dress)
                    Max_22 "[restrain!t]Давай, сестрёнка! Ты сосёшь просто отпадно! Если ты продолжишь ещё быстрее, то сдержаться я уже не смогу... О да, молодчинка... Д-а-а... Давай ещё... Именно так! Ох-х-х, я кончаю..."

                    # tv-mass-15 + tv-mass-cum01-alice-(01a/01b/01c) + tv-mass-cum01-max-(01a/01b) + tv-mass-cum01-max&alice-(01/01a)
                    scene BG char Alice tv-mass-15
                    $ renpy.show('Alice tv-mass cum-01' + alice.dress)
                    $ renpy.show('Max tv-mass cum-01' + mgg.dress)
                    $ renpy.show('FG Alice tv-mass cum-01' + renpy.random.choice(['a', 'b']))
                    Alice_07 "Давай! Кончи мне на грудь... Я бы удивилась, если бы ты продержался ещё дольше. Массаж получился классный, Макс... и я не только про сам массаж. А сейчас, давай-ка засовывай свой член обратно, а мне нужно скорее привести себя в порядок."
                    Max_03 "Да, повеселились от души."
                    jump advanced_massage1_end

    # (Не удалось сдержаться!)
    jump advanced_massage1_no_restrain

# Макс не сдержался во время "ответной услуги"
label advanced_massage1_no_restrain:
    Max_20 "[norestrain!t]Ох, Алиса... Нет, я уже больше не могу... Ухх... Сейчас кончу!"

    # tv-mass-15 + tv-mass-cum01-alice-(01a/01b/01c) + tv-mass-cum01-max-(01a/01b) + tv-mass-cum01-max&alice-(01/01a)
    scene BG char Alice tv-mass-15
    $ renpy.show('Alice tv-mass cum-01' + alice.dress)
    $ renpy.show('Max tv-mass cum-01' + mgg.dress)
    $ renpy.show('FG Alice tv-mass cum-01' + renpy.random.choice(['a', 'b']))
    Alice_07 "Давай! Кончи мне на грудь... Я бы удивилась, если бы ты продержался ещё дольше. Массаж получился классный, Макс... и я не только про сам массаж. А сейчас, давай-ка засовывай свой член обратно, а мне нужно скорее привести себя в порядок."
    Max_03 "Да, повеселились от души."
    jump advanced_massage1_end

## === закончен просмотр ТВ с Алисой ===


label alice_aboutbooks:
    menu:
        Alice_13 "Книжку, очевидно..."
        "Спасибо, кэп!":
            Alice_01 "Так чего хотел, Макс?"
            Max_00 "Хотел узнать что именно читаешь..."
        "Очень смешно...":
            Alice_01 "Так чего хотел, Макс?"
            Max_00 "Хотел узнать что именно читаешь..."
        "Это понятно, а какую? Только не говори, что бумажную...":
            Alice_01 "Ну вот... Хотела пошутить, и ты так меня обломал... А если серьёзно, то чего хотел?"
            Max_00 "Да вот и хотел узнать, что именно читаешь..."
    menu:
        Alice_02 "Забавно. А тебе не всё равно? Или делать нечего?"
        "Не всё равно, раз спрашиваю":
            pass
        "Так ты скажешь или нет?":
            pass
    menu:
        Alice_00 "Не скажу. Сиди теперь и гадай! \n\n{i}Алиса прикрыла обложку рукой{/i}"
        "Какой-то дамский роман?":
            pass
        "Какие-то сопли с сахаром?":
            pass
        "Неужели справочник по квантовой механике?":
            pass
    $ poss['secretbook'].open(0)
    menu:
        Alice_01 "Думай, что хочешь, а я всё равно не скажу."
        "Ну и ладно!":
            pass
        "{i}узнать подробнее о \"Возможностях\"{/i}" if sum([1 if sum(poss[ps].stages) else 0 for ps in poss_dict]) < 2:
            call about_poss from _call_about_poss_1
    $ spent_time += 10
    $ AvailableActions['searchbook'].enabled = True
    jump Waiting


label first_talk_smoke:
    $ __mood = 0
    Alice_13 "Упс. Макс, ты ничего не видел!"
    $ poss['smoke'].open(0)
    Max_08 "Алиса, ты куришь?!"
    $ alice.dcv.special.stage = 1
    menu:
        Alice_12 "Нет, блин, просто зажгла сигарету, посмотреть как горит... Давай так, ты уйдёшь и сделаешь вид, что ничего не было, хорошо?"
        "А если уйду, что мне за это будет?":
            Alice_16 "Вот если не уйдёшь, то узнаешь, что тебе за это будет! Бегом отсюда!"
            Max_09 "Может быть я и уйду, но..."
        "Ну ок, только я ничего не обещаю...":
            pass
    menu:
        Alice_14 "Что это значит? Шантажировать меня вздумал?!"
        "Ну да. Мама что с тобой сделает, если узнает?":
            menu:
                Alice_13 "Макс, я тебя по-человечески прошу. Сделай вид, что ничего не было. Я не хочу расстраивать маму..."
                "Не хочешь расстраивать маму или получить по заднице?":
                    menu:
                        Alice_12 "Может быть, и то и другое. Ну так как, Макс?"
                        "Мы всё ещё можем договориться...":
                            jump .talk
                        "Посмотрим...":
                            jump .maybe
                        "Ну ладно, ладно...":
                            $ __mood += 75
                            jump .goodend
                "Мы всё ещё можем договориться...":
                    jump .talk
                "Посмотрим...":
                    jump .maybe
                "Ну ладно, ладно...":
                    $ __mood += 100
                    jump .goodend
        "Ну, мы можем договориться":
            jump .talk
        "Как знать, может быть...":
            jump .maybe
        "Нет, конечно. Мне жизнь дорога!":
            $ __mood += 50
            jump .goodend

    menu .talk:
        Alice_13 "Договориться? Ну ладно. Чего ты хочешь?"
        "Если заплатишь, буду молчать":
            menu:
                Alice_12 "Макс, ты же знаешь, что я на мели. У меня нет денег. Ну, точнее есть, но баксов 10. Тебя устроит?"
                "Ну, давай":
                    $ __mood -= 50
                    $ spent_time += 10
                    $ mgg.ask(0)
                    $ alice.req.req = 'money'
                    menu:
                        Alice_13 "Сейчас сбегаю за деньгами...\nВот, держи $10, и теперь-то уж точно ты ничего не видел. Так?"
                        "Так!":
                            jump .end
                        "Как знать...":
                            menu:
                                Alice_16 "И как это понимать, Макс? Мы же договорились! Ну ты и гад... Всё, вали отсюда!"
                                "Ну, как скажешь...":
                                    jump .end

                "Нет, этого мало...":
                    $ __mood -= 100
                    menu:
                        Alice_12 "Ну... больше у меня нет. Может, просто забудем обо всём?"
                        "Покажи сиськи!":
                            jump .bad
                        "Сними трусы!":
                            jump .bad
                        "Отсоси мне!":
                            jump .suck
                        "Ты будешь мне должна услугу":
                            jump .owe
        "Покажи сиськи!":
            jump .bad
        "Сними трусы!":
            jump .bad
        "Отсоси мне!":
            jump .suck
        "Ты будешь мне должна услугу":
            jump .owe

    menu .bad:
        Alice_15 "Что?! Ну ты хам! Всё, быстро свалил!"
        "Ну, как скажешь...":
            $ __mood -= 100
            jump .end

    menu .suck:
        Alice_14 "Что?! Отсоси себе сам! Пошёл вон отсюда!"
        "Ну, как скажешь...":
            $ __mood -= 150
            jump .end

    menu .owe:
        Alice_06 "И какую услугу я тебе буду должна? Например?"
        "Покажешь сиськи, когда попрошу...":
            pass
        "Разденешься, когда скажу...":
            pass
        "Отсосёшь, когда нужно будет...":
            jump .suck
        "Я ещё не решил...":
            menu:
                Alice_03 "Ну, вот когда решишь, тогда и поговорим. А теперь иди отсюда, пока ещё можешь!"
                "Ну, как скажешь...":
                    jump .end

    menu:
        Alice_15 "Да ты что?! А не охренел ли ты, мальчик? Это всего лишь сигарета, а запросы у тебя... Всё, свалил отсюда!"
        "Ну, как скажешь...":
            $ __mood -= 100
            jump .end

    menu .maybe:
        Alice_12 "Сам смотри... Воевать со мной - себе дороже. И, вообще, иди отсюда. Я уже взрослая и могу делать что хочу..."
        "Ну, как скажешь...":
            pass

    menu .goodend:
        Alice_05 "Вот это другое дело. Ладно, разговор окончен..."
        "Хорошо...":
            pass

    label .end:
        $ spent_time += 10
        $ AddRelMood('alice', 0, __mood)
        jump Waiting


label second_talk_smoke:
    $ __mood = 0
    menu:
        Alice_12 "А, Макс... Чего хотел?"
        "Да хотел узнать, что ты куришь?":
            menu:
                Alice_03 "Это так важно для тебя? Почему спрашиваешь?"
                "Просто любопытно":
                    Alice_00 "Любопытный он... Это сигареты Lucky Strike..."
                "Для поддержания разговора":
                    Alice_00 "Да уж, поддержание разговора... А курю я сигареты Lucky Strike..."
                "А, не важно...":
                    Alice_00 "Ну, раз не важно, то и не скажу..."
                    Max_01 "Конечно, если это секрет..."
                    Alice_01 "Вот ты зануда, Макс! Обычные сигареты Lucky Strike..."
        "Нет, ничего...":
            jump Waiting
    Max_07 "Они же не женские?!"
    menu:
        Alice_13 "Ну да... Просто нравится именно эти. Их наш отец курил, сначала запах нравился. Когда выросла, попробовала и теперь вот втянулась..."
        "Скучаешь о нём?":
            Alice_00 "Ну так, не очень, если честно. Уже слишком много времени прошло... А сигареты - это так, привычка..."
            Max_00 "Может, и мне попробовать?"
        "Может, и мне попробовать?":
            pass
    menu:
        Alice_06 "Нет уж, самой мало. Знаешь, как сложно их достать? Особенно, чтобы мама не узнала..."
        "Может быть, тебе помочь?":
            $ __mood += 100
            menu:
                Alice_02 "С чем? Можешь доставать такие сигареты?"
                "Ну, я попробую через интернет":
                    pass
                "Может быть...":
                    pass
            Alice_03 "Давай! Было бы чудненько. Только маме не пали меня, а то я на тебя обижусь и больше никогда разговаривать не буду..."
            Max_05 "Договорились!"

        "Ну и ладно...":
            $ __mood += 50
            Alice_12 "Я закончила. Если мама спросит, скажешь, от соседей надуло, хорошо?"
            Max_01 "Конечно!"

    $ AddRelMood('alice', 5, __mood)
    $ items['cigarettes'].unblock()
    $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    $ alice.dcv.special.stage = 2
    $ alice.dcv.special.set_lost(1)
    $ AvailableActions['searchciga'].enabled = True
    $ spent_time = 30 - int(tm[-2:])
    jump Waiting


label gift_cigarettes:
    $ __mood = 0
    menu:
        Alice_03 "Это то, что я думаю? Давай сюда!"
        "А что взамен?":
            Alice_13 "Макс! Не будь придурком. Давай сюда!"
            Max_01 "Ну, держи..."
        "Только давай условимся, что ты не скажешь маме о том, как я за тобой подглядывал в душе..." if alice.daily.shower == 3:
            Alice_12 "Хоть ты и тот ещё извращенец, Макс, но мне было сложно достать эти сигареты самой... Так и быть, мама ничего не узнает, по крайней мере в этот раз."
            Max_05 "Спасибо, Алиса! И я не извращенец. Просто проходил мимо, а там такая красотища..."
            Alice_05 "Ну да, ну да... Мимо он проходил..."
            $ punreason[1] = 0
            $ alice.daily.shower = 0
        "Держи!":
            if alice.GetMood()[0] < -1:
                Alice_05 "Хотя ты и полный придурок, но, похоже, начинаешь исправляться!"
                Max_08 "Я не полный придурок!"
                $ __mood += 50
            else:
                Alice_07 "Спасибо, Макс. Вот теперь я понимаю, ты настоящий брат!"
                Max_05 "Да не за что..."
    Alice_03 "Спасибо. И маме ни слова! У неё рука очень тяжёлая, особенно когда речь о сигаретах..."
    Max_01 "Конечно!"
    $ items['cigarettes'].use()
    $ __mood += 100
    $ spent_time += 10
    $ alice.dcv.special.set_lost(0) # теперь Алиса снова может курить
    $ AddRelMood('alice', 10, __mood, 3)
    return


label smoke_nofear:
    Alice_00 "Макс, поглазеть пришёл?"
    Max_09 "Не боишься, что мама накажет, если узнает?"
    menu:
        Alice_03 "И как она узнает? Ты расскажешь?"
        "Может быть...":
            Alice_12 "Ты хорошо подумал, Макс? Жизнь-то у тебя одна... И что ты хочешь за... молчание?"
            Max_01 "Вот это разговор!"
            menu:
                Alice_13 "Сначала скажи, что у тебя на уме..."
                "Дай $20, и я буду молчать":
                    pass
                "Если днём ты будешь ходить без трусов, буду молчать":
                    pass
                "Если будешь курить без верха, буду молчать":
                    pass
                "Если разрешишь тебя отшлёпать, ничего не скажу":
                    pass
                "Ничего. Не переживай!":
                    jump .no
            Alice_16 "А больше ты ничего не хочешь? Свали отсюда, пока не наваляла!!"
            $ AddRelMood('alice', 0, -100)
            $ poss['smoke'].open(2)
            $ alice.dcv.set_up.enabled = True
            $ punalice.append([2, 0, 0, 0, 0,]) # добавим самый первый элемент, чтобы можно было подставить Алису
            $ spent_time = 10
            jump Waiting
        "Нет, конечно!":
            jump .no
    menu .no:
        Alice_03 "Ну вот и пугать не надо. Не узнает. А если ты проболтаешься, я тебя во сне придушу, понял? Теперь иди, не мешай мне..."
        "Угу...":
            $ AddRelMood('alice', 0, 30)
            $ spent_time = 10
            jump Waiting


label smoke_fear:
    Alice_00 "Макс, поглазеть пришёл?"
    Max_09 "Не боишься, что мама накажет если узнает?"
    Alice_12 "Ты же ей не скажешь? Она так больно меня отшлёпала в прошлый раз, что до сих пор сидеть неприятно..."
    Max_01 "Ну, это зависит от тебя..."
    $ __can_nojeans = all(['kira' in chars, alice.clothes.casual.cur==0, 'pajamas' in alice.gifts])
    menu:
        Alice_13 "Говори, что ты хочешь за молчание?"
        "Дай $20, и я ничего не скажу" ('soc', get_chance_intimidate(punalice, 8)):
            jump .money
        "Если днём ты будешь ходить без трусов, буду молчать" ('soc', get_chance_intimidate(punalice, 4)) if alice.clothes.casual.cur==0:
            # пункт доступен, если Алиса носит джинсы
            jump .nopants
        "Если больше не будешь носить лифчик, буду молчать" ('soc', get_chance_intimidate(punalice, 3)):
            jump .sleep_toples
        "Если будешь курить без верха купальника, буду молчать" ('soc', get_chance_intimidate(punalice, 3)):
            jump .smoke_toples
        "Если хочешь, чтобы мама ничего не знала, ты будешь ходить без джинсов." if __can_nojeans:
            Alice_12 "Ходить без джинсов? А ты не обнаглел, Макс?!"
            Max_01 "Нет, нисколько. Согласна?"
            Alice_05 "И как ты себе это представляешь? Или в твоей извращённой фантазии мама просто не заметит, что я расхаживаю по дому в трусах?!"
            Max_02 "А ты снимай джинсы когда её нет дома и всё будет в порядке."
            Alice_13 "Ладно, тётя Кира ещё может на это и не обратит внимание, а если Лиза спросит, почему я без штанов?"
            Max_08 "Ой, Алиса, хватит уже искать отговорки... Как будто тебе бы и в голову не пришло сказать ей, что дома просто жарко."
            menu:
                Alice_06 "Лучше попроси что-то другое..."
                "Нет. Или получаешь вечером по заднице или не одеваешь джинсы." ('soc', get_chance_intimidate(punalice, 2)):
                    if rand_result:
                        $ poss['smoke'].open(4)
                        menu:
                            Alice_03 "[succes!t]Хорошо. Не буду я одевать джинсы, только дай уже покурить спокойно!"
                            "Конечно!":
                                $ punalice[0][0] = 7
                                $ alice.req.req = "nojeans"
                                $ alice.req.result = "nojeans"
                                $ added_mem_var('nojeans')
                                jump .end
                    else:
                        jump .fail2
                "Дай $20, и я ничего не скажу" ('soc', get_chance_intimidate(punalice, 8)):
                    jump .money
                "Если днём ты будешь ходить без трусов, буду молчать" ('soc', get_chance_intimidate(punalice, 4)) if alice.clothes.casual.cur==0:
                    # пункт доступен, если Алиса носит джинсы
                    jump .nopants
                "Если больше не будешь носить лифчик, буду молчать" ('soc', get_chance_intimidate(punalice, 3)):
                    jump .sleep_toples
                "Если будешь курить без верха купальника, буду молчать" ('soc', get_chance_intimidate(punalice, 3)):
                    jump .smoke_toples
        "Если разрешишь тебя отшлёпать, то я ничего не скажу!" if alice.dcv.private.stage > 4 and not alice.spanked:
            # если состоялось первое приватное наказание и Алиса сегодня ещё не отшлёпана
            if not alice.dcv.private.done:
                # накануне спасли попку Алисы от наказания
                $ poss['smoke'].open(4)
                jump alice_private_punish_r.smoke
            else:
                if not (punalice[1][2] or punalice[1][3]):
                    #если Алису не наказывали
                    Alice_12 "Это ещё с чего, Макс?! Меня же не наказывали! А мы договаривались, если ты меня спас от мамы, то и отшлёпать можешь..."  nointeract
                else: # punalice[1][3]:
                    # Ализа понесла наказание
                    Alice_12 "Это ещё с чего, Макс?! Ты же мою попку от мамы не спас! А мы договаривались, если ты меня выручаешь, то и отшлёпать можешь..."  nointeract
                menu:
                    "Но сейчас тебя есть за что отшлёпать!" ('soc', get_chance_intimidate(punalice)):
                        if rand_result:
                            $ poss['smoke'].open(4)
                            # удалось убедить
                            Alice_05 "[succes!t]Ну... Только если легонько! Понял?! Только докурю сперва в тишине и покое..."
                            menu:
                                Max_03 "Хорошо. Я подожду..."
                                "{i}подождать Алису{/i}":
                                    jump alice_private_punish_r.smoke_pun
                        else:
                            menu:
                                Alice_16 "[failed!t]Нет уж! Что-то другое ещё можешь попробовать выпросить, но к своей попке я тебя сегодня не подпущу."
                                "Дай $20, и я ничего не скажу" ('soc', get_chance_intimidate(punalice, 8)):
                                    jump .money
                                "Если днём ты будешь ходить без трусов, буду молчать" ('soc', get_chance_intimidate(punalice, 4)) if alice.clothes.casual.cur==0:
                                    # пункт доступен, если Алиса носит джинсы
                                    jump .nopants
                                "Если больше не будешь носить лифчик, буду молчать" ('soc', get_chance_intimidate(punalice, 3)):
                                    jump .sleep_toples
                                "Если будешь курить без верха купальника, буду молчать" ('soc', get_chance_intimidate(punalice, 3)):
                                    jump .smoke_toples
        "Хочу, чтобы ты спала голой!" ('soc', get_chance_intimidate(punalice, 2)) if all([eric.stat.mast, alice.flags.nakedpunish, flags.eric_photo1>0]):
            # если Эрик был хотя бы раз замечен на балконе Алисы и алису наказывали голой
            if rand_result:
                $ poss['smoke'].open(4)
                Alice_14 "Голой? Прямо совсем-совсем голой?! Что, фантазия закончилась, скатился до самого простейшего?"
                Max_07 "То же голое наказание, только без шлёпающей по твоей чудесной попке руки мамы. Просто подумал, ты бы и сама этого хотела."
                Alice_12 "Я то совсем не против спать голой, только вот ты же неспроста этого хочешь... Задумал что-то, Макс?! Ну-ка признавайся!"
                Max_03 "Всё ты какого-то подвоха от меня ждёшь! Спи себе голенькой в удовольствие, а мне уже от одной этой мысли на душе приятно."
                Alice_05 "Не знаю, зачем тебе, извращенцу, это нужно, но лучше я соглашусь на этот пустяк... Пока ты что-нибудь ещё не попросил."
                Max_04 "Вот и отлично!"
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                $ punalice[0][0] = 8
                $ alice.req.req = "naked"
                $ alice.req.result = "naked"
                $ alice.sleepnaked = True
                $ added_mem_var('alice_sleepnaked')
                jump .end
            else:
                jump .fail
        "Ты знаешь, я сегодня добрый...":
            $ punalice[0][0] = 1
            menu:
                Alice_06 "Сегодня? Значит, попросишь в следующий раз?"
                "Как знать, может быть...":
                    pass
                "Что ты! Нет, конечно...":
                    pass
            menu:
                Alice_13 "Ну вот тогда иди чем-нибудь займись, а меня не отвлекай..."
                "{i}уйти{/i}":
                    $ alice.req.reset()
                    jump .end

    label .smoke_toples:
        if rand_result:
            $ poss['smoke'].open(4)
            Alice_12 "[succes!t]Маленький извращенец... Ладно, но при условии, что маме не будешь ничего говорить. И разденусь только с завтрашнего дня. Договорились?"
            Max_03 "Само собой!"
            $ punalice[0][0] = 4
            $ alice.req.req = "toples"
            menu:
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                "{i}уйти{/i}":
                    jump .end
        else:
            jump .fail

    label .sleep_toples:
        if rand_result:
            $ poss['smoke'].open(4)
            Alice_03 "[succes!t]Да я вообще-то и так без лифчика все время хожу, только когда сплю одеваю..."
            Max_01 "Значит, тогда просто спи без него."
            Alice_05 "Не знаю, зачем тебе, извращенцу, это нужно, но лучше я соглашусь на этот пустяк... Пока ты что-нибудь ещё не попросил."
            Max_04 "Вот и отлично!"
            $ punalice[0][0] = 5
            $ alice.req.req = "sleep"
            $ alice.req.result = 'sleep'
            $ alice.sleeptoples = True
            $ added_mem_var('alice_sleeptoples')
            menu:
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                "{i}уйти{/i}":
                    jump .end
        else:
            jump .fail

    label .nopants:
        if rand_result:
            $ poss['smoke'].open(4)
            Alice_13 "[succes!t]Тебя так заботят мои трусы? Ну, хорошо. Всё равно я почти всё время в джинсах, так что не страшно. Значит, договорились?"
            Max_02 "Конечно!"
            $ punalice[0][0] = 6
            $ alice.req.req = "nopants"
            $ alice.req.result = 'nopants'
            $ alice.nopants = True
            $ added_mem_var('alice_nopants')
            menu:
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                "{i}уйти{/i}":
                    jump .end
        else:
            jump .fail

    label .money:
        if rand_result:
            $ poss['smoke'].open(4)
            $ punalice[0][0] = 3
            $ spent_time += 10
            $ alice.req.req = 'money'
            menu:
                Alice_12 "[succes!t]Ладно, Макс, я дам тебе денег, но только $10, ок?"
                "Нет, давай $20" ('soc', get_chance_intimidate(punalice, 2)):
                    if rand_result:
                        Alice_13 "[succes!t]Чёрт с тобой, Макс. Совсем без денег оставить хочешь... Сейчас принесу..."
                        Max_03 "Я жду..."
                        $ mgg.ask(1)
                        $ AddRelMood('alice', 0, -50)
                    else:
                        Alice_16 "[failed!t]Макс, не наглей! Сейчас принесу $10. Жди..."
                        Max_04 "Ну ладно, я жду..."
                        $ mgg.ask(0)
                        $ AddRelMood('alice', 0, -75)
                "Хорошо, устроит и $10":
                    $ mgg.ask(0)
                    $ AddRelMood('alice', 0, -25)
            menu:
                Alice_12 "Держи свои деньги... И больше меня не шантажируй. Я очень это не люблю... А теперь вали отсюда!"
                "Удачи!":
                    jump .end
        else:
            jump .fail

    label .fail:
        menu:
            Alice_16 "[failed!t]Ага, сейчас! Ну ты и хам, Макс... Всё, отвали, дай покурить спокойно..."
            "{i}уйти{/i}":
                $ alice.req.reset()
                $ punalice[0][0] = 2
                $ AddRelMood('alice', 0, -50)
                jump .end

    label .fail2:
        menu:
            Alice_12 "[failed!t]Вот так значит? А я вот выбираю вариант, в котором ты, может быть, останешься сегодня цел, если очень быстро свалишь отсюда и не будешь мне надоедать... Пока я ещё более-менее добрая."
            "{i}Ну, как скажешь...{/i}":
                $ alice.req.reset()
                $ punalice[0][0] = 2
                $ AddRelMood('alice', 0, -50)
                jump .end

    label .end:
        $ spent_time += 10
        jump Waiting


label smoke_toples:
    menu:
        Alice_02 "Ну что, извращенец, доволен видом?"
        "Доволен, конечно!":
            menu:
                Alice_05 "Надеюсь, маме ничего не расскажешь? А то это опасно для твоей жизни..."
                "Не переживай, не скажу":
                    Alice_04 "Вот и молодец. А теперь иди, займись чем-нибудь..."
                    Max_01 "Хорошо..."
                "Ну... это зависит от тебя!":
                    Alice_09 "Макс, не играй с огнём! Мы договоривались. А теперь сгинь с глаз моих!"
                    Max_07 "Уже ухожу..."
                    $ AddRelMood('alice', 0, -50)
        "А чего ты прикрываешься?":
            Alice_04 "А про руки мы не договаривались. Хочу - прикрываюсь. Хочу - нет. А тебя так радовать я точно не хочу... Так что вали уже..."
            Max_09 "Ну и ладно..."
        "Я передумал. Можешь одеться.":
            menu:
                Alice_12 "Спасибо, ваше величество! А чего это ты так расщедрился? Я больше не в твоём вкусе?"
                "Ну, я перегнул палку...":
                    menu:
                        Alice_04 "Спасибо, Макс! Это мудрый поступок... Но ты можешь в последний раз поглазеть..."
                        "{i}уйти{/i}":
                            $ AddRelMood('alice', 0, 100)
                "Это мой шаг к дружбе":
                    menu:
                        Alice_03 "Даже так?! Ну, дружбу я не обещаю, но могу пытаться с тобой как-то уживаться. А если серьёзно, то спасибо, Макс. Я это оценила..."
                        "{i}уйти{/i}":
                            $ AddRelMood('alice', 0, 120)
                "Да надоела!":
                    menu:
                        Alice_15 "Что?! А ну-ка вали отсюда, пока цел! И оденусь теперь, будь уверен!"
                        "{i}свалить{/i}":
                            pass
                "Ты знаешь, пусть всё остаётся как есть...":
                    menu:
                        Alice_12 "Ах вот как? Опять передумал? Всё, ты мне надоел, свали отсюда!"
                        "{i}свалить{/i}":
                            $ AddRelMood('alice', 0, -50)
                            $ spent_time += 10
                            jump Waiting
            $ alice.req.reset()
            $ alice.dcv.prudence.set_lost(0)

    label .end:
        $ spent_time += 10
        jump Waiting


label smoke_not_toples:
    Alice_02 "Ты чего-то хотел, Макс?"
    Max_07 "Да, хотел... Мы ведь договорились, что ты будешь курить без верха купальника!"
    Alice_13 "Знаешь, Макс, мне это надоело... Сколько можно? Я хочу спокойно курить и не волноваться, что ты за мной подглядываешь!"
    Max_09 "Ну хорошо, Алиса, как скажешь, можешь курить одетой. Только вот, если ты решила нарушить условия нашей договорённости, то почему бы тогда и мне не поступить так же?"
    Alice_06 "Только не надо маме рассказывать о об этом..."
    Max_00 "Всё зависит от тебя, сестрёнка... Если сейчас снимешь верх и в качестве извинения покажешь грудь, то я представлю, будто ты ничего не нарушала."
    Alice_15 "Ах ещё и грудь показать! Может сразу и полапать её дать?!"
    Max_03 "Очень заманчивое предложение... Но просто показать - я считаю справедливо! Сама накосячила..."

    $ renpy.show("Alice smoke "+renpy.random.choice(["01", "02", "03"])+"c")

    Alice_06 "Ладно, один разок и быстро... Но не вздумай маме рассказывать! Ни про это, ни про сигареты."
    Max_05 "Конечно, я ведь своё слово держу. Симпатичные сосочки!"
    menu:
        Alice_13 "Ну всё, полюбовался и хватит. Вали отсюда, дай спокойно покурить..."
        "Ага...":
            pass
    $ renpy.show("Alice smoke "+pose3_3+alice.dress)
    $ alice.req.reset()
    $ alice.dcv.prudence.set_lost(0)
    $ spent_time += 10
    $ current_room = house[5]
    jump Waiting


label smoke_nopants:
    menu:
        Alice_02 "Макс, чего хотел?"
        "Ничего, просто любуюсь...":
            Alice_13 "Налюбовался? А вот теперь постой в сторонке, пока я покурю! Давай, вали уже..."
            Max_01 "Хорошо, хорошо..."
        "А ты чего в трусах?":
            menu:
                Alice_12 "В каком смысле?!"
                "Мы же договорились - без трусов!":
                    Alice_01 "Ты совсем идиот, Макс? Я в купальнике. Это не трусы. А трусы я и так не ношу под джинсами. Можешь себе фантазировать теперь сколько хочешь... Всё, уйди с глаз моих долой!"
                    Max_01 "Ухожу, ухожу..."
                "Да шучу я...":
                    Alice_02 "Ты наверное думаешь, что у тебя забавные шутки, да? Так вот нет. Абсолютно несмешные, дебильные шутки, как и ты сам. Всё, свалил отсюда. Я занята..."
                    Max_01 "Как скажешь..."
        "Я передумал. Можешь носить трусы...":
            menu:
                Alice_03 "А чего передумал? А, хотя не важно. Я рада, а то мне всё натирает в джинсах... Хотя, тебе такие подробности знать не нужно. Спасибо за разрешение, ваше величество. Теперь дай покурю..."
                "{i}уйти{/i}":
                    $ alice.req.reset()
                    $ alice.dcv.prudence.set_lost(0)
                    $ alice.nopants = False
                    $ AddRelMood('alice', 0, 100)

    $ spent_time += 10
    jump Waiting


label smoke_not_nopants:
    Alice_02 "Ты чего-то хотел, Макс?"
    Max_09 "Алиса, ну что за дела?! Я думал у нас уговор!"
    Alice_06 "Это ты сейчас о чём, Макс?"
    Max_08 "Мы ведь договорились, что ты не будешь одевать трусы днём. А я их на тебе видел!"
    Alice_14 "А мне вот интересно, когда это ты их мог увидеть?! Подглядывал, как я одеваюсь?"
    Max_07 "Да здесь и подглядывать не нужно, они у тебя иногда прямо из-под джинс слегка торчат... Так что важно не то, как и где я это увидел, а то, что они на тебе были!"
    Alice_00 "Ладно, ладно, признаю, я их снова ношу, потому что без них мне все натирает. Да и мама, если видит, что я без трусов во время наказания, шлепает гораздо сильней."
    Max_00 "Ну хорошо, я тебя освобождаю от уговора. Но только, если в качестве компенсации ты прямо сейчас покажешь мне сиськи!"
    Alice_16 "А не многого ли ты, мелкий извращенец, хочешь?!"
    Max_01 "Посмотреть на красивые сиськи - не извращение! И мне кажется, проще один раз показать, чем всё натирать будет..."

    $ renpy.show("Alice smoke "+renpy.random.choice(["01", "02", "03"])+"c")

    Alice_06 "Ну на, любуйся, раз уж и дня не можешь прожить без извращений."
    Max_03 "Классные сиськи!"
    Alice_13 "Спасибо. А теперь иди уже, погуляй где-нибудь. Дай докурить спокойно."
    Max_01 "Хорошо. Я ушёл..."

    $ added_mem_var('alice_not_nopants')
    $ renpy.show("Alice smoke "+pose3_3+alice.dress)
    $ alice.req.reset()
    $ alice.dcv.prudence.set_lost(0)
    $ spent_time += 10
    $ current_room = house[5]
    jump Waiting


label smoke_sleep:
    menu:
        Alice_02 "Макс, чего хотел?"
        "Ничего, просто любуюсь...":
            Alice_13 "Налюбовался? А вот теперь постой в сторонке, пока я покурю! Давай, вали уже..."
            Max_01 "Хорошо, хорошо..."
            $ spent_time += 10
            jump Waiting

        "Я передумал. Ты можешь спать в лифчике, если хочешь." if alice.req.req=='sleep':
            pass
        "Я передумал. Ты можешь спать в нижнем белье..." if alice.req.req=='naked':
            pass
    menu:
        Alice_04 "А чего это ты передумал? А, хотя не важно. Я рада, а то мне неудобно ночью, если выйти куда-то нужно, да и мама заметить может. Спасибо за разрешение, ваше величество. Теперь дай покурю..."
        "{i}уйти{/i}":
            pass

    $ alice.req.reset()
    $ alice.dcv.prudence.set_lost(0)
    $ AddRelMood('alice', 0, 100)

    $ spent_time += 10
    jump Waiting


label smoke_nojeans:
    menu:
        Alice_02 "Макс, чего хотел?"
        "Ничего, просто любуюсь...":
            Alice_13 "Налюбовался? А вот теперь постой в сторонке, пока я покурю! Давай, иди уже..."
            Max_01 "Ладно, ладно, как скажешь..."
        "Я передумал. Ты можешь носить свои джинсы, если захочешь.":
            menu:
                Alice_04 "Чего это ты вдруг передумал? Надоело глазеть на мою попку? А, не важно. Спасибо за разрешение, ваше величество. Теперь дай покурю..."
                "{i}уйти{/i}":
                    $ alice.req.reset()
                    $ alice.dcv.prudence.set_lost(0)
                    $ AddRelMood('alice', 0, 100)
    $ spent_time += 10
    jump Waiting


label Alice_sorry:
    # $ renpy.dynamic('waiting_days')
    $ waiting_days = 1
    if len(alice.sorry.give) == 0:      # Первый диалог
        Alice_15 "Ух ты, у тебя, извращенца мелкого, совесть проснулась?! Неожиданно..."
        Max_10 "Нет, я думаю, ты вряд ли правильно поняла то, что случилось. Я за тобой не подглядывал..."
        Alice_16 "Макс, я по-твоему полная дура что ли?! Ты стоял за стеной, и нагло смотрел, как я принимала душ!"
        Max_14 "Но на деле же, так получилось не специально... Я просто шёл мимо..."
        Alice_05 "Да, да, конечно... Я очень хочу посмотреть, что с тобой сделает мама, когда об этом узнает..."
        Max_10 "Да, знаю, в такое очень трудно поверить, но я просто шёл мимо, а ты душ как раз принимала... Ну я и отскочил к стене... где ты меня и заметила... Вот и всё, я даже и не видел ничего такого!"
        Alice_03 "Ну вот никак мне в это не верится, Макс! Никаких твоих оправданий не хватит, чтобы я в это поверила."
        Max_07 "В таком случае, предлагаю представить, что ничего такого утром не было. Ты ничего не говоришь маме, а я в свою очередь куплю тебе чего-нибудь вкусненького?"
        if weekday == 6:
            Alice_08 "Ах ты... паршивец... Это подлый ход, потому что от вкусняшки я бы не отказалась... Хорошо, но обещать ничего не буду, сперва посмотрю, что это будет за вкусность... Если ты конечно успеешь до вечера понедельника!"
            Max_01 "Обязательно успею! В понедельник всё будет..."
        else:
            Alice_08 "Ах ты... паршивец... Это подлый ход, потому что от вкусняшки я бы не отказалась... Хорошо, но обещать ничего не буду, сперва посмотрю, что это будет за вкусность... Если ты конечно успеешь до завтрашего вечера!"
            Max_01 "Обязательно успею! Завтра всё будет..."
        Alice_07 "И смотри, чтобы мне понравилось..."
        Max_04 "Хорошо."
        $ alice.sorry.valid = {'ritter-m', 'raffaello-m', 'ferrero-m'}
        if not all([items['ritter-m'].InShop, items['raffaello-m'].InShop, items['ferrero-m'].InShop]):
            $ notify_list.append(_("В интернет-магазине доступен новый товар."))
        $ items['ritter-m'].unblock()
        $ items['raffaello-m'].unblock()
        $ items['ferrero-m'].unblock()
        $ poss['risk'].open(0)
    elif len(alice.sorry.give) == 1:    # Второй диалог
        Alice_03 "Ой, Макс, конечно же я тебя прощаю! Не переживай ты так... Всё прекрасно!"
        Max_09 "Э-э-э... Правда?!"
        Alice_16 "Конечно нет, дубина! Стоял снова и глазел на меня голую! Мама обязательно об этом узнает..."
        Max_08 "А вдруг это была случайность и ты напрасно меня сдашь?"
        Alice_12 "Макс, какая это случайность, стоять за углом и глазеть на меня?!"
        Max_07 "Понимаю, верится с большим трудом. Тогда давай это разрешим без мамы?"
        Alice_05 "Снова хочешь попробовать купить моё молчание сладостью? Серьёзно?!"
        Max_10 "Да, серьёзно! Попытка - не пытка..."
        Alice_02 "Ты, конечно, можешь попробовать, от чего-нибудь сладенького я не откажусь, но ты же понимаешь, что мне должно это очень понравиться."
        if weekday == 6:
            Max_01 "Значит, до ужина понедельника?"
        else:
            Max_01 "Значит, до следующего ужина?"
        Alice_05 "Ничего не обещаю, но не опаздывай, Макс!"
        Max_04 "Постараюсь."
    elif len(alice.sorry.give) == 2:    # Третий диалог
        Alice_05 "Макс, а давай всё упростим до того, что ты сейчас уходишь покупать мне конфеты, а я их жду до следующего ужина? Как тебе, а?!"
        Max_08 "Можно и так... Только мне как-то немного не по себе от того, что это предлагаешь ты, а не я!"
        Alice_03 "Просто экономлю время, которое тебе лучше потратить на то, чтобы я в итоге осталась очень довольна этим."
        Max_07 "Тогда я пойду, да?"
        Alice_01 "Бегом! Извращенец тормозной..."
        Max_01 "Ага..."
    elif len(alice.sorry.give) == 3 and 'pajamas' not in alice.gifts:   # Четвёртый диалог - пижамка
        Alice_05 "Но ведь не только это! Ясно же, что снова пообещаешь вкусняшку за моё молчание."
        Max_07 "Ну а что мне ещё остаётся?"
        Alice_03 "Только вот на этот раз Я буду ставить условия! Сладости - это хорошо, но я хочу большего..."
        Max_09 "И чего такого ты хочешь?"
        Alice_07 "Хочу себе новую одежду, а то надоело в одном и том же дома сидеть. А именно - пижаму!"
        Max_05 "Пижаму?! А при чём тут пижама, в ней же спать положено? А если надоела одежда, просто сними её и сиди в нижнем белье. Или голая!"
        Alice_05 "Конечно, тебе бы это понравилось! Но я не хочу спать в пижаме. Я почти всё время провожу дома и хочу одевать что-то лёгкое."
        Max_07 "Тогда это должна быть какая-нибудь коротенькая пижама!"
        Alice_02 "Именно! Хочу лёгкие топик и шортики для дома. И ты мне их купишь, если не хочешь получить по заднице от мамы."
        Max_08 "Хорошо, но мне нужно больше времени..."
        Alice_01 "Согласна подождать три дня. А ты не тормози..."
        Max_00 "Хорошо."
        $ alice.sorry.valid.clear()
        $ items['pajamas'].unblock()
        $ poss['risk'].open(8)
        $ waiting_days = 3
    elif 'sexbody2' in alice.gifts and 'mistress1' not in alice.gifts:  # Пятый диалог - кожаный костюм
        Alice_05 "Это, конечно, очень здорово, Макс. Дай угадаю... Сейчас ты пообещаешь купить мне сладостей, чтобы мама не узнала, какой ты извращенец, верно?"
        Max_01 "Верно. Но ты, видимо, хочешь чего-то другого?"
        Alice_01 "О да, Макс! У меня есть кое-какие мыслишки, как отучить тебя от этих \"случайных\" подглядываний за мной."
        Max_04 "А может я лучше сам себя отучу..."
        Alice_02 "Ну уж нет! Макс, ты что?! У нас здесь очень тяжёлый случай - хронический вуайеризм! Но не переживай, уж я возьмусь за твоё лечение... Но это позже... Сейчас, мне нужно кое-что другое."
        Max_07 "Другое? И что же?"
        Alice_05 "Я тут подумала, что в этот раз стильный кожаный костюмчик вполне мог бы спасти твою задницу от маминого наказания. Их ещё используют в ролевых играх..."
        Max_08 "Ничего себе запросики! И зачем тебе такой? Перед кем ты собираешься его демонстрировать?"
        Alice_03 "А вот есть перед кем... Но это не твоё дело, Макс, кому я его продемонстрирую."
        Max_02 "Ну, интересно же..."
        Alice_07 "Не сомневаюсь! Наверняка уже во всю представляешь, как я его при тебе буду примерять, но не угадал."
        Max_09 "Эй, но так же не интересно!"
        Alice_16 "Это что вообще за недовольства?! Наверное, я погорячилась со свои заказом и тебя нужно просто отправить маме, которая отучит тебя подглядывать."
        Max_08 "Э-э-э... Да ладно тебе! Чего ты сразу? Я же просто так... без задней мысли ляпнул..."
        Alice_12 "Ну конечно, без задней, у тебя все мысли только \"передние\"... Думать надо, что говоришь, особенно когда находишься в таком шатком положении. Ну так что, принимаешь моё предложение?"
        Max_09 "Так-то да, принимаю, но..."
        Alice_17 "Что, но?"
        Max_10 "Но ведь это, наверняка, стоит очень дорого."
        Alice_05 "Ну конечно, ведь всё имеет свою цену. Это только подглядывать за собственной сестрой и дрочить на неё в тихушку ничего не стоит!"
        Max_08 "Эй... Я не дрочил!"
        Alice_03 "Ага, давай рассказывай... Короче, это твои проблемы, где ты возьмёшь деньги. И не тормози, если не хочешь получить по заднице от мамы."
        Max_09 "Ладно... Я постараюсь."
        Alice_01 "Да уж, постарайся. И не затягивай, я не буду ждать вечно. Если уложишься в четыре дня, то мама, так уж и быть, ничего не узнает."
        Max_00 "Я понял..."
        $ alice.sorry.valid.clear()
        $ items['mistress1'].unblock()
        $ poss['risk'].open(11)
        $ waiting_days = 4
    elif 'mistress1' in alice.gifts and 'whip' not in alice.gifts:      # Шестой диалог - стек
        Alice_05 "Да неужели?! И что, хочешь снова, как всегда, откупиться?"
        Max_01 "Ну-у... да... Мне как, бежать за сладостями или, как в тот раз, тебе нужно что-то другое?"
        Alice_02 "Ты проницателен как никогда, Макс, именно другое..."
        Max_04 "И что же это?"
        Alice_01 "Плётка!"
        Max_08 "Что? Плётка?! Я не ослышался?"
        Alice_03 "Нет-нет, всё верно - мне нужна плётка. Она вроде стеком называется. Ну знаешь, которой лошадок подгоняют."
        Max_09 "Я стесняюсь спросить, а кого ты собираешься ей подгонять?"
        Alice_05 "Тебя, Макс, кого же ещё!"
        Max_10 "Э-э-э... А серьёзно?"
        Alice_12 "А я как раз серьёзно. Меня уже достали твои подглядывания! Может быть теперь ты подумаешь о последствиях, прежде чем засунешь свой длинный нос ко мне в ванную комнату."
        Max_08 "Так я же случайно..."
        Alice_07 "Ха-ха... Ладно, я шучу! Видел бы ты сейчас своё лицо!"
        Max_07 "Фух... Отстойные у тебя шутки, Алиса!"
        Alice_05 "Сам ты отстойный! Короче, мне нужна плётка, чтобы дополнить тот кожаный костюм. В противном случае, будешь объясняться с мамой о своём фетише."
        Max_09 "Ладно, я понял..."
        Alice_03 "Вот и хорошо. Я готова подождать три дня, а там пеняй на себя."
        Max_00 "Ага..."
        $ alice.sorry.valid.clear()
        $ items['whip'].unblock()
        $ poss['risk'].open(13)
        $ waiting_days = 3
    elif 'whip' in alice.gifts and poss['risk'].st() < 15:              # Седьмой диалог - переход на доминирование
        Alice_05 "Ух ты! Неужели у тебя, мелкого извращенца, проснулась совесть и ты решил сразу замолить свои грехи?"
        Max_07 "Чего сразу грехи-то? Просто небольшая слабость..."
        Alice_12 "А то, что подглядывать за голой сестрой это грех! Или ты этого не знал? В общем собирайся и пошли к маме... Очень хочется посмотреть, что она с тобой сделает, когда об этом узнает..."
        Max_01 "Так может мы договоримся, как раньше? Может быть тебе что-то надо?"
        Alice_13 "Ай-ай-ай... Пытаешься меня подкупить?"
        Max_08 "Почему сразу подкупить?"
        Alice_05 "А как ещё это можно назвать? Взятка? Кстати, за неё тоже предусмотрено наказание."
        Max_10 "Так я ведь хотел..."
        Alice_07 "Откупиться и избежать наказания... Ха-ха-ха... Ладно, Макс, не парься, я пошутила. Я сегодня добрая и потому наказывать тебя не буду... пока что."
        Max_09 "В каком смысле, пока что?!"
        Alice_03 "Ну... Я решила отложить твоё наказание. С этого момента, если есть за что извиниться, можешь подходить ко мне вечером, когда я смотрю ТВ. И уже тогда я скажу, что с тобой будет..."
        Max_07 "И что будет этим вечером?"
        Alice_05 "Сказала же, вечером узнаешь. Если, конечно, не решишь, что лучше позориться перед всеми нами у мамы на коленях. А сейчас можешь идти."
        Max_00 "Хорошо..."
        $ alice.sorry.valid.clear()
        $ poss['risk'].open(15)
        $ alice.dcv.mistress.set_lost(1)
        $ flags.mistres_pun = True
        $ waiting_days = 0

    $ punreason[1] = 0
    $ alice.daily.shower = 0
    # $ print(waiting_days)
    if waiting_days:
        $ alice.sorry.start(waiting_days)
    $ spent_time += 10
    jump Waiting


label gift_dress:
    Alice_15 "Макс? Это платье для клуба? Правда?!"
    Max_01 "Ага..."
    menu:
        Alice_07 "Спасибо, Макс! Ты такой... Не знаю даже, я просто в шоке!"
        "Держи...":
            jump .gift
        "Не так быстро...":
            menu:
                Alice_02 "Так и знала, что есть какой-то подвох... И что ты хочешь за него?"
                "Да ничего, просто держи...":
                    jump .gift
                "Устрой мне показ в нём...":
                    Alice_05 "Ты хочешь, чтобы я его примерила прямо при тебе?"
                    Max_03 "Конечно! Я это и хочу!"
                    Alice_03 "Макс... А жить... хочешь?"
                    Max_07 "Эй, что за угрозы?"
                    jump .newdress_show

    label .gift:
        Alice_02 "Вот так вот сразу и без подвоха? Обалдеть... Не ожидала от тебя, Макс... Спасибо!"
        Max_04 "Не за что!"
        $ AddRelMood('alice', 0, 300)
        $ AttitudeChange('alice', 0.9)
        jump .end

    label .newdress_show:
        if '09:00' <= tm < '20:00':
            $ __suf = ""
        else:
            $ __suf = "a"

        if "06:00" <= tm < "11:00":
            scene location house aliceroom door-morning
        elif "11:00" <= tm < "18:00":
            scene location house aliceroom door-day
        elif "18:00" <= tm < "22:00":
            scene location house aliceroom door-evening
        else:
            scene location house aliceroom door-night

        menu:
            Alice_03 "Жди за дверью. Я сейчас надену платье и тебе покажу, так уж и быть..."
            "Э... Хорошо...":
                pass
        if __suf == "":
            scene BG char Alice newdress
        else:
            scene BG char Alice spider-night-05
        $ renpy.show("Alice newdress 01"+__suf)
        with fade4
        Alice_05 "Ну как, Макс? Мне идёт?"
        Max_05 "Выглядишь... шикарно!"
        $ renpy.show("Alice newdress 02"+__suf)
        Alice_07 "Спасибо, Макс! Честно говоря, я не ожидала от тебя такого подарка. Спасибо! И..."
        Max_07 "И?"
        $ renpy.show("Alice newdress 03"+__suf)
        menu:
            Alice_05 "...И небольшой бонус. Я знаю, что ты ждал чего-то подобного..."
            "Очень... очень хорошо...":
                pass
            "А можешь наклониться?":
                pass
        $ renpy.show("Alice newdress 04"+__suf)
        Alice_02 "Хорошего в меру... Правда, ты меня очень сильно выручил. Спасибо ещё раз!"
        Max_01 "Не за что!"
        $ AddRelMood('alice', 0, 200)
        $ AttitudeChange('alice', 0.9)
        $ spent_time += max((50 - int(tm[-2:])), 30)
        $ current_room = house[5]

    label .end:
        $ items['dress'].give()
        $ poss['nightclub'].open(4)
        $ alice.gifts.append('dress')
        $ alice.dcv.feature.set_lost(1)
        $ infl[alice].add_m(40, True)
        $ spent_time += 10
        jump Waiting


label gift_book:
    if items['erobook_1'].have:
        Alice_02 "У тебя для меня подарок? У ТЕБЯ... для МЕНЯ? Какая прелесть. Давай, показывай, что за книжка?"
        Max_01 "Держи..."
        menu:
            Alice_01 "Прикольно... Давно хотела её почитать. А ты как узнал, что мне такие нравятся?"
            "Порылся в твоих вещах и нашёл, что читаешь!":
                Alice_14 "Что?! Да как ты посмел?!"
                Max_02 "Да я пошутил. Просто угадал!"
                Alice_13 "Шуточки у тебя, как и прежде, дурацкие! А книжку я возьму. Молодец, что угадал... Спасибо."
                Max_04 "Не за что"
            "Ну, я догадался! Я же умный!":
                Alice_07 "Умный он... Ну, молодец, что догадался. Спасибо, Макс! Если ещё попадутся из этой серии, буду рада принять их от тебя. Безвозмездно!"
                Max_04 "Хорошо..."
            "Я и не знал. Просто угадал видимо...":
                Alice_05 "Поздравляю, попал в десятку! Если найдёшь ещё что-то подобное, буду рада такому подарку. Даже от тебя..."
                Max_04 "Ну, если даже от меня, то ладно..."
        $ poss['secretbook'].open(3)
        $ AddRelMood('alice', 0, 100)
        $ AttitudeChange('alice', 0.25)
        $ items['erobook_1'].give()
        $ alice.gifts.append('erobook_1')
        $ alice.dcv.gifts.set_lost(7) # Покупка второй книги возможна через неделю.
        $ alice.dcv.gifts.stage = 2
    elif items['erobook_2'].have:
        Alice_04 "Да? И какая на этот раз? Давай сюда..."
        Max_01 "Держи..."
        Alice_07 "Супер! Ты меня удивляешь, Макс! Если ещё что будет почитать, приноси. Я люблю подобную... литературу."
        Max_04 "Конечно!"
        $ AddRelMood('alice', 0, 120)
        $ AttitudeChange('alice', 0.3)
        $ items['erobook_2'].give()
        $ alice.gifts.append('erobook_2')
        $ alice.dcv.gifts.set_lost(9) # Покупка третьей книги возможна через девять дней.
        $ alice.dcv.gifts.stage = 3
    elif items['erobook_3'].have or items['erobook_4'].have:
        Alice_04 "Супер! Давай, показывай, что тут у нас..."
        Max_01 "Держи..."
        Alice_05 "То, что нужно! Если ещё что будет почитать, приноси. Ты же знаешь, как я люблю такие книги..."
        Max_04 "Конечно!"
        $ AddRelMood('alice', 0, 100)
        $ AttitudeChange('alice', 0.25)
        if items['erobook_4'].have:
            $ items['erobook_4'].give()
            $ alice.gifts.append('erobook_4')
            $ alice.dcv.gifts.set_lost(13) # Покупка пятой книги возможна через тринадцать дней.
            $ alice.dcv.gifts.stage = 5
        else:
            $ items['erobook_3'].give()
            $ alice.gifts.append('erobook_3')
            $ alice.dcv.gifts.set_lost(11) # Покупка четвертой книги возможна через одинадцать дней.
            $ alice.dcv.gifts.stage = 4
    elif items['erobook_5'].have:
        Alice_04 "Да? И какая на этот раз? Давай сюда..."
        Max_01 "Держи..."
        Alice_07 "Забавная книжка. Давно хотела почитать... Спасибо, Макс. Ты меня балуешь!"
        Max_04 "Конечно!"
        $ AddRelMood('alice', 0, 160)
        $ AttitudeChange('alice', 0.4)
        $ items['erobook_5'].give()
        $ alice.dcv.gifts.stage = 6
        $ alice.gifts.append('erobook_5')

    $ spent_time += 10
    return


label gift_pajamas:
    if not _in_replay:
        if 'gift_pajamas' not in persistent.memories:
            $ persistent.memories['gift_pajamas'] = -1
    else:
        # формируем фон для воспоминания
        if alice.plan_name == 'sun':
            call alice_sun from _call_alice_sun
        else:
            if tm > '20:00':
                call alice_evening_closer from _call_alice_evening_closer
            else:
                call alice_morning_closer from _call_alice_morning_closer
    Alice_06 "Только скажи, что это пижамка, а не сладости! Ты же купил то, что я просила?!"
    Max_04 "Конечно! Топик и шортики, как ты хотела. Вот, держи..."
    Alice_07 "О да! Какие симпатичные! Ты такой молодец, Макс! Спасибо тебе большое..."
    Max_03 "Ну что, примеришь при мне?"
    if not alice.sorry.owe:  # не успел подарить пижамку вовремя
        Alice_04 "А жирно тебе не будет?! В душе не нагляделся на меня и теперь хочешь подсмотреть, как я переодеваюсь, да?"
        Max_01 "Нет, просто хотел увидеть, как на тебе будет смотреться пижама..."
        Alice_05 "Ладно, поверю... Ого, а что это у тебя здесь..."   #спрайт с ушами
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."
    elif alice.flags.hugs_type > 3: # после 3-ей сладости были родственные обнимашки
        if not _in_replay:
            $ persistent.memories['gift_pajamas'] = 1
        Alice_03 "Примерю при тебе? Об этом мы не договаривались. Я покажусь в ней, но... Хотя, ладно. Примерю при тебе, но ты не подглядывай! Увижу, что смотришь, получишь и пойдёшь в бассейн. Вниз головой."
        Max_02 "Как страшно... Давай уже, примеряй."
        scene BG char Alice newpajamas
        $ __suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
        if not ('09:00' <= tm < '20:00'):
            $ __suf += 'e'
        $ renpy.show('Alice newpajamas 01'+__suf)
        with fade4
        if not _in_replay:
            $ SetCamsGrow(house[1], 150)
        menu:
            Alice_05 "Макс, у тебя же есть инстинкт самосохранения, верно? Не вздумай подглядывать!"   #примерка в комнате/спрайт в одежде (01)
            "Ага, я и не подглядываю...":
                if renpy.random.randint(0, 1):      # линейка началась без верха
                    $ renpy.show('Alice newpajamas 02'+__suf)
                    Alice_01 "Макс! Ты что, пялишься на мою грудь? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"   #спрайт без верха (02)
                    Max_03 "Я не пялюсь..."
                    $ renpy.show('Alice newpajamas 04'+__suf)
                    Alice_02 "Похоже, размер мне подходит... и удобно. Очень лёгонький топик. Ну, как тебе?"   #спрайт с одетым топиком (04)
                    Max_04 "Тебе идёт! Мне нравится..."
                    if alice.req.result != 'nopants':
                        Alice_03 "Отлично! А теперь отвернись, не подглядывай! Нужно ещё шортики примерить."   #спрайт в топике без низа, но в трусиках (если бикини, то без трусиков) (06)
                        if not _in_replay:
                            $ SetCamsGrow(house[1], 180)
                    else:
                        Alice_05 "Класс! А теперь быстро отвернись, а то на мне трусиков нет, благодаря твоим уговорам! Нужно ещё шортики примерить."   #спрайт в топике без низа, трусиков по уговору нет
                    $ __suf = 'an' if any([alice.plan_name in ['sun', 'swim'], alice.dress=='d', alice.req.result == 'nopants']) else 'a'
                    if not ('09:00' <= tm < '20:00'):
                        $ __suf += 'e'
                    $ renpy.show('Alice newpajamas 06'+__suf)
                    if any([alice.req.result != 'not_nopants', alice.plan_name in ['sun', 'swim'], alice.dress=='d']):
                        Max_02 "Конечно, я не смотрю..."
                    else:
                        Max_08 "Конечно, я не смотрю... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"   #если на Алисе трусики, но их не должно быть
                        Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                        Max_01 "Ладно, считай, я ничего не видел."
                    if '09:00' <= tm < '20:00':
                        show Alice newpajamas 08
                    else:
                        show Alice newpajamas 08e
                    Alice_07 "Размер в самый раз... Удобненько и легко. Как тебе, Макс? Хорошо сидит?"   #спрайт с одетыми топиком и шортиками (08)
                    Max_05 "Не то слово, всё выглядит шикарно!"
                else:           # линейка началась без низа
                    $ __suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
                    if __suf=='a' and alice.req.result == 'nopants':  # если Алиса в обычной одежде и без трусиков
                        $ __suf += 'n'
                    if not ('09:00' <= tm < '20:00'):
                        $ __suf += 'e'
                    $ renpy.show('Alice newpajamas 03'+__suf)
                    if alice.req.result != 'nopants':
                        Alice_03 "Макс! Ты что, пялишься на мой зад? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"   #линейка началась без низа, но в трусиках (03)
                    else:
                        if not _in_replay:
                            $ SetCamsGrow(house[1], 180)
                        Alice_05 "Макс! Ты что, пялишься на мой зад? Быстро отвернись, на мне же нет трусиков, благодаря твоим уговорам!"   #линейка началась без низа, трусиков по уговору нет
                    if alice.req.result != 'not_nopants' or alice.plan_name in ['sun', 'swim']:
                        Max_02 "Я не пялюсь..."
                    else:
                        Max_08 "Я не пялюсь... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"   #если на Алисе трусики, но их не должно быть
                        Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                        Max_01 "Ладно, считай, я ничего не видел."
                    $ __suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
                    if not ('09:00' <= tm < '20:00'):
                        $ __suf += 'e'
                    $ renpy.show('Alice newpajamas 05'+__suf)
                    Alice_02 "Размер в самый раз... Удобненько и легко. Как тебе, Макс? Хорошо сидят?"   #спрайт с одетыми шортиками (05)
                    Max_04 "Не то слово, сидят прекрасно!"
                    Alice_01 "Здорово! А теперь отвернись, не подглядывай! Нужно ещё топик примерить."   #спрайт в шортиках без верха (07)
                    if '09:00' <= tm < '20:00':
                        show Alice newpajamas 07
                    else:
                        show Alice newpajamas 07e
                    Max_03 "Конечно, я не смотрю..."
                    if '09:00' <= tm < '20:00':
                        show Alice newpajamas 08
                    else:
                        show Alice newpajamas 08e
                    Alice_07 "Похоже, размер мне подходит... и удобно. Очень лёгонький топик. Ну, как тебе всё в целом?"   #спрайт с одетыми топиком и шортиками (08)
                    Max_05 "Тебе идёт, всё выглядит шикарно!"
        Alice_03 "Спасибо тебе ещё раз! Иди ко мне, я тебя приобниму... немного."
        Max_04 "О, это я с радостью!"
        scene BG char Alice newdress
        if '09:00' <= tm < '20:00':
            $ renpy.show("Alice hugging aliceroom 02b"+mgg.dress)
        else:
            $ renpy.show("Alice hugging aliceroom 02b"+mgg.dress+'e')
        Alice_05 "Но ты не зазнавайся, Макс. В следующий раз тебе может так не повезти, как сегодня."   #спрайт с обнимашками в комнате
        Max_02 "Буду иметь ввиду, сестрёнка."
        Alice_02 "Всё, давай шуруй по своим делам, не надоедай мне."
        Max_01 "Ага..."
        if not _in_replay:
            $ spent_time += 20
    elif alice.flags.hugs_type > 2: # после 3-ей сладости было прощение без выкручивания ушей
        Alice_04 "А жирно тебе не будет?! В душе на меня глазел, а теперь и здесь хочешь подглядеть... Нет уж! Но за пижамку я тебя всё же обниму! Ну так... совсем немного..."   #спрайт с обнимашками"
        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs
        Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
        Alice_07 "Не смотря на твои замашки, ты всё-таки купил мне пижамку, которую я просила. Вот я и не вредничаю..."
        Max_05 "Да, надо бы почаще так делать."
        Alice_02 "Подглядывать или что-нибудь мне дарить?!"
        Max_02 "Второе, конечно!"
        Alice_05 "Ну да, конечно... Иди давай."
    elif alice.flags.hugs_type > 1: # после 3-ей сладости было выкручивание ушей
        menu:
            Alice_04 "А жирно тебе не будет?! В душе не нагляделся на меня и теперь хочешь подсмотреть, как я переодеваюсь, да?"
            "Нет, просто хотел увидеть, как на тебе будет смотреться пижама..." ('soc', mgg.social * 3, 90):
                if rand_result:
                    Alice_03 "[succes!t]Ладно, поверю, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                    Max_07 "Что, вот так вот просто?!"
                    Alice_05 "Ну, ты обещал купить мне пижаму и сдержал слово. А я сейчас более-менее добрая... Так что не искушай судьбу!"
                    Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                else:
                    Alice_05 "[failed!t]Ладно, поверю, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
                    call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_1
                    Max_12 "А-а-ай! Мне же больно, Алиса!"
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    Max_10 "Да я же случайно оказался около душа..."
                    Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                    Max_14 "Ой! Я понял... Больше не буду!"
                    Alice_02 "Вот и молодец! Гуляй..."
    else:  # после 3-ей сладости было наказание
        Alice_04 "А жирно тебе не будет?! В душе не нагляделся на меня и теперь хочешь подсмотреть, как я переодеваюсь, да?"
        Max_01 "Нет, просто хотел увидеть, как на тебе будет смотреться пижама..."
        Alice_05 "Ладно, поверю, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_2
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."

    $ renpy.end_replay()

    if alice.flags.hugs_type > 3:
        $ poss['risk'].open(9)
    else:
        $ poss['risk'].open(10)

    $ AddRelMood('alice', 0, 200)
    $ AttitudeChange('alice', 0.9)
    $ items['pajamas'].give()
    $ alice.gifts.append('pajamas')
    $ added_mem_var('pajamas')
    $ setting_clothes_by_conditions()
    $ infl[alice].add_m(40, True)

    $ alice.sorry.valid = {'ferrero-b', 'ferrero-m'}

    $ alice.sorry.give.append(4)
    $ spent_time += 10
    $ alice.sorry.owe = False
    jump Waiting


label Alice_solar:
    $ alice.hourly.sun_cream = 1
    ## Загораешь?
    menu:
        Alice_02 "Как ты догадался, Шерлок?"
        "Может быть, тебя намазать кремом для загара?" if 3 > alice.daily.oiled > 0:
            Alice_04 "Достаточно на сегодня, Макс..."
            Max_00 "Ясно. Ну, тогда, может, завтра..."
            $ alice.daily.oiled += 2
            jump AfterWaiting
        "Может быть, тебя намазать кремом для загара?" if not items['solar'].have:  # нет крема
                Alice_13 "Может быть. Вот только у меня его нет..."
                Max_00 "Ясно. Ну, в другой раз значит..."
                if not any([items['max-a'].InShop, items['max-a'].have]):
                    Max_09 "{m}Такой крем наверняка можно найти в интернет-магазине. Да и прежде чем пытаться поприставать к сестрёнке таким образом, стоит обзавестись одеждой полегче.{/m}"
                    $ items['solar'].unblock()
                    $ items['max-a'].unblock()
                    $ notify_list.append(_("В интернет-магазине доступен новый товар."))
                    $ poss['massage'].open(0)
                jump AfterWaiting
        "{i}Предложить Алисе намазать её кремом{/i}" if items['solar'].have and alice.daily.oiled==0 and any([mgg.dress == 'a', kol_cream < 3]):
            if mgg.dress == 'a':  # Максу нужна одежда
                if items['max-a'].have:
                    $ mgg.dress = 'b'
                    $ alice.daily.oiled = 1
                else:
                    Max_07 "{m}Прежде чем пытаться поприставать к сестрёнке таким образом, стоит обзавестись одеждой полегче.{/m}"
                    $ items['max-a'].unblock()
                    jump AfterWaiting

            if kol_cream < 3:  # крема не хватит даже просто нанести
                Max_07 "{m}Крем почти закончился. Нужно купить ещё.{/m}"
                $ items['solar'].unblock()
                jump AfterWaiting

        "Может быть, тебя намазать кремом для загара?" if all([alice.daily.oiled==0, kol_cream>=3, mgg.dress!='a']):
            Alice_03 "Если у тебя есть крем, то давай, раз тебе делать нечего."
            Max_01 "Ложись на живот тогда..."
            $ alice.daily.oiled = 1
        "Ладно, загорай...":
            jump AfterWaiting

    scene BG char Alice sun-alone 01f
    show Alice sun-alone 01-01
    $ renpy.show('Max sun-alone 01'+mgg.dress)
    menu .type_choice:
        Alice_07 "Эти шезлонги всем хороши, но на животе загорать не получается. Приходится коврик для йоги использовать..."
        "{i}нанести крем{/i}" if (kol_cream >= 3 and not learned_foot_massage()) or 3<=kol_cream<7:  # просто наносим крем. близко к оригиналу
            $ SetCamsGrow(house[6], 140)
            $ poss['massage'].open(1)
            $ _massaged = []
            $ _suf = 'a'
            $ spent_time += 20
            $ kol_cream -= 3
            scene BG char Alice sun-alone 05
            $ renpy.show('Alice sun-alone 05'+_suf+mgg.dress)
            show screen Cookies_Button
            Max_01 "{m}Так, хорошенько намажем эти стройные ножки...{/m}"
            hide screen Cookies_Button
            scene BG char Alice sun-alone 04
            $ renpy.show('Alice sun-alone 04'+_suf+mgg.dress)
            menu:
                Max_01 "{m}Теперь плечи и совсем немного шею...{/m}"
                "{i}наносить крем молча{/i}":
                    pass
                "А тебе нравится, что следы от лямок остаются?":
                    $ _talk_top = True
                    call massage_sunscreen.talk_topless from _call_massage_sunscreen_talk_topless
            $ __r1 = renpy.random.choice(['02','03'])
            $ renpy.scene()
            $ renpy.show('BG char Alice sun-alone '+__r1)
            $ renpy.show('Alice sun-alone '+__r1+_suf+mgg.dress)
            Max_03 "{m}И закончим, хорошенько намазав всю её спину...{/m}"
            $ Skill('massage', 0.005)
            if mgg.massage >= 0.01 and len(online_cources) == 1:
                Alice_04 "Спасибо, Макс! На сегодня достаточно. У тебя очень неплохо получается, а если поучишься, может стать ещё лучше!"
                Max_04 "Да не за что, обращайся!"
                scene BG char Alice sun-alone 01
                if alice.daily.oiled == 2:
                    show Alice sun-alone 01a
                else:
                    show Alice sun-alone 01
                Max_07 "{m}В чём-то Алиса права, поучиться этому, пожалуй, стоит.{/m}"
                $ poss['massage'].open(2)
                $ online_cources.append(
                    OnLineCources(_("Массаж"), "massage", "bm", [
                        OnLineCource(_("Массаж ступней"), _("Это уникальная методика массажа с целью оказания оздоравливающего воздействия на организм. Она эффективна и в тоже время несложна в исполнении."), 3, 100, 2),
                        OnLineCource(_("Массаж кистей рук"), _("Это уникальная методика массажа с целью оказания оздоравливающего воздействия на организм. Она эффективна и в тоже время несложна в исполнении."), 3, 200, 2),
                        ]),
                    )
            else:
                Alice_03 "Спасибо, Макс. Так намного лучше..."
                Max_04 "Обращайся, если что..."
            scene BG char Alice sun-alone 01
            if alice.daily.oiled == 2:
                show Alice sun-alone 01a
            else:
                show Alice sun-alone 01

            if kol_cream < 2:
                call left_cream from _call_left_cream_2
                # Max_10 "{m}Ну вот, крем закончился. Надо ещё купить.{/m}"
                # if kol_cream == 0:
                #     $ items['solar'].use()
                #     $ items['solar'].unblock()
            elif kol_cream < 7:
                call left_cream(1) from _call_left_cream_3
                # Max_08 "{m}Осталось мало крема, в следующий раз может не хватить, лучше купить заранее.{/m}"
                # $ items['solar'].unblock()
            $ AddRelMood('alice', 5, 50, 2)
        "{i}сделать массаж с кремом{/i}" if all([kol_cream >= 7, learned_foot_massage()]):  # попытка сделать массаж с кремом
            $ _massaged = []
            $ _talk_top = False
            $ SetCamsGrow(house[6], 160)
            jump massage_sunscreen
        "{i}{color=[gray]}сделать массаж с кремом{/color}{color=[red]}\nкрема недостаточно{/color}{/i}" if kol_cream < 7:
            jump .type_choice
        "{i}Блин, крем практически закончился... Давай в другой раз тогда...{/i}" if kol_cream < 3:
            Alice_00 "Ну что же ты, Макс... Эх, только настроилась..."
            $ alice.daily.oiled = 3
            jump AfterWaiting

    jump Waiting


label massage_sunscreen:
    scene BG char Alice sun-alone 01f
    if alice.daily.oiled == 2:
        show Alice sun-alone 01-01a
        $ _suf = 'b'
    else:
        show Alice sun-alone 01-01
        $ _suf = 'a'
    $ renpy.show('Max sun-alone 01'+mgg.dress)
    if learned_hand_massage():
        if len(_massaged) == (5 if alice.dcv.intrusion.stage in [5, 7] else 4): # 5:
            Alice_07 "Макс, ты делаешь успехи! Ещё немного попрактикуешься, и к тебе будет сложно записаться на приём!"
            Max_03 "Да пустяки, обращайся!"
            Alice_04 "Ладно, хватит на сегодня, Макс. И... спасибо!"
            Max_05 "Не за что! Всегда рад..."
            $ AddRelMood('alice', 15, 150, 3)
            if not _in_replay and all([alice.daily.oiled == 2, _massaged[0:2]==['foot', 'shin']]):
                $ poss['massage'].open(4)
            jump .end  # если Макс подарил Алисе кружевное боди, есму доступно 5 зон массажа

    elif len(_massaged) == 4:
        Alice_04 "Спасибо, Макс! На сегодня достаточно. У тебя очень неплохо получается, а если поучишься, может стать ещё лучше!"
        Max_04 "Да не за что, обращайся!"
        $ AddRelMood('alice', 10, 100, 3)
        if not _in_replay and all([alice.daily.oiled == 2, _massaged[0:2]==['foot', 'shin']]):
            $ poss['massage'].open(4)
        jump .end  # если курсы не пройдены и первыми массировались ступни, доступно 4 зоны

    elif len(_massaged) == 2 and _massaged[0] != 'foot':
        Alice_03 "Спасибо, Макс! На сегодня достаточно."
        Max_01 "Да не за что, обращайся!"
        $ AddRelMood('alice', 5, 50, 2)
        jump .end

    if all([len(_massaged)==2, _massaged==['foot', 'shin']]):
        if not _in_replay:
            $ poss['massage'].open(3)

    ### выбираем зону массажа
    if not _in_replay:
        $ kol_cream -= 1
    call screen choice_zone_sunscreen

    label .left_foot:
        scene BG char Alice sun-alone 06
        $ renpy.show('Alice sun-alone 06'+_suf+mgg.dress)
        Max_01 "{m}Начнём сегодня с левой пяточки... Вот так. И, пока я хорошенько её массирую, можно заодно поглазеть на аппетитную Алисину попку!{/m}"
        scene BG char Alice sun-alone 07
        $ renpy.show('Alice sun-alone 07'+_suf+mgg.dress)
        Max_03 "{m}А теперь правую... Вот так. Да уж, глаз не оторвать, попка - что надо!{/m}"
        jump .foot

    label .right_foot:
        scene BG char Alice sun-alone 07
        $ renpy.show('Alice sun-alone 07'+_suf+mgg.dress)
        Max_01 "{m}Начнём сегодня с правой пяточки... Вот так. И, пока я хорошенько её массирую, можно заодно поглазеть на аппетитную Алисину попку!{/m}"
        scene BG char Alice sun-alone 06
        $ renpy.show('Alice sun-alone 06'+_suf+mgg.dress)
        Max_03 "{m}А теперь левую... Вот так. Да уж, глаз не оторвать, попка - что надо!{/m}"
        jump .foot

    label .shin:
        scene BG char Alice sun-alone 05
        $ renpy.show('Alice sun-alone 05'+_suf+mgg.dress)
        show screen Cookies_Button
        Max_02 "{m}Помассируем эти стройные ножки, вот так...{/m}"
        if 'shin' in _massaged:
            # голени уже массировались
            jump .double
        else:
            $ _multipler = 10 - len(_massaged)
            if len(_massaged)>0 and _massaged[0]=='foot':
                $ _multipler *= 2 # множитель навыка удваивается, если ступни были первыми

            $ skill_outcome('massage', mgg.massage * _multipler, 95)
            if rand_result:
                # Алисе понравилось
                Alice_07 "Ух, как приятно... Ты молодец, Макс! Моим ножкам это понравилось... Не останавливайся, продолжай..."
                $ infl[alice].add_m(4)
            else:
                jump .fail
        $ _massaged.append('shin')
        hide screen Cookies_Button
        jump massage_sunscreen

    label .shoulders:
        scene BG char Alice sun-alone 04
        $ renpy.show('Alice sun-alone 04'+_suf+mgg.dress)
        if not _talk_top:
            menu:
                Max_04 "{m}Хорошенько разомнём плечи и немного шею...{/m}"
                "{i}массировать молча{/i}":
                    pass
                "А тебе нравится, что следы от лямок остаются?":
                    $ _talk_top = True
                    call massage_sunscreen.talk_topless from _call_massage_sunscreen_talk_topless_1
                    $ renpy.show('Alice sun-alone 04'+_suf+mgg.dress)
                    Max_01 "И ещё немного..."
        else:
            Max_04 "{m}Хорошенько разомнём плечи и немного шею...{/m}"

        if 'shoulders' in _massaged:
            # плечи уже массировались
            jump .double
        else:
            $ _multipler = 10 - len(_massaged)
            if len(_massaged)>0 and _massaged[0]=='foot':
                $ _multipler *= 2 # множитель навыка удваивается, если ступни были первыми

            $ _massaged.append('shoulders')
            $ skill_outcome('massage', mgg.massage * _multipler, 95)
            if rand_result:
                # Алисе понравилось
                $ infl[alice].add_m(4)
                menu:
                    Alice_07 "Это так классно расслабляет... У тебя очень хорошо получается, Макс!"
                    "{i}продолжить{/i}":
                        pass
                    "{i}выпустить рядом паука{/i}" if items['spider'].have and poss['spider'].used(4) and not _in_replay:
                        show FG sun-alone-04
                        jump .spider
            else:
                jump .fail
        jump massage_sunscreen

    label .spine:
        $ __r1 = renpy.random.choice(['02','03'])
        $ renpy.scene()
        $ renpy.show('BG char Alice sun-alone '+__r1)
        $ renpy.show('Alice sun-alone '+__r1+_suf+mgg.dress)
        if not _talk_top:
            menu:
                Max_05 "{m}Вот так, нужно хорошенько растереть крем... А теперь тщательно помнём спинку... Нежно, но сильно.{/m}"
                "{i}массировать молча{/i}":
                    pass
                "А тебе нравится, что следы от лямок остаются?":
                    $ _talk_top = True
                    call massage_sunscreen.talk_topless from _call_massage_sunscreen_talk_topless_2
                    $ renpy.show('Alice sun-alone '+__r1+_suf+mgg.dress)
                    Max_01 "Ещё немного крема..."
        else:
            Max_05 "{m}Вот так, нужно хорошенько растереть крем... А теперь тщательно помнём спинку... Нежно, но сильно.{/m}"

        if 'spine' in _massaged:
            # спина уже массировалась
            jump .double
        else:
            $ _multipler = 10 - len(_massaged)
            if len(_massaged)>0 and _massaged[0]=='foot':
                $ _multipler *= 2 # множитель навыка удваивается, если ступни были первыми

            $ _massaged.append('spine')
            $ skill_outcome('massage', mgg.massage * _multipler, 95)
            if rand_result:
                # Алисе понравилось
                $ infl[alice].add_m(4)
                menu:
                    Alice_07 "Как приятно... Макс, ты делаешь успехи! Мне это нравится..."
                    "{i}продолжить{/i}":
                        pass
                    "{i}выпустить рядом паука{/i}" if items['spider'].have and poss['spider'].used(4) and not _in_replay:
                        $ renpy.show("FG sun-alone-"+__r1)
                        jump .spider
            else:
                jump .fail
        jump massage_sunscreen

    label .ass:  # попка пока недоступна, поэтому не прописывал алгоритм
        "попка"
        jump massage_sunscreen

    label .hips:

        #ракурс массажа бёдер выходит рандомно, не выбирая какую ногу массировать
        if renpy.random.randint(1, 2)<2:
            # sun-alone-07 + sun-alone-08-max-(01a/01b)-alice-(01/01a)
            scene BG char Alice sun-alone 07
            $ renpy.show('Alice sun-alone 08'+_suf+mgg.dress)
        else:
            # sun-alone-01 + sun-alone-09-max-(01a/01b)-alice-(01/01a)
            scene BG char Alice sun-alone 01f
            $ renpy.show('Alice sun-alone 09'+_suf+mgg.dress)

        if 'hips' in _massaged:
            # бёдна уже массировались
            jump .double

        if not len(_massaged):
            #если Макс начал массировать бёдра самыми первыми
            Alice_06 "Макс, а ты куда это там полез так неожиданно?! Лучше сосредоточься на всём остальном, а туда не лезь..."

        elif all([len(_massaged)==1, _massaged[0] in ['foot', 'shin']]) or _massaged==['shin', 'foot']:
            #если Макс массировал только или ступни или голени, после чего начал бёдра
            Alice_13 "Макс, ты слишком высоко забрался! Лучше сосредоточься на всём остальном..."

        elif (all([len(_massaged)==2, _massaged==['foot', 'shin']]) or
                any([_massaged==['shoulders', 'spine', 'foot', 'shin'], _massaged==['spine', 'shoulders', 'foot', 'shin']])):
            #если Макс массировал ступни и голени, после чего начал бёдра
            Alice_04 "Хоть это и приятно, но ощущение, будто ты не знаешь, как правильно массировать там... Лучше сосредоточься на том, что ты умеешь..."
            $ infl[alice].add_m(4)

        elif any([_massaged==['shoulders'], _massaged==['spine'], set(_massaged)==set(['shoulders', 'spine']), set(_massaged)==set(['shoulders', 'spine', 'shin'])]):
            #если Макс массировал только или спину или плечи (или же и спину и плечи), после чего начал бёдра
            Alice_13 "Макс, а ты куда это там полез так неожиданно?! Если уж решил перейти на ноги, то массируй с самого низа..."
        else:
            #если Макс переходил с ног на спину, после чего начал бёдра
            Alice_06 "Макс, ты уже определись, что ты массируешь! Ноги или спину... Похоже, на твоих онлайн-курсах не учили тому, что прыгать туда-сюда не здорово..."

        $ _massaged.append('hips')
        jump massage_sunscreen

    label .foot:
        if 'foot' in _massaged:
            # ступни уже массировались
            jump .double
        else:
            $ _multipler = 10 - len(_massaged) if len(_massaged) else 20  # множитель навыка. Если ступни первые, шанс удваивается
            $ skill_outcome('massage', mgg.massage * _multipler, 95)
            if rand_result:
                # Алисе понравилось
                $ infl[alice].add_m(4)
                Alice_07 "Ух, как же моим пяточкам приятно... Не останавливайся, продолжай..."
            else:
                jump .fail
        $ _massaged.append('foot')
        jump massage_sunscreen

    label .double:
        hide screen Cookies_Button
        Alice_13 "Взялся делать массаж, а сам не знаешь что делать! Хватит, иди отсюда, дай позагорать спокойно."
        Max_11 "Эх... Ладно..."
        jump .end

    label .fail:
        hide screen Cookies_Button
        if len(_massaged) > 0:  # есть успешно помассированные участки
            Alice_06 "Хватит, Макс... Что-то у тебя не так пошло... А ведь так хорошо начал..."
        else:  # первый же массаж
            Alice_13 "Макс, хватит... Что-то не похоже, что ты знаешь, что делаешь... Давай на этом закончим..."
        Max_10 "Хорошо, извини..."
        jump .end

    label .talk_topless:
        menu:
            Alice_06 "Нет, конечно. Но тебя я так радовать не собираюсь!"
            "Что, стесняешься?" ('soc', mgg.social * (1 + len(_massaged) if _massaged[0:2]==['foot', 'shin'] else 1), 90):
                if rand_result or _in_replay:
                    Alice_07 "[succes!t]Нет, но... Ладно, всё равно тебе ничего не видно..."
                    Max_02 "Так держать, сестрёнка!"
                    $ alice.daily.oiled = 2
                    $ alice.dress = 'b'
                    $ _suf = 'b'
                    $ SetCamsGrow(house[6], 200)
                else:
                    Alice_04 "[failed!t]Вот только на \"слабо\" меня брать не надо!"
                    Max_01 "Ладно, как скажешь..."
            "Ну, как хочешь...":
                pass
        return

    label .spider:
        if _in_replay:
            $ _suf = 'b' if alice.daily.oiled == 2 else 'a'
            $ __r1 = renpy.random.choice(['02','03'])
            $ renpy.scene()
            $ renpy.show('BG char Alice sun-alone '+__r1)
            $ renpy.show('Alice sun-alone '+__r1+_suf+mgg.dress)
            $ renpy.show("FG sun-alone-"+__r1)
        else:
            $ poss['spider'].open(5)
            $ items['spider'].use()
            $ SpiderKill = 0  # паук остался жив
            $ SpiderResp = 1  # поэтому поймать можно уже на следующий день
            if 'massage_sunscreen.spider' not in persistent.memories:
                $ persistent.memories['massage_sunscreen.spider'] = 0
        Max_07 "Э-э-э... Алиса, ты только не пугайся, просто лежи, как лежала..."
        Alice_13 "А чего мне пугаться, Макс? Сейчас что, будешь больно массировать?"
        Max_00 "Нет, просто у нас тут одна проблемка подкралась..."
        scene BG char Alice sun-alone 03
        $ renpy.show('Alice sun-alone 03'+_suf+mgg.dress)
        show FG sun-alone-03
        Alice_12 "Что?! Подкралась?! Ты же говоришь не о том, о чём я подумала?"
        Max_08 "Ну... Ты только не дёргайся!"
        # spider-sun-01 + spider-sun-01-max-(01/01a)-alice-(01/01a) + spider-sun-01-spider
        scene BG char Alice spider-sun-01
        $ renpy.show('Alice spider-sun 01'+_suf+mgg.dress)
        show FG spider-sun-01
        Alice_15 "А-а-а! Макс! Вот чёрт! Какой он здоровенный!"   # spider-sun-01
        Max_02 "И не говори!"
        Alice_14 "Макс, чего сидишь?! Убери его отсюда! А ещё лучше убей!"
        Max_04 "Да мне как-то не хочется."
        # spider-sun-02 + spider-sun-02-max-(01/01a)-alice-(01/01a)
        scene BG char Alice spider-sun-02
        $ renpy.show('Alice spider-sun 02-01'+_suf+mgg.dress)
        Alice_06 "В смысле, не хочется?! Охренеть, он страшный!"   # spider-sun-02
        Max_05 "Так хорошо же сидим. Да и он в нашу сторону не ползёт. По-моему, он в сторону травы сменил курс..."
        if alice.daily.oiled != 2:
            Alice_16 "Да плевать мне, куда он ползёт! Я хочу, чтобы его не было!"
            # верх купальника не снят
            Max_01 "Ладно, тогда слезай, я с ним разберусь."
            Alice_06 "Не-е-ет, он тогда сразу ко мне поползёт! Что я их, не знаю что ли..."
            Max_03 "Ты определись уже, Алиса, чего хочешь. Я бы просто немного подождал, вон он, уползает..."
            Alice_12 "Точно?!"
            Max_04 "Ага. В траву убежал."
            # hugging-sun-01 + hugging-sun-max-(02a/02b)-alice-02
            scene BG char Alice hugging sun-01
            $ renpy.show('Alice hugging sun 02a'+mgg.dress)
            Alice_07 "Фух... Ладно. Только ты посматривай, временами, чтобы в мою сторону никто не полз."   #спрайт с родственными обнимашками
            Max_02 "Хорошо. Но, если что, зови. Ещё посидим."
            Alice_05 "Тебе хватит. Не обольщайся..."
            Max_01 "Ага."
            $ renpy.end_replay()
            $ infl[alice].add_m(4)
            jump .end
        else:
            # верх купальника снят
            menu:
                Alice_16 "Да плевать мне, куда он ползёт! Я хочу, чтобы его не было!"
                "Давай лучше ещё так посидим, подождём. Вон он, уползает...":
                    Alice_12 "Макс, а что это в меня такое упёрлось там внизу?!"
                    Max_02 "Ну... это я, так сказать."
                    Alice_14 "Ой, блин, это член твой что ли?!"
                    Max_01 "Ага. Он самый."
                    jump .sit_and_wait

                "Спрячься за меня, хотя бы..." if all([alice.dcv.intrusion.stage in [5, 7], alice.flags.privpunish, mgg.dress=='c']):
                    #если Макс опередил Эрика с кружевным бельём, было положительное приватное наказание Алисы и Макс только в шортах
                    jump .hide_behind

                "{i}потискать Алису за грудь{/i}" if alice.dcv.intrusion.stage in [5, 7]:
                    jump .squeeze_chest

    label .sit_and_wait:
        if mgg.dress == 'b':
            ###если Макс в майке и шортах###
            if alice.flags.touched:
                #если вариант "Спрячься за меня, хотя бы..." пройден
                # spider-sun-02 + spider-sun-02-max-01-alice-01a
                scene BG char Alice spider-sun-02
                show Alice spider-sun 02-01bb
                Alice_13 "Ну, Макс... Может хватит уже так на меня реагировать?! Я же твоя сестра всё-таки!"
                Max_02 "А ты ещё сильнее прижмись ко мне своими сиськами... Эффект будет ещё ощутимее!"
                Alice_06 "Паука бы лучше отогнал!"
                Max_03 "Незачем, он и так уползает..."
                Alice_12 "Точно?!"
                Max_04 "Ага. В траву убежал."
                # hugging-sun-01 + hugging-sun-max-02a-alice-02a
                scene BG char Alice hugging sun-01
                show Alice hugging sun 02bb
                Alice_07 "Фух... Ладно. Только ты посматривай, временами, чтобы в мою сторону никто не полз."
                Max_02 "Хорошо. Но, если что, зови. Ещё посидим."
                Alice_05 "Тебе хватит. Не обольщайся..."
                Max_01 "Ага."
            else:
                scene BG char Alice hugging sun-01
                show Alice hugging sun 01bb
                Alice_15 "Ты совсем что ли извращенец? На родную сестру у него стоит!"   #спрайт с выкручиванием ушей
                Max_10 "Ай, Алиса, больно! Сама же своими голыми сиськами в моё лицо упёрлась! А они красивые... Чего ты ещё ожидала?!"
                Alice_16 "Всё, не хочу об этом говорить... Давай, шуруй отсюда. Бегом! А то я живо тебе по заднице напинаю!"
                Max_09 "Да ухожу я, уши только мои в покое оставь!"
            jump .end
        else:
            ###если Макс только в шортах###
            if alice.flags.touched:
                # spider-sun-02 + spider-sun-02-max-01a-alice-01a   #если вариант "Спрячься за меня, хотя бы..." пройден
                scene BG char Alice spider-sun-02
                show Alice spider-sun 02-01bc
                Alice_13 "Ну, Макс... Может хватит уже так на меня реагировать?! Я же твоя сестра всё-таки!"
                Max_02 "А ты ещё сильнее прижмись ко мне своими сиськами... Эффект будет ещё ощутимее!"
                Alice_06 "Куда уж ещё ощутимее! Я и так почти что на твоём члене сижу..."
                Max_03 "Зато, паук в совершенно противоположную сторону от нас уползает!"
                Alice_12 "Точно?!"
                Max_04 "Ага. В траву убежал."
                # hugging-sun-01 + hugging-sun-max-02c-alice-02a
                scene BG char Alice hugging sun-01
                show Alice hugging sun 02bc
                Alice_05 "Ой... Ты извини, что я тебя тут, посовращала немного... Я же не специально."
                Max_03 "Не слишком-то ты раскаиваешься, а?"
                Alice_02 "Будем считать, что твой стояк меня сегодня спас! Паук сразу убежал... И я теперь чувствую себя, какой-то защищённой, что ли... Кажется, уже и я какой-то извращенкой становлюсь!"
                Max_04 "Это у нас семейное, по-видимому."
                Alice_07 "Только ты давай прибери свою штуку, а то мы со стороны очень странно сейчас выглядим."
                Max_02 "Да не так-то это просто сделать..."
                Alice_05 "А ты постарайся."
                Max_01 "Ага."
            else:
                show Alice spider-sun 02-02bc
                Alice_12 "Какого чёрта, Макс?! Совсем что ли извращенец? Я же твоя сестра! Блин... Прикройся хоть..."   #спрайт с прикрывающейся от Макса Алисой
                Max_01 "Да не так-то это просто, прикрыть его."
                Alice_06 "Не ожидала я от тебя такого, Макс. И что у тебя в голове творится?!"
                Max_07 "А чего ты ожидала?! Сама же на меня запрыгнула и сиськами своими голыми мне в лицо упёрлась... Кстати, не могу не отметить, они у тебя красивые и упругие!"
                Alice_13 "Нет, ну ты точно больной... Ладно, представим, что ничего не было. Убирай эту свою штуку и не появляйся в таком виде рядом со мной!"
                Max_02 "Хорошо. Не скучай."
                $ renpy.end_replay()
                $ persistent.memories['massage_sunscreen.spider'] = 1
                $ infl[alice].add_m(10)
            jump .end

    label .hide_behind:
        $ added_mem_var('hide_behind')
        Alice_06 "Нет, я боюсь..."
        Max_09 "А вдруг он на нас побежит, прямо к твоей попке!"
        # spider-sun-03 + spider-sun-03-max-01b-alice-01a
        scene BG char Alice spider-sun-03
        show Alice spider-sun 03bc
        Alice_13 "Ой, нет! Не надо к моей попке! Что ему вообще надо тут?! Почему ему в траве не сидится или где он там живёт..."
        Max_07 "Ну... Не то, чтобы меня что-то не устраивало сейчас, но ты держишься за меня!"
        # spider-sun-04 + spider-sun-04-max-01b-alice-01a
        scene BG char Alice spider-sun-04
        show Alice spider-sun 04-01bc
        Alice_12 "Конечно держусь! Мне же страшно, Макс! Ты ведь знаешь, как я их боюсь..."
        Max_03 "Нет, я в смысле, ты держишься за мой член! Это, конечно, весьма приятно... Но ты же на меня, как всегда, разорёшься потом!"
        # spider-sun-04 + spider-sun-04-max-02b-alice-02a
        show Alice spider-sun 04-02bc
        Alice_15 "Ой! Я это не специально! Видишь, насколько я этих пауков не переношу? Даже не поняла, за что схватилась..."
        Max_02 "Да ладно, схватилась и схватилась. Уж это точно не страшно!"
        Alice_12 "Он уползает, кстати..."
        Max_05 "Точно! Наверно, испугался моей торчащей мощи!"
        Alice_07 "У тебя что, стоит до сих пор?!"
        Max_04 "Ну... Ты так классно ко мне прижимаешься... Мне приятно!"
        # hugging-sun-01 + hugging-sun-max-02c-alice-02a
        scene BG char Alice hugging sun-01
        show Alice hugging sun 02bc
        Alice_05 "Ой... Ты извини, что я тебя тут, посовращала немного... Я же не специально."
        Max_03 "Не слишком-то ты раскаиваешься, а?"
        Alice_02 "Будем считать, что твой стояк меня сегодня спас! Паук сразу убежал... И я теперь чувствую себя, какой-то защищённой, что ли... Кажется, уже и я какой-то извращенкой становлюсь!"
        Max_04 "Это у нас семейное, по-видимому."
        Alice_07 "Только ты давай прибери свою штуку, а то мы со стороны очень странно сейчас выглядим."
        Max_02 "Да не так-то это просто сделать..."
        Alice_05 "А ты постарайся."
        Max_01 "Ага."
        if not _in_replay:
            $ poss['spider'].open(6)
        $ alice.flags.touched = True
        jump .end

    label .squeeze_chest:
        $ added_mem_var('squeeze_chest')
        # spider-sun-02 + spider-sun-02-max-(03/03a)-alice-03a
        scene BG char Alice spider-sun-02
        $ renpy.show('Alice spider-sun 02-03b'+mgg.dress)
        Alice_14 "Ты офигел что ли, Макс! Ну-ка руки быстро убери, пока не получил..."
        Max_07 "Шуму-то сколько... У тебя сиськи голые, вот я их и прикрыл! А то мало ли кто увидит..."
        $ ctd = Countdown(3, 'massage_sunscreen.hands_off')
        $ renpy.block_rollback()
        Alice_15 "Кто??? Пауки что ли?! Если через пять секунд не уберёшь руки, тебе будет плохо...{p=5}{nw}"
        show screen countdown       # меню с таймером
        extend "" nointeract

        $ rl = create_random_list(3)
        menu (rand='all'):
            "{i}убрать руки{/i}":
                $ rez = 1
            "{i}тискать дальше...{/i}":
                $ rez = 0

        $ renpy.block_rollback()
        if rez:
            # (успел)
            hide screen countdown
            # spider-sun-02 + spider-sun-02-max-(01/01a)-alice-01a
            scene BG char Alice spider-sun-02
            $ renpy.show('Alice spider-sun 02-01b'+mgg.dress)
            Max_02 "Всё, убрал. Правда, если ты продолжишь так крепко прижиматься ими к моему лицу, то есть риск..."
            Alice_06 "Макс... Я что, практически на твоём члене сейчас сижу?!"
            Max_03 "А сама как думаешь?"
            jump .sit_and_wait
        else:
            hide screen countdown
            jump .hands_off

    label .hands_off:
        $ renpy.block_rollback()
        # (не успел)
        if mgg.dress == 'b':
            #если Макс в майке и шортах
            # hugging-sun-01 + hugging-sun-max-01a-alice-01a
            scene BG char Alice hugging sun-01
            show Alice hugging sun 01bb
            Max_12 "А-а-ай! Мне же больно, Алиса! Перестань!"
            Alice_16 "А я ведь тебя предупреждала! Наверно, раз до тебя не дошло, нужно крутануть ещё сильнее..."
            Max_14 "Ой! Я понял... Больше не буду! Отпусти уже..."
            Alice_17 "Всё, давай, шуруй отсюда. Бегом! А то я живо тебе по заднице напинаю!"
        else:
            #если Макс только в шортах
            # hugging-sun-01 + hugging-sun-max-01c-alice-01a
            scene BG char Alice hugging sun-01
            show Alice hugging sun 01bc
            Max_12 "А-а-ай! Мне же больно, Алиса! Перестань!"
            Alice_00 "Ах, у тебя ещё и стоит на это всё! Совсем что ли извращенец? Я же твоя сестра!"
            Max_07 "А чего ты ожидала?! Сама же на меня запрыгнула и сиськами своими голыми мне в лицо упёрлась... Кстати, не могу не отметить, они у тебя красивые и упругие!"
            Alice_13 "Нет, ну ты точно больной... Ладно, представим, что ничего не было. Убирай эту свою штуку и не появляйся в таком виде рядом со мной!"
        Max_09 "Да ухожу я, уши только мои в покое оставь!"
        jump .end

    label .end:
        $ renpy.end_replay()
        scene BG char Alice sun-alone 01
        if alice.daily.oiled == 2:
            show Alice sun-alone 01a
            if all([len(_massaged)>3, _massaged[0:2]==['foot', 'shin']]):
                $ poss['massage'].open(4)
        else:
            show Alice sun-alone 01
        $ spent_time += 10 + clip(int(round(5*len(_massaged), -1)), 0, 30)
        if kol_cream < 3 and mgg.massage < 2.0:
            call left_cream from _call_left_cream_4
            # Max_10 "{m}Ну вот, крем закончился. Надо ещё купить.{/m}"
            # if kol_cream == 0:
            #     $ items['solar'].use()
            #     $ items['solar'].unblock()
        elif kol_cream < 7:
            call left_cream(1) from _call_left_cream_5
            # Max_08 "{m}Осталось мало крема, в следующий раз может не хватить, лучше купить заранее.{/m}"
            # $ items['solar'].unblock()

        jump Waiting


label alice_sorry_gifts:
    if alice.sorry.days[0] == day:
        Max_09 "{m}Думаю, не стоит дарить вкусняшку сегодня. Это может вызвать ненужные подозрения... Лучше это сделать завтра.{/m}"
        return

    if not len(alice.sorry.give):
        Alice_02 "Да ладно! Это мне нравится... И что там у тебя?" nointeract
    elif len(alice.sorry.give) == 1:
        Alice_02 "Ого! И правда хочешь рискнуть... И что там у тебя на этот раз?" nointeract
    else:
        Alice_02 "Наконец-то! Ну давай, показывай, что у тебя на этот раз?!" nointeract
    menu:
        "Конфеты \"Raffaello\" (16 штук)" if items['raffaello-m'].have:
            $ __give = 'raffaello-m'
            jump .bad
        "Конфеты \"Raffaello\" (24 штуки)" if items['raffaello-b'].have:
            $ __give = 'raffaello-b'
            jump .bad
        "Конфеты \"Ferrero Rocher\" (16 штук)" if items['ferrero-m'].have:
            $ __give = 'ferrero-m'
            jump .good
        "Конфеты \"Ferrero Rocher\" (24 штуки)" if items['ferrero-b'].have:
            $ __give = 'ferrero-b'
            jump .good
        "Шоколад \"Ritter Sport\" mini (9 штук)" if items['ritter-m'].have:
            $ __give = 'ritter-m'
            jump .middle
        "Шоколад \"Ritter Sport\" (4 штуки)" if items['ritter-b'].have:
            $ __give = 'ritter-b'
            jump .middle

    label .kick_ears:
        $ poss['risk'].open(6)
        if current_room == house[1]:
            scene BG char Alice newdress
            if '09:00' <= tm < '20:00':
                $ renpy.show("Alice hugging aliceroom 01"+alice.dress+mgg.dress)
            else:
                $ renpy.show("Alice hugging aliceroom 01"+alice.dress+mgg.dress+'e')
        elif current_room == house[5]:
            scene BG char Alice hugging terrace-01
            $ renpy.show("Alice hugging terrace 01"+alice.dress+mgg.dress)
        elif current_room == house[6]:
            scene BG char Alice hugging sun-01
            $ renpy.show("Alice hugging sun 01"+alice.dress+mgg.dress)
        return

    label .kindred_hugs:
        $ poss['risk'].open(7)
        if current_room == house[1]:
            scene BG char Alice newdress
            if '09:00' <= tm < '20:00':
                $ renpy.show("Alice hugging aliceroom 02"+alice.dress+mgg.dress)
            else:
                $ renpy.show("Alice hugging aliceroom 02"+alice.dress+mgg.dress+'e')
        elif current_room == house[5]:
            scene BG char Alice hugging terrace-01
            $ renpy.show("Alice hugging terrace 02"+alice.dress+mgg.dress)
        elif current_room == house[6]:
            scene BG char Alice hugging sun-01
            $ renpy.show("Alice hugging sun 02"+alice.dress+mgg.dress)
        return

    label .middle_again:
        Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
        Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
        Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."   #спрайт с ушами
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_3
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        menu:
            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
            "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                if rand_result:
                    Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                    Max_14 "Ой! Я понял... Больше не буду!"
                    Alice_02 "Вот и молодец! Гуляй..."
                    $ alice.flags.hugs_type = 2
                else:
                    Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                    Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                    Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                    Max_14 "Ой! Я понял... Больше не буду!"
                    Alice_02 "Вот и молодец! Гуляй..."
                    $ alice.flags.hugs_type = 1
                    $ punreason[1] = 1
        return

    label .bad_again:
        Alice_17 "Макс, ты что, тупой?! Я тебе уже говорила, что не люблю эти конфеты! Ты меня, что, совсем не слушаешь, или у тебя помяти нет?!"
        Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
        Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."   #спрайт с ушами
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_4
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
        Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
        Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."
        $ punreason[1] = 1
        $ alice.flags.hugs_type = 1
        return

    label .apology_accepted:
        Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_5
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."
        $ alice.flags.hugs_type = 2
        return

    label .you_deserve:
        Alice_04 "[succes!t]Ладно, Макс, пожалуй ты заслужил это своими подарками..."   #спрайт с обнимашками
        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_1
        Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
        Alice_07 "Я вижу, что ты не просто хочешь избежать наказания, а ещё и мне приятно сделать стремишься. Вот я и не вредничаю..."
        Max_05 "Да, надо бы почаще так делать."
        Alice_02 "Подглядывать за мной или дарить мне сладости?!"
        Max_02 "Второе, конечно!"
        Alice_05 "Ну да, конечно... Иди давай."
        $ alice.flags.hugs_type = 4
        return

    label .what_bummer:
        Alice_05 "[failed!t]Ах, а так хотелось! Какой облом..."
        Max_09 "Обнять меня или придушить?"
        Alice_07 "Зачем останавливаться на чём-то одном, Макс? Хи-хи..."
        Max_01 "Я тогда лучше пойду... погуляю."
        Alice_02 "Ну как хочешь..."
        $ alice.flags.hugs_type = 3
        return

    label .im_in_pain:
        Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_6
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        $ alice.flags.hugs_type = 2
        return

    label .what_disgusting:
        Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
        Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
        Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."   #спрайт с ушами
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_7
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        $ alice.flags.hugs_type = 2
        return

    label .bad: ## ненавистное
        $ items[__give].use()
        $ poss['risk'].open(2)
        if len(alice.sorry.give) == 0:  # ненавистное в первый раз
            Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
            Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
            Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."   #спрайт с ушами
            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_8
            Max_12 "А-а-ай! Алиса! Больно ведь!"
            menu:
                Alice_16 "Будешь ещё, извращенец лохматый, за мной подглядывать?"
                "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                    if rand_result:
                        Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                        Max_14 "Ой! Понял-понял, не буду! Больше не буду..."
                        Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                        Max_08 "И какая у тебя любимая?"
                        Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                        Max_11 "Ладно! Я учту, только отпусти..."
                        Alice_02 "Вот и правильно! Гуляй..."
                    else:
                        Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                        Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                        Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                        Max_08 "И какая у тебя любимая?"
                        Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                        Max_11 "Ладно! Я учту, только отпусти..."
                        Alice_02 "Вот и правильно! Гуляй..."
                        $ punreason[1] = 1

        elif len(alice.sorry.give) == 1:  ## второе вручение
            if alice.sorry.give[0] == 1:  ## ненавистное, ненавистное
                Alice_17 "Макс, ты что, тупой?! Я тебе уже говорила, что не люблю эти конфеты! Ты меня, что, совсем не слушаешь, или у тебя помяти нет?!"
                Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
                Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_9
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                Max_08 "И какая у тебя любимая?"
                Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."
                $ punreason[1] = 1

            elif alice.sorry.give[0] == 2: ## преемлемое, ненавистное
                call alice_sorry_gifts.what_disgusting from _call_alice_sorry_gifts_what_disgusting
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                Max_08 "И какая у тебя любимая?"
                Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."
                $ punreason[1] = 1

            elif alice.sorry.give[0] == 3: ## любимое, ненавистное
                Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
                Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
                Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_10
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                            Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1

        elif len(alice.sorry.give) == 2:  ### третье вручение
            if alice.sorry.give == [1, 1]:  ## ненависное, ненавистное, ненавистное
                Alice_17 "Макс, ты что, тупой, я тебе, уже дважды говорила, что не люблю эти конфеты?! Ты меня, что, совсем не слушаешь, или у тебя мозгов нет?!"
                Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
                Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_11
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_16 "Да тебе просто наплевать на всё то, что я тебе говорю! Так что - сам виноват..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_17 "Понял он... Катись отсюда!"
                $ alice.flags.hugs_type = 1
                $ punreason[1] = 1

            elif alice.sorry.give == [1, 2]:  ### ненавистное, преемлемое, ненавистное
                call alice_sorry_gifts.bad_again from _call_alice_sorry_gifts_bad_again

            elif alice.sorry.give == [1, 3]:  ### ненавистное, любимое, ненавистное
                Alice_17 "Макс, ты что, тупой?! Я тебе уже говорила, что не люблю эти конфеты! Ты меня, что, совсем не слушаешь, или у тебя помяти нет?!"
                Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
                Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_12
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            elif alice.sorry.give == [2, 1]:  ### преемлемое, ненавистное, ненавистное
                call alice_sorry_gifts.bad_again from _call_alice_sorry_gifts_bad_again_1

            elif alice.sorry.give == [2, 2]:  ### преемлемое, преемлемое, ненавистное
                Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
                Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
                Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_13
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            elif alice.sorry.give == [2, 3]:  ### преемлемое, любимое, ненавистное
                call alice_sorry_gifts.what_disgusting from _call_alice_sorry_gifts_what_disgusting_1
                Alice_05 "Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_02 "Вот и молодец! Гуляй..."

            elif alice.sorry.give == [3, 1]:  ### любимое, ненавистное, ненавистное
                call alice_sorry_gifts.bad_again from _call_alice_sorry_gifts_bad_again_2

            elif alice.sorry.give == [3, 2]:  ### любимое, преемлемое, ненавистное
                Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
                Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
                Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_14
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            else:  ### любимое, любимое, ненавистное
                call alice_sorry_gifts.what_disgusting from _call_alice_sorry_gifts_what_disgusting_2
                Alice_05 "Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_02 "Вот и молодец! Гуляй..."

        $ alice.sorry.give.append(1)
        jump .end

    label .middle: ## преемлемое
        $ items[__give].use()
        $ poss['risk'].open(3)
        if len(alice.sorry.give) == 0:  # преемлемой в первый раз
            Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
            Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
            Alice_05 "Конечно, Макс, считай твои извинения приняты... А ну-ка иди сюда..."   #спрайт с ушами
            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_15
            Max_12 "А-а-ай! Алиса! Больно ведь!"
            Alice_16 "Будешь ещё, извращенец лохматый, за мной подглядывать?"
            Max_10 "Да я же случайно оказался около душа..."
            Alice_05 "Ответ неправильный! Наверно, нужно сильнее потянуть..."
            Max_14 "Ой! Понял-понял, не буду! Больше не буду..."
            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
            Max_08 "И какая у тебя любимая?"
            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
            Max_11 "Ладно! Я учту, только отпусти..."
            Alice_02 "Вот и правильно! Гуляй..."

        elif len(alice.sorry.give) == 1:  ## второе вручение
            if alice.sorry.give[0] == 1:  ## ненавистное, преемлемое
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_16
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1

            elif alice.sorry.give[0] == 2:  ## преемлемое, преемлемое
                Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_17
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1

            else:  ## любимое, преемлемое
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_18
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."

        elif len(alice.sorry.give) == 2:  ###  третье вручение
            if alice.sorry.give == [1, 1]:  ### ненависное, ненавистное, преемлемое
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_12 "Я тебе сейчас дам, ничего не расскажу... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_19
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_05 "Не считается, если она мне неинтересна! Ты так и не подарил самую мою любимую сладость! Так что - не повезло тебе..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_02 "Вот и молодец! Гуляй..."
                $ alice.flags.hugs_type = 1
                $ punreason[1] = 1

            elif alice.sorry.give == [1, 2]:  ### ненавистное, преемлемое, преемлемое
                call alice_sorry_gifts.middle_again from _call_alice_sorry_gifts_middle_again

            elif alice.sorry.give == [1, 3]:  ### ненавистное, любимое, преемлемое
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted

            elif alice.sorry.give == [2, 1]:  ### преемлемое, ненавистное, преемлемое
                call alice_sorry_gifts.middle_again from _call_alice_sorry_gifts_middle_again_1

            elif alice.sorry.give == [2, 2]:  ### преемлемое третий раз
                Alice_13 "Вот значит как! Снова купил эти шоколадки... А ты рисковый! Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_1

            elif alice.sorry.give == [2, 3]:  ### преемлемое, любимое, преемлемое
                Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                menu:
                    Alice_04 "Видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                    "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я сейчас более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        else:
                            Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
                            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_20
                            Max_12 "А-а-ай! Мне же больно, Алиса!"
                            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                            Max_10 "Да я же случайно оказался около душа..."
                            Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2

            elif alice.sorry.give == [3, 1]:  ### любимое, ненавистное, преемлемое
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_21
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1
                            $ alice.flags.hugs_type = 1

            elif alice.sorry.give == [3, 2]:  ### любимое, преемлемое, преемлемое
                Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_2

            else:  ### любимое, любимое, преемлемое
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                menu:
                    Alice_04 "Видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                    "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я сейчас более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        else:
                            Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
                            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_22
                            Max_12 "А-а-ай! Мне же больно, Алиса!"
                            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                            Max_10 "Да я же случайно оказался около душа..."
                            Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2

        $ alice.sorry.give.append(2)
        jump .end

    label .good: ## любимое
        $ items[__give].use()
        $ poss['risk'].open(4)
        $ items['ferrero-b'].unblock()
        $ alice.sorry.valid.add('ferrero-b')
        if len(alice.sorry.give) == 0:  # любимое, самый первый раз
            Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
            Max_03 "Никто! Просто угадал..."
            Alice_05 "Хм... Похоже, что ты, Макс, большой везунчик! Поглазел на меня голую в душе, да ещё и с конфетами угадал... Не слишком ли?"
            Max_04 "Просто благоприятное стечение обстоятельств! И я за тобой не подглядывал, просто случайность..."
            menu:
                Alice_04 "В таком случае, видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                "Именно на это я и надеюсь..." ('soc', mgg.social * 3, 90):
                    if rand_result:
                        Alice_03 "[succes!t]Ладно, Макс, считай твои извинения приняты... Мама ничего не узнает, так что можешь дышать спокойно."
                        Max_07 "И даже без подвоха?!"
                        Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                        Max_01 "О, я понял, сестрёнка! Не буду мешать..."
                    else:
                        Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... А ну-ка иди сюда..."   #спрайт с ушами
                        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_23
                        Max_12 "А-а-ай! Алиса! Больно ведь!"
                        Alice_16 "Будешь ещё, извращенец лохматый, за мной подглядывать?"
                        Max_10 "Да я же случайно оказался около душа..."
                        Alice_05 "Ответ неправильный! Наверно, нужно сильнее потянуть..."
                        Max_14 "Ой! Понял-понял, не буду! Больше не буду..."
                        Alice_02 "Вот и правильно! Гуляй..."
            $ AddRelMood('alice', 0, 50)

        elif len(alice.sorry.give) == 1:  ## дарим во второй раз
            if alice.sorry.give[0] == 1:  ## ненавистное, любимое
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_05 "Хм... Похоже, что ты, Макс, большой везунчик! Поглазел на меня голую в душе, да ещё и с конфетами угадал... Не слишком ли?"
                Max_04 "Просто благоприятное стечение обстоятельств! И я за тобой не подглядывал, просто случайность..."
                Alice_04 "В таком случае, видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                Max_01 "Хочется надеяться, что так и будет..."
                Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_24
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Разве только это не будет большая коробка моих любимых конфет..."
                Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 50)

            elif alice.sorry.give[0] == 2:  ## преемлемое, любимое
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_05 "Хм... Похоже, что ты, Макс, большой везунчик! Поглазел на меня голую в душе, да ещё и с конфетами угадал... Не слишком ли?"
                Max_04 "Просто благоприятное стечение обстоятельств! И я за тобой не подглядывал, просто случайность..."
                menu:
                    Alice_04 "В таком случае, видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                    "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                        else:
                            Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."   #спрайт с ушами
                            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_25
                            Max_12 "А-а-ай! Мне же больно, Алиса!"
                            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                            Max_10 "Да я же случайно оказался около душа..."
                            Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 50)

            else:  ## любимое, любимое
                Alice_07 "Ага! Снова купил мои любимые конфеты! Большое тебе спасибо, Макс! Я удивлена, они ведь дорогие..."
                Max_03 "Почему бы не порадовать старшую сестрёнку её любимыми конфетами, если уж возможность подворачивается."
                if __give[-1:] == 'm':  #если сладость маленькая
                    menu:
                        Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                        "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                            if rand_result:
                                Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                                Max_07 "Что, вот так вот просто?!"
                                Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Но, Макс, просто на будущее, знай, в следующий раз ты так легко не отделаешься! Разве только это не будет большая коробка моих любимых конфет..."
                                Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            else:
                                call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain
                                Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Разве только это не будет большая коробка моих любимых конфет..."
                                Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                                Alice_02 "Вот и молодец! Гуляй..."
                    $ AddRelMood('alice', 0, 100)
                else:    #если сладость большая
                    Alice_05 "В этот раз конфет даже больше, так что я не припоминаю, чтобы утром за мной кто-то подглядывал! Всё было в порядке..."
                    Max_01 "Ну да, меня и рядом тогда не было!"
                    menu:
                        Alice_03 "Я даже подумываю, а не обнять ли тебя, Макс? Ну так... по семейному..."
                        "Только если без последующего насилия..." ('soc', mgg.social * 3, 90):
                            if rand_result:
                                call alice_sorry_gifts.you_deserve from _call_alice_sorry_gifts_you_deserve
                            else:
                                call alice_sorry_gifts.what_bummer from _call_alice_sorry_gifts_what_bummer
                    $ AddRelMood('alice', 5, 150, 3)

        elif len(alice.sorry.give) == 2:  ### дарим в третий раз
            if alice.sorry.give == [1, 1]:  ### ненависное, ненавистное, любимое
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_05 "Лучше поздно, чем никогда! А ну-ка иди сюда..."   #спрайт с ушами
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_26
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        else:
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Слишком уж долго до тебя доходило, что я больше всего люблю... Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            elif alice.sorry.give == [1, 2]:  ### ненавистное, преемлемое, любимое
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_3
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [1, 3]:  ### ненавистное, любимое, любимое
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                menu:
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            menu:
                                Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. Я даже подумываю, а не обнять ли тебя, Макс? Ну так... совсем немного..."
                                "Только если без последующего насилия..." ('soc', mgg.social * 3, 90):
                                    if rand_result:
                                        Alice_04 "[succes!t]Пожалуй ты заслужил это своими подарками..."   #спрайт с обнимашками
                                        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_2
                                        Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
                                        Alice_07 "Я вижу, что ты не просто хочешь избежать наказания, а ещё и мне приятно сделать стремишься. Вот я и не вредничаю..."
                                        Max_05 "Да, надо бы почаще так делать."
                                        Alice_02 "Подглядывать за мной или дарить мне сладости?!"
                                        Max_02 "Второе, конечно!"
                                        Alice_05 "Ну да, конечно... Иди давай."
                                        $ alice.flags.hugs_type = 4
                                    else:
                                        Alice_05 "[failed!t]Ах, а так хотелось! Какой облом..."
                                        Max_09 "Обнять меня или придушить?"
                                        Alice_07 "Зачем останавливаться на чём-то одном, Макс? Хи-хи..."
                                        Max_01 "Я тогда лучше пойду... погуляю."
                                        Alice_02 "Ну как хочешь..."
                                        $ alice.flags.hugs_type = 3
                        else:
                            call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain_1
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [2, 1]:  ### преемлемое, ненавистное, любимое
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_4
                $ AddRelMood('alice', 0, 50)

            elif alice.sorry.give == [2, 2]:  ### преемлемое, преемлемое, любимое
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                menu:
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        else:
                            call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain_2
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 50)

            elif alice.sorry.give == [2, 3]:  ### преемлемое, любимое, любимое
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                menu:
                    Alice_03 "Я даже подумываю, а не обнять ли тебя, Макс? Ну так... совсем немного..."
                    "Только если без последующего насилия..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            call alice_sorry_gifts.you_deserve from _call_alice_sorry_gifts_you_deserve_1
                        else:
                            call alice_sorry_gifts.what_bummer from _call_alice_sorry_gifts_what_bummer_1
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [3, 1]:  ### любимое, ненавистное, любимое
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_5
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [3, 2]:  ### любимое, преемлемое, любимое
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                menu:
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    "Хочется надеяться, что так и будет..." ('soc', mgg.social * 3, 90):
                        if rand_result:
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        else:
                            call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain_3
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 100)

            else:  ### любимое три раза
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                if __give[-1:] == 'm':  #если сладость маленькая
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"   #если сладость маленькая
                    Max_01 "Хочется надеяться, что так и будет..."
                    menu:
                        Alice_03 "Я даже подумываю, а не обнять ли тебя, Макс? Ну так... совсем немного..."
                        "Только если без последующего насилия..." ('soc', mgg.social * 3, 90):
                            if rand_result:
                                call alice_sorry_gifts.you_deserve from _call_alice_sorry_gifts_you_deserve_2
                            else:
                                call alice_sorry_gifts.what_bummer from _call_alice_sorry_gifts_what_bummer_2
                    $ AddRelMood('alice', 0, 100)
                else:    #если сладость большая
                    Alice_05 "Конфет так много, что я не припоминаю, чтобы утром за мной кто-то подглядывал! Всё было в порядке..."
                    Max_01 "Ну да, меня и рядом тогда не было!"
                    Alice_04 "Я даже обниму тебя за это! Ну так... совсем немного... Иди ко мне."   #спрайт с обнимашками
                    call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_3
                    Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
                    Alice_07 "Я вижу, что ты не просто хочешь избежать наказания, а ещё и мне приятно сделать стремишься. Вот я и не вредничаю..."
                    Max_05 "Да, надо бы почаще так делать."
                    Alice_02 "Подглядывать за мной или дарить мне сладости?!"
                    Max_02 "Второе, конечно!"
                    Alice_05 "Ну да, конечно... Иди давай."
                    $ alice.flags.hugs_type = 4
                    $ AddRelMood('alice', 5, 150, 3)

        $ alice.sorry.give.append(3)
        jump .end

    label .end:
        $ spent_time += 10
        $ alice.sorry.owe = False
        $ alice.dcv.shower.stage = 1
        $ alice.dcv.shower.set_lost(3)
        jump Waiting


label alice_about_bath:
    $ alice.flags.incident = 2 if alice.flags.incident<2 else 4
    Alice_12 "Ты о чём, Макс?"
    Max_01 "Ну, ты вернулась ночью из клуба и мы разговаривали в ванной..."
    menu:
        Alice_13 "Я не помню такого... Тебе приснилось!"
        "Ты мне кое-что показала...":
            Alice_05 "Что?! Всё ты врёшь, Макс. Не было такого!"
            Max_02 "Да? Ну, думай так..."
            Alice_13 "Макс. Повторяю, ничего не было. И даже если и было, ты об этом забудешь, если хочешь жить. Ты меня понял?"
            Max_03 "Конечно..."
            Alice_16 "Я серьёзно! А теперь вали отсюда..."
            Max_01 "Хорошо..."
            $ AddRelMood('alice', 0, -50)
            jump .end
        "Ты мне кое-что сделала...":
            pass
        "Мы делали кое-что...":
            pass
        "Да, ну извини...":
            Alice_03 "Надо же, даже извинился... Вот только я правда мало что помню. Будем считать, что ничего и не было. И не напоминай мне больше об этом. Понял?"
            Max_03 "Ага..."
            $ AddRelMood('alice', 0, 50)
            jump .end

    Alice_15 "Что?! Макс! Ты всё врёшь! Если это правда, я тебя убью, обещаю! А если нет, то тоже! Быстро свалил отсюда!"
    Max_01 "Хорошо..."
    $ AddRelMood('alice', 0, -100)
    jump .end

    label .end:
        $ spent_time += 10
        jump Waiting


label alice_about_kiss:
    $ renpy.block_rollback()
    Alice_02 "Прости, Макс, что?"
    Max_01 "Да вот спрашиваю, умеешь ты целоваться или нет?"
    Alice_05 "Да, не показалось... Тебе заняться больше нечем, Макс?"
    Max_08 "Мне срочно нужно научиться целоваться, и я не знаю кто может помочь..."
    Alice_07 "Срочно?! Бедняжка... Ты знаешь, я в каком-то фильме смотрела, там учились целоваться на помидорах. Попробуй, может получится хотя бы у тебя..."
    Max_07 "Алиса, я серьёзно же!"
    Alice_12 "Макс, отвали. Я не буду целоваться с тобой, даже не мечтай. И придумай другой способ клеиться, а то этот на уровне детского сада, серьёзно."
    Max_09 "Да я не клеился!"

    $ flags.how_to_kiss.append('alice')
    $ spent_time += 10
    return


label talkblog2:
    # стартовая фраза "Насчёт блога..."

    Alice_00 "Я тебя внимательно слушаю..."
    Max_00 "Я выяснил, какие блоги популярны..."
    Alice_02 "Открыл топ блогов и посмотрел? Или что-то более толковое удалось выяснить?"
    Max_01 "В общем, тебе нужно сделать акцент на форме, а не на содержании..."
    Alice_01 "Ты хочешь сказать, что не важно о чём мой блог, важно как я его веду? Я об этом думала... И если ты помнишь, проблема всё ещё в одежде. Я не могу в одном и том же появляться постоянно, если это бьюти-блог..."
    Max_07 "А если это не бьюти-блог?"
    Alice_05 "И что же это? Я больше ничего не умею... Или ты на что намекаешь?"
    Max_02 "Как у тебя со скромностью дела?"
    Alice_06 "Кажется, я знаю к чему ты клонишь, Макс. Наверняка, ты насмотрелся каких-нибудь девочек, которые крутят задницами перед камерами за деньги? Нет, я на это не соглашусь!"
    Max_03 "Воу... Я не думал об этом, но если ты говоришь..."
    Alice_12 "Я знаю, что на этом можно много заработать, но вдруг кто-то из моих друзей или знакомых увидит... Нет, я на это не пойду."
    Max_09 "Ты уверена в этом?"
    Alice_00 "Да, Макс! Уверена, я смогу развить свой блог и без этого."
    Max_00 "Ясно. Нет, так нет..."
    $ poss['blog'].open(3 if len(house[1].cams) else 2)  # если камера установлена, открываем стадию 3 иначе 2
    $ spent_time += 10
    jump Waiting


label talkblog3:
    #если Макс стал очевидцем развлечения Алисы во время занятий блогом через камеру
    # стартовая фраза "Насчёт твоего блога... А если не особо раздеваться?"

    Alice_02 "Не особо? Это как? Раздеваться частично?"
    Max_07 "Ты можешь рекламировать что-то..."
    Alice_05 "Макс, да все блогеры что-то рекламируют. Ты снова не изобрёл велосипед..."
    Max_01 "Я имею в виду другое..."
    Alice_03 "Хорошо, я внимательно слушаю..."
    Max_04 "Ты можешь рекламировать нижнее бельё или игрушки для взрослых."
    Alice_05 "Макс... Это не очень отличается от той идеи с позированием перед камерами за деньги... Хотя, в этом что-то есть, конечно. И я не об игрушках для взрослых..."
    Max_03 "Значит, нижнее бельё?"
    Alice_13 "Ну можно попробовать. Однако, главная проблема остаётся в силе, у меня только один комплект белья, тот в котором я сплю, а этого мало даже чтобы просто начать... И денег на новое нет..."
    Max_07 "Ну а если я тебе его подарю?"
    menu:
        Alice_05 "Ты подаришь мне нижнее бельё? На какие деньги? И что я за это буду тебе должна?"
        "Ничего...":
            Alice_02 "И давно ты в альтруисты записался?"
            Max_01 "Я просто хочу помочь..."

        "Может, попозируешь для меня...":
            Alice_02 "Только и всего? Если там что-то приличное, то почему нет..."
            Max_03 "Было бы супер!"

    Alice_03 "Давай попробуем, но я не уверена и ничего не обещаю. Твои вложения могут оказаться бесполезными... Для начала мне нужно бельё просто для того, чтобы заинтересовать людей."
    Max_07 "Для начала?"
    Alice_00 "Ага. Затем, уже нужно будет найти рекламодателей, которые будут присылать бельё, которое я и буду рекламировать. Обычно это так делается... Или ты думал, что мне кто-то будет платить за моё же бельё?"
    Max_00 "Ну, если это так делается..."
    Alice_01 "Да, Макс. Причём, желающих на этом зарабатывать больше, чем желающих за это платить. И в этом главная проблема. Но как я уже сказала, я могу попробовать. Если купишь что-то, посмотрим..."
    Max_01 "Понял, с меня симпатичное бельишко..."
    $ poss['blog'].open(4)
    $ items['b.lingerie'].unblock()
    $ spent_time += 10
    jump Waiting


label gift_black_lingerie:
    # стартовая фраза "У меня есть кое-что, о чём мы беседовали..."
    if _in_replay:
        # формируем фон для воспоминания
        if alice.plan_name == 'sun':
            call alice_sun from _call_alice_sun_1
        else:
            if tm > '20:00':
                call alice_evening_closer from _call_alice_evening_closer_1
            else:
                call alice_morning_closer from _call_alice_morning_closer_1

    Alice_02 "И что же это? Я должна угадать?"
    Max_01 "Нижнее бельё..."
    menu:
        Alice_07 "Ой. Это супер! Симпатичное? Дай посмотреть..."
        "Ну что, примеришь при мне?" if 'pajamas' in alice.gifts or _in_replay:
            Alice_05 "Примерю при тебе? Об этом мы не договаривались. Я покажусь в нём, но... Хотя, ладно. Примерю при тебе, но ты не подглядывай! Увижу, что смотришь, получишь и пойдёшь в бассейн. Вниз головой."

        "Ну что, примеришь при мне?" ('soc', mgg.social * 2, 90) if 'pajamas' not in alice.gifts and not _in_replay:
            if not rand_result:
                # (не удалось убедить)
                Alice_12 "[failed!t]Примерю при тебе? Об этом мы не договаривались. Я покажусь в нём и только... А если будешь и дальше упрашивать, то вообще ничего не увидишь! Понял?"
                Max_10 "Да понял... Ладно. Буду ждать за дверью."

                #на фоне двери в комнату Алисы
                $ renpy.scene()
                $ renpy.show('location house aliceroom door-'+get_time_of_day())
                Max_09 "{m}А посмотреть-то хочется! Быстренько оббежать комнаты и подглядеть в окно? Может заметить... Или пойти в комнату и подглядеть через камеру? Пока дойду и открою свой сайт она уже переоденется... Эх, вот я пролетел!{/m}"
                Alice "{b}Алиса:{/b} Всё, Макс. Можешь заходить..."

                ###Алиса стоит в новом белье
                scene BG char Alice newpajamas
                $ renpy.show('Alice newlingerie '+'08' if '09:00' <= tm < '20:00' else '08e')
                with fade4
                Alice_01 "Ну, как тебе? Хорошо сидит? Вроде бы немного лифчик не того размера... Или нет... Ну, Макс, чего молчишь?"
                Max_05 "Ну, я... э..."
                Alice_05 "Контуженый что ли? Я тебя спрашиваю хорошо сидит или нет... Хотя... по тебе же всё сразу видно. Значит, всё в порядке..."
                Max_02 "Ага, полный порядок!"
                $ poss['blog'].open(5)
                jump .final
            else:
                # (удалось убедить)
                Alice_05 "[succes!t]Примерю при тебе? Об этом мы не договаривались. Я покажусь в нём, но... Хотя, ладно. Примерю при тебе, но ты не подглядывай! Увижу, что смотришь, получишь и пойдёшь в бассейн. Вниз головой."

    Max_00 "Опять угрозы..."
    $ __suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
    if not ('09:00' <= tm < '20:00'):
        $ __suf += 'e'
    scene BG char Alice newpajamas
    $ renpy.show('Alice newpajamas 01'+__suf)
    with fade4
    Alice_03 "Макс, у тебя же есть инстинкт самосохранения, верно? Не вздумай подглядывать!"
    Max_01 "Ага..."
    if not _in_replay:
        $ SetCamsGrow(house[1], 160)

    # примерка
    scene BG char Alice newpajamas
    if renpy.random.randint(0, 1) > 0 and alice.dress!='c':
        # примерка началась без верха
        $ renpy.show('Alice newpajamas 02'+__suf)
        Alice_01 "Макс! Ты что, пялишься на мою грудь? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"   #спрайт без верха
        Max_03 "Я не пялюсь..."

        $ renpy.show('Alice newlingerie 04'+__suf)
        Alice_02 "Похоже, размер мне подходит... и удобно. ... Ну, как тебе?"   #спрайт с одетым лифчиком
        Max_04 "Тебе идёт! Мне нравится..."

        $ __suf = 'a' if alice.dress=='a' and alice.req.result != 'nopants' else 'an'
        $ __suf += 'e' if not ('09:00' <= tm < '20:00') else ''
        if __suf in ['an', 'ane'] and alice.req.result == 'nopants':
            # Алиса без трусиков, согласно договорённости
            Alice_05 "Класс! А теперь быстро отвернись, а то на мне трусиков нет, благодаря твоим уговорам! Нужно ещё новые трусики примерить."
            $ renpy.show('Alice newlingerie 06'+__suf)
            Max_02 "Конечно, я не смотрю..."
        else:
            # Алиса в трусиках или без них, если такая одежда
            Alice_03 "Отлично! А теперь отвернись, не подглядывай! Нужно ещё трусики примерить."
            $ renpy.show('Alice newlingerie 06'+__suf)
            if alice.req.result != 'not_nopants':
                Max_02 "Конечно, я не смотрю..."
            else:
                # Алиса нарушает договор
                Max_08 "Конечно, я не смотрю... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"
                Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                Max_01 "Ладно, считай, я ничего не видел."
                $ alice.req.noted = True

        $ renpy.show('Alice newlingerie '+('08' if '09:00' <= tm < '20:00' else '08e'))
        Alice_07 "Размер в самый раз... ... Как тебе, Макс? Хорошо сидит?"
        Max_05 "Не то слово, всё выглядит шикарно!"
        if not _in_replay:
            $ poss['blog'].open(6)
        jump .final

    else:
        # примерка началась без низа
        $ __suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
        if __suf=='a' and alice.req.result == 'nopants':  # если Алиса без трусиков
            $ __suf += 'n'
        if not ('09:00' <= tm < '20:00'):
            $ __suf += 'e'
        $ renpy.show('Alice newpajamas 03'+__suf)
        if __suf in ['a', 'ae']:
            # Алиса в трусиках
            Alice_03 "Макс! Ты что, пялишься на мой зад? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"
            if alice.req.result != 'not_nopants':
                 # Алиса одета как должно
                Max_02 "Я не пялюсь..."
            else:
                # Алиса нарушает договор
                Max_08 "Я не пялюсь... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"
                Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                Max_01 "Ладно, считай, я ничего не видел."
                $ alice.req.noted = True
        elif __suf in ['an', 'ane']:
            # Алиса без трусиков по уговору
            if not _in_replay:
                $ SetCamsGrow(house[1], 180)
            Alice_05 "Макс! Ты что, пялишься на мой зад? Быстро отвернись, на мне же нет трусиков, благодаря твоим уговорам!"
            Max_02 "Я не пялюсь..."
        else:
            # Алиса без трусиков (такая одежда)
            if not _in_replay:
                $ SetCamsGrow(house[1], 180)
            Alice_03 "Макс! Ты что, пялишься на мой зад? Тут же кругом зеркала и я всё вижу! Быстро отвернись, на мне же нет трусиков!"
            Max_02 "Я не пялюсь..."

        $ __suf = 's' if alice.plan_name in ['sun', 'swim'] else 'a' if alice.dress in ['a', 'c'] else alice.dress
        if not ('09:00' <= tm < '20:00'):
            $ __suf += 'e'
        $ renpy.show('Alice newlingerie 05'+__suf)
        Alice_02 "Размер в самый раз... ... Как тебе, Макс? Хорошо сидят?"
        Max_04 "Не то слово, сидят прекрасно!"
        Alice_01 "Здорово! А теперь отвернись, не подглядывай! Нужно ещё лифчик примерить."

        $ renpy.show('Alice newlingerie '+('07' if '09:00' <= tm < '20:00' else '07e'))
        Max_03 "Конечно, я не смотрю..."

        $ renpy.show('Alice newlingerie '+('08' if '09:00' <= tm < '20:00' else '08e'))
        Alice_07 "Похоже, размер мне подходит... и удобно. Очень лёгонький топик. Ну, как тебе всё в целом?"
        Max_05 "Тебе идёт, всё выглядит шикарно!"
        if not _in_replay:
            $ poss['blog'].open(6)
        jump .final

    label .final:
        if not _in_replay:
            call alice_add_black_linderie from _call_alice_add_black_linderie
            # ставим откат, после которого откроются фотик и сексбоди
            $ alice.dcv.photo.set_lost(8)

    Alice_02 "Ну, спасибо тебе. Да, в этом точно можно покрасоваться перед камерами. Не уверена, что даст эффект, но я же одета... В общем, я попробую!"
    Max_04 "Этого достаточно?"
    Alice_03 "Сомневаюсь, если честно. Ты знаешь... Давай попробуем на всякий случай ещё кое-что. Поищи что-нибудь более сексуальное. Ничего не обещаю, но вдруг поможет..."
    Max_01 "Хорошо, я что-нибудь подыщу..."
    $ renpy.end_replay()

    $ spent_time += 30
    jump Waiting


label alice_gift_sweets:   # Периодическое дарение сладости

    if alice.sorry.owe and alice.sorry.days[0] == day:
        Max_09 "{m}Думаю, не стоит дарить вкусняшку сегодня. Это может вызвать ненужные подозрения... Лучше это сделать завтра.{/m}"
        $ alice.daily.sweets = 1
        return

    if not alice.sorry.owe and not alice.dcv.sweets.done:
        Max_09 "{m}Ещё рановато для сладостей, так недолго и фигуру Алисе испортить. Лучше немного подождать...{/m}"
        $ alice.daily.sweets = 1
        jump Waiting

    # $ renpy.dynamic("give")
    menu:
        Alice_02 "Да ладно! Это мне нравится... И что там у тебя?"
        "Конфеты \"Ferrero Rocher\" (16 штук)" if items['ferrero-m'].have:
            $ give = 'ferrero-m'
        "Конфеты \"Ferrero Rocher\" (24 штуки)" if items['ferrero-b'].have:
            $ give = 'ferrero-b'

    $ items[give].use()
    Alice_07 "Ага! Мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
    Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
    if give=='ferrero-m':
        # маленькая коробка
        menu:
            Alice_03 "Я даже подумываю, а не обнять ли тебя за это, Макс? Ну так... совсем немного..."
            "Только если без последующего насилия..." ('soc', mgg.social * 3, 90):
                pass
        if rand_result:
            Alice_04 "[succes!t]Ладно, Макс, пожалуй ты это заслужил..."
            # спрайт с обнимашками
            call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_4
            Max_03 "Хорошо, что хоть так можно взять и обнять тебя без ущерба своему здоровью!"
            Alice_07 "Я вижу, что ты действительно стремишься сделать мне приятно, вот я и не вредничаю..."
            Max_05 "Да, надо бы почаще так делать."
            Alice_13 "Ой, Макс, нет! Почаще - не надо... А то я фигуру испорчу, мне так нельзя!"
            Max_02 "Согласен, такую стройную фигуру лучше не портить... Но временами, любимыми конфетами можно и побаловаться!"
            Alice_05 "Ну да, временами... И сейчас как раз такой момент!"
            Max_01 "Наслаждайся, сластёна! Не буду мешать..."
            $ alice.flags.hugs += 1
            $ infl[alice].add_m(6 if alice.sorry.owe else 12)
        else:
            Alice_05 "[failed!t]Ах, а так хотелось! Какой облом..."
            # спрайт с ушами
            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_27
            Max_09 "Ну вот, я тебе любимые конфеты покупаю от чистого сердца, а ты..."
            Alice_07 "Не повезло тебе просто сегодня... Если бы купил большую коробку конфет, я бы чувствовала себя самой любимой сестрёнкой! А так..."
            Max_01 "Понятно всё с тобой. Я тогда лучше пойду..."
        $ AddRelMood('alice', 10, 100, 3)
    else:
        # большая коробка
        Alice_04 "Я даже обниму тебя за это! Ну так... совсем немного... Иди ко мне."
        # спрайт с обнимашками
        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_5
        Max_03 "Хорошо, что хоть так можно взять и обнять тебя без ущерба своему здоровью!"
        Alice_07 "Я вижу, что ты действительно стремишься сделать мне приятно, вот я и не вредничаю..."
        Max_05 "Да, надо бы почаще так делать."
        if all([alice.daily.oiled==2, mgg.dress>'b']):
            # Алиса без лифчика, Макс в одних шортах
            Alice_12 "Так, Макс, это что за дела? У тебя почему стоит? На меня что ли?"
            Max_02 "Даже не знаю! Здесь больше никого нет. Похоже, что на тебя..."
            Alice_03 "Ты же в курсе, что есть иные способы сказать, что я нисколько не порчу этими конфетами фигуру?"
            Max_04 "Ну, а я выдал комплимент без слов! Честнее некуда."
            Alice_05 "Ну да, я вижу... Считай, этот комплимент принят!"
            Max_01 "Наслаждайся конфетами, сластёна! Не буду мешать..."
        else:
            Alice_13 "Ой, Макс, нет! Почаще - не надо... А то я фигуру испорчу, мне так нельзя!"
            Max_02 "Согласен, такую стройную фигуру лучше не портить... Но временами, любимыми конфетами можно и побаловаться!"
            Alice_05 "Ну да, временами... И сейчас как раз такой момент!"
            Max_01 "Наслаждайся, сластёна! Не буду мешать..."
        $ alice.flags.hugs += 1
        $ infl[alice].add_m(10 if alice.sorry.owe else 20)
        $ AddRelMood('alice', 15, 150, 3)
    $ spent_time += 10
    $ alice.daily.sweets = 1

    # включаем откат на дарение сладости
    if alice.sorry.owe:
        $ alice.sorry.owe = False
        $ alice.dcv.shower.stage = 1
        $ alice.dcv.shower.set_lost(3)
        if alice.dcv.sweets.lost < 3:
            $ alice.dcv.sweets.set_lost(3)
    else:
        $ alice.dcv.sweets.set_lost(renpy.random.randint(5, 7))
    jump Waiting


label alice_about_lingerie0:
    Alice_12 "Слышал или подслушал?"
    Max_01 "Слышал. Эрик мне и сказал."
    Alice_05 "Да, мне нужно ещё одно сексуальное боди. И я показала ему, какое конкретно хочу. Решили, что купим, когда поедем на шопинг в субботу. А что?"
    Max_02 "Да так, интересно было, какое ты себе боди захотела. Покажешь?"
    if current_room == house[1]:
        jump alice_showing_lingerie1
    else:
        Alice_03 "Для этого компьютер нужен. Так что, если интересно, то заходи, когда я в своей комнате. Покажу..."
        Max_01 "Ага. Обязательно зайду"
        $ alice.dcv.intrusion.stage = 2  # Макс говорил с Алисой о белье, которое купит Эрик, но подошел не вовремя

    $ spent_time += 10
    jump Waiting


label alice_showing_lingerie1:  #Алиса показывает Максу бельё, которое она выбрала
    #если Алиса за ноутбуком (во время блога и утром)
    # blog-desk-01 + alice 02 + max 04 (для блога, для утра - на фон кровати Алисы)
    if tm>='20:00' and weekday in [3, 4]:
        $ renpy.show('Alice blog 02'+alice.dress)
        $ renpy.show('Max blog 04'+mgg.dress)
    Alice_03 "Вот, смотри... Боди, как боди, слегка прозрачное и кружевное. Всё, как вы, мальчики, любите."
    Max_03 "Ну да, мне уже не терпится увидеть его на тебе!"
    Alice_05 "Это если я ещё разрешу тебе смотреть на меня в этом боди! Вот Эрик купит - ему и можно будет смотреть, ну и тем, для кого я всё это рекламирую."
    Max_11 "А как же я?"
    Alice_02 "Интернет тебе в помощь, Макс! Там полно всяких разных девушек в любом нижнем белье. Может и меня там найдёшь, уже..."
    Max_08 "Ладно, я тебя понял."
    Max_09 "{m}Мне ещё как можно будет на тебя смотреть, когда я куплю это боди первее Эрика! Вот только времени совсем в обрез, надо торопиться... Блин, Эрик точно будет этому не рад! Стоит ли оно того, это боди?{/m}"

    $ alice.dcv.intrusion.stage = 3  # Макс знает, какое бельё хочет Алиса
    $ items['sexbody2'].unblock()
    $ poss['blog'].open(14)
    $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    $ spent_time += 10
    jump Waiting


label gift_lace_lingerie:

    # стартовая фраза "Я тут не удержался и купил тебе боди раньше Эрика!"
    Alice_15 "Ого! В смысле, то самое, которое я тебе показывала или какое-то другое?"
    Max_01 "Да, то самое. Ты же не против?"
    Alice_05 "Конечно не против! Давай его сюда, буду примерять... Только, если не будешь смотреть..."
    Max_03 "Конечно! Мне не терпится увидеть, как оно на тебе сидит..."

    # spider-night-04 + aliceroom-blog-dresses-01-max-(01/01a) + Алиса в белье(spider-night-04-alice-(01/02/03) / spider-night-04-alice-(01a/02a/03a) / aliceroom-blog-dresses-01-alice-(01a/02a/03a))
    scene BG char Alice spider-night-04
    $ renpy.show('Max newbody2 01'+mgg.dress)
    $ renpy.show('Alice newbody2 '+renpy.random.choice(['01', '02', '03'])+alice.dress)
    with fade4
    Alice_12 "Неплохо это ты уселся в первых рядах, Макс! Отвернись хоть для приличия или живо пойдёшь гулять..."
    Max_02 "Я глаза закрою..."

    # spider-night-04 + aliceroom-blog-dresses-01-max-(01/01a) + Алиса раздевается(spider-night-04-alice-(04/05/06) / spider-night-04-alice-(04a/05a/06a) / aliceroom-blog-dresses-01-alice-(04a/05a/06a))
    $ renpy.show('Alice newbody2 '+renpy.random.choice(['04', '05', '06'])+alice.dress)
    Alice_14 "Эй! Макс! Ты же сказал, что закроешь глаза. Хорошо я заметила, что ты пялишься на меня, прежде чем всё с себя сняла! Отвернись, быстро! Ну или хотя бы закрой глаза руками..."
    Max_04 "Ты так красиво начала раздеваться, что я забыл не смотреть. Считай, закрыл."

    # spider-night-04 + aliceroom-blog-dresses-01-max-(02/02a) + Алиса раздевается(spider-night-04-alice-(04/05/06) / spider-night-04-alice-(04a/05a/06a) / aliceroom-blog-dresses-01-alice-(04a/05a/06a))
    $ renpy.show('Max newbody2 02'+mgg.dress)
    Alice_05 "Смотри мне, Макс! Я ведь сразу увижу в зеркало, если ты начнёшь подглядывать сквозь пальцы. Ты же не хочешь получить с ноги за это?"
    menu:
        Max_19 "Естественно, не хочу."
        "{i}подглядывать{/i}" ('hide', mgg.stealth * 1.5, 90):
            show FG blog-dresses-max-03
            if rand_result:
                # (повезло)
                # spider-night-04 + aliceroom-blog-dresses-01-max-(02/02a + (aliceroom-blog-dresses-01-max-03)) + Алиса голая(aliceroom-blog-dresses-02-alice-(01a/02a))
                $ renpy.show('Alice newbody2 '+renpy.random.choice(['07', '08']))
                Max_02 "{m}Ага, взял и закрыл! Я что, совсем святой, чтобы не рискнуть хоть одним глазком увидеть голую Алису! Да ещё так близко! Бесподобная у меня сестрёнка...{/m}"
                # spider-night-04 + aliceroom-blog-dresses-01-max-(02/02a + (aliceroom-blog-dresses-01-max-03)) + Алиса одевается(aliceroom-blog-dresses-02-alice-(03a/04a))
                $ renpy.show('Alice newbody2 '+renpy.random.choice(['09', '10']))
                Max_07 "{m}Ухх... Алиса не спешит спрятать свои аппетитные сисечки под боди! Прямо, как мне и хочется... Хм, а может она заметила, что я всё равно подглядываю и таким образом дразнит меня?! Знать бы это наверняка...{/m}"

            else:
                # (не повезло)
                # spider-night-04 + aliceroom-blog-dresses-01-max-(02/02a) + Алиса раздевается(spider-night-04-alice-(04/05/06) / spider-night-04-alice-(04a/05a/06a) / aliceroom-blog-dresses-01-alice-(04a/05a/06a))
                Alice_18 "Макс!!!"
                hide FG
                menu:
                    Max_08 "Не бей! Я просто тебя проверял. На внимательность..."
                    "{i}ждать{/i}":
                        pass
        "{i}ждать{/i}":
            pass


    # spider-night-04 + aliceroom-blog-dresses-01-max-(01/01a) + Алиса в новом боди(aliceroom-blog-dresses-02-alice-05a)
    hide FG
    $ renpy.show('Max newbody2 01'+mgg.dress)
    show Alice newbody2 11
    Alice_02 "Всё, можно смотреть... Что скажешь, тебе нравится или нет? Мне вот в нём удобно..."
    Max_04 "Алиса, на твоём чудесном теле, что угодно будет смотреться шикарно. И да, мне нравится, как это выглядит! Покрутись ещё немного для меня..."

    # spider-night-04 + aliceroom-blog-dresses-01-max-(01/01a) + Алиса в новом боди(aliceroom-blog-dresses-02-alice-06a)
    show Alice newbody2 12
    Alice_06 "Ну как, всё посмотрел? Ай!!! У меня ногу свело! Ой, как же сильно свело... Ой-ёй-ёй!!!"
    Max_07 "Которую? Давай её мне, я помассирую..."

    # aliceroom-blog-mass-01-f + aliceroom-blog-mass-01-alice-01 + aliceroom-blog-mass-01-max-(01a/01b)
    scene BG char Alice blog-mass-01
    show Alice newbody2 mass-01
    $ renpy.show("Max newbody2 mass-01"+mgg.dress)
    Alice_13 "Правую. Ой, Макс! По-моему, лучше не трогать... Очень уж тянет. А хотя... вроде лучше... Да, так намного лучше... Фух!"
    Max_09 "Многовато ты за компьютером времени проводишь. Двигаться надо побольше."
    Alice_05 "Ой, ну вторая мама появилась у меня! Просто разок свело ногу, подумаешь."
    Max_08 "Ага, скоро снова сведёт, это я тебе гарантирую. На онлайн-курсах узнал, если сводит, то нужно или двигаться больше, или массаж делать серьёзнее."

    # aliceroom-blog-mass-02-f + aliceroom-blog-mass-02-alice-01 + aliceroom-blog-mass-02-max-(01a/01b)
    scene BG char Alice blog-mass-02
    show Alice newbody2 mass-02
    $ renpy.show("Max newbody2 mass-02"+mgg.dress)
    Alice_03 "Двигаться больше — это спортом заниматься, ты хочешь сказать? Не люблю я это. Я люблю на солнышке понежиться, за книжкой посидеть или перед экраном ТВ или компьютера. Ты же знаешь."
    Max_07 "Знаю. Значит массаж. Надо больше внимания уделить твоим ножкам. Согласна?"
    Alice_05 "А согласна! Ты так самоотверженно мне сейчас ногу помассировал. Даже ни разу не попытался на грудь мою засмотреться или ещё куда. А боди ведь слегка прозрачное!"
    Max_02 "Да я твои сосочки наизусть знаю! Это шутка..."
    Alice_01 "Но правдивая, извращенец ты мелкий! Давай гуляй, у меня блог простаивает... И спасибо за подарок. Нужно будет Эрику не забыть сказать, что ты его опередил. Это же не станет для вас проблемой?"
    Max_01 "Разберёмся как-нибудь, не переживай."

    #открывается возможность массировать Алисе бёдра во дворе (с ограничениями)
    $ renpy.end_replay()
    $ added_mem_var('lace_ling_max1')
    $ spent_time += 40
    $ alice.dcv.intrusion.stage = 5  # бельё Алисе подарил Макс
    $ items['sexbody2'].give()
    $ alice.gifts.append('sexbody2')
    $ setting_clothes_by_conditions()
    $ infl[alice].add_m(40)
    $ poss['blog'].open(18)
    jump Waiting


label alice_about_defend_punish0:

    # "Хотел узнать, хорошо ли тебе сидится?"
    Alice_12 "Эээ... Прекрасно сидится, как видишь."
    Max_02 "Ну ещё бы, ведь твою симпатичную попку никто сегодня не отшлёпал, благодаря мне."
    Alice_05 "А, вот ты о чём! Ну да, моя попка цела и невредима. Почаще бы ты меня от маминой руки ещё спасал, было бы супер!"
    Max_07 "Да как-то не очень хочется, на самом деле, вообще это делать. По крайней мере за просто так."
    Alice_13 "А что ты хочешь? Гадости какие-нибудь наверняка..."
    Max_03 "Самое правильное - это всё равно тебя наказать! Только в отличие от мамы, я сделаю это с нежностью."
    Alice_15 "Чего?! Вот ещё! Чтобы меня младший брат наказывал? Обойдёшься, Макс!"
    Max_09 "Ты уверена? Ох, не сладко тебе будет без моего вмешательства. Но дело твоё."
    Alice_05 "Вот именно."

    $ spent_time += 10
    $ alice.dcv.private.stage = 1
    $ poss['ass'].open(1)
    jump Waiting


label alice_about_defend_punish1:

    # "Не слабо тебя отшлёпали!"
    $ alice.dcv.private.stage = 3
    Alice_13 "Так ты позлорадствовать пришёл. Нет, чтобы заступиться за сестрёнку..."
    Max_01 "Если разрешишь тебя немного пошлёпать за это, то буду заступаться."
    Alice_12 "Макс, давай иначе договоримся? Это отстой..."
    Max_09 "Иногда получать от меня легонько по попке - это значит отстой, а всегда и сурово от мамы - это класс?! Ты ведь даже не знаешь, как я буду шлёпать!"
    menu:
        Alice_16 "Я и узнавать не хочу!"
        "Ладно, как знаешь..." ('soc', mgg.social * 1.5, 90):   #(убеждение)
            jump .convince

    label .cont:
        menu:
            Alice_12 "Чтобы меня младший брат наказывал? Обойдёшься, Макс!"
            "Ладно, как знаешь..." ('soc', mgg.social * 1.5, 90):   #(убеждение)
                jump .convince

    label .convince:
        if not rand_result:
            # (не удалось)
            Alice_17 "Я лучше от мамы наказания потерплю, чем от тебя..."
            Max_07 "Ох, не завидую я тебе..."
        else:
            # (удалось)
            Alice_06 "А ты точно не больно будешь шлёпать?"
            Max_04 "Точно."
            Alice_05 "Ладно, можешь меня шлёпать. Конечно, если от мамы спасёшь. Тогда и поговорим."
            Max_01 "Я постараюсь."
            $ poss['ass'].open(2)
            $ alice.dcv.private.stage = 4
            $ alice.dcv.private.set_lost(0)

    $ spent_time += 10
    jump Waiting


label alice_about_private_punish:

    if tm> '19:00' and 1<weekday<5:
        #если приватное наказание выпадает на пн-пт
        Alice_13 "Макс, давай завтра! Днём, например. Когда мы дома одни остаёмся... Ну и всё, что выпадет на выходные дни, будем переносить на понедельник, хорошо?"
        $ alice.dcv.private.set_lost(2)
    else:
        #если приватное наказание выпадает на сб-вс
        Alice_13 "Макс, давай теперь уже в понедельник днём! Когда мы дома одни остаёмся..."
        $ alice.dcv.private.set_lost(2+weekday-5)

    Max_04 "Без проблем."
    Alice_16 "И смотри, если мне будет больно, то ты с фингалом ходить неделю будешь... Ясно?"
    Max_01 "Ага, не переживай."
    $ alice.flags.private = True
    $ poss['ass'].open(3)
    $ spent_time += 10
    jump Waiting


label alice_private_punish_0:
    # "Пора отшлёпать одну милую попку!"
    Alice_03 "Эх, Макс... Я так хорошо лежала и загорала. Ну да ладно, где это сделам?"
    jump .pun

    menu .smoke:
        Alice_00 "Макс, поглазеть пришёл?"
        "Пора отшлёпать одну милую попку!":
            Alice_05 "Да, Макс, сейчас... Только дай докурю спокойно и я в твоём распоряжении."
            menu:
                Max_03 "Хорошо. Я подожду..."
                "{i}подождать Алису{/i}":
                    pass
            # punish-sun-01 + punish-sun-01-alice-01 + punish-sun-01-max-(01a/01b)
            scene BG punish-sun 01
            show Alice punish-sun 01-01
            $ renpy.show("Max punish-sun 01-01"+mgg.dress)
            Alice_03 "Всё, я готова. Где это сделаем?"
            jump .pun

    label .pun:
        Max_01 "Да прямо тут, во дворе."

    if alice_sun_topless():
        # punish-sun-02 + punish-sun-02-max-(01a/01b)-alice-01a
        scene BG punish-sun 02
        $ renpy.show('Alice punish-sun 02-01'+mgg.dress+'a')
        with fade4
    else:
        # punish-sun-02 + punish-sun-02-max-(01a/01b)-alice-01
        scene BG punish-sun 02
        $ renpy.show('Alice punish-sun 02-01'+mgg.dress)
        with fade4
    Alice_05 "Ладно, давай здесь. Только не больно, хорошо? И не приставать!"
    Max_02 "Ага, раздевайся давай..."

    if alice_sun_topless():
        # punish-sun-02 + punish-sun-02-max-(01a/01b)-alice-01a
        $ renpy.show('Alice punish-sun 02-02'+mgg.dress+'a')
    else:
        # punish-sun-02 + punish-sun-02-max-(02a/02b)-alice-02
        $ renpy.show('Alice punish-sun 02-02'+mgg.dress)
    Alice_14 "Чего?! В смысле, раздевайся? О таком мы не договаривались!"
    Max_07 "Это само собой разумеющееся, Алиса. Со всеми претензиями обращайся к маме, это ведь она установила такой порядок наказаний."
    Alice_13 "Если ты думаешь, что я стану тут перед тобой раздеваться..." nointeract
    if not alice_sun_topless():
        menu:
            "{i}стянуть верх купальника{/i}":
                # punish-sun-02 + punish-sun-02-max-(03a/03b)-alice-03
                $ renpy.show("Alice punish-sun 02-03"+mgg.dress)
                Alice_15 "Макс!!! Ты офигел так делать?! Я же тебе сейчас уши оторву..."
                Max_09 "Сколько от тебя шума, Алиса! Да ещё и по такому пустяку. Надоели уже твои угрозы." nointeract
    menu:
        "{i}стянуть низ купальника{/i}":
            pass
    # punish-sun-02 + punish-sun-02-max-(04a/04b)-alice-04
    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
    Alice_06 "Дикарь ты и извращенец! Я тебе потом такое устрою..."
    Max_01 "Ага, обязательно. Только давай сперва тебя накажем."
    menu:
        Alice_12 "Только не вздумай глазеть на меня при этом!"
        "{i}шлёпать сильно{/i}":
            play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop
            # punish-sun-03 + punish-sun-03-max-(01a/01b)-alice-01
            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            show screen Cookies_Button
            Alice_18 "Ай, ай, ай! Больно же! Ну ты чего, Макс? Меня и мама могла также отшлёпать. Всё, хватит!"
            Max_07 "Это же наказание всё-таки, Алиса. Должно быть немножко больно."
            hide screen Cookies_Button
            # punish-sun-04 + punish-sun-04-max-(03a/03b)-alice-03
            scene BG punish-sun 04
            $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
            stop sound
            Alice_15 "Это не немножко... У тебя ещё и стоит на всё это! Я в шоке! Прикрылся бы хоть..."
            Max_03 "Ну, ты же девушка... И очень привлекательная!"
            Alice_17 "И что? Я ещё и твоя сестра! Забыл? Всё, мы закончили. И что у тебя там, вообще, в башке творится..."
            Max_02 "Хорошо, до следующего раза. А попка у тебя славная!"
            menu:
                Alice_13 "Ох, и зачем я на всё это согласилась..."
                "{i}уйти{/i}":
                    jump .end

    label .end:
        $ spent_time += 30
        $ poss['ass'].open(4)
        $ alice.dcv.private.stage = 5
        $ alice.dcv.private.set_lost(0)
        $ alice.dcv.prudence.set_lost(renpy.random.randint(1, 3))
        $ alice.spanked = True
        jump Waiting


label alice_private_punish_r:
    # "Пора отшлёпать одну милую попку!"
    Alice_03 "Эх, Макс... Я так хорошо лежала и загорала. Ну да ладно, давай побыстрее с этим покончим..."
    jump .pun

    label .smoke:
        Alice_05 "Да, Макс, сейчас... Только дай докурю спокойно и я в твоём распоряжении."
        menu:
            Max_03 "Хорошо. Я подожду..."
            "{i}подождать Алису{/i}":
                jump .smoke_pun

    label .smoke_pun:
        # punish-sun-01 + punish-sun-01-alice-01 + punish-sun-01-max-(01a/01b)
        scene BG punish-sun 01
        show Alice punish-sun 01-01
        $ renpy.show("Max punish-sun 01-01"+mgg.dress)
        Alice_03 "Всё, я готова. Давай побыстрее с этим покончим..."
        jump .pun

    label .pun:
        Max_01 "А ты куда-то торопишься разве?"

    if alice_sun_topless():
        # punish-sun-02 + punish-sun-02-max-(01a/01b)-alice-01a
        scene BG punish-sun 02
        $ renpy.show('Alice punish-sun 02-01'+mgg.dress+'a')
        # with fade4
    else:
        # punish-sun-02 + punish-sun-02-max-(01a/01b)-alice-01
        scene BG punish-sun 02
        $ renpy.show('Alice punish-sun 02-01'+mgg.dress)
        # with fade4
    Alice_05 "Мне же больше делать нечего, только и жду с самого утра, когда ты придёшь и накажешь меня!"
    Max_02 "Сама разденешься или помочь?"
    if alice_sun_topless():
        # punish-sun-02 + punish-sun-02-max-(01a/01b)-alice-01a
        $ renpy.show('Alice punish-sun 02-02'+mgg.dress+'a')
    else:
        # punish-sun-02 + punish-sun-02-max-(02a/02b)-alice-02
        $ renpy.show('Alice punish-sun 02-02'+mgg.dress)
    Alice_04 "Вот тебе надо, чтобы я была голая, так сам и раздевай! Не облегчать же тебе работу..." nointeract
    if not alice_sun_topless():
        menu:
            "{i}стянуть верх купальника{/i}":
                # punish-sun-02 + punish-sun-02-max-(03a/03b)-alice-03
                $ renpy.show("Alice punish-sun 02-03"+mgg.dress)
                Alice_15 "Ну не так же резко, Макс! Смотри, если порвёшь мой купальник, я тебе тоже мигом что-нибудь порву..." nointeract
    menu:
        "{i}стянуть низ купальника{/i}":
            pass
    # punish-sun-02 + punish-sun-02-max-(04a/04b)-alice-04
    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
    menu:
        Alice_06 "И чего глазеем? Шлёпай давай! Руки только не распускай слишком сильно."
        "{i}шлёпать нежно{/i}":
            # punish-sun-03 + punish-sun-03-max-(01a/01b)-alice-01
            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            show screen Cookies_Button
            play sound [slap3, "<silence .5>", slap3, "<silence .5>", slap3, "<silence 1.5>"] loop
            menu:
                Alice_05 "Ты там уже начал? А то мне показалось, что это больше тянет на поглаживания, а не на шлепки..."
                "И как, тебе нравится?":
                    hide screen Cookies_Button
                    # punish-sun-02 + punish-sun-02-max-(05a/05b)-alice-05
                    scene BG punish-sun 02
                    $ renpy.show("Alice punish-sun 02-05"+mgg.dress)
                    stop sound
                    Alice_02 "Мне нравится, что небольно. Ну всё, потискал мою попку и хватит. А то, если тебя не остановить, ты так и будешь залипать, куда не надо..."
                    Max_03 "Просто зрелище такое... завораживающее."
                    # punish-sun-02 + punish-sun-02-max-(04a/04b)-alice-04
                    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
                    Alice_03 "Ты меня своим озабоченным взглядом не смущай. Вали уже, оденусь я без твоей помощи..."

                "Могу сильнее, раз ты заскучала!":
                    play sound [slap2, "<silence .5>", slap2, "<silence .5>", slap2, "<silence 1.5>"] loop
                    $ __r1 = renpy.random.randint(1, 2)
                    # punish-sun-04 + punish-sun-04-max-(01a/01b)-alice-01 или punish-sun-04-max-(02a/02b)-alice-02
                    scene BG punish-sun 04
                    $ renpy.show("Alice punish-sun 04-0"+str(__r1)+mgg.dress)
                    Alice_06 "Ой, Макс! Ну ты чего? Так уже больно. Ты же говорил, что будешь с нежностью шлёпать!"
                    stop sound
                    Max_04 "А я потру, чтобы не болело... Так легче?"
                    # punish-sun-05 + punish-sun-05-max-(01a/01b)-alice-01 или punish-sun-05-max-(02a/02b)-alice-02
                    scene BG punish-sun 05
                    $ renpy.show("Alice punish-sun 05-0"+str(__r1)+mgg.dress)
                    Alice_13 "Да, я не жалуюсь... Но можно было ведь и дальше шлёпать легонько."
                    Max_07 "Это я чисто, чтобы напомнить, что это всё равно наказание."
                    Alice_02 "Ну всё, потискал мою попку и хватит. А то, если тебя не остановить, ты так и будешь залипать, куда не надо..."
                    Max_03 "Просто зрелище такое... завораживающее."
                    # punish-sun-04 + punish-sun-04-max-(03a/03b)-alice-03
                    scene BG punish-sun 04
                    $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
                    Alice_03 "Ага, сложно не заметить, сколько радости от этого в твоих шортах. Приму это за комплимент, но хватит уже меня смущать своим озабоченным видом!"
                    if not _in_replay:
                        $ poss['ass'].open(5)
                        $ alice.flags.privpunish += 1
            menu:
                Max_02 "Хорошо, до следующего раза."
                "{i}уйти{/i}":
                    jump .end

        "{i}шлёпать сильно{/i}": # if not _in_replay:
            play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop
            # punish-sun-03 + punish-sun-03-max-(01a/01b)-alice-01
            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            show screen Cookies_Button
            Alice_18 "Ай, ай, ай! Больно же! Ну ты чего, Макс? Меня и мама могла также отшлёпать. Всё, хватит!"
            Max_07 "Это же наказание всё-таки, Алиса. Должно быть немножко больно."
            stop sound
            hide screen Cookies_Button
            # punish-sun-04 + punish-sun-04-max-(03a/03b)-alice-03
            scene BG punish-sun 04
            $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
            Alice_15 "Это не немножко... У тебя ещё и стоит на всё это! Я в шоке! Прикрылся бы хоть..."
            Max_03 "Ну, ты же девушка... И очень привлекательная!"
            Alice_17 "И что? Я ещё и твоя сестра! Забыл? Всё, мы закончили. И что у тебя там, вообще, в башке творится..."
            Max_02 "Хорошо, до следующего раза. А попка у тебя славная!"
            menu:
                Alice_13 "Ох, и зачем я на всё это согласилась..."
                "{i}уйти{/i}":
                    jump .end

    label .end:
        $ renpy.end_replay()
        $ spent_time += 30
        $ alice.dcv.private.set_lost(0)
        $ alice.dcv.prudence.set_lost(renpy.random.randint(1, 3))
        $ alice.spanked = True
        jump Waiting


label alice_gift_mistress1:

    Alice_14 "Подожди! Ты серьёзно достал деньги на кожаный костюм?! Неужели ты действительно его купил?!"
    Max_01 "Разумеется! Твой кожаный костюм, как ты и хотела. Вот, держи..."

    if not alice.sorry.owe:  # не успел подарить вовремя
        Alice_02 "О да! Моя мечта сбылась! Ты такой молодец, Макс! Правда, со сроками ты опоздал, но спасибо тебе большое, что всё-таки подарил..."
        Max_07 "Ну так, зря я что ли деньги на этот костюм собирал? Может хоть примеришь его при мне?"
    else:   # подарил вовремя
        Alice_07 "О да! Моя мечта сбылась! Ты такой молодец, Макс! Спасибо тебе большое..."
        Max_02 "Ну что, примеришь его при мне?"

    Alice_13 "Примерю при тебе? Разве мы с тобой об этом договаривались?"
    Max_08 "Нет, но... просто я подумал... Почему бы и не примерить?"
    Alice_12 "Что? Раз ты мне его купил, то я обязательно тебе в нём должна показаться? Так ты считаешь, да? Костюмчик ведь для ролевых игр, а мы с тобой вообще-то брат и сестра!"
    Max_05 "Видишь, даже играть не нужно!"
    Alice_16 "Ну, Макс! Если продолжишь прикалываться в таком же духе дальше, то я сыграю нашу маму, только вот бить буду ногами и со всего размаху! Давай гуляй иди... Или тебе помочь?"
    Max_10 "Нет, я сам."

    $ alice.sorry.valid = {'ferrero-b', 'ferrero-m'}

    $ alice.sorry.give.append(5)
    $ alice.sorry.owe = False
    $ alice.gifts.append('mistress1')
    $ items['mistress1'].give()
    $ poss['risk'].open(12)
    $ spent_time += 10
    $ infl[alice].add_m(40)
    jump Waiting


label alice_gift_whip:

    Alice_15 "Да где ты деньги-то на всё это берешь?! Надеюсь, она именно такая, как я просила..."
    Max_02 "О да! Твоя плётка для садо-мазо, как ты и хотела. Вот, держи..."
    Alice_13 "Какое садо-мазо, Макс, что ты несёшь?"
    Max_01 "Ну так, а для чего же она ещё?"
    Alice_05 "Может быть тебе показать? С удовольствием продемонстрирую... прямо на твоей заднице!"

    if not alice.sorry.owe:  # не успел подарить вовремя
        Max_10 "Нет-нет... Спасибо, но посягательств от мамы более чем хватило! Так что не надо."
    else:   # подарил вовремя
        Max_08 "Нет-нет... не надо!"

    Alice_01 "Точно не надо? А то я могу!"
    Max_07 "Точно! Я как-нибудь обойдусь..."
    Alice_02 "Вот то-то же! А, вообще, ты молодец, Макс! Спасибо тебе..."
    Max_01 "Да на здоровье..."

    $ alice.sorry.valid = {'ferrero-b', 'ferrero-m'}

    $ alice.sorry.give.append(6)
    $ alice.sorry.owe = False
    $ alice.gifts.append('whip')
    $ items['whip'].give()
    $ poss['risk'].open(14)
    $ spent_time += 10
    $ infl[alice].add_m(40)
    jump Waiting


label alice_mistress_0:

    call alice_tv_closer from _call_alice_tv_closer_1

    Alice_16 "Господи, ну что за детский сад?! Что ты не будешь?"

    Max_10 "Подглядывать..."
    Alice_17 "Нет, Макс, так не пойдёт! Я не услышала искренности в твоих словах!"
    Max_09 "И что мне теперь, в театральный поступать?"
    Alice_05 "Нет, мы поступим проще... Тебе придётся пойти со мной!"
    Max_08 "Куда это? Зачем?"
    menu:
        Alice_01 "Сейчас узнаешь... Пошли в мою комнату..."
        "{i}идти за Алисой{/i}":
            pass

    # aliceroomdoor-04-night
    scene location house aliceroom door-night
    Alice "{b}Алиса:{/b} Жди за дверью, Макс! Я сейчас подготовлюсь и позову тебя."
    Max_09 "К чему подготовишься?"
    Alice "{b}Алиса:{/b} Немного терпения и ты всё узнаешь!"
    Max_14 "Ладно. Жду..."
    Max_09 "{m}Хм... Меня начинают терзать смутные сомнения, насчёт того, к чему она там готовится. Уж как-то подозрительно она улыбалась, когда я извинялся.{/m}"
    menu:
        Alice "{b}Алиса:{/b} Можешь входить, если ты ещё не сбежал..."
        "{i}войти в комнату{/i}":
            pass

    # alice-blog-evening-01 + domin-00-max-(01a/01b) + domin-00-alice-01
    scene BG char Alice evening
    $ renpy.show('Max domin 00'+mgg.dress)
    show Alice domin 00
    Max_05 "{m}Ох, ничего себе, вот это вид! Она такая секси в этом костюмчике. А говорила, что не покажется мне в нём!{/m}"
    Alice_02 "Ну же, Макс, чего ты застыл в дверях, проходи!"
    Max_03 "Я это... опешил от твоего вида!"
    Alice_05 "Что, так страшно?"
    Max_02 "Нет, что ты! Ты очень классно выглядишь - такая сексуальная!"
    Alice_07 "Вообще-то, ты с сестрой разговариваешь, если что... Но мне приятно такое слышать."
    Max_04 "И сидит он на тебе отпадно!"
    if mgg.dress == 'b':
        # Макс в майке и шортах
        Alice_03 "Ну конечно... всё только благодаря тебе. Проходи... Снимай майку, она будет только мешаться... Присаживайся на стул, у меня для тебя есть кое-что интересное."
    else:
        Alice_03 "Ну конечно... всё только благодаря тебе. Проходи... Присаживайся на стул, у меня для тебя есть кое-что интересное."
    Max_05 "Серьёзно?! Ну хорошо..."

    # domin-01 + domin-01-max-01b-alice-01
    scene BG char Alice domin 01
    show Alice domin 01-01c
    Alice_05 "А чтобы это стало ещё более интересным для тебя, я привяжу тебя к стулу..."
    Max_07 "Э-э-э... Но только, если так мне действительно будет ещё интереснее."
    Alice_02 "Ну как, не туго?"
    Max_01 "Нет, всё нормально. Продолжай..."
    Alice_06 "Макс, я же вижу, что ты пялишься на мой зад... Оу! Я так же вижу, что твой восторг уже не умещается в шортах... Тебе как, не стыдно вообще?"
    Max_02 "Немного... Но по большей части, твоя блестящая попка вызывает во мне много пошлых фантазий!"
    Alice_14 "Ты совершенно испорченный мальчишка и я вынуждена познакомить тебя с ещё одним предметом моего гардероба!"
    Max_03 "О да! Интересно, с каким же..."

    # domin-02 + domin-02-max-01b-alice-01
    scene BG char Alice domin 02
    show Alice domin 02-01c
    Alice_05 "Да вот с этим, Макс... Ну что, узнаёшь его?"
    Max_08 "Эй... Потише, это тебе не игрушки!"
    Alice_03 "Хм... А ты думал, что тебя здесь будут ожидать игрушки?! После того, как ты всё так же, как и раньше, продолжаешь подглядывать за мной?"
    Max_10 "Эй... Ты чего? Я могу ещё раз извиниться..."

    # domin-03 + domin-03-max-01b-alice-01
    scene BG char Alice domin 03
    show Alice domin 03-01c
    Alice_05 "А с чего ты взял, что это поможет? Нет, благодаря этому ты конечно не сразу оказываешься у мамы на коленях, но... мне этого мало, Макс... Я хочу, чтобы оказавшись у ванной комнаты, ты начал задумываться, а стоит ли оно того!"
    Max_07 "Знаешь, очень сложно удержаться и не..."
    Alice_12 "Это не важно, Макс! Раз за разом, ты говоришь, что это случайность или больше не будешь подглядывать за мной, и... это снова повторяется!"
    Max_10 "Я просто..."

    # domin-04 + domin-04-max-01b-alice-01
    scene BG char Alice domin 04
    show Alice domin 04-01c
    Alice_16 "Не перебивай меня, Макс! Я ведь могу использовать этот стек по его назначению... Хочешь?"
    Max_13 "Нет-нет... Извини."
    Alice_12 "Так вот, если ты действительно мужчина, а твоя торчащая штуковина говорит именно об этом, будь добр, перестань говорить, что ты случайно увидел, как я принимаю душ и не подглядывай за мной! Ты меня понял?"
    Max_14 "Д-да... Я понял..."
    Alice_05 "Хороший мальчик. Но если продолжишь, то вы с этим стеком станете очень близки. Особенно близки вы станете в районе твоей голой задницы, по которой я буду хлестать так, что ты будешь молить меня отпустить тебя к маме!"
    Max_10 "Понял."

    # domin-01 + domin-01-max-01b-alice-01
    scene BG char Alice domin 01
    show Alice domin 01-01c
    Alice_02 "Умница... Теперь можешь идти. Сейчас развяжу..."
    Max_08 "Ага..."
    Alice_15 "Ты что, бессмертным себя считаешь что ли?! Снова пялишься?"
    Max_10 "Нет. Просто задумался."
    menu:
        Alice_01 "Вот и правильно!"
        "{i}уйти{/i}":
            pass

    # aliceroomdoor-04-night
    scene location house aliceroom door-night
    Max_09 "{m}Странный вечерок получился! С одной стороны, Алиса хотела мне пригрозить и напугать... Но с другой, а зачем так сексуально наряжаться передо мной было для этого? Может, проверяет меня?!{/m}"
    Max_07 "{m}Хорошо, что есть способ проверить, что у неё действительно на уме. Нужно продолжить за ней подглядывать, а когда она снова меня заметит, как-то умудриться уговорить её на конфету с ликёром перед этим... наказанием...{/m}"

    $ renpy.end_replay()
    $ alice.dcv.mistress.stage = 1
    $ alice.dcv.mistress.disable()
    $ alice.daily.mistress = 1
    $ poss['risk'].open(16)
    $ spent_time += 40
    $ current_room = house[0]
    jump Waiting


label alice_mistress_1:

    call alice_tv_closer from _call_alice_tv_closer_2

    Alice_12 "Ты что, Макс, забыл, что одних \"извини\" мне мало? Думаю, нам стоит подняться ко мне в комнату и побеседовать там в... особой обстановке..."
    Max_08 "Это точно необходимо?"
    Alice_05 "Ты что, боишься?! Ха-ха..."
    Max_07 "Нет, просто я думал, что мы сможем решить это как-то без всего, что было в прошлый раз..."
    menu:
        Alice_16 "Тебе сейчас не думать нужно, а просто делать то, что я хочу. Пошли ко мне в комнату..."
        "{i}идти за Алисой{/i}":
            pass

    # aliceroomdoor-04-night
    scene location house aliceroom door-night
    Max_09 "{m}Надеюсь, всё обойдётся привязыванием и угрозами, как в прошлый раз. И зачем я ей этот стек купил?!{/m}"
    menu:
        Alice "{b}Алиса:{/b} Макс, заходи!"
        "{i}войти в комнату{/i}":
            pass

    # alice-blog-evening-01 + domin-00-max-(01a/01b) + domin-00-alice-01
    scene BG char Alice evening
    $ renpy.show('Max domin 00'+mgg.dress)
    show Alice domin 00
    Alice_02 "Ну же, Макс, не тормози, проходи! Или снова наслаждаешься видом!"
    Max_03 "Ага... Ты очень красивая!"
    if mgg.dress == 'b':
        # Макс в майке и шортах
        Alice_05 "Спасибо! Но комплименты не спасут тебя от того, что я хочу сделать. Снимай майку и присаживайся на стул." nointeract
    else:
        Alice_05 "Спасибо! Но комплименты не спасут тебя от того, что я хочу сделать. Присаживайся на стул." nointeract
    menu:
        "Конфетка, я полагаю, тоже не спасёт. Но я всё равно предложу...":
            pass
    Alice_16 "На стул, Макс. Живо!"
    Max_14 "Понял, сажусь..."

    # domin-01 + domin-01-max-01b-alice-01
    scene BG char Alice domin 01
    show Alice domin 01-01c
    Alice_03 "Ну как, не туго я тебя привязала?"
    Max_09 "Вообще-то, немного жмёт."
    Alice_05 "Это ничего, тем более, что ты, как я вижу, снова блещешь своими причиндалами. Тебе что, так нравится, когда тебя связывают, фетишист мелкий?"
    Max_02 "Просто наряд твой очень нравится..."

    # domin-02 + domin-02-max-01b-alice-01
    scene BG char Alice domin 02
    show Alice domin 02-01c
    Alice_12 "Ах... Ты, видимо, считаешь, что всё это шутки. Тебе было так же весело стоять за углом и глазеть, как я моюсь? Это очень по-мужски! Подглядывать за собственной сестрой! Хм... Может быть, тебе всё-таки всыпать?!"
    Max_08 "Эй, потише с этой штукой! Ты чего?"
    Alice_16 "А ничего! Наверняка ты стоял, смотрел на меня и представлял, как зайдёшь в душ и жёстко оттрахаешь меня?!"
    Max_10 "Ну... Оно само так получается думать..."

    # domin-03 + domin-03-max-01b-alice-01
    scene BG char Alice domin 03
    show Alice domin 03-01c
    Alice_15 "Ах вот так! Само получается?! У меня начинает складываться впечатление, что моя \"запугивающая терапия\" не даст результатов с таким извращугой, как ты."
    Max_15 "Тогда прекращай размахивать этой плёткой... Давай, развяжи меня!"

    # domin-01 + domin-01-max-02b-alice-02
    scene BG char Alice domin 01
    show Alice domin 01-02c
    Alice_17 "Что, не нравится? Мне тоже не нравится, что ты постоянно за мной подглядываешь! Знаешь, Макс... Я могла бы, например, дать тебе этим стеком по яйцам. Ну так... чтобы до тебя лучше дошло! Но я поступлю иначе..."
    Max_09 "Да?! И как же, интересно?"

    # domin-04 + domin-04-max-01b-alice-01
    scene BG char Alice domin 04
    show Alice domin 04-01c
    Alice_05 "А очень просто! Я буду высекать эту твою мерзкую привычку подглядывать за мной. Прямо этим стеком и прямо по твоей заднице. И сила, с которой я это буду делать, будет зависеть от того, насколько покладисто ты этому подчинишься."
    Max_15 "Эй! Может мне ещё и самому себя отхлестать, прямо на твоих глазах?!"

    # domin-03 + domin-03-max-01b-alice-01
    scene BG char Alice domin 03
    show Alice domin 03-01c
    Alice_07 "Ох, я бы с удовольствием на это посмотрела, но стек я тебе не доверю. Всё будет в моей власти. Но ты всегда можешь выбрать наказание от мамы перед всеми нами."
    Max_14 "Какие классные у меня варианты! Один лучше другого."
    Alice_16 "В общем, я предупредила тебя в последний раз. Дальше всё зависит от тебя. Увижу, что подглядываешь - накажу или сама, или это будет мама! Понял меня?!"
    Max_11 "Понял-понял..."

    # domin-01 + domin-01-max-01b-alice-01
    scene BG char Alice domin 01
    show Alice domin 01-01c
    menu:
        Alice_12 "Это не шутка, Макс - я тебя предупредила! Всё, вали отсюда."
        "{i}уйти{/i}":
            pass

    $ renpy.end_replay()
    $ alice.dcv.mistress.stage = 2
    $ alice.dcv.mistress.disable()
    $ alice.daily.mistress = 1
    $ poss['risk'].open(17)
    $ spent_time += 40
    $ current_room = house[0]
    jump Waiting


label alice_mistress_2:

    call alice_tv_closer from _call_alice_tv_closer_3

    Alice_02 "Ой, Макс, спасибо, что разрешил... А как ты хочешь, чтобы я это сделала? Понежнее?"
    Max_07 "Желательно, да!"
    menu:
        Alice_05 "Ха-ха... Размечтался! Сперва глазел на меня голую, а теперь пришёл и ещё указываешь, как тебя наказать?! Совсем больной что ли? Идём быстро в мою комнату..."
        "{i}идти за Алисой{/i}":
            pass

    # aliceroomdoor-04-night
    scene location house aliceroom door-night
    Alice "{b}Алиса:{/b} И даже не думай сбегать, потому что я уже почти оделась!"
    Max_09 "Да, конечно. Жду."
    menu:
        Alice "{b}Алиса:{/b} Давай, заходи."
        "{i}войти в комнату{/i}":
            pass

    # alice-blog-evening-01 + domin-00-max-(01a/01b) + domin-00-alice-01
    scene BG char Alice evening
    $ renpy.show('Max domin 00'+mgg.dress)
    show Alice domin 00
    Alice_02 "Ну же, Макс, не тормози, проходи!"
    Max_11 "Опять привязывать будешь?"
    Alice_03 "А вот и не угадал! Раздевайся!"
    Max_08 "В смысле?"
    Alice_07 "В прямом. Ты же смотрел на меня голую, теперь я на тебя посмотрю!"
    Max_09 "Это ещё зачем?"
    Alice_05 "Чтобы побольше неудобства тебе принести... Это такая часть наказания."
    Max_10 "Ну-у... ладно..."

    # blog-desk-01 + aliceroom-punish-00-alice-01 + aliceroom-punish-00-max-01c
    scene BG char Alice blog-desk-01
    show Alice domin pun 00
    show Max domin pun 00
    Alice_03 "Ну вот, теперь ты в том же положении, что и я в ванной комнате. Нравится обстановка?"
    Max_09 "Вообще-то не очень..."
    Alice_05 "Вот именно так я чувствую себя, когда ты за мной смотришь! А теперь живо поворачивайся к столу и подставляй задницу!"
    Max_13 "Ты что, меня серьёзно накажешь? Прямо плёткой?!"

    # aliceroom-punish-01 + aliceroom-punish-01-alice-01 + aliceroom-punish-01-max-02c
    scene BG char Alice domin pun 01
    show Alice domin pun 01
    show Max domin pun 02
    menu:
        Alice_12 "Да, Макс, серьёзно! И если помнишь, я говорила в прошлый раз от чего будет зависеть сила, с которой я буду это делать... Так как? Есть желание меня злить или ты будешь послушным мальчиком?"
        "Давай уже быстрее с этим покончим...":
            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-01d + звук шлепка
            show Alice domin pun 02
            show Max domin pun 01a
            play sound slap1
            Max_12 "Ай!!! Бо-о-ольно... С ума сошла что ли так бить?!"
            menu:
                Alice_16 "Запомни, глупый мальчишка, мы здесь не для того, чтобы побыстрее со всем разобраться, а чтобы ты прочувствовал, что подглядывать не хорошо! Живо руки на стол!"
                "{i}подчиниться{/i}":
                    jump .submit
                "Да пошла ты!":
                    jump .fuck_you
        "Ты же понимаешь, что я могу всыпать по твоей заднице в ответ?":
            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-01d + звук шлепка
            show Alice domin pun 02
            show Max domin pun 01a
            play sound slap1
            Max_12 "Ай!!! Бо-о-ольно... С ума сошла что ли так бить?!"
            menu:
                Alice_16 "Ну как? Ты прочувствовал, что мне лучше не угрожать и не подглядывать за мной?! Живо руки на стол!"
                "{i}подчиниться{/i}":
                    jump .submit
                "Да пошла ты!":
                    jump .fuck_you

    label .submit:
        # aliceroom-punish-01 + aliceroom-punish-01-alice-01 + aliceroom-punish-01-max-02d + звук шлепка
        show Alice domin pun 01
        show Max domin pun 02a
        play sound slap1
        Max_14 "Ай! Ай... Всё, я всё понял..."
        Alice_05 "Точно? Может добавки?"
        Max_10 "Не надо! Я всё прочувствовал..."

        # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-03d
        show Alice domin pun 02
        show Max domin pun 03a
        Alice_07 "Ну, раз так, можешь идти. Да, и спасибо ещё раз за то, что подарил мне этот стек. Надеюсь, ты его оценил."
        menu:
            Max_11 "Ага... Оценил..."
            "{i}одеться и уйти{/i}":
                jump .end

    label .fuck_you:
        # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-01e + звук шлепка
        show Alice domin pun 02
        show Max domin pun 01b
        play sound slap1
        Alice_15 "Что?! Ничего себе, как ты заговорил! Ну держись..."

        # звук шлепка
        play sound slap1
        Max_13 "Чёрт!!! Алиса, бо-о-ольно... Я всё понял!"

        # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-03e
        show Alice domin pun 02
        show Max domin pun 03b
        Alice_05 "Точно? Может добавки?"
        Max_10 "Нет-нет, я всё прочувствовал! Достаточно!"
        Alice_07 "Ну ладно, сделаю вид, что я поверила. Вали отсюда. Да, и спасибо ещё раз за твой великолепный подарок. Надеюсь, он тебе понравился?"
        menu:
            Max_11 "Ага... Очень..."
            "{i}одеться и уйти{/i}":
                jump .end

    label .end:
        $ renpy.end_replay()
        $ alice.dcv.mistress.stage = 3
        $ alice.dcv.mistress.disable()
        $ alice.daily.mistress = 1
        $ poss['risk'].open(18)
        $ spent_time += 40
        $ current_room = house[0]
        jump Waiting


label alice_mistress_3:

    # $ renpy.dynamic('ch')
    call alice_tv_closer from _call_alice_tv_closer_4

    menu:
        Alice_02 "Я рада, что ты сделал такой выбор. Это справедливо, когда жертве вопиющего вуайеризма даётся возможность расквитаться с обидчиком!"
        "Конфетку? Она ни к чему не обязывает. Просто признание моей испорченности..." ('soc', mgg.social, 90) if kol_choco or _in_replay:
            if rand_result:
                Alice_05 "[succes!t]Звучит вроде искренне... Хорошо, твоё признание я принимаю. Но учти, наказание от этого добрее не станет!"
                Max_01 "Конечно..."
                $ give_choco()
                $ alice.daily.drink = 1
                menu:
                    Alice_08 "Ммм... Люблю эти конфетки! Пошли за мной!"
                    "{i}идти за Алисой{/i}":
                        jump .follow
            else:
                Alice_06 "[failed!t]А мне вот чувствуется, что это просто способ меня задобрить... Так что нет. Спасибо, но я обойдусь."
                Max_07 "Ну и зря, я хотел, как лучше."
        "То же мне, преступника нашла..." if not _in_replay:
            pass

    menu:
        Alice_05 "За каждым преступлением должно следовать наказание! Так что не будем медлить. Пойдём ко мне в комнату..."
        "Хотя, знаешь... Я передумал. Лучше уж от мамы получить..." if not _in_replay:
            Alice_03 "Да? Вот обидно... Ну ладно, это твой выбор... В любом случае, когда тебя будут наказывать, на моём лице будет очень довольная улыбка."
            menu:
                Max_09 "Да мне всё-равно..."
                "{i}уйти{/i}":
                    $ alice.daily.mistress = 1
                    $ spent_time += 40
                    $ current_room = house[0]
                    jump Waiting
        "{i}идти за Алисой{/i}":
            jump .follow

    label .follow:
        # aliceroomdoor-04-night
        scene location house aliceroom door-night

    Alice "{b}Алиса:{/b} И даже не думай сбегать, потому что я уже почти оделась!"
    Max_09 "Да, конечно. Жду."
    menu:
        Alice "{b}Алиса:{/b} Давай, заходи."
        "{i}войти в комнату{/i}":
            pass

    # alice-blog-evening-01 + domin-00-max-(01a/01b) + domin-00-alice-01
    scene BG char Alice evening
    $ renpy.show('Max domin 00'+mgg.dress)
    show Alice domin 00
    if alice.daily.drink:
        # у Макса получилось дать Алисе конфету с ликёром
        jump alice_domine_drink

    # конфету Алисе дать не получилось
    menu:
        Alice_02 "Ну же, Макс, не тормози. Хватит на меня так пялиться и проходи! Раздевайся давай..."
        "{i}снять одежду{/i}":
            jump .domine_no_drink

    label .domine_no_drink:
        # blog-desk-01 + aliceroom-punish-00-alice-01 + aliceroom-punish-00-max-01c
        scene BG char Alice blog-desk-01
        show Alice domin pun 00
        show Max domin pun 00

    menu:
        Alice_05 "Ну и чего стоишь? Ты же знаешь, что делать! Не заставляй меня ждать... Хуже ведь будет тебе!"
        "{i}подчиниться{/i}":
            # aliceroom-punish-01 + aliceroom-punish-01-alice-01 + aliceroom-punish-01-max-02c
            scene BG char Alice domin pun 01
            show Alice domin pun 01
            show Max domin pun 02
            menu:
                Alice_03 "Хороший мальчик. Что теперь нужно сказать?"
                "Накажи меня! Я это заслужил...":
                    # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-02d + звук шлепка
                    show Alice domin pun 02
                    show Max domin pun 02a
                    play sound slap1
                    menu:
                        Alice_04 "Ох, как же моим ушам приятно слышать такое... Это ведь искреннее твоё желание?"
                        "Да, я виноват и меня нужно наказать!":
                            # aliceroom-punish-01 + aliceroom-punish-01-alice-01 + aliceroom-punish-01-max-02e + звук шлепка
                            show Alice domin pun 01
                            show Max domin pun 02b
                            play sound slap1
                            Alice_05 "Ой, когда меня так об этом просят, я не могу отказать... Может, ещё разок для закрепления, чтобы лучше прочувствовать, что подглядывать не хорошо?"
                            Max_10 "Не надо! Я всё прочувствовал..."

                            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-03d
                            show Alice domin pun 02
                            show Max domin pun 03a
                            menu:
                                Alice_07 "Ну, раз так, можешь идти. Я на самом деле сильно сомневаюсь, что до тебя дошло. Но всё же понадеюсь..."
                                "{i}одеться и уйти{/i}":
                                    jump .end
                        "Давай уже быстрее, тебя ждём...":
                            #как при варианте "Ничего. Подождёшь, не развалишься..."
                            pass
                "Давай уже быстрее, тебя ждём...":
                    #как при варианте "Ничего. Подождёшь, не развалишься..."
                    pass
        "Ничего. Подождёшь, не развалишься...":
            pass

    # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-01d + звук шлепка
    scene BG char Alice domin pun 01
    show Alice domin pun 02
    show Max domin pun 01a
    play sound slap1
    Max_12 "Ай!!! Бо-о-ольно... С ума сошла что ли так бить?!"
    menu:
        Alice_16 "Вот так ты значит хочешь? Дерзить мне будешь... Ну, смотри... Если не поставишь руки на стол и не отклячишь свою задницу, добавки будет столько, что ноги откажут!"
        "{i}подчиниться{/i}":
            # aliceroom-punish-01 + aliceroom-punish-01-alice-01 + aliceroom-punish-01-max-02d + звук шлепка
            show Alice domin pun 01
            show Max domin pun 02a
            play sound slap1
            Alice_04 "Хороший мальчик. Сейчас ты у меня прочувствуешь, что подглядывать не хорошо! Как тебе?"
            Max_14 "Больно... Может уже хватит?"
            Alice_05 "Правда? Хмм... Что-то как-то быстро до тебя дошло... Давай ещё раз, для закрепления..."

            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-02e + звук шлепка
            show Alice domin pun 02
            show Max domin pun 02b
            play sound slap1
            Max_13 "Ай! Я всё прочувствовал... Прекращай!"
            Alice_03 "Ну как, понравилось? Я надеюсь, сейчас ты всё понял?"

            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-03e
            show Alice domin pun 02
            show Max domin pun 03b
            Max_10 "Да, я понял, что подглядывать не хорошо..."
            menu:
                Alice_07 "Ну, а раз понял, можешь идти. Я на самом деле сильно сомневаюсь, что до тебя дошло. Но всё же понадеюсь..."
                "{i}одеться и уйти{/i}":
                    $ infl[alice].sub_m(3)
                    jump .end

        "Вертел я тебя знаешь на чём?!":
            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-01e + звук шлепка
            show Alice domin pun 02
            show Max domin pun 01b
            play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop
            Alice_15 "Что?! Ничего себе, как ты заговорил! Ну держись..."

            # звук шлепка
            play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop
            Max_13 "Чёрт!!! Алиса, бо-о-ольно... Хватит!"

            stop sound
            # aliceroom-punish-01 + aliceroom-punish-01-alice-02 + aliceroom-punish-01-max-03e
            show Alice domin pun 02
            show Max domin pun 03b
            Alice_05 "Точно? Может добавки? Хотя вижу, что и правда хватит, а то вот-вот чувствую - заплачешь. Или всё-таки..."
            Max_10 "Нет-нет, я усвоил, что подглядывать не хорошо! Достаточно!"
            menu:
                Alice_07 "Ну ладно, сделаю вид, что я поверила. Вали отсюда. Надеюсь, ты и правда что-то усвоил."
                "{i}одеться и уйти{/i}":
                    $ infl[alice].sub_m(6)
                    jump .end

    label .end:
        $ renpy.end_replay()
        $ alice.dcv.mistress.disable()
        $ alice.daily.mistress = 1
        $ spent_time += 40
        $ current_room = house[0]
        jump Waiting

label alice_domine_drink:
    Alice_02 "Ну же, Макс, не тормози. Хватит на меня так пялиться и проходи! Раздевайся давай..."
    Max_07 "А может без этого? Может, лучше привяжешь меня к стулу и уже там как-нибудь накажешь?"
    menu:
        Alice_05 "Неужели такому мелкому извращенцу, как ты, стало страшно поворачиваться ко мне задом? Это хорошо... Но раздеться тебе придётся всё равно! Или есть возражения?!"
        "{i}снять одежду{/i}":
            pass

    # domin-01 + domin-01-max-01c-alice-01
    scene BG char Alice domin 01
    show Alice domin 01-01d
    Alice_12 "Хм... А я смотрю, Макс, тебе нравится то, что я делаю. Задницу подставлять боишься, а вот демонстрировать, насколько ты \"большой\" извращенец и близко не стесняешься!"
    Max_04 "А чего стесняться? Это естественно, что у парня стоит на такую сексуальную девушку... Да ещё и в таком костюмчике..."
    Alice_16 "Ах, вот так, да?! Вообще-то, тебя должен настораживать мой внешний вид!"
    Max_03 "А меня заводит! С огромной радостью бы залез руками под этот костюмчик, да вот только они связаны..."

    # domin-01 + domin-01-max-03c-alice-03
    show Alice domin 01-03d
    Alice_17 "Вот ты наглец, Макс! Думаешь, это шуточки такие и я тебя связала ради развлечений?"
    Max_07 "Нет... Просто у меня не получается по другому реагировать на тебя!"
    Alice_05 "Ох... Это так мило... У моего младшего брата-извращенца на меня стоит. Должно быть это так мучительно, просто смотреть и мечтать обо мне!"
    Max_10 "А то! Очень мучительно..."
    Alice_03 "Ха! В таком случае, теперь я знаю, как тебя нужно наказывать... Как тебе это!"

    # domin-05 + domin-05-max-01c-alice-01
    scene BG char Alice domin 05
    show Alice domin 05-01d
    Max_05 "Ого! Эти офигенные сисечки всегда радуют мои глаза!"
    Alice_06 "Ну ещё бы! Ты же наверняка их уже наизусть запомнил, пока подглядывал за мной в душе... Ведь я ловила тебя на этом так много раз, что даже страшно представить, сколько раз ты подглядывал за мной, пока я не видела!"
    Max_02 "Я бы сказал, соотношение примерно 50 на 50. Около того..."
    menu:
        Alice_13 "Ну и что ты там, подглядывая в душе, мечтал со мной сделать, а Макс?! Признавайся!"
        "Как-то мне страшно это озвучивать..." if not _in_replay:
            #domin-02 + domin-02-max-02c-alice-02
            scene BG char Alice domin 02
            show Alice domin 02-02d
            Alice_05 "И правильно! Твои похотливые мысли и фантазии обо мне должны таковыми и оставаться. Но это полбеды! В добавок к этому, что ты ещё должен?"
            Max_10 "Ай! Моё ухо! Наверно... не подглядывать за тобой..."
            jump .afraid_to_say

        "Для начала, я бы полюбовался твоими прелестями поближе!" if _in_replay or poss['risk'].used(19):
            # domin-07 + domin-07-max-01c-alice-01
            scene BG char Alice domin 07
            show Alice domin 07-01d
            Alice_05 "Поближе, значит... Настолько ближе? Или ты хотел бы быть ещё ближе к моей груди?!"
            Max_05 "О да! Я бы хотел ещё ближе!"
            menu:
                Alice_07 "Какая жалость! Похоже, кто-то привязан к стулу и не может быть так близко ко мне, как ему хотелось... Должно быть, обидно?"
                "А ты меня развяжи и мы это исправим..." if not _in_replay:
                    # domin-04 + domin-04-max-02c-alice-02
                    scene BG char Alice domin 04
                    show Alice domin 04-02d
                    Alice_16 "Вот ещё! Такое мог попросить только очень плохой мальчик, который совершенно не понимает, как себя надо вести со своей госпожой!"
                    Max_08 "А как надо?"

                    # domin-01 + domin-01-max-01c-alice-01
                    scene BG char Alice domin 01
                    show Alice domin 01-01d
                    Alice_12 "Услужливо! Если ты ещё до сих пор это не усвоил, то я просто обязана тебя наказать... Как ты того и заслужил!"
                    Max_10 "Эй! В смысле плёткой что ли?!"
                    jump alice_mistress_3.domine_no_drink

                "Раз я привязан, то на меня можно очень удобно присесть...":
                    if alice.flags.hip_mass < 5:
                        # Макс ещё не прошёл "трезвый" фут-джоб
                        Alice_04 "Ох, я ценю такую услужливость, но твои похотливые мысли и фантазии обо мне должны таковыми и оставаться. В добавок к этому, что ты ещё должен?"
                        Max_07 "Наверно... не подглядывать за тобой..."
                        jump .afraid_to_say

                    else:
                        # domin-07 + domin-07-max-02c-alice-02
                        scene BG char Alice domin 07
                        show Alice domin 07-02d
                        Alice_03 "И правда! Ах, как приятно порой бывает сесть и расслабиться... Приятно, что ты не просто извращенец, а галантный извращенец!"
                        Max_04 "Таким стройным и красивым ножкам надо давать отдых."
                        Alice_08 "Ну а моя грудь... Не поверю, что ты хотел только любоваться!"
                        Max_02 "Не только! Я и без рук могу дарить приятные ощущения..."

                        # domin-01 + domin-01-max-04c-alice-04
                        scene BG char Alice domin 01
                        show Alice domin 01-04d
                        menu:
                            Alice_07 "Смотри, Макс! Я не хочу разочаровываться... Ах-х! Это хорошо... Но если мне хоть что-то не понравится, то я..."
                            "{i}ласкать её грудь языком{/i}" ('sex', mgg.sex * 3, 90): #(сексуальный опыт)
                                jump .caressing_tongue
                            "{i}ласкать её грудь губами{/i}" ('sex', mgg.sex * 3, 90): #(сексуальный опыт)
                                jump .caressing_lips

    label .afraid_to_say:
        # domin-06 + domin-06-max-01c-alice-01
        scene BG char Alice domin 06
        show Alice domin 06-01d
        Alice_03 "А твоя штуковина, похоже, всё ещё считает иначе, как и ты! Или всё из-за того, что я глажу по нему своей плёткой? Учти, я могу сделать то, для чего она предназначена!"
        Max_08 "Э-э-э... Может, не надо этого?"
        Alice_07 "А может, наоборот, надо? Как думаешь, если я шлёпну по нему, то твоё возбуждение в миг исчезнет?"
        Max_14 "Уверен, всё дело именно в том, что ты гладишь его!"

        # domin-04 + domin-04-max-02c-alice-02
        scene BG char Alice domin 04
        show Alice domin 04-02d
        Alice_05 "Тогда я, пожалуй, это прекращу и в следующий раз, если таковой будет, уже не буду такой... деликатной... Или ты хочешь уже сейчас пожёстче?!"
        Max_13 "Нет-нет, не надо! Я этого не хочу!"
        Alice_03 "Ха-ха... Боишься? Это хорошо... Так и должно быть, ты должен меня бояться!"
        Alice_05 "В общем, я предупредила тебя в последний раз. Дальше всё зависит от тебя. Увижу, что подглядываешь - накажу или сама, или это будет мама! Понял меня?!"
        Max_11 "Понял-понял..."

        # domin-01 + domin-01-max-01c-alice-01
        scene BG char Alice domin 01
        show Alice domin 01-01d
        menu:
            Alice_12 "Это не шутка, Макс - я тебя предупредила! Всё, вали отсюда."
            "{i}уйти{/i}":
                if not _in_replay:
                    $ poss['risk'].open(19)
                jump .end

    label .caressing_tongue:
        if rand_result:
            # (Ей нравится!)
            # domin-03 + domin-03-max-02c-alice-02
            scene BG char Alice domin 03
            show Alice domin 03-02d
            menu:
                Alice_09 "[like!t]Ахх, Макс! Ты так приятно и нежно ласкаешь языком мои сосочки... Ммм... Я чувствую, твой дружок стал твёрже! Меня это очень возбуждает! Д-а-а..."
                "{i}продолжить ласкать{/i}":
                    pass

            #domin-08 + domin-08-max-01c-alice-01
            scene BG char Alice domin 08
            show Alice domin 08-01d
            menu:
                Alice_08 "Охх... Да, Макс, ещё! Ммм... Хорошо... Не знаю где ты научился это делать, но получается у тебя... Ах-х-х... Превосходно! Ты, наверно, и целуешься так же хорошо?"
                "{i}целоваться с Алисой{/i}":
                    jump .kiss
        else:
            # (Ей не нравится!)
            # domin-07 + domin-07-max-01c-alice-01
            scene BG char Alice domin 07
            show Alice domin 07-01d
            Alice_16 "[dont_like!t]Ай! Ты слишком грубо это делаешь! Я люблю грубость, но не до такой же степени... Такое мог сделать только очень плохой мальчик, который совершенно не знает, как надо ублажать свою госпожу!"
            jump .how_should

    label .caressing_lips:
        if rand_result:
            # (Ей нравится!)
            # domin-08 + domin-08-max-01c-alice-01
            scene BG char Alice domin 08
            show Alice domin 08-01d
            menu:
                Alice_09 "[like!t]Ахх, Макс! Ты так приятно и нежно посасываешь мои сосочки... Ммм... Я чувствую, твой дружок стал твёрже! Меня это очень возбуждает! Д-а-а..."
                "{i}продолжить ласкать{/i}":
                    pass

            # domin-03 + domin-03-max-02c-alice-02
            scene BG char Alice domin 03
            show Alice domin 03-02d
            menu:
                Alice_08 "Охх... Да, Макс, ещё! Ммм... Хорошо... Не знаю где ты научился это делать, но получается у тебя... Ах-х-х... Превосходно! Ты, наверно, и целуешься так же хорошо?"
                "{i}целоваться с Алисой{/i}":
                    jump .kiss
        else:
            # (Ей не нравится!)
            # domin-07 + domin-07-max-01c-alice-01
            scene BG char Alice domin 07
            show Alice domin 07-01d
            Alice_16 "[dont_like!t]Ай! Ты слишком грубо это делаешь! Я люблю грубость, но не до такой же степени... Такое мог сделать только очень плохой мальчик, который совершенно не знает, как надо ублажать свою госпожу!"
            jump .how_should

    label .kiss:
        # domin-08 + domin-08-max-02c-alice-02
        scene BG char Alice domin 08
        show Alice domin 08-02d
        menu:
            Max_20 "{m}Надеюсь, моего опыта поцелуев хватит, чтобы Алиса приятно удивилась... Она так страстно целуется и трётся о мой член, что вполне могла бы в порыве страсти взять и отсосать мне! Это было бы круто!{/m}"
            "{i}пытаться впечатлить{/i}" ('kiss', mgg.kissing * 5, 90): #(навык поцелуев)
                if not _in_replay:
                    $ poss['risk'].open(20)

        if rand_result:
            # (Ей нравится!)
            # domin-01 + domin-01-max-05c-alice-05
            scene BG char Alice domin 01
            show Alice domin 01-05d
            Max_19 "[like!t]{m}Эх, если бы мои руки не были привязаны к стулу, мне бы не пришлось так стараться и мои прикосновения завели её ещё сильнее. Но судя по тому, как сладко наши язычки играют с друг другом, у меня всё получается и так!{/m}"

            # domin-06 + domin-06-max-02c-alice-02
            scene BG char Alice domin 06
            show Alice domin 06-02d
            Alice_06 "Всё, Макс, я больше не могу! Эти шортики не должны мешать тому, что я хочу от тебя получить..."
            Max_03 "Оу... И что же это?"
            Alice_08 "Ни слова, Макс! Это должно остаться нашей тайной, ведь брат с сестрой не должны таким заниматься... Но я {b}ХОЧУ{/b}!"

            # domin-07 + domin-07-max-03c-alice-03
            scene BG char Alice domin 07
            show Alice domin 07-03d
            Alice_09 "Ахх... Так намного лучше... Ммм... Он такой твёрдый и горячий! Я совсем сошла с ума, раз делаю такое... Ох, как же хорошо!"
            Max_20 "Ухх... Это точно! Но почему бы не посходить с ума, если об этом никто не узнает?"
            Alice_11 "Вот именно! Д-а-а... Я хочу скользить киской по твоему мощному члену до тех пор, пока не кончу! Как приятно... Держись, Макс, ведь я буду это делать это всё быстрее и быстрее... Ах-х-х..."

            # domin-08 + (domin-08-max-03c-alice-03 или domin-08-max-04c-alice-04)
            scene BG char Alice domin 08
            if random_outcome(50):
                show Alice domin 08-03d
            else:
                show Alice domin 08-04d
            menu:
                Max_19 "{m}Да я этому только рад, сестрёнка! Как бы мне не кончить от её стонов и жарких поцелуев... Так можно ей всё удовольствие обломать, а после схлопотать вдогонку по заднице её стеком! Мне лучше и правда держаться, но как же это непросто...{/m}"
                "{i}дать Алисе кончить{/i}":
                    if random_outcome(50):
                        # domin-01 + domin-01-max-06c-alice-06
                        scene BG char Alice domin 01
                        show Alice domin 01-06d
                    else:
                        # domin-08 + domin-08-max-05c-alice-05
                        show Alice domin 08-05d
                    Alice_10 "Ох, Божечки! Макс! Я сейчас кончу... Д-а-а... Ммм... Ещё немножко и... Ах! Да-а-а... Как же это было классно! Ох..."
                    Max_05 "Вау, Алиса! Хорошо порезвилась?"
                    Alice_06 "Фух... Это было нечто... Макс... Я не совсем ЭТО планировала! Но..."
                    Max_02 "Но, может ты поможешь мне с кое-чем?"

                    # domin-05 + domin-05-max-02c-alice-02
                    scene BG char Alice domin 05
                    show Alice domin 05-02d
                    Alice_05 "Ладно я, но вот ты точно не должен забывать, Макс, что мы тут делаем! Наказываем тебя!"
                    Max_10 "Ну Алиса! Так нельзя..."
                    Alice_13 "Что нельзя, так это подглядывать за мной! Но знаешь, кое-чем я тебе всё же помогу..."
                    Max_07 "Правда?!"

                    # domin-01 + domin-01-max-01c-alice-01a
                    scene BG char Alice domin 01
                    show Alice domin 01-01da
                    menu:
                        Alice_05 "Отвяжу тебя от стула и ты сможешь уйти без какого-либо вреда для здоровья. А в остальном помоги себе сам! Всё, вали отсюда."
                        "{i}уйти{/i}":
                            jump .end
        else:
            # (Ей не нравится!)
            # domin-07 + domin-07-max-01c-alice-01
            scene BG char Alice domin 07
            show Alice domin 07-01d
            Alice_16 "[dont_like!t]Макс! С чего ты взял, что мне понравится, если ты так грубо будешь напирать своим языком?! Такое мог сделать только очень плохой мальчик, который совершенно не знает, как надо себя вести со своей госпожой!"
            jump .how_should

    label .how_should:
        Max_08 "А как надо?"

        # domin-01 + domin-01-max-01c-alice-01
        scene BG char Alice domin 01
        show Alice domin 01-01d
        Alice_12 "Приятно и нежно! Если ты так не умеешь, то я просто обязана тебя наказать... Как ты того и заслужил!"
        Max_10 "Эй! В смысле плёткой что ли?!"
        jump alice_mistress_3.domine_no_drink

    label .end:
        $ renpy.end_replay()
    $ alice.dcv.mistress.disable()
    $ alice.daily.mistress = 1
    $ spent_time += 40
    $ current_room = house[5]
    jump Waiting


label alice_help_carry_plates:
    # на ближнем фоне с готовкой Алисы
    # "Тебе помочь накрыть на стол?"
    # call alice_cooking_closer
    # $ renpy.dynamic('r1')

    if alice.flags.help:
        Alice_07 "На это я, на самом деле, и надеялась. Пара лишних рук мне точно не помешает... Пока я здесь со всем закончу и наведу порядок, ты можешь отнести тарелки с едой на веранду." nointeract
    else:
        Alice_07 "Помочь?! Чего это ты, Макс, такой добрый? Хотя, пара лишних рук мне точно не помешает... Пока я здесь со всем закончу и наведу порядок, ты можешь отнести тарелки с едой на веранду." nointeract

    menu:
        "Ага, не вопрос. Сделаю.":
            # dinner-covers-00 + dinner-covers-00-max-(01a/01b)
            scene BG char Max dinner-covers-00
            $ renpy.show('Max covers 01'+mgg.dress)
            menu:
                Max_09 "{m}Вот зачем таскать эти тарелки на второй этаж, когда у нас есть прямо здесь, в гостиной, прекрасный большой стол?!{/m}"
                "{i}отнести тарелки на веранду{/i}":
                    # terrace-punish-evening-00 + dinner-covers-00-max-(02a/02b)
                    scene BG punish-evening 00
                    $ renpy.show('Max covers 02'+mgg.dress)

                    # рандом одной из мыслей
                    $ r1 = renpy.random.randint(1, 3)
                    if r1 < 1:
                        Max_07 "{m}Блин! Теперь я хочу съесть не только своё, но и макароны Лизы. Уж слишком аппетитно они выглядят и пахнут...{/m}" nointeract
                    elif r1 < 2:
                        Max_07 "{m}Ну вот! Алиса себе самые большие котлеты положила... Надо будет хотя бы одной, да поменяться.{/m}" nointeract
                    else:
                        Max_07 "{m}А вот это не хорошо! У мамы в тарелке слишком много углеводов. Нужно приглядывать за её фигурой, поэтому отложу немного себе...{/m}" nointeract
                    menu:
                        "{i}приступить к ужину{/i}":
                            pass

                        "{i}подмешать Эрику в тарелку слабительное{/i}" if can_use_laxative():
                            # в инвентаре Макса есть слабительное и можно его подмешать
                            menu:
                                Max_02 "{m}Ну что, Эрик... Удачно тебе посидеть на унитазе. Думаю, тебе будет не скучно...{/m}"
                                "{i}приступить к ужину{/i}":
                                    $ eric.daily.sweets = 1     # применено слабительное
                                    $ flags.trick = True

                        "{i}подмешать Эрику в тарелку успокоительное{/i}" if can_use_sedative():
                            # в инвентаре Макса есть средство от потенции и можно его подмешать
                            menu:
                                Max_03 "{m}Надеюсь, сегодня Эрику никакие потрахушки не светят, благодаря этому средству. Если он сгорит со стыда, я только порадуюсь...{/m}"
                                "{i}приступить к ужину{/i}":
                                    $ eric.daily.sweets = 2     # применено средство от потенции
                                    $ flags.trick = True

            $ AddRelMood('alice', 10, 60, 2)
            $ infl[alice].add_m(12)
            $ spent_time = 60 - int(tm[-2:])
            jump Waiting

        "Нет, лучше давай сама...":
            Alice_16 "Вот ты козлина, Макс!"
            Max_01 "Заодно и попку разомнёшь, а то за своим ноутбуком слишком много сидишь."
            $ AddRelMood('alice', 0, -30)
            $ spent_time += 10
            jump Waiting


label alice_about_wallet:

    Alice_16 "Мне это не интересно, Макс!"
    Max_07 "Э-э-э... Что не интересно?"
    Alice_12 "Всё, с чем бы ты не пришёл. Просто уходи... Или врежу!"
    Max_09 "Ты что, поверила Эрику?!"
    Alice_17 "А ты ещё здесь?!"
    Max_10 "Ладно. Всё понял. Ухожу."

    $ notify_list.append(__("{b}Оповещение:{/b} Алиса больше не хочет взаимодействовать с Максом"))

    $ spent_time = 10
    $ alice.hourly.talkblock = 1
    $ alice.flags.talkblock = 1
    jump Waiting


label smoke_after_wallet:
    if alice.req.result is None:
        Alice_12 "Нечего на меня тут глазеть, Макс! Иди отсюда. Или тебя поджопником ускорить?"
        Max_09 "Ты, конечно, можешь это сделать... Но, знаешь кто вечером узнает, что ты продолжаешь курить?"
        Alice_16 "Не вздумай говорить маме!"
        Max_07 "Запросто! Ты спишь голая, а я молчу. И всем хорошо..."
        Alice_17 "Говнюк ты, Макс! Не знаю, зачем тебе, извращенцу, это нужно, но лучше я соглашусь на этот пустяк... Пока ты что-нибудь ещё не попросил."
        Max_01 "Вот и отлично!"
        menu:
            Alice_13 "А теперь вали отсюда. Дай спокойно покурить!"
            "{i}уйти{/i}":
                $ punalice[0][0] = 8
                $ alice.req.req = "naked"
                $ alice.req.result = "naked"
                $ alice.sleepnaked = True
                $ added_mem_var('alice_sleepnaked')
                $ alice.dcv.prudence.set_lost(7)
    else:
        menu:
            Alice_17 "Тебя выпнуть, Макс, или сам отвалишь?"
            "{i}уйти{/i}":
                $ alice.hourly.talkblock = 1
    $ spent_time += 10
    jump Waiting


label alice_about_showdown:
    # "Как ты после случившегося?"

    if eric.dcv.battle.stage == 1:
        # была подстава через Алису
        Alice_12 "Даже не знаю, как тебе сказать... Узнать, что кто-то приходит ночью и дрочит на тебя - довольно мерзко!"
        Max_07 "Я как раз хотел поговорить с тобой об этом."
        Alice_13 "Макс, ты меня прости, но сейчас я не настроена для разговора по-душам."
        Max_10 "Понимаю. Но ты ведь не злишься за эти снимки?"
        Alice_16 "Во-первых, удали их! А то я там голая... А во-вторых, злюсь. Я так понимаю, ты поэтому уговорил меня спать голой? Чтобы Эрика было на чём подловить..."
        Max_09 "Да, всё верно. Вы же меня не слушали. Вот и приходилось его заманивать к тебе в комнату."
        Alice_06 "А если бы он меня взял и... сделал бы что-нибудь со мной?"
        Max_02 "Так он и сделал. Из-за этого ты ко мне и прибежала."
        Alice_17 "Макс! Ещё раз так пошутишь и я тебе врежу!"
        Max_04 "Да ничего бы он такого дерзкого не сделал. Он же не в конец придурок. К тому же, если бы он распоясался, то я бы вмешался."
        Alice_12 "И Макс, узнаю, что ты фотографируешь меня в душе или когда я сплю... Ты покойник..."
        Max_03 "О! Хорошую мысль ты подкинула, спасибо."
        Alice_17 "Макс, я не шутила!"
        Max_07 "Да ладно тебе. Какая-то ты напряжённая, моих шуток не понимаешь. Давай я тебя отвлеку чем-нибудь? Например, сходим и выберем тебе какое-нибудь нижнее бельё новенькое. Да и фоточки с ним можно будет красивые сделать. Как тебе?"

    else:
        # была подстава через Лизу
        Alice_12 "Даже не знаю, как тебе сказать... Узнать, что Эрик хотел сделать с нашей Лизой - довольно мерзко!"
        Max_07 "Я как раз хотел поговорить с тобой об этом."
        Alice_06 "Ты молодец, Макс, что показал, как мы ошибались в Эрике. Уж не знаю, что бы тут без тебя произошло."

        if flags.eric_photo1:
            # был 1 снимок
            Max_09 "Нууу... Я вот не знаю, показать тебе кое-что или нет."
            Alice_17 "Если ты сейчас высунешь свою пипирку, то я тебе врежу!"
            Max_00 "Не это. Дело в том, что аудиозапись разговора с Эриком, это не всё, что у меня есть. У меня ещё есть фотография, как он дрочит на тебя, пока ты спишь."
            Alice_14 "Макс, ты сейчас серьёзно?!"
            Max_15 "Ага. Я как-то заметил его случайно со двора, ночью. Поближе подобрался и сфотографировал, как он стоит у твоего окна и шишку свою натирает."
            Alice_12 "Фу, Макс! Ты зачем мне это обрисовал. У меня теперь эта картина перед глазами стоит!"
            Max_09 "Посмотреть снимок хочешь?"
            Alice_15 "Нет, конечно, сдурел что ли! Нашёл, что предлагать."

        elif not eric.stat.mast:
            # не было снимков, но видел Эрика на балконе
            Max_09 "Ничего хорошего. Ты знаешь не всё. Я например видел, как Эрик дрочит на тебя, пока ты спишь."
            Alice_14 "Макс, ты сейчас серьёзно?!"
            Max_15 "Ага. Я как-то заметил его случайно со двора, ночью. Хотел сфотографировать, но не успел. Он прямо у твоего окна стоял и шишку свою натирал."
            Alice_12 "Фу, Макс! Ты зачем мне это обрисовал. У меня теперь эта картина перед глазами стоит!"
            Max_09 "Был бы снимок - показал бы."
            Alice_15 "Оно мне надо, такое видеть?! Сдурел что ли!"

        Max_07 "Да ладно тебе. Какая-то ты напряжённая. Давай я тебя отвлеку чем-нибудь? Например, сходим и выберем тебе какое-нибудь нижнее бельё новенькое. Да и фоточки с ним можно будет красивые сделать. Как тебе?"

    Alice_06 "Звучит очень заманчиво, но я пока ещё не готова. Мне нужно время, чтобы отойти от того, что делал Эрик. Фууу..."
    Max_01 "Конечно. Если что, зови."

    $ spent_time = 20
    $ alice.flags.showdown_e = 1
    $ poss['blog'].open(21)
    jump Waiting
