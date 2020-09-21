

################################################################################
## события Алисы

label alice_bath:
    scene location house bathroom door-evening
    if peeping['alice_bath'] != 0:
        return

    $ peeping['alice_bath'] = 1
    menu:
        Max_00 "Если полночь, значит Алиса отмокает в ванне... Входить без стука - опасно для жизни."
        "{i}постучаться{/i}":
            menu:
                Alice "{b}Алиса:{/b} Кому там не спится? Я ванну набираю..."
                "Это я, Макс. Можно войти?":
                    Alice "{b}Алиса:{/b} Макс, ты глухой? Я же сказала, буду в ванне плескаться. Жди как минимум час!"
                    Max_00 "Ладно, ладно..."
                "{i}уйти{/i}":
                    pass
            jump .end
        "{i}заглянуть со двора{/i}" if 'ladder' not in flags or flags['ladder'] < 2:
            scene Alice bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "Кажется, Алиса и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но подходить ближе опасно - может заметить..."
            menu:
                Max_09 "Нужно что-нибудь придумать..."
                "{i}уйти{/i}":
                    $ flags['ladder'] = 1
                    jump .end
        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
            $ flags['ladder'] = 3
            $ items['ladder'].have = False
            $ items['ladder'].InShop = False
            jump .ladder
        "{i}воспользоваться стремянкой{/i}" if flags['ladder'] > 2:
            jump .ladder
        "{i}уйти{/i}":
            jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-evening 02'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."

        $ __r1 = renpy.random.randint(1, 4)

        scene BG bath-00
        $ renpy.show('Alice bath-window 0'+str(__r1))
        show FG bath-00
        $ Skill('hide', 0.03)
        if __r1 == 1:
            menu:
                Max_03 "Вот это повезло! Алиса как раз собирается принять ванну... Её шикарная попка меня просто завораживает! Так бы любовался и любовался..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Alice bath-window '+renpy.random.choice(['02', '03', '04']))
                    $ Skill('hide', 0.03)
                    menu:
                        Max_05 "Чёрт возьми, она меня что, специально дразнит своей мокренькой грудью... Может моя старшая сестренка и стерва, но какая же она горячая! Очень сексуальна..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ alice.dress_inf = '00aa'
                            pass
                "{i}уйти{/i}":
                    pass
        else:
            menu:
                Max_05 "Чёрт возьми, она меня что, специально дразнит своей мокренькой грудью... Может моя старшая сестренка и стерва, но какая же она горячая! Очень сексуальна..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Alice bath-window 05
                    $ Skill('hide', 0.03)
                    menu:
                        Max_07 "Эх! Самое интересное продолжалось недолго... Единственное, что напоследок остаётся сделать, это насладится её бесподобной попкой!"
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
    if peeping['alice_sleep'] != 0:
        return

    $ peeping['alice_sleep'] = 1
    menu:
        Max_00 "Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья..."
        "{i}заглянуть в окно{/i}":
            $ spent_time = 10
            scene BG char Alice bed-night-01
            $ renpy.show('Alice sleep-night '+pose3_2)
            $ renpy.show('other Alice sleep-night '+pose3_2+alice.dress)
            $ renpy.show('FG alice-voyeur-night-00'+mgg.dress)
            if 'smoke' in flags and flags['smoke'] == 'sleep':
                #  условие выполняется
                if pose3_2 == '01':
                    Max_07 "О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела, в одних лищь трусиках, хочется смотреть вечно!" nointeract
                elif pose3_2 == '02':
                    Max_04 "Эх! Не повезло, что Алиса спит спиной к окну и её грудь не видно... Правда, в таком случае, всегда можно насладиться красотой Алисиной попки." nointeract
                else:
                    Max_01 "Обалденно! Сестрёнка спит выгнув спину, отчего её голая грудь торчит, как два холмика... Соблазнительное зрелище..." nointeract
            elif 'smoke' in flags and flags['smoke'] == 'not_sleep' and not flags['noted']:
                # Алиса нарушила условие
                $ flags['noted'] = True
                $ alice.dress_inf = clothes[alice].sleep.GetCur().info
                if pose3_2 == '01':
                    Max_07 "О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела в этом полупрозрачном белье хочется смотреть вечно! Только вот не всё из этого должно быть на ней одето!"
                elif pose3_2 == '02':
                    Max_04 "Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою попку для меня во всей красе. И есть на ней что-то явно лишнее!"
                else:
                    Max_01 "Обалденно! Сестрёнка спит выгнув спину, отчего её грудь торчит, как два холмика... Соблазнительно... Но, похоже, она кое-что забыла с себя снять перед сном!"
                Max_09 "Так что надо выводить тебя на чистую воду... Возможно, мне стоит воспользоваться тем, чего Алиса боится больше всего?!" nointeract
            else:
                if pose3_2 == '01':
                    Max_07 "О, да! Моя старшая сестрёнка выглядит потрясающе... На изгибы её тела в этом полупрозрачном белье хочется смотреть вечно!" nointeract
                elif pose3_2 == '02':
                    Max_04 "Ого! Мне повезло, что Алиса спит спиной к окну... И не подозревает, что демонстрирует свою попку для меня во всей красе." nointeract
                else:
                    Max_01 "Обалденно! Сестрёнка спит выгнув спину, отчего её грудь торчит, как два холмика... Соблазнительно..." nointeract
            $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
            if rez != 'exit':
                $ spent_time += 10
                scene BG char Alice bed-night-02
                $ renpy.show('Alice sleep-night-closer '+pose3_2)
                $ renpy.show('other Alice sleep-night-closer '+pose3_2+alice.dress)
                if 'smoke' in flags and flags['smoke'] == 'sleep':
                    if pose3_2 == '01':
                        Max_03 "Да уж... Жаль только, что грудь не видно так, как хотелось бы, но её обворожительной попкой можно любоваться бесконечно... Так и хочется по ней шлёпнуть... Правда, тогда это будет последнее, что я сделаю в жизни. Так что лучше потихоньку уходить..." nointeract
                    elif pose3_2 == '02':
                        Max_02 "Класс! Может Алиса мне и сестра, но рядом с этой упругой попкой я бы пристроился с огромным удовольствием... Можно было бы пройти ещё дальше и хоть одним глазком увидеть сиськи, но лучше уйти, а то ещё проснётся..." nointeract
                    else:
                        Max_05 "Чёрт, какая же она притягательная, когда лежит вот так, с совершенно голой грудью... Так и хочется занырнуть между этих сисечек и её стройных ножек! Только бы она сейчас не проснулась..." nointeract
                else:
                    if pose3_2 == '01':
                        Max_03 "Да уж... Её обворожительной попкой можно любоваться бесконечно... Так и хочется по ней шлёпнуть... Правда, тогда это будет последнее, что я сделаю в жизни. Так что лучше потихоньку уходить..." nointeract
                    elif pose3_2 == '02':
                        Max_02 "Класс! Может Алиса мне и сестра, но рядом с этой упругой попкой я бы пристроился с огромным удовольствием... Но пора уходить, а то ещё проснётся..." nointeract
                    else:
                        Max_01 "Чёрт, какая же она притягательная, когда лежит вот так... Так и хочется занырнуть между этих сисечек и её стройных ножек! Только бы она сейчас не проснулась..." nointeract
                $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
        "{i}уйти{/i}":
            pass
    jump Waiting


