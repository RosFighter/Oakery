################################################################################
## события Анны

label ann_sleep:
    scene location house annroom door-night
    if ann.hourly.sleep != 0:
        return
    $ ann.hourly.sleep = 1

    menu:
        Max_00 "{m}В это время мама обычно спит.\nМне кажется, не стоит её будить...{/m}"
        "{i}заглянуть в окно{/i}":

            if all([ann.flags.showdown_e > 1, flags.eric_wallet > 4, ann.flags.truehelp > 4, not ann.dcv.drink.stage, '02:00'>tm>='01:00']):
                # состоялся за завтраком разговор об изгнании Эрика
                # Макс набрал 5 успешных расширенных йог
                scene Ann_sleep no_ann
                Max_09 "Хм... Мамы нет. Где же она?"
                jump Waiting

            scene Ann_sleep
            # scene BG char Ann bed-night-01
            # $ renpy.show('Ann sleep-night '+pose3_3+ann.dress)
            # $ renpy.show('FG ann-voyeur-night-00'+mgg.dress)
            if ann.dress == 'a':
                if pose3_3 == '01':
                    Max_01 "{m}Класс! Мама спит... Даже не верится, что у этой конфетки трое детей... В жизни бы в такое не поверил!{/m}" nointeract
                elif pose3_3 == '02':
                    Max_04 "{m}О, да! Какая у мамы попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь... Просто супер!{/m}" nointeract
                else:
                    Max_07 "{m}Обалденно! Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!{/m}" nointeract
            elif ann.dress == 'b':
                if pose3_3 == '01':
                    Max_01 "{m}Класс! Мама спит в ночнушке... Даже не верится, что у этой конфетки трое детей... В жизни бы в такое не поверил!{/m}" nointeract
                elif pose3_3 == '02':
                    Max_04 "{m}О, да! Какая у мамы попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь... Её попку даже немного видно через ночнушку!{/m}" nointeract
                else:
                    Max_07 "{m}Обалденно! Как же повезло, что у меня такая горячая мама... В этой ночнушке она выглядит потрясающе, аж глаза отрывать не хочется!{/m}" nointeract

            menu:
                "{i}прокрасться в комнату{/i}":
                    $ spent_time += 10
                    # scene BG char Ann bed-night-02
                    # $ renpy.show('Ann sleep-night-closer '+pose3_3+ann.dress)
                    scene Ann_sleep closer
                    if ann.dress == 'a':
                        if pose3_3 == '01':
                            Max_03 "{m}Чёрт, у меня самая аппетитная мама на свете! Вот бы снять с неё всё белье и пристроиться сзади... Но лучше потихоньку уходить, пока она не проснулась.{/m}" nointeract
                        elif pose3_3 == '02':
                            Max_02 "{m}Ухх! Так и хочется прижаться к этой обворожительной попке и шалить всю ночь... Но пора уходить, а то она может проснуться.{/m}" nointeract
                        else:
                            Max_05 "{m}Вот это да! От вида этих раздвинутых ножек становится всё равно, что она моя мама... Слишком соблазнительно! Только бы она сейчас не проснулась...{/m}" nointeract
                    elif ann.dress == 'b':
                        if pose3_3 == '01':
                            Max_03 "{m}Чёрт, у меня самая аппетитная мама на свете! Вот бы пристроиться сзади и запустить руки под эту сорочку... Но лучше потихоньку уходить, пока она не проснулась.{/m}" nointeract
                        elif pose3_3 == '02':
                            Max_02 "{m}Ухх! Так и хочется задрать её сорочку, прижаться к этой обворожительной попке и шалить всю ночь... Но пора уходить, а то она может проснуться.{/m}" nointeract
                        else:
                            Max_05 "{m}Вот это да! От вида этих раздвинутых ножек становится всё равно, что она моя мама... Слишком уж соблазнительно она выглядит в этой сорочке! Только бы она сейчас не проснулась...{/m}" nointeract
                    menu:
                        "{i}уйти{/i}":
                            pass
                "{i}уйти{/i}":
                    pass
        "{i}уйти{/i}":
            pass
    $ spent_time = 10
    jump Waiting


