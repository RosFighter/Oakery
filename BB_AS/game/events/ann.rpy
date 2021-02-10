################################################################################
## события Анны

label ann_sleep:
    scene location house annroom door-night
    if peeping['ann_sleep'] != 0:
        return
    $ peeping['ann_sleep'] = 1

    menu:
        Max_00 "В это время мама обычно спит.\nМне кажется, не стоит её будить..."
        "{i}заглянуть в окно{/i}":
            scene BG char Ann bed-night-01
            $ renpy.show('Ann sleep-night '+pose3_3+ann.dress)
            $ renpy.show('FG ann-voyeur-night-00'+mgg.dress)
            if ann.dress == 'a':
                if pose3_3 == '01':
                    Max_01 "Класс! Мама спит... Даже не верится, что у этой конфетки трое детей... В жизни бы в такое не поверил!" nointeract
                elif pose3_3 == '02':
                    Max_04 "О, да! Какая у мамы попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь... Просто супер!" nointeract
                else:
                    Max_07 "Обалденно! Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!" nointeract
            elif ann.dress == 'b':
                if pose3_3 == '01':
                    Max_01 "Класс! Мама спит в ночнушке... Даже не верится, что у этой конфетки трое детей... В жизни бы в такое не поверил!" nointeract
                elif pose3_3 == '02':
                    Max_04 "О, да! Какая у мамы попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь... Её попку даже немного видно через ночнушку!" nointeract
                else:
                    Max_07 "Обалденно! Как же повезло, что у меня такая горячая мама... В этой ночнушке она выглядит потрясающе, аж глаза отрывать не хочется!" nointeract

            $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
            if rez != 'exit':
                $ spent_time += 10
                scene BG char Ann bed-night-02
                $ renpy.show('Ann sleep-night-closer '+pose3_3+ann.dress)
                if ann.dress == 'a':
                    if pose3_3 == '01':
                        Max_03 "Чёрт, у меня самая аппетитная мама на свете! Вот бы снять с неё всё белье и пристроиться сзади... Но лучше потихоньку уходить, пока она не проснулась." nointeract
                    elif pose3_3 == '02':
                        Max_02 "Ухх! Так и хочется прижаться к этой обворожительной попке и шалить всю ночь... Но пора уходить, а то она может проснуться." nointeract
                    else:
                        Max_05 "Вот это да! От вида этих раздвинутых ножек становится всё равно, что она моя мама... Слишком соблазнительно! Только бы она сейчас не проснулась..." nointeract
                elif ann.dress == 'b':
                    if pose3_3 == '01':
                        Max_03 "Чёрт, у меня самая аппетитная мама на свете! Вот бы пристроиться сзади и запустить руки под эту сорочку... Но лучше потихоньку уходить, пока она не проснулась." nointeract
                    elif pose3_3 == '02':
                        Max_02 "Ухх! Так и хочется задрать её сорочку, прижаться к этой обворожительной попке и шалить всю ночь... Но пора уходить, а то она может проснуться." nointeract
                    else:
                        Max_05 "Вот это да! От вида этих раздвинутых ножек становится всё равно, что она моя мама... Слишком уж соблазнительно она выглядит в этой сорочке! Только бы она сейчас не проснулась..." nointeract
                $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
        "{i}уйти{/i}":
            pass
    $ spent_time = 10
    jump Waiting