label alice_sleep_morning:
    scene location house aliceroom door-morning
    if peeping['alice_sleep'] != 0:
        return
    $ peeping['alice_sleep'] = 1
    menu:
        Max_00 "Кажется, Алиса спит. Стучать в дверь точно не стоит.\nДа и входить опасно для здоровья..."
        "{i}заглянуть в окно{/i}":
            $ spent_time = 10
            scene BG char Alice bed-morning-01
            $ renpy.show('Alice sleep-morning '+pose3_2)
            $ renpy.show('other Alice sleep-morning '+pose3_2+alice.dress)
            $ renpy.show('FG alice-voyeur-morning-00'+mgg.dress)
            if 'smoke' in flags and flags['smoke'] == 'sleep':
                $ alice.dress_inf = '02ga'
                if pose3_2 == '01':
                    Max_07 "Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную фигурку, на которой лишь одни трусики..." nointeract
                elif pose3_2 == '02':
                    Max_01 "Чёрт! Как же хорошо, что теперь она спит без лифчика и я могу насладится почти всей красотой её тела, и ещё как... Обалденные у неё сиськи!" nointeract
                else:
                    Max_04 "Вот это да! От таких соблазнительных изгибов и сисечек можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка!" nointeract
            elif 'smoke' in flags and flags['smoke'] == 'not_sleep' and not flags['noted']:
                $ flags['noted'] = True
                $ alice.dress_inf = '02'
                if pose3_2 == '01':
                    Max_07 "Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную, почти голую фигурку как следует... Только вот одето на ней больше, чем должно быть!"
                elif pose3_2 == '02':
                    Max_01 "Чёрт! Хоть она и спит, но прямо лицом ко мне... И тем не менее, насладится красотой её тела я могу, и ещё как... Хотя, если бы она не забыла кое-что с себя снять, было бы куда интереснее!"
                else:
                    Max_02 "Вот это да! От таких соблазнительных изгибов можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка! А была бы ещё лучше, если бы снимала с себя то, что должна!"
                Max_09 "Надо бы мне вывести тебя на чистую воду... Может, стоит воспользоваться тем, что пугает Алису больше всего?!" nointeract
            else:
                if pose3_2 == '01':
                    Max_07 "Ухх! Алиса ещё спит, что меня безусловно радует... Ведь это значит, что я могу рассмотреть её классную, почти голую фигурку как следует... " nointeract
                elif pose3_2 == '02':
                    Max_01 "Чёрт! Хоть она и спит, но прямо лицом ко мне... И тем не менее, насладится красотой её тела я могу, и ещё как..." nointeract
                else:
                    Max_02 "Вот это да! От таких соблазнительных изгибов можно сознание потерять с утра пораньше... Классная у меня старшая сестрёнка!" nointeract
            $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
            if rez != 'exit':
                $ spent_time += 10
                scene BG char Alice bed-morning-02
                $ renpy.show('Alice sleep-morning-closer '+pose3_2)
                $ renpy.show('other Alice sleep-morning-closer '+pose3_2+alice.dress)
                if 'smoke' in flags and flags['smoke'] == 'sleep':
                    if pose3_2 == '01':
                        Max_05 "Ох, от такого вида в голове остаются лишь самые пошлые мысли... Как же я хочу помять эти сиськи! И стянуть эти трусики... и ещё... пожалуй, пока она не проснулась, тихонько отсюда уйти." nointeract
                    elif pose3_2 == '02':
                        Max_03 "О, да! Не лечь и не приобнять эту нежную попку – настоящее преступление... Как и поласкать эти аппетитные сосочки! Только вот Алиса посчитает иначе и оторвёт мне голову прямо здесь. Так что лучше потихоньку уходить..." nointeract
                    else:
                        Max_02 "Вот чёрт! С каким же огромным удовольствием я бы сел рядом с ней, запустил свои руки в её трусики и мял эти упругие сисечки всё утро... Эх, хороша сестрёнка, но пора уходить... Если она проснётся, мне точно не поздоровится." nointeract
                else:
                    if pose3_2 == '01':
                        Max_05 "Ох, от такого вида в голове остаются лишь самые пошлые мысли... Как же я хочу помять эту попку! И стянуть эти трусики... и ещё... пожалуй, пока она не проснулась, тихонько отсюда уйти." nointeract
                    elif pose3_2 == '02':
                        Max_03 "О, да! Не лечь и не приобнять эту нежную попку – настоящее преступление... Только вот Алиса посчитает иначе и оторвёт мне голову прямо здесь. Так что лучше потихоньку уходить..." nointeract
                    else:
                        Max_02 "Вот чёрт! С каким же огромным удовольствием я бы сел рядом с ней, запустил свои руки под её белье и ласкал эти упругие сисечки всё утро... Эх, хороша сестрёнка, но пора уходить... Если она проснётся, мне точно не поздоровится." nointeract
                $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
        "{i}уйти{/i}":
            pass
    jump Waiting


