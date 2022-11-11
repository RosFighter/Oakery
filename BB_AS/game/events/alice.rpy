
################################################################################
## события Алисы

label alice_bath:
    scene location house bathroom door-evening
    if alice.daily.bath != 0:
        return

    $ alice.daily.bath = 1
    $ alice.prev_plan = alice.plan_name

    if alice.flags.promise == 'bath':
        # перед дверью в ванную комнату, если Макс выбрал награду у ТВ
        jump ev_v92_020

    menu:
        Max_00 "{m}Если полночь, значит Алиса отмокает в ванне... Входить без стука - опасно для жизни.{/m}"
        "{i}постучаться{/i}":
            menu:
                Alice "{b}Алиса:{/b} Кому там не спится? Я ванну набираю..."
                "Это я, Макс. Можно войти?":
                    Alice "{b}Алиса:{/b} Макс, ты глухой? Я же сказала, буду в ванне плескаться. Жди как минимум час!"
                    Max_00 "Ладно, ладно..."
                "{i}уйти{/i}":
                    pass
            jump .end
        "{i}заглянуть со двора{/i}" if flags.ladder < 2:
            scene Alice bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "{m}Кажется, Алиса и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но подходить ближе опасно - может заметить...{/m}"
            menu:
                Max_09 "{m}Нужно что-нибудь придумать...{/m}"
                "{i}уйти{/i}":
                    $ flags.ladder = 1
                    jump .end
        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "{m}Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное...{/m}"
            $ flags.ladder = 3
            $ items['ladder'].give()
            jump .ladder
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump .ladder
        "{i}уйти{/i}":
            jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-evening 02'+mgg.dress)
        Max_04 "{m}Посмотрим, что у нас тут...{/m}"

        $ r1 = random_randint(1, 4)

        scene BG bath-00
        $ renpy.show('Alice bath-window 0'+str(r1))
        show FG bath-00
        $ Skill('hide', 0.025, 10)
        if r1 == 1:
            menu:
                Max_03 "{m}Вот это повезло! Алиса как раз собирается принять ванну... Её шикарная попка меня просто завораживает! Так бы любовался и любовался...{/m}"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Alice bath-window '+random_choice(['02', '03', '04']))
                    $ Skill('hide', 0.025, 10)
                    menu:
                        Max_05 "{m}Чёрт возьми, она меня что, специально дразнит своей мокренькой грудью... Может моя старшая сестрёнка и стерва, но какая же она горячая! Очень сексуальна...{/m}"
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ alice.dress_inf = '00aa'
                            pass
                "{i}уйти{/i}":
                    pass
        else:
            menu:
                Max_05 "{m}Чёрт возьми, она меня что, специально дразнит своей мокренькой грудью... Может моя старшая сестрёнка и стерва, но какая же она горячая! Очень сексуальна...{/m}"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Alice bath-window 05
                    $ Skill('hide', 0.025, 10)
                    menu:
                        Max_07 "{m}Эх! Самое интересное продолжалось недолго... Единственное, что напоследок остаётся сделать, это насладится её бесподобной попкой!{/m}"
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ alice.dress_inf = '04aa'
                            pass
                "{i}уйти{/i}":
                    pass
    label .end:
        $ spent_time += 10
        jump Waiting


label alice_sleep_night:
    scene location house aliceroom door-night
    if alice.hourly.sleep != 0:
        return

    $ alice.hourly.sleep = 1
    $ alice.prev_plan = alice.plan_name
    menu:
        Max_00 "{m}Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья...{/m}"
        "{i}заглянуть в окно{/i}":
            $ spent_time += 10
            if flags.eric_jerk and '02:00'<=tm<'02:30':
                jump jerk_balkon

            if alice.sleeptoples and alice.req.result == 'not_sleep':
                $ alice.sleeptoples = False
            if alice.sleepnaked and alice.req.result == 'not_naked':
                $ alice.sleepnaked = False

            # scene BG char Alice bed-night-01
            # $ renpy.show('Alice sleep-night '+pose3_2)
            # if not alice.sleepnaked:
            #     $ renpy.show('cloth1 Alice sleep-night '+pose3_2+alice.dress)
            # $ renpy.show('FG alice-voyeur-night-00'+mgg.dress)
            scene alice_sleep_night
            if alice.req.result == 'naked':
                # договорённость спать голой
                # условие выполняется
                if pose3_2 == '01':
                    Max_07 "{m}О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её совершенно обнажённого тела хочется смотреть вечно!{/m}" nointeract
                elif pose3_2 == '02':
                    Max_04 "{m}Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою голенькую попку для меня во всей красе.{/m}" nointeract
                else:
                    Max_01 "{m}Обалденно! Сестрёнка спит выгнув спину, отчего её голая грудь торчит, как два холмика... Соблазнительное зрелище...{/m}" nointeract

            elif alice.req.result == 'sleep' or alice.flags.shower_max > 2:
                # договорённость спать топлес или после третьего совместного душа с Максом
                # условие выполняется
                if pose3_2 == '01':
                    Max_07 "{m}О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела, в одних лишь трусиках, хочется смотреть вечно!{/m}" nointeract
                elif pose3_2 == '02':
                    Max_04 "{m}Эх! Не повезло, что Алиса спит спиной к окну и её грудь не видно... Правда, в таком случае, всегда можно насладиться красотой Алисиной попки.{/m}" nointeract
                else:
                    Max_01 "{m}Обалденно! Сестрёнка спит выгнув спину, отчего её голая грудь торчит, как два холмика... Соблазнительное зрелище...{/m}" nointeract

            elif alice.req.result == 'not_sleep' and not alice.req.noted:
                # Алиса нарушила условие
                $ alice.req.noted = True
                $ alice.dress_inf = alice.clothes.sleep.GetCur().info
                if pose3_2 == '01':
                    Max_07 "{m}О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела в этом полупрозрачном белье хочется смотреть вечно! Только вот не всё из этого должно быть на ней одето!{/m}"
                elif pose3_2 == '02':
                    Max_04 "{m}Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою попку для меня во всей красе. И есть на ней что-то явно лишнее!{/m}"
                else:
                    Max_01 "{m}Обалденно! Сестрёнка спит выгнув спину, отчего её грудь торчит, как два холмика... Соблазнительно... Но, похоже, она кое-что забыла с себя снять перед сном!{/m}"
                Max_09 "{m}Так что надо выводить тебя на чистую воду... Возможно, мне стоит воспользоваться тем, чего Алиса боится больше всего?!{/m}" nointeract

            elif alice.req.result == 'not_naked' and not alice.req.noted:
                # Алиса нарушила условие
                $ alice.req.noted = True
                $ alice.dress_inf = alice.clothes.sleep.GetCur().info
                if pose3_2 == '01':
                    Max_07 "{m}О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела в этом полупрозрачном белье хочется смотреть вечно! Но она должна быть совершенно голой! Эх, Алиса, не хорошо нарушать наш уговор...{/m}"
                elif pose3_2 == '02':
                    Max_04 "{m}Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою попку для меня во всей красе. Но она должна быть совершенно голой! Эх, Алиса, не хорошо нарушать наш уговор...{/m}"
                else:
                    Max_01 "{m}Обалденно! Сестрёнка спит выгнув спину, отчего её грудь торчит, как два холмика... Соблазнительно... Но она должна быть совершенно голой! Эх, Алиса, не хорошо нарушать наш уговор...{/m}"
                Max_09 "{m}Так что надо выводить тебя на чистую воду... Возможно, мне стоит воспользоваться тем, чего Алиса боится больше всего?!{/m}" nointeract

            else:
                if pose3_2 == '01':
                    Max_07 "{m}О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела в этом полупрозрачном белье хочется смотреть вечно!{/m}" nointeract
                elif pose3_2 == '02':
                    Max_04 "{m}Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою попку для меня во всей красе.{/m}" nointeract
                else:
                    Max_01 "{m}Обалденно! Сестрёнка спит выгнув спину, отчего её грудь торчит, как два холмика... Соблазнительно...{/m}" nointeract
            menu:
                "{i}прокрасться в комнату{/i}":
                    pass
                "{i}уйти{/i}":
                    jump .end
            $ spent_time += 10
            # scene BG char Alice bed-night-02
            # $ renpy.show('Alice sleep-night-closer '+pose3_2)
            # if not alice.sleepnaked:
            #     $ renpy.show('cloth1 Alice sleep-night-closer '+pose3_2+alice.dress)
            scene alice_sleep_night closer
            if alice.req.result == 'naked':
                # договорённость спать голой
                # условие выполняется
                if pose3_2 == '01':
                    Max_03 "{m}Да уж... Её обворожительной попкой можно любоваться бесконечно... Так и хочется кое-что в неё присунуть... Правда, тогда это будет последнее, что я сделаю в жизни. Так что лучше потихоньку уходить...{/m}" nointeract
                elif pose3_2 == '02':
                    Max_02 "{m}Класс! Может Алиса мне и сестра, но рядом с этой упругой попкой я бы не лежал без дела, а как следует её... Но пора уходить, а то ещё проснётся...{/m}" nointeract
                else:
                    Max_05 "{m}Чёрт, какая же она притягательная, когда лежит вот так, полностью голая... И как будто только и ждёт, когда я занырну между этих сисечек и её стройных ножек! Только бы она сейчас не проснулась...{/m}" nointeract

            elif alice.req.result == 'sleep' or alice.flags.shower_max > 2:
                # договорённость спать топлес или после третьего совместного душа с Максом
                # условие выполняется
                if pose3_2 == '01':
                    Max_03 "{m}Да уж... Жаль только, что грудь не видно так, как хотелось бы, но её обворожительной попкой можно любоваться бесконечно... Так и хочется по ней шлёпнуть... Правда, тогда это будет последнее, что я сделаю в жизни. Так что лучше потихоньку уходить...{/m}" nointeract
                elif pose3_2 == '02':
                    Max_02 "{m}Класс! Может Алиса мне и сестра, но рядом с этой упругой попкой я бы пристроился с огромным удовольствием... Можно было бы пройти ещё дальше и хоть одним глазком увидеть сиськи, но лучше уйти, а то ещё проснётся...{/m}" nointeract
                else:
                    Max_05 "{m}Чёрт, какая же она притягательная, когда лежит вот так, с совершенно голой грудью... Так и хочется занырнуть между этих сисечек и её стройных ножек! Только бы она сейчас не проснулась...{/m}" nointeract

            else:
                if pose3_2 == '01':
                    Max_03 "{m}Да уж... Её обворожительной попкой можно любоваться бесконечно... Так и хочется по ней шлёпнуть... Правда, тогда это будет последнее, что я сделаю в жизни. Так что лучше потихоньку уходить...{/m}" nointeract
                elif pose3_2 == '02':
                    Max_02 "{m}Класс! Может Алиса мне и сестра, но рядом с этой упругой попкой я бы пристроился с огромным удовольствием... Но пора уходить, а то ещё проснётся...{/m}" nointeract
                else:
                    Max_01 "{m}Чёрт, какая же она притягательная, когда лежит вот так... Так и хочется занырнуть между этих сисечек и её стройных ножек! Только бы она сейчас не проснулась...{/m}" nointeract
            menu:
                "{i}уйти{/i}":
                    pass
            jump .end
        "{i}уйти{/i}":
            jump .end
    label .end:
        jump Waiting


label alice_sleep_morning:
    scene location house aliceroom door-morning
    if alice.hourly.sleep != 0:
        return
    $ alice.hourly.sleep = 1
    $ alice.prev_plan = alice.plan_name
    menu:
        Max_00 "{m}Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья...{/m}"
        "{i}заглянуть в окно{/i}":
            $ spent_time = 10

            if alice.sleeptoples and alice.req.result == 'not_sleep':
                $ alice.sleeptoples = False
            if alice.sleepnaked and alice.req.result == 'not_naked':
                $ alice.sleepnaked = False

            # scene BG char Alice bed-morning-01
            # $ renpy.show('Alice sleep-morning '+pose3_2)
            # if not (alice.sleepnaked or alice.dress==''):
            #     $ renpy.show('cloth1 Alice sleep-morning '+pose3_2+alice.dress)
            # $ renpy.show('FG alice-voyeur-morning-00'+mgg.dress)
            scene alice_sleep_morning
            if alice.req.result == 'naked':
                if pose3_2 == '01':
                    Max_07 "{m}Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную, совершенно голую фигурку как следует...{/m}" nointeract
                elif pose3_2 == '02':
                    Max_01 "{m}Чёрт! Как же хорошо, что теперь она спит голая и я могу насладится всей красотой её тела, и ещё как... Обалденные у неё сиськи!{/m}" nointeract
                else:
                    Max_04 "{m}Вот это да! От таких соблазнительных изгибов её полностью голого тела можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка!{/m}" nointeract

            elif alice.req.result == 'sleep' or alice.flags.shower_max > 2:
                $ alice.dress_inf = '02ga'
                if pose3_2 == '01':
                    Max_07 "{m}Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную фигурку, на которой лишь одни трусики...{/m}" nointeract
                elif pose3_2 == '02':
                    Max_01 "{m}Чёрт! Как же хорошо, что теперь она спит без лифчика и я могу насладится почти всей красотой её тела, и ещё как... Обалденные у неё сиськи!{/m}" nointeract
                else:
                    Max_04 "{m}Вот это да! От таких соблазнительных изгибов и сисечек можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка!{/m}" nointeract

            elif alice.req.result == 'not_sleep' and not alice.req.noted:
                $ alice.req.noted = True
                $ alice.dress_inf = '02'
                if pose3_2 == '01':
                    Max_07 "{m}Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную, почти голую фигурку как следует... Только вот одето на ней больше, чем должно быть!{/m}"
                elif pose3_2 == '02':
                    Max_01 "{m}Чёрт! Хоть она и спит, но прямо лицом ко мне... И тем не менее, насладится красотой её тела я могу, и ещё как... Хотя, если бы она не забыла кое-что с себя снять, было бы куда интереснее!{/m}"
                else:
                    Max_02 "{m}Вот это да! От таких соблазнительных изгибов можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка! А была бы ещё лучше, если бы снимала с себя то, что должна!{/m}"

                Max_09 "{m}Надо бы мне вывести тебя на чистую воду... Может, стоит воспользоваться тем, что пугает Алису больше всего?!{/m}" nointeract

            elif alice.req.result == 'not_naked' and not alice.req.noted:
                $ alice.req.noted = True
                $ alice.dress_inf = '02'
                if pose3_2 == '01':
                    Max_07 "{m}Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную, почти голую фигурку как следует... А если бы она снимала с себя то, что должна, то было бы просто шикарно! Нарушительница...{/m}"
                elif pose3_2 == '02':
                    Max_01 "{m}Чёрт! Хоть она и спит, но прямо лицом ко мне... И тем не менее, насладится красотой её тела я могу, и ещё как... А если бы она снимала с себя то, что должна, то было бы просто шикарно! Нарушительница...{/m}"
                else:
                    Max_02 "{m}Вот это да! От таких соблазнительных изгибов можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка! А если бы она снимала с себя то, что должна, то было бы просто шикарно! Нарушительница...{/m}"

                Max_09 "{m}Надо бы мне вывести тебя на чистую воду... Может, стоит воспользоваться тем, что пугает Алису больше всего?!{/m}" nointeract

            else:
                if pose3_2 == '01':
                    Max_07 "{m}Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную, почти голую фигурку как следует... {/m}" nointeract
                elif pose3_2 == '02':
                    Max_01 "{m}Чёрт! Хоть она и спит, но прямо лицом ко мне... И тем не менее, насладится красотой её тела я могу, и ещё как...{/m}" nointeract
                else:
                    Max_02 "{m}Вот это да! От таких соблазнительных изгибов можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка!{/m}" nointeract
            menu:
                "{i}прокрасться в комнату{/i}":
                    pass
                "{i}уйти{/i}":
                    jump Waiting
            $ spent_time += 10

            # scene BG char Alice bed-morning-02
            # $ renpy.show('Alice sleep-morning-closer '+pose3_2)
            # if not (alice.sleepnaked or alice.dress==''):
            #     $ renpy.show('cloth1 Alice sleep-morning-closer '+pose3_2+alice.dress)
            scene alice_sleep_morning closer
            if alice.req.result == 'naked':
                if pose3_2 == '01':
                    Max_05 "{m}Ох, от такого вида в голове остаются лишь самые пошлые мысли... Как же я хочу помять эту попку! А после натянуть её на свой... И ещё... пожалуй, пока она не проснулась, тихонько отсюда уйти.{/m}" nointeract
                elif pose3_2 == '02':
                    Max_03 "{m}О, да! Не лечь и не приобнять эту нежную попку – настоящее преступление... Как и поласкать эти аппетитные сосочки! Только вот Алиса посчитает иначе и оторвёт мне голову прямо здесь. Так что лучше потихоньку уходить...{/m}" nointeract
                else:
                    Max_02 "{m}Вот чёрт! С каким же огромным удовольствием я бы запустил свои руки во все самые интересные места на ёё теле... Эх, хороша сестрёнка, но пора уходить... Если она проснётся, мне точно не поздоровится.{/m}" nointeract

            elif alice.req.result == 'sleep' or alice.flags.shower_max > 2:
                if pose3_2 == '01':
                    Max_05 "{m}Ох, от такого вида в голове остаются лишь самые пошлые мысли... Как же я хочу помять эти сиськи! И стянуть эти трусики... и ещё... пожалуй, пока она не проснулась, тихонько отсюда уйти.{/m}" nointeract
                elif pose3_2 == '02':
                    Max_03 "{m}О, да! Не лечь и не приобнять эту нежную попку – настоящее преступление... Как и поласкать эти аппетитные сосочки! Только вот Алиса посчитает иначе и оторвёт мне голову прямо здесь. Так что лучше потихоньку уходить...{/m}" nointeract
                else:
                    Max_02 "{m}Вот чёрт! С каким же огромным удовольствием я бы сел рядом с ней, запустил свои руки в её трусики и мял эти упругие сисечки всё утро... Эх, хороша сестрёнка, но пора уходить... Если она проснётся, мне точно не поздоровится.{/m}" nointeract

            else:
                if pose3_2 == '01':
                    Max_05 "{m}Ох, от такого вида в голове остаются лишь самые пошлые мысли... Как же я хочу помять эту попку! И стянуть эти трусики... и ещё... пожалуй, пока она не проснулась, тихонько отсюда уйти.{/m}" nointeract
                elif pose3_2 == '02':
                    Max_03 "{m}О, да! Не лечь и не приобнять эту нежную попку – настоящее преступление... Только вот Алиса посчитает иначе и оторвёт мне голову прямо здесь. Так что лучше потихоньку уходить...{/m}" nointeract
                else:
                    Max_02 "{m}Вот чёрт! С каким же огромным удовольствием я бы сел рядом с ней, запустил свои руки под её белье и ласкал эти упругие сисечки всё утро... Эх, хороша сестрёнка, но пора уходить... Если она проснётся, мне точно не поздоровится.{/m}" nointeract
            menu:
                "{i}уйти{/i}":
                    pass
        "{i}уйти{/i}":
            pass
    jump Waiting