label ann_shower:
    scene location house bathroom door-morning
    if ann.daily.shower == 3:
        Max_00 "{m}Я уже попался сегодня на подглядывании за мамой. Не стоит злить её ещё больше.{/m}"
        return
    elif ann.daily.shower == 1:
        Max_00 "{m}Я уже подсматривал сегодня за мамой. Не стоит искушать судьбу слишком часто.{/m}"
        return
    elif  ann.daily.shower == 2:
        Max_00 "{m}Сегодня мама и так сегодня едва не поймала меня. Не стоит искушать судьбу слишком часто.{/m}"
        return
    elif ann.daily.shower > 3:
        menu:
            Max_00 "{m}Мама сейчас принимает душ...{/m}"
            "{i}уйти{/i}":
                return
    else:
        $ ann.daily.shower = 4
        menu:
            Max_00 "{m}Похоже, мама принимает душ...{/m}"
            "{i}заглянуть со двора{/i}" if not flags.block_peeping:
                jump .start_peeping
            "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
                jump .ladder
            "{i}уйти{/i}":
                jump .end_peeping

    label .ladder:
        $ renpy.scene()
        $ renpy.show("Max bathroom-window-morning 01"+mgg.dress)
        Max_04 "{m}Посмотрим, что у нас тут...{/m}"
        $ ann.flags.ladder += 1
        if ann.dress_inf != '04a':
            $ __r1 = {'04c':'a', '04d':'b', '02b':'c', '00':'d', '00a':'d'}[ann.dress_inf]
        else:
            $ __r1 = random_choice(['a', 'b', 'c', 'd'])
            $ ann.dress_inf = {'a':'04c', 'b':'04d', 'c':'02b', 'd':'00'}[__r1]

        scene BG bathroom-morning-00
        $ renpy.show('Ann bath-window-morning '+random_choice(['01', '02', '03'])+__r1)
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        if __r1 == 'a':
            Max_07 "{m}Да-а... Распахнутый халатик на маме - это просто изумительное шоу! Такие соблазнительные сосочки... да ещё и так близко... Ммм...{/m}"
        elif __r1 == 'b':
            Max_05 "{m}О, да! Мама решила не надевать трусики и правильно сделала, потому что увидеть эту киску с утра пораньше - просто сказка!{/m}"
        elif __r1 == 'c':
            Max_03 "{m}Вот это повезло... Мама в одних лишь трусиках, а её упругая грудь предстаёт передо мной во всей своей красе! Так бы любовался и любовался ей...{/m}"
        else:
            Max_06 "{m}Ничего себе! Такое зрелище не каждый раз увидишь - она же совершенно голая! Только бы со стремянки не упасть от такого вида... Как было бы круто потискать все её округлости!{/m}"

        if looked_ladder():
            $ house[3].max_cam = 2
            $ items['hide_cam'].unblock()
            Max_07 "{m}Мои зрители явно пропускают много всего интересного! Мне однозначно стоит установить сюда ещё одну камеру...{/m}"
        Max_00 "{m}Лучше бы мне уже уйти, пока никто не увидел...{/m}"
        jump .end_peeping

    label .start_peeping:
        $ Skill('hide', 0.03, 10)
        $ __ran1 = random_randint(1, 4)

        scene image ('Ann shower 0'+str(__ran1))
        $ renpy.show('FG shower 00'+mgg.dress)
        if flags.eric_wallet == 2:
            Max_09 "{m}Лучше вообще свести подглядывания к минимуму, пока я не избавлюсь от Эрика. Чтобы никого ещё больше не расстраивать...{/m}"
            menu:
                Max_01 "{m}Хорошо, что это не распространяется на Киру...{/m}"
                "{i}уйти{/i}":
                    $ flags.block_peeping = 1
                    jump .end_peeping

        play music spying
        menu:
            Max_07 "{m}Ух, аж завораживает! Повезло же, что у меня такая сексуальная мама...  Надеюсь, она меня не заметит...{/m}"
            "{i}продолжить смотреть{/i}" ('hide', mgg.stealth * 3, 90, 2):
                jump .closer_peepeng
            "{i}взглянуть со стороны{/i}" ('hide', mgg.stealth * 2, 90, 2):
                jump .alt_peepeng
            "{i}уйти{/i}":
                jump .end_peeping

    label .alt_peepeng:
        if rand_result < 2:
            jump .not_luck
        $ spent_time += 10
        $ ann.daily.shower = 1
        $ ann.dress_inf = '00a'
        $ __ran1 = random_randint(1, 6)
        scene BG bathroom-shower-03
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Ann shower-alt 0'+str(__ran1))
        show FG shower-water
        if __ran1 % 2 > 0:
            Max_03 "[undetect!t]{m}Обалдеть можно! Не каждый день выпадает такое счастье, любоваться этой красотой! Её большая упругая грудь и стройная фигурка просто загляденье...{/m}"
        else:
            Max_05 "[undetect!t]{m}О, да! Зрелище просто потрясающее... Такой сочной попке может позавидовать любая женщина! Какая мокренькая...{/m}"
        jump .end_peeping

    label .closer_peepeng:
        $ spent_time += 10
        if rand_result > 1:
            $ ann.daily.shower = 1
            $ ann.dress_inf = '00a'
            $ __ran1 = random_randint(1, 6)
            scene BG bathroom-shower-01
            $ renpy.show('Ann shower-closer 0'+str(__ran1))
            show FG shower-closer
            if __ran1 % 2 > 0:
                Max_03 "[undetect!t]{m}Обалдеть можно! Не каждый день выпадает такое счастье, любоваться этой красотой! Её большая упругая грудь и стройная фигурка просто загляденье...{/m}"
            else:
                Max_05 "[undetect!t]{m}О, да! Зрелище просто потрясающее... Такой сочной попке может позавидовать любая женщина! Какая мокренькая...{/m}"
            jump .end_peeping
        else:
            jump .not_luck

    label .not_luck:
        if ann.dcv.private.stage > 4:
            # после прохождения 2-ого интимного урока (ванна)
            $ ann.daily.shower = 2
            $ ann.dress_inf = '00a'
            scene BG bathroom-shower-01
            $ renpy.show('Ann shower-closer '+random_choice(['07', '08']))
            show FG shower-closer
            Ann_14 "[spotted!t]Сынок, я вообще-то всё вижу! Понимаю, тебе интересно, но меня это несколько... смущает. Не мешай маме." nointeract
            menu:
                "{i}уйти{/i}":
                    jump .end_peeping

        if rand_result:
            $ ann.daily.shower = 2
            $ ann.dress_inf = '00a'
            $ __ran1 = random_randint(7, 8)
            scene BG bathroom-shower-01
            $ renpy.show('Ann shower-closer 0'+str(__ran1))
            show FG shower-closer
            Max_12 "{color=[orange]}{i}Кажется, мама что-то заподозрила!{/i}{/color}\n{m}Упс... надо бежать, пока она меня не увидела!{/m}"
            jump .end_peeping
        else:
            $ ann.daily.shower = 3
            $ __ran1 = random_choice(['09', '10'])
            scene BG bathroom-shower-01
            $ renpy.show('Ann shower-closer '+__ran1)
            show FG shower-closer
            menu:
                Ann_15 "[spotted!t]Макс!!! Что ты здесь делаешь? А ну быстро отвернись!!!"
                "{i}Отвернуться{/i}":
                    jump .serious_talk

    label .serious_talk:
        $ spent_time += 10
        $ punreason[2] = 1
        scene BG char Alice spider-bathroom-00
        $ renpy.show('Max spider-bathroom 03'+mgg.dress)
        show Ann shower 05
        menu:
            Ann_19 "Ты что, подглядываешь за мной? Тебе должно быть стыдно! Нас ждёт серьёзный разговор..."
            "Я не подглядывал. Это случайность!" ('soc', mgg.social * 3, 90):
                if rand_result:
                    Ann_12 "[succes!t]Случайность, говоришь? Ну ладно, поверю. А теперь бегом отсюда!"
                    Max_04 "Ага, хорошо, мам!"
                    $ punreason[2] = 0
                else:
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
        $ current_room = house[6]
        $ spent_time += 10
        jump Waiting


label ann_yoga:
    $ var_pose = '0' + str(int(eval('pose3_' + str(1 + int(tm[3]) % 3) )))
    scene Ann_yoga basic
    $ persone_button1 = 'Ann yoga ann-yoga-' + var_pose + ann.dress
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