label alice_shower:
    scene location house bathroom door-morning
    if peeping['alice_shower'] == 3:
        Max_00 "Алиса меня уже поймала сегодня. Не стоит злить её ещё больше, а то точно что-нибудь оторвет."
        return
    elif peeping['alice_shower'] == 1:
        Max_00 "Я уже подсматривал сегодня за Алисой. Не стоит искушать судьбу слишком часто."
        return
    elif  peeping['alice_shower'] == 2:
        Max_00 "Алиса меня и так сегодня едва не поймала. Не стоит искушать судьбу слишком часто."
        return
    elif peeping['alice_shower'] > 3:
        menu:
            Max_00 "Алиса сейчас принимает душ..."
            "{i}уйти{/i}":
                return
    else:
        $ peeping['alice_shower'] = 4
        menu:
            Max_00 "Похоже, Алиса принимает душ..."
            "{i}заглянуть со двора{/i}":
                if sorry_gifts['alice'].owe:
                    Max_10 "С радостью бы подсмотрел за голенькой сестрёнкой, но это слишком опасно! Сперва нужно подарить то, что обещал..."
                    $ current_room, prev_room = prev_room, current_room
                    jump AfterWaiting
                jump .start_peeping
            "{i}воспользоваться стремянкой{/i}" if flags['ladder'] > 2:
                jump .ladder
            "{i}уйти{/i}":
                return

    label .start_peeping:
        $ Skill('hide', 0.03)
        $ __ran1 = renpy.random.randint(1, 4)

        $ _ch1 = GetChance(mgg.stealth, 3, 900)
        $ _ch2 = GetChance(mgg.stealth, 2, 900)
        scene image ('Alice shower 0'+str(__ran1))
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Ого... Голая Алиса всего в паре метров от меня! Как же она хороша... Главное, чтобы она меня не заметила, а то ведь убьёт на месте."
            "{i}продолжить смотреть\n{color=[_ch1.col]}(Скрытность. Шанс: [_ch1.vis]){/color}{/i}":
                jump .closer_peepeng
            "{i}взглянуть со стороны\n{color=[_ch2.col]}(Скрытность. Шанс: [_ch2.vis]){/color}{/i}":
                jump .alt_peepeng
            "{i}немного пошуметь{/i}" if 1 <= len(sorry_gifts['alice'].give) < 4:
                jump .pinded
            "{i}запустить паука к Алисе{/i}" if items['spider'].have:
                jump .spider
            "{i}уйти{/i}":
                jump .end

    label .spider:
        $ renpy.scene()
        $ renpy.show('Max spider-bathroom 01'+mgg.dress)
        if not _in_replay:
            $ items['spider'].have = False
            $ SpiderKill = 1
            $ SpiderResp = 2
            $ spent_time += 10
        menu:
            Max_03 "Давай, паучок, вперёд! Я хочу, чтобы ты познакомился с моей очаровательной сестрёнкой. Характер у неё правда так себе, но думаю, вы оба поладите..."
            "{i}спрятаться{/i}":
                pass
        scene BG char Max spider-bathroom-00
        $ renpy.show('Max spider-bathroom 02'+mgg.dress)
        Max_01 "Похоже, я успел обойти ванную комнату через дом ещё до криков Алисы... Это хорошо, значит Алиса вот-вот должна заметить паука! Остаётся только немного..."
        Alice "{b}Алиса:{/b} А-а-а-а-а!!! Вот чёрт... Охренеть!"
        Max_02 "...подождать."
        if not _in_replay:
            $ poss['spider'].OpenStage(3)
        scene BG char Alice spider-bathroom-00
        $ renpy.show('Alice spider-shower 01'+renpy.random.choice(['a','b','c']))
        Alice_06 "Боже мой, какой кошмар... И что мне теперь с этим пауком делать... Ну почему эти твари лезут именно ко мне? Может быть, он уползёт..."
        $ renpy.show('Max spider-bathroom 03'+mgg.dress)
        Max_07 "Алиса, ты кричала... Что случилось?"
        $ renpy.show('Alice spider-shower 02'+renpy.random.choice(['a','b','c']))
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
            Alice_06 "Макс! Вот чёрт, ещё и ты меня напугал! Ко мне здоровенный паук в душ заполз..."
            Max_04 "Не переживай! Сейчас я его поймаю и выброшу... И ты спокойно домоешься."
            Alice_13 "Нет уж, я не смогу пока зайти обратно... Мне нужно время, чтобы перестать думать обо всём этом кошмаре. Лучше принеси мне полотенце, оно там, в ванной... А то слишком уж тебе повезло на меня голую глазеть!"
            menu:
                Max_01 "Хорошо, сейчас принесу. Никуда не уходи..."
                "{i}принести Алисе полотенце{/i}":
                    pass
        scene BG char Alice spider-bathroom-01
        $ renpy.show('Alice spider-shower 03'+renpy.random.choice(['a','b','c']))
        Alice_12 "Макс, ну ты где там?! Только смотри, чтобы этого монстра не было на моём полотенце! Иначе тебе будет очень-очень больно..."
        $ renpy.show('Max spider-bathroom 04'+mgg.dress)
        if not _in_replay:
            $ spent_time += 10
        menu:
            Max_03 "Вот я и вернулся! С полотенцем всё в порядке, вот, держи."
            "{i}отдать Алисе полотенце{/i}":
                $ renpy.show('Alice spider-shower 04'+renpy.random.choice(['a','b']))
                $ renpy.show('Max spider-bathroom 06'+mgg.dress)
                Alice_07 "Ох, Макс, спасибо тебе огромное! Думала, ты будешь прикалываться, но ты можешь временами вести себя, не как озабоченный... Это приятно."
                Max_04 "Да ладно, это ерунда, обращайся."
                Alice_03 "Ну всё, я пошла... Только не забудь паука вышвырнуть из ванной, хорошо?!"
                Max_01 "Да. Не забуду..."
                $ AddRelMood('alice', 10, 50, 3)

            "{i}отдать Алисе полотенце (выронив его из одной руки){/i}":
                $ renpy.show('Alice spider-shower 05'+renpy.random.choice(['a','b','c','d']))
                $ renpy.show('Max spider-bathroom 05'+mgg.dress)
                Alice_14 "Макс!!! Ах ты... Ну-ка дай сюда полотенце!!!"
                show Alice spider-shower 04b
                $ renpy.show('Max spider-bathroom 06'+mgg.dress)
                Max_08 "Ой! Извини, я..."
                $ _ch1 = GetChance(mgg.social, 3, 900)
                menu:
                    Alice_17 "Какого чёрта, Макс?! Что за шуточки! Или ты безрукий? Живо признавайся, ты специально это сделал?!"
                    "Конечно нет! Оно случайно выскочило из руки! {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}":
                        pass
                if RandomChance(_ch1.ch) or _in_replay:
                    $ Skill('social', 0.2)
                    Alice_12 "[succes!t]Ну ты и криворукий, Макс! Даже такую простую вещь не можешь сделать, не накосячив... Всё, я пошла! И паука вышвырни из ванной, если конечно и он у тебя из рук не выскочит!"
                    Max_00 "Да это случайно вышло!"
                    Alice_05 "Ну да, конечно..."
                else:
                    $ Skill('social', 0.1)
                    Alice_16 "[failed!t]Я тебе не верю! Наверняка ты это сделал специально, чтобы поглазеть на меня! Твоё счастье, что я не могу знать этого точно... А так бы врезала тебе между ног!"
                    Max_10 "Так получилось! Я не хотел..."
                    Alice_17 "Да иди ты, Макс!"
                    $ AddRelMood('alice', -15, -75)
        $ renpy.end_replay()
        jump .end

    label .alt_peepeng:
        if not RandomChance(_ch2.ch):
            jump .not_luck
        $ spent_time += 10
        $ peeping['alice_shower'] = 1
        $ Skill('hide', 0.2)
        $ alice.dress_inf = '00aa'
        $ __ran1 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Alice shower-alt 0'+str(__ran1))
        show FG shower-water
        if __ran1 % 2 > 0:
            Max_01 "[undetect!t]Супер! С распущенными волосами моя старшая сестрёнка становится очень сексуальной... Ухх, помылить бы эти сисечки, как следует..."
        else:
            Max_01 "[undetect!t]О, да... Перед мокренькой Алисой сложно устоять! Особенно, когда она так соблазнительно крутит своей попкой..."
        jump .end

    label .closer_peepeng:
        $ spent_time += 10
        if RandomChance(_ch1.ch):
            $ peeping['alice_shower'] = 1
            $ Skill('hide', 0.2)
            $ alice.dress_inf = '00aa'
            $ __ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            $ renpy.show('Alice shower-closer 0'+str(__ran1))
            show FG shower-closer
            if __ran1 % 2 > 0:
                Max_01 "[undetect!t]Супер! С распущенными волосами моя старшая сестрёнка становится очень сексуальной... Ухх, помылить бы эти сисечки, как следует..."
            else:
                Max_01 "[undetect!t]О, да... Перед мокренькой Алисой сложно устоять! Особенно, когда она так соблазнительно крутит своей попкой..."
            jump .end
        else:
            jump .not_luck

    label .not_luck:
        if RandomChance(_ch1.ch) or len(sorry_gifts['alice'].give) > 3:
            $ peeping['alice_shower'] = 2
            $ Skill('hide', 0.1)
            $ alice.dress_inf = '00aa'
            $ __ran1 = renpy.random.randint(7, 8)
            scene BG shower-closer
            $ renpy.show('Alice shower-closer 0'+str(__ran1))
            show FG shower-closer
            Max_09 "{color=[orange]}{i}Кажется, Алиса что-то заподозрила!{/i}{/color}\nОх, чёрт! Нужно скорее уносить ноги, пока они ещё есть..."
            jump .end
        else:
            jump .pinded

    label .pinded:
        $ peeping['alice_shower'] = 3
        $ punreason[1] = 1
        $ Skill('hide', 0.05)
        $ __ran1 = renpy.random.choice(['09', '10'])
        scene BG shower-closer
        $ renpy.show('Alice shower-closer '+__ran1)
        show FG shower-closer
        menu:
            Alice_12 "[spotted!t]Макс!!! Ты за мной подглядываешь?! Ты труп! Твоё счастье, что я сейчас голая... Но ничего, я маме всё расскажу, она тебя накажет!"
            "{i}Бежать{/i}":
                jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        if alice.dress_inf != '04aa':
            $ __r1 = {'04ca':'a', '04da':'b', '02fa':'c', '00a':'d'}[alice.dress_inf]
        else:
            if alice.nopants:
                $ __r1 = renpy.random.choice(['b', 'd'])
            else:
                $ __r1 = renpy.random.choice(['a', 'c'])
            $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[__r1]

        scene BG bathroom-morning-00
        $ renpy.show('Alice bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1)
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        if flags['smoke'] == 'not_nopants' and not flags['noted']:
            # Алиса в трусиках, хотя должна быть без них и Макс ещё об этом не знает
            Max_00 "Посмотреть на Алису всегда приятно, но почему она в трусиках? Ведь мы же с ней договаривались..."
            Max_00 "Непорядок. Нужно с этим что-то делать..."
            $ added_mem_var('alice_not_nopants')
            $ flags['noted'] = True
        elif __r1 == 'a':
            Max_02 "Да-а... Может Алиса и в халатике, но сиськи её видны просто замечательно! А они у неё - что надо..."
        elif __r1 == 'b':
            Max_05 "Ого! Кто бы мог подумать, что курение может принести пользу в виде моей сестрёнки, не носящей трусики. Как же она хороша..."
        elif __r1 == 'c':
            Max_04 "Прекрасно! Алиса сегодня без халатика... в одних трусиках... Глядя на эту красоту, можно мечтать лишь об одном!"
        else:
            Max_06 "Вау! Алиса сегодня совершенно голая! Как мы и договорились, трусики она не носит и даже не представляет, что тем самым дарит мне возможность любоваться всеми её прелестями..."

        Max_00 "Ладно, хорошего понемногу, а то ещё заметит меня здесь кто-нибудь..."

    label .end:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting


label alice_rest_morning:
    scene BG char Alice morning
    $ renpy.show('Alice morning 01'+alice.dress)
    $ persone_button1 = 'Alice morning 01'+alice.dress+'b'
    return


label alice_rest_evening:
    if get_format_blog()>0:
        jump alice_blog_lingerie

    scene BG char Alice evening
    $ renpy.show('Alice evening 01'+alice.dress)
    $ persone_button1 = 'Alice evening 01'+alice.dress+'b'
    return


label alice_dressed_shop:
    scene location house aliceroom door-morning
    if peeping['alice_dressed'] == 0:
        $ peeping['alice_dressed'] = 1
        menu:
            Max_09 "Кажется, все собираются на шоппинг и Алиса сейчас переодевается..."
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кто там? Я переодеваюсь!"
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Даже не вздумай! Прибью на месте! Жди там. А лучше свали подальше, чтобы под дверью не сопел тут."
                        Max_00 "Хорошо..."
                    "Хорошо, я подожду...":
                        pass
            "{i}заглянуть в окно{/i}":
                $ __list = {
                        'a':['01', '02', '03'],
                        'b':['02',],
                        'c':['02','03'],
                        'd':['02','03','05']
                    }[alice.dress]
                $ __ran1 = renpy.random.choice(__list)

                $ __suf = 'a' if all([__ran1 != '01', 'smoke' in talk_var, flags['smoke'] == 'nopants']) else ''
                if flags['smoke'] == 'not_nopants':
                    $ added_mem_var('alice_not_nopants')
                    $ flags['noted'] = True

                $ alice.dress_inf = {
                        '01':'02b',
                        '02':'02a' if __suf else '02d',
                        '03':'02c' if __suf else '02e',
                        '05':'02h',
                    }[__ran1]

                if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
                    scene BG char Alice voyeur-01
                    $ renpy.show('Alice voyeur alt-'+__ran1+__suf)
                    $ renpy.show('FG voyeur-morning-01'+mgg.dress)
                else:
                    scene BG char Alice voyeur-00
                    $ renpy.show('Alice voyeur '+__ran1+__suf)
                    $ renpy.show('FG voyeur-morning-00'+mgg.dress)

                $ Skill('hide', 0.03)
                if flags['smoke'] == 'not_nopants' and __ran1 not in ['01', '05']:
                    # Макс видит, что на Алисе трусики, когда их быть не должно
                    Max_01 "Ага! Алиса одевается на шопинг. И похоже, пойдёт она в трусиках, а не должна... Считай, сестрёнка, ты попала! Но не сейчас... Сейчас мне лучше уходить, пока никто не заметил."
                    $ added_mem_var('alice_not_nopants')
                elif flags['smoke'] == 'nopants' and __ran1 not in ['01', '05']:
                    # Макс видит, что Алиса соблюдает договоренность
                    Max_05 "Ого! Алиса даже на шопинг пойдёт без трусиков! Интересно, что она скажет маме в кабинке для переодевания, если та это заметит? Но лучше буду гадать об этом в другом месте, а то меня заметят..."
                elif __ran1 in ['02', '03']:
                    # Если нет договоренности по поводу трусов
                    Max_04 "Алиса переодевается... Какая соблазнительная попка у неё... Ммм! Так. Пора бы сваливать. Вдруг, кто-то заметит!"
                else:
                    # Сиськи , однако
                    Max_03 "О, какой вид! Да, сестрёнка, такими классными и голыми сиськами грех не покрасоваться перед зеркалом... Однако, пора сваливать. Вдруг, кто-то заметит!"
            "{i}уйти{/i}":
                pass
        $ spent_time += 10
        jump Waiting
    return


label alice_dishes:
    scene BG crockery-morning-00
    $ renpy.show('Alice crockery-morning 01'+alice.dress)
    $ persone_button1 = 'Alice crockery-morning 01'+alice.dress+'b'
    return


label alice_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show('Alice crockery-closer '+pose3_2+alice.dress)
    return


label alice_read:
    scene BG reading
    $ renpy.show('Alice reading '+pose3_2+alice.dress)
    $ persone_button1 = 'Alice reading '+pose3_2+alice.dress+'b'
    return


label alice_read_closer:
    scene BG reading
    $ renpy.show('Alice reading-closer 01'+alice.dress)
    return


label alice_dressed_friend:
    scene location house aliceroom door-day
    if peeping['alice_dressed'] == 0:
        $ peeping['alice_dressed'] = 1
        menu:
            Max_09 "Кажется, Алиса куда-то собирается..."
            "{i}постучаться{/i}":
                menu:
                    Alice "{b}Алиса:{/b} Кто там? Я переодеваюсь!"
                    "Это я, Макс. Можно войти?":
                        Alice "{b}Алиса:{/b} Даже не вздумай! Прибью на месте! Жди там. А лучше свали подальше, чтобы под дверью не сопел тут."
                        Max_00 "Хорошо..."
                    "Хорошо, я подожду...":
                        pass
            "{i}заглянуть в окно{/i}":
                $ __list = {
                        'a':['01', '02', '03'],
                        'b':['02',],
                        'c':['02','03'],
                        'd':['02','03','05']
                    }[alice.dress]
                $ __ran1 = renpy.random.choice(__list)

                $ __suf = 'a' if all([__ran1 != '01', 'smoke' in talk_var, flags['smoke'] == 'nopants']) else ''
                if flags['smoke'] == 'not_nopants':
                    $ added_mem_var('alice_not_nopants')
                    $ flags['noted'] = True

                $ alice.dress_inf = {
                        '01':'02b',
                        '02':'02a' if __suf else '02d',
                        '03':'02c' if __suf else '02e',
                        '05':'02h',
                    }[__ran1]

                if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
                    scene BG char Alice voyeur-01
                    $ renpy.show('Alice voyeur alt-'+__ran1+__suf)
                    $ renpy.show('FG voyeur-morning-01'+mgg.dress)
                else:
                    scene BG char Alice voyeur-00
                    $ renpy.show('Alice voyeur '+__ran1+__suf)
                    $ renpy.show('FG voyeur-morning-00'+mgg.dress)

                $ Skill('hide', 0.03)
                if flags['smoke'] == 'not_nopants' and __ran1 not in ['01', '05']:
                    # Макс видит, что на Алисе трусики, когда их быть не должно
                    $ added_mem_var('alice_not_nopants')
                    Max_01 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала! Но не сейчас... Сейчас мне лучше уходить, пока никто не заметил."
                    $ added_mem_var('alice_not_nopants')
                elif flags['smoke'] == 'nopants' and __ran1 not in ['01', '05']:
                    # Макс видит, что Алиса соблюдает договоренность
                    Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Надеюсь, кто-то это заметит там, куда она идёт... А чтобы меня никто не заметил, лучше уходить!"
                elif __ran1 in ['02', '03']:
                    # Если нет договоренности по поводу трусов
                    Max_04 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Но без них было бы лучше... Так. Пора бы сваливать. Вдруг, кто-то заметит!"
                else:
                    # Сиськи , однако
                    Max_03 "О, какой вид! Да, сестрёнка, такими классными и голыми сиськами грех не покрасоваться перед зеркалом... Однако, пора сваливать. Вдруг, кто-то заметит!"

            "{i}уйти{/i}":
                pass
        # $ current_room, prev_room = prev_room, current_room
        $ spent_time = 10
        jump Waiting
    return


label alice_dressed_club:
    scene location house aliceroom door-evening
    if peeping['alice_dressed'] != 0:
        return

    $ peeping['alice_dressed'] = 1
    menu:
        Max_00 "{i}( Кажется, Алиса собирается в ночной клуб... ){/i}"
        "{i}постучаться{/i}":
            jump .knock
        "{i}заглянуть в окно{/i}":
            ## показываем фон и спрайт в зависимости от ношения трусиков
            if 'smoke' in talk_var and flags['smoke'] == 'nopants':
                $ __suf = 'a'
                $ alice.dress_inf = '06b'
            else:
                $ __suf = ''
                $ alice.dress_inf = '06a'
            if 'smoke' in talk_var and flags['smoke'] == 'not_nopants':
                $ added_mem_var('alice_not_nopants')
                $ flags['noted'] = True
            if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
                scene BG char Alice voyeur-01
                $ renpy.show('Alice voyeur alt-04'+__suf)
                $ renpy.show('FG voyeur-morning-01'+mgg.dress)
            else:
                scene BG char Alice voyeur-00
                $ renpy.show('Alice voyeur 04'+__suf)
                $ renpy.show('FG voyeur-morning-00'+mgg.dress)
            $ Skill('hide', 0.03)

            ## у нас 3 варианта:
            if flags['smoke'] == 'not_nopants':
                ## Алиса в трусиках, но их быть не должно
                $ added_mem_var('alice_not_nopants')
                Max_01 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Вот только быть их на ней не должно... Считай, сестрёнка, ты попала! Но не сейчас... Сейчас мне лучше уходить, пока никто не заметил."
            elif flags['smoke'] == 'nopants':
                ## Алиса без трусиков, как и должна
                Max_05 "Супер! Алиса не надевает трусики... И правильно делает! Это платье без трусиков смотрится гораздо лучше... Интересно, в клубе на это кто-нибудь обратит внимание? А чтобы меня никто не заметил, лучше уходить!"
            else:
                ## Алиса в трусиках. Договоренностей нет
                Max_04 "Алиса переодевается... Трусики хорошо смотрятся на её попке. Но без них это платье смотрелось бы гораздо лучше... Так. Пора бы сваливать. Вдруг, кто-то заметит!"

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
                $ flags['alice.drink'] = 1
                menu:
                    Alice_05 "Люблю... И что, никакого подвоха? Просто взял и подарил конфетку на дорожку?"
                    "Ну, можешь трусы показать...":
                        Alice_02 "Может быть, мне их ещё и снять для тебя? Давай, вали уже, извращенец. А за конфетку спасибо..."
                    "Да, никакого подвоха!":
                        Alice_07 "Вот это да! Ну, спасибо тогда... А теперь вали. Я ещё не закончила..."
                $ give_choco()
                jump .end
            # "{i}дать две конфеты {/i} ## убеждение ##" if kol_choco > 1 and poss['nightclub'].stages[7].used:
            #     $ flags['alice.drink'] = 2
    label .end:
        Max_04 "Ага..."
        $ spent_time += 10
        $ cam_flag.append('alice_dressed')
        jump Waiting


label alice_sun:
    if talk_var['sun_oiled']:
        scene BG char Alice sun-alone 01
        if talk_var['sun_oiled'] == 2:
            show Alice sun-alone 01a
        else:
            show Alice sun-alone 01
    else:
        scene BG char Alice sun
        $ renpy.show('Alice sun '+pose2_2+alice.dress)
        $ persone_button1 = 'Alice sun '+pose2_2+alice.dress+'b'
    return


label alice_swim:
    scene image 'Alice swim '+pose3_2+alice.dress
    $ persone_button1 = 'Alice swim '+pose3_2+alice.dress+'b'
    return


label alice_cooking_dinner:
    scene BG cooking-00
    $ renpy.show('Alice cooking 01'+alice.dress)
    $ persone_button1 = 'Alice cooking 01'+alice.dress+'b'
    return


label alice_cooking_closer:
    scene BG cooking-01
    $ renpy.show('Alice cooking-closer '+pose3_2+alice.dress)
    return


label alice_tv:
    scene BG lounge-tv-00
    $ renpy.show('Alice tv '+pose3_2+alice.dress)
    $ persone_button1 = 'Alice tv '+pose3_2+alice.dress+'b'
    return


label alice_tv_closer:
    scene BG lounge-tv-01
    $ renpy.show('Alice tv-closer '+pose3_2+alice.dress)
    $ renpy.show('Max tv 00'+mgg.dress)
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
    $ __mood = 0
    if 'smoke' in talk_var and flags['smoke'] == 'sleep':
        $ __suf = 't'
        $ __toples = True
    else:
        $ __suf = ''
        $ __toples = False
    if flags['smoke'] == 'not_sleep':
        $ flags['noted'] = True

    scene BG char Alice spider-night-01
    $ renpy.show('Alice spider-night 01-'+renpy.random.choice(['01', '02', '03'])+alice.dress+__suf)
    Alice_13 "Макс!"

    scene BG char Alice spider-night-02
    $ renpy.show('Max spider-night 02-'+renpy.random.choice(['01', '02', '03']))
    $ renpy.show('Alice spider-night 02-01'+alice.dress+__suf)
    menu:
        Alice_12 "Макс! Макс! Вставай быстрее! Мне нужна помощь!"
        "Что случилось?":
            pass
        "Разбирайся сама..." if not _in_replay:
            jump .goaway

    show Max spider-night 02-04
    menu:
        Alice_06 "Макс, помоги. В моей комнате огромный такой, просто гигантский паук! Убей его, пожалуйста!"
        "Ну, пойдём посмотрим...":
            jump .help
        "Паук? Ерунда какая. Сама разбирайся с ним..." if not _in_replay:
            jump .goaway

    label .goaway:
        scene BG char Max bed-night-01
        $ renpy.show('Max sleep-night '+pose3_3)
        menu:
            Max_09 "Бегает ещё, кричит что-то... Совсем сдурела..."
            "{i}спать до утра{/i}":
                $ __mood -= 20
                $ spent_time = 10
                $ AddRelMood('alice', 0, __mood)
                return

    label .help:
        scene BG char Alice spider-night-03
        $ renpy.show('Alice spider-night 03-'+renpy.random.choice(['01', '02', '03'])+alice.dress+__suf)
        show Max spider-night 03-01

        $ _ch1 = GetChance(mgg.social, 5, 900)
        $ _ch2 = GetChance(mgg.social, 3, 900)
        $ _ch3 = GetChance(mgg.social, 2, 900)

        menu:
            Alice_13 "Макс, Макс! Вот он! Убей его, скорее!!!"
            "А что мне за это будет?" if __suf == '' and not flags['noted']:  # Вариант недоступен, если Алиса без лифчика или нарушает договоренность и Макс об этом знает
                show Max spider-night 03-02
                $ renpy.show('Alice spider-night 03-04'+alice.dress+__suf)
                menu:
                    Alice_12 "Что ты хочешь за смерть этого паука?"
                    "Давай $10! {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}":
                        if RandomChance(_ch1.ch) or _in_replay:
                            jump .money
                        else:
                            jump .fail
                    "Покажи сиськи! {color=[_ch2.col]}(Убеждение. Шанс: [_ch2.vis]){/color}":
                        if RandomChance(_ch2.ch) or _in_replay:
                            jump .tits
                        else:
                            jump .fail
                    "Сними верх! {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}":
                        if RandomChance(_ch3.ch) or _in_replay:
                            jump .toples
                        else:
                            jump .fail
                    "А, ничего. Так поймаю...":
                        $ __mood += 100
                        jump .spider
            "А что мне за это будет?" if __suf != '':  # Алиса без лифчика
                show Max spider-night 03-02
                $ renpy.show("Alice spider-night 03-04"+alice.dress+__suf)
                Alice_06 "Макс, не наглей! Я и так перед тобой тут в одних трусиках... Тебе этого мало что ли?!"
                Max_07 "Ну, я вижу, что условия нашей договорённости ты соблюдаешь, только вот к поимке паука это никак не относится."
                Alice_12 "И чего тебе, в таком случае, ещё от меня надо?"
                Max_01 "Видишь ли, глаза совсем заспанные, никак не могу разглядеть паука... Но думаю твои прекрасные сосочки мне с этим помогут!"
                menu:
                    Alice_15 "Ах, так! Значит то, что договорённость я соблюдаю, ты видишь, а вот здоровенного паука на моей кровати нет?!"
                    "На красивое глаза легче открываются... {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}":
                        if RandomChance(_ch3.ch) or _in_replay:
                            jump .toples
                        else:
                            jump .fail
                    "Давай уже показывай сиськи!" if not _in_replay:
                        jump .fail
                jump .spider
            "Хорошо, где он там..." if not flags['noted']:
                $ __mood += 100
                jump .spider
            "Паука-то я поймаю, только вот кое-кто нарушает уговор! Или может я не прав?!" if flags['noted']:
                if flags['smoke'] == 'not_sleep':    # Алиса должна спать без лифчика
                    Alice_12 "Ну забыла я снять лифчик перед сном, просто по привычке... Подумаешь, какое большое преступление!"
                    Max_09 "Конечно большое! Ты просто наплевала на наш уговор, а я ведь твою задницу спас от маминой хлёсткой руки... Я его тоже тогда соблюдать не стану, так что завтра получишь! Приятных снов..."
                    Alice_14 "Нет, нет, нет! Ты куда собрался?! У меня же паук на кровати!"
                    Max_07 "Что тут скажешь... Успехов тебе!"
                    Alice_06 "Ну не надо так, Макс! Я не буду больше нарушать наш уговор, только избавься от паука... Пожалуйста!"
                else:   # Алиса должна днем ходить без трусов
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
                scene BG char Alice spider-night-05
                $ renpy.show('Alice spider-night 05-'+renpy.random.choice(['01', '02', '03'])+alice.dress)
                Alice_06 "Ну вот... смотри... И не говори, что этого мало... большего не покажу! Доволен?"
                Max_05 "О да, я очень доволен! Попка у тебя просто супер, сестрёнка!"
                Alice_12 "Всё! Посмотрел и хватит, давай уже, лови этого паука!"
                Max_04 "Ладно, теперь можно и поймать..."
                $ punalice[2][0]=10  #ставим на три дня раньше требование Макса, чтобы ослушание Алисы наступило раньше, чем при требовании во время курения
                $ flags['smoke'] = flags['smoke.request']
                $ flags['noted'] = False
                if flags['smoke.request'] == 'nopants':
                    $ alice.nopants = True
                elif flags['smoke.request'] == 'sleep':
                    $ alice.sleeptoples = True
                    $ alice.dress = 'b'
                jump .spider

    label .fail:
        $ Skill('social', 0.1)
        $ renpy.show('Alice spider-night 03-05'+alice.dress+__suf)
        Alice_17 "[failed!t]Что?! Да я сама тебя сейчас придушу! Тебя-то я не боюсь! Быстро убил его! Или он, или ты. Кто-то из вас умрёт сегодня!"
        Max_08 "Ух, какая ты кровожадная. Ну ладно..."
        $ __mood -= 100
        jump .spider

    label .money:
        $ renpy.show('Alice spider-night 03-06'+alice.dress)
        $ Skill('social', 0.2)
        Alice_16 "[succes!t]Ну ты и хам, Макс! Ладно, держи $10, только убей его, быстрее!!!"
        Max_04 "Деньги всегда пригодятся! Ладно, где этот твой паук..."
        $ __mood -= 20
        $ mgg.ask(0)
        jump .spider

    label .tits:
        show Max spider-night 03-03
        $ Skill('social', 0.2)
        if alice.GetMood()[0] < 3:
            $ __mood -= 50
            $ renpy.show('Alice spider-night 03-'+renpy.random.choice(['07', '08'])+alice.dress)
            Alice_14 "[succes!t]Ах! Ну ты хам... Ладно, смотри быстро. И убей его уже, наконец!"
        else:
            $ renpy.show('Alice spider-night 03-09'+alice.dress)
            Alice_09 "[succes!t]Ах! Ну и хам же ты, Макс... Ладно, любуйся, я сегодня добрая. И убей его уже, наконец!"
        Max_04 "Сиськи - что надо! Ладно, где этот твой паук..."
        jump .spider

    label .toples:
        $ __toples = True
        $ Skill('social', 0.2)
        show Max spider-night 03-03
        $ renpy.show('Alice spider-night 03-'+renpy.random.choice(['10', '11', '12'])+alice.dress)
        if alice.GetMood()[0] < 3:
            $ __mood -= 50
        Alice_15 "[succes!t]Ах! Ну ты хам... Ладно... Ну что, доволен, извращенец? А теперь иди, убей его уже, наконец!"
        Max_05 "Отличные сиськи! Ладно, где этот твой паук..."
        jump .spider

    label .spider:
        scene BG char Alice spider-night-04
        show Max spider-night 04-01
        if __toples:
            $ renpy.show('Alice spider-night 04-'+renpy.random.choice(['04', '05', '06'])+alice.dress)
        else:
            $ renpy.show('Alice spider-night 04-'+renpy.random.choice(['01', '02', '03'])+alice.dress)
        $ _ch1 = GetChance(mgg.social, 3, 900)
        menu:
            Max_07 "Ага, попался! Пожалуй, вот что я сделаю..."
            "{i}оставлю этого паука себе{/i}":
                menu:
                    Alice_16 "Макс! Ты должен его убить! А не то я подумаю, что это твоих рук дело... Докажи, что это был не ты!"
                    "Я не буду его убивать!":
                        menu:
                            Alice_17 "Ах так... Ну, тогда я обижусь на тебя! Всё, вали отсюда!"
                            "{i}вернуться в кровать{/i}":
                                $ renpy.end_replay()
                                $ __mood -= 100
                                $ spent_time = 30
                                $ AddRelMood('alice', 0, __mood)
                                $ SpiderKill = 0
                                $ SpiderResp = 0
                                $ items['spider'].have = True
                                return
                    "Пусть живёт. Я пойду и выкину его с балкона за ограду, чтобы он обратно не приполз.\n{color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}":
                        show Max spider-night 04-02
                        if RandomChance(_ch1.ch) or _in_replay:
                            $ Skill('social', 0.2)
                            Alice_12 "[succes!t]Ладно, Макс, уговорил. Только сделай так, чтобы его и близко к этому дому не было..."
                            menu:
                                Alice_13 "Всё, хватит уже сидеть на моей кровати, иди отсюда. Я хочу спать!"
                                "{i}вернуться в кровать{/i}":
                                    $ renpy.end_replay()
                                    $ __mood += 50
                                    $ spent_time = 30
                                    $ AddRelMood('alice', 0, __mood)
                                    $ SpiderKill = 0
                                    $ SpiderResp = 0
                                    $ items['spider'].have = True
                                    return
                        else:
                            $ Skill('social', 0.1)
                            $ __mood -50
                            Alice_16 "[failed!t]Нет уж, Макс! Ты его убиваешь прямо здесь и сейчас или я сильно на тебя обижусь! Выбирай..."
                            Max_09 "Ладно, будет тебе! Раз ты такая кровожадная..."
                            jump .kill
                    "{i}выбросить с балкона{/i}":
                        jump .let_go
                    "{i}убить паука{/i}":
                        jump .kill
            "{i}выброшу этого паука с балкона{/i}":
                jump .let_go
            "{i}убью этого паука{/i}":
                jump .kill
    label .let_go:
        scene BG char Alice spider-balcony
        menu:
            Alice_13 "Макс! Я тебя просила убить его, а не отпускать! Спасибо, конечно, что убрал его из комнаты, но вдруг он вернётся?.. Всё, иди отсюда. Я хочу спать!"
            "{i}вернуться в кровать{/i}":
                $ renpy.end_replay()
                $ spent_time = 30
                $ __mood -= 50
                $ AddRelMood('alice', 0, __mood)
                $ SpiderKill = 0
                $ SpiderResp = 1
                return

    label .kill:
        show Max spider-night 04-03
        menu:
            Alice_01 "Так ему! Спасибо, Макс! Ты мой спаситель. А теперь иди отсюда, я спать хочу!"
            "{i}вернуться в кровать{/i}":
                $ renpy.end_replay()
                $ __mood += 100
                $ AddRelMood('alice', 0, __mood)
                $ spent_time = 30
                $ SpiderKill = 2
                $ SpiderResp = 3
                return


label alice_smoke:

    scene BG char Alice smoke

    if talk_var['smoke']:
        $ renpy.show('Alice smoke '+pose3_3+alice.dress)
        $ persone_button1 = 'Alice smoke '+pose3_3+alice.dress
        return
    else:
        $ renpy.show('Alice smoke '+pose3_3+alice.dress)

    $ talk_var['smoke'] = True

    if dcv['smoke'].done:
        if dcv['smoke'].stage == 0:
            jump first_talk_smoke  # первый разговор про курение
        elif dcv['smoke'].stage == 1:
            jump second_talk_smoke  # второй разговор про курение
        elif talk_var['alice.pun'] == 0:
            jump smoke_nofear  # разговор во время курения до наказаний
        else:
            if flags['smoke'] is None:
                # нет текущих требований
                jump smoke_fear
            elif flags['smoke'] == 'toples':
                # текущее требование курить топлес. Выполняется
                jump smoke_toples
            elif flags['smoke'] == 'not_toples':
                #  текущее требование курить топлес. Не выполняется
                jump smoke_not_toples
            elif flags['smoke'] == 'sleep' or flags['smoke'] == 'not_sleep':
                # текущее требование спать топлес.
                # если макс знает о нарушениях, решает все через паука.
                jump smoke_sleep
            elif flags['smoke'] == 'nopants' or (flags['smoke'] == 'not_nopants' and not flags['noted']):
                # текущее требование ходить днем без трусов. Выполняется или Макс не знает о нарушении
                jump smoke_nopants
            elif flags['smoke'] == 'not_nopants' and flags['noted']:
                # текущее требование ходить днем без трусов. Не выполняется
                jump smoke_not_nopants
            elif flags['smoke'] == 'nojeans':
                # текущее требование ходить беж джинсов, когда Ани нет дома
                jump smoke_nojeans

    return


label alice_after_club:
    scene location house bathroom door-evening
    if peeping['alice_bath'] != 0:
        return

    $ peeping['alice_bath'] = 1
    if tm[-2:] > '10':
        Max_07 "После клуба Алиса сразу пошла в ванную. Интересно, в каком она состоянии?" nointeract
    else:
        Max_07 "Алиса только что вернулась из клуба и сразу забежала в ванную. Интересно, в каком она состоянии?" nointeract

    $ __list = [(_("{i}постучаться{/i}"), 1), ]
    if 'ladder' not in flags or flags['ladder'] < 2:
        $ __list.append((_("{i}заглянуть со двора{/i}"), 2))
    if items['ladder'].have:
        $ __list.append((_("{i}установить стремянку{/i}"), 3))
    if flags['ladder'] > 2:
        $ __list.append((_("{i}воспользоваться стремянкой{/i}"), 4))
    $ __list.append((_("{i}уйти{/i}"), 0))
    $ rez = renpy.display_menu(__list)
    if rez==1:
        if tm[-2:] > '10':
            menu:
                Alice "{b}Алиса:{/b} Кому там не спится? Я ванну принимаю..."
                "Это я, Макс. Можно войти?":
                    Alice "{b}Алиса:{/b} Макс, ты глухой? Я же сказала, буду в ванне плескаться. Жди как минимум час!"
                    Max_10 "Ладно, ладно..."
                "{i}уйти{/i}":
                    pass

        elif flags['alice.drink']:
            jump .knock
        else:
            menu:
                Alice "{b}Алиса:{/b} Кому там не спится? Я ванну набираю..."
                "Это я, Макс. Можно войти?":
                    Alice "{b}Алиса:{/b} Макс, ты глухой? Я же сказала, буду в ванне плескаться. Жди как минимум час!"
                    Max_10 "Ладно, ладно..."
                "{i}уйти{/i}":
                    pass
        jump .end

    elif rez==2:
        scene Alice bath 01
        $ renpy.show('FG voyeur-bath-00'+mgg.dress)
        Max_00 "Эх! Не повезло... Алиса уже плюхнулась принимать ванну. Отсюда я уже ничего увидеть не смогу..."
        jump .end

    elif rez==3:
        scene BG char Max bathroom-window-evening-00
        $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
        Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
        $ flags['ladder'] = 3
        $ items['ladder'].have = False
        $ items['ladder'].InShop = False
        jump alice_bath.ladder

    elif rez==4:
        jump alice_bath.ladder

    else:
        jump .end

    label .knock:
        if 'smoke' in talk_var and flags['smoke'] == 'nopants':
            $ __suf = 'a'
            $ alice.dress_inf = '04da'
        else:
            $ __suf = ''
            $ alice.dress_inf = '04ca'
        $ __r1 = renpy.random.choice(['01', '02', '03'])
        scene BG char Alice bach-after-club-01
        $ renpy.show('Alice bach-after-club 01-'+__r1+__suf)
        show Max bach-after-club 01
        Alice_05 "А, Макс... Не спится? Чего хотел?"
        Max_01 "Да... Я вот... Умыться перед сном хотел!"
        Alice_03 "Ну, проходи. Я собиралась ванну принять, но ещё вода набирается..."
        Max_04 "Как в клубе повеселилась?"
        Alice_04 "Ты знаешь, очень... очень хорошо. Я обычно не пью, но в этот раз что-то потянуло и... всё прошло просто чудесно! А у тебя как дела?"
        Max_07 "Ого. Тебе и правда интересно?"
        Alice_05 "Конечно! Ты же мой брат. Ты извини, если я с тобой бываю груба. Это просто защитная реакция..."
        Max_09 "Защитная реакция?"
        Alice_04 "Тебе не понять... Ты знаешь, я бы хотела извиниться, если тебя чем-то обижала в последнее время... Ой, у тебя что-то в штанах шевелится..."
        show Max bach-after-club 02
        Max_07 "Э... Ты точно в порядке?"
        $ __r1 = {'01':'04', '02':'05', '03':'06'}[__r1]
        $ renpy.show('Alice bach-after-club 01-'+__r1+__suf)
        menu:
            Alice_07 "Ага. И ты, я вижу, тоже... Какой же он у тебя большой..."
            "У тебя... Очень красивая грудь...":
                Alice_04 "Спасибо, Макс. Девушке очень приятно такое слышать от парня. Даже, если это её младший брат... которого ей хочется подразнить..."
                if flags['smoke'] == 'not_nopants':
                    # Алиса нарушила уговор по трусикам
                    Max_09 "А почему на тебе есть трусики?"
                    Alice_05 "Какой ужас! Похоже, я нарушила наш уговор... или нет... Разве я не могу носить их ночью?"
                    Max_07 "Когда спишь - да, а вот всё остальное время - нет!"
                    Alice_03 "Ну что ж, значит на мне есть кое-что лишнее... Это можно легко исправить..."
                    $ renpy.show('Alice bach-after-club 01-'+__r1+'b')
                    Alice_07 "Вот... Теперь всё так, как должно быть. И твоему дружку явно стало очень тесно в трусах, да?"
                elif flags['smoke'] == 'nopants':
                    # Алиса без трусиков
                    Max_04 "Да, эти сосочки выглядят очень соблазнительно... Но чтобы меня подразнить, нужно показать куда больше..."
                    $ renpy.show('Alice bach-after-club 01-'+__r1+'b')
                    Alice_07 "Например, так? Да, я вижу твой дружок запульсировал ещё сильнее... Это так возбуждает!"
                Max_03 "А ты не хочешь мне помочь?"
                if 'black_linderie' in alice.gifts:
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
        $ poss['nightclub'].SetStage(7)
        $ flags['talkaboutbath'] = 1
        jump .end

    label .next1:
        scene BG char Alice bach-after-club-02
        $ renpy.show('Alice bach-after-club 02-01'+__suf)
        $ spent_time += 10

        Alice_13 "Может и хочу! Я ведь была очень плохой девочкой... Ты помогаешь мне с блогом, купил классное нижнее бельё, балуешь сладостями... а я только угрозами в тебя сыплю..."
        Max_01 "Не только... С тобой бывают светлые моменты!"
        menu:
            Alice_08 "Сейчас их может стать на один больше! Что ты хочешь, чтобы я сделала?"
            "Хочу, чтобы ты сняла трусики..." if __suf!='a':   #если на Алисе есть трусики

                $ __suf = 'a'
                $ renpy.show('Alice bach-after-club 02-01'+__suf)

                Alice_05 "Какие у тебя скромные желания, Макс! Всего лишь раздеть свою старшую сестру..."
                Max_02 "На тебе ещё есть халат, так что ты точно не раздетая!"
                menu:
                    Alice_04 "Неужели это всё, чего ты хотел?"
                    "Хочу, чтобы ты поласкала его...":
                        jump .caress

                    "Хочу, чтобы ты отсосала...":
                        jump .suck

            "Хочу, чтобы ты поласкала его...":
                jump .caress

            "Хочу, чтобы ты отсосала...":
                jump .suck

    label .caress:
        $ renpy.show('Alice bach-after-club 02-02'+__suf)
        $ spent_time += 10

        Alice_09 "Ого... Я даже не могу обхватить его всей рукой! Ты ведь давно об этом мечтал, да Макс?"
        Max_04 "Может быть..."
        Alice_07 "Наверняка, ты много раз фантазировал, как я буду чувственно дрочить его своими нежными руками... Ну и как, Макс, приятно?"
        Max_05 "О да! Намного приятнее, чем фантазировать об этом..."
        menu:
            Alice_05 "Не сомневаюсь. Ванна почти наполнилась водой, так что мы можем быстренько успеть что-то ещё! Но осторожнее с желаниями..."
            "Хочу показать тебе, как я научился целоваться..." if talk_var['teachkiss']>3:   #если пройдены уроки поцелуев с Кирой

                scene BG char Alice bach-after-club-03
                $ renpy.show('Alice bach-after-club 03-02'+__suf)

                Alice_03 "Да ладно! Где это ты успел? Ты же дома больше меня сидишь. Не верю я тебе..."
                menu:
                    Max_03 "А ты попробуй!"
                    "{i}целовать Алису{/i}":
                        pass

                $ renpy.show('Alice bach-after-club 03-01'+__suf)

                menu:
                    Max_02 "{i}( А Алиса хорошо целуется! Да со страстью, увлечённо... Ммм... Губки у неё сочные... А уж как в член мой вцепилась! ){/i}"
                    "{i}закончить целоваться{/i}":
                        pass

                $ renpy.show('Alice bach-after-club 03-02'+__suf)

                Alice_09 "Нифига себе! Ты и этому что ли на интернет-курсах научился? Не может быть такого..."
                Max_04 "А вот теперь ванну принимай и гадай, как я научился."
                Alice_02 "Ой, уже наполнилась! А это значит что? Правильно, спокойной ночи!"
                Max_01 "Ага. Приятных снов, Алиса."

            "А если бы я был твоим парнем... Что бы ты сделала дальше?" if flags['double_mass_alice']>1:   #если Макс ласкал Алисе киску у ТВ

                scene BG char Alice bach-after-club-03
                $ renpy.show('Alice bach-after-club 03-02'+__suf)

                Alice_07 "Ха! Кое-чего ты обо мне не знаешь, Макс... Я предпочитаю девушек... Но не откажусь от парня, если у него есть что-то... особенное..."
                Max_03 "Как удачно, что ты как раз держишь в руке кое-что особенное!"

                $ renpy.show('Alice bach-after-club 03-03'+__suf)

                Alice_04 "Да... И я бы, пожалуй, сняла с себя халат, пока ласкала его член... Чтобы ничто не мешало ему наслаждаться моим совершенно голым телом!"
                if __suf:
                    Max_05 "Правильно, Алиса... Такое шикарное тело лучше не скрывать! А потом?"   #если Алиса без трусиков
                else:
                    Max_05 "ПОЧТИ голым телом, но это мелочи... Мне нравится к чему всё идёт! А потом?"   #если Алиса в трусиках

                scene BG char Alice bach-after-club-04
                $ renpy.show('Alice bach-after-club 04-01'+__suf)

                Alice_08 "А потом я бы опустилась на колени и начала водить его членом по своему лицу... неспеша и слегка задевая губами..."
                Max_20 "Ох, чёрт! А потом..."

                scene BG char Alice bach-after-club-03
                $ renpy.show('Alice bach-after-club 03-04'+__suf)

                Alice_05 "У меня ванна набралась, так что спокойной ночи!"
                Max_10 "Да ладно, Алиса! Это слишком жёсткий облом!"
                Alice_04 "Макс... Ты же не хочешь, чтобы я рассказала маме, что ты ко мне приставал?"
                Max_00 "Всё понял, ухожу..."

            "Хочу, чтобы ты отсосала...":
                jump .suck

            "На всё остальное ты не согласишься...":
                Alice_07 "Думаешь? Как знать... Но в любом случае уже поздно, а мне ещё ванну принимать, так что спокойной ночи, Макс."
                Max_01 "Ага. Приятных снов, Алиса."

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
        $ spent_time += 10
        jump Waiting


label alice_lisa_shower:
    scene location house bathroom door-morning
    if peeping['lisa_shower'] > 0:
        menu:
            Max_00 "Сестрёнки принимают душ, не стоит им мешать..."
            "{i}уйти{/i}":
                return
    $ peeping['lisa_shower'] = 1
    menu:
        Max_01 "Интересно, кто сейчас в душе?"
        "{i}заглянуть со двора{/i}":
            jump .start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags['ladder'] > 2:
            jump .ladder
        "{i}уйти{/i}":
            return

    label .ladder:
        $ Skill('hide', 0.03)
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        if 'alice_sh' in cam_flag:
            $ __r0 = 1 if tm[-2:] < '30' else 2 # в первой половине часа перед зекралом Лиза
        elif 'lisa_sh' in cam_flag:
            $ __r0 = 2 if tm[-2:] < '30' else 1 # в первой половине часа перед зекралом Алиса
        elif 'lisa_alice_sh' in cam_flag:
            $ __r0 = 0 # $ __var = 'lisa_alice'
        else:
            $ __r0 = renpy.random.randint(1, 4)
            if __r0 < 3: # если выпал один персонаж
                $ __var = 'alice' if __r0 == 1 else 'lisa'
                if __var == 'alice':
                    $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'alice_sh')
                else: # Алиса в душе, соответственно, перед умывальниками первые полчаса Лиза
                    $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'lisa_sh')
            # else:
            #     $ __var = 'lisa_alice'

        scene BG bathroom-morning-00
        if __r0 == 1:
            if lisa.dress_inf != '04a': # Лизу уже видели через камеру
                $ __r1 = {'04c':'a', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
            else:
                if tm[-2:] < '10'  and 'bathrobe' in lisa.gifts:
                    $ __r1 = 'a'
                elif tm[-2:] < '20':
                    $ __r1 = 'c'
                else:
                    $ __r1 = 'd'
                $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[__r1]

            $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1)
            show FG bathroom-morning-00
            if __r1 == 'a':
                Max_03 "Лиза смотрится в подаренном мною халатике очень соблазнительно... Особенно когда так хорошо видно её упругие сисечки, а за кадром ещё и Алиса принимает душ!"
            elif __r1=='c':
                Max_07 "Моя обворожительная сестрёнка в одних трусиках... Так и хочется зайти и стянуть их с её прекрасной попки, а за кадром ещё и Алиса принимает душ!"
            else:
                Max_06 "Утро может быть действительно очень добрым, если удаётся полюбоваться совершенно голенькой Лизой, а за кадром ещё и Алиса принимает душ!"

        elif __r0 == 2:
            if alice.dress_inf != '04aa': # Алису видели через камеру
                $ __r1 = {'04ca':'a', '04da':'b', '02fa':'c', '00a':'d'}[alice.dress_inf]
            else:
                if tm[-2:] < '10':
                    $ __r1 = 'a'
                elif tm[-2:] < '20':
                    $ __r1 = 'c'
                else:
                    $ __r1 = 'd'
                $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[__r1]
            $ renpy.show('Alice bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1)
            show FG bathroom-morning-00
            if __r1=='a':
                Max_02 "Может Алиса и в халатике, но сиськи её видны просто замечательно, а за кадром ещё и Лиза принимает душ!"
            elif __r1=='c':
                Max_04 "Алиса сегодня без халатика... в одних трусиках... Гдядя на эту красоту, можно мечтать лишь об одном, а за кадром ещё и Лиза принимает душ!"
            else:
                Max_06 "Алиса сегодня совершенно голая! И даже не представляет, что тем самым дарит мне возможность любоваться всеми её прелестями, а за кадром ещё и Лиза принимает душ!"

        else: # если девчонки перед зеркалом вдвоём, то они могут быть либо в трусиках, либо голыми
            $ __r1 = 'd' if 'lisa_alice_sh' in cam_flag else renpy.random.choice(['c', 'd', 'c', 'd', 'c', 'd'])
            $ renpy.show('Alice bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[ladder_left_shift,])
            $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1, at_list=[ladder_right_shift,])
            show FG bathroom-morning-00
            if __r1=='c':
                Max_05 "Две мои сестрёнки красуются перед зеркалом в одних лишь трусиках! Такую прелесть редко можно увидеть..."
            else:
                $ alice.dress_inf = '00a'
                $ lisa.dress_inf = '00'
                Max_06 "Да они же обе голенькие красуются перед зеркалом! Ох, сестрёнки, я бы вами целую вечность любовался..."

        Max_00 "Ладно, хорошего понемногу, а то ещё заметит меня здесь кто-нибудь..."
        jump .end

    label .start_peeping:
        $ Skill('hide', 0.03)

        scene Alice shower-Lisa 01
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Класс! Сегодня мои прекрасные сестрёнки принимают душ вместе... Красота!"
            "{i}продолжить смотреть{/i}":
                pass
            "{i}взглянуть со стороны{/i}":
                jump .alt_peepeng
            "{i}уйти{/i}":
                jump .end

        $ spent_time += 10
        $ __r1 = renpy.random.randint(1, 6)
        $ __r2 = renpy.random.randint(1, 6)
        scene BG shower-closer
        $ renpy.show('Alice shower-closer 0'+str(__r2), at_list=[left_shift,])
        $ renpy.show('Lisa shower-closer 0'+str(__r1), at_list=[right_shift,])
        show FG shower-closer
        Max_03 "Да-а-а... Вот бы оказаться между двумя этими мокрыми попками... Я бы уж их помылил!"
        jump .end

    label .alt_peepeng:
        $ spent_time += 10
        $ alice.dress_inf = '00aa'
        $ lisa.dress_inf = '00a'
        $ __r1 = renpy.random.randint(1, 6)
        $ __r2 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Lisa shower-alt 0'+str(__r1), at_list=[alt_left_shift,])
        $ renpy.show('Alice shower-alt 0'+str(__r2), at_list=[alt_right_shift,])
        show FG shower-water
        Max_03 "Да-а-а... Вот бы оказаться между двумя этими мокрыми попками... Я бы уж их помылил!"
        jump .end

    label .end:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting


label alice_blog_lingerie:
    $ renpy.scene()
    $ renpy.show('location house aliceroom door-'+get_time_of_day())
    if peeping['alice_blog']:
        return

    $ peeping['alice_blog'] = 1
    menu:
        Max_00 "Обычно в это время Алиса занимается своим блогом, но сейчас её дверь закрыта..."
        "{i}заглянуть в окно{/i}":
            $ spent_time += 20
            scene BG char Alice blog-desk-01
            $ alice.dress_inf = {'a':'02', 'b':'02ia'}[alice.dress]
            if renpy.random.randint(1, 2) < 2:
                # Алиса сидит и спаливает Макса
                $ renpy.show('Alice blog 01'+alice.dress)
                $ renpy.show('Max blog 01'+mgg.dress)
                menu:
                    Alice_15 "Что?! Макс! Ну-ка иди отсюда, пока в ухо не получил!"
                    "{i}сбежать{/i}":
                        pass
                    "Классно смотришься!":
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
            else:
                # Алиса позирует стоя и Макс остаётся незамеченным
                $ renpy.show('Alice blog '+renpy.random.choice(['03', '04'])+alice.dress)
                $ renpy.show('Max blog 03'+mgg.dress)
                menu:
                    Max_05 "{i}( Отлично! Алиса крутит задом перед камерой в одном нижнем белье! Надеюсь, не заметит... Отсюда вид точно лучше, чем через камеру... ){/i}"
                    "{i}уйти{/i}":
                        pass

        "{i}уйти{/i}":
            pass
    jump Waiting