label alice_shower:
    scene location house bathroom door-morning
    if alice.daily.shower == 3:
        Max_00 "{m}Алиса меня уже поймала сегодня. Не стоит злить её ещё больше, а то точно что-нибудь оторвет.{/m}"
        return
    elif alice.daily.shower == 1:
        Max_00 "{m}Я уже подсматривал сегодня за Алисой. Не стоит искушать судьбу слишком часто.{/m}"
        return
    elif  alice.daily.shower == 2:
        Max_00 "{m}Алиса меня и так сегодня едва не поймала. Не стоит искушать судьбу слишком часто.{/m}"
        return
    elif alice.daily.shower > 3:
        menu:
            Max_00 "{m}Алиса сейчас принимает душ...{/m}"
            "{i}уйти{/i}":
                return
    else:
        $ alice.daily.shower = 4
        $ alice.prev_plan = alice.plan_name

        if alice.flags.promise == 'shower':
            # выбрал обещание для душа
            jump ev_v92_021 # Целовашки/обнимашки от Алисы в душе (обещание во время куни у ТВ)

        menu:
            Max_00 "{m}Похоже, Алиса принимает душ...{/m}"
            "{i}заглянуть со двора{/i}" if not flags.block_peeping:
                if alice.sorry.owe:
                    Max_10 "{m}С радостью бы подсмотрел за голенькой сестрёнкой, но это слишком опасно! Сперва нужно подарить то, что обещал...{/m}"
                    $ current_room = house[6]
                    jump AfterWaiting
                jump .start_peeping
            "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
                jump .ladder
            "{i}уйти{/i}":
                return

    label .start_peeping:
        # $ renpy.dynamic('r1')
        $ Skill('hide', 0.025, 10)
        $ r1 = random_randint(1, 4)

        scene image ('Alice shower 0'+str(r1))
        $ renpy.show('FG shower 00'+mgg.dress)
        play music spying

        if flags.eric_wallet == 2:
            Max_09 "{m}Лучше вообще свести подглядывания к минимуму, пока я не избавлюсь от Эрика. Чтобы никого ещё больше не расстраивать...{/m}"
            menu:
                Max_01 "{m}Хорошо, что это не распространяется на Киру...{/m}"
                "{i}уйти{/i}":
                    $ flags.block_peeping = 1
                    jump .end
        if not get_alice_shower_peeping_stage():
            Max_07 "{m}Ого... Голая Алиса всего в паре метров от меня! Как же она хороша... Главное, чтобы она меня не заметила, а то ведь убьёт на месте.{/m}" nointeract
        elif get_alice_shower_peeping_stage() == 1:
            Max_07 "{m}Ого... Голая Алиса всего в паре метров от меня! Но мне стоит подглядывать очень осторожно... Помогая Алисе с блогом у меня могут возникнуть незапланированные траты, а если она меня сейчас заметит - траты только увеличатся.{/m}" nointeract
        else:   # get_alice_shower_peeping_stage() == 2
            Max_07 "{m}Ого... Голая Алиса всего в паре метров от меня! Как же она хороша... И даже если она меня заметит - не страшно! Выкручусь как-нибудь.{/m}" nointeract

        menu:
            "{i}продолжить смотреть{/i}" ('hide', mgg.stealth * 3, 90, 2) if alice.dcv.shower.stage < 2:
                jump .closer_peepeng
            "{i}взглянуть со стороны{/i}" ('hide', mgg.stealth * 2, 90, 2) if alice.dcv.shower.stage < 2:
                jump .alt_peepeng
            "{i}немного пошуметь{/i}" if get_alice_shower_peeping_stage() == 0 and alice.dcv.shower.stage < 2:
                jump .pinded
            "{i}немного пошуметь{/i}" if get_alice_shower_peeping_stage() > 1:
                jump .pinded
            "{i}запустить паука к Алисе{/i}" if items['spider'].have:
                jump .spider
            "{i}уйти{/i}":
                jump .end

    label .spider:
        $ renpy.scene()
        $ renpy.show('Max spider-bathroom 01'+mgg.dress)
        if not _in_replay:
            $ items['spider'].use()
            $ SpiderKill = 1
            $ SpiderResp = 2
            $ spent_time += 10
        menu:
            Max_03 "Давай, паучок, вперёд! Я хочу, чтобы ты познакомился с моей очаровательной сестрёнкой. Характер у неё правда так себе, но думаю, вы оба поладите..."
            "{i}спрятаться{/i}":
                stop music fadeout 1.5
        scene BG char Max spider-bathroom-00
        $ renpy.show('Max spider-bathroom 02'+mgg.dress)
        Max_01 "{m}Похоже, я успел обойти ванную комнату через дом ещё до криков Алисы... Это хорошо, значит Алиса вот-вот должна заметить паука! Остаётся только немного...{/m}"
        play sound scare1
        Alice "{b}Алиса:{/b} А-а-а-а-а!!! Вот чёрт... Охренеть!"
        Max_02 "{m}...подождать.{/m}"
        if not _in_replay:
            $ poss['spider'].open(3)
        $ var_pose = random_choice(['a','b','c'])
        scene BG char Alice spider-bathroom-00
        $ renpy.show('Alice spider-shower 01'+var_pose)
        Alice_06 "Боже мой, какой кошмар... И что мне теперь с этим пауком делать... Ну почему эти твари лезут именно ко мне? Может быть, он уползёт..."
        $ renpy.show('Max spider-bathroom 03'+mgg.dress)
        Max_07 "Алиса, ты кричала... Что случилось?"
        $ var_pose = random_choice(['a','b','c'])
        $ renpy.show('Alice spider-shower 02'+var_pose)
        if GetRelMax('alice')[0] < 1:
            Alice_16 "Макс! Ты какого хрена так тихо подходишь, я же тут голая стою! Мало того, что паук ко мне в душ заполз, так ещё ты тут на меня пялишься... А ну вали отсюда, бегом!"
            Max_00 "Ладно, ладно... Как скажешь. Ухожу."
            jump .end
        elif GetRelMax('alice')[0] == 1:
            Alice_14 "Макс! Ты почему так тихо подходишь, а ну не смотри, я же голая... Иди куда-нибудь в другое место, пожалуйста. И не вздумай подглядывать!"
            Max_08 "Ну хорошо, как скажешь... А случилось-то что?"
            Alice_12 "Ко мне в душ паук заполз, вот что! Не смотри на меня... Отвернись и уходи."
            Max_01 "Хочешь, я уберу паука и..."
            Alice_18 "Макс!!!"
            Max_00 "Ладно, ладно... Уже ухожу."
            jump .end
        else:
            if alice.flags.together_sleep > 3:
                # Макс обломал Алису с куни в её комнате при защите от пауков
                if not alice.flags.shower_max:
                    # Макс охраняет Алису в душе 1-ый раз
                    jump ev_v92_009
                elif alice.flags.shower_max == 1:
                    # Макс охраняет Алису в душе 2-ый раз
                    jump ev_v92_010
                elif alice.flags.shower_max == 2:
                    # Макс охраняет Алису в душе 3-ый раз
                    jump ev_v92_011
                else:
                    # в дальнейшем
                    jump ev_v92_022
            elif alice.flags.together_sleep > 0:
                # Макс начал ночевать с Алисой
                call ev_v92_008 from _call_ev_v92_008
            else:
                # Макс ещё не ночевал с Алисой
                Alice_06 "Макс! Вот чёрт, ещё и ты меня напугал! Ко мне здоровенный паук в душ заполз..."
                Max_04 "Не переживай! Сейчас я его поймаю и выброшу... И ты спокойно домоешься."
                Alice_13 "Нет уж, я не смогу пока зайти обратно... Мне нужно время, чтобы перестать думать обо всём этом кошмаре. Лучше принеси мне полотенце, оно там, в ванной... А то слишком уж тебе повезло на меня голую глазеть!" nointeract
                menu:
                    "Хорошо, сейчас принесу. Никуда не уходи...":
                        pass

        # scene BG char Alice spider-bathroom-01
        # $ renpy.show('Alice spider-shower 03'+random_choice(['a','b','c']))
        $ var_pose = random_choice(['a','b','c'])
        $ var_stage, var_pose2 = '03', '04'
        scene alice_near_shower
        Alice_12 "Макс, ну ты где там?! Только смотри, чтобы этого монстра не было на моём полотенце! Иначе тебе будет очень-очень больно..."
        # $ renpy.show('Max spider-bathroom 04'+mgg.dress)
        scene alice_near_shower mgg
        if not _in_replay:
            $ spent_time = 50 - int(tm[-2:])
        menu:
            Max_03 "Вот я и вернулся! С полотенцем всё в порядке, вот, держи."
            "{i}отдать Алисе полотенце{/i}":
                # $ renpy.show('Alice spider-shower 04'+random_choice(['a','b']))
                # $ renpy.show('Max spider-bathroom 06'+mgg.dress)
                $ var_pose = random_choice(['a', 'b'])
                $ var_stage, var_pose2 = '04', '06'
                if 'sexbody1' in alice.gifts and alice.flags.hugs>4:
                    # подарено сексуальное боди + 3-5 обнимашек за сладости
                    menu:
                        Alice_07 "Ох, Макс, спасибо тебе огромное! Думала, ты будешь прикалываться, но ты можешь временами вести себя, не как озабоченный... Это приятно."
                        "Да ладно, это ерунда, обращайся.":
                            pass
                        "А как же братика обнять?" ('soc', mgg.social * 2, 90):  #(убеждение)
                            jump .hug
                else:
                    Alice_07 "Ох, Макс, спасибо тебе огромное! Думала, ты будешь прикалываться, но ты можешь временами вести себя, не как озабоченный... Это приятно."
                    Max_04 "Да ладно, это ерунда, обращайся."
                Alice_03 "Ну всё, я пошла... Только не забудь паука вышвырнуть из ванной, хорошо?!"
                Max_01 "Да. Не забуду..."
                $ renpy.end_replay()
                $ infl[alice].add_m(10)
                $ AddRelMood('alice', 10, 50, 3)

            "{i}отдать Алисе полотенце (выронив его из одной руки){/i}":
                # $ renpy.show('Alice spider-shower 05'+random_choice(['a','b','c','d']))
                # $ renpy.show('Max spider-bathroom 05'+mgg.dress)
                $ var_pose = random_choice(['a','b','c','d'])
                $ var_stage, var_pose2 = '05', '05'
                Alice_14 "Макс!!! Ах ты... Ну-ка дай сюда полотенце!!!"
                # show Alice spider-shower 04b
                # $ renpy.show('Max spider-bathroom 06'+mgg.dress)
                $ var_pose, var_stage, var_pose2 = 'b', '04', '06'
                Max_08 "Ой! Извини, я..."
                menu:
                    Alice_17 "Какого чёрта, Макс?! Что за шуточки! Или ты безрукий? Живо признавайся, ты специально это сделал?!"
                    "Конечно нет! Оно случайно выскочило из руки!" ('soc', mgg.social * 3, 90):
                        pass
                if rand_result:
                    Alice_12 "[succes!t]Ну ты и криворукий, Макс! Даже такую простую вещь не можешь сделать, не накосячив... Всё, я пошла! И паука вышвырни из ванной, если конечно и он у тебя из рук не выскочит!"
                    Max_00 "Да это случайно вышло!"
                    Alice_05 "Ну да, конечно..."
                    $ renpy.end_replay()
                    $ infl[alice].add_m(4)
                else:
                    Alice_16 "[failed!t]Я тебе не верю! Наверняка ты это сделал специально, чтобы поглазеть на меня! Твоё счастье, что я не могу знать этого точно... А так бы врезала тебе между ног!"
                    Max_10 "Так получилось! Я не хотел..."
                    Alice_17 "Да иди ты, Макс!"
                    $ AddRelMood('alice', -15, -75)
        $ renpy.end_replay()
        jump .end

    label .hug:
        if rand_result:
            Alice_05 "[succes!t]Это я, конечно, могу сделать... Но если вздумаешь с меня полотенце сорвать, то я тебя прибью нафиг!"
            Max_07 "Не буду я ничего такого делать! Что я, маленький что ли?"
            # spider-bathroom-01 + spider-shower-01-max-(01a/01b)-alice-01
            scene BG char Alice spider-bathroom-01
            $ renpy.show('Alice spider-shower 01-01'+mgg.dress)
            $ added_mem_var('alice_hug_in_shower')
            menu:
                Alice_03 "Таких объятий тебе достаточно? Уж извини, что не обнимаю обеими руками... сам знаешь почему..."
                "Зато у меня руки свободны... {i}(обнять в ответ){/i}":
                    # spider-shower-02 + spider-shower-02-max-(01a/01b)-alice-01
                    scene BG char Alice spider-bathroom-02
                    $ renpy.show('Alice spider-shower 02-01'+mgg.dress)
                    menu:
                        Alice_04 "Эм... Макс... Это уже как-то слишком, тебе не кажется?!"
                        "Нет. Слишком - это вот так... {i}(обнять за попку){/i}" if alice.flags.privpunish:
                            jump .dangerous_hugs

                        "Может быть, чуть-чуть... Рад был помочь.":
                            pass
                "Вот это другое дело! Рад был помочь.":
                    pass
            Alice_03 "Ну всё, я пошла... Только не забудь паука вышвырнуть из ванной, хорошо?!"
            Max_01 "Да. Не забуду..."
            jump .end
        else:
            # (Убеждение не удалось!)
            Alice_05 "[failed!t]Ага, знаю я, чего ты хочешь! Полуголую сестрёнку полапать за всякие запретные места... Нет уж, Макс, я пошла... Только не забудь паука вышвырнуть из ванной, хорошо?!"
            Max_01 "Да. Не забуду..."

    label .dangerous_hugs:
        #если было приватное наказание с поглаживанием
        scene BG char Alice spider-bathroom-02
        $ renpy.show('Alice spider-shower 02-02'+mgg.dress)
        # spider-shower-02 + spider-shower-02-max-(02a/02b)-alice-02
        $ ctd = Countdown(3, 'alice_shower.hands_off')

        # (на время c вариантами "убрать руки" и "не убирать руки")
        # варианты располагаем рандомно, чтобы отучить бездумно жать "1"
        $ renpy.block_rollback()
        Alice_14 "Так, ну всё! У тебя три... ну максимум пять секунд, чтобы убрать руки. Иначе я тебе что-нибудь оторву!{p=5}{nw}"
        # меню с таймером
        show screen countdown
        extend "" nointeract

        $ rl = create_random_list(3)
        menu (rand='all'):
            "{i}убрать руки{/i}":
                $ rez = 1
            "{i}не убирать руки{/i}":
                $ rez = 0

        $ renpy.block_rollback()
        if rez:
            # (успел)
            hide screen countdown
            $ added_mem_var('alice_danger_in_shower')
            $ renpy.show('Alice spider-shower 02-01'+mgg.dress)
            # spider-shower-02 + spider-shower-02-max-(01a/01b)-alice-01
            Max_04 "Всё, убрал. Но я просто хотел прикрыть твою попку, чтобы никто на неё не глазел."
            Alice_05 "Ну конечно. И кто, интересно, на неё глазеет?!"
            Max_07 "Пауки, Алиса. Они такие! И глаз у них дофига бывает!"
            Alice_06 "Бррр... Фу! Какая мерзость... Всё, я пошла! Только не забудь паука вышвырнуть из ванной, хорошо?!"
            Max_01 "Да. Не забуду..."
            jump .end
        else:
            hide screen countdown
            jump .hands_off

    label .hands_off:
        $ renpy.block_rollback()
        # (не успел)
        # spider-shower-02 + spider-shower-02-max-(03a/03b)-alice-03
        scene BG char Alice spider-bathroom-02
        $ renpy.show('Alice spider-shower 02-03'+mgg.dress)
        Max_12 "А-а-ай! Мне же больно, Алиса! Перестань!"
        Alice_16 "А я ведь тебя предупреждала! Наверно, раз до тебя не дошло, нужно крутануть ещё сильнее..."
        Max_14 "Ой! Я понял... Больше не буду! Отпусти уже..."
        Alice_17 "То-то же! Всё, я пошла! И паука вышвырни из ванной..."
        Max_10 "Хорошо... Как только отпустишь!"
        jump .end

    label .alt_peepeng:
        $ spent_time += 10
        if rand_result < 2:
            jump .not_luck
        # $ renpy.dynamic('r1')
        $ alice.daily.shower = 1
        $ alice.dress_inf = '00aa'
        $ r1 = random_randint(1, 6)
        scene BG bathroom-shower-03
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Alice shower-alt 0'+str(r1))
        show FG shower-water
        if r1 % 2 > 0:
            Max_01 "[undetect!t]{m}Супер! С распущенными волосами моя старшая сестрёнка становится очень сексуальной... Ухх, помылить бы эти сисечки, как следует...{/m}"
        else:
            Max_01 "[undetect!t]{m}О, да... Перед мокренькой Алисой сложно устоять! Особенно, когда она так соблазнительно крутит своей попкой...{/m}"
        jump .end

    label .closer_peepeng:
        $ spent_time += 10
        if rand_result > 1:
            # $ renpy.dynamic('r1')
            $ alice.daily.shower = 1
            $ alice.dress_inf = '00aa'
            $ r1 = random_randint(1, 6)
            scene BG bathroom-shower-01
            $ renpy.show('Alice shower-closer 0'+str(r1))
            show FG shower-closer
            if r1 % 2 > 0:
                Max_01 "[undetect!t]{m}Супер! С распущенными волосами моя старшая сестрёнка становится очень сексуальной... Ухх, помылить бы эти сисечки, как следует...{/m}"
            else:
                Max_01 "[undetect!t]{m}О, да... Перед мокренькой Алисой сложно устоять! Особенно, когда она так соблазнительно крутит своей попкой...{/m}"
            jump .end
        else:
            jump .not_luck

    label .not_luck:
        if rand_result or get_alice_shower_peeping_stage() == 1:
            # $ renpy.dynamic('r1')
            $ alice.daily.shower = 2
            $ alice.dress_inf = '00aa'
            $ r1 = random_randint(7, 8)
            scene BG bathroom-shower-01
            $ renpy.show('Alice shower-closer 0'+str(r1))
            show FG shower-closer
            Max_09 "{color=[orange]}{i}Кажется, Алиса что-то заподозрила!{/i}{/color}\n{m}Ох, чёрт! Нужно скорее уносить ноги, пока они ещё есть...{/m}"
            jump .end
        else:
            jump .pinded

    label .pinded:
        # $ renpy.dynamic('r1')

        if flags.mistres_pun:
            $ alice.dcv.mistress.set_lost(1)
        else:
            $ punreason[1] = 1
            $ alice.daily.shower = 3
        if not alice.flags.shower_max:
            # Макс ещё не принимал душ с Алисой
            $ r1 = random_choice(['09', '10'])
        else:
            # shower-alice-(09/10) - уходят, на смену приходят shower-alice-(07/08)
            $ r1 = random_choice(['07', '08'])

        scene BG bathroom-shower-01
        $ renpy.show('Alice shower-closer '+r1)
        show FG shower-closer
        if alice.dcv.shower.stage and get_alice_shower_peeping_stage() < 2:
            Alice_15 "[spotted!t]Макс!!! Опять ты за мной подглядываешь! Сколько можно-то?! Совсем что ли весь страх потерял?"
            Max_13 "Нет! Я просто... Так получилось. Чистое совпадение!"
            Alice_18 "А ну пошёл отсюда, извращенец такой! Считай мама уже всё знает! И даже не пытайся извиняться! Брысь!!!"
            Max_10 "Вот чёрт!"
            $ alice.dcv.shower.stage = 2
            $ alice.dcv.shower.set_lost(4)
            jump .end
        elif 18 > poss['risk'].st() > 14:
            Alice_15 "[spotted!t]Макс!!! Опять ты за мной подглядываешь! Сколько можно-то?! Совсем что ли весь страх потерял?"
            Max_13 "Нет! Я просто... Так получилось. Чистое совпадение!"
            Alice_18 "Ух, я тобой займусь вечером, если осмелишься подойти... А сейчас брысь отсюда!!!"
            Max_10 "Вот чёрт!"
            jump .end
        elif poss['risk'].st() > 17 and not alice.flags.shower_max:
            Alice_15 "[spotted!t]Макс!!! Опять ты здесь! Сколько можно-то?! Тебе по заднице нравится получать что ли?"
            Max_13 "Нет! Я просто..."
            Alice_18 "Ух, я тобой займусь вечером, если осмелишься подойти... А сейчас брысь отсюда!!!"
            Max_10 "Вот чёрт!"
            jump .end
        elif alice.flags.shower_max > 0:
            # после того, как Макс 1-ый раз примет душ вместе с Алисой (из-за паука)
            Alice_12 "[spotted!t]Блин, Макс! Напугал! Тебе по заднице так сильно неймётся получить? Я это запросто устрою..."
            Max_10 "Да за что?! Я же не увидел ничего нового!"
            Alice_16 "Подглядывать - нехорошо! И это обязательно должно наказываться. Не мной, так мамой."
            Max_11 "Вот же ёлки-палки."
            jump .end

        menu:
            Alice_12 "[spotted!t]Макс!!! Ты за мной подглядываешь?! Ты труп! Твоё счастье, что я сейчас голая... Но ничего, я маме всё расскажу, она тебя накажет!"
            "{i}Бежать{/i}":
                jump .end

    label .ladder:
        # $ renpy.dynamic('r1')
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "{m}Посмотрим, что у нас тут...{/m}"
        $ alice.flags.ladder += 1
        if alice.dress_inf != '04aa':
            $ r1 = {'04ca':'a', '04da':'b', '02fa':'c', '00a':'d', '00aa':'d'}[alice.dress_inf]
        else:
            if alice.nopants:
                $ r1 = random_choice(['b', 'd'])
            else:
                $ r1 = random_choice(['a', 'c'])
            $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[r1]

        scene BG bathroom-morning-00
        $ renpy.show('Alice bath-window-morning '+random_choice(['01', '02', '03'])+r1)
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        if alice.req.result == 'not_nopants' and not alice.req.noted:
            # Алиса в трусиках, хотя должна быть без них и Макс ещё об этом не знает
            Max_00 "{m}Посмотреть на Алису всегда приятно, но почему она в трусиках? Ведь мы же с ней договаривались...{/m}"
            Max_00 "{m}Непорядок. Нужно с этим что-то делать...{/m}"
            $ added_mem_var('alice_not_nopants')
            $ alice.req.noted = True
        elif r1 == 'a':
            Max_02 "{m}Да-а... Может Алиса и в халатике, но сиськи её видны просто замечательно! А они у неё - что надо...{/m}"
        elif r1 == 'b':
            Max_05 "{m}Ого! Кто бы мог подумать, что курение может принести пользу в виде моей сестрёнки, не носящей трусики. Как же она хороша...{/m}"
        elif r1 == 'c':
            Max_04 "{m}Прекрасно! Алиса сегодня без халатика... в одних трусиках... Глядя на эту красоту, можно мечтать лишь об одном!{/m}"
        else:
            Max_06 "{m}Вау! Алиса сегодня совершенно голая! Как мы и договорились, трусики она не носит и даже не представляет, что тем самым дарит мне возможность любоваться всеми её прелестями...{/m}"

        if looked_ladder():
            $ house[3].max_cam = 2
            $ items['hide_cam'].unblock()
            Max_07 "{m}Мои зрители явно пропускают много всего интересного! Мне однозначно стоит установить сюда ещё одну камеру...{/m}"
        Max_00 "{m}Ладно, хорошего понемногу, а то ещё заметит меня здесь кто-нибудь...{/m}"

    label .end:
        $ renpy.end_replay()
        $ current_room = house[6]
        $ spent_time += 10
        jump Waiting