label ann_shower:
    scene location house bathroom door-morning
    if peeping['ann_shower'] == 3:
        Max_00 "Я уже попался сегодня на подглядывании за мамой. Не стоит злить её ещё больше."
        return
    elif peeping['ann_shower'] == 1:
        Max_00 "Я уже подсматривал сегодня за мамой. Не стоит искушать судьбу слишком часто."
        return
    elif  peeping['ann_shower'] == 2:
        Max_00 "Сегодня мама и так сегодня едва не поймала меня. Не стоит искушать судьбу слишком часто."
        return
    elif peeping['ann_shower'] > 3:
        menu:
            Max_00 "Мама сейчас принимает душ..."
            "{i}уйти{/i}":
                return
    else:
        $ peeping['ann_shower'] = 4
        menu:
            Max_00 "Похоже, мама принимает душ..."
            "{i}заглянуть со двора{/i}":
                jump .start_peeping
            "{i}воспользоваться стремянкой{/i}" if flags['ladder'] > 2:
                jump .ladder
            "{i}уйти{/i}":
                jump .end_peeping

    label .ladder:
        $ renpy.scene()
        $ renpy.show("Max bathroom-window-morning 01"+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        if ann.dress_inf != '04a':
            $ __r1 = {'04c':'a', '04d':'b', '02b':'c', '00':'d', '00a':'d'}[ann.dress_inf]
        else:
            $ __r1 = renpy.random.choice(['a', 'b', 'c', 'd'])
            $ ann.dress_inf = {'a':'04c', 'b':'04d', 'c':'02b', 'd':'00'}[__r1]

        scene BG bathroom-morning-00
        $ renpy.show('Ann bath-window-morning '+renpy.random.choice(['01', '02', '03'])+__r1)
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        if __r1 == 'a':
            Max_07 "Да-а... Распахнутый халатик на маме - это просто изумительное шоу! Такие соблазнительные сосочки... да ещё и так близко... Ммм..."
        elif __r1 == 'b':
            Max_05 "О, да! Мама решила не надевать трусики и правильно сделала, потому что увидеть эту киску с утра пораньше - просто сказка!"
        elif __r1 == 'c':
            Max_03 "Вот это повезло... Мама в одних лишь трусиках, а её упругая грудь предстаёт передо мной во всей своей красе! Так бы любовался и любовался ей..."
        else:
            Max_06 "Ничего себе! Такое зрелище не каждый раз увидишь - она же совершенно голая! Только бы со стремянки не упасть от такого вида... Как было бы круто потискать все её округлости!"

        Max_00 "Лучше бы мне уже уйти, пока никто не увидел..."
        jump .end_peeping

    label .start_peeping:
        $ Skill('hide', 0.03)
        $ __ran1 = renpy.random.randint(1, 4)

        $ _ch1 = GetChance(mgg.stealth, 3, 900)
        $ _ch2 = GetChance(mgg.stealth, 2, 900)
        scene image ('Ann shower 0'+str(__ran1))
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Ух, аж завораживает! Повезло же, что у меня такая сексуальная мама...  Надеюсь, она меня не заметит..."
            "{i}продолжить смотреть\n{color=[_ch1.col]}(Скрытность. Шанс: [_ch1.vis]){/color}{/i}":
                jump .closer_peepeng
            "{i}взглянуть со стороны\n{color=[_ch2.col]}(Скрытность. Шанс: [_ch2.vis]){/color}{/i}":
                jump .alt_peepeng
            "{i}уйти{/i}":
                jump .end_peeping

    label .alt_peepeng:
        if not RandomChance(_ch2.ch):
            jump .not_luck
        $ spent_time += 10
        $ peeping['ann_shower'] = 1
        $ Skill('hide', 0.2)
        $ ann.dress_inf = '00a'
        $ __ran1 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Ann shower-alt 0'+str(__ran1))
        show FG shower-water
        if __ran1 % 2 > 0:
            Max_03 "[undetect!t]Обалдеть можно! Не каждый день выпадает такое счастье, любоваться этой красотой! Её большая упругая грудь и стройная фигурка просто загляденье..."
        else:
            Max_05 "[undetect!t]О, да! Зрелище просто потрясающее... Такой сочной попке может позавидовать любая женщина! Какая мокренькая..."
        jump .end_peeping

    label .closer_peepeng:
        $ spent_time += 10
        if RandomChance(_ch1.ch):
            $ peeping['ann_shower'] = 1
            $ Skill('hide', 0.2)
            $ ann.dress_inf = '00a'
            $ __ran1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            $ renpy.show('Ann shower-closer 0'+str(__ran1))
            show FG shower-closer
            if __ran1 % 2 > 0:
                Max_03 "[undetect!t]Обалдеть можно! Не каждый день выпадает такое счастье, любоваться этой красотой! Её большая упругая грудь и стройная фигурка просто загляденье..."
            else:
                Max_05 "[undetect!t]О, да! Зрелище просто потрясающее... Такой сочной попке может позавидовать любая женщина! Какая мокренькая..."
            jump .end_peeping
        else:
            jump .not_luck

    label .not_luck:
        if RandomChance(_ch1.ch):
            $ peeping['ann_shower'] = 2
            $ Skill('hide', 0.1)
            $ ann.dress_inf = '00a'
            $ __ran1 = renpy.random.randint(7, 8)
            scene BG shower-closer
            $ renpy.show('Ann shower-closer 0'+str(__ran1))
            show FG shower-closer
            Max_12 "{color=[orange]}{i}Кажется, мама что-то заподозрила!{/i}{/color}\nУпс... надо бежать, пока она меня не увидела!"
            jump .end_peeping
        else:
            $ peeping['ann_shower'] = 3
            $ Skill('hide', 0.05)
            $ __ran1 = renpy.random.choice(['09', '10'])
            scene BG shower-closer
            $ renpy.show('Ann shower-closer '+__ran1)
            show FG shower-closer
            menu:
                Ann_15 "[spotted!t]Макс!!! Что ты здесь делаешь? А ну быстро отвернись!!!"
                "{i}Отвернуться{/i}":
                    jump .serious_talk

    label .serious_talk:
        $ spent_time += 10
        $ _ch1 = GetChance(mgg.social, 3, 900)
        $ punreason[2] = 1
        scene BG char Alice spider-bathroom-00
        $ renpy.show('Max spider-bathroom 03'+mgg.dress)
        show Ann shower 05
        menu:
            Ann_19 "Ты что, подглядываешь за мной? Тебе должно быть стыдно! Нас ждёт серьёзный разговор..."
            "Я не подглядывал. Это случайность! {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}":
                if RandomChance(_ch1.ch):
                    $ Skill('social', 0.2)
                    Ann_12 "[succes!t]Случайность, говоришь? Ну ладно, поверю. А теперь бегом отсюда!"
                    Max_04 "Ага, хорошо, мам!"
                    $ punreason[2] = 0
                else:
                    $ Skill('social', 0.1)
                    Ann_16 "[failed!t]Случайно пробрался сюда, спрятался и глазеешь тут? Случайно?! А ну-ка марш отсюда! Перед завтраком поговорим!"
                    Max_10 "Хорошо..."
            "Мам, извини...":
                Ann_12 "Что, думаешь извинился и всё, можно снова подглядывать? Нет, Макс. В этот раз всё так просто не пройдёт. Сейчас иди отсюда, а перед завтраком поговорим!"
                Max_11 "Хорошо..."
            "Попка у тебя - что надо!":
                Ann_13 "Что?! Ну всё, Макс, ты попал! Быстро вернулся в дом, а перед завтарком поговорим ещё на эту тему!"
                Max_14 "Хорошо..."
        jump .end_peeping

    label .end_peeping:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting


label ann_yoga:
    scene BG char Ann yoga-00
    if int(tm[3:4])%3 == 0: # смена позы каждые 10 минут
        $ renpy.show('Ann yoga '+pose3_1)
        $ persone_button1 = 'Ann yoga '+pose3_1+'b'
    elif int(tm[3:4])%3 == 1:
        $ renpy.show('Ann yoga '+pose3_2)
        $ persone_button1 = 'Ann yoga '+pose3_2+'b'
    else:
        $ renpy.show('Ann yoga '+pose3_3)
        $ persone_button1 = 'Ann yoga '+pose3_3+'b'
    return


label ann_cooking:
    scene BG cooking-00
    $ renpy.show('Ann cooking 01'+ann.dress)
    $ persone_button1 = 'Ann cooking 01'+ann.dress+'b'
    return


label ann_cooking_closer:
    scene BG cooking-01
    $ renpy.show('Ann cooking-closer '+pose3_3+ann.dress)
    return


label ann_dressed_work:
    scene location house annroom door-morning
    if peeping['ann_dressed'] != 0:
        return
    $ peeping['ann_dressed'] = 1
    $ __mood = 0
    menu:
        Max_09 "Сейчас 10 часов, а значит, мама собирается на работу..."
        "{i}постучаться{/i}":
            menu:
                Ann "{b}Анна:{/b} Кто там?"
                "Это я, Макс. Можно войти?"  if not items['nightie'].have:
                    Ann "{b}Анна:{/b} Макс, я не одета. Собираюсь на работу. Подожди немного, дорогой."
                    Max_00 "Хорошо, мам."
                    jump .end
                "Это я, Макс. Можно войти? У меня для тебя кое-что есть." if items['nightie'].have:
                    Ann "{b}Анна:{/b} Макс, я не одета. Собираюсь на работу. Подожди немного, дорогой."
                    Max_00 "Хорошо, мам."
                    $ __open = False
                    jump .gift
                "{i}уйти{/i}":
                    jump .end
        "{i}открыть дверь{/i}":
            scene BG char Ann morning
            $ __list = ['01', '01a', '02', '02a', '03', '03a', '01', '01a', '02', '02a', '03', '03a', '04']
            if ann.dress=='d':
                $ __list.extend(['06', '07', '07a'])
            $ __ran1 = renpy.random.choice(__list)
            $ __open = True
            $ renpy.show('Ann dressed '+__ran1)
            $ ann.dress_inf = {'01':'02',  '01a':'02e', '02':'02b', '02a':'02d', '03':'02a', '03a':'02c', '04':'00', '06':'2g', '07':'2i', '07a':'2h'}[__ran1]
            menu:
                Ann_13 "Макс! Я же учила тебя стучаться!"
                "Хорошо выглядишь, мам!":
                    $ __mood += 30
                    Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?"
                    Max_00 "Конечно, мам!"
                "У меня для тебя кое-что есть." if items['nightie'].have:
                    Ann_12 "Очень здорово, Макс! Но сначала, ты закроешь дверь и я спокойно переоденусь, а уже после этого посмотрим, что у тебя там такое срочное..."
                    Max_00 "Конечно, мам!"
                    scene location house annroom door-morning
                    Max_00 "Пожалуй, не стоило вот так врываться к маме... Надеюсь, подарок всё сгладит."
                    jump .gift
                "Зачётные сиськи!":
                    $ __mood -= 30
                    Ann_19 "Что?! Макс! А ну-ка быстро выйди и закрой дверь!"
                    Max_00 "Как скажешь, мам..."
                "Ой, извини. Я забыл...":
                    $ __mood -= 10
                    Ann_07 "Ну, бывает. Я сама ещё не привыкла к тому, что замков нигде нет. Ладно, дорогой. Подожди за дверью, пока мама одевается. хорошо?"
                    Max_00 "Хорошо, мам..."
            $ AddRelMood('ann', 0, __mood)
            jump .end
        "{i}заглянуть в окно{/i}":
            $ __list = ['01', '01a', '02', '03', '03a', '04']
            if ann.dress=='d':
                $ __list.extend(['05', '06', '06a'])
            $ __ran1 = renpy.random.choice(__list)
            $ ann.dress_inf = {'01':'02e', '01a':'02c', '02':'02d', '03':'02', '03a':'02a', '04':'02b', '05':'2g', '06':'2i', '06a':'2h'}[__ran1]

            if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
                scene BG char Ann voyeur-01
                $ renpy.show('Ann voyeur alt-'+__ran1)
                $ renpy.show('FG voyeur-morning-01'+mgg.dress)
            else:
                scene BG char Ann voyeur-00
                $ renpy.show('Ann voyeur '+__ran1)
                $ renpy.show('FG voyeur-morning-00'+mgg.dress)

            $ Skill('hide', 0.03)
            Max_01 "Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но пора уходить, а то вдруг увидит меня в зеркало!"
            jump .end
        "{i}уйти{/i}":
            jump .end

    label .gift:
        scene BG char Ann morning
        show Ann dressed 05
        Ann_01 "Ну вот, я одета. Ты сказал, что у тебя что-то есть для меня?! О чём это ты?"
        Max_04 "У меня для тебя подарок! Ночнушка!"
        Ann_06 "Ты это серьёзно? Но в честь чего?"
        Max_05 "Просто ты - самая лучшая мама на свете!"
        Ann_08 "Ох, Макс, ты мне льстишь! Это так... неожиданно! Спасибо тебе мой милый, я очень тронута!"
        Max_03 "Может, примеришь?"
        Ann_06 "Примерить? Для тебя? Ну... ладно... Думаю, ты это заслужил. Подожди, пожалуйста, за дверью..."
        Max_01 "Хорошо, мам."
        scene location house annroom door-morning
        Ann "{b}Анна:{/b} Ничего себе, она полупрозрачная! Дорогой, ты же понимаешь, что твоя мама не может показаться в этом перед сыном..."
        Max_10 "Тебе не понравился подарок?!"
        Ann "{b}Анна:{/b} Нет, мне очень нравится! Это прекрасный подарок! Только вот, тебе не кажется, что ты ещё слишком мал, чтобы делать подобные подарки?"
        Max_09 "Я уже большой, мам! Я же от души!"
        Ann "{b}Анна:{/b} Ох, Макс, ты меня смущаешь, такой откровенный подарок, да ещё родной матери... Но всё равно, я очень это ценю... и ещё раз огромное спасибо!"
        Max_02 "Думаю, смотрится она на тебе просто фантастически!"
        scene BG char Ann morning
        show Ann dressed 05
        Ann_08 "Ох... Спасибо за комплимент, мой милый. Сразу видно, что мой сын настоящий мужчина! Иди ко мне, я тебя обниму..."
        $ __r1 = renpy.random.choice(['01', '02'])
        $ renpy.show('Ann hugging morning-annroom '+__r1+'-1a'+mgg.dress)
        Max_05 "{i}( О да... У меня действительно лучшая мама на свете! Какая же потрясающая у неё фигура... Так приятно прижиматься к ней... её упругой груди... Эту мечту не хочется отпускать! ){/i}"
        $ renpy.show('Ann hugging morning-annroom '+__r1+'-2a'+mgg.dress)
        $ _ch1 = GetChance(mgg.social, 3, 900)
        $ spent_time += 10
        menu:
            Ann_04 "Ну всё, мой дорогой, мне уже скоро на работу и нужно успеть сделать ещё кое-какие дела..."
            "Ну мам! Этого было так мало, давай ещё... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if not __open:
                if RandomChance(_ch1.ch):
                    $ spent_time += 10
                    $ Skill('social', 0.2)
                    Ann_05 "[succes!t]Ты сегодня очень мил, Макс! За это я тебя даже в щёчку поцелую, чтобы ты почаще старался меня радовать..."
                    $ renpy.show('Ann hugging morning-annroom '+__r1+'-3a'+mgg.dress)
                    Max_06 "{i}( Ого! Это даже больше того, на что я надеялся... И не менее приятно чувствовать прикосновение её губ на своём лице! Блаженно... ){/i}"
                    $ renpy.show('Ann hugging morning-annroom '+__r1+'-2a'+mgg.dress)
                    $ AddRelMood('ann', 0, 200)
                    $ AttitudeChange('ann', 0.9)
                    menu:
                        Ann_04 "А теперь иди, сынок... Пора заниматься делами."
                        "Хорошо... Я тебя люблю, мам!":
                            jump .loveyou
                        "Конечно, мам! Хорошего тебе дня...":
                            jump .goodday
                else:
                    $ Skill('social', 0.1)
                    $ AddRelMood('ann', 0, 170)
                    $ AttitudeChange('ann', 0.8)
                    jump .fail

            "Ну мам! Этого было так мало, давай ещё..." if __open:
                $ AddRelMood('ann', 0, 150)
                $ AttitudeChange('ann', 0.7)
                jump .fail
            "Конечно, мам! Хорошего тебе дня...":
                jump .goodday
    label .fail:
        $ _text = failed if __open else ""
        menu:
            Ann_01 "[_text!t]Макс, я так на работу не успею собраться... Давай, сынок, иди... Пора заниматься делами."
            "Хорошо... Я тебя люблю, мам!":
                jump .loveyou
            "Конечно, мам! Хорошего тебе дня...":
                jump .goodday

    label .loveyou:
        Ann_07 "И я тебя, Макс..."
        jump .endgift

    label .goodday:
        Ann_02 "Спасибо, сынок! И тебе тоже..."
        jump .endgift

    label .endgift:
        $ items['nightie'].have = False
        $ items['nightie'].InShop = False
        $ ann.gifts.append('nightie')
        $ clothes[ann].sleep.sel.append(Garb('b', '02f', 'НОЧНУШКА', True))
        $ clothes[ann].sleep.cur = 1
        $ clothes[ann].sleep.rand = True
        $ infl[ann].add_m(40, True)
        jump .end

    label .end:
        $ spent_time += 10
        jump Waiting


label ann_dressed_shop:
    scene location house annroom door-morning
    if peeping['ann_dressed'] != 0:
        return

    $ peeping['ann_dressed'] = 1
    $ __mood = 0
    menu:
        Max_09 "Сегодня суббота, день шоппинга. Видимо, мама собирается..."
        "{i}постучаться{/i}":
            menu:
                Ann "{b}Анна:{/b} Кто там?"
                "Это я, Макс. Можно войти?" if not items['nightie'].have:
                    Ann "{b}Анна:{/b} Нет, Макс. Я переодеваюсь. Подожди немного, дорогой."
                    Max_00 "Хорошо, мам."
                "Это я, Макс. Можно войти? У меня для тебя кое-что есть." if items['nightie'].have:
                    Ann "{b}Анна:{/b} Макс, я не одета. Собираюсь на шопинг. Подожди немного, дорогой."
                    Max_00 "Хорошо, мам."
                    $ __open = False
                    jump .gift
                "{i}уйти{/i}":
                    pass
            jump .end
        "{i}открыть дверь{/i}":
            scene BG char Ann morning
            $ __list = ['01', '02', '03', '04']
            if ann.dress=='d':
                $ __list.extend(['06', '07', '07a'])
            $ __ran1 = renpy.random.choice(__list)
            $ __open = True
            $ renpy.show('Ann dressed '+__ran1)
            $ ann.dress_inf = {'01':'02', '02':'02b', '03':'02a', '04':'00', '06':'2g', '07':'2i', '07a':'2h'}[__ran1]
            menu:
                Ann_13 "Макс! Я же учила тебя стучаться!"
                "Хорошо выглядишь, мам!":
                    $ __mood += 30
                    Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?"
                    Max_00 "Конечно, мам!"
                "У меня для тебя кое-что есть." if items['nightie'].have:
                    Ann_12 "Очень здорово, Макс! Но сначала, ты закроешь дверь и я спокойно переоденусь, а уже после этого посмотрим, что у тебя там такое срочное..."
                    Max_00 "Конечно, мам!"
                    scene location house annroom door-morning
                    Max_00 "Пожалуй, не стоило вот так врываться к маме... Надеюсь, подарок всё сгладит."
                    jump .gift
                "Ой, извини...":
                    Ann_07 "И Макс... Постарайся больше не входить без стука, хорошо?"
                    Max_00 "Хорошо, мам..."
            $ AddRelMood('ann', 0, __mood)
            jump .end
        "{i}заглянуть в окно{/i}":
            $ __list = ['03', '03a', '04']
            if ann.dress=='d':
                $ __list.extend(['05', '06', '06a'])
            $ __ran1 = renpy.random.choice(__list)
            $ ann.dress_inf = {'03':'02', '03a':'02a', '04':'02b', '05':'2g', '06':'2i', '06a':'2h'}[__ran1]

            if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
                scene BG char Ann voyeur-01
                $ renpy.show('Ann voyeur alt-'+__ran1)
                $ renpy.show('FG voyeur-morning-01'+mgg.dress)
            else:
                scene BG char Ann voyeur-00
                $ renpy.show('Ann voyeur '+__ran1)
                $ renpy.show('FG voyeur-morning-00'+mgg.dress)

            $ Skill('hide', 0.03)
            Max_01 "Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но пора уходить, а то вдруг увидит меня в зеркало!"
            jump .end
        "{i}уйти{/i}":
            jump .end

    label .gift:
        scene BG char Ann morning
        show Ann dressed 05a
        Ann_01 "Ну вот, я одета. Ты сказал, что у тебя что-то есть для меня?! О чём это ты?"
        Max_04 "У меня для тебя подарок! Ночнушка!"
        Ann_06 "Ты это серьёзно? Но в честь чего?"
        Max_05 "Просто ты - самая лучшая мама на свете!"
        Ann_08 "Ох, Макс, ты мне льстишь! Это так... неожиданно! Спасибо тебе мой милый, я очень тронута!"
        Max_03 "Может, примеришь?"
        Ann_06 "Примерить? Для тебя? Ну... ладно... Думаю, ты это заслужил. Подожди, пожалуйста, за дверью..."
        Max_01 "Хорошо, мам."
        scene location house annroom door-morning
        Ann "{b}Анна:{/b} Ничего себе, она полупрозрачная! Дорогой, ты же понимаешь, что твоя мама не может показаться в этом перед сыном..."
        Max_10 "Тебе не понравился подарок?!"
        Ann "{b}Анна:{/b} Нет, мне очень нравится! Это прекрасный подарок! Только вот, тебе не кажется, что ты ещё слишком мал, чтобы делать подобные подарки?"
        Max_09 "Я уже большой, мам! Я же от души!"
        Ann "{b}Анна:{/b} Ох, Макс, ты меня смущаешь, такой откровенный подарок, да ещё родной матери... Но всё равно, я очень это ценю... и ещё раз огромное спасибо!"
        Max_02 "Думаю, смотрится она на тебе просто фантастически!"
        scene BG char Ann morning
        show Ann dressed 05a
        Ann_08 "Ох... Спасибо за комплимент, мой милый. Сразу видно, что мой сын настоящий мужчина! Иди ко мне, я тебя обниму..."
        $ __r1 = renpy.random.choice(['01', '02'])
        $ renpy.show('Ann hugging morning-annroom '+__r1+'-1b'+mgg.dress)
        Max_05 "{i}( О да... У меня действительно лучшая мама на свете! Какая же потрясающая у неё фигура... Так приятно прижиматься к ней... её упругой груди... Эту мечту не хочется отпускать! ){/i}"
        $ renpy.show('Ann hugging morning-annroom '+__r1+'-2b'+mgg.dress)
        $ _ch1 = GetChance(mgg.social, 3, 900)
        $ spent_time += 10
        menu:
            Ann_04 "Ну всё, мой дорогой, нам с девочками ещё нужно успеть пробежаться по магазинам сегодня..."
            "Ну мам! Этого было так мало, давай ещё... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if not __open:
                if RandomChance(_ch1.ch):
                    $ spent_time += 10
                    $ Skill('social', 0.2)
                    Ann_05 "[succes!t]Ты сегодня очень мил, Макс! За это я тебя даже в щёчку поцелую, чтобы ты почаще старался меня радовать..."
                    $ renpy.show('Ann hugging morning-annroom '+__r1+'-3b'+mgg.dress)
                    Max_06 "{i}( Ого! Это даже больше того, на что я надеялся... И не менее приятно чувствовать прикосновение её губ на своём лице! Блаженно... ){/i}"
                    $ renpy.show('Ann hugging morning-annroom '+__r1+'-2b'+mgg.dress)
                    $ AddRelMood('ann', 0, 200)
                    $ AttitudeChange('ann', 0.9)
                    menu:
                        Ann_04 "А теперь иди, сынок... Пора заниматься делами."
                        "Хорошо... Я тебя люблю, мам!":
                            jump .loveyou
                        "Конечно, мам! Хорошего тебе дня...":
                            jump .goodday
                else:
                    $ Skill('social', 0.1)
                    $ AddRelMood('ann', 0, 170)
                    $ AttitudeChange('ann', 0.8)
                    jump .fail

            "Ну мам! Этого было так мало, давай ещё..." if __open:
                $ AddRelMood('ann', 0, 150)
                $ AttitudeChange('ann', 0.7)
                jump .fail
            "Конечно, мам! Хорошего тебе дня...":
                jump .goodday
    label .fail:
        $ _text = failed if __open else ""
        menu:
            Ann_01 "[_text!t]Макс, мне нужно ещё успеть сделать кое-какие дела... Давай, сынок, иди... Займись чем-нибудь."
            "Хорошо... Я тебя люблю, мам!":
                jump .loveyou
            "Конечно, мам! Хорошего тебе дня...":
                jump .goodday

    label .loveyou:
        Ann_07 "И я тебя, Макс..."
        jump .endgift

    label .goodday:
        Ann_02 "Спасибо, сынок! И тебе тоже..."
        jump .endgift

    label .endgift:
        $ items['nightie'].have = False
        $ items['nightie'].InShop = False
        $ ann.gifts.append('nightie')
        $ clothes[ann].sleep.sel.append(Garb('b', '02f', 'НОЧНУШКА', True))
        $ clothes[ann].sleep.cur = 1
        $ clothes[ann].sleep.rand = True
        # if ann.inferic is not None:
        #     $ ann.inferic = clip(ann.inferic-50.0, 0.0, 100.0)
        # if ann.infmax is not None:
        #     $ ann.infmax = clip(ann.infmax+20.0, 0.0, 100.0)
        # else:
        #     $ ann.infmax = 20.0
        $ infl[ann].add_m(40, True)
        jump .end

    label .end:
        $ spent_time += 10
        jump Waiting


label ann_resting:
    if tm < '19:00':
        scene BG char Ann relax-morning-01
        $ renpy.show('Ann relax-morning '+pose3_3+ann.dress)
        $ persone_button1 = 'Ann relax-morning '+pose3_3+ann.dress+'b'
    else:
        scene BG char Ann relax-evening-01
        $ renpy.show('Ann relax-evening '+pose3_3+ann.dress)
        $ persone_button1 = 'Ann relax-evening '+pose3_3+ann.dress+'b'
    return


label ann_read:
    scene BG reading
    $ renpy.show('Ann reading '+pose3_3+ann.dress)
    $ persone_button1 = 'Ann reading '+pose3_3+ann.dress+'b'
    return


label ann_read_closer:
    scene BG reading
    $ renpy.show('Ann reading-closer 01'+ann.dress)
    return


label ann_swim:
    scene image 'Ann swim '+pose3_3+'a'
    $ persone_button1 = 'Ann swim '+pose3_3+'ab'
    return


label ann_sun:
    scene BG char Ann sun
    $ renpy.show('Ann sun '+pose3_3+'a')
    $ persone_button1 = 'Ann sun '+pose3_3+'ab'
    return


label ann_alice_sun:
    scene BG char Ann Alice 2sun-00
    $ renpy.show('Alice 2sun '+pose3_2)
    # $ persone_button1 = 'Alice 2sun '+pose3_2
    $ renpy.show('Ann 2sun '+pose3_3)
    # $ persone_button2 = 'Ann 2sun '+pose3_3
    return


label ann_alice_swim:
    $ renpy.scene()
    $ renpy.show('BG char Ann Alice 2swim-'+pose3_1)
    return


label ann_bath:
    scene location house bathroom door-evening
    if peeping['ann_bath'] != 0:
        return

    $ peeping['ann_bath'] = 1
    menu:
        Max_00 "Видимо, мама принимает ванну..."
        "{i}постучаться{/i}":
            menu:
                Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
                "Это я, Макс.":
                    menu:
                        Ann "{b}Анна:{/b} Дорогой, что ты хотел?"
                        "Можно я войду?":
                            $ config.menu_include_disabled = True
                            menu:
                                Ann "{b}Анна:{/b} Ну... хорошо, входи. Только не смотри!"
                                # "{i}Войти{/i} \n(в следующей версии...)" if False: ## пока нет изображений
                                #     menu:
                                #         Ann_01 "Макс, так что там у тебя такое срочное, что ты не мог подождать пол часа?"
                                #         "Просто, я соскучился!":
                                #             Ann_07 "Макс! Я думала, что-то случилось, а ты просто балуешься. Подожди меня за дверью. Я скоро!"
                                #             Max_00 "Хорошо..."
                                #             jump .end
                                #         "Ну это, хотел поглазеть...":
                                #             Ann_13 "Что?! А ну-ка быстро выметайся отсюда! Я скоро закончу."
                                #             Max_00 "Как скажешь!"
                                #             jump .end
                                #         "Я собирался спать и хотел принять душ перед сном":
                                #             ###############################
                                #             pass
                                #         "Ой, не буду тебе мешать":
                                #             jump .end
                                "Ой, нет, я передумал":
                                    jump .end
                        "Нет, ничего":
                            pass
                        "Я подожду...":
                            pass
                    Ann "{b}Анна:{/b} Хорошо, я скоро закончу..."
                    Max_00 "Ага..."
                    jump .end
                "{i}уйти{/i}":
                    jump .end
        "{i}заглянуть со двора{/i}" if 'ladder' not in flags or flags['ladder'] < 2:
            scene Ann bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "Эх... жаль, что стекло частично матовое. Так ничего не разглядеть! А если подобраться ближе, то мама может заметить..."
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
        $ renpy.show('Ann bath-window 0'+str(__r1))
        show FG bath-00
        $ Skill('hide', 0.03)
        if __r1 == 1:
            menu:
                Max_03 "Ох, как горячо! Разумеется, я не про воду, а про её внешний вид. Ухх... Мама потрясающе выглядит..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Ann bath-window '+renpy.random.choice(['02', '03', '04']))
                    $ Skill('hide', 0.03)
                    menu:
                        Max_05 "Ух ты, аж завораживает! Мамины водные процедуры могут посоперничать с самыми горячими эротическими роликами! Эта упругая грудь и эти длинные стройные ножки сведут с ума кого угодно..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ ann.dress_inf = '00a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end
        else:
            menu:
                Max_05 "Ух ты, аж завораживает! Мамины водные процедуры могут посоперничать с самыми горячими эротическими роликами! Эта упругая грудь и эти длинные стройные ножки сведут с ума кого угодно..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Ann bath-window 05
                    $ Skill('hide', 0.03)
                    menu:
                        Max_07 "Эх! Похоже, самое интересное закончилось... Хотя, смотреть как мама вытирает своё мокрое и соблазнительное тело не менее приятно! Ох, какая же у неё попка..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ ann.dress_inf = '04a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end

    label .end:
        $ config.menu_include_disabled = False
        $ spent_time += 10
        jump Waiting


label ann_tv:
    scene BG lounge-tv-00
    $ renpy.show('Ann tv '+pose3_3+'a')
    $ persone_button1 = 'Ann tv '+pose3_3+'ab'
    return


label ann_tv_closer:
    scene BG lounge-tv-01
    $ renpy.show('Ann tv-closer '+pose3_3+'a')
    $ renpy.show('Max tv 00'+mgg.dress)
    return