label ann_dressed:
    scene location house annroom door-morning
    if ann.hourly.dressed:
        return
    $ ann.hourly.dressed = 1
    # $ renpy.dynamic('open', 'lst', 'r1', 'balcony')
    $ open = False
    $ mood = 0
    $ spent_time = 10
    # Эрик изгнан, час переодеваний в будние дни, в сумке нет ночнушки
    $ balcony = random_choice([True, False]) if all([flags.eric_banished, '11:00' > tm >= '10:00', weekday != 6, not items['nightie'].have]) else False

    if weekday == 6:
        Max_09 "{m}Сегодня суббота, день шоппинга. Видимо, мама собирается...{/m}" nointeract
    else:
        Max_09 "{m}Сейчас 10 часов, а значит, мама собирается на работу...{/m}" nointeract
    menu:
        "{i}постучаться{/i}":
            menu:
                Ann "{b}Анна:{/b} Кто там?"
                "Это я, Макс. Можно войти?"  if not items['nightie'].have:
                    if weekday == 6:
                        Ann "{b}Анна:{/b} Нет, Макс. Я переодеваюсь. Подожди немного, дорогой."
                    else:
                        Ann "{b}Анна:{/b} Макс, я не одета. Собираюсь на работу. Подожди немного, дорогой."
                    Max_00 "Хорошо, мам."
                    jump .end
                "Это я, Макс. Можно войти? У меня для тебя кое-что есть." if items['nightie'].have:
                    Ann "{b}Анна:{/b} Макс, я не одета. Собираюсь на шопинг. Подожди немного, дорогой."
                    Max_00 "Хорошо, мам."
                    jump .gift
                "{i}уйти{/i}":
                    jump .end
        "{i}открыть дверь{/i}":
            if balcony:
                call .balcony from _call_ann_dressed_balcony
            elif all([random_outcome(40), tm[-2:]=='00', not (items['nightie'].have and ann.plan_name == 'dressed')]):
                # не срабатывает в час переодевания, если в сумке ночнушка
                call .moment0 from _call_ann_dressed_moment0_1   # "нулевой"
            elif random_outcome(45):
                call .moment1 from _call_ann_dressed_moment1   # неповезло
            else:
                call .moment2 from _call_ann_dressed_moment2   # повезло
            jump .end
        "{i}заглянуть в окно{/i}":
            $ mood = 0
            if weekday == 6:
                $ lst = ['03', '03a', '04']
            else:
                $ lst = ['01', '01a', '02', '03', '03a', '04']
            if ann.dress=='d':
                $ lst.extend(['05', '06', '06a'])
            $ r1 = random_choice(lst)
            $ ann.dress_inf = {'01':'02e', '01a':'02c', '02':'02d', '03':'02', '03a':'02a', '04':'02b', '05':'2g', '06':'2i', '06a':'2h'}[r1]

            if mgg.stealth >= 11.0 and random_choice([False, False, True]):
                scene BG char Ann voyeur-01
                $ renpy.show('Ann voyeur alt-'+r1)
                $ renpy.show('FG voyeur-morning-01'+mgg.dress)
            else:
                scene BG char Ann voyeur-00
                $ renpy.show('Ann voyeur '+r1)
                $ renpy.show('FG voyeur-morning-00'+mgg.dress)

            $ Skill('hide', 0.03, 10)
            Max_01 "{m}Ничего себе, вот это зрелище! Это я удачно выбрал момент... Но пора уходить, а то вдруг увидит меня в зеркало!{/m}"
            jump .end
        "{i}уйти{/i}":
            jump .end

    label .stay_in_room:
        # $ renpy.dynamic('lvl')
        $ ann.hourly.dressed = 1
        $ get_ann_dress(0)
        $ mood = 0

        ### фон + поза
        if ann.prev_plan == 'shower2':      # Эрик в комнате
            scene Ann_dressing eric
            if flags.eric_wallet == 2:      # Макс на сроке за воровство
                Eric_09 "Макс, не мешай взрослым! В твоём положении это просто верх наглости! Найди себе занятие..." nointeract
            else:
                Ann_00 "Сынок, мы с Эриком собирались переодеться. Не мешай взрослым, займись чем-нибудь..." nointeract
        else:                               # Анна одна
            scene Ann_dressing
            if flags.eric_wallet == 2:      # Макс на сроке за воровство
                Ann_12 "Сынок, я собиралась переодеться. Не мешай маме. Займись чем-нибудь полезным..." nointeract
            else:
                Ann_00 "Сынок, я собиралась переодеться. Иди пока, займись чем-нибудь..." nointeract
        if all([lvl > 2, ann.prev_plan != 'shower2', flags.eric_wallet != 2]):
            menu:
                "А посмотреть нельзя?":
                    Ann_12 "Нет, конечно! Ишь ты, что удумал! Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
                "Да легко! Не буду мешать. Выглядишь, кстати, превосходно!":
                    Ann_05 "Приятно слышать, сынок. Спасибо, что подметил." nointeract
        menu:
            "{i}уйти{/i}":
                jump .end

    label .moment0:     # "нулевой"
        $ ann.hourly.dressed = 1
        $ lvl = get_ann_emancipation()
        $ get_ann_dress(0)
        $ mood = 0

        ### фон + поза
        if ann.prev_plan == 'shower2':      # Эрик в комнате
            scene Ann_dressing eric
            if flags.eric_wallet == 2:      # Макс на сроке за воровство
                Eric_09 "Макс, не мешай взрослым! В твоём положении это просто верх наглости! Найди себе занятие..." nointeract
            else:
                Ann_00 "Сынок, мы с Эриком собирались переодеться. Не мешай взрослым, займись чем-нибудь..." nointeract
            menu:
                "{i}уйти{/i}":
                    jump .end

        scene Ann_dressing
        menu:
            Ann_00 "Так, сынок... Ты можешь погулять? А то мне нужно переодеться..."
            "А я разве чем-то помешаю?" if lvl == 1:
                Ann_13 "Конечно! Это как-то неправильно, если мать будет переодеваться при своём ребёнке. Так что, пожалуйста, выйди ненадолго." nointeract
            "А я не помешаю. Начинай..." if lvl == 2:
                Ann_12 "Ишь ты, что удумал! Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
            "Да легко! Не буду мешать..." if lvl < 3:
                Ann_01 "Спасибо, Макс. Если ты что-то хотел, то я недолго..." nointeract
            "А посмотреть нельзя?" if lvl == 3:
                Ann_12 "Нет, конечно! Ишь ты, что удумал! Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
            "Да легко! Не буду мешать. Выглядишь, кстати, превосходно!" if lvl == 3:
                Ann_05 "Приятно слышать, сынок. Спасибо, что подметил." nointeract
            "Подожди! Мне кажется или у тебя под халатом что-то шевелится..." if lvl > 3 and var_dress[0] == 'b':
                $ get_ann_dress(2, var_pose)
                # первый момент с халатом
                Ann_13 "Ой, Макс! Где именно?!"
                Max_02 "А нет, это были твои прекрасные сосочки!"
                # третий момент с халатом
                $ get_ann_dress(3, var_pose)
                Ann_05 "Ну и шуточки у тебя, Макс! Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
            "А можно остаться и посмотреть?" if lvl > 3:
                Ann_05 "Макс! Тебе что, мало того, что ты уже увидел? Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
            "Да легко! А повернуться можешь, пока я ухожу?" if lvl > 3  and var_dress[0] not in ['b', 'g']:
                # Анна поворачивается задом
                $ get_ann_dress(3, var_pose, True)
                Ann_05 "Только под ноги смотри, сынок. А то мало ли куда лбом врежешься..." nointeract
        menu:
            "{i}уйти{/i}":
                jump .end

    label .moment2:   # повезло
        $ ann.hourly.dressed = 1
        $ lvl = get_ann_emancipation()
        $ get_ann_dress(2)
        $ mood = 0

        ### фон + поза
        scene Ann_dressing

        if lvl == 1:
            Ann_15 "Макс! Я же учила тебя стучаться! {p=3}{nw}"
        elif lvl == 2:
            Ann_15 "Макс! А стучаться кто будет?! {p=3}{nw}"
        else:
            Ann_13 "Ой, Макс! Почему не стучишься? {p=3}{nw}"

        # изменение позы вызывает автоматическое обновление изображения
        ### поза
        if lvl > 3:
            $ get_ann_dress(3, var_pose)
        else:
            $ get_ann_dress(1, var_pose)

        if lvl == 1:
            Ann_14 "Нельзя вот так без предупреждения врываться в комнату! Что-то случилось?" nointeract
            jump .lvl_1
        elif lvl == 2 or (items['nightie'].have and ann.plan_name=='dressed'):
            Ann_12 "Прекращай уже без предупреждения врываться в комнату! Или у тебя что-то срочное?" nointeract
            jump .lvl_2
        elif lvl == 3:
            Ann_02 "Ты что-то хотел или просто от безделья маешься?"
            jump .lvl_3
        elif lvl==4:
            Ann_02 "Ты что-то хотел или просто от безделья маешься?"
            jump .lvl_4

    label .moment1:     # неповезло
        $ ann.hourly.dressed = 1
        $ lvl = get_ann_emancipation()
        if lvl > 3:
            $ get_ann_dress(3)
        else:
            $ get_ann_dress(1)
        $ mood = 0

        ### фон + поза
        scene Ann_dressing

        if lvl == 1:
            Ann_15 "Макс! Я же учила тебя стучаться! Нельзя вот так без предупреждения врываться в комнату! Что-то случилось?" nointeract
            jump .lvl_1
        elif lvl == 2 or (items['nightie'].have and ann.plan_name=='dressed'):
            Ann_15 "Макс! А стучаться кто будет?! Прекращай уже без предупреждения врываться в комнату! Или у тебя что-то срочное?" nointeract
            jump .lvl_2
        elif lvl == 3:
            Ann_13 "Ой, Макс! Почему не стучишься? Ты что-то хотел или просто от безделья маешься?"
            jump .lvl_3
        elif lvl == 4:
            Ann_13 "Ой, Макс! Почему не стучишься? Ты что-то хотел или просто от безделья маешься?"
            jump .lvl_4

    label .lvl_1:
        menu:
            "У меня для тебя кое-что есть." if items['nightie'].have and ann.plan_name=='dressed':
                Ann_12 "Очень здорово, Макс! Но сначала, ты закроешь дверь и я спокойно переоденусь, а уже после этого посмотрим, что у тебя там такое срочное..."
                Max_00 "Конечно, мам!"
                scene location house annroom door-morning
                Max_00 "{m}Пожалуй, не стоило вот так врываться к маме... Надеюсь, подарок всё сгладит.{/m}"
                jump .gift

            "У тебя самые зачётные сиськи, которые я видел!" if var_pose < '04':
                # Анна стоит передом к Максу
                $ mood -= 30
                Ann_17 "Что?! Макс! Это что ещё за словечки такие? А ну-ка быстро выйди и закрой дверь!" nointeract

            "У тебя самый потрясный зад на свете, мам!" if '03' < var_pose < '08':
                # Анна стоит задом к Максу
                $ mood -= 30
                Ann_17 "Что я слышу! Вряд ли я та женщина, которой стоит такое говорить, Макс. А теперь выйди и закрой дверь!" nointeract

            "Я просто хотел посмотреть..." if var_pose == '08':
                # Анна прикрывает только низ
                $ mood -= 10
                Ann_13 "Как я переодеваюсь?! Сынок, ты что такое говоришь! Давай-ка выйди и закрой за собой дверь." nointeract

            "Ой, извини. Я забыл... Хорошо выглядишь, мам!":
                Ann_12 "Спасибо, конечно. Но... Макс, не мог бы ты подождать за дверью, пока я оденусь?" nointeract
        menu:
            "{i}уйти{/i}":
                jump .end

    label .lvl_2:
        menu:
            "У меня для тебя кое-что есть." if items['nightie'].have and ann.plan_name=='dressed':
                Ann_12 "Очень здорово, Макс! Но сначала, ты закроешь дверь и я спокойно переоденусь, а уже после этого посмотрим, что у тебя там такое срочное..."
                Max_00 "Конечно, мам!"
                scene location house annroom door-morning
                Max_00 "{m}Пожалуй, не стоило вот так врываться к маме... Надеюсь, подарок всё сгладит.{/m}"
                jump .gift

            "Да не прикрывай такую красоту, все свои же!" if var_pose < '04':
                # Анна стоит передом к Максу
                $ mood -= 10
                Ann_13 "Макс! И не стыдно тебе такое своей маме говорить, а? Ну-ка бегом за дверь, а то мешаешь." nointeract

            "Сразу видно, что попка у тебя тренированная!" if '03' < var_pose < '08':
                # Анна стоит задом к Максу
                $ mood -= 10
                Ann_13 "Даже не знаю, что на это ответить... Ну-ка бегом за дверь, а то засмущал меня." nointeract

            "А посмотреть нельзя?" if var_pose == '08':
                # Анна прикрывает только низ
                Ann_12 "Нет, конечно! Ишь ты, что удумал! Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract

            "Извини, всё позабыл, когда тебя увидел. Ты прекрасна!":
                $ mood += 20
                Ann_02 "Приятно слышать. Но маме нужно переодеться... Так что подожди за дверью, хорошо?" nointeract
        menu:
            "{i}уйти{/i}":
                jump .end

    label .lvl_3:
        Max_01 "Нет, просто решил заглянуть. А ты что, всё ещё стесняешься? Это же я!"

        $ relax = get_ann_dress(3, var_pose)

        if relax:
            Ann_04 "Да это я так, по привычке. Если у тебя ничего срочного, то выйди пожалуйста. Мне нужно переодеться..." nointeract
        else:
            Ann_04 "Конечно стесняюсь! Ещё я тут всю себя на показ не выставляла, только из-за того, что ты уже всё видел. Если у тебя ничего срочного, то выйди пожалуйста. Мне нужно переодеться..." nointeract
        menu:
            "А посмотреть нельзя?":
                Ann_12 "Нет, конечно! Ишь ты, что удумал! Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
            "Да легко! Не буду мешать. Выглядишь, кстати, превосходно!":
                Ann_05 "Приятно слышать, сынок. Спасибо, что подметил." nointeract
        menu:
            "{i}уйти{/i}":
                jump .end

    label .lvl_4:
        Max_02 "Нет, просто решил заглянуть и полюбоваться на твою шикарную фигуру. Ты же не против?"
        Ann_04 "Ну... Если налюбовался, то выйди пожалуйста. Мне нужно переодеться..." nointeract
        menu:
            "А можно остаться и посмотреть?":
                Ann_05 "Макс! Тебе что, мало того, что ты уже увидел? Завязывай с этими глупостями и дай маме спокойно переодеться." nointeract
            "Да легко! А повернуться можешь, пока я ухожу?":
                # Анна поворачивается задом, если стояла передом и наоборот
                $ get_ann_dress(3, var_pose, True)
                Ann_05 "Только под ноги смотри, сынок. А то мало ли куда лбом врежешься..." nointeract
        menu:
            "{i}уйти{/i}":
                jump .end

    label .gift:
        # scene BG char Ann mde-01
        # $ renpy.show('Ann dressed 07' + ('j' if weekday == 6 else 'a'))
        $ get_ann_dress('g')
        scene Ann_dressing
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
        # scene BG char Ann mde-01
        # $ renpy.show('Ann dressed 07' + ('j' if weekday == 6 else 'a'))
        scene Ann_dressing
        Ann_08 "Ох... Спасибо за комплимент, мой милый. Сразу видно, что мой сын настоящий мужчина! Иди ко мне, я тебя обниму..."
        # $ r1 = random_choice(['01', '02'])
        # $ renpy.show('Ann hugging morning-annroom '+r1+'-1'+('b' if weekday == 6 else 'a')+mgg.dress)
        $ var_pose = random_choice(['01', '02'])
        scene Ann_gift hug1
        Max_05 "{m}О да... У меня действительно лучшая мама на свете! Какая же потрясающая у неё фигура... Так приятно прижиматься к ней... её упругой груди... Эту мечту не хочется отпускать!{/m}"
        # $ renpy.show('Ann hugging morning-annroom '+r1+'-2'+('b' if weekday == 6 else 'a')+mgg.dress)
        scene Ann_gift hug2
        $ spent_time += 10
        if weekday == 6:
            Ann_04 "Ну всё, мой дорогой, нам с девочками ещё нужно успеть пробежаться по магазинам сегодня..." nointeract
        else:
            Ann_04 "Ну всё, мой дорогой, мне уже скоро на работу и нужно успеть сделать ещё кое-какие дела..." nointeract
        menu:
            "Ну мам! Этого было так мало, давай ещё..." ('soc', mgg.social * 3, 90) if not open:
                if rand_result:
                    $ spent_time += 10
                    Ann_05 "[succes!t]Ты сегодня очень мил, Макс! За это я тебя даже в щёчку поцелую, чтобы ты почаще старался меня радовать..."
                    # $ renpy.show('Ann hugging morning-annroom '+r1+'-3'+('b' if weekday == 6 else 'a')+mgg.dress)
                    scene Ann_gift hug3
                    Max_06 "{m}Ого! Это даже больше того, на что я надеялся... И не менее приятно чувствовать прикосновение её губ на своём лице! Блаженно...{/m}"
                    # $ renpy.show('Ann hugging morning-annroom '+r1+'-2'+('b' if weekday == 6 else 'a')+mgg.dress)
                    scene Ann_gift hug2
                    $ AddRelMood('ann', 0, 200)
                    $ AttitudeChange('ann', 0.9)
                    menu:
                        Ann_04 "А теперь иди, сынок... Пора заниматься делами."
                        "Хорошо... Я тебя люблю, мам!":
                            jump .loveyou
                        "Конечно, мам! Хорошего тебе дня...":
                            jump .goodday
                else:
                    $ AddRelMood('ann', 0, 170)
                    $ AttitudeChange('ann', 0.8)
                    jump .fail

            "Ну мам! Этого было так мало, давай ещё..." if open:
                $ AddRelMood('ann', 0, 150)
                $ AttitudeChange('ann', 0.7)
                jump .fail
            "Конечно, мам! Хорошего тебе дня...":
                jump .goodday

    label .fail:
        $ _text = failed if open else ""
        if weekday == 6:
            Ann_01 "[_text!t]Макс, мне нужно ещё успеть сделать кое-какие дела... Давай, сынок, иди... Займись чем-нибудь." nointeract
        else:
            Ann_01 "[_text!t]Макс, я так на работу не успею собраться... Давай, сынок, иди... Пора заниматься делами." nointeract
        menu:
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
        $ items['nightie'].give()
        $ ann.gifts.append('nightie')
        $ setting_clothes_by_conditions()
        $ infl[ann].add_m(40, True)
        $ mood = 0
        $ prev_room = house[2]
        $ current_room = house[5]  # Макс выходит на веранду
        jump .end

    label .balcony:
        # $ renpy.dynamic('lvl')
        # $ ann.hourly.dressed = 1
        $ lvl = get_ann_emancipation()
        $ mood = 0

        # annroom-wardrobe-mde-01
        scene Ann_dressing empty
        Max_07 "{m}Хм... Должно быть мама на балконе...{/m}"

        if _in_replay or any([
            all([tm>='10:30', 6 > weekday > 0, not ann.flags.showdown_e]),   # 1-ый разговор (только в рабочие дни)
            all([tm>='10:30', 6 > weekday > 0, ann.flags.showdown_e == 1, ann.dcv.other.done]),   # 2-ой разговор (в рабочие дни или воскресенье), не раньше, чем через 5 дней после 1-ого разговора на балконе
            all(['11:00'>tm>='10:00', weekday == 0, ann.flags.showdown_e == 1, ann.dcv.other.done]),   # 2-ой разговор (в рабочие дни или воскресенье), не раньше, чем через 5 дней после 1-ого разговора на балконе
            all([tm>='10:30', 6 > weekday > 0, ann.flags.showdown_e > 1]),   # периодический разговор (в рабочие дни или воскресенье), доступен через день
            all(['11:00'>tm>='10:00', weekday == 0, ann.flags.showdown_e > 1]),   # периодический разговор (в рабочие дни или воскресенье), доступен через день
                                                            ]):
            # если рабочий день и Анна одета
            # annroom-balcony-md-01 + annroom-balcony-md-01-ann-dresses-01a
            $ get_ann_dress('b0')
            scene Ann_dressing balcony zero
            Max_09 "{m}То ли мама просто задумалась, то ли грустит...{/m}" nointeract
            menu:
                "Мам, всё нормально?" if not _in_replay and ann.flags.showdown_e < 2:
                    # annroom-balcony-md-01 + annroom-wardrobe-mde-01-ann-dresses-07a
                    scene Ann_dressing balcony
                    Ann_12 "Ой, Макс! Ты слишком тихо ходишь. А я так, ничего, просто задумалась немного..."
                    Max_07 "Расскажешь, о чём?"
                    if not ann.flags.showdown_e:
                        jump .balkon_talk1
                    else:   # elif ann.flags.showdown_e == 1:
                        jump .balkon_talk2
                "Видами любуешься, мам?"  if _in_replay or ann.flags.showdown_e > 1:
                    jump .balkon_r

                "{i}уйти{/i}" if not _in_replay:
                    jump .end
        else:
            # annroom-balcony-md-01 + annroom-balcony-md-01-ann-dresses-(01/01c2)   # рабочий день и Анна ещё не одета
            $ get_ann_dress('b')
            scene Ann_dressing balcony zero
            Max_05 "{m}Оу! Мама ещё не оделась... Это я вовремя зашёл. Она шикарно смотрится...{/m}" nointeract
            menu:
                "Мам?":
                    # annroom-balcony-md-01 + прикрывания
                    # дальше текст, как в переодеваниях НЕ ПОВЕЗЛО по уровням
                    $ get_ann_dress(1, var_pose)
                    scene Ann_dressing balcony
                    if lvl == 1:
                        Ann_15 "Макс! Я же учила тебя стучаться! Нельзя вот так без предупреждения врываться в комнату! Что-то случилось?" nointeract
                        jump .lvl_1
                    elif lvl == 2:
                        Ann_15 "Макс! А стучаться кто будет?! Прекращай уже без предупреждения врываться в комнату! Или у тебя что-то срочное?" nointeract
                        jump .lvl_2

                "{i}продолжить смотреть{/i}":
                    #annroom-balcony-md-01 + 3 сек задержки
                    #дальше текст, как в переодеваниях ПОВЕЗЛО по уровням
                    scene Ann_dressing balcony
                    if lvl == 1:
                        Ann_15 "Макс! Я же учила тебя стучаться! {p=3}{nw}"
                    elif lvl == 2:
                        Ann_15 "Макс! А стучаться кто будет?! {p=3}{nw}"
                    $ get_ann_dress(1, var_pose)
                    if lvl == 1:
                        Ann_14 "Нельзя вот так без предупреждения врываться в комнату! Что-то случилось?" nointeract
                        jump .lvl_1
                    elif lvl == 2:
                        Ann_12 "Прекращай уже без предупреждения врываться в комнату! Или у тебя что-то срочное?" nointeract
                        jump .lvl_2

                "{i}уйти{/i}":
                    jump .end

    label .balkon_talk1:
        # 1-ый разговор (только в рабочие дни)
        # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-01 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
        $ var_pose = '01'
        scene Ann_dressing talk
        Ann_14 "У меня сейчас такое состояние, что я не знаю, как мне жить дальше... Я... Я ужасная мать..."
        Max_08 "Что?! Как ты можешь такое говорить?"
        Ann_13 "А разве нет? Я... Я была так глупа, что привела в дом проходимца, который не только воспользовался мной, но и чуть не совратил моих девочек!"
        Max_09 "Мам, прекрати, это уже всё в прошлом... Забудь..."
        Ann_14 "Забыть? Забыть, как я чуть не отправила единственного сына в военный лагерь и... который один оказался настолько умным и благородным, что не только не разозлился на меня, а наоборот, спас всю семью от этого ублюдка - Эрика."
        Max_07 "Ну хватит... Было и было. Прими это и сделай выводы. Нельзя же всё время теперь ходить такой печальной и заниматься самобичеванием. Ты ни в чём не виновата!"
        Ann_17 "Возможно ты прав, но... присутствие Эрика на работе постоянно мне напоминает о тех событиях и мне это ужасно неприятно."
        Max_15 "Да и чёрт с ним! Просто игнорируй его. К тому же, у тебя есть мы, и мы все тебя очень любим!"
        Ann_02 "Спасибо, мой хороший, за твои тёплые слова и поддержку, мне очень приятно это слышать."
        Max_04 "Не стоит благодарить, мам. Я очень тебя люблю! Ты самая замечательная мама на свете! Самая добрая и самая красивая!"
        # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-02 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
        $ var_pose = '02'
        Ann_04 "Ой! Вот же ты маленький льстец, Макс!"
        Max_07 "Это я-то маленький?"
        Ann_05 "Ну, конечно, ты большой, Макс! Совсем взрослый, почти мужчина."
        Max_09 "Что значит почти?"
        Ann_07 "Ну... То и значит, что полноценным мужчиной ты станешь только после того, как у тебя появится девушка."
        Max_08 "Серьёзно? А поподробнее можно узнать, как и что делать с ней, чтобы стать мужчиной?"
        Ann_02 "Макс, что за вопросы? Как будто ты до сих пор не знаешь."
        Max_02 "Да это я просто так спросил... Теперь ты уже не такая печальная и задумчивая, как до моего прихода."
        Ann_05 "Вот же ты хитрец! Нашёл чем меня отвлечь..."
        Max_03 "Могу отвлечь чем-нибудь приятным. Например, массажем спины. Думаю, это тебе бы сейчас помогло. Хочешь?"
        Ann_04 "Нет, Макс, сейчас мне некогда. Давай вечерком, сынок, у ТВ."
        Max_01 "Договорились, мам. И не забывай, если что, я всегда рядом. Обращайся!"
        Ann_01 "Обязательно!" nointeract
        menu:
            "{i}уйти{/i}":
                $ spent_time = 20
                $ ann.flags.showdown_e = 1
                $ ann.dcv.other.set_lost(6)
                $ prev_room = house[2]
                $ current_room = house[5]  # Макс выходит на веранду
                $ infl[ann].add_m(20, True)
                $ poss['boss'].open(2)
                $ mood = 100
                jump .end

    label .balkon_talk2:
        # 2-ой разговор (в рабочие дни или воскресенье)
        #не раньше, чем через 5 дней после 1-ого разговора на балконе
        # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-01 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
        $ var_pose = '01'
        scene Ann_dressing talk
        Ann_14 "Это всё моя работа... Присутствие Эрика делает её просто невыносимой."
        Max_15 "Он пристаёт к тебе?"
        Ann_18 "Нет, но его ехидная ухмылочка и постоянные намёки о возможных неприятностях, если я вдруг попытаюсь уволиться, сводят меня с ума."
        Max_09 "Просто постарайся не обращать на него внимание."
        Ann_12 "Вряд ли это возможно, сынок, он же мой начальник." nointeract
        menu:
            "{i}приобнять маму за попку{/i}":
                pass

        # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-03 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
        $ var_pose = '03'
        Ann_13 "Макс, ты что это делаешь? За зад меня обнимаешь?!"
        Max_07 "Ну да. Это я так приободрить тебя решил. Если бы он действительно хотел тебе что-то сделать, то он бы уже давно это сделал."
        Ann_17 "Сынок, такое вот твое приободрение не работает. Оно меня скорее смущает..."

        # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-02 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
        $ var_pose = '02'
        Max_09 "Ладно, уберу... Просто Эрику нравится играть на нервах, вот и всё, что он может сделать."
        Ann_12 "Возможно так и есть, но... мне бы очень не хотелось искушать судьбу... это ведь может отразиться и на вас, моих детях, а вы для меня самое дорогое."
        Max_10 "Ты тоже самое дорогое для меня... для нас... И нам бы не хотелось видеть тебя такой печальной, мам."
        Ann_02 "Спасибо, Макс. Мне очень приятно это слышать. Как хорошо, что у меня есть такой внимательный и заботливый сын."
        Max_07 "В любом случае, если ты захочешь сменить место работы и у нас, вдруг, появятся сложности с деньгами, мы все тебя поймём и поддержим."
        Ann_04 "Спасибо, мой хороший, я подумаю об этом..."
        Max_09 "Обязательно подумай. Нужно покончить с этим прошлым раз и навсегда!"
        Ann_05 "Хм... Глядя на тебя в последнее время, я вижу, что ты очень повзрослел."
        Max_04 "Ну, тебе виднее."
        Ann_08 "Так и есть. И мне нравится то, что я вижу..."
        Max_03 "Главное не унывай, мам. Всё образуется."
        Ann_07 "Хорошо! Спасибо, что поддержал меня и развеял тоску."
        Max_01 "Пожалуйста! Если что, я всегда рядом. Обращайся!"
        Ann_01 "Обязательно!" nointeract

        menu:
            "{i}уйти{/i}":
                $ spent_time = 20
                $ ann.flags.showdown_e = 2
                $ ann.dcv.other.set_lost(3)
                $ infl[ann].add_m(15, True)
                $ poss['boss'].open(3)
                $ mood = 75

        # after-breakfast + ad-max-(00a/00b)
        scene thinking_max_terrace
        # scene BG after-breakfast
        # $ renpy.show("Max talk-terrace 00"+mgg.dress)
        Max_09 "{m}Смущают её мои прикосновения... Ясно. Значит, нужно больше прикасаться тогда, когда это максимально естественно, чтобы она привыкла. Пожалуй, йога - то, что нужно! Стоит попробовать...{/m}"

        $ prev_room = house[2]
        $ current_room = house[5]  # Макс выходит на веранду
        jump .end

    label .balkon_r:
        # annroom-balcony-md-01 + annroom-wardrobe-mde-01-ann-dresses-(07a/07e/07f)
        scene Ann_dressing balcony
        Ann_02 "Ой, Макс! Как ты так тихо подкрадываешься? Да, любуюсь... А ты почему без дела слоняешься?" nointeract
        menu:
            "А что, я мешаю?" if not ann.dcv.other.done:
                Ann_01 "Не то, чтобы мешаешь... Иди лучше чем-нибудь продуктивным займись. Маме пока некогда."
                Max_00 "Ладно, не буду мешать." nointeract
                menu:
                    "{i}уйти{/i}":
                        jump .end
            "С тобой хотел побыть. Или я мешаю?" if ann.dcv.other.done:
                pass
        Ann_04 "Нет. Побудь, если хочется. Я не против." nointeract
        menu:
            "{i}приобнять маму{/i}":
                pass
        # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-01 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
        $ var_pose = '01'
        scene Ann_dressing talk
        Ann_02 "Как у тебя дела, Макс? Всё хорошо?"
        Max_04 "Да, порядок. А ты как? Не скучаешь?"
        Ann_05 "Ох, сынок, с вами разве заскучаешь. Да и на работе дел хватает." nointeract
        menu:
            "{i}продолжить обнимать{/i}":
                # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-02 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
                $ var_pose = '02'
                Max_07 "Ты, мам, побольше отдыхать не забывай."
                Ann_07 "Это я и делаю сейчас. А ты давай беги, займись чем-нибудь полезным."

                if ann.flags.m_back > 2:
                    # было 3 успешных массажа спины Анны у ТВ
                    #annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-05 + Одежда (Макс перекрывает Анну) + annroom-balcony-md-02a
                    $ var_pose = '05'

            "{i}приобнять маму за попку{/i}" if ann.flags.truehelp > 4:
                # было 5 успешных расширенных йог
                # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-03 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
                $ var_pose = '03'
                Max_07 "Ты, мам, побольше отдыхать не забывай. У нас слишком прекрасный дом, чтобы грустить."
                Ann_08 "Да, здесь здорово! Маленький рай. Ты зашёл меня просто вот так подбодрить?"

                # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-04 + Одежда (Анна перекрывает Макса) + annroom-balcony-md-02a
                $ var_pose = '04'
                Max_02 "Ну, да. Хотел напомнить, что я всегда рядом."
                Ann_07 "Спасибо, но лучше беги, займись чем-нибудь полезным. У меня всё в порядке."

                if ann.flags.m_back > 2:
                    # было 3 успешных массажа спины Анны у ТВ
                    # annroom-balcony-md-02 + annroom-balcony-md-02-max&ann-05 + Одежда (Макс перекрывает Анну) + annroom-balcony-md-02a
                    $ var_pose = '05'
                    $ added_mem_var('balcony_hug')

        Max_03 "Ладно, не буду отвлекать. Я тебя люблю, мам!"
        Ann_06 "Я тебя тоже, сынок." nointeract
        menu:
            "{i}уйти{/i}":
                $ renpy.end_replay()
                $ spent_time = 20
                $ ann.dcv.other.set_lost(2)
                $ infl[ann].add_m(5, True)
                $ mood = 30
                $ prev_room = house[2]
                $ current_room = house[5]  # Макс выходит на веранду

    label .end:
        $ ann.hourly.dressed = 1
        $ ann.prev_plan = ann.plan_name
        $ AddRelMood('ann', 0, mood)
        jump Waiting