label alice_rest_morning:
    scene BG char Alice morning
    $ renpy.show('Alice morning 01'+alice.dress)
    $ persone_button1 = 'Alice morning 01'+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_rest_evening:

    scene BG char Alice evening
    $ renpy.show('Alice evening 01'+alice.dress)
    $ persone_button1 = 'Alice evening 01'+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_dressed_shop:
    # $ renpy.dynamic('lst', 'r1', 'suf')
    scene location house aliceroom door-morning
    if alice.hourly.dressed == 0:
        $ alice.hourly.dressed = 1
        $ alice.prev_plan = alice.plan_name
        menu:
            Max_09 "{m}Кажется, все собираются на шоппинг и Алиса сейчас переодевается...{/m}"
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кто там? Я переодеваюсь!"
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Даже не вздумай! Прибью на месте! Жди там. А лучше свали подальше, чтобы под дверью не сопел тут."
                        Max_00 "Хорошо..."
                    "Хорошо, я подожду...":
                        pass
            "{i}заглянуть в окно{/i}":
                $ lst = {
                        'a':['01', '02', '03'],
                        'b':['02',],
                        'c':['02','03'],
                        'd':['02','03','05']
                    }[alice.dress]
                $ r1 = random_choice(lst)

                $ suf = 'a' if all([r1 != '01', alice.req.result == 'nopants']) else ''
                if alice.req.result == 'not_nopants':
                    $ added_mem_var('alice_not_nopants')
                    $ alice.req.noted = True

                $ alice.dress_inf = {
                        '01':'02b',
                        '02':'02a' if suf else '02d',
                        '03':'02c' if suf else '02e',
                        '05':'02h',
                    }[r1]

                if mgg.stealth >= 11.0 and random_choice([False, False, True]):
                    scene BG char Alice voyeur-01
                    $ renpy.show('Alice voyeur alt-'+r1+suf)
                    $ renpy.show('FG voyeur-morning-01'+mgg.dress)
                else:
                    scene BG char Alice voyeur-00
                    $ renpy.show('Alice voyeur '+r1+suf)
                    $ renpy.show('FG voyeur-morning-00'+mgg.dress)

                $ Skill('hide', 0.025, 10)
                if alice.req.result == 'not_nopants' and r1 not in ['01', '05']:
                    # Макс видит, что на Алисе трусики, когда их быть не должно
                    Max_01 "{m}Ага! Алиса одевается на шопинг. И похоже, пойдёт она в трусиках, а не должна... Считай, сестрёнка, ты попала! Но не сейчас... Сейчас мне лучше уходить, пока никто не заметил.{/m}"
                    $ added_mem_var('alice_not_nopants')
                elif alice.req.result == 'nopants' and r1 not in ['01', '05']:
                    # Макс видит, что Алиса соблюдает договоренность
                    Max_05 "{m}Ого! Алиса даже на шопинг пойдёт без трусиков! Интересно, что она скажет маме в кабинке для переодевания, если та это заметит? Но лучше буду гадать об этом в другом месте, а то меня заметят...{/m}"
                elif r1 in ['02', '03']:
                    # Если нет договоренности по поводу трусов
                    Max_04 "{m}Алиса переодевается... Какая соблазнительная попка у неё... Ммм! Так. Пора бы сваливать. Вдруг, кто-то заметит!{/m}"
                else:
                    # Сиськи , однако
                    Max_03 "{m}О, какой вид! Да, сестрёнка, такими классными и голыми сиськами грех не покрасоваться перед зеркалом... Однако, пора сваливать. Вдруг, кто-то заметит!{/m}"
            "{i}уйти{/i}":
                pass
        $ spent_time += 10
        jump Waiting
    return


label alice_dishes:
    scene BG crockery-morning-00
    $ renpy.show('Alice crockery-morning 01'+alice.dress)
    $ persone_button1 = 'Alice crockery-morning 01'+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show('Alice crockery-closer '+pose3_2+alice.dress)
    return


label alice_read:
    scene BG reading
    $ renpy.show('Alice reading '+pose3_2+alice.dress)
    $ persone_button1 = 'Alice reading '+pose3_2+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_read_closer:
    scene BG reading
    $ renpy.show('Alice reading-closer 01'+alice.dress)
    return


label alice_dressed_friend:
    # $ renpy.dynamic('lst', 'r1', 'suf')
    scene location house aliceroom door-day
    if alice.hourly.dressed == 0:
        $ alice.hourly.dressed = 1
        $ alice.prev_plan = alice.plan_name
        menu:
            Max_09 "{m}Кажется, Алиса куда-то собирается...{/m}"
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кто там? Я переодеваюсь!"
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Даже не вздумай! Прибью на месте! Жди там. А лучше свали подальше, чтобы под дверью не сопел тут."
                        Max_00 "Хорошо..."
                    "Хорошо, я подожду...":
                        pass
            "{i}заглянуть в окно{/i}":
                $ lst = {
                        'a':['01', '02', '03'],
                        'b':['02',],
                        'c':['02','03'],
                        'd':['02','03','05']
                    }[alice.dress]
                $ r1 = random_choice(lst)

                $ suf = 'a' if all([r1 != '01', alice.req.result == 'nopants']) else ''
                if alice.req.result == 'not_nopants':
                    $ added_mem_var('alice_not_nopants')
                    $ alice.req.noted = True

                $ alice.dress_inf = {
                        '01':'02b',
                        '02':'02a' if suf else '02d',
                        '03':'02c' if suf else '02e',
                        '05':'02h',
                    }[r1]

                if mgg.stealth >= 11.0 and random_choice([False, False, True]):
                    scene BG char Alice voyeur-01
                    $ renpy.show('Alice voyeur alt-'+r1+suf)
                    $ renpy.show('FG voyeur-morning-01'+mgg.dress)
                else:
                    scene BG char Alice voyeur-00
                    $ renpy.show('Alice voyeur '+r1+suf)
                    $ renpy.show('FG voyeur-morning-00'+mgg.dress)

                $ Skill('hide', 0.025, 10)
                if alice.req.result == 'not_nopants' and r1 not in ['01', '05']:
                    # Макс видит, что на Алисе трусики, когда их быть не должно
                    $ added_mem_var('alice_not_nopants')
                    Max_01 "{m}Алиса переодевается... Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала! Но не сейчас... Сейчас мне лучше уходить, пока никто не заметил.{/m}"
                elif alice.req.result == 'nopants' and r1 not in ['01', '05']:
                    # Макс видит, что Алиса соблюдает договоренность
                    Max_05 "{m}Супер! Алиса не надевает трусики... И правильно делает! Надеюсь, кто-то это заметит там, куда она идёт... А чтобы меня никто не заметил, лучше уходить!{/m}"
                elif r1 in ['02', '03']:
                    # Если нет договоренности по поводу трусов
                    Max_04 "{m}Алиса переодевается... Трусики хорошо смотрятся на её попке. Но без них было бы лучше... Так. Пора бы сваливать. Вдруг, кто-то заметит!{/m}"
                else:
                    # Сиськи , однако
                    Max_03 "{m}О, какой вид! Да, сестрёнка, такими классными и голыми сиськами грех не покрасоваться перед зеркалом... Однако, пора сваливать. Вдруг, кто-то заметит!{/m}"

            "{i}уйти{/i}":
                pass
        # $ current_room = house[6]
        $ spent_time = 10
        jump Waiting
    return


label alice_dressed_club:
    # $ renpy.dynamic('suf')
    scene location house aliceroom door-evening
    if alice.hourly.dressed != 0:
        return

    $ alice.hourly.dressed = 1
    $ alice.prev_plan = alice.plan_name
    menu:
        Max_00 "{m}Кажется, Алиса собирается в ночной клуб...{/m}"
        "{i}постучаться{/i}" if not flags.eric_wallet == 2:
            jump .knock
        "{i}заглянуть в окно{/i}":
            ## показываем фон и спрайт в зависимости от ношения трусиков
            if alice.req.result == 'nopants':
                $ suf = 'a'
                $ alice.dress_inf = '06b'
            else:
                $ suf = ''
                $ alice.dress_inf = '06a'
            if alice.req.result == 'not_nopants':
                $ added_mem_var('alice_not_nopants')
                $ alice.req.noted = True
            if mgg.stealth >= 11.0 and random_choice([False, False, True]):
                scene BG char Alice voyeur-01
                $ renpy.show('Alice voyeur alt-04'+suf)
                $ renpy.show('FG voyeur-morning-01'+mgg.dress)
            else:
                scene BG char Alice voyeur-00
                $ renpy.show('Alice voyeur 04'+suf)
                $ renpy.show('FG voyeur-evening-00'+mgg.dress)
            $ Skill('hide', 0.025, 10)

            ## у нас 3 варианта:
            if alice.req.result == 'not_nopants':
                ## Алиса в трусиках, но их быть не должно
                $ added_mem_var('alice_not_nopants')
                Max_01 "{m}Алиса переодевается... Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала! Но не сейчас... Сейчас мне лучше уходить, пока никто не заметил.{/m}"
            elif alice.req.result == 'nopants':
                ## Алиса без трусиков, как и должна
                Max_05 "{m}Супер! Алиса не надевает трусики... И правильно делает! Это платье без трусиков смотрится гораздо лучше... Интересно, в клубе на это кто-нибудь обратит внимание? А чтобы меня никто не заметил, лучше уходить!{/m}"
            else:
                ## Алиса в трусиках. Договоренностей нет
                Max_04 "{m}Алиса переодевается... Трусики хорошо смотрятся на её попке. Но без них это платье смотрелось бы гораздо лучше... Так. Пора бы сваливать. Вдруг, кто-то заметит!{/m}"

            $ spent_time += 10
            $ cam_flag.append('alice_dressed')
            jump Waiting
        "{i}уйти{/i}":
            jump Waiting

    label .knock:
        $ alice.dress_inf = '06'
        Alice "{b}Алиса:{/b} Кто там? Я собираюсь, подождите..."
        Max_00 "Это я, Макс. У меня к тебе дело..."
        $ spent_time += 20
        scene BG char Alice newdress
        show Alice newdress 02a
        menu:
            Alice_13 "Ну, Макс, чего хотел? Что за дело такое срочное?"
            "Выглядишь... шикарно!":
                $ AddRelMood('alice', 0, 50)
                show Alice newdress 04a
                menu:
                    Alice_03 "Спасибо... Так чего хотел, рассказывай!"
                    "Ты знаешь, я забыл...":
                        Alice_02 "Эх, Макс. Память у тебя дырявая. Тебе бы рыбки поесть. Там, говорят, фосфор. Помогает для мозгов... Ладно, вали отсюда, я ещё не закончила..."
                        jump .end
                    "У меня для тебя презент..." if kol_choco > 0:
                        jump .choco
            "У меня для тебя презент..." if kol_choco > 0:
                jump .choco
    label .choco:
        Alice_02 "Макс, ты меня удивляешь всё больше. Какой? Дай угадаю... книжка!"
        menu:
            Max_01 "Не угадала. Ты же любишь конфеты?"
            "{i}дать одну конфету{/i}":
                $ alice.daily.drink = 1
                menu:
                    Alice_05 "Люблю... И что, никакого подвоха? Просто взял и подарил конфетку на дорожку?"
                    "Ну, можешь трусы показать...":
                        Alice_02 "Может быть, мне их ещё и снять для тебя? Давай, вали уже, извращенец. А за конфетку спасибо..."
                    "Да, никакого подвоха!":
                        Alice_07 "Вот это да! Ну, спасибо тогда... А теперь вали. Я ещё не закончила..."
                $ give_choco()
                jump .end
            # "{i}дать две конфеты{/i} ## убеждение ##" if kol_choco > 1 and poss['nightclub'].used(7):
            #     $ alice.daily.drink = 2
    label .end:
        Max_04 "Ага..."
        $ spent_time += 10
        $ cam_flag.append('alice_dressed')
        jump Waiting


label alice_sun:
    if alice.daily.oiled:
        scene alice_sun_alone
        $ persone_button1 = 'Alice sun-alone 01'
        if alice.req.result == 'bikini' or all([alice.daily.oiled in [2, 4], alice.flags.shower_max > 2]):
            $ persone_button1 += 'b'
        elif alice.daily.oiled in [2, 4]:
            $ persone_button1 += 'a'

    else:
        scene BG char Alice sun
        $ renpy.show('Alice sun '+pose2_2+alice.dress)
        $ persone_button1 = 'Alice sun '+pose2_2+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_swim:
    scene image 'Alice swim '+pose3_2+alice.dress
    $ persone_button1 = 'Alice swim '+pose3_2+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_cooking_dinner:
    scene BG cooking-00
    $ renpy.show('Alice cooking 01'+alice.dress)
    $ persone_button1 = 'Alice cooking 01'+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_cooking_closer:
    scene BG cooking-01
    $ renpy.show('Alice cooking-closer '+pose3_2+alice.dress)
    return


label alice_tv:
    scene BG lounge-tv-00
    $ renpy.show('Alice tv '+pose3_2+alice.dress)
    $ persone_button1 = 'Alice tv '+pose3_2+alice.dress+'b'
    $ alice.prev_plan = alice.plan_name
    return


label alice_tv_closer:
    $ var_pose = '00'
    scene tv_talk alice
    return


label alice_morning_closer:
    scene BG char Alice morning-closer
    $ renpy.show('Alice morning-closer '+pose3_2+alice.dress)
    return


label alice_evening_closer:
    scene BG char Alice evening-closer
    $ renpy.show('Alice evening-closer '+pose3_2+alice.dress)
    return

label spider_in_bed:
    $ mood = 0
    $ naked = False
    $ toples = False
    if alice.req.result == 'naked':
        # договорённость спать голой
        $ suf = 'n'
        $ naked = True
    elif alice.req.result == 'sleep':
        # договорённость спать топлес
        $ suf = alice.dress[:1]+'t'
        $ toples = True
    else:
        $ suf = alice.dress[:1]
    if alice.req.result in ['not_sleep', 'not_naked']:
        $ alice.req.noted = True

    # scene BG char Alice spider-night-01
    # $ renpy.show('Alice spider-night 01-'+random_choice(['01', '02', '03'])+suf)
    $ var_stage, var_pose, var_dress = '01', random_choice(['01', '02', '03']), suf
    scene alice_wakes_max_up with fade4
    Alice_13 "Макс!"

    # scene BG char Alice spider-night-02
    # $ renpy.show('Max spider-night 02-'+random_choice(['01', '02', '03']))
    # $ renpy.show('Alice spider-night 02-01'+suf)
    $ var_stage, var_pose, var_pose2 = '02', '01', random_choice(['01', '02', '03'])
    scene alice_wakes_max_up mgg
    if alice.dress == 'b':
        show screen Cookies_Button
    menu:
        Alice_12 "Макс! Макс! Вставай быстрее! Мне нужна помощь!"
        "Что случилось?":
            pass
        "Разбирайся сама..." if not _in_replay:
            jump .goaway

    # show Max spider-night 02-04
    $ var_pose2 = '04'
    menu:
        Alice_06 "Макс, помоги. В моей комнате огромный такой, просто гигантский паук! Убей его, пожалуйста!"
        "Ну, пойдём посмотрим...":
            hide screen Cookies_Button
            jump .help
        "Паук? Ерунда какая. Сама разбирайся с ним..." if not _in_replay:
            jump .goaway

    label .goaway:
        hide screen Cookies_Button
        scene Max_sleep with diss5
        menu:
            Max_09 "Бегает ещё, кричит что-то... Совсем сдурела..."
            "{i}спать до утра{/i}":
                $ mood -= 20
                $ spent_time = 10
                $ AddRelMood('alice', 0, mood)
                return

    label .help:
        $ var_stage, var_pose, var_pose2 = '03', random_choice(['01', '02', '03']), '01'
        scene alice_talk_max_aliceroom

        if not _in_replay:
            $ poss['spider'].open(4)

        menu:
            Alice_13 "Макс, Макс! Вот он! Убей его, скорее!!!"
            "А что мне за это будет?" if all([not toples, not naked, not alice.req.noted]):  # Вариант недоступен, если Алиса без лифчика или нарушает договоренность и Макс об этом знает
                $ var_pose, var_pose2 = '04', '02'
                menu:
                    Alice_12 "Что ты хочешь за смерть этого паука?"
                    "Давай $10!" ('soc', mgg.social * 5, 90):
                        if rand_result:
                            jump .money
                        else:
                            jump .fail
                    "Покажи сиськи!" ('soc', mgg.social * 3, 90):
                        if rand_result:
                            jump .tits
                        else:
                            jump .fail
                    "Сними верх!" ('soc', mgg.social * 2, 90):
                        if rand_result:
                            jump .toples
                        else:
                            jump .fail
                    "А, ничего. Так поймаю..." if not _in_replay:
                        $ mood += 100
                        $ infl[alice].add_m(20)
                        jump .spider
            "А что мне за это будет?" if toples:
                # Алиса без лифчика
                $ var_pose, var_pose2 = '04', '02'
                Alice_06 "Макс, не наглей! Я и так перед тобой тут в одних трусиках... Тебе этого мало что ли?!"
                Max_07 "Ну, я вижу, что условия нашей договорённости ты соблюдаешь, только вот к поимке паука это никак не относится."
                Alice_12 "И чего тебе, в таком случае, ещё от меня надо?"
                Max_01 "Видишь ли, глаза совсем заспанные, никак не могу разглядеть паука... Но думаю твои прекрасные сосочки мне с этим помогут!"
                menu:
                    Alice_15 "Ах, так! Значит то, что договорённость я соблюдаю, ты видишь, а вот здоровенного паука на моей кровати нет?!"
                    "На красивое глаза легче открываются..." ('soc', mgg.social * 2, 90):
                        if rand_result:
                            jump .toples
                        else:
                            jump .fail
                    "Давай уже показывай сиськи!" if not _in_replay:
                        jump .fail
                jump .spider
            "А что мне за это будет?" if naked:
                # Алиса голая
                $ var_pose, var_pose2 = '04', '02'
                menu:
                    Alice_12 "Что ты хочешь за смерть этого паука?"
                    "Покажи сиськи!":
                        # spider-night-03-alice-(10b/11b/12b)
                        $ var_pose, var_pose2 = random_choice(['10', '11', '12']), '03'
                        if alice.GetMood()[0] < 3:
                            $ mood -= 50
                        Alice_09 "Ах! Ну и хам же ты, Макс... Ладно, любуйся, я сегодня добрая. И убей его уже, наконец!"
                        Max_04 "Сиськи - что надо! Ладно, где этот твой паук..."
                    "Не прикрывайся руками!":
                        Alice_06 "В смысле не прикрывайся руками?! Совсем что ли обнаглел! Я и так перед тобой тут голая стою, рук всё прикрыть не хватает... Тебе этого мало что ли?!"
                        Max_02 "Без рук будет поинтереснее!"
                        Alice_17 "Да я сама тебя сейчас без рук оставлю! Тебя-то я не боюсь! Быстро убил его! Или он, или ты. Кто-то из вас умрёт сегодня!"
                        Max_08 "Ух, какая ты кровожадная. Ну ладно..."
                    "А, ничего. Так поймаю..." if not _in_replay:
                        $ mood += 100
                        $ infl[alice].add_m(20)
                jump .spider
            "Хорошо, где он там..." if not alice.req.noted and not _in_replay:
                $ mood += 100
                $ infl[alice].add_m(20)
                jump .spider
            "Паука-то я поймаю, только вот кое-кто нарушает уговор! Или может я не прав?!" if alice.req.noted:
                $ var_pose = '04'
                if alice.req.result == 'not_sleep':
                    # Алиса должна спать без лифчика
                    Alice_12 "Ну забыла я снять лифчик перед сном, просто по привычке... Подумаешь, какое большое преступление!"
                    Max_09 "Конечно большое! Ты просто наплевала на наш уговор, а я ведь твою задницу спас от маминой хлёсткой руки... Я его тоже тогда соблюдать не стану, так что завтра получишь! Приятных снов..."
                    Alice_14 "Нет, нет, нет! Ты куда собрался?! У меня же паук на кровати!"
                    Max_07 "Что тут скажешь... Успехов тебе!"
                    Alice_06 "Ну не надо так, Макс! Я не буду больше нарушать наш уговор, только избавься от паука... Пожалуйста!"

                elif alice.req.result == 'not_naked':
                    # Алиса должна спать голой
                    Alice_12 "Серьёзно, Макс?! Может я оделась и прибежала! Как тебе такое, а?"
                    $ var_pose2 = '02'
                    Max_09 "Что я тебя, не знаю что ли! Ты так боишься пауков, что одежда - это последнее, о чём ты вспомнишь увидя их. Ты просто наплевала на наш уговор, а я ведь твою задницу спас от маминой хлёсткой руки... Я его тоже тогда соблюдать не стану, так что завтра получишь! Приятных снов..."
                    Alice_14 "Нет, нет, нет! Ты куда собрался?! У меня же паук на кровати!"
                    Max_07 "Что тут скажешь... Успехов тебе!"
                    menu:
                        Alice_06 "Ну не надо так, Макс! Я не буду больше нарушать наш уговор, только избавься от паука... Пожалуйста!"
                        "Раздевайся!":
                            Alice_13 "Какой же ты извращенец, Макс! Не стыдно тебе такое просить?!"
                            Max_01 "Сама виновата! Я с тобой по хорошему хотел... Не спускать же тебе это теперь с рук?!"
                            # spider-night-03-alice-04d
                            $ var_pose, var_pose2, var_dress = '04', '03', 'n'
                            menu:
                                Alice_06 "Ну вот... разделась... И не говори, что этого мало... Я и так перед тобой тут голая стою, рук всё прикрыть не хватает... Доволен?"
                                "Сиськи ещё покажи...":
                                    # spider-night-03-alice-(10b/11b/12b)
                                    $ var_pose = random_choice(['10', '11', '12'])
                                    Alice_14 "Ах! Ну ты хам... Ладно, смотри быстро. И убей его уже, наконец!"
                                    Max_04 "Сиськи - что надо! Ладно, где этот твой паук..."
                                "О да, я очень доволен!":
                                    Alice_12 "Вот и хватит глазеть! Давай уже, лови этого паука!"
                                    Max_04 "Классная у тебя фигура, сестрёнка! Особенно когда ты голенькая. Ну да ладно, теперь можно и поймать..."

                    $ alice.dcv.prudence.set_lost(random_randint(3, 7))
                    $ alice.req.result = alice.req.req
                    $ alice.req.noted = False
                    $ alice.sleepnaked = True
                    $ alice.dress = ''
                    $ suf = 'n'
                    $ naked = True
                    jump .spider

                else:
                    # Алиса должна днем ходить без трусов
                    Alice_06 "О чём это ты говоришь, Макс?"
                    Max_08 "Мы ведь договорились, что ты не будешь одевать трусы днём. А я их на тебе видел!"
                    Alice_14 "А мне вот интересно, когда это ты их мог увидеть?! Подглядывал, как я одеваюсь?"
                    Max_07 "Как будто это нужно?! Они у тебя иногда прямо из-под джинс слегка торчат... Так что важно не то, как и где я это увидел, а то, что они на тебе были!"
                    Alice_00 "Ладно, ладно, признаю, они были сегодня на мне, потому что без них мне всё натирает."
                    Max_09 "То есть ты просто наплевала на наш уговор?! А я ведь твою задницу спас от маминой хлёсткой руки... Я его тоже тогда соблюдать не стану, так что завтра получишь! Приятных снов..."
                    Alice_14 "Эй, ты куда это собрался?! У меня же паук здоровенный на кровати!"
                    Max_07 "Что тут скажешь... Развлекайся!"
                    Alice_06 "Ну не уходи, Макс! Я не буду больше нарушать наш уговор, только избавься от этого паука... Ну пожалуйста!"

                Max_09 "Вот и хорошо, что не будешь! А за сегодняшнее нарушение ты покажешь мне свою попку, если хочешь, чтобы я убрал паука... Не зря же я её спас от наказания?!"
                Alice_13 "Какой же ты извращенец, Макс! Не стыдно тебе такое просить?!"
                Max_01 "Сама виновата! Я с тобой по хорошему хотел... Не спускать же тебе это теперь с рук?!"
                $ var_stage, var_pose = '05', random_choice(['01', '02', '03'])
                scene alice_wakes_max_up
                Alice_06 "Ну вот... смотри... И не говори, что этого мало... большего не покажу! Доволен?"
                Max_05 "О да, я очень доволен! Попка у тебя просто супер, сестрёнка!"
                Alice_12 "Всё! Посмотрел и хватит, давай уже, лови этого паука!"
                Max_04 "Ладно, теперь можно и поймать..."

                $ alice.dcv.prudence.set_lost(random_randint(3, 7))
                $ alice.req.result = alice.req.req
                $ alice.req.noted = False
                if alice.req.req == 'nopants':
                    $ alice.nopants = True
                elif alice.req.req == 'sleep':
                    $ alice.sleeptoples = True
                    $ alice.dress = alice.dress[:1]+'a'
                jump .spider

    label .fail:
        $ var_pose = '05'
        Alice_17 "[failed!t]Что?! Да я сама тебя сейчас придушу! Тебя-то я не боюсь! Быстро убил его! Или он, или ты. Кто-то из вас умрёт сегодня!"
        Max_08 "Ух, какая ты кровожадная. Ну ладно..."
        $ mood -= 100
        jump .spider

    label .money:
        $ var_pose = '06'
        Alice_16 "[succes!t]Ну ты и хам, Макс! Ладно, держи $10, только убей его, быстрее!!!"
        Max_04 "Деньги всегда пригодятся! Ладно, где этот твой паук..."
        $ mood -= 20
        $ mgg.ask(0)
        jump .spider

    label .tits:
        $ var_pose2 = '03'
        if alice.GetMood()[0] < 3:
            $ mood -= 50
            $ var_pose = random_choice(['07', '08'])
            Alice_14 "[succes!t]Ах! Ну ты хам... Ладно, смотри быстро. И убей его уже, наконец!"
        else:
            $ var_pose = '09'
            Alice_09 "[succes!t]Ах! Ну и хам же ты, Макс... Ладно, любуйся, я сегодня добрая. И убей его уже, наконец!"
        Max_04 "Сиськи - что надо! Ладно, где этот твой паук..."
        jump .spider

    label .toples:
        if not toples:
            $ toples = True
            $ suf += 't'
            $ var_dress += 't'
        $ var_pose2, var_pose = '03', random_choice(['10', '11', '12'])
        if alice.GetMood()[0] < 3:
            $ mood -= 50
        Alice_15 "[succes!t]Ах! Ну ты хам... Ладно... Ну что, доволен, извращенец? А теперь иди, убей его уже, наконец!"
        Max_05 "Отличные сиськи! Ладно, где этот твой паук..."
        jump .spider

    label .spider:
        $ var_pose = random_choice(['04', '05', '06']) if toples else random_choice(['01', '02', '03'])
        $ var_stage, var_pose2 = '04', '01'
        scene alice_wakes_max_up mgg
        if alice.dress == 'a':
            show screen Cookies_Button
        menu:
            Max_07 "Ага, попался! Пожалуй, вот что я сделаю..."
            "{i}оставлю этого паука себе{/i}" if not all([alice.dcv.mistress.stage > 3, alice.flags.sober_fj, alice.flags.touched, alice.dcv.intrusion.stage in [5, 7]]):
                menu:
                    Alice_16 "Макс! Ты должен его убить! А не то я подумаю, что это твоих рук дело... Докажи, что это был не ты!"
                    "Я не буду его убивать!":
                        menu:
                            Alice_17 "Ах так... Ну, тогда я обижусь на тебя! Всё, вали отсюда!"
                            "{i}вернуться в кровать{/i}":
                                hide screen Cookies_Button
                                $ renpy.end_replay()
                                $ mood -= 100
                                $ spent_time = 30
                                $ AddRelMood('alice', 0, mood)
                                $ SpiderKill = 0
                                $ SpiderResp = 0
                                $ items['spider'].have = True
                                return
                    "Пусть живёт. Я пойду и выкину его с балкона за ограду, чтобы он обратно не приполз." ('soc', mgg.social * 3, 90):
                        $ var_pose2 = '02'
                        if rand_result:
                            Alice_12 "[succes!t]Ладно, Макс, уговорил. Только сделай так, чтобы его и близко к этому дому не было..."
                            menu:
                                Alice_13 "Всё, хватит уже сидеть на моей кровати, иди отсюда. Я хочу спать!"
                                "{i}вернуться в кровать{/i}":
                                    hide screen Cookies_Button
                                    $ renpy.end_replay()
                                    $ mood += 50
                                    $ spent_time = 30
                                    $ AddRelMood('alice', 0, mood)
                                    $ SpiderKill = 0
                                    $ SpiderResp = 0
                                    $ items['spider'].have = True
                                    return
                        else:
                            $ mood -50
                            Alice_16 "[failed!t]Нет уж, Макс! Ты его убиваешь прямо здесь и сейчас или я сильно на тебя обижусь! Выбирай..."
                            Max_09 "Ладно, будет тебе! Раз ты такая кровожадная..."
                            jump .kill
                    "{i}выбросить с балкона{/i}":
                        jump .let_go
                    "{i}убить паука{/i}":
                        jump .kill
            "{i}выброшу этого паука с балкона{/i}":
                jump .let_go
            "{i}убью этого паука{/i}" if not all([alice.dcv.mistress.stage > 3, alice.flags.sober_fj, alice.flags.touched, alice.dcv.intrusion.stage in [5, 7]]):
                jump .kill
    label .let_go:
        hide screen Cookies_Button
        scene BG char Alice spider-balcony
        pause
        if alice.sleepnaked:
            $ var_dress = 'n'
        elif alice.sleeptoples:
            $ var_dress = alice.dress[:1] + 't'
        else:
            $ var_dress = alice.dress[:1]

        $ var_stage, var_pose, var_pose2 = '03', '04', '02'
        scene alice_wakes_max_up mgg
        $ SpiderKill = 0
        $ SpiderResp = 1

        if all([alice.dcv.mistress.stage > 3, alice.flags.sober_fj, alice.flags.touched, alice.dcv.intrusion.stage in [5, 7]]):
            # - успешно пройдено доминирование Алисы с конфетой
            # - получен трезвый fj перед ТВ
            # - пройдены "прятки" от паука (а значит, Макс опередил Эрика с боди)
            if not alice.flags.together_sleep:
                # (1-ый раз)
                jump ev_v92_004
            elif alice.flags.together_sleep < 2:
                jump ev_v92_005
            elif alice.flags.together_sleep < 3:
                jump ev_v92_006
            elif alice.flags.together_sleep < 4:
                jump ev_v92_007

        menu:
            Alice_13 "Макс! Я тебя просила убить его, а не отпускать! Спасибо, конечно, что убрал его из комнаты, но вдруг он вернётся?.. Всё, иди отсюда. Я хочу спать!"
            "{i}вернуться в кровать{/i}":
                $ renpy.end_replay()
                $ spent_time = 30
                $ mood -= 50
                $ AddRelMood('alice', 0, mood)
                return

    label .kill:
        hide screen Cookies_Button
        # show Max spider-night 04-03
        $ var_pose2 = '03'
        menu:
            Alice_01 "Так ему! Спасибо, Макс! Ты мой спаситель. А теперь иди отсюда, я спать хочу!"
            "{i}вернуться в кровать{/i}":
                $ renpy.end_replay()
                $ mood += 100
                $ AddRelMood('alice', 0, mood)
                $ spent_time = 30
                $ SpiderKill = 2
                $ SpiderResp = 3
                return


label alice_smoke:

    if all([not alice.daily.smoke, alice.dcv.revenge.enabled]):
        # Макс сегодня ещё не видел курящую Алису, за последний куни ещё не отомстил
        $ chance = 100
        if alice.dcv.revenge.lost:
            $ chance /= 2 * alice.dcv.revenge.lost
        if random_outcome(chance):
            scene BG char Alice smoke
            $ renpy.show('Alice smoke '+pose3_3+alice.dress)
            $ persone_button1 = 'Alice smoke '+pose3_3+alice.dress
            Max_02 "Ну вот, Алиса, ты и попалась! Видимо, уже невмоготу стало, как курить захотелось..."
            $ alice.dcv.revenge.disable()
        else:
            call alice_swim from _call_alice_swim
            Max_09 "Странно, Алиса в это время обычно курит... Она решила бросить, что ли?"
            $ alice.daily.smoke = 1
            return

    elif alice.dcv.revenge.enabled:
        # за последний куни ещё не отомстил
        call alice_swim from _call_alice_swim_1
        return

    scene BG char Alice smoke
    if alice.daily.smoke:
        $ renpy.show('Alice smoke '+pose3_3+alice.dress)
        $ persone_button1 = 'Alice smoke '+pose3_3+alice.dress
        return
    else:
        $ renpy.show('Alice smoke '+pose3_3+alice.dress)
        # with fade4

    $ alice.daily.smoke = 1
    $ alice.prev_plan = alice.plan_name

    if alice.dcv.special.done:
        if alice.dcv.special.stage == 0:
            jump first_talk_smoke  # первый разговор про курение
        elif alice.dcv.special.stage == 1:
            jump second_talk_smoke  # второй разговор про курение
        elif alice.flags.pun == 0:
            jump smoke_nofear  # разговор во время курения до наказаний
        else:
            if all([alice.flags.private, alice.dcv.private.stage==4, not alice.dcv.private.done]):
                # доступно первое приватное наказание. Отменяем все прочие договорённости
                $ alice.req.reset()
                jump alice_private_punish_0.smoke

            if flags.eric_wallet == 2 and flags.eric_photo1:
                jump smoke_after_wallet

            if alice.flags.shower_max > 2:
                # после 3-его совместного принятия душа Алисы и Макса
                if alice.req.result == 'bikini':
                    jump ev_v92_013
                elif alice.req.result == 'naked':
                    jump ev_v92_014
                else:
                    jump ev_v92_012

            if alice.req.result is None:
                # нет текущих требований
                jump smoke_fear
            elif alice.req.result == 'toples':
                # текущее требование курить топлес. Выполняется
                jump smoke_toples
            elif alice.req.result == 'not_toples':
                #  текущее требование курить топлес. Не выполняется
                jump smoke_not_toples
            elif alice.req.result == 'sleep' or alice.req.result == 'not_sleep':
                # текущее требование спать топлес.
                # если Макс знает о нарушениях, решает все через паука.
                jump smoke_sleep
            elif alice.req.result == 'naked' or alice.req.result == 'not_naked':
                # текущее требование спать голой.
                # если Макс знает о нарушениях, решает все через паука.
                jump smoke_sleep
            elif alice.req.result == 'nopants' or (alice.req.result == 'not_nopants' and not alice.req.noted):
                # текущее требование ходить днем без трусов. Выполняется или Макс не знает о нарушении
                jump smoke_nopants
            elif alice.req.result == 'not_nopants' and alice.req.noted:
                # текущее требование ходить днем без трусов. Не выполняется
                jump smoke_not_nopants
            elif alice.req.result == 'nojeans':
                # текущее требование ходить без джинсов, когда Ани нет дома
                jump smoke_nojeans

    return