label ann_resting:

    if any([
        all([not ann.hourly.dressed, '11:00' > tm >= '10:00', ann.flags.showdown_e == 1, ann.dcv.other.done]),  # 2-ой разговор (в рабочие дни или воскресенье), не раньше, чем через 5 дней после 1-ого разговора на балконе
        all([not ann.hourly.dressed, '11:00' > tm >= '10:00', ann.flags.showdown_e > 1]),                       # периодический разговор (в рабочие дни или воскресенье), доступен через день
        ]):
        jump ann_dressed.balcony

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
    scene BG 2sun-00
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
    if ann.daily.bath != 0:
        return

    $ ann.daily.bath = 1
    if ann.dcv.private.stage > 3:
        # Анну удалось уговорить на продолжение интимных уроков
        jump s1_ann_bath

    menu:
        Max_00 "{m}Видимо, мама принимает ванну...{/m}"
        "{i}постучаться{/i}" if all([get_rel_eric()[0] == 2, flags.voy_stage == 8, ann.dcv.feature.stage > 3, ann.flags.m_back > 2, ann.flags.truehelp > 4, not ann.dcv.private.stage]):
            # Д-, прекращены шоу АиЭ, знает секрет Анны, 3 раза успешно сделал массаж, 5 раз скрыл стояк на йоге
            jump .about_intime_0
        "{i}постучаться{/i}" if all([get_rel_eric()[0] == 3, flags.voy_stage > 11, flags.voy_stage != 0, ann.dcv.feature.stage > 3, ann.flags.m_back > 2, ann.flags.truehelp > 4, not ann.dcv.private.stage]):
            # Д+, попал на просмотр шоу АиЭ (после возобновления), знает секрет Анны, 3 раза успешно сделал массаж, 5 раз скрыл стояк на йоге
            jump .about_intime_0
        "{i}заглянуть со двора{/i}" if flags.ladder < 2:
            scene Ann bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "{m}Эх... жаль, что стекло частично матовое. Так ничего не разглядеть! А если подобраться ближе, то мама может заметить...{/m}"
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

        $ __r1 = random_randint(1, 4)

        scene BG bath-00
        $ renpy.show('Ann bath-window 0'+str(__r1))
        show FG bath-00
        $ Skill('hide', 0.025, 10)
        if __r1 == 1:
            menu:
                Max_03 "{m}Ох, как горячо! Разумеется, я не про воду, а про её внешний вид. Ухх... Мама потрясающе выглядит...{/m}"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Ann bath-window '+random_choice(['02', '03', '04']))
                    $ Skill('hide', 0.025, 10)
                    menu:
                        Max_05 "{m}Ух ты, аж завораживает! Мамины водные процедуры могут посоперничать с самыми горячими эротическими роликами! Эта упругая грудь и эти длинные стройные ножки сведут с ума кого угодно...{/m}"
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ ann.dress_inf = '00a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end
        else:
            menu:
                Max_05 "{m}Ух ты, аж завораживает! Мамины водные процедуры могут посоперничать с самыми горячими эротическими роликами! Эта упругая грудь и эти длинные стройные ножки сведут с ума кого угодно...{/m}"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Ann bath-window 05
                    $ Skill('hide', 0.025, 10)
                    menu:
                        Max_07 "{m}Эх! Похоже, самое интересное закончилось... Хотя, смотреть как мама вытирает своё мокрое и соблазнительное тело не менее приятно! Ох, какая же у неё попка...{/m}"
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ ann.dress_inf = '04a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end

    label .about_intime_0:
        Ann "{b}Анна:{/b} Кто там? Я принимаю ванну!"
        Max_07 "Это я, Макс. Можно войти?"
        Ann "{b}Анна:{/b} Зачем, дорогой? Тебе что-то нужно?"
        Max_09 "Да, мам. Хотел поговорить."
        Ann "{b}Анна:{/b} Если это может подождать, то я через полчасика освобожусь..." nointeract
        menu:
            "{i}войти{/i}":
                $ ann.dcv.private.stage = 1     # состоялся первый разговор с Анной о "других" уроках
                $ ann.dcv.private.set_lost(3)
            "{i}уйти{/i}":
                jump .end

        if get_rel_eric()[0] == 2:
            $ poss['control'].open(12)
        elif get_rel_eric()[0] == 3:
            $ poss['control'].open(15)


        # bath-open-00 + bath-open-ann-01
        scene ann_in_bath_open with diss4
        Ann_15 "Макс! Ты почему так нагло врываешься! Я же сказала, что скоро освобожусь! Не мог подождать?"
        Max_08 "Нет, нужно кое-что обсудить, пока ты здесь."

        # bathrooom-bath-02 + bathrooom-bath-02-ann-00
        $ var_pose = '00'
        scene ann_in_bath_enter with diss4
        Ann_14 "И что там у тебя такого срочного?!"
        Max_07 "Хотел поговорить о девочках!"
        Ann_17 "И ты считаешь, что это настолько важно, что кроме как здесь об этом говорить нельзя, да?"
        Max_01 "Ну... Не просто о девочках, а том, как им... делать приятно... там, внизу..."
        Ann_02 "Вот это вопросы у тебя, Макс! А что, у тебя девочка появилась?"
        Max_07 "Ещё нет, но появится же. А я хочу быть готовым! Вы мне с Эриком показали на тех уроках, как себя вести, если женщина... так сказать, ласкает мужчину, а вот как ласкать женщин - нет."
        Ann_14 "Ой, сынок, какие же это неудобные вопросы! Я всё ещё до конца не могу осознать, что ты уже почти взрослый."
        Max_09 "Пора бы уже осознать, мам! И уроки ваши, какие-то односторонние. Как-то неправильно."
        Ann_13 "Ну... Что-то я даже не знаю..."

        # after-club-bath01-max&alice-01-f + bathrooom-bath-02-ann&max-01 + Одежда(только Макс)
        $ var_stage = '02'
        $ var_pose = '01'
        scene ann_in_bath_talk with diss4
        Max_07 "Да ладно, я же уже такое видел с вами на тех уроках..."
        Ann_12 "Ой, Макс, не напоминай. Это всё было исключительно для твоего... сексуального образования..."
        Max_08 "Так и это тоже для образования! Потому что я хочу не только получать ласку от девочек, но и давать её им. А это, как я понимаю, куда сложнее."
        Ann_13 "Ох, с учётом того, чему мы с Эриком уже тебя тогда научили, твоя просьба очень логична, сынок. Так что я поговорю об этом с Эриком..."
        Max_10 "Нет, мам, я хочу только с тобой этому учиться!"
        Ann_17 "То есть, только со мной?! А Эрик тебе чем не угодил?"
        Max_09 "Мне кажется, он это... направление не особо любит. Мне же лучше, чтобы такому учила именно женщина, ведь вам виднее."
        Ann_12 "Виднее, конечно. Но без Эрика я даже не знаю... Не уверена... Ничего, если я подумаю об этом в более... комфортной обстановке?"
        Max_01 "Да, мам! Я не буду мешать, расслабляйся." nointeract
        menu:
            "{i}уйти{/i}":
                $ spent_time += 10
                jump .end

    label .end:
        $ spent_time += 10
        jump Waiting


label ann_tv:
    scene BG lounge-tv-00
    $ renpy.show('Ann tv '+pose3_3)
    $ persone_button1 = 'Ann tv '+pose3_3+'ab'
    return


label ann_tv_closer:
    $ var_pose = '00'
    scene tv_talk ann
    return