#  Алиса перед зеркалом ванной
label alice_after_club:
    scene location house bathroom door-evening
    if alice.daily.bath != 0:
        return

    $ alice.daily.bath = 1
    if tm[-2:] > '10':
        Max_07 "{m}После клуба Алиса сразу пошла в ванную. Интересно, в каком она состоянии?{/m}" nointeract
    else:
        Max_07 "{m}Алиса только что вернулась из клуба и сразу забежала в ванную. Интересно, в каком она состоянии?{/m}" nointeract

    menu:
        "{i}постучаться{/i}":
            if alice.daily.drink and tm[-2:] <= '10':
                jump .knock
            else:
                menu:
                    Alice "{b}Алиса:{/b} Кому там не спится? Я ванну набираю..."
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Макс, ты глухой? Я же сказала, буду в ванне плескаться. Жди как минимум час!"
                        Max_10 "Ладно, ладно..."
                    "{i}уйти{/i}":
                        pass
        "{i}заглянуть со двора{/i}" if flags.ladder < 2:
            scene Alice bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "{m}Эх! Не повезло... Алиса уже плюхнулась принимать ванну. Отсюда я уже ничего увидеть не смогу...{/m}"
        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "{m}Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное...{/m}"
            $ flags.ladder = 3
            $ items['ladder'].give()
            jump alice_bath.ladder
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump alice_bath.ladder
        "{i}уйти{/i}":
            pass
    jump .end

    label .knock:
        $ alice.dress_inf = '04da' if alice.req.result == 'nopants' else '04ca'
        # after-club-01 + after-club-01-alice-(01/02/03)(/a)+ after-club-01-max-01
        $ var_pose, var_pose2, var_dress = random_choice(['01', '02', '03']), '01', 'a' if alice.req.result == 'nopants' else ''
        scene alice_bath_mirror with fade4
        Alice_05 "А, Макс... Не спится? Чего хотел?"
        Max_01 "Да... Я вот... Умыться перед сном хотел!"
        Alice_03 "Ну, проходи. Я собиралась ванну принять, но ещё вода набирается..."
        Max_04 "Как в клубе повеселилась?"
        Alice_04 "Ты знаешь, очень... очень хорошо. Я обычно не пью, но в этот раз что-то потянуло и... всё прошло просто чудесно! А у тебя как дела?"
        Max_07 "Ого. Тебе и правда интересно?"
        Alice_05 "Конечно! Ты же мой брат. Ты извини, если я с тобой бываю груба. Это просто защитная реакция..."
        Max_09 "Защитная реакция?"
        Alice_04 "Тебе не понять... Ты знаешь, я бы хотела извиниться, если тебя чем-то обижала в последнее время... Ой, у тебя что-то в штанах шевелится..."

        # after-club-01 + after-club-01-alice-(01/02/03)(/a)+ after-club-01-max-02
        $ var_pose2 = '02'
        Max_07 "Э... Ты точно в порядке?"
        menu:
            Alice_07 "Ага. И ты, я вижу, тоже... Какой же он у тебя большой..."
            "У тебя... Очень красивая грудь...":
                if not _in_replay:
                    if alice.flags.incident < 1:
                        $ alice.flags.incident = 3 if alice.req.result == 'nopants' else 1
                    $ poss['nightclub'].open(8)
                # after-club-01 + after-club-01-alice-(04/05/06)(/a)+ after-club-01-max-02
                $ var_pose = {'01':'04', '02':'05', '03':'06'}[var_pose]
                Alice_04 "Спасибо, Макс. Девушке очень приятно такое слышать от парня. Даже, если это её младший брат... которого ей хочется подразнить..."

                if alice.req.result == 'not_nopants':
                    # Алиса нарушила уговор по трусикам
                    Max_09 "А почему на тебе трусики?"
                    Alice_05 "Какой ужас! Похоже, я нарушила наш уговор... или нет... Разве я не могу носить их ночью?"
                    Max_07 "Когда спишь - да, а вот всё остальное время - нет!"
                    Alice_03 "Ну что ж, значит на мне есть кое-что лишнее... Это можно легко исправить..."

                    # after-club-01 + after-club-01-alice-(04b/05b/06b)+ after-club-01-max-02
                    $ var_dress = 'b'
                    Alice_07 "Вот... Теперь всё так, как должно быть. И твоему дружку явно стало очень тесно в трусах, да?"

                elif alice.req.result == 'nopants':
                    # Алиса без трусиков
                    if not _in_replay:
                        if alice.flags.incident == 2:
                            $ alice.flags.incident = 4
                    Max_04 "Да, эти сосочки выглядят очень соблазнительно... Но чтобы меня подразнить, нужно показать куда больше..."

                    # after-club-01 + after-club-01-alice-(04b/05b/06b)+ after-club-01-max-02
                    $ var_dress = 'b'
                    Alice_07 "Например, так? Да, я вижу твой дружок запульсировал ещё сильнее... Это так возбуждает!"

                Max_03 "А ты не хочешь мне помочь?"
                if 'black_linderie' in alice.gifts:
                    # если подарен комплект тёмного белья для блога
                    jump .next1

            "А ты не хочешь мне помочь?" if not _in_replay:
                pass
        menu:
            Alice_05 "Ты знаешь... Я ещё не настолько пьяна и, кажется, меня уже отпускает. Так что... Придётся тебе самому разбираться с твоей проблемой... А у меня набралась ванна. Так что..."
            "Ну Алиса... Ну чуть-чуть...":
                Alice_04 "Макс... Ты же не хочешь, чтобы я рассказала маме, что ты ко мне приставал?"
                Max_00 "Всё понял, ухожу..."

            "Хорошо. Спокойной ночи, Алиса...":
                pass

        $ renpy.end_replay()
        ### здесь ставим флаг разговора в ванной, продвижение возможности тусовщица
        $ spent_time += 10
        $ poss['nightclub'].open(7)
        jump .end

    label .next1:   # подарен комплект тёмного белья для блога
        if _in_replay:
            $ var_dress = 'a' if alice.req.result else ''
        $ spent_time += 10

        # after-club-02 + after-club-02-max-01-alice-(01/01a)
        $ var_stage, var_pose = '02', '01'
        if var_dress > 'a':
            $ var_dress = 'a'
        scene alice_bath_mirror_01
        Alice_13 "Может и хочу! Я ведь была очень плохой девочкой... Ты помогаешь мне с блогом, купил классное нижнее бельё, балуешь сладостями... а я только угрозами в тебя сыплю..."
        Max_01 "Не только... С тобой бывают светлые моменты!"
        menu:
            Alice_08 "Сейчас их может стать на один больше! Что ты хочешь, чтобы я сделала?"
            "Хочу, чтобы ты сняла трусики..." if var_dress != 'a':   #если на Алисе есть трусики

                # after-club-02 + after-club-02-max-01-alice-01a
                $ var_dress = 'a'
                Alice_05 "Какие у тебя скромные желания, Макс! Всего лишь раздеть свою старшую сестру..."
                Max_02 "На тебе ещё есть халат, так что ты точно не раздетая!"
                menu:
                    Alice_04 "Неужели это всё, чего ты хотел?"
                    "Хочу, чтобы ты поласкала его...":
                        jump .caress

                    "Хочу, чтобы ты отсосала..." if not _in_replay:
                        jump .suck

            "Хочу, чтобы ты поласкала его...":
                jump .caress

            "Хочу, чтобы ты отсосала..." if not _in_replay:
                jump .suck

    label .caress:
        # after-club-02 + after-club-02-max-02-alice-(02/02a)
        $ var_pose = '02'
        # scene alice_bath_mirror_01
        $ spent_time += 10
        if not _in_replay:
            $ poss['nightclub'].open(9)

        Alice_09 "Ого... Я даже не могу обхватить его всей рукой! Ты ведь давно об этом мечтал, да Макс?"
        Max_04 "Может быть..."
        Alice_07 "Наверняка, ты много раз фантазировал, как я буду чувственно дрочить его своими нежными руками... Ну и как, Макс, приятно?"
        Max_05 "О да! Намного приятнее, чем фантазировать об этом..."
        menu:
            Alice_05 "Не сомневаюсь. Ванна почти наполнилась водой, так что мы можем быстренько успеть что-то ещё! Но осторожнее с желаниями..."
            "Хочу показать тебе, как я научился целоваться..." if lisa.dcv.seduce.stage>3:   #если пройдены уроки поцелуев с Кирой

                # after-club-03 + after-club-03-max-02-alice-(02/02a)
                $ var_stage = '03'
                Alice_03 "Да ладно! Где это ты успел? Ты же дома больше меня сидишь. Не верю я тебе..."
                menu:
                    Max_03 "А ты попробуй!"
                    "{i}целовать Алису{/i}":
                        if not _in_replay:
                            $ poss['nightclub'].open(10)

                # after-club-03 + after-club-03-max-01-alice-(01/01a)
                $ var_pose = '01'
                menu:
                    Max_02 "{m}А Алиса хорошо целуется! Да со страстью, увлечённо... Ммм... Губки у неё сочные... А уж как в член мой вцепилась!{/m}"
                    "{i}закончить целоваться{/i}":
                        pass
                    "{i}прикоснуться к её груди{/i}" if all([alice.dcv.intrusion.stage in [5, 7], var_dress=='a', alice.daily.drink>1, alice.flags.hip_mass<5]):  # Макс подарил Алисе кружевное боди, две конфетки, пьяный путь
                        jump .next2
                    "{i}прикоснуться к её груди{/i}" if all([alice.dcv.intrusion.stage in [5, 7], var_dress=='a', alice.flags.hip_mass>4]):  # Макс подарил Алисе кружевное боди, пройден "трезвый путь"
                        jump .next2

                # after-club-03 + after-club-03-max-02-alice-(02/02a)
                $ var_pose = '02'

                Alice_09 "Нифига себе! Ты и этому что ли на интернет-курсах научился? Не может быть такого..."
                Max_04 "А вот теперь ванну принимай и гадай, как я научился."
                Alice_02 "Ой, уже наполнилась! А это значит что? Правильно, спокойной ночи!"
                Max_01 "Ага. Приятных снов, Алиса."

            "А если бы я был твоим парнем... Что бы ты сделала дальше?" if alice.flags.hip_mass>1:   #если Макс ласкал Алисе киску у ТВ

                # after-club-03 + after-club-03-max-02-alice-(02/02a)
                $ var_stage = '03'
                Alice_07 "Ха! Кое-чего ты обо мне не знаешь, Макс... Я предпочитаю девушек... Но не откажусь от парня, если у него есть что-то... особенное..."
                Max_03 "Как удачно, что ты как раз держишь в руке кое-что особенное!"

                # after-club-03 + after-club-03-max-03-alice-(03/03a)
                $ var_pose = '03'

                Alice_04 "Да... И я бы, пожалуй, сняла с себя халат, пока ласкала его член... Чтобы ничто не мешало ему наслаждаться моим совершенно голым телом!"
                if var_dress:
                    Max_05 "Правильно, Алиса... Такое шикарное тело лучше не скрывать! А потом?"   #если Алиса без трусиков
                else:
                    Max_05 "ПОЧТИ голым телом, но это мелочи... Мне нравится к чему всё идёт! А потом?"   #если Алиса в трусиках

                # after-club-04 + after-club-04-max-01-alice-(01/01a)
                $ var_stage, var_pose = '04', '01'
                Alice_08 "А потом я бы опустилась на колени и начала водить его членом по своему лицу... неспеша и слегка задевая губами..."
                Max_20 "Ох, чёрт! А потом..."

                # after-club-03 + after-club-03-max-04-alice-04a
                $ var_stage, var_pose = '03', '04'
                Alice_05 "У меня ванна набралась, так что спокойной ночи!"
                Max_10 "Да ладно, Алиса! Это слишком жёсткий облом!"
                Alice_04 "Макс... Ты же не хочешь, чтобы я рассказала маме, что ты ко мне приставал?"
                Max_00 "Всё понял, ухожу..."

            "Хочу, чтобы ты отсосала..." if not _in_replay:
                jump .suck

            "На всё остальное ты не согласишься..." if not _in_replay:
                Alice_07 "Думаешь? Как знать... Но в любом случае уже поздно, а мне ещё ванну принимать, так что спокойной ночи, Макс."
                Max_01 "Ага. Приятных снов, Алиса."

        jump .end

    label .next2:   # после поцелуя прикоснулся к груди + Макс дарил Алисе кружевное боди
        if not _in_replay:
            $ poss['nightclub'].open(11)

        # after-club-03 + after-club-03-max-06-alice-06a
        $ var_stage, var_pose, var_dress = '03', '06', 'a'
        scene alice_bath_mirror_01
        Max_04 "{m}Ох, какая у неё нежная и упругая грудь! Ухх.. Она ещё активнее начала мне дрочить, а это означает, что ей нравится, как я мну её сиськи! Может даже удастся зайти ещё дальше...{/m}"

        # after-club-03 + after-club-03-max-05-alice-05a
        $ var_pose = '05'
        Alice_09 "Ах, Макс! И где ты такому научился?! У меня теперь сосочки изнывают от возбуждения! А как жарко стало..."
        Max_03 "Сними халатик и я покажу, что ещё умею..."

        # after-club-05 + after-club-05-max&alice-01
        $ var_stage, var_pose = '05', '01'
        scene alice_bath_mirror_02
        Alice_06 "Ммм... Макс... Ну вот что ты делаешь?! Я же твоя сестра, а ты... ведёшь себя со мной... как будто я твоя девушка..."
        Max_07 "Так почему бы тебе не представить ненадолго, что я твой парень?"
        menu:
            Alice_07 "Ты должно быть не в курсе, но я предпочитаю девушек... Но для парня, у которого есть кое-что особенное, я не прочь сделать исключение, ради любопытства..."
            "{i}ласкать её киску рукой{/i}":
                # after-club-05 + after-club-05-max&alice-02
                # after-club-06 + after-club-06-max&alice-01
                $ var_stage, var_pose = random_choice([('05', '02'), ('06', '01')])
                Alice_15 "Макс! Ахх... Ты полез рукой прямо туда... Это же так..."
                Max_02 "Приятно? Это ты хотела сказать?"
                menu:
                    Alice_06 "Д-а-а... То есть, я хотела сказать... неправильно! Но к чёрту, продолжай... Мне нравится, как ты это делаешь, ммм..."
                    "{i}проникнуть в её киску пальцами{/i}" ('sex', (10 + mgg.sex) * 4, 90):
                        if rand_result:
                            # (Ей нравится!)
                            # after-club-06 + after-club-06-max&alice-02
                            $ var_stage, var_pose = '06', '02'
                            Alice_10 "[like!t]Ах! Вот чёрт, Макс! Да-а-а... это так классно... быстрее... Как же меня возбуждает твой огромный член!"
                            menu:
                                Max_04 "{m}Алиса так приятно постанывает... А уж мне не менее приятно трахать эту нежную киску пальцами. Может быть, она даже кончит, если я ускорюсь...{/m}"
                                "{i}ускориться{/i}" ('sex', (10 + mgg.sex) * 3, 90):
                                    jump .fast_fingers

                                "{i}ласкать её киску языком{/i}" ('sex', (10 + mgg.sex) * 4, 90):
                                    jump .cunnilingus
                        else:
                            # (Ей не нравится!)
                            jump .dont_like

                    "{i}ласкать её киску языком{/i}" ('sex', (10 + mgg.sex) * 4, 90):
                        jump .cunnilingus

    label .fast_fingers:
        if rand_result:
            # (Ей нравится!)
            Alice_11 "[like!t]Да, Макс, да! Я кончаю... загони свои шаловливые пальчики поглубже... да... Ох... Класс! А ты скоро кончишь?"
            Max_02 "Для этого тебе придётся очень постараться..."

            # after-club-04 + after-club-04-max-01-alice-01a
            $ var_stage, var_pose, var_dress = '04', '01', 'a'
            scene alice_bath_mirror_01
            Alice_08 "Если я кончила, то и мой парень должен кончить... Только так и не иначе! Хочешь узнать, на что мой язычок способен?"
            Max_01 "Жду не дождусь, Алиса!"

            # after-club-04 + after-club-04-max&alice-01
            # after-club-08 + after-club-08-max&alice-bj01
            $ var_stage, var_pose = random_choice(['04', '08']), '01'
            if var_stage == '04':
                scene alice_bath_mirror_02
            else:
                scene alice_bath_mirror_02 bj
            menu:
                Alice_07 "Ммм... Никогда бы не подумала, что буду вытворять такое с тобой! Ну и вымахал же у тебя такой член, Макс! Ты уже скоро?"
                "{i}кончить ей на лицо{/i}":
                    jump .cum_face

                "{i}кончить ей на грудь{/i}":
                    jump .cum_breast

                "Нет, я хочу ещё, но нужно поторопиться..." if all([alice.flags.touched, alice.flags.hip_mass > 4, alice.daily.drink>1]):
                    # пройден "трезвый" путь с фут-джобом у ТВ, Алисе дали вторую конфету после клуба
                    jump .need_hurry

                "Вообще-то, я надеялся, что ты возьмёшь его в рот..." if False:  #для версии 0.07
                    pass
        else:
            # (Ей не нравится!)
            jump .dont_like

    label .cunnilingus:
        if rand_result:
            #(Ей нравится!)
            # after-club-05 + after-club-05-max&alice-03
            # after-club-07 + after-club-07-max&alice-01
            $ var_stage, var_pose = random_choice([('05', '03'), ('07', '01')])
            scene alice_bath_mirror_02
            menu:
                Alice_09 "[like!t]Да, Макс, да! Я уже так близко... Не останавливайся... У тебя такой быстрый и ловкий язычок, Макс... Ммм..."
                "{i}ещё быстрее работать языком{/i}":
                    pass

            # after-club-05 + after-club-05-max&alice-04
            # after-club-07 + after-club-07-max&alice-02
            $ var_pose = '04' if var_stage == '05' else '02'
            Alice_11 "Ах! Я больше не могу, Макс... Кончаю! Да... Как же это было классно! Ох... А ты кончил?"
            Max_02 "А должен был?"

            # after-club-04 + after-club-04-max-01-alice-01a
            $ var_stage, var_pose, var_dress = '04', '01', 'a'
            scene alice_bath_mirror_01
            Alice_08 "Если я кончила, то и мой парень должен кончить... Только так и не иначе! Хочешь узнать, на что мой язычок способен?"
            Max_01 "Жду не дождусь, Алиса!"

            # after-club-04 + after-club-04-max&alice-01
            # after-club-08 + after-club-08-max&alice-bj01
            $ var_stage, var_pose = random_choice(['04', '08']), '01'
            if var_stage == '04':
                scene alice_bath_mirror_02
            else:
                scene alice_bath_mirror_02 bj
            menu:
                Alice_07 "Ммм... Никогда бы не подумала, что буду вытворять такое с тобой! Ну и вымахал же у тебя такой член, Макс! Ты уже скоро?"
                "{i}кончить ей на лицо{/i}":
                    jump .cum_face

                "{i}кончить ей на грудь{/i}":
                    jump .cum_breast

                "Нет, я хочу ещё, но нужно поторопиться..." if all([alice.flags.touched, alice.flags.hip_mass > 4, alice.daily.drink>1]):
                    # пройден "трезвый" путь с фут-джобом у ТВ, Алисе дали вторую конфету после клуба
                    jump .need_hurry

                "Вообще-то, я надеялся, что ты возьмёшь его в рот..." if False:  #для версии 0.07
                    pass
        else:
            #(Ей не нравится!)
            jump .dont_like

    label .need_hurry:
        # пройден "трезвый" путь с фут-джобом у ТВ
        # after-club-04 + after-club-04-max-01-alice-01a
        $ var_stage, var_pose, var_dress = '04', '01', 'a'
        scene alice_bath_mirror_01
        Alice_08 "В таком случае, я буду меньше говорить и больше делать... Тебе понравится!"
        if not _in_replay:
            $ poss['nightclub'].open(12)

        # after-club-09 + after-club-09-max&alice-bj02
        $ var_stage, var_pose = '09', '02'
        scene alice_bath_mirror_02 bj
        menu:
            Max_21 "Ох, Алиса, это мне очень нравится! Так приятно... Д-а-а... Давай ещё... Как же сладко твои сочные губки это делают, д-а-а..."
            "{i}сдерживаться{/i}" ('sex', (10 + mgg.sex) * 4, 90):
                if rand_result:
                    # (Удалось сдержаться!)
                    # after-club-08 + after-club-08-max&alice-bj02
                    $ var_stage = '08'
                    menu:
                        Max_22 "[restrain!t]Да, продолжай вот так! Давай быстрее, сестрёнка... Вижу, что с ним не просто справиться, но у тебя классно получается! Ещё немного... Я сейчас кончу..."
                        "{i}кончить ей на лицо{/i}":
                            jump .cum_face

                        "{i}кончить ей на грудь{/i}":
                            jump .cum_breast
                else:
                    # (Не удалось сдержаться!)
                    jump .no_restrain

    label .cum_breast:
        # after-club-08 + after-club-08-max&alice-cum02 + after-club-08-max&alice-(cum02a/cum02b)
        $ var_stage, var_pose, var_pose2 = '08', '02', random_choice(['a', 'b'])
        scene alice_bath_mirror_02 cum
        Alice_09 "Ого, сколько в тебе было... потенциала... Ты заляпал мне всю грудь! Теперь мыться надо..."
        Max_03 "А ты разве не для этого ванну собиралась принять?"
        Alice_06 "Да, точно... Ты же никому не проболтаешься о том, что тут было?"
        Max_02 "Где было? Что было? Не понимаю, о чём ты!"
        menu:
            Alice_05 "Вот именно, что ничего!"
            "{i}отправиться спать{/i}":
                jump .end

    label .cum_face:
        # after-club-09 + after-club-09-max&alice-cum01 + after-club-09-max&alice-(cum01a/cum01b)
        $ var_stage, var_pose, var_pose2 = '09', '01', random_choice(['a', 'b'])
        scene alice_bath_mirror_02 cum
        Alice_06 "Макс! Ну то за фигня! Ты кончил мне прямо на лицо!"
        Max_07 "А ты хотела как-то по-другому?"
        Alice_13 "Ну, предупредил бы хоть, чтобы в глаза не попало... Теперь мыться надо..."
        Max_03 "А ты разве не для этого ванну собиралась принять?"
        Alice_06 "Да, точно... Ты же никому не проболтаешься о том, что тут было?"
        Max_02 "Где было? Что было? Не понимаю, о чём ты!"
        menu:
            Alice_05 "Вот именно, что ничего!"
            "{i}отправиться спать{/i}":
                jump .end

    label .no_restrain:
        # after-club-09 + after-club-09-max&alice-cum01 + after-club-09-max&alice-(cum01a/cum01b)
        $ var_stage, var_pose, var_pose2 = '09', '01', random_choice(['a', 'b'])
        scene alice_bath_mirror_02 cum
        Alice_06 "[norestrain!t]Макс! Ну то за фигня! Ты кончил мне прямо на лицо!"
        Max_07 "А ты хотела как-то по-другому?"
        Alice_13 "Ну, предупредил бы хоть, чтобы в глаза не попало... Теперь мыться надо..."
        Max_03 "А ты разве не для этого ванну собиралась принять?"
        Alice_06 "Да, точно... Ты же никому не проболтаешься о том, что тут было?"
        Max_02 "Где было? Что было? Не понимаю, о чём ты!"
        menu:
            Alice_05 "Вот именно, что ничего!"
            "{i}отправиться спать{/i}":
                jump .end

    label .dont_like:
        # (Ей не нравится!)
        menu:
            Alice_13 "[dont_like!t]Ай, Макс! Ты слишком грубо это делаешь! Я люблю грубость, но не до такой же степени... Испортил ты всё! И вообще, у меня ванна набралась, так что спокойной ночи."
            "Я могу лучше...":
                Alice_04 "Макс... Ты же не хочешь, чтобы я рассказала маме, что ты ко мне приставал?"
                Max_00 "Всё понял, ухожу..."
            "Извини, я не хотел. Не обижайся...":
                pass
        jump .end

    label .suck:
        menu:
            Alice_13 "Какой ты грубый, Макс! Я люблю грубость, но не так сразу... Испортил ты всё! И вообще, у меня ванна набралась, так что спокойной ночи."
            "Ну Алиса... Ну чуть-чуть...":
                Alice_04 "Макс... Ты же не хочешь, чтобы я рассказала маме, что ты ко мне приставал?"
                Max_00 "Всё понял, ухожу..."
            "Хорошо. Спокойной ночи, Алиса...":
                pass
        jump .end

    label .end:
        $ renpy.end_replay()
        if check_is_home('kira'):
            $ current_room = house[0]
            jump Sleep

        $ spent_time += 10
        jump Waiting


label alice_lisa_shower:
    scene location house bathroom door-morning
    if lisa.daily.shower > 0:
        menu:
            Max_00 "{m}Сестрёнки принимают душ, не стоит им мешать...{/m}"
            "{i}уйти{/i}":
                return
    $ lisa.daily.shower = 1
    $ alice.prev_plan = alice.plan_name
    $ lisa.prev_plan = lisa.plan_name
    menu:
        Max_01 "{m}Интересно, кто сейчас в душе?{/m}"
        "{i}заглянуть со двора{/i}" if not flags.block_peeping:
            jump .start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump .ladder
        "{i}уйти{/i}":
            return

    label .ladder:
        # $ renpy.dynamic('r0', 'r1', 'vr')
        $ Skill('hide', 0.025, 10)
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "{m}Посмотрим, что у нас тут...{/m}"
        if 'alice_sh' in cam_flag:
            $ r0 = 1 if tm[-2:] < '30' else 2 # в первой половине часа перед зекралом Лиза
        elif 'lisa_sh' in cam_flag:
            $ r0 = 2 if tm[-2:] < '30' else 1 # в первой половине часа перед зекралом Алиса
        elif 'lisa_alice_sh' in cam_flag:
            $ r0 = 0 # $ vr = 'lisa_alice'
        else:
            $ r0 = random_randint(1, 4)
            if r0 < 3: # если выпал один персонаж
                $ vr = 'alice' if r0 == 1 else 'lisa'
                if vr == 'alice':
                    $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'alice_sh')
                else: # Алиса в душе, соответственно, перед умывальниками первые полчаса Лиза
                    $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'lisa_sh')
            # else:
            #     $ vr = 'lisa_alice'

        scene BG bathroom-morning-00
        if r0 == 1:
            if lisa.dress_inf != '04a': # Лизу уже видели через камеру
                $ r1 = {'04c':'a', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
            else:
                if tm[-2:] < '10'  and 'bathrobe' in lisa.gifts:
                    $ r1 = 'a'
                elif tm[-2:] < '20':
                    $ r1 = 'c'
                else:
                    $ r1 = 'd'
                $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[r1]

            $ renpy.show('Lisa bath-window-morning '+random_choice(['01', '02', '03'])+r1)
            show FG bathroom-morning-00
            if r1 == 'a':
                Max_03 "{m}Лиза смотрится в подаренном мною халатике очень соблазнительно... Особенно когда так хорошо видно её упругие сисечки, а за кадром ещё и Алиса принимает душ!{/m}"
            elif r1=='c':
                Max_07 "{m}Моя обворожительная сестрёнка в одних трусиках... Так и хочется зайти и стянуть их с её прекрасной попки, а за кадром ещё и Алиса принимает душ!{/m}"
            else:
                Max_06 "{m}Утро может быть действительно очень добрым, если удаётся полюбоваться совершенно голенькой Лизой, а за кадром ещё и Алиса принимает душ!{/m}"

        elif r0 == 2:
            if alice.dress_inf != '04aa': # Алису видели через камеру
                $ r1 = {'04ca':'a', '04da':'b', '02fa':'c', '00a':'d'}[alice.dress_inf]
            else:
                if tm[-2:] < '10':
                    $ r1 = 'a'
                elif tm[-2:] < '20':
                    $ r1 = 'c'
                else:
                    $ r1 = 'd'
                $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[r1]
            $ renpy.show('Alice bath-window-morning '+random_choice(['01', '02', '03'])+r1)
            show FG bathroom-morning-00
            if r1=='a':
                Max_02 "{m}Может Алиса и в халатике, но сиськи её видны просто замечательно, а за кадром ещё и Лиза принимает душ!{/m}"
            elif r1=='c':
                Max_04 "{m}Алиса сегодня без халатика... в одних трусиках... Гдядя на эту красоту, можно мечтать лишь об одном, а за кадром ещё и Лиза принимает душ!{/m}"
            else:
                Max_06 "{m}Алиса сегодня совершенно голая! И даже не представляет, что тем самым дарит мне возможность любоваться всеми её прелестями, а за кадром ещё и Лиза принимает душ!{/m}"

        else: # если девчонки перед зеркалом вдвоём, то они могут быть либо в трусиках, либо голыми
            $ r1 = 'd' if 'lisa_alice_sh' in cam_flag else random_choice(['c', 'd', 'c', 'd', 'c', 'd'])
            $ renpy.show('Alice bath-window-morning '+random_choice(['01', '02', '03'])+r1, at_list=[ladder_left_shift,])
            $ renpy.show('Lisa bath-window-morning '+random_choice(['01', '02', '03'])+r1, at_list=[ladder_right_shift,])
            show FG bathroom-morning-00
            if r1=='c':
                Max_05 "{m}Две мои сестрёнки красуются перед зеркалом в одних лишь трусиках! Такую прелесть редко можно увидеть...{/m}"
            else:
                $ alice.dress_inf = '00a'
                $ lisa.dress_inf = '00'
                Max_06 "{m}Да они же обе голенькие красуются перед зеркалом! Ох, сестрёнки, я бы вами целую вечность любовался...{/m}"

        Max_00 "{m}Ладно, хорошего понемногу, а то ещё заметит меня здесь кто-нибудь...{/m}"
        jump .end

    label .start_peeping:
        # $ renpy.dynamic('r1', 'r2')
        $ Skill('hide', 0.025, 10)

        scene Alice shower-Lisa 01
        $ renpy.show('FG shower 00'+mgg.dress)

        if flags.eric_wallet == 2:
            Max_09 "{m}Лучше вообще свести подглядывания к минимуму, пока я не избавлюсь от Эрика. Чтобы никого ещё больше не расстраивать...{/m}"
            menu:
                Max_01 "{m}Хорошо, что это не распространяется на Киру...{/m}"
                "{i}уйти{/i}":
                    $ flags.block_peeping = 1
                    jump .end

        menu:
            Max_07 "{m}Класс! Сегодня мои прекрасные сестрёнки принимают душ вместе... Красота!{/m}"
            "{i}продолжить смотреть{/i}":
                pass
            "{i}взглянуть со стороны{/i}":
                jump .alt_peepeng
            "{i}уйти{/i}":
                jump .end

        $ spent_time += 10
        $ r1 = random_randint(1, 6)
        $ r2 = random_randint(1, 6)
        scene BG bathroom-shower-01
        $ renpy.show('Alice shower-closer 0'+str(r2), at_list=[left_shift,])
        $ renpy.show('Lisa shower-closer 0'+str(r1), at_list=[right_shift,])
        show FG shower-closer
        Max_03 "{m}Да-а-а... Вот бы оказаться между двумя этими мокрыми попками... Я бы уж их помылил!{/m}"
        jump .end

    label .alt_peepeng:
        # $ renpy.dynamic('r1', 'r2')
        $ spent_time += 10
        $ alice.dress_inf = '00aa'
        $ lisa.dress_inf = '00a'
        $ r1 = random_randint(1, 6)
        $ r2 = random_randint(1, 6)
        scene BG bathroom-shower-03
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Lisa shower-alt 0'+str(r1), at_list=[alt_left_shift,])
        $ renpy.show('Alice shower-alt 0'+str(r2), at_list=[alt_right_shift,])
        show FG shower-water
        Max_03 "{m}Да-а-а... Вот бы оказаться между двумя этими мокрыми попками... Я бы уж их помылил!{/m}"
        jump .end

    label .end:
        $ current_room = house[6]
        $ spent_time += 10
        jump Waiting


label alice_blog_lingerie:
    if not alice.dcv.feature.done:
        call alice_rest_evening from _call_alice_rest_evening
        return

    $ renpy.scene()
    $ renpy.show('location house aliceroom door-'+get_time_of_day())
    if alice.daily.blog:
        return

    $ alice.daily.blog = 1
    $ alice.prev_plan = alice.plan_name
    menu:
        Max_00 "{m}Обычно в это время Алиса занимается своим блогом, но сейчас её дверь закрыта...{/m}"
        "{i}заглянуть в окно{/i}" if not flags.eric_wallet == 2:
            $ spent_time += 20
            scene BG char Alice blog-desk-01
            $ alice.dress_inf = {'a':'02', 'b':'02ia', 'c':'02ka', 'd':'02la'}[alice.dress]
            if any([
                    random_randint(1, 2) < 2,             # поза за столом
                    (_in_replay and items['sexbody1'].have),    # повтор и в сумке сексбоди
                    can_give_sexbody2(),                        # или можно подарить гружевное боди (не дожидаясь, когда выпадет поза за столом)
                ]):
                # Алиса сидит и спаливает Макса
                if alice.dcv.photo.stage > 0:
                    # blog-desk-01 + alice 02 + max 02
                    $ renpy.show('Alice blog 02'+alice.dress)
                    $ renpy.show('Max blog 02'+mgg.dress)
                    menu:
                        Alice_02 "О, Макс! Что-то хотел или просто проведать меня решил?"
                        "Я твои фотки принёс..." if all([alice.dcv.photo.stage==1, alice.dcv.photo.done]):
                            jump give_photos1
                        "Я тут не удержался и купил тебе боди раньше Эрика!" if can_give_sexbody2():
                            jump gift_lace_lingerie
                        "Отлично смотришься в этом белье!" if all([not _in_replay, alice.dcv.intrusion.enabled, not can_give_sexbody2()]):
                            # if alice.dcv.intrusion.lost<4 and alice.dcv.intrusion.stage<1:
                            if get_stage_sexbody2() == 2:
                                # Макс еще не знает о том, что Эрик собирается купить бельё Алисе
                                Alice_03 "Знаю, а в новом кружевном боди буду смотреться ещё лучше!"
                                Max_04 "Намёк понял. Купить на мой вкус?"
                                Alice_02 "Можешь не париться, Макс. Эрик купит то, что мне нужно."
                                Max_08 "Эрик купит тебе новое нижнее бельё?"
                                Alice_05 "Да, мне нужно ещё одно сексуальное боди. И я показала ему, какое конкретно хочу. Решили, что купим, когда поедем на шопинг в субботу. А что?"
                                Max_02 "Да так, интересно было, какое ты себе боди захотела. Покажешь?"
                                jump alice_showing_lingerie1
                            else:
                                Alice_03 "Знаю, но всё равно спасибо! Надеюсь, ты не станешь мешать, а то я тут немного занята..."
                                Max_04 "Не буду. Успехов тебе..."
                                menu:
                                    Alice_01 "Ага, хорошо бы."
                                    "{i}уйти{/i}":
                                        pass
                        "Как идут дела с блогом?" if all([not _in_replay, alice.dcv.other.done, alice.dcv.photo.stage>1, not can_give_sexbody2()]):  #после 1-ой фотосессии / откат 3 дня
                            $ alice.dcv.other.set_lost(3)

                            # if alice.dcv.battle.stage in [0, 2] and (alice.dcv.intrusion.lost>3 or not alice.dcv.intrusion.enabled):
                            if get_stage_sexbody2() < 2:
                                # Эрик ещё не помогает Алисе с блогом или уже изгнан
                                if random_randint(1, 2) < 2:
                                    Alice_03 "Неплохо. Развиваюсь понемногу. Подаренное тобой бельё зачастую сильно выручает!"
                                    Max_04 "Рад помочь своей сестрёнке! Если что, обращайся."
                                    menu:
                                        Alice_01 "Хорошо, Макс. Спасибо."
                                        "{i}уйти{/i}":
                                            pass
                                else:
                                    Alice_03 "Более-менее. Скажем так - с переменным успехом. Но я нацелена стать очень популярной!"
                                    Max_04 "Вот это правильный настрой! Ладно, удачи..."
                                    menu:
                                        Alice_01 "Спасибо, Макс!"
                                        "{i}уйти{/i}":
                                            pass
                            elif alice.dcv.battle.stage in [4, 5, 7, 8]:
                                #если Эрик начал помогать Алисе с блогом, направление дружбы (легкие меры)
                                if alice.dcv.battle.stage in [4, 5]:
                                    #первый раз
                                    $ alice.dcv.battle.stage += 3  # 7 или 8
                                    Alice_03 "Ты знаешь, хорошо! Но это в основном заслуга Эрика. Он помогает с раскруткой по моему блогу."
                                    Max_07 "Какой он молодец! Реальные вещи делает. А моя помощь нужна?"
                                    if get_stage_sexbody2() < 2:
                                        # Макс еще не знает о том, что Эрик собирается купить бельё Алисе
                                        Alice_02 "Можешь не париться, Макс. Эрик купит то, что мне нужно."
                                        Max_08 "Эрик купит тебе новое нижнее бельё?"
                                        Alice_05 "Да, мне нужно ещё одно сексуальное боди. И я показала ему, какое конкретно хочу. Решили, что купим, когда поедем на шопинг в субботу. А что?"
                                        Max_02 "Да так, интересно было, какое ты себе боди захотела. Покажешь?"
                                        jump alice_showing_lingerie1
                                    else:
                                        Alice_02 "Пока что нет, Макс. Эрик обо всём позаботится, можешь расслабиться."
                                        Max_01 "Но если что, всё равно обращайся."
                                        Alice_01 "Хорошо, Макс. Спасибо."
                                else:
                                    #периодический
                                    Alice_03 "Ты знаешь, хорошо! С раскруткой от Эрика по другому и быть не может."
                                    Max_07 "Круто. А моя помощь нужна?"
                                    Alice_02 "Пока что нет, Макс. Эрик обо всём позаботится, можешь расслабиться."
                                    Max_01 "Но если что, всё равно обращайся."
                                    Alice_01 "Хорошо, Макс. Спасибо."
                            else:  # alice.dcv.battle.stage in [6, 9]
                                #если Эрик начал помогать Алисе с блогом, направление вражды (сильные меры)
                                if alice.dcv.battle.stage == 6:
                                    #первый раз
                                    $ alice.dcv.battle.stage = 9
                                    Alice_07 "Ты знаешь, отлично! Но это в основном заслуга Эрика. Он помогает с раскруткой и рекламой по моему блогу."
                                    Max_00 "Вот козлина какой!"
                                    Alice_13 "Что, Макс? Я тут занята немного, прослушала тебя..."
                                    Max_09 "Я говорю, вот молодчина какой..."
                                    Alice_05 "Ну да. А то мне послышалось что-то... В общем, всё идёт хорошо у меня. Я довольна!"
                                    Max_08 "А я могу чем-то помочь?"
                                    if get_stage_sexbody2() < 2:
                                        # Макс еще не знает о том, что Эрик собирается купить бельё Алисе
                                        Alice_02 "Можешь не париться, Макс. Эрик купит то, что мне нужно."
                                        Max_08 "Эрик купит тебе новое нижнее бельё?"
                                        Alice_05 "Да, мне нужно ещё одно сексуальное боди. И я показала ему, какое конкретно хочу. Решили, что купим, когда поедем на шопинг в субботу. А что?"
                                        Max_02 "Да так, интересно было, какое ты себе боди захотела. Покажешь?"
                                        jump alice_showing_lingerie1
                                    else:
                                        Alice_02 "Пока что нет, Макс. Эрик обо всём позаботится, можешь расслабиться."
                                        Max_01 "Но если что, всё равно обращайся."
                                        Alice_01 "Хорошо, Макс. Спасибо."
                                else:
                                    #периодический
                                    Alice_07 "Ты знаешь, отлично! С раскруткой и размещением рекламы от Эрика по другому и быть не может."
                                    Max_08 "Ну просто фантастика! А я могу чем-то помочь?"
                                    Alice_02 "Пока что нет, Макс. Эрик обо всём позаботится, можешь расслабиться."
                                    Max_01 "Но если что, всё равно обращайся."
                                    Alice_01 "Хорошо, Макс. Спасибо."
                        "Я слышал, Эрик тебе новое бельё собирается купить?" if get_stage_sexbody2() == 3:
                            jump alice_about_lingerie0
                        "Покажешь боди, которое тебе Эрик купит?" if get_stage_sexbody2() == 4:
                            jump alice_showing_lingerie1
                else:
                    $ renpy.show('Alice blog 01'+alice.dress)
                    $ renpy.show('Max blog 01'+mgg.dress)
                    menu:
                        Alice_15 "Что?! Макс! Ну-ка иди отсюда, пока в ухо не получил!"
                        "{i}сбежать{/i}" if not _in_replay:
                            pass
                        "Классно смотришься!" if not _in_replay:
                            Alice_16 "Тебе чего надо, Макс?! Я тут занята..."
                            Max_07 "Да я так, спросить хотел..."
                            $ renpy.show('Alice blog 02'+alice.dress)
                            $ renpy.show('Max blog 02'+mgg.dress)
                            menu:
                                Alice_13 "Ну..."
                                "Чем занята?":
                                    Alice_05 "Блогом занимаюсь! И ты это прекрасно знаешь... А если ты тупой, в чём я уверена, то мог бы спросить и через дверь..."
                                    Max_03 "Так не интересно! Ну и как, получается?"
                                    menu:
                                        Alice_03 "Да, получается! И не мешай, иди уже..."
                                        "{i}уйти{/i}":
                                            pass
                                        "Точно получается?":
                                            menu:
                                                Alice_18 "Макс!!! Я тебе сейчас..."
                                                "{i}сбежать{/i}":
                                                    pass
                                "Чего дверь-то закрыла?":
                                    Alice_05 "А что, мне с распахнутой дверью в нижнем белье тут сидеть?!"
                                    Max_03 "Конечно, да! Мне вот нравится..."
                                    menu:
                                        Alice_03 "Ой, Макс, свали уже... Не мешай!"
                                        "{i}уйти{/i}":
                                            pass
                                        "Что делаешь-то?":
                                            menu:
                                                Alice_18 "Да ты бессмертный что ли!!! Сейчас я тебе напинаю..."
                                                "{i}сбежать{/i}":
                                                    pass
                        "А я тебе принёс кое-что!" if all([items['sexbody1'].have, items['photocamera'].have, not expected_photo]):
                            $ renpy.show('Alice blog 02'+alice.dress)
                            $ renpy.show('Max blog 02'+mgg.dress)
                            Alice_05 "Если это только твои ухмылки, Макс, а не что-нибудь полезное, то ты сейчас полетишь в бассейн..."
                            Max_01 "Ну, это такое чёрное, полупрозрачное... и смотреться это на тебе должно очень сексуально..."
                            Alice_07 "Снова бельё мне купил! Ну ты даёшь, Макс! Давай сюда, посмотрим..."

                            scene BG char Alice newbody-00f
                            $ renpy.show('Alice newbody 01'+alice.dress)
                            $ renpy.show('Max newbody 01'+mgg.dress)

                            Max_04 "Конечно! Ну как тебе?"
                            Alice_03 "Ого, какое классное! Мне уже не терпится примерить... А это у тебя что, фотоаппарат? Макс, ты серьёзно решил, что я позволю тебе фотографировать, как я переодеваюсь?!"
                            Max_02 "Нет, это я подумал, что тебе для блога пригодятся хорошие фотографии. В белье."
                            Alice_05 "Ага, ну конечно, для блога... Здесь кому угодно будет понятно, что у тебя на самом деле на уме!"
                            Max_07 "Я думаю, несколько качественных фотографий пойдут твоему блогу только на пользу."
                            Alice_02 "Ты фотографировать хоть умеешь?"
                            Max_03 "Конечно! Так что давай примеряй боди и я тебя пощёлкаю."
                            menu:
                                Alice_13 "Вот ещё! Не буду я переодеваться, когда у тебя в руках эта штука. За дверью подожди..."
                                "Ладно, подожду..." if not _in_replay or (_in_replay and not alice.daily.drink):
                                    #дверь в комнату Алисы
                                    $ renpy.scene()
                                    $ renpy.show('location house aliceroom door-'+get_time_of_day())
                                    Max_02 "{m}Алиса не отказалась от снимков - уже хорошо. Интересно, как много через это боди будет видно...{/m}"
                                "А если конфетку дам, то остаться можно?" if (_in_replay and alice.daily.drink) or (not _in_replay and kol_choco>0):
                                    Alice_05 "Так, конфетку я возьму, а ты всё равно отправляешься за дверь. А будешь спорить, я засуну тебе этот фотоаппарат в ..."
                                    $ give_choco()
                                    $ alice.daily.drink = 1
                                    Max_08 "Ладно, подожду за дверью..."
                                    #дверь в комнату Алисы
                                    $ renpy.scene()
                                    $ renpy.show('location house aliceroom door-'+get_time_of_day())
                                    Max_02 "{m}Алиса не отказалась от конфетки. Интересно, как много я увижу, а главное сфотографирую...{/m}"
                            menu:
                                Alice "{b}Алиса:{/b} Заходи давай, пока я не передумала!"
                                "{i}войти в комнату{/i}":
                                    jump alice_body_photoset1
            else:
                # Алиса позирует стоя и Макс остаётся незамеченным
                if all([alice.dcv.photo.stage==1, alice.dcv.photo.done]):
                    # blog-desk-01 + alice 02 + max 02
                    $ renpy.show('Alice blog '+random_choice(['03', '04'])+alice.dress)
                    $ renpy.show('Max blog 02'+mgg.dress)
                    menu:
                        Alice_05 "Макс, совсем стыд потерял! Уже не подглядываешь, а просто открыто приходишь и глазеешь?"
                        "Я твои фотки принёс...":
                            jump give_photos1
                elif alice.dcv.intrusion.stage in [1, 2]:
                    # blog-desk-01 + alice 03-04 + max 02
                    $ renpy.show('Alice blog '+random_choice(['03', '04'])+alice.dress)
                    $ renpy.show('Max blog 02'+mgg.dress)
                    menu:
                        Alice_05 "Макс, совсем стыд потерял! Уже не подглядываешь, а просто открыто приходишь и глазеешь?"
                        "Я слышал, Эрик тебе новое бельё собирается купить?" if get_stage_sexbody2() == 3:
                            jump alice_about_lingerie0
                        "Покажешь боди, которое тебе Эрик купит?" if get_stage_sexbody2() == 4:
                            jump alice_showing_lingerie1
                else:
                    $ renpy.show('Alice blog '+random_choice(['03', '04'])+alice.dress)
                    $ renpy.show('Max blog 03'+mgg.dress)
                    menu:
                        Max_05 "{m}Отлично! Алиса крутит задом перед камерой в одном нижнем белье! Надеюсь, не заметит... Отсюда вид точно лучше, чем через камеру...{/m}"
                        "{i}уйти{/i}":
                            pass

        "{i}уйти{/i}" if not _in_replay:
            pass
    jump Waiting


label alice_body_photoset1:

    $ expected_photo = []

    scene BG char Alice spider-night-05
    show Alice newbody 01

    Alice_02 "По-моему, оно обалденное, Макс! А ты как думаешь?"
    Max_03 "Это точно! Снимки получатся прямо как для обложки!"

    show Alice newbody 02

    Alice_05 "Да вижу я по твоим шортам, что ты там уже не на обложку напредставлял, а на разворот."
    Max_01 "Зато отличный индикатор! Сразу ясно, что выглядишь ты в этом боди очень классно. А как там сзади всё выглядит? Ну-ка покрутись..."

    if not alice.daily.drink:
        Alice_03 "Там всё в порядке. Может тебе повезёт во время съёмки и ты что-то да увидишь. Будешь щёлкать меня прямо здесь, у стены или у зеркала?"   #без конфеты
        Max_04 "Давай, я думаю, на кровати. Будет больше ярких цветов."
    else:
        show Alice newbody 03
        Alice_07 "Там всё в порядке, так ведь?"
        Max_05 "О да, такую обалденную попку нужно как можно скорее пощёлкать!"

        show Alice newbody 02

        Alice_03 "Будешь щёлкать меня прямо здесь, у стены или у зеркала?"
        Max_04 "Давай, я думаю, на кровати. Будет больше ярких цветов."

    # $ expected_photo.append('01')
    scene photoshot 01-Alice 01
    Alice_02 "На кровати, так на кровати. А теперь давай признавайся, Макс, когда успел фотоаппарат научиться держать? Не на своих же любимых онлайн-курсах?"
    show FG photocamera
    play sound "<from 1>audio/PhotoshootSound.ogg"
    Max_01 "Ты не вопросы спрашивай, а позируй лучше красиво! Может, я просто талантлив во всём, чего касаюсь... {p=1.5}{nw}"
    hide FG
    extend "Снимок готов! Залазь теперь на кровать, снимем твою прелестную попку..."

    # $ expected_photo.append('02')
    scene photoshot 01-Alice 02
    Alice_03 "Смотри, чтобы красиво получалось, но не слишком откровенно! Я всё-таки бельё рекламирую, а не свои прелести. Хотя, и свои прелести тоже, но хоть немного скрытые бельём!"
    show FG photocamera
    play sound "<from 1>audio/PhotoshootSound.ogg"
    Max_02 "На тебе ведь сексуальное полупрозрачное бельё, Алиса! Думаешь могут получится не откровенные снимки? {p=1.5}{nw}"
    hide FG
    extend "Получилось хорошо! Ложись на кровать, раз уж рекламируем бельё, то надо во всей красе показать, как оно на тебе сидит."

    # $ expected_photo.append('03')
    scene photoshot 01-Alice 03
    Alice_04 "Мог бы просто сказать, что ты извращенец, который обожает глазеть на полуголый зад своей сестры! А то, что это якобы для развития блога - просто удобный предлог."
    show FG photocamera
    play sound "<from 1>audio/PhotoshootSound.ogg"
    Max_04 "То, что я обожаю глазеть - не моя вина, мужчины здесь бессильны. {p=1.5}{nw}"
    hide FG
    extend "Отличный кадр! Тебе только остаётся принять этот факт, повернуться ко мне и быть погорячее..."   #открывает снимок 04

    # $ expected_photo.append('04')
    scene photoshot 01-Alice 04
    Alice_05 "Вот так погорячее сойдёт или ты хочешь, чтобы я показала ещё больше?"
    show FG photocamera
    play sound "<from 1>audio/PhotoshootSound.ogg"
    Max_03 "Ага, я хочу! Такой кадр упускать нельзя, замри... {p=1.5}{nw}"
    hide FG
    extend "Вот так, готово! А теперь можешь показать больше..."

    if not alice.daily.drink:
        scene BG char Alice spider-night-05
        show Alice newbody 04
        Alice_01 "Конечно, уже раздеваюсь... Закатай губу, Макс! Ты ещё маленький для такого."
        Max_07 "Да ладно тебе, Алиса! Мы всего-то четыре снимка сделали!"

        show Alice newbody 02
        Alice_02 "Мне вполне этого будет достаточно для развития блога, пока что. Только будь добр, обработай эти фото побыстрее."
        Max_11 "Вот и помогай тебе! Никакого праздника..."
        Alice_05 "А ты не ожидай многого и разочарований тогда не будет. Всё, жду мои фотографии."
        Max_09 "Конечно. Спасибо, Макс за фотосессию... Ой, да не за что, Алиса..."
        $ renpy.end_replay()
        $ SetCamsGrow(house[1], 200)
        $ poss['blog'].open(7)
        $ spent_time += 20
        jump .end

    Alice_04 "Ты же хоть примерно понимаешь, что с тобой будет, если дальнейшие фотографии окажутся в интеренете?"   #с конфетой
    Max_01 "Там окажутся только те фотографии, которые тебе пригодятся для блога. За остальные можешь не переживать, они только для меня."   #открывает снимок 05

    # $ expected_photo.append('05')
    scene photoshot 01-Alice 05
    Alice_08 "Ох, как-то жарковато стало моим арбузикам, да и тебе я вижу тоже. Ого, а что это у нас тут такое большое и твёрдое? Похоже, будет интересный кадр!"
    Max_07 "Хоть это и очень приятно, но мне будет не просто сосредоточиться на съёмке, если ты продолжишь тереться ногой об мой член! Может продолжишь это делать после того, как я тебя отщёлкаю?"
    play sound "<from 1>audio/PhotoshootSound.ogg"
    show FG photocamera
    Alice_07 "Ой, я кажется заигралась немного... Не удержалась... {p=1.5}{nw}"
    hide FG
    extend "Люблю исследовать что-нибудь интересное своими ножками! Это меня очень заводит..."
    Max_02 "А тем временем я заснял твои шалости и готов к новым... Что твои ножки ещё любят делать?"   #открывает снимок 06

    # $ expected_photo.append('06')
    scene photoshot 01-Alice 06
    Alice_03 "Я могу их немножко раздвинуть, чтобы этот кадр стал твоим любимым... Какая же я плохая сестрёнка! В хорошем смысле..."
    play sound "<from 1>audio/PhotoshootSound.ogg"
    show FG photocamera
    Max_04 "Мне бы фотоаппарат не выронить от восхищения! Фокус настроил и... {p=1.5}{nw}"
    hide FG
    extend "Готово. Кадр и правда очень хорош!"   #открывает снимок 07

    # $ expected_photo.append('07')
    scene photoshot 01-Alice 07
    Alice_02 "Или всё-таки снимок моей попки будет твоим любимым, а Макс? Тебе же нравится, когда я делаю так?"
    play sound "<from 1>audio/PhotoshootSound.ogg"
    show FG photocamera
    Max_03 "Да-а-а... От вида этих изгибов в голове появляются такие пошлые мысли и желания! {p=1.5}{nw}"
    hide FG
    extend "Да, кадр получился что надо! Может, теперь фото без белья?"   #открывает снимок 08

    # $ expected_photo.append('08')
    scene photoshot 01-Alice 08
    Alice_01 "Конечно, уже раздеваюсь... Закатай губу, Макс! Ты ещё маленький для такого, хоть у тебя и есть кое-что большое..."
    play sound "<from 1>audio/PhotoshootSound.ogg"
    show FG photocamera
    Max_05 "Тогда последний снимок... {p=1.5}{nw}"
    hide FG
    extend "Сделал! Вот и отснимались."

    scene BG char Alice spider-night-05
    show Alice newbody 04
    Alice_07 "Классное боди ты купил! Спасибо тебе, Макс! Ты же скоро обработаешь снимки?"
    Max_04 "Да, как только - так сразу. Шикарно пофотографировались!"
    Alice_04 "Это же останется нашим маленьким секретом?"
    Max_03 "Конечно, Алиса!"

    $ renpy.end_replay()
    $ added_mem_var('alice_photoset1')
    $ SetCamsGrow(house[1], 250)
    $ spent_time += 40
    $ poss['blog'].open(8)

    label .end:
        $ items['sexbody1'].give()
        $ alice.gifts.append('sexbody1')
        $ setting_clothes_by_conditions()
        $ alice.dcv.photo.stage = 1
        $ alice.dcv.photo.set_lost(2)
        $ current_room = house[0]
        jump Waiting


label alice_towel_after_club:
    scene location house bathroom door-evening
    menu:
        Max ""
        "{i}постучаться{/i}" if alice.daily.drink < 2:
            Alice "{b}Алиса:{/b} Кому там не спится? Я ванну принимаю..."
            Max_02 "Это я, Макс. Полотенце твоё принёс."
            Alice "{b}Алиса:{/b} Поздно, Макс! Я уже в ванне, так что гуляй."
            menu:
                Max_10 "Вот чёрт! И здесь облом."
                "{i}отправиться спать{/i}":
                    $ current_room = house[0]
                    jump Sleep

        "{i}открыть дверь{/i}" if alice.daily.drink > 1 or all([alice.flags.hip_mass>4, alice.daily.drink]):
            # Алиса съела две конфеты или пройден "трезвый путь", тогда достаточно конфеты перед клубом
            pass

    # bath-open-00 + bath-open-alice-01
    scene alice_open_bath with fade4
    Alice_15 "Макс, я тут вообще-то голая лежу в ванне! Оу, ты всё же принёс мне полотенце..."
    Max_02 "Да, я тут как раз нашёл, на что его можно повесить..."

    # bath-talk-02 + bath-talk-02-alice-01 + bath-talk-02-max-03
    $ var_pose = '03'
    scene alice_bath_talk
    Alice_06 "Оригинально... А ты не думал, что нужно было постучаться, прежде чем входить? Я ведь могла здесь... чем-нибудь ещё заниматься..."
    Max_03 "На это я, если честно, и надеялся."

    # bath-talk-03-max&alice-01-f + bath-talk-03-max&alice-01
    $ var_pose = '01'

    Alice_05 "Ты что, стоял перед дверью и о чём-то таком думал, чтобы ТАК отдать мне полотенце?"

    if not all(['sexbody1' in alice.gifts, alice.flags.nakedpunish]):
        # Алису ещё не наказывали полностью голую + ещё не подарено чёрное сексуальное боди
        Max_04 "Ага, специально стоял перед дверью и представлял, как ты тут ублажаешь себя в самых эротичных позах!"
        Alice_14 "Ну ты и больной, Макс! Даже больше и сказать на это нечего... Давай моё полотенце и скройся, извращенец озабоченный."
        Max_02 "Да ладно, весело же придумал с полотенцем?!"
        Alice_16 "Ещё веселее будет, если вешать будет больше не на что!"
        menu:
            Max_10 "Ну вот, опять угрозы пошли..."
            "{i}отправиться спать{/i}":
                $ current_room = house[0]
                jump Sleep

    $ added_mem_var('bath_fan')
    # Алису наказывали полностью голую + Макс подарил чёрное сексуальное боди
    Max_04 "Это тётя Кира мне стриптиз показала, до сих пор стоит..."
    Alice_13 "Да не смеши, Макс! Тётя Кира, конечно, пьяная, но... хотя в клубе она это вытворяла..."

    # after-club-bath01-max&alice-01-f + after-club-bath01-max&alice-01
    $ var_pose = '01'
    scene alice_in_bath_02

    Max_03 "Двигалась она классно! Ну а как ты повеселилась в клубе?"
    Alice_02 "Ты знаешь, очень... очень хорошо. Но, похоже, я выпила сегодня куда больше, чем планировала... А что это твоя рука забыла на моей попке?"
    Max_07 "Она потянулась к прекрасному! А может ей хочется наказать эту попку..."

    # bath-cun-02 + after-club-bath01-max&alice-02
    $ var_pose = '02'
    scene alice_in_bath_cun

    Alice_12 "За что это?!"
    Max_09 "Может, потому что ты была плохой девочкой?! Я тебе с блогом помогаю, бельё покупаю, сладостями балую... а ты только угрозами в меня сыпешь..."
    menu:
        Alice_06 "Не надо меня наказывать, Макс! Может, я могу как-то это исправить? Каким-нибудь приятным образом?"
        "Ну, разве, что так...\n{i}(начать массировать её киску рукой){/i}":

            # after-club-bath02a-max&alice-02-f + after-club-bath02a-max&alice-02
            $ var_pose = '02a'
            scene alice_in_bath_03
            Alice_15 "Макс! Ну что ты делаешь?! Ахх... Ты полез рукой прямо туда... Это же так..."
            Max_02 "Приятно? Это ты хотела сказать?"
            Alice_06 "Д-а-а... То есть, я хотела сказать... неправильно! Ммм..."
            Max_01 "Хочешь, чтобы я перестал это делать?"

            # after-club-bath01-max&alice-01-f + after-club-bath02a-max&alice-01
            $ var_pose = '02a'
            scene alice_in_bath_02
            Alice_09 "Хочу... ухх... чтобы ты продолжал... Как же хорошо... Ты этому на своих курсах массажа научился?!"
            Max_03 "Считай, да. Давно хотел попрактиковаться в этом!"
            menu:
                Alice_07 "Такое ощущение, что практика у тебя уже была... Да... я хочу чуть быстрее, Макс... Ммм..."
                "{i}проникнуть в её киску пальцами{/i}":
                    pass

            # after-club-bath03a-max&alice-02-f + after-club-bath03a-max&alice-02
            $ var_pose = '03a'
            scene alice_in_bath_03
            Alice_10 "Ах! Вот чёрт, Макс! Да-а-а... это так классно... быстрее..."
            Max_04 "{m}Алиса так приятно постанывает... А уж мне не менее приятно трахать эту нежную киску пальцами. Может быть, она даже кончит, если я ускорюсь...{/m}"

            # after-club-bath01-max&alice-01-f + after-club-bath03a-max&alice-01
            $ var_pose = '03a'
            scene alice_in_bath_02

            Alice_11 "Да, Макс, да! Я кончаю... загони свои шаловливые пальчики поглубже... да... Ох... Класс!"

            jump .max_turn

        "Поласкай свою киску для меня...":
            Alice_15 "Ты такой извращенец, Макс! Подглядываешь, фантазируешь всякое, а теперь хочешь смотреть, как я себя ублажаю..."
            Max_09 "Вот об этом я и говорю, ты очень неблагодарно себя ведёшь. Совершенно не хочешь меня порадовать в ответ..."

            # after-club-bath01-max&alice-01-f + after-club-bath02b-max&alice-01
            $ var_pose = '02b'
            scene alice_in_bath_02
            Alice_06 "Нет, я хочу... Ахх... но это ведь так... неправильно. Ммм..."
            Max_02 "Может, мне помассировать твои ножки, чтобы тебя это не так напрягало?"
            menu:
                Alice_09 "Ох... Ты же знаешь, я никогда не смогу от этого отказаться. Уже можно было давно заметить, что они у меня целиком - эрогенная зона..."
                "{i}массировать её ножки{/i}":
                    pass

            # bath-talk-03-max&alice-01-f + after-club-bath03b-max&alice-01
            $ var_pose = '03'
            scene alice_in_bath_01
            Alice_07 "О да... Наши с тобой пальчики сегодня творят чудеса! Расшалились не на шутку. Как же меня это всё заводит..."
            Max_03 "Хочешь узнать, как твои ножки любят шалить?"
            menu:
                Alice_08 "Ухх, как интригующе звучит! Я вся в предвкушении узнать, что же они у меня такое любят?"
                "{i}тереться членом о её ногу{/i}":
                    pass

            # after-club-bath04b-max&alice-02-f + after-club-bath04b-max&alice-02
            $ var_pose = '04b'
            scene alice_in_bath_03
            Alice_10 "Ах! Да-а-а... это так классно... чувствовать твой большущий член... Я и не думала, что тебе понравится такое!"
            Max_04 "Как могут не нравится прикосновения твоих красивых и нежных ног... Особенно к члену!"

            # bath-talk-03-max&alice-01-f + after-club-bath04b-max&alice-01
            $ var_pose = '04'
            scene alice_in_bath_01
            Alice_09 "Ммм... Да, Макс, продолжай! Кажется, я скоро кончу... Ахх... ты сводишь меня с ума! Ох..."
            Max_05 "{m}Алиса так приятно постанывает и всё глубже проникает пальцами в свою киску... Наверняка представляет, как я её трахаю! Вот бы до этого дошло...{/m}"
            Alice_11 "Ох, Макс... да, да! Я... кончаю... Ухх... Кажется, я не чувствую своих ног... всё..."

            jump .max_turn

    label .max_turn:

        Max_02 "Ну вот, можешь же быть хорошей девочкой, хоть недолго."

        # bath-cun-02 + after-club-bathbj01-max&alice-01
        $ var_pose = '01'
        scene alice_in_bath_cun
        menu:
            Alice_05 "Мне понравилось, как ты меня \"наказал\", Макс! И я хочу, чтобы ты тоже кончил..."
            "Ох! Тогда тебе стоит быстрее работать рукой...":

                # bath-talk-03-max&alice-01-f + after-club-bathbj01-max&alice-01a
                $ var_pose = '01'
                scene alice_in_bath_01
                menu:
                    Alice_04 "Так достаточно быстро? Ну и вымахал же у тебя такой член, Макс! Нравится? Не сдерживайся, а то у меня начинает уставать рука..."
                    "{i}кончить{/i}":
                        jump .cum_breast

            "Так пусти в дело свой язычок..." if alice.flags.nakedpunish and alice.dcv.intrusion.stage in [5, 7]:   #если Алису наказывали полностью голую + Макс опередил Эрика с дарением белья
                $ added_mem_var('bath_tongue')
                Alice_08 "Честно говоря, я еле сдерживалась, чтобы не начать именно так! Но раз ты настаиваешь..."

                # after-club-bath02a-max&alice-02-f + after-club-bathbj01-max&alice-02
                # after-club-bathbj01-max&alice-02a-f + after-club-bathbj01-max&alice-02a
                if random_choice([True, False]):
                    scene alice_in_bath_bj
                else:
                    $ var_pose = '02a'
                    scene alice_in_bath_bj_01

                Max_20 "{m}О да, сестрёнка... Она так сладко скользит своим языком по всей длине моего члена! И про головку не забывает... Ухх...{/m}"
                menu:
                    Alice_04 "Ммм... Только никому ни слова, что я тут вытворяла с твоим членом! Ты уже скоро?"
                    "{i}кончить ей на лицо{/i}":
                        jump .cum_face

                    "{i}кончить ей на грудь{/i}":
                        jump .cum_breast

                    "Нет, я даже не близко..." if alice.flags.hip_mass > 4:
                        # пройден "трезвый" путь с фут-джобом у ТВ
                        jump .not_even_close

            "Вообще-то, я надеялся, что ты возьмёшь его в рот..." if False:  #для версии 0.07
                pass

    label .cum_breast:

        # after-club-bathbj01-max&alice-03-f + after-club-bathbj01-max&alice-06 + after-club-bathbj01-max&alice-06a
        $ var_pose = '06'
        scene alice_in_bath_cum
        Alice_09 "Ого, сколько спермы... Ты заляпал мне всю грудь! Теперь мыться надо..."
        Max_03 "А ты разве не для этого ванну решила принять?"
        Alice_06 "Да, точно... Мы же никому не станем рассказывать, что тут было?"
        Max_02 "Я только полотенце принёс и пошёл спать..."
        menu:
            Alice_05 "Ага. Именно так всё и было!"
            "{i}отправиться спать{/i}":
                $ renpy.end_replay()
                $ current_room = house[0]
                jump Sleep

    label .cum_face:

        # after-club-bathbj01-max&alice-03-f + after-club-bathbj01-max&alice-05 + after-club-bathbj01-max&alice-05a
        $ var_pose = '05'
        scene alice_in_bath_cum
        Alice_06 "Макс! Ну то за фигня! Ты кончил мне прямо на лицо!"
        Max_07 "А ты хотела как-то по-другому?"
        Alice_13 "Ну, предупредил бы хоть, чтобы в глаза не попало... Теперь мыться надо..."
        Max_03 "А ты разве не для этого ванну решила принять?"
        Alice_06 "Да, точно... Мы же никому не станем рассказывать, что тут было?"
        Max_02 "Я только полотенце принёс и пошёл спать..."
        menu:
            Alice_05 "Ага. Именно так всё и было!"
            "{i}отправиться спать{/i}":
                $ renpy.end_replay()
                $ current_room = house[0]
                jump Sleep

    label .not_even_close:
        # пройден "трезвый" путь с фут-джобом у ТВ
        # bath-talk-03-max&alice-01-f + after-club-bathbj01-max&alice-01a
        $ var_pose = '01'
        scene alice_in_bath_01
        Alice_08 "Кажется, я знаю, что с этим поможет... Смотри, не упади от наслаждения!"
        # after-club-bathbj01-max&alice-03-f + after-club-bathbj01-max&alice-03
        $ var_pose = '03'
        scene alice_in_bath_bj_02
        menu:
            Max_21 "Ох, Алиса! Упасть здесь действительно есть от чего! Какие у тебя нежные губы... Д-а-а... У тебя хорошо получается, сестрёнка... Давай поактивнее... Как же приятно, д-а-а..."
            "{i}сдерживаться{/i}" ('sex', mgg.sex * 4, 90):
                if rand_result:
                    # (Удалось сдержаться!)
                    # after-club-bathbj01-max&alice-03-f + after-club-bathbj01-max&alice-03a
                    $ var_pose = '03a'
                    scene alice_in_bath_bj_02
                    menu:
                        Max_22 "[restrain!t]Вот чёрт, Алиса! Ты делаешь это просто потрясающе! Да, продолжай вот так... Ещё быстрее... Вот умница! Я держусь из последних сил... Вот-вот кончу..."
                        "{i}кончить ей на лицо{/i}":
                            jump .cum_face

                        "{i}кончить ей на грудь{/i}":
                            jump .cum_breast
                else:
                    # (Не удалось сдержаться!)
                    jump .no_restrain

    label .no_restrain:
        # не сджерждался. как в варианте "кончить ей на лицо"
        # after-club-bathbj01-max&alice-03-f + after-club-bathbj01-max&alice-05 + after-club-bathbj01-max&alice-05a
        $ var_pose = '05'
        scene alice_in_bath_cum
        Alice_06 "[norestrain!t]Макс! Ну то за фигня! Ты кончил мне прямо на лицо!"
        Max_07 "А ты хотела как-то по-другому?"
        Alice_13 "Ну, предупредил бы хоть, чтобы в глаза не попало... Теперь мыться надо..."
        Max_03 "А ты разве не для этого ванну решила принять?"
        Alice_06 "Да, точно... Мы же никому не станем рассказывать, что тут было?"
        Max_02 "Я только полотенце принёс и пошёл спать..."
        menu:
            Alice_05 "Ага. Именно так всё и было!"
            "{i}отправиться спать{/i}":
                $ renpy.end_replay()
                $ current_room = house[0]
                jump Sleep

label give_photos1:
    Alice_07 "Ну наконец-то, давай сюда, я их сразу размещу везде, где только можно..."
    Max_01 "Вот, держи."

    # blog-desk-01 + alice 02 + max 04
    $ renpy.show('Alice blog 02'+alice.dress)
    $ renpy.show('Max blog 04'+mgg.dress)
    Alice_06 "Надеюсь, мы не зря их сделали и они привлекут ко мне больше внимания."
    Max_02 "Уж точно лишними не будут, на них же такая сексуальная девочка!"
    Alice_05 "Да, я такая! Даже и подумать не могла, что когда-нибудь буду позировать полуголой для своего брата... А снимки хороши, Макс! Мне нравится, ты хорошо снимаешь..."
    Max_07 "Так там через бельё почти ничего не видно. Так, слегка..."
    Alice_02 "Ой, Макс, не смущай меня, а! Повезло тебе, что я как раз думала о том, что мне нужны хорошие снимки. И хорошо, что ты купил не сильно откровенное боди. Именно такое, какое было нужно."
    Max_03 "Наверно, ещё нужно будет купить что-нибудь из белья, да?"
    Alice_13 "Ага, желательно. Но не сейчас. Пока и этого хватит, а позже посмотрим..."
    Max_04 "Хорошо. Не буду тебе мешать. Ещё ведь пофотографируемся?"
    Alice_03 "Не исключаю такого, когда будет в чём позировать. Хотя, будет зависеть от откровенности белья."
    Max_01 "Понял. Ладно, удачи..."
    Alice_01 "Спасибо, Макс!"

    $ alice.dcv.photo.stage = 2
    # $ append_photo('01-Alice', 8)
    if poss['blog'].used(8):
        $ append_album('01-Alice', ['01', '02', '03', '04', '05', '06', '07', '08'])
    elif poss['blog'].open(7):
        $ append_album('01-Alice', ['01', '02', '03', '04'])

    if expected_photo == ['01', '02', '03', '04'] or expected_photo == ['01', '02', '03', '04', '05', '06', '07', '08']:
        $ expected_photo.clear()
    jump Waiting


label blog_with_Eric:
    scene location house aliceroom door-evening
    if alice.daily.blog or (alice.daily.blog and check_is_room('eric', house[1])):
        return

    if not _in_replay:
        if check_is_room('eric', house[1]):
            $ alice.daily.blog = 1
        else:
            $ alice.daily.blog = 1

    $ alice.prev_plan = alice.plan_name
    menu:
        Max_09 "{m}Кажется, в комнате Алиса с Эриком... Хорошо бы узнать, что они там делают. А то мало ли...{/m}"
        "{i}заглянуть в окно{/i}":
            $ spent_time += 20
            if _in_replay or all([alice.dcv.intrusion.stage==8, alice.dcv.battle.stage in [4, 5, 7, 8], GetRelMax('eric')[0]>0]):
                # Эрик купил Алисе чёрное кружевное боди вперёд Макса

                # spider-night-04 + aliceroom-blog-dresses-01-eric-(01/01a) + Алиса в белье(spider-night-04-alice-(01/02/03) / spider-night-04-alice-(01a/02a/03a) / aliceroom-blog-dresses-01-alice-(01a/02a/03a))
                scene BG char Alice spider-night-04
                $ renpy.show('Eric newbody2 01'+eric.dress)
                $ renpy.show('Alice newbody2 '+random_choice(['01', '02', '03'])+alice.dress)
                Max_07 "{m}Хоть Эрик и сказал, что подглядывать можно, но вот Алиса вряд ли с этим согласится, так что нужно быть как можно осторожнее...{/m}"
                Alice_06 "Эрик, ты правда хочешь, чтобы я здесь перед тобой одела новое боди? Я, конечно, могу... но только, если ты закроешь глаза и не будешь подглядывать! Хорошо?"
                Eric_02 "Конечно, Алиса. Давай, мне не терпится увидеть, как оно на тебе сидит..."

                # spider-night-04 + aliceroom-blog-dresses-01-eric-(01/01a) + Алиса раздевается(spider-night-04-alice-(04/05/06) / spider-night-04-alice-(04a/05a/06a) / aliceroom-blog-dresses-01-alice-(04a/05a/06a))
                $ renpy.show('Alice newbody2 '+random_choice(['04', '05', '06'])+alice.dress)
                Alice_14 "Эй! Эрик! Ты обещал не подглядывать. Я же вижу, что ты пялишься на меня! Отвернись, быстро! Ну или хотя бы закрой глаза руками..."
                Eric_03 "Ты так красиво начала раздеваться, что я забыл не смотреть. Считай, закрыл."

                # spider-night-04 + aliceroom-blog-dresses-01-eric-(02/02a) + Алиса голая(aliceroom-blog-dresses-02-alice-(01a/02a))
                $ renpy.show('Eric newbody2 02'+eric.dress)
                $ renpy.show('Alice newbody2 '+random_choice(['07', '08']))
                Max_02 "{m}Ага, закрыл он, как же! Точно во всю глазеет сквозь пальцы... Я бы уж точно рискнул так близко поглазеть на голую Алису! Бесподобная у меня сестрёнка...{/m}"

                # spider-night-04 + aliceroom-blog-dresses-01-eric-(02/02a) + Алиса одевается(aliceroom-blog-dresses-02-alice-(03a/04a))
                $ renpy.show('Eric newbody2 02'+eric.dress)
                $ renpy.show('Alice newbody2 '+random_choice(['09', '10']))
                Max_07 "{m}Ухх... Алиса не спешит спрятать свои аппетитные сисечки под боди! Прямо, как мне и хочется... Хм, а может она заметила, что Эрик всё равно подглядывает и таким образом дразнит его?! И не подозревает, что заодно и меня...{/m}"

                # spider-night-04 + aliceroom-blog-dresses-01-eric-(01/01a) + Алиса в новом боди(aliceroom-blog-dresses-02-alice-05a)
                $ renpy.show('Eric newbody2 01'+eric.dress)
                show Alice newbody2 11
                Alice_02 "Всё, можно смотреть... Что скажешь, тебе нравится или нет? Мне вот в нём удобно..."
                Eric_05 "Алиса, на твоём чудесной теле, что угодно будет смотреться шикарно. И да, мне нравится, как это выглядит!"
                Alice_05 "Я рада! А если мне понадобится ещё что-то из нижнего белья, ты поможешь?"
                Eric_01 "Естественно! Всегда можешь ко мне обращаться... Только старайся немного заранее, а то я человек занятой..."
                menu:
                    Max_09 "{m}Понятно всё с вами, Алиса села на шею Эрику, а он и рад. А мне лучше сматываться отсюда, не хватало ещё чтобы меня сейчас заметили...{/m}"
                    "{i}уйти{/i}":
                        $ renpy.end_replay()
                        $ added_mem_var('lace_ling_eric1')
                        $ spent_time += 20
                        $ alice.dcv.intrusion.stage = 9  # бельё Алисе подарил Эрик
                        # $ alice.dress = 'd'
                        # $ alice.dress_inf = '02la'
                        # $ blog_lingerie = ['d', 'd', 'd']
                        $ alice.gifts.append('sexbody2')
                        $ setting_clothes_by_conditions()
                        $ infl[alice].add_e(40)
                        $ poss['blog'].open(17)

            else:
                # blog-desk-01 + alice-02 + eric-01 + max-03
                scene BG char Alice blog-desk-01
                $ alice.dress_inf = {'a':'02', 'b':'02ia', 'c':'02ka', 'd':'02la'}[alice.dress]
                $ renpy.show('Alice blog 02'+alice.dress)
                $ renpy.show('Eric blog 01'+eric.dress)
                $ renpy.show('Max blog 03'+mgg.dress)

                if all([alice.dcv.intrusion.enabled, not alice.dcv.intrusion.done, alice.dcv.intrusion.stage==0]):
                    #в первую среду после разговора с Эриком по Алисе дополнение к мыслям Макса
                    Max_07 "{m}Эрик решил поумничать перед Алисой знаниями в потребительстве и рекламе... Ну да, а тем временем глазеет на её прелести, еле прикрытые бельём. Делать мне здесь пока нечего...{/m}"
                    menu:
                        Max_09 "{m}Подождите-ка, они о покупке белья разговаривают... И без меня! Нужно будет поскорее узнать у Алисы, что это ей там Эрик собрался покупать...{/m}"
                        "{i}уйти{/i}":
                            if not poss['blog'].used(14):
                                $ poss['blog'].open(13)
                            $ alice.dcv.intrusion.stage = 1
                else:
                    menu:
                        Max_07 "{m}Эрик решил поумничать перед Алисой знаниями в потребительстве и рекламе... Ну да, а тем временем глазеет на её прелести, еле прикрытые бельём. Делать мне здесь пока нечего...{/m}"
                        "{i}уйти{/i}":
                            if not poss['blog'].used(14):
                                $ poss['blog'].open(13)
        "{i}уйти{/i}" if not _in_replay:
            if not poss['blog'].used(14):
                $ poss['blog'].open(13)
    jump Waiting
